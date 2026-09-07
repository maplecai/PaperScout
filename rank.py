"""相关性筛选模块 —— 整个项目最核心的部分。

两阶段：
1. keyword_prefilter: 用关键词/作者名打一个 0-1 粗筛分，砍掉大量明显无关论文，省 LLM token。
2. llm_rank: 把剩下的论文分批送 LLM，输入 research profile + title + abstract，
   输出结构化 {relevance_score, priority, why_relevant, novelty_for_me, worth_reading}。
3. select_top: 动态阈值 + 上限，选出 Top 5-10。
"""
from __future__ import annotations

import json
import logging
import re

from llm import LLMClient

log = logging.getLogger("paper-scout")


# ====================================================================
# 阶段 1：关键词粗筛
# ====================================================================
def keyword_prefilter(papers: list[dict], profile: dict, threshold: float = 0.08) -> list[dict]:
    """给每篇打 _kw_score (0-1)。低于 threshold 的丢弃。
    信号：
    - title/abstract 命中 core/preferred topic → 高分
    - title/abstract 命中 important_method → 中分
    - 作者命中 tracked_authors → 强加分
    - 命中 negative_topic → 降分
    """
    core = [t.lower() for t in profile.get("core_topics", [])]
    interests = [t.lower() for t in profile.get("research_interests", [])]
    # active_projects 的 keywords 也作为强信号
    proj_kw = []
    for proj in profile.get("active_projects", []):
        proj_kw.extend(proj.get("keywords", []))
    proj_kw = [k.lower() for k in proj_kw]
    negatives = [t.lower() for t in profile.get("negative_topics", [])]
    # 泛词：命中也不给高分（太宽泛，几乎每篇 ML 文章都有）
    broad = {"machine learning", "computational genomics"}

    # 把 interests + proj_kw 拆成单个有意义的词，用于词级匹配（提升召回）
    stop = {"model", "learning", "method", "methods", "specific", "design",
            "activity", "prediction", "foundation", "sequence", "virtual",
            "cell", "single", "response", "modeling", "based", "data"}
    tokens = set()
    for t in interests + proj_kw:
        for w in re.findall(r"[a-z]+", t):
            if len(w) > 4 and w not in stop:
                tokens.add(w)
    # 额外补充领域核心词
    tokens.update({"enhancer", "chromatin", "epigenetic", "epigenome",
                   "transcription", "accessibility", "genomics", "regulatory",
                   "promoter", "perturbation", "embedding", "pretrained"})

    kept = []
    for p in papers:
        text = (p.get("title", "") + " " + p.get("abstract", "")).lower()
        authors = " ".join(p.get("authors", [])).lower()
        score = 0.0

        # 作者命中（强信号）
        for a in profile.get("tracked_authors", []):
            al = a.lower()
            # 去掉括号里的中文/别名
            al = re.sub(r"\(.*?\)", "", al).strip()
            if al and al in authors:
                score += 0.4
                break  # 命中一次即可

        # core topics —— 泛词只给 0.05，具体词给 0.15
        for t in core:
            if t and t in text:
                score += 0.05 if t in broad else 0.15
        # active_projects keywords —— 最高分（0.25，直接命中当前项目）
        for t in proj_kw:
            if t and t in text:
                score += 0.25
        # research_interests —— 中分
        for t in interests:
            if t and t in text:
                score += 0.2
        # 词级匹配（低分 0.08，提升召回）
        for w in tokens:
            if w in text:
                score += 0.08

        # negative 降分
        for t in negatives:
            if t and t in text:
                score -= 0.3

        # 没有计算方法信号的纯生物文章：检测是否有 ML/计算关键词
        comp_markers = ["model", "learning", "algorithm", "neural", "embedding",
                        "prediction", "computational", "deep", "transformer",
                        "regression", "bayesian", "graph", "representation"]
        if not any(m in text for m in comp_markers):
            score -= 0.2

        score = max(0.0, min(1.0, score))
        p["_kw_score"] = round(score, 3)
        if score >= threshold:
            kept.append(p)

    log.info("关键词粗筛: %d -> %d (阈值 %.2f)", len(papers), len(kept), threshold)
    return kept


# ====================================================================
# 阶段 2：LLM 批量打分
# ====================================================================
SYSTEM_PROMPT = """你是一位资深的计算基因组学/机器学习研究者，正在帮另一位研究者做个性化论文筛选。

你是严格的、宁缺毋滥的。绝大多数论文应当被排除。只有真正与下方 research profile 相关的才给高分。

## 我的 Research Profile
{profile_json}

## 优先级定义（严格遵守）
- P0: 和 active_projects 中列出的当前研究问题直接相关。极少数。
- P1: 方法、模型、数据集或思路与 research_interests 高度相关。
- P2: 间接相关，但可能对我的研究有启发。
- exclude: 基本不值得关注，包括：没有计算方法的纯生物文章、纯临床、纯理论证明、不切题的综述。

## 评分
relevance_score: 0-10 的整数。10 = 直接命中我的当前研究问题；5 = 间接相关有启发；<5 = 基本无关。

## 判断要点
- 模型架构本身（CNN/Transformer/diffusion）不是重点，关键看它解决的是不是 sequence-to-function / 基因组功能预测 / 增强子 / 表观遗传这类问题。
- 纯实验生物学但用了计算模型做分析的，给 P2 而非 P0/P1。
- 综述只在高度切题时给 P2，否则 exclude。
"""


