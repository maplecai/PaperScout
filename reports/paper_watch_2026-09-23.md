# Paper Scout 日报 2026-09-23

共筛选出 **3** 篇推荐论文。
📊 抓取 biorxiv 109/pubmed 36 → 粗筛 46 篇 → LLM 选中 3 篇

## 1. DeepSCENIC: transfer learning from sequence-to-function models enables causal gene regulatory network inference

- **期刊**: bioRxiv
- **作者**: Partel, G., De Winter, S., Konstantakos, V., Blaauw, C. H., Aerts, S.
- **机构**: Stein Aerts @ VIB Center of AI & Computational Biology, VIB-KU Leuven Center for Brain and Disease Research, KU Leuven
- **日期**: 2026-09-22
- **ID**: DOI: 10.64898/2026.09.18.752607  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.18.752607v1
- **相关分数**: 9/10
- **一句话推荐**: DeepSCENIC将Enformer/Borzoi等S2F预训练模型迁移到单细胞multiome数据，预测增强子-基因关联和扰动效应，直接命中你的sequence-to-function、单细胞扰动和增强子活性研究兴趣。
- **方法**: 结合预训练序列到功能（S2F）模型与单细胞多组学数据的迁移学习框架，用于推断因果基因调控网络。
- **主要发现**: 该框架无需先验PWM即可高保真恢复TF-RE和RE-TG相互作用，并能作为机制模拟器准确预测细胞状态转换中的扰动效应及跨物种保守调控网络。
- **对我的启发**: 结合预训练S2F模型（如Enformer/Borzoi）与单细胞多组学推断增强子-基因关联的范式，可为评估不同padding策略下预训练模型在游离型增强子活性预测中的表征能力提供基准对比。

<details><summary>Abstract</summary>

Sequence-to-function (S2F) deep learning models have become an important aid to decipher the genomic cis-regulatory code. However, current S2F models do not take the cellular trans-environment of transcription factors (TF) into account. Conversely, methods for gene regulatory network (GRN) inference often rely on heuristics or simple position weight matrices (PWMs), without exploiting the combinatorial grammar of genomic enhancers. Here, we present DeepSCENIC, a deep learning framework that enables causal GRN inference by performing transfer learning from S2F models to single-cell multiome atlases. We first test and validate DeepSCENIC on ENCODE cell lines, demonstrating that the framework accurately predicts single-cell gene expression and chromatin accessibility by leveraging pretrained S2F models like Enformer and Borzoi. We show that DeepSCENIC recovers TF-region (TF-RE) interactions with high fidelity, and captures de novo TF binding motifs without prior PWM knowledge. The model improves enhancer-gene associations (RE-TG) over correlation-based baselines when benchmarked against large-scale CRISPRi screens. After training a DeepSCENIC model, it enables the prediction of perturbation effects during cell state changes by acting as a mechanistic simulator. In a melanoma cell line atlas, the model accurately recapitulates the transcriptional shift from melanocytic to mesenchymal states, and predicted knock-down effects show high concordance with experimental time series data. Finally, we use DeepSCENIC to identify mouse-human cortex conserved GRNs, finding high cross-species concordance in TF activity programs across matched neuronal subclasses and validating top-ranked enhancers against experimental reporter assays. By unifying S2F enhancer representations with single-cell multiomics, DeepSCENIC provides a new paradigm for jointly modeling and simulating cis-sequence and trans-cellular perturbations.

</details>

---

## 2. ChromBPNet: bias factorized, base-resolution deep learning models of chromatin accessibility reveal cis-regulatory sequence syntax, transcription factor footprints and regulatory variants

