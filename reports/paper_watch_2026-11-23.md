# Paper Scout 日报 2026-11-23

共推荐 **1** 篇论文。

## 1. An open long non-coding RNA foundation model for generalizable prediction

bioRxiv · 预印本 · 2026-11-22 · 相关性 7/10

**研究关联：方法可借鉴**

- **为什么值得看**：lncRNA基础模型，涉及序列到功能预测、预训练策略和评估基准构建，与你的基因组基础模型研究高度相关。
- **任务与验证范围**：输入：lncRNA序列 → 输出：lncRNA功能、注释、结构及调控预测；研究物种/细胞体系：摘要未说明（提及跨物种）；验证范围：包含跨物种、跨任务泛化评估
- **核心方法**：采用混合双向状态空间编码器结合结构引导的掩码策略进行预训练。
- **主要发现与证据**：模型在13个下游数据集中的11个取得SOTA；在外部泛化基准上，lncRNA接触预测AUROC达0.962，跨物种编码潜力迁移F1为0.374。
- **可借鉴点（研究建议）**：混合双向状态空间模型（SSM）在处理长序列时可能规避传统Transformer的padding需求，可为评估预训练基因组学模型的长序列处理策略提供参考。
- **迁移边界**：原论文针对lncRNA序列的结构与功能预测，而我的研究关注DNA序列的增强子活性及padding影响；SSM在RNA上的长程依赖捕获能力不能直接等同于在DNA增强子任务上的表现，跨模态迁移需独立验证。
- **阅读时核实**：混合双向状态空间编码器在处理不同长度输入时是否依赖padding，其计算机制能否天然支持变长序列从而消除padding开销？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.20.768117v1) · [DOI](https://doi.org/10.64898/2026.11.20.768117)

作者：Chang, A., Zhu, H., Li, R. et al. (9 authors)
来源标注的末位/通讯作者：S. Kevin Zhou
机构：University of Science and Technology of China	School of Biomedical Engineering, Division of Life Sciences and Medicine

### 英文摘要

Long non-coding RNAs (lncRNAs) play essential roles in transcriptional regulation and chromatin organization, yet predicting their functional properties from sequence remains challenging because informative signals span both local motifs and long-range base pairing across kilobase-scale transcripts. Current RNA foundation models are restricted to short sequences and existing lncRNA prediction models narrowly focus on isolated tasks, leaving a dedicated foundation model notably absent. Here we present LncRFM, a dedicated lncRNA foundation model, supported by the LncCorpus pretraining data and the LncBench evaluation suite, which stand for a systematic framework to decode lncRNAs. For foundation model pretraining, we develop a hybrid bidirectional state-space encoder trained with a structure-guided masking strategy to effectively capture both local sequence patterns and long-range contexts. For pretraining data, we contribute over 9.6 million lncRNA sequences to assemble LncCorpus, a pretraining corpus of 24.7 million sequences. For benchmarking evaluation, we construct a comprehensive benchmark, LncBench, comprising 15 datasets and totaling over 1,010,000 sequences across 10 prediction tasks: six core lncRNA functional and annotation tasks and four structural and regulatory RNA assay tasks. Evaluated against seven RNA foundation models under a unified frozen-encoder protocol, our LncRFM achieves the state-of-the-art primary-metric scores on 11 of the 13 datasets that allow downstream adaptation. On two external generalization benchmarks evaluated without further adaptation, LncRFM matches the best structure-specialized baseline in F1 (0.141) and achieves the highest AUROC (0.962) on lncRNA contact prediction, while maintaining competitive cross-species coding-potential transfer (F1 of 0.374) under severe multi-kingdom domain shift. To benefit the scientific community, we make all datasets, source code, and pretrained models publicly available.

---

中文笔记基于标题和摘要生成，未核验全文；研究建议不代表论文已验证的结论。相关性分数不是论文质量评分。

检索统计：窗口 [2026-11-20 00:00, 2026-11-23 00:00) UTC；抓取 biorxiv 64/pubmed 45 → 粗筛 7 篇 → LLM 选中 1 篇
