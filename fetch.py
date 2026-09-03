"""论文抓取模块。

三个数据源各自独立，单个失败不影响其它。统一输出 Paper dict：
{
  "id": "pubmed:12345678",          # 去重主键 source:raw_id
  "source": "pubmed|arxiv|biorxiv",
  "raw_id": "12345678",
  "title": str,
  "abstract": str,
  "authors": [str],
  "date": "YYYY-MM-DD",
  "url": str,
  "doi": str | "",
  "pmid": str | "",
  "arxiv_id": str | "",
}
"""
from __future__ import annotations

import logging
import time
import urllib.parse
from datetime import datetime, timedelta

import requests

log = logging.getLogger("paper-scout")

PUBMED_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
ARXIV_BASE = "http://export.arxiv.org/api/query"
BIORXIV_BASE = "https://api.biorxiv.org/details/biorxiv"


def _date_range(days: int) -> tuple[str, str, str]:
    today = datetime.utcnow().date()
    start = today - timedelta(days=days)
    # arXiv/bioRxiv 用 YYYY-MM-DD
    return start.strftime("%Y-%m-%d"), today.strftime("%Y-%m-%d"), today.strftime("%Y-%m-%d")


# ====================================================================
# PubMed (NCBI E-utilities)
# ====================================================================
def fetch_pubmed(cfg: dict, days: int) -> list[dict]:
    src_cfg = cfg.get("sources", {}).get("pubmed", {})
    if not src_cfg.get("enabled", True):
        return []
    api_key = os_get("NCBI_API_KEY")
    start, end, _ = _date_range(days)

    # 构造查询：用户 query > search_terms > 自动从 preferred_topics 构造
    # 注意：不要把 "machine learning" / "computational genomics" 这种泛词当搜索词，
    # 否则 PubMed 会返回海量无关临床 ML 论文。只用基因组学专用词。
    query = src_cfg.get("query", "").strip()
    if not query:
        prof = cfg.get("_profile", {})
        terms = prof.get("preferred_topics", []) + prof.get("important_methods", [])
        # 过滤掉过于宽泛的泛词
        broad = {"machine learning", "computational genomics",
                 "representation learning for biological sequences"}
        terms = [t for t in terms if t.lower() not in broad]
        topic_q = " OR ".join(f'"{t}"' for t in terms) if terms else '"enhancer" OR "epigenetic"'
        query = f'({topic_q}) AND ("{start}"[PDAT] : "{end}"[PDAT])'
    else:
        query = f'({query}) AND ("{start}"[PDAT] : "{end}"[PDAT])'

    params = {
        "db": "pubmed",
        "term": query,
        "retmax": str(src_cfg.get("max_results", 300)),
        "sort": "date",
        "datetype": "pdat",
        "retmode": "json",
    }
    if api_key:
        params["api_key"] = api_key

    try:
        r = requests.get(f"{PUBMED_BASE}/esearch.fcgi", params=params, timeout=30)
        r.raise_for_status()
        ids = r.json().get("esearchresult", {}).get("idlist", [])
    except Exception as e:
        log.error("PubMed esearch 失败: %s", e)
        return []
    if not ids:
        log.info("PubMed: 0 hits")
        return []
    log.info("PubMed: %d hits, efetch...", len(ids))

    # efetch 分批（每批 100）
    papers = []
    for i in range(0, len(ids), 100):
        batch = ids[i : i + 100]
        try:
            r = requests.get(
                f"{PUBMED_BASE}/efetch.fcgi",
                params={
                    "db": "pubmed", "id": ",".join(batch),
                    "rettype": "abstract", "retmode": "xml",
                    **({"api_key": api_key} if api_key else {}),
                },
                timeout=60,
            )
            r.raise_for_status()
            papers.extend(_parse_pubmed_xml(r.text))
        except Exception as e:
            log.error("PubMed efetch 批次失败: %s", e)
        time.sleep(0.3)
    log.info("PubMed: 解析得 %d 篇", len(papers))
    return papers