- **期刊**: bioRxiv
- **作者**: Pampari, A., Shcherbina, A., Kvon, E. Z. et al. (13 authors)
- **机构**: Anshul Kundaje @ Stanford University
- **日期**: 2026-09-22
- **ID**: DOI: 10.1101/2024.12.25.630221  |  URL: https://www.biorxiv.org/content/10.1101/2024.12.25.630221v1
- **相关分数**: 9/10
- **一句话推荐**: ChromBPNet是DNA序列到染色质可及性的深度学习模型，预测变异效应和TF footprint，直接属于sequence-to-function和调控序列建模核心领域。
- **方法**: 基于偏倚解卷积的碱基分辨率染色质可及性序列预测深度学习模型。
- **主要发现**: 该轻量级模型通过分离实验酶切偏倚与调控序列特征，在预测变异效应和TF结合上媲美大型模型，并精准提取motif语法与足迹。
- **对我的启发**: 在评估预训练基因组学模型padding对增强子活性预测的影响时，可借鉴其偏倚解卷积策略，显式分离padding引入的序列边界伪影与真实的顺式调控语法，以提升模型鲁棒性。

<details><summary>Abstract</summary>

Despite extensive mapping of cis-regulatory elements (cREs) across cellular contexts with chromatin accessibility assays, the sequence syntax and genetic variants that regulate transcription factor (TF) binding and chromatin accessibility at context-specific cREs remain elusive. We introduce ChromBPNet, a deep learning DNA sequence model of base-resolution accessibility profiles that detects, learns and deconvolves assay-specific enzyme biases from regulatory sequence determinants of accessibility, enabling robust discovery of compact TF motif lexicons, cooperative motif syntax and precision footprints across assays and sequencing depths. Extensive benchmarks show that ChromBPNet, despite its lightweight design, is competitive with much larger contemporary models at predicting variant effects on chromatin accessibility, pioneer TF binding and reporter activity across assays, cell contexts and ancestry, while providing interpretation of disrupted regulatory syntax. ChromBPNet also helps prioritize and interpret regulatory variants that influence complex traits and rare diseases, thereby providing a powerful lens to decode regulatory DNA and genetic variation.

</details>

---

## 3. Deep genomic models of allele-specific measurements.

- **期刊**: Genome research
- **作者**: Xinming Tu, Alexander Sasse, Kaitavjeet Chowdhary, Anna Spiro, Liang Yang, Maria Chikina, Christophe Benoist, Sara Mostafavi
- **机构**: Sara Mostafavi @ University of Washington, Canadian Institute for Advanced Research saramos@cs.washington.edu.
- **日期**: 2026-09-21
- **ID**: DOI: 10.1101/gr.282189.126  |  PMID: 42767805  |  URL: https://pubmed.ncbi.nlm.nih.gov/42767805/
- **相关分数**: 8/10
- **一句话推荐**: DeepAllele是sequence-to-function深度学习模型，用配对等位基因输入预测顺式调控变异效应，与你的调控变异预测和序列到功能研究方向高度契合。
- **方法**: 提出DeepAllele，一种采用配对等位基因特异性序列作为输入的深度学习sequence-to-function模型，通过对比等位基因间序列差异预测基因调控的微小变化。
- **主要发现**: 在F1杂交小鼠免疫细胞数据上，该模型相比基线模型能在更广泛的基因组区域中学习到与已知生物学机制相符的顺式调控语法，有效挖掘功能相关的调控基序。
- **对我的启发**: 利用配对等位基因对比学习微小序列差异对调控活性的影响，此范式可借鉴用于评估预训练基因组学模型在padding或微小序列扰动下对虚拟表观遗传特征及增强子活性预测的鲁棒性。

<details><summary>Abstract</summary>

Allele-specific quantification of sequencing data allows for a systematic investigation of how DNA sequence variations influence cis gene regulation. Current methods for analyzing allele-specific measurements for causal analysis rely on statistical associations between genetic variation across individuals and allelic imbalance. Instead, we propose DeepAllele, a novel deep learning sequence-to-function model using paired allele-specific input, designed to learn sequence features that predict subtle changes in gene regulation between alleles. Our approach is suited for datasets with unambiguous phasing, such as F1 hybrids and other controlled genetic crosses, or long-read sequencing technologies used in Fiber-seq, in which reads can be assigned to complete allele sequences. We apply our framework to allele-specific measurements in immune cells from F1 hybrid mice, and show that the model's additionally learned cis-regulatory grammar aligns with known biological mechanisms across a significantly larger number of genomic regions compared to baseline models. In summary, our work presents a computational framework to leverage genetic variation to uncover functionally-relevant regulatory motifs, enhancing discovery in genomics.

</details>

---
