# PaperScout — Agent 参考文档

## 项目概述

PaperScout 是一个个性化的日更论文推荐系统。每天从 PubMed、arXiv、bioRxiv 三个数据源抓取最新论文，经过关键词粗筛和 LLM 相关性打分，只推送与你 research profile 最相关的 Top N 篇，附带中文总结笔记。跑在 GitHub Actions 上，日均成本 < ¥0.5。

## 架构

```
config.yaml          科研画像 + 数据源/筛选/推送参数（唯一事实来源）
main.py              主编排器：抓取 → 去重 → 粗筛 → LLM → Top → 总结 → 日报 → 推送 → state
fetch.py             三源独立抓取 + 跨源 DOI 合并去重。单个源失败不影响其它两个
rank.py              关键词加权粗筛 + LLM 批量打分 + 动态阈值 Top 选择
summarize.py         对入选论文逐篇生成中文总结（{core_method, main_finding, inspiration}）
notify.py            Markdown 日报渲染 + 微信 (Server酱³) + Email (SMTP) 推送
llm.py               OpenAI 兼容 LLM 客户端。纯 requests，无 SDK。429/5xx 指数退避重试，4xx 直接抛
state.json           去重 dict（120 天滚动清理）+ 运行历史
```

## 核心设计决策

### 去重：三层防线

1. **抓取时跨源合并** — 按 DOI 跨源合并，优先级 pubmed > arxiv > biorxiv。合并时把 PubMed 侧未记录的 arxiv_id/pmid 补到保留的那篇上
2. **state.json 多键标记** — 每篇论文存全部已知标识符：`pubmed:ID`、`doi:DOI`、`pmid:ID`、`arxiv_id:ID`。同一个论文换一套 ID 系统出现也会被 `filter_seen` 挡掉
3. **seen 标记在推送之前落盘** — `mark_seen + save_state` 在 push 前面执行。推送阶段崩了（比如 Server酱 挂了、SMTP 超时），明天也不会把同一篇论文重新推荐出来。例外：LLM 调用失败的论文（`_rank._failed=True`）不会被标记 seen，下次运行时重新送 LLM 评估，防止因网络抖动永久漏掉论文

### LLM 失败容错

- 批次失败 → 该批所有论文填入 `_placeholder_rank`（priority=EXCLUDE，`_failed=True`），不阻塞后续批次
- 总结失败 → 单篇回退空 dict，不影响其它入选论文的总结
- 以上两种情况都不写 seen，下次运行重试

### 微信与 Email 内容完全一致

- `build_report_md(papers, date_str, errors, stats)` 只调用一次，返回的 md 字符串原样用于归档、微信推送、Email 发送
- `send_wechat(md, date_str, n_papers)` 直接收同一份 md，不再自己渲染
- 标题统一为 `# Paper Scout 日报 2026-09-01`
- 微信内容超过 Server酱 约 30KB 上限时截断，尾部注明「完整版见 Email / reports/」

### 检索窗口锚定（`--end-date`）

`--end-date D`（不含 D 当天）→ 检索窗口 `[D-3 0:00, D 0:00)`，严格 72 小时，覆盖日期为 D-3、D-2、D-1。日报记为该边界日 D。

| 数据源 | 底层机制 | 为什么不受 cron 延迟影响 |
|---|---|---|
| PubMed | PDAT 按日期（非时间戳） | `PDAT [D-3 : D-1]`，三整天 |
| bioRxiv | API 按 posted date | `/{D-3}/{D-1}/`，三整天 |
| arXiv | 时间戳，但显式加 上界 | `dt >= D-3 00:00 AND dt < D 00:00` |

定时触发命令：`python main.py --end-date $(date -u +%F)` （cron UTC 2:00）

手动触发（workflow_dispatch）时不加 `--end-date`，以实际运行时刻为终点的自然窗口。

### lookback 为什么是 3 天

基于实测数字：

- PubMed：PDAT 索引延迟 < 1 天（逐日 esearch count 验证：昨天 57 篇、前天 49 篇均满额）
- bioRxiv：API 延迟 ~0–1 天（完整翻页 1491 篇验证，今天 posted 的论文已经在返回）
- arXiv：最坏 ~2.3 天（周五 14:00 ET 后提交 → 周日 20:00 ET 发布）

所以 3 天窗口覆盖了 arXiv 的最坏情况再加约 0.7 天余量。state 去重保证重叠天不会推荐重复论文，所以可以大胆设宽窗口。

### 通讯作者 = 最后一位作者

