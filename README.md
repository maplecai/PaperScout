# PaperScout — 个性化科研论文推荐器

每天自动抓取 PubMed / arXiv / bioRxiv 最新论文，用 LLM 根据你的 research profile 做相关性筛选，只推送最相关的 5–10 篇，附带中文总结。运行在 GitHub Actions 上，不依赖本地电脑开机。

## 流程

```
PubMed / arXiv / bioRxiv  (过去 48h)
  → DOI/PMID/arXiv ID 去重 (+ 历史去重)
  → 关键词 + 作者名粗筛 (省 LLM token)
  → LLM 批量相关性评分 (profile + title + abstract)
  → 动态阈值选 Top 5–10
  → 中文总结
  → reports/paper_watch_YYYY-MM-DD.md
  → 微信(Server酱)简版 + Email 完整版
  → 更新 state.json
```

## 快速开始

### 1. 配置 research profile

编辑 `config.yaml`。这是整个系统最重要的文件——LLM 的相关性判断完全基于它。关键字段：
- `profile.core_topics` / `current_research_questions` / `important_methods`
- `profile.representative_papers`（DOI，校准 LLM 口味）
- `profile.preferred_topics` / `negative_topics`
- `tracked_authors`（来自 Google Scholar alerts，作者命中 = 强信号）

### 2. 设置 LLM（必需）

走 OpenAI 兼容接口。GLM 百度千帆 / OpenAI / DeepSeek 均可。设置环境变量：

```bash
export OPENAI_BASE_URL=https://qianfan.baidubce.com/v2   # 千帆示例
export OPENAI_API_KEY=your_key
export OPENAI_MODEL=glm-5.2                               # 或 gpt-5-mini / deepseek-chat
```

### 3. 本地测试

```bash
pip install -r requirements.txt

# 只抓取 + 粗筛，不调 LLM、不推送（验证数据源和 profile）
python main.py --dry-run --days 3

# 完整流程但不推送
python main.py --no-notify

# 完整流程
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

不配置推送时，日报仍会写入 `reports/` 并提交回仓库。

### 6. GitHub Actions 自动运行

把仓库推到 GitHub，在 **Settings → Secrets** 添加上述所有环境变量（`OPENAI_BASE_URL` / `OPENAI_API_KEY` / `OPENAI_MODEL` / `NCBI_API_KEY` / `SC_SENDKEY` / `SMTP_*` / `EMAIL_TO`）。

Workflow 每天北京时间 09:00 自动运行，也支持手动触发（Actions → Daily Paper Watch → Run workflow，可填 `days` 和 `dry_run`）。

日报和 state.json 会自动 commit 回仓库。

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
├── state.json           # 历史推荐记录，避免重复
├── reports/             # 每日 markdown 日报
├── google_scholar_alerts.txt   # 你的 Scholar alerts 原始列表
└── .github/workflows/daily.yml
```

## 成本控制

- 第一轮只用 title + abstract，不读全文
- 关键词粗筛砍掉 ~60% 无关论文
- LLM 批量评分（每批 12 篇），每日 ~10 次调用
- 只对最终 5–10 篇做详细中文总结
- abstract 截断 1500 字防 token 爆炸
- 粗筛候选上限 120 篇（可调 `ranking.max_llm_candidates`）

GLM/DeepSeek 级别模型每日成本通常 < ¥0.5。

## LLM 输出结构

每篇候选论文 LLM 输出：

```json
{
  "relevance_score": 8,
  "priority": "P0",
  "why_relevant": "直接用 sequence-to-function 模型预测增强子活性，与你的当前问题一致",
  "novelty_for_me": "提出了新的 padding 策略处理长序列边界效应",
  "worth_reading": true
}
```

优先级：`P0` 直接命中当前研究问题 / `P1` 方法模型高度相关 / `P2` 间接启发 / `exclude` 不关注。

## 调优

- 推太多无关论文 → 提高 `ranking.selection.min_score`（如 6）或在 `negative_topics` 加词
- 漏掉相关论文 → 降低 `keyword_prefilter_threshold`（如 0.03）或在 `preferred_topics` 加词
- 想看更多 → 提高 `ranking.selection.max_papers`
- 想换 LLM → 只改环境变量，代码不动

## 故障容忍

- 单个数据源失败 → 跳过，继续其它源
- LLM 批次失败 → 该批标记 exclude，不中断
- 推送失败 → 日报仍写入 reports/ 并提交
- 全部已推荐过 → 当日不重复推送
