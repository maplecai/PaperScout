# PaperScout — 个性化科研论文推荐器

每天自动抓取 PubMed / arXiv / bioRxiv 最新论文，用 LLM 根据你的 research profile 做相关性筛选，推送最相关的 Top N 篇。运行在 GitHub Actions 上，不依赖本地电脑开机。

## 流程

```
PubMed / arXiv / bioRxiv（过去 3 天）
  → DOI/PMID/arXiv ID 去重（含历史去重）
  → 关键词 + 作者名粗筛（省 LLM token）
  → LLM 批量相关性打分
  → 动态阈值选 Top
  → 中文总结
  → 微信 + Email 同一份日报（标题 "Paper Scout 日报 2026-09-01"，含英文摘要）
  → 更新 state.json
```

## 快速开始

### 0. 本地 Python 环境（Windows / Linux）

使用 Python 3.13，与 GitHub Actions 一致。在项目根目录执行：

```text
conda env list
# 仅当 paper_scout 环境不存在时创建
conda create -n paper_scout python=3.13 pip -y
conda run -n paper_scout python -m pip install -r requirements.txt
```

Windows PowerShell 启动（按实际位置修改项目路径）：

```powershell
Set-Location C:\Users\maple\projects\paper_scout
conda run --no-capture-output -n paper_scout python -X utf8 main.py --dry-run
```

Linux / WSL Bash 启动：

```bash
cd /path/to/paper_scout
conda run --no-capture-output -n paper_scout python -X utf8 main.py --dry-run
```

`conda run` 无需先激活环境；`-X utf8` 保证 Windows 重定向输出时中文日志也使用 UTF-8。
配置、状态和报告路径相对于当前工作目录，因此请先进入项目根目录。
Windows 和 WSL 的 Conda 环境各自独立，不能直接复制环境目录共用。

### 1. 配置科研兴趣

编辑 `config.yaml`。最关键的两个部分：

- `profile`：`core_topics`、`active_projects`（含 `keywords`）、`research_interests`、`negative_topics`
- `tracked_authors`：作者命中 = 强信号

### 2. 设置 LLM

走 OpenAI 兼容接口（GLM/DeepSeek/OpenAI 均可）。在项目根目录的 `.env` 中设置（Windows / Linux 通用）：

```dotenv
OPENAI_BASE_URL=https://qianfan.baidubce.com/v2/tokenplan/personal
OPENAI_API_KEY=your_key
OPENAI_MODEL=glm-5.3-flash
```

首次配置可复制 `.env.example` 为 `.env`；已有 `.env` 时保留原文件。程序自动读取它，文件已被 Git 忽略；GitHub Actions 仍从 Secrets 读取相同变量。

### 3. 本地测试

以下命令在已激活的 `paper_scout` 环境中执行（`conda activate paper_scout`），也可以使用上面的 `conda run` 前缀。

```bash
# 只检查命令行入口，不访问网络
python -X utf8 main.py --help

# 离线回归测试
python -X utf8 -m unittest discover -s tests

# 只抓取 + 粗筛，不调 LLM、不推送
python -X utf8 main.py --dry-run

# 完整流程但不推送（日报仍写入 reports/）
python -X utf8 main.py --no-notify

# 推送已有日报（不重新抓取/调 LLM，可用于测试推送通道）
python -X utf8 main.py --test-notify

# 回填指定日期
python -X utf8 main.py --date 2026-09-03
```

### 4. 可选：PubMed 提速

申请 NCBI API key 以提升限频（10 req/s vs 3 req/s）：https://www.ncbi.nlm.nih.gov/account/settings/

在 `.env` 中添加：

```dotenv
NCBI_API_KEY=your_key
```

### 5. 推送配置

**微信（Server酱³）**：扫码绑定 https://sct.ftqq.com/，拿到 SENDKEY：
在 `.env` 中添加：
```dotenv
SC_SENDKEY=SCT...
```

**Email（SMTP）**：
在 `.env` 中添加：
```dotenv
SMTP_HOST=smtp.qq.com
SMTP_PORT=465
SMTP_USER=you@qq.com
SMTP_PASSWORD=应用专用密码
EMAIL_TO=you@example.com
```

至少配一个推送通道。都不配时日报仅写入 `reports/`。

### 6. GitHub Actions

把仓库推到 GitHub，在 Settings → Secrets 添加上述所有环境变量。

Workflow 使用 Ubuntu + Python 3.13，通过同一份 `requirements.txt` 安装依赖，无需 Conda。每天 UTC 00:00（北京时间 08:00）自动运行。定时触发时窗口用 `--end-date` 锚定到 UTC 0 点，严格覆盖 `[今日0点-72h, 今日0点)` 的论文。也支持手动触发（Actions → PaperScout → Run workflow）。日报和 state.json 自动 commit 回仓库。

**注意**：GitHub Actions cron 可能延迟 5-30 分钟（免费 tier 高峰期更长）。这不影响论文覆盖（窗口锚定了），只影响收到消息的时间。

## 日报格式

微信和 Email 推送同一份内容，标题为 `Paper Scout 日报 {日期}`。开头是流水统计（抓取数 → 粗筛 → LLM 选中），每条论文包含：期刊 / 作者 / 机构（通讯作者 ailiation）/ 日期 / ID / 一句话推荐 / 方法 / 主要发现 / 对我的启发 / 英文 Abstract 折叠块。

## 成本

GLM/DeepSeek 级别模型，每日 < ¥0.5。控制策略：
- 关键词粗筛砍掉大部分无关论文
- LLM 批量评分（每批 10 篇，候选上限 100）
- 只对最终 Top 论文做详细中文总结
- abstract 截断 1500 字

## 调优

- 无关论文太多 → 提高 `ranking.selection.min_score` 或在 `negative_topics` 加词
- 漏掉相关论文 → 降低 `keyword_prefilter_threshold` 或在 `research_interests` 加词
- 想换 LLM → 只改环境变量，代码不变

## 项目结构

```
├── config.yaml          # 你的科研画像（最重要）
├── fetch.py             # 三源抓取 + 去重
├── rank.py              # 关键词粗筛 + LLM 批量评分 + Top 选择
├── summarize.py         # 对 Top 论文逐篇生成中文总结
├── notify.py            # 日报生成 + 微信/Email 推送
├── llm.py               # LLM 客户端封装
├── main.py              # 主入口
├── state.json           # 去重记录 + 运行历史
└── reports/             # {date}.md / {date}.json
```
