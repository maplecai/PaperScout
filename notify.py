"""推送模块：写日报 + 微信(Server酱) + Email。

微信和 Email 推送同一份日报全文（含 Abstract），日报写入 reports/ 归档。
"""
from __future__ import annotations

import logging
import os
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests

log = logging.getLogger("paper-scout")


# ====================================================================
# 日报生成
# ====================================================================
def build_report_md(papers: list[dict], date_str: str, errors: list[str] | None = None,
                    stats: str = "") -> str:
    lines = [
        f"# Paper Scout 日报 {date_str}",
        "",
        f"共筛选出 **{len(papers)}** 篇推荐论文。",
    ]
    if stats:
        lines.append(f"📊 {stats}")
    if errors:
        lines.append("")
        lines.append(f"> ⚠️ 抓取异常: {'; '.join(errors)}，今日日报可能不全")
    lines.append("")

    for i, p in enumerate(papers, 1):
        r = p.get("_rank", {})
        s = p.get("_summary", {})
        lines.append(f"## {i}. {p.get('title','')}")
        lines.append("")
        if p.get("journal"):
            lines.append(f"- **期刊**: {p['journal']}")
        lines.append(f"- **作者**: {_authors(p)}")
        if p.get("corr_affiliation"):
            lines.append(f"- **机构**: {p.get('corr_author','') or '（未标注）'} @ {p['corr_affiliation']}")
        lines.append(f"- **日期**: {p.get('date','')}")
        lines.append(f"- **ID**: {_id_str(p)}")
        if r.get("why_relevant"):
            lines.append(f"- **一句话推荐**: {r['why_relevant']}")
        if s.get("core_method"):
            lines.append(f"- **方法**: {s['core_method']}")
        if s.get("main_finding"):
            lines.append(f"- **主要发现**: {s['main_finding']}")
        if s.get("inspiration"):
            lines.append(f"- **对我的启发**: {s['inspiration']}")
        lines.append("")
        if p.get("abstract"):
            lines.append(f"<details><summary>Abstract</summary>\n\n{p['abstract']}\n\n</details>")
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


def _post_wechat(title: str, body: str) -> bool:
    key = os.environ.get("SC_SENDKEY", "").strip()
    if not key:
        log.warning("未配置 SC_SENDKEY，跳过微信推送")
        return False
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
        return True
    except Exception as e:
        log.error("微信推送失败: %s", e)
        return False


def send_empty_notice(date_str: str, reason: str, no_push: bool = False) -> bool:
    """无推荐也发一条，让用户知道程序跑了、只是今天没有货。
    no_push（检索阶段）时不推送，写入空日报 JSON，由推送阶段（--test-notify）发送。"""
    if no_push:
        write_report_json([], date_str)
        log.info("空日：已写入空日报标记，待推送阶段发送")
        return False
    body = f"### {date_str}\n\n今日没有符合标准的论文，未生成日报。\n\n> {reason}"
    ok = _post_wechat(f"📄 Paper Scout 日报 {date_str} · 今日无推荐", body)
    if ok:
        log.info("空日通知推送成功")
    return ok


def send_wechat(md: str, date_str: str, n_papers: int, no_push: bool = False) -> bool:
    """微信推送与 Email 完全相同的一份日报全文（含 Abstract）。"""
    if n_papers <= 0:
        log.info("无推荐论文，跳过微信推送")
        return False

    body = md
    if len(body) > SC_MAX_DESP:
        body = body[:SC_MAX_DESP] + "\n\n…（内容过长已截断，完整版见 Email / reports/）"

    if no_push:
        log.info("微信推送内容已生成，跳过推送")
        return False
    if _post_wechat(f"📄 Paper Scout 日报 {date_str} · {n_papers} 篇", body):
        log.info("微信推送成功 (%d 篇)", n_papers)
        return True
    return False


# ====================================================================
# Email (SMTP)
# ====================================================================
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