PubMed XML 解析时，对每个 Author 结点都检查是否有 `AffiliationInfo`。用覆盖赋值取最后一位带单位的作者。如果真实通讯作者（最后一位）在 XML 里没挂单位，回退到前一位带单位的（名字与单位保持配对）。

arXiv 无作者单位元数据，bioRxiv 走 `author_corresponding` 字段。

### 作者显示规则

- ≤ 8 人 → 全部展示
- \> 8 人 → 展示前 3 人 + et al. (N authors)

## 各模块不变量与细节

### fetch.py

- 统一输出 dict 格式见模块 docstring。所有源都必须产出完全一致的字段集合
- `_get_backoff` 是唯一的 HTTP 封装：指数退避 1s→2s→…→64s，共 7 次。429/502/503 + RequestException 都重试
- **bioRxiv API 每页返回 30 条（不是 100）**。分页终止条件必须是 `if not coll: break`，不能写成 `len(coll) < 100`
- PubMed XML 解析 —— **严禁 `.//` 取 PMID/DOI**：`ReferenceList` 下的参考文献有相同结构的 PMID/DOI 节点。所有 XPath 必须以文章结点的直接子结点为锚（`./PubmedData/ArticleIdList/ArticleId` 而非 `.//ArticleId`）
- PubMed 标题可能有内嵌 `<i>/<sup>` 等标签，必须用 `itertext()` 取全文
- `fetch_all` 的 `backfill` 参数只在 `--date` 回填时为 True —— 这是给 arXiv/bioRxiv 额外天数的原因（索引延迟缓冲）

### rank.py

- `_rank` dict 的键由 `_normalize_rank` 或 `_placeholder_rank` 构造，键恒齐全（`relevance_score`, `priority`, `why_relevant`, `novelty_for_me`, `worth_reading`），`priority` 恒大写。所有消费方可以安全地用 `p["_rank"]["priority"]` 而非 `.get(…, default)`
- 关键词粗筛时 `if t and t in text` —— 不能去掉 `if t`，因为 `"" in text` 恒为 True，config 里混入空串会让所有论文全局加分
- LLM 批次按 index 对齐：LLM 可能少返或乱序，`rank_by_idx.get(i)` 兜底为 `_placeholder_rank`
- `select_top`：双层条件不是冗余。外层 `pri in accept or score >= min_score` 进候选，内层 `worth_reading or score >= min_score or P0/P1` 最后把关 —— 确保 P2 + 不值得读 + 低分的论文不会入选

### llm.py

- `LLMClient(enabled=True/False)`：三个环境变量缺一不可。`enabled=False` 时所有方法静默返回空/None
- `chat_json` → `_chat` → `parse_json_defensive`：解析链先去掉 markdown fence，再尝试 `json.loads`，失败后匹配第一个 `[ ]` 或 `{ }` 子串
- LLM 重试：429 + 5xx → 指数退避（2^attempt 秒，3 次）；4xx 其它 → 不重试，直接抛

### notify.py

- `build_report_md` 是这个模块唯一渲染日报的地方。微信和 Email 不要各自组装内容
- `send_empty_notice` 两种模式：`no_push=True`（检索阶段）写空 JSON 标记，留待后续 `--test-notify` 发送；`no_push=False`（一次性全流程）直接推微信
- SMTP 端口解析：`int(os.environ.get("SMTP_PORT") or 465)`。必须用 `or` 而不是 get 的默认值，因为 GitHub Secrets 设为空字符串时 `get("SMTP_PORT", "465")` 返回 `""` 而非 `"465"`
- Server酱 API 返回 `code: 0` 表示成功，但仅表示 API 已接受 —— 消息能否送达微信还取决于用户是否关注了「方糖」服务号

### main.py

三种运行模式，互斥：

1. `--date 2026-09-03` 回填：只取目标日期的论文，各源加缓冲区（arxiv+2d, biorxiv+5d），只写入 state 该日
2. `--end-date 2026-09-07` 锚定：窗口 `[D-3 0:00, D 0:00)`，日报记 D，state 记 D。定时触发专用
3. 默认：自然窗口（配置的 lookback_days 天，以当前时刻为终点）

`--test-notify` 独立：读最新一份 report JSON/MD 测试推送通道，不抓取不调 LLM。

| 路径 | 是否会落 seen 标记 | 是否会推送 |
|---|---|---|
| 正常有论文 | ✓（推送前） | ✓ |
| 0 候选/0 选中 | ✓（空日通知前保存 state） | 空日微信通知 |
| 全源失败 | ✓（写空 JSON 标记前保存 state） | 空日微信通知 |
| `--no-notify` | ✓ | 不推 |
| `--dry-run` | 不写 | 不推 |
| `--test-notify` | 不写 | ✓ |

