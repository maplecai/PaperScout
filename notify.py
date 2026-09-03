"""推送模块：写日报 + 微信(Server酱) + Email。

- 微信发简版 Top N
- Email 发完整日报
- 日报始终写入 reports/ 作为归档
"""
from __future__ import annotations

import logging
import os
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

import requests

log = logging.getLogger("paper-scout")


# ====================================================================
# 日报生成
# ====================================================================
def build_report_md(papers: list[dict], date_str: str, errors: list[str] | None = None) -> str:
    lines = [
        f"# Paper Watch 日报 — {date_str}",
        "",
        f"共筛选出 **{len(papers)}** 篇推荐论文。",
        "",
    ]
    if errors:
        lines.append(f"> ⚠️ 抓取异常（已跳过不影响整体）: {'; '.join(errors)}")
        lines.append("")

    for i, p in enumerate(papers, 1):
        r = p.get("_rank", {})
        s = p.get("_summary", {})
        ids = _id_str(p)
        lines.append(f"## {i}. [{r.get('priority','')}] {p.get('title','')}")
        lines.append("")
        lines.append(f"- **作者**: {_authors(p)}")
        lines.append(f"- **来源**: {p.get('source','')}  |  **日期**: {p.get('date','')}")
        lines.append(f"- **ID**: {ids}")
        lines.append(f"- **相关性分数**: {r.get('relevance_score','')} / 10  |  **优先级**: {r.get('priority','')}  |  **值得精读**: {'是' if r.get('worth_reading') else '否'}")
        lines.append(f"- **为什么相关**: {r.get('why_relevant','')}")
        lines.append(f"- **对我而言的新意**: {r.get('novelty_for_me','')}")
        lines.append("")
        lines.append(f"- **核心方法**: {s.get('core_method','')}")
        lines.append(f"- **主要发现**: {s.get('main_finding','')}")
        lines.append(f"- **对我研究的启发**: {s.get('inspiration','')}")
        lines.append("")
        if p.get("abstract"):
            lines.append(f"<details><summary>Abstract (原文)</summary>\n\n{p['abstract']}\n\n</details>")
            lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def _id_str(p: dict) -> str:
    parts = []
    if p.get("doi"):
        parts.append(f"DOI: {p['doi']}")
    if p.get("pmid"):
        parts.append(f"PMID: {p['pmid']}")
    if p.get("arxiv_id"):
        parts.append(f"arXiv: {p['arxiv_id']}")
    if p.get("url"):
        parts.append(f"URL: {p['url']}")
    return "  |  ".join(parts) if parts else ""


def _authors(p: dict) -> str:
    a = p.get("authors", [])
    if not a:
        return ""
    if len(a) <= 3:
        return ", ".join(a)
    return f"{a[0]}, {a[1]}, {a[2]} et al. ({len(a)} authors)"