def _parse_pubmed_xml(xml: str) -> list[dict]:
    import xml.etree.ElementTree as ET

    out = []
    try:
        root = ET.fromstring(xml)
    except Exception as e:
        log.error("PubMed XML 解析失败: %s", e)
        return out
    for art in root.findall(".//PubmedArticle"):
        try:
            # 全部路径都锚定到文章自身，不能用 .// —— 否则会抓到
            # ReferenceList / CommentsCorrections 里参考文献的 PMID/DOI/作者。
            cit = art.find("./MedlineCitation")
            article = cit.find("./Article") if cit is not None else None
            if article is None:
                continue
            pmid = _txt(cit, "./PMID")
            # ArticleTitle 内可能有 <i>/<sup> 等嵌套标签，必须用 itertext 取全文
            title_el = article.find("./ArticleTitle")
            title = "".join(title_el.itertext()) if title_el is not None else ""
            # abstract may have multiple AbstractText sections
            abs_parts = []
            for at in article.findall("./Abstract/AbstractText"):
                label = at.get("Label")
                txt = "".join(at.itertext()).strip()
                if txt:
                    abs_parts.append(f"{label}: {txt}" if label else txt)
            abstract = "\n".join(abs_parts)
            authors = []
            for a in article.findall("./AuthorList/Author"):
                ln = _txt(a, "./LastName")
                fn = _txt(a, "./ForeName")
                if ln:
                    authors.append(f"{fn} {ln}".strip())
            # date：优先 ArticleDate（电子发表日），PubDate 是期刊卷期日期可能超前数月
            adate = article.find("./ArticleDate")
            if adate is not None:
                y = _txt(adate, "./Year")
                m = _txt(adate, "./Month") or "01"
                d = _txt(adate, "./Day") or "01"
            else:
                pd = article.find("./Journal/JournalIssue/PubDate")
                y = _txt(pd, "./Year") if pd is not None else ""
                m = (_txt(pd, "./Month") if pd is not None else "") or "01"
                d = (_txt(pd, "./Day") if pd is not None else "") or "01"
            m_num = _month_to_num(m)
            try:
                d_num = int(d)
            except ValueError:
                d_num = 1
            date = f"{y}-{m_num:02d}-{d_num:02d}" if y else datetime.utcnow().strftime("%Y-%m-%d")
            # DOI：必须限定在文章自身的 ArticleIdList / ELocationID 里。
            # 用 .//ArticleId 会把 ReferenceList 里参考文献的 DOI 也抓进来（严重串号 bug）。
            doi = ""
            for aid in art.findall("./PubmedData/ArticleIdList/ArticleId"):
                if aid.get("IdType") == "doi":
                    doi = (aid.text or "").strip()
                    break
            if not doi:
                for eid in article.findall("./ELocationID"):
                    if eid.get("EIdType") == "doi":
                        doi = (eid.text or "").strip()
                        break
            out.append({
                "id": f"pubmed:{pmid}", "source": "pubmed", "raw_id": pmid,
                "title": _clean(title), "abstract": _clean(abstract),
                "authors": authors, "date": date,
                "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/" if pmid else "",
                "doi": doi.lower(), "pmid": pmid, "arxiv_id": "",
            })
        except Exception as e:
            log.warning("PubMed 单篇解析失败: %s", e)
    return out


