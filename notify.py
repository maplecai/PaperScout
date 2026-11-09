"""推送模块：写日报 + Email。

Email 发送日报全文（含 Abstract），日报写入 reports/ 归档。
"""
from __future__ import annotations

import html
import logging
import os
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from urllib.parse import quote

log = logging.getLogger("paper-scout")


# ====================================================================
# 日报生成
# ====================================================================
def build_report_md(papers: list[dict], date_str: str, errors: list[str] | None = None,
                    stats: str = "") -> str:
    lines = [f"# Paper Scout 日报 {date_str}", "", f"共推荐 **{len(papers)}** 篇论文。", ""]
    for i, p in enumerate(papers, 1):
        r, summary = p.get("_rank", {}), p.get("_summary", {})
        source = p.get("journal") or p.get("source", "")
        kind = "预印本" if p.get("source") in ("arxiv", "biorxiv") else "期刊文献"
        relation = summary.get("relevance_type", "")
        lines.extend([f"## {i}. {p.get('title', '')}", "",
                      f"{source} · {kind} · {p.get('date', '')} · 相关性 {r.get('relevance_score', '未评分')}/10", ""])
        if relation:
            lines.extend([f"**研究关联：{relation}**", ""])
        for label, value in (
            ("为什么值得看", r.get("why_relevant")),
            ("任务与验证范围", summary.get("task_scope")),
            ("核心方法", summary.get("core_method")),
            ("主要发现与证据", summary.get("main_finding")),
            ("可借鉴点（研究建议）", summary.get("inspiration")),
            ("迁移边界", summary.get("applicability")),
            ("阅读时核实", summary.get("reading_question")),
        ):
            if value:
                lines.append(f"- **{label}**：{value}")
        if not summary.get("core_method"):
            lines.append("- **中文笔记**：生成未成功，请参考下方原始摘要。")
        links = []
        if p.get("url", "").startswith(("https://", "http://")):
            links.append(f"[原文]({quote(p['url'], safe=':/?=&%#')})")
        if p.get("doi"):
            links.append(f"[DOI](https://doi.org/{quote(p['doi'], safe='/')})")
        lines.extend(["", " · ".join(links), ""])
        resources = list(dict.fromkeys(
            url.rstrip(".,;:)") for url in re.findall(r"https?://[^\s<>]+", p.get("abstract", ""))
        ))
        if resources:
            lines.append("摘要提供的链接（未核验可用性）：" + " · ".join(
                f"[资源 {n}]({quote(url, safe=':/?=&%#')})" for n, url in enumerate(resources, 1)
            ))
            lines.append("")
        lines.append(f"作者：{_authors(p)}")
        if p.get("corr_author"):
            label = "末位带机构信息的作者" if p.get("source") == "arxiv" else "来源标注的末位/通讯作者"
            lines.append(f"{label}：{p['corr_author']}")
        if p.get("corr_affiliation"):
            affiliation = re.sub(r"[\w.+-]+@[\w.-]+", "", p["corr_affiliation"]).strip(" .,")
            lines.append(f"机构：{affiliation}")
        else:
            lines.append("机构：当前 API 未提供机构信息")
        lines.extend(["", "### 英文摘要", "", p.get("abstract") or "归档未保存摘要，请打开原文查看。", "", "---", ""])
    lines.extend(["中文笔记基于标题和摘要生成，未核验全文；研究建议不代表论文已验证的结论。相关性分数不是论文质量评分。", ""])
    if stats:
        lines.extend([f"检索统计：{stats}", ""])
    if errors:
        lines.append(f"> 抓取异常：{'; '.join(errors)}。本期可能不完整。")
    return "\n".join(lines)


