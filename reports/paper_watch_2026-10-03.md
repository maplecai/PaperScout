# Paper Scout 日报 2026-10-03

共筛选出 **5** 篇推荐论文。
📊 抓取 biorxiv 123/pubmed 252 → 粗筛 95 篇 → LLM 选中 5 篇

## 1. Applying AlphaGenome Variant Impact for SNV Prioritization

- **期刊**: bioRxiv
- **作者**: Qu, H.-Q., Hakonarson, H.
- **机构**: Hakon Hakonarson @ Children's Hospital of Philadelphia
- **日期**: 2026-10-01
- **ID**: DOI: 10.64898/2026.09.26.754650  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.26.754650v1
- **相关分数**: 7/10
- **一句话推荐**: 直接应用并评估了AlphaGenome的变异效应预测分数，与你的代表性论文及调控变异预测兴趣相关。
- **方法**: 基于ROC分析与Youden指数校准AlphaGenome变异影响预测分数（AVI）的临床分类阈值。
- **主要发现**: 确定了区分致病/良性SNV的全局AVI阈值（0.9938），并证实该预训练模型的功能预测信息与统计精细定位（SuSiE）信号相互正交。
- **对我的启发**: 预训练模型在非编码区预测的阈值偏低，提示在评估游离型增强子活性等非编码功能时需建立特定置信度阈值，且模型提取的序列功能特征可与传统统计遗传学信号互补使用。

<details><summary>Abstract</summary>

AlphaGenome Atlas, released in September 2026, provides functional predictions for nearly all possible human single-nucleotide variants using the AlphaGenome Variant Impact (AVI) score. However, empirical thresholds relating AVI quantile rank (AVI_QUANTILE) to clinical variant classifications have not been established. We derived AVI_QUANTILE thresholds distinguishing ClinVar pathogenic, likely pathogenic, uncertain, conflicting, likely benign, and benign SNVs using receiver operating characteristic analyses. Pathogenic/likely pathogenic variants were strongly enriched at the upper end of the AVI_QUANTILE distribution, yielding a Youden-optimal ClinVar-derived cutoff of 0.9938. Optimal cutoffs were generally consistent across several major molecular consequence classes, although lower thresholds were observed for selected noncoding categories. Similarly, most well-powered gene-disease groups showed cutoffs close to the global threshold, with modest gene-specific variation. Among 24,989 variants of uncertain significance, 11,357 (45.45%) exceeded the global cutoff, identifying a substantial subset with AlphaGenome-predicted functional effects comparable to those observed among pathogenic/likely pathogenic variants and potentially warranting further evaluation. In a steroid-dependent asthma fine-mapping analysis, AVI_QUANTILE showed little correspondence with SuSiE posterior inclusion probabilities, indicating that AlphaGenome functional predictions capture information distinct from statistical fine-mapping.

</details>

---

## 2. snpXplorer: haplotype-block representation of GWAS signals for integrated variant and cross-trait interpretation

- **期刊**: bioRxiv
- **作者**: Tesi, N., Green, G. S., Salazar, A., van der Lee, S. J., Hulsman, M., Holstege, H., Reinders, M.
- **机构**: Niccolo' Tesi @ Amsterdam University Medical Center
- **日期**: 2026-10-02
- **ID**: DOI: 10.64898/2026.07.20.739485  |  URL: https://www.biorxiv.org/content/10.64898/2026.07.20.739485v1
- **相关分数**: 5/10
- **一句话推荐**: 该工具整合了AlphaGenome等功能预测分数用于GWAS变异解释，与调控变异效应预测有一定关联。
- **方法**: 基于重组率与成对LD聚类预计算单倍型块，并结合预训练生物医学语言嵌入聚类表型描述，构建多尺度GWAS信号整合与跨性状解释的交互式平台。
- **主要发现**: 以单倍型块为单位聚合GWAS信号与功能注释，能有效揭示跨性状的协同与拮抗多效性，并大幅降低大规模GWAS库的表型冗余度。
- **对我的启发**: 无明显直接启发。

<details><summary>Abstract</summary>

