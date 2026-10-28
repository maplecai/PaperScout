# Paper Scout 日报 2026-10-28

共筛选出 **4** 篇推荐论文。
📊 抓取 biorxiv 110/pubmed 55 → 粗筛 36 篇 → LLM 选中 4 篇

## 1. How Much Can AI Virtual Cells Gain from Unified Perturbational Modeling?

- **期刊**: bioRxiv
- **作者**: Wei, Z., Ye, Y., Cui, S., Ma, W., You, Y.
- **机构**: Yuning You @ School of Science and Engineering, The Chinese University of Hong Kong, Shenzhen (CUHK-Shenzhen)
- **日期**: 2026-10-27
- **ID**: DOI: 10.64898/2026.10.25.761625  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.25.761625v1
- **相关分数**: 8/10
- **一句话推荐**: 直接聚焦AI虚拟细胞的统一扰动建模，整合异质Perturb-seq数据集训练十亿参数预测器，高度匹配virtual cell和single-cell perturbation研究方向。
- **方法**: 提出统一扰动建模（UPM）范式，基于变分自编码器（VAE）引入基因通道对齐、共享扰动编码与联合嵌入模块，整合异构Perturb-seq数据训练超大规模虚拟细胞预测器。
- **主要发现**: 通过统一异构扰动数据训练的超10亿参数UPM模型，在跨环境的遗传扰动与组合扰动预测任务上均显著优于特定场景模型，并在下游HSC应用中实现40%的准确率提升。
- **对我的启发**: UPM中处理异构基因集的“基因通道对齐”模块，可为预训练基因组学模型在处理不同长度序列padding或跨细胞类型特征对齐时提供统一特征空间的方法借鉴。

<details><summary>Abstract</summary>

Predicting how individual cells respond to perturbations is a central task in artificial intelligence virtual cell (AIVC) modeling. However, integrating perturbation datasets is challenging because they differ in measured gene sets, perturbation types and cellular contexts. Existing AIVC predictors are typically developed for specific settings, limiting their applicability across heterogeneous datasets. Here, we investigate the extent to which AIVC predictors can benefit from unified perturbational modeling (UPM), a novel paradigm designed to integrate heterogeneous Perturb-seq datasets into a single predictive model. To this end, we introduce three unification modules into a variational autoencoder (VAE)-based AIVC predictor to address these sources of heterogeneity: gene-channel alignment, shared perturbation encoding, and joint embedding of gene expression and identity. We systematically evaluate and validate the individual contributions of these modules. Building on UPM, we assemble a dataset of 110 million cells spanning over 22,000 genes, four perturbation types and 76 cellular contexts, and use 89.7 million cells from 71 contexts to train a unified AIVC predictor with more than one billion parameters. Across genetic perturbation benchmarks, UPM achieves the highest PES and gene-wise response correlation among the evaluated models. It also improves all four evaluation metrics over State on the five held-out Tahoe-100M cell lines and over Stack on the cytokine benchmark. UPM also improves combinatorial perturbation prediction relative to specialized predictors. In the HSC application, our model achieves a 40.0% improvement in accuracy on a downstream task involving the recapitulation of effects induced by the knockdown of hepatic stellate cell (HSC)-related targets. Our implementation is openly available at https://github.com/youlab2025/UPM.

</details>

---

## 2. Mimic: A Unified Neural Network Architecture for Modelling Genomic Sequences and Module-level Comparison

- **期刊**: bioRxiv
- **作者**: Abdulnabi, H., Westwood, J. T.
- **机构**: Husam Abdulnabi @ University of Toronto
- **日期**: 2026-10-27
- **ID**: DOI: 10.64898/2026.10.26.761901  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.26.761901v1
- **相关分数**: 8/10
- **一句话推荐**: 统一NN架构框架用于比较基因组序列建模组件，直接在增强子活性（DeepSTARR）和蛋白-DNA相互作用上评测，与sequence-to-function和增强子预测高度相关。
- **方法**: 提出名为 Mimic 的统一神经网络架构，通过模块化拆解（k-mer嵌入、序列嵌入、输出映射）实现不同基因组学模型组件的原则性比较。
- **主要发现**: 发现特定序列嵌入组件能显著提升模型性能，且该架构在增强子活性预测任务上显著优于 DeepSTARR 等现有基线模型。
- **对我的启发**: Mimic 统一架构对变长序列的自适应性，可作为系统评估不同 padding 策略对预训练基因组学模型 sequence-to-function 预测性能影响的理想测试平台。

<details><summary>Abstract</summary>

There exist a wide range of Neural Networks (NNs) that have modelled genomic sequences well. The architectures of these NNs consist of three steps: k-mer embedding, sequence embedding, and output mapping. The NNs are primarily differentiated from one another by their sequence embedding components. Although different NNs have been compared before, these comparisons are often either limited or involve drastically different NNs. Another issue is that some NNs are configured for a specific sequence length, and different length sequences require manual modification of the architectures. This study examines the architectures of established NNs for genomics sequences. Based on these architectures, a novel NN called Mimic is developed that provides a unified architecture for the principled comparison of NN components. Mimic was used to model two different types of genomic datasets: protein-DNA interactions and enhancer activity. Along with other architecture components, different sequence embedding strategies were tried such as recurrent layers and convolutional layers. It was found that there exist specific NN components that yield significantly better performing models. Furthermore, Mimic significantly outperformed prevailing standard NNs, Bichrom and DeepSTARR, in modelling protein-DNA interactions and enhancer activity, respectively. This study provides a framework for more extensive studies toward a general prescription of NN architecture for modelling genomics data.

