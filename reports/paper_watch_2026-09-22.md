# Paper Scout 日报 2026-09-22

共筛选出 **4** 篇推荐论文。
📊 抓取 biorxiv 72/pubmed 18 → 粗筛 35 篇 → LLM 选中 4 篇

## 1. miRstring: An RNA language model enables mature miRNA decoding and artificial small RNA design across species

- **期刊**: bioRxiv
- **作者**: Peng, R., Li, X., fang, t., Yu, X.
- **机构**: Xiang Yu @ Shanghai Jiao Tong Unviversity
- **日期**: 2026-09-20
- **ID**: DOI: 10.64898/2026.09.17.752258  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.17.752258v1
- **相关分数**: 7/10
- **一句话推荐**: 使用RNA语言模型进行序列到功能预测（miRNA边界解码）和人工小RNA设计，与DNA语言模型和增强子设计思路高度契合。
- **方法**: 基于注意力机制的RNA语言模型，用于从前体序列预测成熟miRNA的边界位点。
- **主要发现**: 该模型在跨物种miRNA解码任务上超越现有方法，其注意力机制成功捕捉到核酸内切酶切割位点的生物学特征，并能有效指导人工miRNA设计。
- **对我的启发**: 模型利用注意力机制定位关键生物学切割位点的方法，可启发我在增强子活性预测中通过注意力权重来解释虚拟表观遗传特征对序列功能的具体贡献。

<details><summary>Abstract</summary>

MicroRNAs (miRNAs) are processed from structured precursors and subsequently loaded into Argonaute proteins to repress target mRNAs. Yet generalized computational frameworks capable of decoding mature miRNAs from precursor context remain limited, constraining both cross-species annotation and rational artificial miRNA design. Here, we present miRstring, a biogenesis-aware RNA language framework that decodes the four boundaries defining the miRNA/miRNA duplex. Trained on 77,708 miRNA precursors spanning 414 species, miRstring outperforms existing methods under family- and species-held-out evaluations and accurately identifies the first nucleotide of mature miRNAs. Importantly, its attention mechanism highlights the miRNA/ miRNA* boundary sites cleaved by endonucleases, indicating that the model captures biologically meaningful features. Furthermore, we employed miRstring to design optimal pre-miRNA scaffolds for artificial miRNAs and validated its efficacy in repressing target mRNAs. Taken together, miRstring establishes a scalable route from cross-species mature-miRNA annotation to predictive design, enabling artificial intelligence-driven miRNA engineering and extending computational miRNA analysis toward broadly applicable small-RNA biotechnology.

</details>

---

## 2. High-order enhancer hubs buffer allelic regulatory variation through kinetic compensation

- **期刊**: bioRxiv
- **作者**: Tan, J., Sentmanat, M., Wu, Y. et al. (11 authors)
- **机构**: Yidan Sun @ Washington University in St. Louis
- **日期**: 2026-09-21
- **ID**: DOI: 10.64898/2026.09.14.750771  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.14.750771v1
- **相关分数**: 5/10
- **一句话推荐**: 研究增强子枢纽如何缓冲调控变异，涉及单细胞动力学建模，对理解增强子活性和变异效应有启发。
- **方法**: 结合长读长 Nanopore-HiChIP 技术与单细胞动力学建模，解析单倍型水平的高阶增强子枢纽结构及转录动力学。
- **主要发现**: 高阶增强子枢纽通过转录爆发频率与爆发大小的反向动力学补偿，缓冲等位基因间的顺式调控变异，维持剂量敏感基因的转录平衡。
- **对我的启发**: 在构建增强子活性预测模型时，可将转录爆发动力学（频率与大小）作为虚拟表观遗传特征或中间预测目标，以捕捉序列变异下的表达鲁棒性。

<details><summary>Abstract</summary>

Diploid genomes carry millions of heterozygous variants in cis-regulatory DNA, yet most genes produce similar RNA output from two parental alleles. How this balance is maintained is unclear. We developed Nanopore-HiChIP, a long-read method that maps high-order enhancer hubs on each haplotype. Over half of these enhancer hubs differ in chromatin architecture and transcription-factor occupancy between homologous chromosomes, but their target genes show substantially lower rates of allele-specific expression than genes lacking hub regulation. Single-cell kinetic modeling shows that burst frequency and burst size change in opposite directions, thereby preserving balanced transcriptional output. This hub-mediated kinetic buffering is enriched at haploinsufficient genes and coincides with smaller effects of expression quantitative trait loci. Enhancer hubs therefore absorb allelic regulatory variation through kinetic compensation, protecting dosage-sensitive transcription.

</details>

---

## 3. Measurement reliability bounds functional benchmarks and relocates where variant effect prediction fails

