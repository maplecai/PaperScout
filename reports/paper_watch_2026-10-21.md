# Paper Scout 日报 2026-10-21

共筛选出 **3** 篇推荐论文。
📊 抓取 biorxiv 116/pubmed 37 → 粗筛 25 篇 → LLM 选中 3 篇

## 1. Predicting cell-state-specific gene regulation from DNA across species

- **期刊**: bioRxiv
- **作者**: Liu, H., Mao, S., Gallent, T. et al. (11 authors)
- **机构**: Jingtian Zhou @ Arc Institute, Palo Alto, CA, USA
- **日期**: 2026-10-20
- **ID**: DOI: 10.64898/2026.10.19.760026  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.19.760026v1
- **相关分数**: 10/10
- **一句话推荐**: 提出Bolero模型，通过细胞状态嵌入条件化sequence-to-function模型，预测跨物种、跨细胞状态的染色质可及性，直接命中我的增强子活性预测与虚拟细胞研究。
- **方法**: 提出Bolero，一种参数以大规模单细胞状态嵌入和连续生物学变量为条件的sequence-to-function深度学习模型。
- **主要发现**: 该模型通过细胞状态条件化，能跨物种、跨未训练状态预测染色质可及性与转录丰度，并成功追踪非编码变异的细胞类型特异性效应及motif协同语法。
- **对我的启发**: 将连续生物学变量作为条件轴注入序列模型以实现虚拟状态预测的范式，可启发我利用虚拟表观遗传特征作为条件变量来预测不同细胞类型的游离型增强子活性。

<details><summary>Abstract</summary>

DNA encodes the cell's phenotype, but the same DNA sequence is interpreted differently in every cell type, developmental stage, and activity state. Existing deep-learning models solve only half of this puzzle: sequence-to-function models read DNA but treat cell state as a fixed label, while single-cell foundation models represent cell state but not sequence. We developed Bolero, a sequence-to-function model whose parameters condition on atlas-scale cell-state embeddings and additional biological variables to predict cell-state-specific chromatin accessibility and transcript abundance from DNA. Trained on 10.7 million cells from 33 datasets across six mammals, Bolero matched or exceeded specialised models and resolved regulatory differences between closely related cell states, including cortical regional and developmental gradients. Extrapolating cell-state embeddings extended Bolero's predictions to cell states that are absent from training. Cell-state conditioning facilitated tracing of the effects of non-coding variants to the cell types in which they act. Using an AP-1 activity score as a further continuous conditioning axis, Bolero predicted activity-regulated chromatin changes without requiring actual stimulation data. Across human cell types, we reconstructed the cooperative grammar of motif identity and spacing underlying predicted AP-1 responses. Bolero further predicted cell-type-specific chromatin accessibility and AP-1 responses in species excluded from training, extending comparative genomics from sequence conservation to predicted functional conservation. Across 84 mammals, we found that predicted AP-1 responses were less conserved than chromatin accessibility at cis-regulatory elements, driven by the human-specific sequence variants on AP-1 and cooperating motifs. By combining reference genomes with reference cell atlases, Bolero allowed genome sequences, either native or mutated, to be queried across cell states, perturbations, and different species for their chromatin and expression signatures.

</details>

---

## 2. Genomic foundation models do not yet boost common variant discovery beyond standard functional annotations

- **期刊**: bioRxiv
- **作者**: Bass, A. J., Park, J., Mukherjee, S., Whittaker, J., Wallace, C.
- **机构**: Andrew J Bass @ University of Cambridge
- **日期**: 2026-10-19
- **ID**: DOI: 10.64898/2026.10.13.758880  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.13.758880v1
- **相关分数**: 8/10
- **一句话推荐**: 直接评估了AlphaGenome等sequence-to-function基因组基础模型在变异发现中的实际效用与局限性。
- **方法**: 采用替代功能错误发现率（sfFDR）框架，对比预训练基因组学基础模型（AlphaGenome、Borzoi、GPN-Star）与传统功能注释在GWAS变异发现中的效能。
- **主要发现**: 现有领先的基因组学基础模型在常见变异发现上尚未超越标准功能注释，且二者结合无显著增益，表明模型主要冗余捕获了已有注释信息。
- **对我的启发**: 在评估预训练模型预测增强子活性时，需验证其提取的虚拟表观遗传特征是否提供了超越传统注释的增量信息，而非仅是已有特征的冗余表达。

