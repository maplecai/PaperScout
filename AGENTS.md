# PaperScout — Agent Reference

## Overview

Daily paper recommender. Three-source fetch (PubMed, arXiv, bioRxiv) → keyword prefilter → LLM relevance scoring → Chinese summaries → WeChat (Server酱) + Email push. Runs on GitHub Actions, costs < ¥0.5/day.

## Architecture

```
config.yaml          Profile, source limits, ranking thresholds (single source of truth)
main.py              Orchestrator: 抓取 → 去重 → 粗筛 → LLM → Top → 总结 → 日报 → 推送 → state
fetch.py             Three-source fetcher + cross-source DOI dedup. Single-source failure never kills others.
rank.py              Keyword prefilter (TF-IDF-like weighted scoring) + LLM batch ranking + Top-N selection
summarize.py         Per-paper Chinese summaries (title + abstract → {method, finding, inspiration})
notify.py            Markdown report builder + WeChat push (Server酱³) + Email (SMTP)
llm.py               OpenAI-compatible client. requests-based, no SDK. 429/5xx retry, 4xx fast fail.
state.json           Seen dedup (120-day rolling) + run history. Keys: source:id + doi:/pmid:/arxiv_id: aliases.
```

## Key Design Decisions

### Dedup: three-layer
1. **Fetch time** — cross-source DOI merge (priority: pubmed > arxiv > biorxiv)
2. **State time** — multi-key seen dict (`pubmed:ID`, `doi:DOI`, `pmid:ID`, `arxiv_id:ID`). Same paper via different ID = blocked.
3. **Seen marks** — written BEFORE push (push crash won't cause re-recommend tomorrow). _failed papers NOT marked (retry next run).

### LLM failure resilience
- Batch failure → placeholder rank with `_failed=True`
- `_failed` papers are NOT marked seen → will be re-evaluated next run
- Single paper summarization failure → empty summary, doesn't block others

### WeChat = Email (identical content)
- Same `build_report_md(papers, date_str, errors, stats)` for both
- `send_wechat(md, date_str, n_papers)` takes the exact same md string
- Title: `Paper Scout 日报 {date}`
- WeChat truncation at ~30KB (Server酱 limit), with "完整版见 Email" note

### Window anchoring (`--end-date`)
- `--end-date D` → fetch window `[D-3 0:00, D 0:00)` = strictly 72h, papers dated D-3/D-2/D-1
- Report dated D (the boundary day)
- PubMed/bioRxiv: date-based PDAT→immune to cron delay
- arXiv: timestamp-based with explicit upper bound → immune to cron delay
- Cron: `python main.py --end-date $(date -u +%F)` at UTC 2:00
- Manual dispatch: natural window (lookback from current time), no anchoring

### Lookback: 3 days
Reasoned from measured latencies: PubMed <1d, bioRxiv ~0-1d, arXiv worst ~2.3d (Fri>14:00 ET → Sun 20:00 ET). State dedup guarantees no duplicates even with overlapping windows.

### Corresponding author = last author
PubMed XML: last author with affiliation wins (overwrite loop). If last author lacks affiliation, falls back to nearest earlier author with one. Name stays paired with affiliation.

## File Map

| File | Role | Key Invariants |
|---|---|---|
| `config.yaml` | Profile, thresholds, source limits | Single source of truth for lookback_days, ranking params |
| `main.py` | Orchestrator | State saved before push; `--date` vs `--end-date` vs default modes |
| `fetch.py` | Data ingestion | Uniform Paper dict (see docstring); `_get_backoff` for all HTTP; bioRxiv API returns 30/page |
| `rank.py` | Relevance pipeline | `_rank` keys always populated (constructor guarantee); `_kw_score` on keyword-prefiltered papers |
| `summarize.py` | Chinese notes | Per-paper; failure → empty dict, doesn't block |
| `notify.py` | Report + push | `build_report_md` called once, result shared by both channels |
| `llm.py` | LLM client | OpenAI-compat, `parse_json_defensive` handles fence/fragments |
| `state.json` | Dedup + history | Always `git pull` before modifying; 120-day TTL on seen entries |

## Environment / Secrets

### Required
- `OPENAI_BASE_URL`, `OPENAI_API_KEY`, `OPENAI_MODEL` — any OpenAI-compat endpoint (GLM/DeepSeek/OpenAI)

### Optional
- `SC_SENDKEY` — Server酱³ sendkey for WeChat push
- `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASSWORD`, `EMAIL_TO` — SMTP for email push
- `NCBI_API_KEY` — PubMed 10req/s vs 3req/s (recommended)

### Local .env
`python-dotenv` loads `.env` automatically in `main.py`. Example:
```bash
OPENAI_BASE_URL=https://qianfan.baidubce.com/v2/tokenplan/personal
OPENAI_API_KEY=sk-xxx
OPENAI_MODEL=glm-5.3-flash
SC_SENDKEY=SCT...
NCBI_API_KEY=xxx
```

### Git proxy (Clash Verge)
WSL with Clash: HTTP proxy on `127.0.0.1:7897`. TUN mode handles direct connections but SSH doesn't route through TUN.

For HTTPS git operations (Claude):
```bash
git config --global http.proxy http://127.0.0.1:7897
git config --global https.proxy http://127.0.0.1:7897
```

For SSH git push (human terminal), add to `~/.ssh/config`:
```
Host github.com
    Hostname github.com
    ProxyCommand nc -X connect -x 127.0.0.1:7897 %h %p
```

### GitHub Actions
- Cron: `0 2 * * *` (UTC 2:00 = Beijing 10:00). Actual start often delayed 5–30 min (free tier), sometimes 4h+.
- Secrets stored in repo Settings → Secrets; empty-valued secrets cause `os.environ.get("KEY", "default")` to return `""` not default → use `or` pattern instead: `os.environ.get("KEY") or default`
- Workflow file changes require `workflow` OAuth scope; `gh auth token` may lack this → human must push workflow changes via SSH

## Commands

```bash
# Full run
python main.py

# Dry-run: fetch + prefilter, no LLM, no push, no state write
python main.py --dry-run

# Full pipeline, no push (report still written to reports/)
python main.py --no-notify

# Anchor window to UTC midnight boundary
python main.py --end-date 2026-09-07

# Backfill specific date (paper-level date filter, extra buffer for lagging sources)
python main.py --date 2026-09-03

# Test push using existing report JSON (no fetch, no LLM)
python main.py --test-notify
```

## Tests

No test framework. Self-check idiom:
```python
python3 - <<'EOF'
import fetch, rank, notify, llm
assert fetch._clean("  a  b ") == "a b"
assert llm.parse_json_defensive('{"a":1}') == {"a": 1}
# ... domain-specific checks
print("OK")
EOF
```

## Gotchas

1. **bioRxiv page size** — API returns 30/page, not 100. Pagination must continue until empty collection (not `< 100` heuristic).
2. **arXiv DOI coverage ~1%** — Can't rely on DOI for arXiv dedup; use arxiv_id.
3. **PubMed XML** — ReferenceList has duplicate PMID/DOI → always anchor XPath to article root, never use `.//`.
4. **empty-string secrets** — `os.environ.get("K", "default")` returns `""` if K is set to empty. Use `os.environ.get("K") or default`.
5. **State before push** — `mark_seen` + `save_state` must run before push. Otherwise push crash → lost seen marks → duplicate recommendations next run.
6. **WeChat delivery** — Server酱³ API "推送成功" only means accepted, not delivered. Delivery requires user to follow "方糖" service account on WeChat.
7. **Config is single source of truth** — workflow must NOT hardcode `--days` (only pass when user explicitly provides input). Config.yaml's `fetch.lookback_days` wins when no CLI override.
8. **Reports and state.json** — committed by Actions bot. Local state quickly diverges from remote; always `git pull` remote state before local test runs that touch production data.