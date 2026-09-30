# Paper Scout 日报 2026-09-30

共筛选出 **5** 篇推荐论文。
📊 抓取 biorxiv 110/pubmed 46 → 粗筛 45 篇 → LLM 选中 5 篇

## 1. EpiZoo: a DNA sequence-aware foundation model for cross-species single-cell epigenomics

- **期刊**: bioRxiv
- **作者**: Li, K., Chen, X., Jiang, Q., Wang, Z., Lv, H., Jiang, R.
- **机构**: Rui Jiang @ Tsinghua University
- **日期**: 2026-09-29
- **ID**: DOI: 10.64898/2026.09.24.754017  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.24.754017v1
- **相关分数**: 8/10
- **一句话推荐**: 提出了一种DNA序列感知的跨物种单细胞表观基因组基础模型，直接契合你对表观遗传基础模型和序列到功能的研究兴趣。
- **方法**: 基于混合专家Transformer的DNA序列感知跨物种单细胞表观基因组基础模型，将表观图谱编码为整合序列与可及性信息的“细胞句子”进行预训练。
- **主要发现**: 该模型在跨物种单细胞分析任务中达到SOTA，并能直接从DNA序列预测跨基因组和物种的细胞类型特异性染色质可及性。
- **对我的启发**: 其将DNA序列与表观上下文整合为“细胞句子”的编码范式，可借鉴用于构建虚拟表观遗传特征以预测游离型增强子活性，并为评估不同padding策略对序列到功能预测的影响提供了基线模型参考。

<details><summary>Abstract</summary>

Large-scale single-cell epigenomic atlases characterize chromatin regulatory landscapes across diverse biological contexts, spanning cell types, tissues, individuals and species. Foundation models provide an opportunity to capture the full spectrum of cellular diversity in these atlases, yet current models remain largely confined to individual species by genomic coordinate dependence and overlook regulatory information encoded in DNA sequences. Here we introduce EpiZoo, a DNA sequence-aware foundation model for cross-species single-cell epigenomics. EpiZoo converts million-dimensional single-cell epigenomic profiles from diverse species into compact cell sentences that integrate DNA-encoded regulatory information, sequence-independent epigenomic context and accessibility-based importance. Built around a mixture-of-experts transformer and containing 2.6 billion parameters in total, EpiZoo is pretrained on our manually curated multi-species Omni-scATAC corpus of approximately 20.9 million cells to learn regulatory programs across species. On external datasets excluded from pretraining, EpiZoo achieves state-of-the-art performance in fundamental single-cell analysis tasks, including feature extraction, cell type annotation and data imputation. Its sequence-aware architecture enables extension to evolutionarily diverse species, and supports comparative analysis of regulatory conservation and divergence during primate evolution. Benefiting from this modeling design, EpiZoo enables context-aware prioritization of somatic mutations in cancer and prediction of cell-type-specific chromatin accessibility from DNA sequences across genomic regions and species.

</details>

---

## 2. Regulon-informed cellular representations reveal task-dependent generalization in drug combination prediction

- **期刊**: bioRxiv
- **作者**: Ignatova, E., Likhter, M.
- **机构**: Maksim Likhter @ OpenLongevity
- **日期**: 2026-09-29
- **ID**: DOI: 10.64898/2026.09.23.753774  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.23.753774v1
- **相关分数**: 5/10
- **一句话推荐**: 评估不同生物表示（如regulon）在跨细胞系药物组合预测中的任务依赖性泛化，与跨细胞类型泛化问题间接相关。
- **方法**: 结合转录因子regulon、通路评分和基因表达特征构建对称三分类预测器，在多种域偏移设置下评估药物组合预测的泛化能力。
- **主要发现**: 生物特征表示的预测价值高度依赖于域偏移类型和评估目标，且叠加额外的生物学表示并不必然提升泛化性能。
- **对我的启发**: 在评估预训练基因组学模型padding策略对跨细胞类型增强子活性预测的影响时，需考虑泛化效果的任务依赖性，系统评估不同域偏移场景而非单一指标定论。

<details><summary>Abstract</summary>

