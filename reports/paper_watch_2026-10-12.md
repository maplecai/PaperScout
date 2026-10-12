# Paper Scout 日报 2026-10-12

共筛选出 **4** 篇推荐论文。
📊 抓取 biorxiv 122/pubmed 33 → 粗筛 34 篇 → LLM 选中 4 篇

## 1. Spatiotemporal AI modeling of gene regulation and variant effects in the developing human brain

- **期刊**: bioRxiv
- **作者**: Hao, Y., Park, C. Y., Theesfeld, C. T., Troyanskaya, O. G.
- **机构**: Olga G Troyanskaya @ Flatiron Institute, Simons Foundation; Princeton University
- **日期**: 2026-10-11
- **ID**: DOI: 10.64898/2026.10.09.757610  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.09.757610v1
- **相关分数**: 8/10
- **一句话推荐**: 基于序列的AI模型预测跨细胞类型基因表达和变异效应，与你的sequence-to-function和跨细胞类型调控预测高度相关。
- **方法**: 提出Seal，一种基于基因组序列的可解释AI迁移学习框架，用于跨脑区、细胞类型和发育阶段的时空基因表达与变异效应建模。
- **主要发现**: 该模型有效克服了瞬时细胞类型数据稀缺问题，成功预测了基因表达与变异效应，并揭示了神经精神疾病风险相关的特定细胞类型、发育窗口及调节性变异负荷。
- **对我的启发**: Seal利用迁移学习克服瞬时细胞类型数据稀缺的策略，启发我在预测不同细胞类型游离型增强子活性时，可利用预训练基因组学模型提取虚拟表观遗传特征，以弥补特定细胞类型的训练数据不足。

<details><summary>Abstract</summary>

Understanding how genetic variation shapes gene regulation in the developing human brain remains a central challenge in neuroscience, particularly in transient cell types and developmental stages where data are limited. We present Seal, an interpretable AI transfer learning framework for genome-based modeling of gene expression and variant effects with spatiotemporal resolution across 26 brain regions, 30 cell types, and seven developmental stages. Seal predictions enable characterization of both germline and somatic brain variants, and provide mechanistic interpretation by linking sequence variants to transcriptional regulators in spatiotemporal context. Applying Seal to genome-wide association studies, we identify cell types and developmental windows relevant to neuropsychiatric disease risk, revealing shared and distinct regulatory architectures across six neuropsychiatric conditions that align with clinical trajectories. In the Simons Simplex Collection autism cohort whole genome data, Seal uncovers a significant burden of de novo regulatory variants in transient fetal excitatory neurons, revealing a cell-type and developmentally specific regulatory burden. By connecting genetic variation to spatiotemporal regulatory programs, Seal offers a general framework for uncovering mechanisms of human brain development and disease.

</details>

---

## 2. A unified framework for quantitative splicing and transcript prediction

- **期刊**: bioRxiv
- **作者**: Jaganathan, K., Chen, J., Liu, X. et al. (19 authors)
- **机构**: Kishore Jaganathan @ Illumina, Inc.
- **日期**: 2026-10-11
- **ID**: DOI: 10.64898/2026.10.08.757673  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.08.757673v1
- **相关分数**: 8/10
- **一句话推荐**: SpliceAI2是直接从基因组序列预测剪接和转录本的深度学习模型，属于sequence-to-function范式，与你的研究兴趣高度契合。
- **方法**: SpliceAI2，一种跨物种多任务端到端深度学习模型，直接从基因组序列联合预测剪接位点、剪接连接及转录本丰度。
- **主要发现**: 该模型显著提升了剪接变异的识别与定量精度，并在罕见病队列中发现约15%的遗传负荷源于外显子测序易遗漏的深层内含子剪接变异。
- **对我的启发**: 其跨物种多任务端到端训练范式（联合预测局部位点与全局转录本丰度）可启发我将局部增强子序列特征与全局细胞类型特异性活性预测整合至单一模型中。

<details><summary>Abstract</summary>

RNA splicing is frequently disrupted by genetic variation, contributing to a wide range of human diseases. Identifying the variants responsible for altered splicing is therefore crucial but has long been challenging. Deep learning models that predict splicing from genomic sequence have substantially advanced their detection, but accurately resolving their quantitative effects on splicing and the resulting transcripts remains an unmet need. Here we introduce SpliceAI2, a deep learning model trained end-to-end on splice site, splice junction, and transcript usage across multiple mammalian species. SpliceAI2 reconstructs complete transcripts directly from genomic sequence and considerably improves identification of splice-altering variants and quantification of their effects in diverse benchmarks spanning cryptic splicing, splicing quantitative trait loci, and massively parallel reporter assays. Human population datasets provide independent validation of these predicted functional effects through evidence of natural selection and associated changes in plasma protein abundance. Application to a rare disease cohort reveals that predicted splice-altering variants are highly enriched in disease-associated genes and account for 15% of the excess genetic burden, with approximately half residing in deep intronic regions likely missed by exome sequencing. Together, these findings establish SpliceAI2 as a major step forward in interpreting splice-altering variants across the human genome.

</details>

---

## 3. CRISCross: Integration of Epigenetic Information for Deep-Learning-Based Prediction of CRISPR-Cas9 Off-Targets Across Cell Types

