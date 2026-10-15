# Paper Scout 日报 2026-10-15

共筛选出 **3** 篇推荐论文。
📊 抓取 biorxiv 102/pubmed 67 → 粗筛 28 篇 → LLM 选中 3 篇

## 1. Response representation shapes AlphaGenome enhancer-gene prediction in human astrocytes

- **期刊**: bioRxiv
- **作者**: Huang, Z., Huang, R., Han, J.
- **机构**: Zhongwei Huang @ University of Washington
- **日期**: 2026-10-13
- **ID**: DOI: 10.64898/2026.08.14.744988  |  URL: https://www.biorxiv.org/content/10.64898/2026.08.14.744988v1
- **相关分数**: 8/10
- **一句话推荐**: 直接评估AlphaGenome在增强子-基因预测中的表现，与你的sequence-to-function和增强子活性预测研究高度相关。
- **方法**: 评估序列到功能模型（如AlphaGenome）的缺失响应与稀疏变异响应表示方法，并结合等权重秩融合预测增强子-基因活性。
- **主要发现**: 整体增强子缺失响应可提升基于染色质的基线模型性能；稀疏变异响应以幅度形式融合优于带符号均值，但在增强子内目标选择及跨细胞迁移上效果未定。
- **对我的启发**: 在利用预训练基因组学模型提取虚拟表观遗传特征时，需关注模型输出响应的表示方式（如幅度与符号的取舍），这直接影响下游增强子活性预测融合的效果。

<details><summary>Abstract</summary>

Background: Sequence-to-function models predict regulatory perturbation responses, but their added value beyond established enhancer-gene predictors and across prediction tasks remains unclear. We evaluated whole-enhancer deletion and sparse variant responses in human astrocytes. Results: We analyzed 2,307 CRISPR-interference-tested relations, including 133 expression-decreasing hits. Adding deletion responses increased fully nested EGrf average precision from 0.5475 to 0.6137. The paired increment was 0.0662 (enhancer-cluster 95% interval 0.0144-0.1181). In a separate exploratory analysis, sparse Atlas responses were combined with seven-input logistic and random-forest comparators by equal-weight rank fusion. Atlas magnitude fusion exceeded absolute-deletion fusion by 0.0519 and 0.0637 in average precision. Enhancer-cluster 95% intervals were 0.0098-0.0957 and 0.0220-0.1094, respectively. Standalone Atlas magnitude reached average precision 0.5570, but its advantage over absolute deletion remained uncertain. Signed Atlas fusion performed worse than either comparator alone. Incremental value for within-enhancer target choice and in the external WTC11 MHC evaluation remained uncertain. The reported performance intervals use one-way clustering of fixed predictions; Atlas analyses were exploratory within the same cohort. Conclusions: In AstroREG, whole-enhancer deletion responses increased observed retrieval performance beyond a fully nested chromatin-based predictor. Sparse variant responses were more informative as magnitudes than as signed averages. Improved within-enhancer target choice and external transfer were not established.

</details>

---

## 2. Decoding super-enhancer regulatory grammar and pathogenic gain-of-function variants directly from DNA sequence

- **期刊**: bioRxiv
- **作者**: Liang, Y., Xu, X., Mao, Y., Zheng, Z., Liu, N.
- **机构**: Nan Liu @ Liangzhu Laboratory, Zhejiang University School of Medicine
- **日期**: 2026-10-14
- **ID**: DOI: 10.64898/2026.10.11.756618  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.11.756618v1
- **相关分数**: 8/10
- **一句话推荐**: 基于Borzoi基因组Transformer从DNA序列直接预测跨细胞类型的超级增强子，核心属于sequence-to-function和细胞类型特异性增强子调控。
- **方法**: 基于预训练基因组Transformer（Borzoi）构建深度学习框架，将超级增强子发现转化为跨多细胞类型的分层序列目标检测任务。
- **主要发现**: 模型直接从长程DNA序列解码超级增强子调控语法，揭示共享增强子的谱系依赖性motif用法，并能在无变异标签训练下精准预测致病性功能获得性非编码变异。
- **对我的启发**: 将增强子活性预测重构为跨细胞类型的分层目标检测任务，可能比直接回归虚拟表观遗传特征更能捕捉调控层级；同时利用in silico ablation解析增强子内部组件功能层级的方法可直接迁移至评估游离型增强子活性。