Genome-wide association studies (GWAS) have identified thousands of loci associated with complex traits, yet translating these signals into biological insight remains challenging: most associated variants are non-coding and lie within linkage disequilibrium (LD) blocks, so interpretation requires functional and cross-trait evidence assembled within haplotypic context. We present an extended version of snpXplorer, an interactive web platform that represents GWAS signals at the haplotype-block level rather than at the variant level. Haplotype-blocks are precomputed genome-wide by partitioning the genome on recombination rate and clustering variants by pairwise LD across European or African ancestries, aggregating association signals, annotations and phenotype associations onto inherited units of variation. The platform incorporates more than 11,000 European and African GWAS datasets from OpenGWAS and enables multi-scale analysis across variants, haplotype-blocks, genes and traits, integrating clinical annotations (ClinVar), allele frequencies (gnomAD), functional predictions (CADD, AlphaGenome), quantitative trait loci (GTEx), structural variation and reported GWAS associations within a single unified interface. Redundancy across closely related phenotypes is reduced by clustering trait descriptions with pretrained biomedical language embeddings, making navigation across large GWAS repositories tractable. Applied to Alzheimer's disease, snpXplorer identified a haplotype-block at the TMEM106B locus linked to eight distinct traits, revealing synergistic pleiotropy across neurological and behavioral phenotypes alongside antagonistic pleiotropy with height. The platform additionally exports PRS-ready variant sets, at user-selected p-value thresholds, for every ingested GWAS. By combining haplotype-aware representation, integrated variant annotation and cross-trait exploration, snpXplorer reduces the need for fragmented queries across databases and lowers the barrier to biological interpretation of GWAS results.

</details>

---

## 3. Dataset structure outweighs method choice in single-cell cell-type annotation

- **期刊**: bioRxiv
- **作者**: Wardhana, O.
- **机构**: Oliver Wardhana @ University of Notre Dame
- **日期**: 2026-10-02
- **ID**: DOI: 10.64898/2026.08.28.747622  |  URL: https://www.biorxiv.org/content/10.64898/2026.08.28.747622v1
- **相关分数**: 5/10
- **一句话推荐**: 系统评估了包括transformer基础模型在内的多种单细胞注释工具，与虚拟细胞和基础模型评估间接相关。
- **方法**: 采用Taguchi正交阵列实验设计结合k近邻纯度评估，对跨七大方法家族的63种单细胞注释工具进行受控变量基准测试。
- **主要发现**: 数据集结构（细胞类型在嵌入空间的分离度）对注释准确率的解释方差远超工具选择（84% vs 4%）；当信号噪声大时，模型复杂度无法弥补数据本身的局限性。
- **对我的启发**: 在评估预训练基因组学模型预测增强子活性时，应优先考察不同细胞类型虚拟表观遗传特征在模型嵌入空间的内在分离度，而非单纯依赖调整padding策略或增加模型复杂度来提升预测效果。

<details><summary>Abstract</summary>

Automated cell-type annotation is a prerequisite for nearly all single-cell RNA-sequencing (scRNA-seq) analysis, and the proliferation of annotation tools -- spanning marker-based, similarity-based, classical machine-learning, deep-learning, semi-supervised, large language model (LLM), and transformer foundation-model families -- has exceeded any existing guidance on how to select among them. Existing benchmarks utilize convenient, well-known datasets in which cell number, class imbalance, cell-type number, and differential-expression strength vary concurrently, so performance cannot be attributed to any dataset property. We benchmarked 63 tools from seven families using a Taguchi L9(34) orthogonal array that varied these four properties independently and extended the comparison under more realistic conditions: real data, cross-platform transfer, public marker databases, LLM annotation, and fine-tuned foundation models. With standardized preprocessing and inputs, the leading cell-level families performed within 0.06 {kappa} of one another, and fine-tuned foundation models averaged only slightly higher. Across families, sequencing platforms, and data types, accuracy was predicted near-linearly by how separable cell types were in a shared expression embedding space, measured as k-nearest-neighbor (kNN) purity (R2 = 0.85-0.99). We found that dataset identity accounted for {approx}84% of {kappa} variance while tool identity accounted for {approx}4%. Strong performers were distributed across families, for example, Seurat label transfer and singleCellNet among reference-based classifiers and mLLMCelltype among LLM annotators. When cell types cleanly separate, many annotation methods suffice; when they do not, algorithmic complexity struggles to compensate for noisy signal. Method selection should therefore prioritize available resources, such as curated references and compute availability, over sophisticated modeling.

</details>

---

## 4. GGE: General-purpose deep meta-learning for classification of human transcriptomes with limited data