def _batch_user_prompt(batch: list[dict]) -> str:
    items = []
    for i, p in enumerate(batch):
        items.append({
            "index": i,
            "title": p.get("title", ""),
            "abstract": p.get("abstract", "")[:1500],  # 截断防止 token 爆炸
            "authors": p.get("authors", [])[:5],
        })
    return (
        "下面是候选论文列表。请对每一篇输出一个 JSON 对象，字段：\n"
        "relevance_score(0-10整数), priority(P0/P1/P2/exclude), "
        "why_relevant(一句话中文，说明与我研究的具体关联；exclude 时写原因), "
        "novelty_for_me(一句话中文，对我而言的新意所在), worth_reading(bool)。\n"
        "严格输出 JSON 数组，数组元素顺序与输入 index 对应，不要输出任何其它内容。\n\n"
        f"候选论文:\n{json.dumps(items, ensure_ascii=False, indent=1)}"
    )


def llm_rank(papers: list[dict], profile: dict, llm: LLMClient, batch_size: int = 12) -> list[dict]:
    """批量送 LLM 打分。把结果写回 paper 的 _rank 字段。"""
    if not papers:
        return []

    system = SYSTEM_PROMPT.format(profile_json=json.dumps(profile, ensure_ascii=False, indent=1))

    for start in range(0, len(papers), batch_size):
        batch = papers[start : start + batch_size]
        try:
            result = llm.chat_json(system, _batch_user_prompt(batch), temperature=0.15)
        except Exception as e:
            log.error("LLM 批次 %d-%d 异常: %s", start, start + len(batch), e)
            result = None

        if not isinstance(result, list):
            log.error("LLM 返回非数组，批次 %d。原始: %s", start, str(result)[:300])
            # 给该批所有论文一个 exclude 占位，避免丢失
            for p in batch:
                p["_rank"] = _placeholder_rank(p)
            continue

        # 按 index 对齐
        rank_by_idx = {item.get("index", i): item for i, item in enumerate(result)}
        for i, p in enumerate(batch):
            item = rank_by_idx.get(i)
            if not isinstance(item, dict):
                item = _placeholder_rank(p)
            p["_rank"] = _normalize_rank(item, p)

    # 排序：按 relevance_score 降序
    papers.sort(key=lambda p: p["_rank"]["relevance_score"], reverse=True)
    return papers


def _normalize_rank(item: dict, paper: dict) -> dict:
    score = item.get("relevance_score")
    try:
        score = int(score)
    except Exception:
        score = 0
    score = max(0, min(10, score))
    priority = str(item.get("priority", "exclude")).upper()
    if priority not in ("P0", "P1", "P2", "EXCLUDE"):
        priority = "EXCLUDE"
    return {
        "relevance_score": score,
        "priority": priority,
        "why_relevant": str(item.get("why_relevant", "")),
        "novelty_for_me": str(item.get("novelty_for_me", "")),
        "worth_reading": bool(item.get("worth_reading", False)),
    }


def _placeholder_rank(paper: dict) -> dict:
    """LLM 调用失败时的占位。_failed=True 标记该篇未被真正评估过，
    main.py 不会把它标记为 seen，下次运行会重新评估。"""
    return {
        "relevance_score": 0,
        "priority": "EXCLUDE",
        "why_relevant": "（LLM 调用失败，未评估）",
        "novelty_for_me": "",
        "worth_reading": False,
        "_failed": True,
    }


# ====================================================================
# 阶段 3：选择 Top
# ====================================================================
def select_top(papers: list[dict], selection_cfg: dict) -> list[dict]:
    """动态阈值 + 上限选择。"""
    min_score = selection_cfg.get("min_score", 5)
    accept = set(selection_cfg.get("accept_priorities", ["P0", "P1", "P2"]))
    max_n = selection_cfg.get("max_papers", 10)
    selected = []
    # 不变量：_rank 由 _normalize_rank/_placeholder_rank 构造，键恒齐全
    for p in papers:
        r = p["_rank"]
        pri = r["priority"]
        score = r["relevance_score"]
        # exclude 直接跳
        if pri == "EXCLUDE":
            continue
        # 满足 priority 或 score 阈值
        if pri in accept or score >= min_score:
            if r["worth_reading"] or score >= min_score or pri in ("P0", "P1"):
                selected.append(p)
        if len(selected) >= max_n:
            break

    # 宁缺毋滥：不足 min_papers 也不硬凑（min_n 不参与选择逻辑）
    log.info("最终选中 %d 篇 (上限 %d)", len(selected), max_n)
    return selected