<details><summary>Abstract</summary>

Genomic foundation models (GFMs) use large-scale AI to model genetic sequences and their influence on molecular phenotypes. While GFMs have shown promise in rare variant analysis, their utility for common variant discovery remains untested. Using the surrogate functional false discovery rate framework for functionally informed GWAS discovery, we compared standard functional annotations (baselineLD) with annotations derived from three leading GFMs: the sequence-to-function models AlphaGenome and Borzoi, and the genomic language model GPN-Star. Across 27 UK Biobank traits, GPN-Star decreased locus discovery relative to a standard GWAS, whereas AlphaGenome and Borzoi increased discovery but by less than baselineLD (medians 1.8%, 3.8%, and 5.1%). When we combined the GFM and baselineLD annotations, there was no increase over baselineLD alone (median changes -0.1% to 0.2%), suggesting that AlphaGenome and Borzoi mostly capture information already in baselineLD. Thus, GFMs may require larger corpora or trait-specific feature engineering to improve discovery beyond standard functional annotations.

</details>

---

## 3. DNA augmentations for semi-supervised learning in genomic sequence classification.

- **期刊**: NAR genomics and bioinformatics
- **作者**: Hyunwoo Yoo, Gail L Rosen
- **机构**: Gail L Rosen @ Department of Electrical and Computer Engineering, Drexel University, 3141 Chestnut St, Philadelphia, PA 19104, United States.
- **日期**: 2026-10-19
- **ID**: DOI: 10.1093/nargab/lqag123  |  PMID: 42898793  |  URL: https://pubmed.ncbi.nlm.nih.gov/42898793/
- **相关分数**: 6/10
- **一句话推荐**: 探讨了DNA语言模型在半监督学习中的数据增强策略，属于生物序列表示学习的范畴。
- **方法**: 基于GROVER预训练语言模型的FixMatch/FlexMatch半监督学习范式，采用生物学感知的弱-强DNA序列增强算子。
- **主要发现**: 在半监督基因组分类中，温和且保留序列核心信息的增强策略（如短掩码配比低频indel）效果最优，而过度掩码或激进突变会破坏模型稳定性与性能。
- **对我的启发**: 在增强子活性预测的数据增强或序列处理（如padding/截断）中，应采用温和且保留调控基序的扰动策略（如短片段掩码），避免过度掩码或激进突变破坏顺式调控元件的核心特征。

<details><summary>Abstract</summary>

Semi-supervised learning (SSL) is a natural fit for genomics, where unlabeled sequences are abundant but high-quality labels are scarce due to costly curation. However, most SSL pipelines rely on generic perturbations that are not tailored to biological constraints, and it remains unclear which augmentation designs yield reliable gains for DNA sequence classification. In this application note, we present an empirical study of genome-aware weak-strong augmentation recipes for pseudo-label-based SSL, focusing on FixMatch and FlexMatch with a GROVER DNA language model backbone. Across two classification benchmarks-antimicrobial resistance (AMR) drug-class prediction from AMR gene sequences and multi-class oncovirus family classification from simulated 150 bp tumor-like reads-we systematically evaluate 25 weak/strong augmentation pairs constructed from biologically motivated operators, including reverse-complement, codon-level back-translation, mild masking/substitution (NN), high-rate substitution, and length-preserving insertion-deletion (indel). We find consistent trends: (i) moderate, sequence-preserving perturbations yield the best accuracy-stability trade-off, (ii) excessive masking or aggressive mutation increases variance and degrades performance, and (iii) short-segment masking (NN) for weak augmentation followed by an indel rate (around 5%) for strong augmentation emerge as a robust strategy to learn from unlabeled genomic data. We release implementations and recommended defaults to facilitate reproducible SSL for genomic sequence modeling under limited-label regimes.

</details>

---