- **期刊**: bioRxiv
- **作者**: Yankovitz, G., Gat-Viks, I.
- **机构**: Irit Gat-Viks @ Tel-Aviv University
- **日期**: 2026-10-02
- **ID**: DOI: 10.64898/2026.09.27.754054  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.27.754054v1
- **相关分数**: 5/10
- **一句话推荐**: 使用深度元学习跨数据集学习转录组分类的通用初始化，对跨细胞类型泛化或虚拟细胞建模思路有一定启发。
- **方法**: 基于跨数千个转录组分类任务的深度元学习框架，学习具有强泛化能力的模型初始化。
- **主要发现**: 跨任务元学习预训练的模型初始化在小样本转录组分类任务上显著优于传统分类器，且能通过注意力机制揭示跨任务的共享关键基因。
- **对我的启发**: 利用跨任务元学习获取强泛化模型初始化的范式，可启发在预测不同细胞类型增强子活性时，通过元学习跨多细胞类型的序列到功能映射，缓解特定细胞类型标注数据稀缺问题。

<details><summary>Abstract</summary>

Transcriptomic classification is often hindered by the small number of samples relative to the high dimensionality of gene expression data. We introduce General Gene Expression (GGE), a deep meta-learning framework designed to support robust classification in this limited-sample setting. By training across 5,220 distinct biomedical prediction objectives drawn from 1,779 different human datasets, GGE learns a model initialization that captures biological patterns shared across heterogeneous classification tasks. This learned initialization has two key advantages. First, it enables improved performance to new datasets using only a small number of labeled samples. Second, because it is learned across diverse prediction objectives, it can be applied to a broad range of biomedical problems. We show that GGE outperforms established classifiers in data-limited settings across a wide range of applications, including datasets generated using different RNA-seq platforms and preprocessing pipelines. In addition, attention-based analysis identifies recurrent genes that contribute to performance across multiple biological objectives, providing insight into shared determinants of human biological states. Together, these results establish GGE is a general-purpose framework for human transcriptome-based classification in biomedical settings where labeled data are scarce.

</details>

---

## 5. LOL: a Python package for leakage-aware phenotype prediction and confounding diagnostics in GEO transcriptomics datasets

- **期刊**: bioRxiv
- **作者**: Muigano, M. N.
- **机构**: Martin Nganga Muigano @ Bio One Scientific Ltd
- **日期**: 2026-10-01
- **ID**: DOI: 10.64898/2026.09.26.754596  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.26.754596v1
- **相关分数**: 3/10
- **一句话推荐**: 关注转录组表型预测中的数据泄露和混杂诊断，对评估基因组模型泛化性有间接方法论启发。
- **方法**: 提出LOL（Latent Omics Learning）Python包，采用防泄漏预处理、类不平衡感知评估和组感知验证的表型预测工作流范式。
- **主要发现**: 该工作流通过泄漏膨胀指数和PVCA-lite等诊断指标，能有效识别并量化转录组学表型预测中的信息泄漏、类不平衡及混杂因素，从而区分稳健预测与需进一步审查的结果。
- **对我的启发**: 在评估预训练基因组学模型预测增强子活性时，可借鉴其防泄漏验证和混杂因素诊断思路（如检查潜在表示与批次或细胞类型协变量的关联），以排除因数据划分不当或混杂特征导致的虚高预测性能。

<details><summary>Abstract</summary>

Phenotype prediction from public gene-expression data is straightforward to implement but reliable prediction is harder. Leakage during feature selection can inflate performance estimates. Class imbalance can hide poor performance in minority classes. Confounds like tissue type, repeated sampling, and demographic differences can also create patterns that resemble phenotype-associated biology. Here, I present LOL (Latent Omics Learning), a Python package for phenotype prediction from bulk GEO RNA-seq and microarray data. LOL uses leakage-safe preprocessing, imbalance-aware evaluation, and group-aware validation where repeated samples are present. Each analysis produces two audit diagnostics. The leakage inflation index ({Delta}LII) measures the change in performance between naive and leakage-safe evaluation. PVCA-lite examines associations between the latent representation and available metadata covariates, including phenotype. I evaluated the workflow across six independent GEO cohorts. The datasets covered microarray and RNA-seq platforms, binary and multi-class phenotypes, and sample sizes ranging from 18 to 566. The analyses produced a varied set of outcomes. Across diverse GEO datasets, LOL can reveal phenotype-associated expression patterns while identifying factors distort their interpretation. These include information leakage, class imbalance, repeated sampling, tissue differences, and demographic or other metadata-associated confounding. The resulting diagnostics help distinguish robust predictions from results that require further scrutiny. LOL does not introduce a new representation-learning algorithm. Its contribution is a reproducible workflow that places validation and diagnostic checks alongside prediction. The resulting analysis can expose weaknesses in an apparently convincing result and make those limitations visible. LOL is freely available under the MIT license from https://github.com/ngangao/lol-omics.

</details>

---
