# Paper Scout 日报 2026-11-18

共推荐 **2** 篇论文。

## 1. AlphaGenome 2 predicts regulatory activity and variant effects across cell states

bioRxiv · 预印本 · 2026-11-17 · 相关性 10/10

**研究关联：当前课题直接相关**

- **为什么值得看**：AlphaGenome 2直接解决跨细胞类型/状态的调控活性与变异效应预测，完美契合增强子活性预测与泛化研究。
- **任务与验证范围**：输入：1Mb DNA序列及指定细胞状态条件 → 输出：调控活性、变异效应及增强子-基因连接；物种/体系：人类和小鼠全生物体单细胞图谱及bulk数据；验证范围：跨数百种人类细胞类型及未见数据集/细胞状态
- **核心方法**：基于条件化深度学习的序列到功能预测模型，通过从基因表达推断条件实现零样本跨细胞状态迁移。
- **主要发现与证据**：AG2在90%精度下单细胞eQTL召回率较微调的AlphaGenome 1翻倍，优于目标数据集专用模型，并在增强子-基因连接和因果变异定位上达到SOTA。
- **可借鉴点（研究建议）**：推测其基于基因表达推断细胞状态的条件化机制，可为我的虚拟表观遗传特征跨细胞类型预测提供解耦序列与状态特征的新思路。
- **迁移边界**：原论文侧重1Mb长序列的变异效应与增强子-基因连接，我的任务若聚焦游离型增强子局部活性及padding影响，其长序列架构与条件化策略在短序列或特定padding下的表现未被证明，不可直接假设泛化有效。
- **阅读时核实**：AG2在处理1Mb输入序列时采用了何种位置编码或padding策略，该策略对局部增强子活性预测的分辨率和精度是否有具体影响？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.11.765857v1) · [DOI](https://doi.org/10.64898/2026.11.11.765857)

作者：Gayoso, A., Mottram, A., Karollus, A. et al. (24 authors)
来源标注的末位/通讯作者：Adam Gayoso
机构：Google DeepMind

### 英文摘要

Most genetic variants associated with human traits and diseases lie in non-coding DNA, where they can alter gene regulation in specific cell types and states. Single-cell atlases chart these states across tissues and development, but rarely profile enough donors to associate variants with expression directly. Deep learning models could bridge this gap by predicting variant effects from DNA sequence, yet they poorly distinguish related cell states and require fine-tuning for new datasets. Here we present AlphaGenome 2 (AG2), which substantially advances cell-type-specific prediction of regulatory activity and variant effects for gene expression and chromatin accessibility. Trained on organism-wide human and mouse single-cell atlases and bulk functional genomics data, AG2 takes as input a 1-Mb DNA sequence and a condition specifying a target tissue, cell type, or cell state. Conditioning enables AG2 to impute unmeasured epigenomic tracks and predict multimodal variant effects across cell types. Inferring this condition directly from gene expression extends AG2 to unseen datasets and cell states without fine-tuning. AG2 outperforms fine-tuned AlphaGenome 1 and specialized models trained on target datasets, doubling recall of causal single-cell eQTLs at 90% precision. AG2 also achieves state-of-the-art enhancer-gene linking and can pinpoint causal variants at complex trait loci. Across hundreds of human cell types, we generated an atlas of enhancer-gene links and scores for 7 million common variants. As single-cell profiling expands across development, tissues, and disease cohorts, AG2 provides a blueprint for turning observational atlases into variant effect maps.

---

## 2. LAMP sheds light on how sequence to function models learn variant effects during post-training

bioRxiv · 预印本 · 2026-11-17 · 相关性 8/10

**研究关联：方法可借鉴**

- **为什么值得看**：深入分析了Enformer等sequence-to-function模型在post-training中学习变异效应的机制与局限性。
- **任务与验证范围**：输入：含人工基序扰动SNV的个人基因组序列 → 输出：基因表达预测；研究物种/细胞体系：摘要未说明；验证范围：未见基因和个体（HOGP），摘要未说明是否跨细胞类型
- **核心方法**：提出LAMP框架，通过在个人基因组中引入人工转录因子基序扰动SNV，对Enformer等序列到功能模型进行微调并分析其注意力机制。
- **主要发现与证据**：即使引入易于学习的人工变异，微调Enformer在未见基因和个体上仍表现不佳（相对线性基线）；原因是预训练先验导致对远端调控元件注意力权重降低，且序列变异性掩盖了基序扰动模式；提出的数据增强策略显著改善了人工变异效应的学习。
- **可借鉴点（研究建议）**：论文对预训练先验影响远端元件注意力的分析，启发我在评估padding影响时，可推测并检验padding操作是否会改变模型对局部或远端调控元件的注意力分布。
- **迁移边界**：原论文聚焦于个人基因组变异对基因表达预测的微调机制，而我的任务是预测不同细胞类型增强子活性及评估padding影响。原论文关于注意力难以重连的结论是在变异微调任务下得出的，不能直接泛化到直接的增强子活性预测或不同padding策略的评估中。
- **阅读时核实**：LAMP框架中引入的人工SNV和数据增强策略，是否受到Enformer固定输入长度或边缘padding效应的影响？模型在处理这些人工变异时，其注意力变化是否与序列在输入窗口中的绝对位置有关？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.13.766567v1) · [DOI](https://doi.org/10.64898/2026.11.13.766567)

作者：Drusinsky, S., Pollard, K. S.
来源标注的末位/通讯作者：Katherine S. Pollard
机构：Gladstone Institutes & UCSF

### 英文摘要

Genomic sequence-to-function (S2F) models show promise for interpreting noncoding genetic variation, yet they currently underestimate the effects of most causal variants. This leads to fine-mapping failures that are reflected in their underperformance relative to linear baselines at predicting gene expression across individuals from personal genome sequences. Improving personal genome predictions, which reflect this underestimation, is therefore critical. There is broad interest in post-training S2F models to improve these predictions, yet many groups have shown that doing so with personal genome sequences and paired expression values does not meaningfully improve predictions on held-out genes and people (HOGP). Why these post-training efforts to improve predictions on HOGP, and therefore causal variant underestimation, remains unclear. To understand why, we introduce LAMP (Learning of Artificial Motif Perturbations), a framework in which artificial SNVs (aSNVs) perturbing transcription factor motifs are substituted into personal genome datasets genome-wide with large, consistent, and causal effects on gene expression. These aSNVs are designed to be deliberately easy to learn, yet fine-tuning Enformer using this LAMP framework led to persistent underperformance on HOGP, which suggests fundamental challenges for learning variant effects during post-training that are independent of the complexity of natural genetic variation. Our findings suggest this underperformance is caused in part due to challenges learning to strengthen enhancer-gene links during post-training. In particular, models struggle with learning to rewire attention weights to relate aSNV detection, over distance, to a change in expression of the target gene. This limitation is caused by strong pre-trained priors that downweight distal regulatory elements, causing extreme data inefficiency in learning to attend to distal elements, and variants within them, during post-training. Second, sequence variability between loci containing different instances of the same TF motif obscures otherwise easy-to-learn motif perturbation patterns and also hinder learning of variant effects. Our results suggest that the scale of observed human genetic variation is vastly insufficient to maximize S2F model accuracy on HOGP via simple fine-tuning, consistent with past outcomes. We propose data augmentation strategies that, under LAMP, significantly improve learning of aSNV effects by strategically targeting the limitations we identified. We release LAMP as a tool to troubleshoot and optimize future S2F post-training objectives.

---

中文笔记基于标题和摘要生成，未核验全文；研究建议不代表论文已验证的结论。相关性分数不是论文质量评分。

检索统计：窗口 [2026-11-15 00:00, 2026-11-18 00:00) UTC；抓取 biorxiv 137/pubmed 57 → 粗筛 36 篇 → LLM 选中 2 篇