- **期刊**: bioRxiv
- **作者**: Jobson Pargeter, W., Rabsch, D., Kaufmann, M. M. et al. (9 authors)
- **机构**: Rolf Backofen @ Bioinformatics Group, Department of Computer Science, University of Freiburg
- **日期**: 2026-10-11
- **ID**: DOI: 10.64898/2026.10.09.757843  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.09.757843v1
- **相关分数**: 7/10
- **一句话推荐**: 跨细胞类型表观遗传特征整合与序列交互建模，直接关联我'跨细胞类型增强子活性预测'项目的方法论需求。
- **方法**: 提出基于交叉注意力机制的CRISCross模型，在核苷酸水平捕获序列与表观遗传特征的交互，并结合合成预训练策略学习跨细胞类型的可迁移表征。
- **主要发现**: 表观遗传特征对跨细胞类型预测的增益依赖于其与序列特征的早期交互建模而非晚期融合；使用预测的染色质可及性作为虚拟特征可有效提升模型在无实验数据场景下的泛化性。
- **对我的启发**: 在增强子活性预测中，虚拟表观遗传特征应通过交叉注意力等机制在序列分辨率上与DNA序列深度交互建模，而非作为独立信号晚期融合，以提升跨细胞类型的泛化能力。

<details><summary>Abstract</summary>

CRISPR-Cas9 enables precise genome editing but remains limited by off-target effects, raising safety concerns and necessitating accurate prediction. Although epigenetic features influence Cas9 binding and cleavage, their predictive signals are often weak, highlyvariable, and context-dependent, limiting the effectiveness of existing machine learning approaches. Cross-cell-type settings are especially challenging: epigenetic landscapes differ substantially, and models trained on one cell type frequently fail to generalize. Here, we systematically investigate the role of epigenetic context in off-target prediction and demonstrate that its utility depends on modeling interactions with sequence features rather than treating it as an independent signal. Tabular and deep learning experiments demonstrate that epigenetic features provide a consistent but modestly complementary signal, and that late-stage fusion strategies are insufficient to effectively exploit this information. To address this, we introduce CRISCross, a cross-attention-based architecture that captures sequence-epigenetic interactions at the nucleotide level, alongside CRISPRAT, a synthetic pretraining strategy that learns transferable representations from genome-derived sgRNA-off-target pairs without relying on dataset-specific pretraining. CRISCross, incorporating AlphaGenome-derived chromatin accessibility signals, shows better predictive performance than sequence-only baselines across three independent test datasets spanning two cell types, demonstrating improved generalization across guide RNAs, datasets, and cellular contexts. This is particularly relevant for therapeutic applications involving cell types or patient-derived contexts that lack dedicated experimental datasets. In such settings, predicted chromatin accessibility may provide scalable contextual information when direct epigenomic profiling is unavailable or impractical. Together, these results show that accurate CRISPR off-target prediction benefits from interaction-aware integration of epigenetic context alongside generalizable pretraining strategies.

</details>

---

## 4. GLARE: Genomic Language model for Automated Repetitive Element classification

- **期刊**: bioRxiv
- **作者**: Haas, N., Bruna, T.
- **机构**: Tomas Bruna @ DOE Joint Genome Institute, Lawrence Berkeley National Laboratory
- **日期**: 2026-10-11
- **ID**: DOI: 10.64898/2026.10.06.757139  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.06.757139v1
- **相关分数**: 6/10
- **一句话推荐**: 微调基因组语言模型（Nucleotide Transformer）并评估跨分类群泛化能力，与我的DNA语言模型/基因组基础模型兴趣间接相关。
- **方法**: 基于Nucleotide Transformer v3预训练基因组语言模型微调的转座元件分类器。
- **主要发现**: 在多源整合参考数据上微调后，模型在跨分类群、跨数据库及序列退化等分布偏移场景下均展现出卓越的泛化能力和鲁棒性。
- **对我的启发**: 借鉴其对不同预训练基因组语言模型的对比评估及模拟序列退化测试鲁棒性的范式，可用于评估增强子活性预测模型在不同padding长度或序列截断下的性能稳定性。

<details><summary>Abstract</summary>

Reliable classification of transposable elements (TEs) is important for genome annotation and evolutionary analysis, yet remains challenging: TE families differ widely across taxa, reference databases label them inconsistently, and many TEs are represented only by degraded copies. We introduce GLARE (Genomic Language model for Automated Repetitive Element classification), a TE classifier built by fine-tuning a genomic language model on harmonized PanTEon and Repbase reference data to predict TE superfamily across 32 superfamilies in 11 orders. Among the genomic language models compared, Nucleotide Transformer v3 provided the strongest representation. Built on this backbone, GLARE exceeded all nine classifiers in the PanTEon benchmark, reaching 0.966 weighted superfamily F1 on its 30-superfamily task. GLARE also showed stronger generalization to clades absent from training, consistently exceeding state-of-the-art classifiers on holdouts spanning three taxonomic ranks: the order Poales, the phylum Arthropoda, and the kingdom Fungi. Training on both PanTEon and Repbase reduced the performance drop seen when a single-source model was applied to the other database. Under simulated sequence decay, GLARE was the most robust classifier tested, and it performed best on independently curated degraded libraries. These findings show that genomic language models fine-tuned on harmonized multi-source references can classify TEs robustly under the taxonomic, database, and sequence-quality shifts that matter in practice. GLARE is available at https://code.jgi.doe.gov/NHaas/glare.

</details>

---