def _authors(p: dict) -> str:
    a = p.get("authors", [])
    if not a:
        return ""
    if len(a) <= 8:
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
    用途：--test-notify 可直接复用，无需重跑 LLM。保留 abstract，便于重排版和核对摘要依据。"""
    import json

    os.makedirs(reports_dir, exist_ok=True)
    path = os.path.join(reports_dir, f"paper_watch_{date_str}.json")
    slim = []
    for p in papers:
        slim.append({k: v for k, v in p.items() if k != "_kw_score"})
    with open(path, "w", encoding="utf-8") as f:
        json.dump(slim, f, ensure_ascii=False, indent=1)
    return path


def load_report(date_str: str | None = None, reports_dir: str = "reports") -> tuple[list[dict], str, str] | None:
    """读指定日期或最新日报（json + md），供 --test-notify 用。"""
    import glob
    import json

    pattern = f"paper_watch_{date_str}.json" if date_str else "paper_watch_*.json"
    jsons = sorted(glob.glob(os.path.join(reports_dir, pattern)))
    if not jsons:
        log.error("%s 下没有找到 %s，先生成日报", reports_dir, pattern)
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


def send_empty_notice(date_str: str, reason: str, no_push: bool = False) -> bool:
    """归档空日报；正常运行时也通过邮件说明没有推荐的原因。"""
    md = build_report_md([], date_str) + f"\n今日没有符合标准的论文。\n\n> {reason}\n"
    write_report(md, date_str)
    write_report_json([], date_str)
    if no_push:
        return False
    return send_email(md, date_str, 0)


# ====================================================================
# Email (SMTP)
# ====================================================================
def render_report_html(markdown: str) -> str:
    """渲染日报使用的 Markdown 子集；原始 HTML 作为文本转义。"""
    blocks = []
    in_list = False
    for line in markdown.splitlines():
        if in_list and not line.startswith("- "):
            blocks.append("</ul>")
            in_list = False
        if not line.strip():
            continue
        escaped = html.escape(line)
        escaped = re.sub(r"\[([^]\n]+)\]\((https?://[^\s)]+)\)",
                         r'<a href="\2" style="color:#2463a5;text-decoration:underline">\1</a>', escaped)
        escaped = re.sub(r"\*\*([^*\n]+)\*\*", r"<strong>\1</strong>", escaped)
        if line.startswith("- "):
            if not in_list:
                blocks.append('<ul style="padding-left:22px">')
                in_list = True
            blocks.append(f'<li style="margin:8px 0">{escaped[2:]}</li>')
        elif line.startswith("### "):
            blocks.append(f'<h3 style="font-size:15px;color:#666">{escaped[4:]}</h3>')
        elif line.startswith("## "):
            blocks.append(f'<h2 style="font-size:19px;margin-top:28px">{escaped[3:]}</h2>')
        elif line.startswith("# "):
            blocks.append(f'<h1 style="font-size:23px">{escaped[2:]}</h1>')
        elif line == "---":
            blocks.append('<hr style="border:0;border-top:1px solid #ddd;margin:28px 0">')
        else:
            blocks.append(f'<p style="margin:10px 0">{escaped}</p>')
    if in_list:
        blocks.append("</ul>")
    return ('<!doctype html><html><head><meta charset="utf-8"></head>'
            '<body style="margin:0;background:#fff;color:#222">'
            '<div style="max-width:760px;margin:auto;padding:24px;font-family:Arial,sans-serif;'
            'font-size:15px;line-height:1.7;overflow-wrap:anywhere">'
            + "".join(blocks) + '</div></body></html>')


def send_email(report_md: str, date_str: str, n_papers: int) -> bool:
    host = os.environ.get("SMTP_HOST", "")
    port = int(os.environ.get("SMTP_PORT") or 465)  # 空串（secrets 设了但值为空）也回退默认
    user = os.environ.get("SMTP_USER", "")
    password = os.environ.get("SMTP_PASSWORD", "")
    to = os.environ.get("EMAIL_TO", "")
    if not (host and user and password and to):
        log.warning("未配置 SMTP_* / EMAIL_TO，跳过 Email 推送")
        return False

    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"📄 Paper Scout 日报 {date_str} · {n_papers} 篇推荐"
    msg["From"] = user
    msg["To"] = to

    msg.attach(MIMEText(report_md, "plain", "utf-8"))
    msg.attach(MIMEText(render_report_html(report_md), "html", "utf-8"))

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