# ====================================================================
# arXiv
# ====================================================================
def fetch_arxiv(cfg: dict, days: int) -> list[dict]:
    import xml.etree.ElementTree as ET

    src_cfg = cfg.get("sources", {}).get("arxiv", {})
    if not src_cfg.get("enabled", True):
        return []
    prof = cfg.get("_profile", {})
    cats = src_cfg.get("categories", ["q-bio"])
    cat_q = " OR ".join(f"cat:{c}*" for c in cats)
    # 关键词
    kws = prof.get("preferred_topics", []) + ["foundation model", "language model", "enhancer", "epigenetic"]
    kw_q = " OR ".join(f'abs:"{k}"' for k in kws[:8])
    query = f"({cat_q}) OR ({kw_q})"

    # arXiv 不支持精确日期窗口，用 submittedDate 排序后客户端按日期过滤
    params = {
        "search_query": query,
        "start": "0",
        "max_results": str(src_cfg.get("max_results", 200)),
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    try:
        r = requests.get(ARXIV_BASE, params=params, timeout=60)
        r.raise_for_status()
    except Exception as e:
        log.error("arXiv 失败: %s", e)
        return []
    out = []
    cutoff = datetime.utcnow() - timedelta(days=days)
    try:
        root = ET.fromstring(r.text)
        ns = {"a": "http://www.w3.org/2005/Atom"}
        for e in root.findall("a:entry", ns):
            try:
                raw_id = e.find("a:id", ns).text.strip().rsplit("/", 1)[-1]
                # strip version v1
                base_id = re_split_version(raw_id)
                title = e.find("a:title", ns).text.strip()
                summary = e.find("a:summary", ns).text.strip()
                published = e.find("a:published", ns).text.strip()
                dt = datetime.strptime(published[:10], "%Y-%m-%d")
                if dt < cutoff:
                    continue
                authors = [a.find("a:name", ns).text for a in e.findall("a:author", ns) if a.find("a:name", ns) is not None]
                # DOI link
                doi = ""
                for link in e.findall("a:link", ns):
                    if link.get("title") == "doi":
                        doi = link.get("href", "").replace("http://dx.doi.org/", "").lower()
                out.append({
                    "id": f"arxiv:{base_id}", "source": "arxiv", "raw_id": base_id,
                    "title": _clean(title), "abstract": _clean(summary),
                    "authors": authors, "date": published[:10],
                    "url": f"https://arxiv.org/abs/{base_id}",
                    "doi": doi, "pmid": "", "arxiv_id": base_id,
                })
            except Exception as ex:
                log.warning("arXiv 单篇解析失败: %s", ex)
    except Exception as e:
        log.error("arXiv XML 解析失败: %s", e)
    log.info("arXiv: %d 篇 (窗口内)", len(out))
    return out


# ====================================================================
# bioRxiv
# ====================================================================
def fetch_biorxiv(cfg: dict, days: int) -> list[dict]:
    src_cfg = cfg.get("sources", {}).get("biorxiv", {})
    if not src_cfg.get("enabled", True):
        return []
    start, end, _ = _date_range(days)
    categories = set(src_cfg.get("categories", []))
    max_results = src_cfg.get("max_results", 500)
    out = []
    cursor = 0
    try:
        while True:
            url = f"{BIORXIV_BASE}/{start}/{end}/{cursor}"
            r = requests.get(url, timeout=60)
            r.raise_for_status()
            data = r.json()
            coll = data.get("collection", [])
            if not coll:
                break
            for item in coll:
                cat = item.get("category", "")
                if categories and cat not in categories:
                    # 仍保留，但在标题/摘要层面由后续关键词粗筛过滤；这里不硬砍
                    pass
                doi = (item.get("doi") or "").lower()
                title = item.get("title", "")
                abstract = item.get("abstract", "")
                authors_str = item.get("authors", "")
                authors = [a.strip() for a in authors_str.split(";") if a.strip()] if authors_str else []
                date = (item.get("date") or "")[:10]
                out.append({
                    "id": f"biorxiv:{doi}", "source": "biorxiv", "raw_id": doi,
                    "title": _clean(title), "abstract": _clean(abstract),
                    "authors": authors, "date": date,
                    "url": f"https://www.biorxiv.org/content/{doi}v1" if doi else "",
                    "doi": doi, "pmid": "", "arxiv_id": "",
                })
                if len(out) >= max_results:
                    break
            if len(out) >= max_results or data.get("messages", [{}])[0].get("status") == "ok" and len(coll) < 100:
                break
            cursor += len(coll)
            time.sleep(0.3)
    except Exception as e:
        log.error("bioRxiv 失败: %s", e)
    log.info("bioRxiv: %d 篇", len(out))
    return out


# ====================================================================
# 汇总 + 去重
# ====================================================================
def fetch_all(cfg: dict, days: int) -> tuple[list[dict], list[str]]:
    """调用所有启用的数据源。单源失败返回空列表，不影响其它。返回 (papers, errors)。"""
    errors = []
    all_papers = []

    for name, fn in [("pubmed", fetch_pubmed), ("arxiv", fetch_arxiv), ("biorxiv", fetch_biorxiv)]:
        try:
            papers = fn(cfg, days)
            all_papers.extend(papers)
        except Exception as e:
            log.error("数据源 %s 整体异常: %s", name, e)
            errors.append(f"{name}: {e}")

    # 跨源去重：优先级 pubmed > arxiv > biorxiv；按 DOI 合并
    seen_ids = set()
    seen_doi = {}
    deduped = []
    # 按 source 优先级排序
    pri = {"pubmed": 0, "arxiv": 1, "biorxiv": 2}
    all_papers.sort(key=lambda p: pri.get(p["source"], 9))
    for p in all_papers:
        if p["id"] in seen_ids:
            continue
        doi = p.get("doi", "")
        if doi and doi in seen_doi:
            # 合并 cross id 到已存在的那篇
            keep = seen_doi[doi]
            if not keep.get("pmid") and p.get("pmid"):
                keep["pmid"] = p["pmid"]
            if not keep.get("arxiv_id") and p.get("arxiv_id"):
                keep["arxiv_id"] = p["arxiv_id"]
            continue
        seen_ids.add(p["id"])
        if doi:
            seen_doi[doi] = p
        deduped.append(p)
    log.info("去重后候选总数: %d (来自 %d)", len(deduped), len(all_papers))
    return deduped, errors


# ---- 小工具 --------------------------------------------------------
_MONTHS = {m: i for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun",
     "jul", "aug", "sep", "oct", "nov", "dec"], start=1)}


def _month_to_num(m: str) -> int:
    """PubMed 月份可能是 '09' / '9' / 'Sep' / 'September'。"""
    m = (m or "").strip()
    if not m:
        return 1
    if m.isdigit():
        n = int(m)
        return n if 1 <= n <= 12 else 1
    return _MONTHS.get(m[:3].lower(), 1)


def _txt(node, path):
    el = node.find(path)
    return (el.text or "").strip() if el is not None and el.text else ""


def _clean(s: str) -> str:
    return re_ws(s.strip()) if s else ""


def re_ws(s: str) -> str:
    import re
    return re.sub(r"\s+", " ", s).strip()


def re_split_version(raw_id: str) -> str:
    import re
    return re.sub(r"v\d+$", "", raw_id)


def os_get(key):
    import os
    return os.environ.get(key, "")
