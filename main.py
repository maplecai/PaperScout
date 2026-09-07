#!/usr/bin/env python3
"""PaperScout 主入口。

流程：抓取 -> 去重(含历史去重) -> 关键词粗筛 -> LLM 相关性打分
     -> 选 Top -> 中文总结 -> 写日报 -> 微信/Email 推送 -> 更新 state.json

用法：
  python main.py                 # 正常运行
  python main.py --dry-run       # 只抓取+粗筛，不调 LLM、不推送、不写 state
  python main.py --no-notify     # 跑完整流程但不推送
  python main.py --days 7        # 覆盖回溯天数
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import sys
from datetime import datetime, timedelta

import yaml

# 本地开发：从 .env 加载环境变量（GitHub Actions 走 secrets，无 .env 文件，忽略）
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

import fetch
import rank
import summarize
import notify
from llm import LLMClient

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("paper-scout")

STATE_FILE = "state.json"
STATE_RETENTION_DAYS = 120


# ====================================================================
# 状态管理
# ====================================================================
def load_state(path: str = STATE_FILE) -> dict:
    if not os.path.exists(path):
        return {"seen": {}, "runs": []}
    try:
        with open(path, encoding="utf-8") as f:
            s = json.load(f)
        s.setdefault("seen", {})
        s.setdefault("runs", [])
        return s
    except Exception as e:
        log.error("state.json 读取失败，重新开始: %s", e)
        return {"seen": {}, "runs": []}


def save_state(state: dict, path: str = STATE_FILE) -> None:
    # 清理过期记录
    cutoff = (datetime.utcnow() - timedelta(days=STATE_RETENTION_DAYS)).strftime("%Y-%m-%d")
    state["seen"] = {k: v for k, v in state["seen"].items() if v >= cutoff}
    state["runs"] = state["runs"][-60:]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=1)
    log.info("state.json 已更新 (seen=%d)", len(state["seen"]))


def filter_seen(papers: list[dict], state: dict) -> list[dict]:
    """按 id + doi + pmid + arxiv_id 多键去重，避免重复推荐。"""
    seen = state["seen"]
    out = []
    for p in papers:
        keys = [p["id"]]
        for k in ("doi", "pmid", "arxiv_id"):
            if p.get(k):
                keys.append(f"{k}:{p[k]}")
        if any(k in seen for k in keys):
            continue
        out.append(p)
    log.info("历史去重: %d -> %d", len(papers), len(out))
    return out


def mark_seen(papers: list[dict], state: dict, date_str: str) -> None:
    """标记已处理。LLM 调用失败的论文（_rank._failed）不标记，
    以便下次运行重新评估，避免因网络问题永久漏掉论文。"""
    skipped = 0
    for p in papers:
        if p.get("_rank", {}).get("_failed"):
            skipped += 1
            continue
        state["seen"][p["id"]] = date_str
        for k in ("doi", "pmid", "arxiv_id"):
            if p.get(k):
                state["seen"][f"{k}:{p[k]}"] = date_str
    if skipped:
        log.warning("%d 篇因 LLM 失败未标记 seen，下次运行会重新评估", skipped)


# ====================================================================
# 主流程
# ====================================================================
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="config.yaml")
    ap.add_argument("--dry-run", action="store_true", help="不调 LLM、不推送、不写 state")
    ap.add_argument("--no-notify", action="store_true", help="不推送")
    ap.add_argument("--test-notify", action="store_true",
                    help="跳过抓取/打分，用 reports/ 里最近一份日报测试推送（省 token，可反复跑）")
    ap.add_argument("--days", type=int, default=None, help="覆盖回溯天数")
    ap.add_argument("--date", help="回填指定日期 (YYYY-MM-DD)：只处理该日发表的论文，日报/state 也记为该日期")
    ap.add_argument("--end-date", help="窗口结束边界（不含，YYYY-MM-DD）：检索 [end-72h, end)，日报记为该日期。"
                                        "定时任务用它把窗口锚定到 UTC 0 点，不受 cron 延迟影响")
    args = ap.parse_args()

    with open(args.config, encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    # --test-notify: 复用已有日报测试推送，不抓取不调 LLM
    if args.test_notify:
        loaded = notify.load_latest_report()
        if not loaded:
            return 1
        papers, md, date_str = loaded
        if not papers:
            # 检索阶段写入的空日报标记：照发空日通知
            ok = notify.send_empty_notice(date_str, "今日无符合标准的论文")
            log.info("空日通知推送: %s", "成功" if ok else "失败/未配置")
            return 0 if ok else 1
        ok_wx = notify.send_wechat(md, date_str, len(papers))
        ok_mail = notify.send_email(md, date_str, len(papers))
        log.info("测试推送结果: 微信=%s Email=%s", "成功" if ok_wx else "失败/未配置",
                 "成功" if ok_mail else "失败/未配置")
        return 0 if (ok_wx or ok_mail) else 1

    profile = cfg.get("profile", {})
    # tracked_authors 放到 profile 里给粗筛用（但不进 LLM prompt，太长）
    profile_for_prefilter = dict(profile)
    profile_for_prefilter["tracked_authors"] = cfg.get("tracked_authors", [])

    fetch_cfg = dict(cfg.get("fetch", {}))
    fetch_cfg["_profile"] = profile
    date_str = args.date or args.end_date or datetime.utcnow().strftime("%Y-%m-%d")
    # --date 回填：窗口只覆盖目标日期（各源加索引延迟缓冲）
    # --end-date：窗口锚定为 [end-72h, end)，即不含 end 当天；lookback-1 天、fetch 端点取前一天
    if args.date and args.days is None:
        days = 1
    elif args.end_date and args.days is None:
        days = fetch_cfg.get("lookback_days", 2) - 1
    else:
        days = args.days if args.days is not None else fetch_cfg.get("lookback_days", 2)
    fetch_end = args.date
    if args.end_date:
        fetch_end = (datetime.strptime(args.end_date, "%Y-%m-%d") - timedelta(days=1)).strftime("%Y-%m-%d")

    # 1. 抓取
    papers, errors = fetch.fetch_all(fetch_cfg, days, end_date=fetch_end, backfill=bool(args.date))
    from collections import Counter
    src_counts = Counter(p["source"] for p in papers)
    src_str = "/".join(f"{k} {v}" for k, v in sorted(src_counts.items()))
    if args.date:
        n0 = len(papers)
        papers = [p for p in papers if p.get("date") == args.date]
        log.info("回填 %s: %d -> %d 篇 (按发表日期过滤)", args.date, n0, len(papers))
    if not papers:
        log.warning("没有抓到任何论文")
        reason = "各源均未抓到论文"
        if errors:
            reason += f": {'; '.join(errors)}"
        notify.send_empty_notice(date_str, reason, no_push=args.no_notify)
        return 0

    # 2. 历史去重
    state = load_state()
    papers = filter_seen(papers, state)
    if not papers:
        log.info("全部已推荐过，无新论文")
        return 0

    # 3. 关键词粗筛
    rank_cfg = cfg.get("ranking", {})
    candidates = rank.keyword_prefilter(
        papers, profile_for_prefilter,
        threshold=rank_cfg.get("keyword_prefilter_threshold", 0.08),
    )
    # 按粗筛分排序，控制送 LLM 的数量上限（成本兜底）
    candidates.sort(key=lambda p: p["_kw_score"], reverse=True)
    llm_cap = rank_cfg.get("max_llm_candidates", 120)
    if len(candidates) > llm_cap:
        log.info("候选 %d 超过 LLM 上限 %d，截断", len(candidates), llm_cap)
        candidates = candidates[:llm_cap]

    if args.dry_run:
        log.info("=== DRY RUN: 粗筛 Top 20 ===")
        for p in candidates[:20]:
            log.info("  [%.2f] %s | %s", p["_kw_score"], p["source"], p["title"][:90])
        log.info("总候选数: %d", len(candidates))
        return 0

    if not candidates:
        log.info("粗筛后无候选，保存空日通知")
        notify.send_empty_notice(date_str, "关键词粗筛后 0 篇候选", no_push=args.no_notify)
        return 0

    # 4. LLM 相关性打分
    llm = LLMClient(cfg)
    if not llm.enabled:
        log.error("LLM 未配置，无法做相关性筛选。请设置 OPENAI_BASE_URL / OPENAI_API_KEY / OPENAI_MODEL")
        return 1
    ranked = rank.llm_rank(candidates, profile, llm, batch_size=rank_cfg.get("batch_size", 12))

    # 5. 选 Top
    selected = rank.select_top(ranked, rank_cfg.get("selection", {}))
    if not selected:
        log.info("今日无符合标准的论文，保存空日通知（宁缺毋滥）")
        notify.send_empty_notice(date_str, f"粗筛候选 {len(candidates)} 篇，LLM 筛选后 0 篇达到标准",
                                 no_push=args.no_notify)
        state["runs"].append({"date": date_str, "candidates": len(candidates), "selected": 0})
        mark_seen(ranked, state, date_str)
        save_state(state)
        return 0

    # 6. 中文总结
    summarize.summarize_papers(selected, llm)

    # 7. 写日报（同一份 md 给微信/Email/reports 归档，json 给 --test-notify 复用）
    stats = f"抓取 {src_str} → 粗筛 {len(candidates)} 篇 → LLM 选中 {len(selected)} 篇"
    md = notify.build_report_md(selected, date_str, errors, stats=stats)
    notify.write_report(md, date_str)
    notify.write_report_json(selected, date_str)

    # 8. 更新 state：所有被 LLM 评过的都标记 seen（避免明天重复评分）。
    # 必须在推送之前 —— 推送崩了也不能丢 seen 记录，否则隔天会重复推荐
    mark_seen(ranked, state, date_str)
    state["runs"].append({
        "date": date_str,
        "fetched": len(papers),
        "candidates": len(candidates),
        "selected": len(selected),
        "errors": errors,
    })
    save_state(state)

    # 9. 推送：微信与 Email 用同一份 md
    notify.send_wechat(md, date_str, len(selected), no_push=args.no_notify)
    if not args.no_notify:
        notify.send_email(md, date_str, len(selected))

    log.info("完成：推荐 %d 篇", len(selected))
    return 0


if __name__ == "__main__":
    sys.exit(main())