Drug combination models must represent cellular context in a form that remains informative when the tested cells or compounds differ from those used for training. Transcription factor regulons offer a biologically structured representation, but their contribution can depend on the accompanying features and the intended prediction task. We developed a symmetric three-class predictor of DrugComb ZIP interactions and compared all seven combinations of landmark expression, Hallmark pathway scores and CollecTRI regulon activities. The common dataset contained 302,042 observations across 3,042 drugs and 155 cellular contexts. We evaluated three group-held-out generalization settings: unseen cell lines, unseen drug scaffolds, and simultaneous exclusion of both, with five training seeds per representation and partition. Pathways plus regulons achieved the highest mean Macro-F1 on unseen cell lines (0.4737, compared with 0.4503 for expression alone). Compared with pathways alone, adding regulons increased mean Macro-F1 by 0.0153 on unseen cell lines and 0.0229 on unseen drug scaffolds, with positive differences across all five paired seeds in both settings. In contrast, the same addition reduced the mean under joint context and scaffold exclusion. Representation rankings also depended on the objective: regulons alone achieved the highest synergy average precision on unseen lines, whereas the Macro-F1-leading combination did not maximize precision among the top-ranked candidates. Further compression of pathways into non-negative matrix factorization programs did not exceed the best context-model Macro-F1 in any setting. These results demonstrate that the predictive value of functional context representations depends on both the type of domain shift and the evaluation objective, and that combining additional biological representations does not necessarily improve generalization. They provide a computational basis for studying drug combinations in senescent states, where transfer must subsequently be assessed using state-specific responses and matched controls.

</details>

---

## 3. A biological-response compound representation allows chemical perturbation prediction across cell lines

- **期刊**: bioRxiv
- **作者**: Le Breton, L., Kaufmann, L., Carraz-Billat, E., Fournier, Q., Lemieux, S.
- **机构**: Sebastien Lemieux @ Universite de Montreal
- **日期**: 2026-09-29
- **ID**: DOI: 10.64898/2026.09.28.755146  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.28.755146v1
- **相关分数**: 5/10
- **一句话推荐**: 使用生物响应表示预测跨细胞系的化学扰动，与单细胞扰动和跨细胞类型泛化有一定关联。
- **方法**: 提出BioPert框架，以参考细胞系的基因表达响应作为化合物表示，结合小型神经网络预测跨细胞系的转录扰动。
- **主要发现**: 基于生物响应的化合物表示在跨细胞系扰动预测上显著优于化学结构表示，且能有效捕捉上下文依赖效应。
- **对我的启发**: 启发我在跨细胞类型增强子活性预测中，可探索引入“参考细胞类型的表观遗传状态”作为虚拟特征，以桥接不同细胞类型间的上下文差异。

<details><summary>Abstract</summary>

Accurately predicting cellular responses to drugs remains a challenge with the potential to reduce experimental screening costs and accelerate drug discovery. Current computational approaches represent compounds through chemical structures, which carry little information regarding their activity within biological systems. We show that gene expression responses, measured in a reference cell line, can instead serve as transferable representations of chemical perturbations. The proposed framework, BioPert, uses biological representations with a small neural network to predict transcriptional delta responses in cell lines of different lineages. Across the Tahoe-100M and LINCS L1000 datasets, BioPert outperforms molecular fingerprints and embeddings learned from chemical structure, which provide limited improvements over random controls. BioPert's prediction correlations reach 0.79 on Tahoe-100M, corresponding to an improvement of 0.34 over the next-best representation. On LINCS, performance varies with the experimental reproducibility of the test conditions, highlighting the impact of batch effects. Notably, BioPert considerably surpasses predictions obtained by copying the reference response, demonstrating that it captures context-dependent effects. Further analysis of a C32-cobimetinib case shows pathway-level accuracy of the predictions, including when the reference and target responses differ. These results open a new path for chemical perturbation prediction and could ultimately reduce the burden of phenotypic screening.

</details>

---

## 4. Detecting Random Mutations in 16S rRNA Sequences

- **期刊**: bioRxiv
- **作者**: Haworth, R. M., Commichaux, S., Pop, M.
- **机构**: Rain M Haworth @ University of Maryland
- **日期**: 2026-09-29
- **ID**: DOI: 10.64898/2026.09.24.753821  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.24.753821v1
- **相关分数**: 5/10
- **一句话推荐**: 关注DNA基础模型生成的序列对公共数据库的污染及检测方法，与基因组基础模型的安全性评估间接相关。
- **方法**: 基于保守基序和gapped k-mer特征构建的机器学习分类器范式。
- **主要发现**: 利用保守核苷酸构建的gapped k-mer分类器能以超90%的准确率检测出5%随机突变的人工16S rRNA序列，且该特征在生命三域中均高度保守。
- **对我的启发**: 在评估预训练基因组学模型padding对增强子活性预测的影响时，可借鉴其利用gapped k-mer分析局部语法结构的方法，探究padding是否破坏了增强子原有的保守基序特征。