- **期刊**: bioRxiv
- **作者**: Zhang, N.
- **机构**: Ningyi Zhang @ Department of Biological Sciences, National University of Singapore
- **日期**: 2026-09-20
- **ID**: DOI: 10.64898/2026.09.14.751496  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.14.751496v1
- **相关分数**: 5/10
- **一句话推荐**: 变异效应预测的基准测试方法论，对评估基因组基础模型在变异预测任务上的性能上限和真实失败区域有方法论启发。
- **方法**: 基于饱和基因组编辑数据的重复样本与标准误，估计各基因组区域的测量可靠性上限，并以此校正变异效应预测器的基准测试。
- **主要发现**: 测量可靠性上限在不同基因组区域间差异显著，校正后重新定义了预测失败的位置（真正的失败位于内含子11-50 bp处），且预测器在分类任务中的区分能力优于相关性指标所暗示的水平。
- **对我的启发**: 在评估预训练基因组学模型对增强子活性预测的基准表现时，应考虑下游实验测定（如MPRA/STARR-seq）在不同细胞类型或基因组上下文中的测量可靠性上限，避免将实验噪声误判为模型预测失败。

<details><summary>Abstract</summary>

Background. Variant effect predictors are increasingly benchmarked against multiplexed assays of variant effect (MAVEs) rather than clinical labels, which removes label circularity but introduces a new problem: a correlation against a measurement cannot exceed the measurement's own reproducibility, and precision varies sharply across the territories compared. Results. We scored nineteen predictors across sixteen strata of a frozen atlas of 64,178 saturation genome editing variants in seven cancer-susceptibility genes. From published replicate scores and standard errors we estimated each territory's reliability ceiling, and showed by simulation that the correction reduces error above a ceiling of about 0.45 and amplifies it below. Ceilings vary more across territory than predictors do, and correcting for them redraws the map at the splice extremes. The collapse at canonical splice sites is largely a property of the assay: the median shortfall relative to coding narrows from 1.7- to 1.4-fold; this convergence survives dropping BARD1 or PALB2 but inverts when BRCA1 is dropped, so we report all three leave-one-gene-out folds rather than claim gene independence, and the frontier parity rests on one deposit. Genuine failure lies 11-50 bp into the intron, which the uncorrected map presents as modest. Across MaveDB, 2,452 of 2,803 score sets carry, at the upper bound, what a reliability estimate needs, though a conventional column-name search finds only a tenth; among 674 human deposits with a computable ceiling, 29.9-51.8% fall below 0.90. Scored as classification against the assays' own functional calls in three genes, the same predictors separate damaging from tolerated better than their correlations suggest, though none reaches the strongest evidence band at the 95%-specificity operating point. Conclusions. Territory-resolved benchmarks should report a per-stratum reliability estimate, or state that the assay permits none. It asks nothing of depositors and applies today, at the upper bound, to most (87%) of MaveDB.

</details>

---

## 4. SMORE: joint dimension reduction and cell population discovery on single-cell methylome data

- **期刊**: bioRxiv
- **作者**: Deng, J., Wang, Z., Tang, W., Hu, G., Feng, H.
- **机构**: Hao Feng @ The University of Texas Health Science Center at Houston
- **日期**: 2026-09-20
- **ID**: DOI: 10.64898/2026.09.14.751514  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.14.751514v1
- **相关分数**: 4/10
- **一句话推荐**: 涉及单细胞DNA甲基化数据的表示学习与降维，与表观基因组特征分析有间接联系。
- **方法**: 基于贝叶斯框架的低秩潜在高斯分解与有限混合物先验，实现单细胞甲基化数据的联合降维与无预设聚类数的细胞群体发现。
- **主要发现**: 该方法通过将甲基化比例转化为有序状态并传播测量不确定性，在多种模拟和真实数据集中准确恢复了细胞群体结构，显著优于现有降维聚类方法。
- **对我的启发**: 其将连续表观比例转化为有序状态并传播测量不确定性的思路，可启发在构建虚拟表观遗传特征时如何处理稀疏甲基化信号并量化下游增强子活性预测的置信度。

<details><summary>Abstract</summary>

Single-cell DNA methylation profiling technology captures novel epigenetic data modality but are challenging to analyze because of their heterogeneity, high dimensionality, and ultra-sparsity. Here we present SMORE (Single-cell MethylOme Reduction and Embedding), a computational method for joint dimensionality reduction and cell population discovery dedicated to single-cell DNA methylation data. SMORE operates on a Bayesian framework that converts methylation proportions into ordered methylation states and jointly infers a low-dimensional representation, cell populations and their number. By using low-rank latent Gaussian factorization and adopting a mixture-of-finite-mixtures prior on latent cell scores, SMORE infers cell assignments without requiring a prespecified cluster number, and propagates uncertainty from methylation measurements to cell assignments. Across simulations spanning varying sample sizes, population imbalance, signal strengths and model misspecification, SMORE accurately recovered latent population structure and outperformed existing methods. Applied to human single-cell methylation datasets from lung, peripheral blood and primary motor cortex, SMORE recovered biologically supported cell population structures. SMORE provides an uncertainty-aware framework for dimension reduction and population discovery for single-cell methylomes.

</details>

---
