# PaperScout — 个性化科研论文推荐器

每天自动抓取 PubMed / arXiv / bioRxiv 最新论文，用 LLM 根据你的 research profile 做相关性筛选，只推送最相关的 5–10 篇，附带中文总结。运行在 GitHub Actions 上，不依赖本地电脑开机。

## 流程

```
PubMed / arXiv / bioRxiv  (过去 3 天)
  → DOI/PMID/arXiv ID 去重 (+ 历史去重)
  → 关键词 + 作者名粗筛 (省 LLM token)
  → LLM 批量相关性打分 (profile + title + abstract)
  → 动态阈值选 Top 5–10
  → 中文总结
  → reports/{date}.md (日报全文，带英文摘要)
  → 微信 (Server酱) + Email 推送 (同一份内容)
  → 更新 state.json
```

## 快速开始

### 1. 配置 research profile

编辑 `config.yaml`。这是整个系统最重要的文件——LLM 的相关性判断完全基于它。关键字段：

- `profile.core_topics` — 长期核心研究领域（粗筛兜底）
- `profile.active_projects` — 当前科研项目（P0 判定核心依据），每项含 `name`、`keywords`
- `profile.representative_papers` — DOI 列表，校准 LLM 口味
- `profile.research_interests` — 长期感兴趣的方法/方向（P1/P2 判定 + 搜索查询构造）
- `profile.negative_topics` — 不感兴趣的话题，降分
- `tracked_authors` — 作者命中 = 强信号（可去中间名缩写以提升匹配）

### 2. 设置 LLM（必需）

走 OpenAI 兼容接口。GLM 百度千帆 / OpenAI / DeepSeek 均可。设置环境变量：

```bash
export OPENAI_BASE_URL=https://qianfan.baidubce.com/v2/tokenplan/personal
export OPENAI_API_KEY=your_key
export OPENAI_MODEL=glm-5.3-flash
```

### 3. 本地测试

```bash
pip install -r requirements.txt

# 只抓取 + 粗筛，不调 LLM、不推送（验证数据源和 profile）
python main.py --dry-run --days 3

# 完整流程但不推送（仍会生成 reports/*.md）
python main.py --no-notify

# 回填指定日期（state.json 和日报都记为该日期）
python main.py --date 2026-09-03 --no-notify

# 用已有日报 JSON 测试推送格式（不重新抓取、不调 LLM）
python main.py --test-notify

# 完整流程（抓取 + LLM + 推送）
python main.py
```

### 4. 可选：PubMed 提速

申请 NCBI API key（每秒 10 请求而非 3）：https://www.ncbi.nlm.nih.gov/account/settings/

```bash
export NCBI_API_KEY=your_key
```

### 5. 推送配置（可选）

**微信 (Server酱)**：扫码绑定 https://sct.ftqq.com/ ，拿到 SENDKEY：

```bash
export SC_SENDKEY=SCT...
```

**Email (SMTP)**：用 Gmail/QQ/163 的应用专用密码：

```bash
export SMTP_HOST=smtp.qq.com
export SMTP_PORT=465
export SMTP_USER=you@qq.com
export SMTP_PASSWORD=应用专用密码
export EMAIL_TO=you@example.com
```

不配置推送时，日报仍会写入 `reports/`。

### 6. GitHub Actions 自动运行

把仓库推到 GitHub，在 **Settings → Secrets** 添加上述所有环境变量（`OPENAI_BASE_URL` / `OPENAI_API_KEY` / `OPENAI_MODEL` / `NCBI_API_KEY` / `SC_SENDKEY` / `SMTP_*` / `EMAIL_TO`）。

Workflow 每天北京时间 10:00（UTC 02:00，GitHub Actions cron 可能延迟 5-30 分钟）自动运行。定时触发时窗口用 `--end-date` 锚定到 UTC 0 点 —— 严格检索 `[今日 0 点 - 72h, 今日 0 点)` 的论文，与运行时刻无关，cron 延迟不影响边界。也支持手动触发（以当前时刻为终点的自然窗口）。日报和 state.json 会自动 commit 回仓库。