<details><summary>Abstract</summary>

Motivation: High-throughput sequencing technologies have driven rapid growth of biological sequence databases. Public repositories must therefore rely on automated computational heuristics to screen submitted sequences for errors and low quality. For example, SILVA SSU Ref, which exploits the conserved nature of 16S and 18S rRNA sequences, applies strict algorithmic quality controls yet still accepts sequences with up to 30% of their nucleotides deviating from any previously accepted sequence. This permissiveness creates opportunities for the admission of modified sequences, such as biologically plausible sequences generated by DNA foundation models. The vulnerability of public sequence databases to becoming polluted or poisoned with modified sequences necessitates the development of methods to detect such sequences. Results: We present the first investigation, to our knowledge, of the detectability of modified sequences. We consider simple computationally-modified 16S rRNA sequences that pass the quality control inclusion criteria of the SILVA database, which we generate via random substitutions. We present classifiers that can distinguish such modified sequences from natural 16S rRNA using conserved motifs. Our best classifier achieves over 90% sensitivity and specificity on our testing set when using a 5% artificial mutation rate. One feature used in our classifiers, gapped k-mers constructed from universally conserved nucleotides, was conserved across all three domains of life despite relying on exact matches to patterns found in E. coli, advancing our understanding of conserved grammatical structure in small subunit rRNA sequences. Availability and Implementation: Our source code is available at https://github.com/rainhaworth/16S-Mutation-Classifiers.

</details>

---

## 5. DECIPHER integrates disentangled representation learning and prototype-based cell-type deconvolution across molecular modalities

- **期刊**: bioRxiv
- **作者**: Lai, W., Li, C., Deng, Q., Zhu, Y., Liu, C., Li, Z., Luo, O. J.
- **机构**: Oscar Junhong Luo @ Department of Systems Biomedical Sciences, School of Medicine, Jinan University, Guangzhou 510632, China
- **日期**: 2026-09-29
- **ID**: DOI: 10.64898/2026.09.24.753940  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.24.753940v1
- **相关分数**: 4/10
- **一句话推荐**: 使用解耦表征学习进行跨模态细胞类型反卷积，与单细胞表征学习有一定关联，可能对虚拟细胞概念有启发。
- **方法**: 提出端到端解耦表征学习框架DECIPHER，结合可微非负最小二乘优化进行跨模态细胞类型去卷积。
- **主要发现**: 通过分离域恒定表征和域特定表征，模型在多模态去卷积中表现鲁棒，且提取的域恒定表征能有效转化为低维生物学信息，支持跨队列年龄预测和预后分层。
- **对我的启发**: 解耦表征学习思路可启发在预测不同细胞类型增强子活性时，将DNA序列基础特征与细胞类型特异性的虚拟表观遗传特征解耦，以提升模型跨细胞类型的泛化能力。

<details><summary>Abstract</summary>

The growing availability of single-cell resources creates new opportunities to extract cell-type-resolved information from the vast body of existing bulk omics data through cell-type deconvolution. Conventional deconvolution methods often rely on linear mixture models or specific probabilistic assumptions and can be sensitive to batch effects, whereas many deep-learning approaches are modality-specific or lack a unified end-to-end learning framework. Here, we developed DECIPHER, an end-to-end representation-learning framework for cell-type deconvolution that can be applied across multiple molecular modalities. DECIPHER learns a domain-constant representation (Zc) for deconvolution and a domain-specific representation (Zs) to model domain-associated variation. By integrating nonlinear representation learning with differentiable non-negative least-squares optimization, DECIPHER estimates cell-type proportions from Zc. Across simulated datasets, experimentally generated bulk-cell mixtures, real-world datasets, and multiple molecular modalities, DECIPHER showed robust and competitive cell-type deconvolution performance. Beyond cell-type proportion estimation, the learned Zc supported chronological age prediction across independent cohorts and prognostic stratification in lung adenocarcinoma, demonstrating that DECIPHER can transform high-dimensional bulk omics data into low-dimensional, biologically informative representations. DECIPHER thus broadens the utility of existing bulk omics resources for biological discovery and clinical research.

</details>

---