<details><summary>Abstract</summary>

Super-enhancers (SEs) drive cell-identity gene expression, yet their identification relies on epigenomic profiling (e.g., H3K27ac ChIP-seq), precluding discovery in unprofiled cellular states and leaving their underlying sequence grammar unknown. Here, we present Borzoi-SE, a deep learning framework built upon the genomic transformer Borzoi that formulates SE discovery as hierarchical, cell-type-resolved genomic object detection directly from long-range sequence across 90 human lineages. Base-resolution attribution recovers lineage-defining master transcription factors across cell types. Within SEs shared across lineages, it reveals lineage-dependent motif usage, suggesting that the same regulatory regions can support distinct cell-type-specific programs. Using in silico ablation, Borzoi-SE decoded the functional hierarchy of the {beta}-globin super-enhancer, prioritizing hypersensitive site 2 (HS2) as the dominant constituent, which we experimentally verified via CRISPR interference. Trained without variant-effect labels, Borzoi-SE identified gain-of-super-enhancer variants in different tissues. At the CHRM2 locus, a single-nucleotide variant created a de novo glucocorticoid receptor (GR) motif that recruited activated GR and potentiated adjacent MEF2 regulatory syntax, nucleating a cardiac super-enhancer. Orthogonal multi-omics and population-genetic evidence linked this variant to increased CHRM2 expression and variation in resting heart rate and PR-interval duration. Borzoi-SE establishes a general framework for decoding SE regulatory grammar and prioritizing causal non-coding variants directly from sequence.

</details>

---

## 3. PlantGeneAnn: a high-accuracy ab initio plant gene annotation tool fine-tuned from a genome foundation model

- **期刊**: bioRxiv
- **作者**: Qizhe, Z., Zhengyang, Z., Kepeng, L., Wang, J., Kaixuan, D., Wei, X., Qing-Yong, Y., Xuehai, H.
- **机构**: Hu Xuehai @ Huazhong Agricultural University
- **日期**: 2026-10-14
- **ID**: DOI: 10.64898/2026.06.25.733695  |  URL: https://www.biorxiv.org/content/10.64898/2026.06.25.733695v1
- **相关分数**: 7/10
- **一句话推荐**: 基于基因组基础模型微调的植物基因注释工具，直接涉及DNA语言模型和表征学习。
- **方法**: 结合 Mamba-MoE DNA 编码器、U-Net 嵌入解码器与半马尔可夫解码的基因组基础模型微调范式。
- **主要发现**: 该模型在植物从头基因注释任务上达到 SOTA，且通过 LoRA 微调能以少量数据显著提升分布外物种性能，同时大幅降低内存消耗。
- **对我的启发**: 其利用 LoRA 微调以少量数据实现跨物种泛化的策略，可启发我针对不同细胞类型增强子活性预测的低资源微调；Mamba 架构的低内存特性也为处理长序列及 padding 问题提供参考。

<details><summary>Abstract</summary>

Structural annotation remains a bottleneck for translating the growing catalog of high-quality plant genomes into biological insights, as current pipelines rely on RNA-seq and homologous protein evidence that are often unavailable for non-model species. Existing ab initio tools are constrained by model scale and perform poorly in complex plant genomic regions. We present PlantGeneAnn, a plant-optimized ab initio gene annotation tool fine-tuned from a genome foundation model. It combines a Mamba-MoE DNA encoder with a U-Net-style embedding decoder and a semi-Markov decoding pipeline. Trained on 40 angiosperm species, PlantGeneAnn establishes a new state-of-the-art (SOTA) across a stringent 20-species benchmark, significantly outperforming Helixer, Tiberius, and ANNEVO at exon-, intron-, and locus-levels, with mean F1 scores of 0.856, 0.880, and 0.707, respectively. It also enables efficient customized fine-tuning: LoRA fine-tuning increased the locus-level F1 of the out-of-distribution bryophyte Physcomitrium patens from 0.581 to 0.736, with performance plateauing at 40% of the fine-tuning data. Notably, PlantGeneAnn requires substantially lower peak memory usage than other baseline tools, allowing annotation of large plant genomes on standard personal workstations. PlantGeneAnn thus provides accurate, hardware-friendly ab initio annotation for diverse plant genomes, particularly newly assembled genomes, population-scale projects, and non-model plants.

</details>

---