def write_report(md: str, date_str: str, reports_dir: str = "reports") -> str:
    os.makedirs(reports_dir, exist_ok=True)
    path = os.path.join(reports_dir, f"paper_watch_{date_str}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(md)
    log.info("日报已写入 %s", path)
    return path


def write_report_json(papers: list[dict], date_str: str, reports_dir: str = "reports") -> str:
    """把入选论文的结构化数据存成 sidecar JSON。
    用途：--test-notify 可直接复用，无需重跑 LLM。不存 abstract 以控制文件大小。"""
    import json

    os.makedirs(reports_dir, exist_ok=True)
    path = os.path.join(reports_dir, f"paper_watch_{date_str}.json")
    slim = []
    for p in papers:
        slim.append({k: v for k, v in p.items() if k not in ("abstract", "_kw_score")})
    with open(path, "w", encoding="utf-8") as f:
        json.dump(slim, f, ensure_ascii=False, indent=1)
    return path


def load_latest_report(reports_dir: str = "reports") -> tuple[list[dict], str, str] | None:
    """读最近一份日报（json + md），供 --test-notify 用。返回 (papers, md, date_str)。"""
    import glob
    import json

    jsons = sorted(glob.glob(os.path.join(reports_dir, "paper_watch_*.json")))
    if not jsons:
        log.error("reports/ 下没有找到任何 paper_watch_*.json，先跑一次 main.py")
        return None
    jpath = jsons[-1]
    date_str = os.path.basename(jpath)[len("paper_watch_"):-len(".json")]
    with open(jpath, encoding="utf-8") as f:
        papers = json.load(f)
    mpath = jpath[: -len(".json")] + ".md"
    md = ""
    if os.path.exists(mpath):
        with open(mpath, encoding="utf-8") as f:
            md = f.read()
    log.info("载入 %s (%d 篇)", jpath, len(papers))
    return papers, md, date_str


# ====================================================================
# 微信 (Server酱)
# ====================================================================
SC_MAX_DESP = 30000  # Server酱 desp 上限约 32KB，留余量


def send_wechat(papers: list[dict], date_str: str, top_n: int = 5) -> bool:
    key = os.environ.get("SC_SENDKEY", "").strip()
    if not key:
        log.warning("未配置 SC_SENDKEY，跳过微信推送")
        return False
    if not papers:
        log.info("无推荐论文，跳过微信推送")
        return False

    top = papers[:top_n]
    title = f"📄 论文日报 {date_str} · {len(top)} 篇"
    desp = [f"### {date_str} 精选 Top {len(top)}", ""]
    for i, p in enumerate(top, 1):
        r = p.get("_rank", {})
        s = p.get("_summary", {})
        desp.append(f"**{i}. [{r.get('priority','')}·{r.get('relevance_score','')}/10] {p.get('title','')}**")
        desp.append("")
        desp.append(f"- 来源: {p.get('source','')} | {p.get('date','')}")
        if p.get("url"):
            desp.append(f"- [原文链接]({p['url']})")
        if r.get("why_relevant"):
            desp.append(f"- **相关**: {r['why_relevant']}")
        if s.get("core_method"):
            desp.append(f"- **方法**: {s['core_method']}")
        if s.get("main_finding"):
            desp.append(f"- **发现**: {s['main_finding']}")
        if s.get("inspiration"):
            desp.append(f"- **启发**: {s['inspiration']}")
        desp.append("")
        desp.append("---")
        desp.append("")
    body = "\n".join(desp)
    if len(body) > SC_MAX_DESP:
        body = body[:SC_MAX_DESP] + "\n\n…（内容过长已截断，完整版见 Email / reports/）"

    # Server酱³ 的 sendkey 形如 sctp<数字>t<随机串>，走独立域名
    m = re.match(r"^sctp(\d+)t", key)
    url = (
        f"https://{m.group(1)}.push.ft07.com/send/{key}.send"
        if m else f"https://sctapi.ftqq.com/{key}.send"
    )

    try:
        r = requests.post(url, data={"title": title, "desp": body}, timeout=30)
        r.raise_for_status()
        try:
            data = r.json()
        except Exception:
            log.error("微信推送返回非 JSON: %s", r.text[:200])
            return False
        # Server酱 成功: code == 0；失败会带 message
        if data.get("code") not in (0, None):
            log.error("微信推送被拒: %s", str(data)[:300])
            return False
        log.info("微信推送成功 (%d 篇)", len(top))
        return True
    except Exception as e:
        log.error("微信推送失败: %s", e)
        return False


# ====================================================================
# Email (SMTP)
# ====================================================================
def send_email(report_md: str, date_str: str, n_papers: int) -> bool:
    host = os.environ.get("SMTP_HOST", "")
    port = int(os.environ.get("SMTP_PORT", "465"))
    user = os.environ.get("SMTP_USER", "")
    password = os.environ.get("SMTP_PASSWORD", "")
    to = os.environ.get("EMAIL_TO", "")
    if not (host and user and password and to):
        log.warning("未配置 SMTP_* / EMAIL_TO，跳过 Email 推送")
        return False

    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"📄 Paper Watch 日报 {date_str} · {n_papers} 篇推荐"
    msg["From"] = user
    msg["To"] = to

    # 简单 markdown -> 文本 + 近似 html
    import html as _html
    text = report_md
    # 极简 markdown 转 html（段落 + 标题 + 列表）
    htmllines = []
    in_list = False
    for ln in report_md.splitlines():
        if ln.startswith("# "):
            htmllines.append(f"<h1>{_html.escape(ln[2:])}</h1>")
        elif ln.startswith("## "):
            htmllines.append(f"<h2>{_html.escape(ln[3:])}</h2>")
        elif ln.startswith("- "):
            htmllines.append(f"<li>{_html.escape(ln[2:])}</li>")
            in_list = True
        elif ln.strip() == "":
            if in_list:
                htmllines.append("</ul>")
                in_list = False
            htmllines.append("<br>")
        else:
            if in_list:
                htmllines.append("</ul>")
                in_list = False
            htmllines.append(f"<p>{_html.escape(ln)}</p>")
    if in_list:
        htmllines.append("</ul>")
    html_body = f"<html><body>{''.join(htmllines)}</body></html>"

    msg.attach(MIMEText(text, "plain", "utf-8"))
    msg.attach(MIMEText(html_body, "html", "utf-8"))

    try:
        if port == 465:
            server = smtplib.SMTP_SSL(host, port, timeout=30)
        else:
            server = smtplib.SMTP(host, port, timeout=30)
            server.starttls()
        server.login(user, password)
        server.sendmail(user, to.split(","), msg.as_string())
        server.quit()
        log.info("Email 推送成功 -> %s", to)
        return True
    except Exception as e:
        log.error("Email 推送失败: %s", e)
        return False