日报和 state.json 会自动 commit 回仓库。

**注意**：GitHub Actions 共享 runner IP 可能被 arXiv 限流（429）。代码已内置指数退避重试（1s→64s），单源失败不中断其它。

## 日报格式

微信和 Email 推送同一份内容，标题为 `Paper Scout 日报 {日期}`，开头是流水统计（各源抓取数 → 粗筛 → LLM 选中）和抓取异常提示，每条论文包含：
- 📊 流水统计（各源抓取数 → 粗筛 → LLM 选中）
- ⚠️ 抓取异常提示（如有）
- 期刊 / 作者 / 机构 / 日期 / ID / 一句话推荐 / 方法 / 主要发现 / 对我的启发

### Email (全文)

微信格式 + 英文 Abstract 折叠块。

## 项目结构

```
paper-scout/
├── config.yaml          # 你的科研画像（最重要，改这里即可调口味）
├── fetch.py             # 三源抓取 + 去重，单源失败不影响整体
├── rank.py              # 关键词粗筛 + LLM 批量相关性评分 + Top 选择
├── summarize.py         # 对 Top 论文逐篇生成中文总结
├── notify.py            # 日报生成 + 微信/Email 推送
├── llm.py               # OpenAI 兼容 LLM 客户端封装
├── main.py              # 主入口，编排全流程
├── state.json           # 历史推荐记录（seen: {id→date}），避免重复
├── reports/             # 每日报告：{date}.md / {date}.json
└── .github/workflows/daily.yml
```

## 成本控制

- 第一轮只用 title + abstract，不读全文
- 关键词粗筛砍掉大部分无关论文
- LLM 批量评分（每批 12 篇）
- 只对最终 Top 5–10 篇做详细中文总结
- abstract 截断 1500 字防 token 爆炸
- 粗筛候选上限 120 篇（可调 `ranking.max_llm_candidates`）
- PubMed 自动查询词已过滤泛词（避免海量无关临床 ML 论文）

GLM/DeepSeek 级别模型每日成本通常 < ¥0.5。

## LLM 输出结构

每篇候选论文 LLM 输出两段：

**相关性评分** (`_rank`)：
```json
{
  "relevance_score": 8,
  "priority": "P0",
  "why_relevant": "直接用 sequence-to-function 模型预测增强子活性",
  "worth_reading": true
}
```

**中文总结** (`_summary`)：
```json
{
  "core_method": "多模态 transformer + 单细胞 ATAC-seq",
  "main_finding": "CREsted 在跨组织增强子预测上显著优于 Enformer",
  "inspiration": "可借鉴序列+染色质的多模态输入范式"
}
```

优先级：`P0` = 直接命中 `active_projects` / `P1` = 与 `research_interests` 高度相关 / `P2` = 间接启发 / `exclude` = 不关注。

## 调优

- 推太多无关论文 → 提高 `ranking.selection.min_score`（如 6）或在 `negative_topics` 加词
- 漏掉相关论文 → 降低 `keyword_prefilter_threshold`（如 0.03）或在 `research_interests` 加词
- 想看更多 → 提高 `ranking.selection.max_papers`
- PubMed 命中太多 → 删减 `active_projects.keywords` 和 `research_interests` 中的宽泛词
- 想换 LLM → 只改环境变量，代码不动

## 故障容忍

- 单个数据源失败 → 跳过，继续其它源；推送中会注明
- LLM 批次失败 → 该批标记 exclude，下次运行重新评估（不标记 seen）
- 推送失败 → 日报仍写入 reports/
- arXiv 限流 → 指数退避重试（1s / 2s / 4s / 8s / 16s / 32s / 64s，共 7 次）
- 全部已推荐过 → 当日发送空日通知（微信 / Email）
- LLM 调用失败 → 指数退避重试 3 次