## 环境配置

### 必需环境变量

```bash
OPENAI_BASE_URL   # OpenAI 兼容 endpoint
OPENAI_API_KEY    # API key
OPENAI_MODEL      # 模型名（如 glm-5.3-flash）
```

### 可选

```bash
SC_SENDKEY        # Server酱³ sendkey，不配则跳过微信推送
SMTP_HOST/PORT/USER/PASSWORD  # SMTP 配置，不配则跳过 Email 推送
EMAIL_TO          # 收件邮箱
NCBI_API_KEY      # PubMed 提速（10 req/s → 标准 3 req/s）
```

### 本地 .env

`main.py` 启动时自动调用 `dotenv.load_dotenv()`（如果装了 `python-dotenv`）。本地可以建 `.env` 文件放以上变量，不用 export。

### Git 代理（Clash Verge）

WSL 下 Clash Verge tun mode + 7897 HTTP/SOCKS 端口。TUN 负责直连，但 SSH 不走 TUN。

**HTTPS git 操作**（Claude/其它工具）：
```bash
git config --global http.proxy http://127.0.0.1:7897
git config --global https.proxy http://127.0.0.1:7897
```

**SSH git push**（人类终端）：
在 `~/.ssh/config` 追加：
```
Host github.com
    Hostname github.com
    ProxyCommand nc -X connect -x 127.0.0.1:7897 %h %p
```
这个规则只对 `git@github.com` 生效，不干扰你的其他 SSH 配置。

### GitHub Actions Secrets

所有环境变量都通过 Settings → Secrets 注入 workflow。注意：
- 值为空的 secret → `os.environ.get("K", "default")` 返回 `""` 而非 `"default"`
- 不用的 secret 直接删除，别留空值（或者代码侧用 `os.environ.get("K") or default`）
- Workflow 文件（`.github/workflows/daily.yml`）的修改需要 OAuth `workflow` 权限 —— `gh auth token` 默认可能不带这个 scope，此时需要用 SSH push workflow 变更

### GitHub Actions cron 延迟

`cron: 0 2 * * *` = UTC 2:00，但免费 tier 实际启动通常延后 5-30 分钟，极端情况下数小时（实测过 4.5 小时延迟，约北京时间 14:30 才执行）。因为 `--end-date` 锚定了检索窗口，这只影响用户收到消息的时间，不影响论文覆盖。

## Gotchas（踩过的坑）

1. **bioRxiv 页大小** — API 每页返回 30 篇，不是 100。终止条件不能依赖 `len(coll) < 100`，只能判 `not coll`
2. **arXiv DOI 覆盖率 ~1%** — 不能指望用 DOI 给 arXiv 论文去重，必须依赖 `arxiv_id` 别名键
3. **PubMed XML 参考文献串号** — `ReferenceList` 里的参考文献节点也有 PMID/DOI。XPath 全部限定到文章结点根下
4. **空字符串 Secrets** — `os.environ.get("KEY", "fallback")` 的 fallback 只在 KEY **不存在** 时生效。Secrets 设了空值 → 返回 `""` → `int("")` 直接崩。用 `os.environ.get("KEY") or fallback`
5. **State 必须先落盘再推送** — 推送阶段的任何崩溃都不能丢 seen 记录，否则隔天重复推荐
6. **Server酱 API 成功 ≠ 送达** — 返回 `code: 0` 仅表示 API 已接受。消息进微信需要用户关注「方糖」服务号。关键词：Server酱³、sct.ftqq.com、sendkey 格式 `sctp<id>t<token>`
7. **Workflow 不要 hardcode `--days`** — 只有手动触发且用户明确填了 days 才传 `--days`，否则 fallback 到 config.yaml 的 `fetch.lookback_days`
8. **本地 state.json 与远程差异** — Actions bot 每次跑完都会 commit state.json。本地 git pull 前本地的 state 是过期版本。在本地跑涉及 state 的操作之前务必 `git pull`

## 测试

无测试框架。自检模式：一次性 Python heredoc 验证核心不变量。

```bash
python3 - <<'EOF'
import fetch, rank, notify, llm
assert fetch._clean("  a\n b ") == "a b"
assert llm.parse_json_defensive("junk {\"a\":1} tail") == {"a": 1}
assert rank._placeholder_rank({})["_failed"] is True
# ...
print("OK")
EOF
```