</details>

---

## 3. VarNexus: an integrative database for interpreting disease-associated regulatory variants through multimodal predictions and functional evidence.

- **期刊**: Nucleic acids research
- **作者**: Lihai Gong, Cheng Tan, Jinhui Zhang et al. (10 authors)
- **机构**: Ruofan Ding @ Institutes of Biomedical Sciences, Inner Mongolia University, Hohhot 010070, China.
- **日期**: 2026-10-27
- **ID**: DOI: 10.1093/nar/gkag1056  |  PMID: 42934171  |  URL: https://pubmed.ncbi.nlm.nih.gov/42934171/
- **相关分数**: 7/10
- **一句话推荐**: 整合AlphaGenome等sequence-to-function模型的预测与实验证据，直接涉及调控变异效应预测和增强子功能解读。
- **方法**: 构建整合序列到功能模型预测与实验/群体遗传学证据的多模态变异数据库系统。
- **主要发现**: 通过交叉链接AlphaGenome多模态预测、xQTL及MPRA实验数据，为疾病相关非编码调控变异的功能解释和优先排序提供了多层证据支持框架。
- **对我的启发**: 在评估预训练基因组学模型在增强子活性预测上的表现时，可利用该数据库的MPRA及单细胞xQTL实验数据作为外部基准，交叉验证虚拟表观遗传特征的预测可靠性。

<details><summary>Abstract</summary>

Genome-wide association studies (GWAS) have identified numerous loci associated with complex diseases and traits, yet the functional interpretation of non-coding risk variants remains challenging. Sequence-to-function models like AlphaGenome provide large-scale multi-modal predictions of variant effects, but their predictions lack direct experimental support. In contrast, empirical resources such as molecular quantitative trait loci (QTLs) and massively parallel reporter assays (MPRAs) offer population-based or experimental support for variant function, but suffer from limited genomic coverage. Here, we present VarNexus (https://biomed.imu.edu.cn/varnexus), an integrative resource for connecting disease-associated variants with predicted, population-based, and experimental evidence. VarNexus currently contains 230 404 fine-mapped candidate variants across 1891 disease-related phenotypes from UK Biobank and FinnGen. It integrates precomputed AlphaGenome predictions across 11 regulatory output types with bulk and single-cell xQTLs, MPRA measurements, and GWAS-eQTL colocalization results. VarNexus enables cross-linked searches by variant, phenotype, and gene, together with on-demand AlphaGenome prediction, multi-omics genome-browser visualization, and regulatory network exploration. By combining sequence-based predictions with population-based and experimental evidence, VarNexus provides a framework for prioritizing candidate regulatory mechanisms supported by multiple evidence layers.

</details>

---

## 4. BLOOM: Biologically Informed Flow Matching for Transcriptomic Virtual Embryo Modeling

- **期刊**: bioRxiv
- **作者**: Liang, Z., Li, S., Li, B., Huang, Y., Yu, L.
- **机构**: Lequan Yu @ The University of Hong Kong
- **日期**: 2026-10-27
- **ID**: DOI: 10.64898/2026.10.26.761895  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.26.761895v1
- **相关分数**: 6/10
- **一句话推荐**: 涉及virtual cell/embryo建模和单细胞扰动预测，与你的“virtual cell”和“single-cell perturbation”兴趣相关。
- **方法**: 结合生物学先验与时间群体上下文的条件流匹配生成模型，用于单细胞转录组时间序列的插值与外推。
- **主要发现**: 该模型在跨三个小鼠单细胞图谱的预测中超越22个基线，能准确恢复未测量时间点的发育表达动态，并支持基因扰动响应预测。
- **对我的启发**: 利用条件流匹配结合调控先验生成虚拟细胞状态的范式，可启发在预测不同细胞类型增强子活性时，将表观遗传调控先验作为条件输入来生成虚拟表观遗传特征。

<details><summary>Abstract</summary>

Constructing a virtual embryo requires a generative representation of how heterogeneous cell populations change across developmental time. Here we introduce BLOOM, a biologically informed framework for conditional generation of developmental cell populations. BLOOM integrates temporal population context with developmental and regulatory priors through conditional flow matching to generate cell-expression distributions at queried stages in either temporal direction. Evaluation spans three mouse single-cell atlases covering prenatal development, visual-cortex maturation and multi-organ endothelial specialization. In comparisons with 22 time-series forecasting baselines, BLOOM ranks first for gene- and cell-expression correlations across all three datasets. Measured-stage evaluations support recovery of developmental expression patterns, population organization and marker-specific temporal relationships. Biological analyses connect these predictions to cell-state identities, gene programmes and regulatory associations. At unmeasured stages, interpolation and autoregressive history and future rollouts extend simulated expression dynamics between and beyond measured timepoints. Analyses of marker genes and temporal descriptors identify candidate differences in the timing of muscle-associated, neural and vascular-specialization programmes. Input-based gene perturbations further probe predicted responses of edited genes and associated molecular programmes across time. Together, BLOOM supports transcriptomic virtual embryo modeling by bridging temporal sampling gaps, exploring extended developmental trajectories and prioritizing gene-dependent hypotheses for experimental investigation.

</details>

---
