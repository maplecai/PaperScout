# Paper Scout 日报 2026-09-16

共筛选出 **10** 篇推荐论文。
📊 抓取 biorxiv 81/pubmed 48 → 粗筛 67 篇 → LLM 选中 10 篇

## 1. TransBind2: Improving Transcription Factor-DNA Binding Prediction with Multimodal Data and Bidirectional Cross Attention

- **期刊**: bioRxiv
- **作者**: Basnet, S., Cheng, J.
- **机构**: Jianlin Cheng @ University of Missouri - Columbia
- **日期**: 2026-09-14
- **ID**: DOI: 10.64898/2026.09.07.749913  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.07.749913v1
- **相关分数**: 7/10
- **一句话推荐**: 多模态TF-DNA结合预测，融合DNA序列、染色质可及性和TF结构，支持跨细胞类型泛化，与regulatory genomics和sequence-to-function高度相关。
- **方法**: 结合双模态蛋白质语言模型与DNA序列及染色质可及性特征，采用双向交叉注意力机制预测TF-DNA结合的多模态分类模型。
- **主要发现**: 引入TF结构与染色质上下文的多模态融合显著提升了跨细胞类型和跨物种的TF-DNA结合预测泛化能力，且模型能在窗口级标签下精确定位结合位点。
- **对我的启发**: 将预测任务重构为<DNA bin, TF, cell type>三元组分类以实现跨细胞类型泛化的思路，可借鉴用于不同细胞类型游离型增强子活性的预测；同时其引入染色质可及性作为上下文输入的做法，对构建虚拟表观遗传特征有直接参考价值。

<details><summary>Abstract</summary>

Accurate genome-wide prediction of transcription factor (TF)-DNA binding remains challenging because many models focus mainly on DNA sequence and overlook chromatin context and TF structure. We previously developed TransBind, a protein-aware model that combines TF and DNA representations through cross-attention. Here, we introduce TransBind2, which improves on TransBind in several ways. It incorporates DNase-seq accessibility and genome mappability tracks as additional input, uses a biomodal protein language model (ProstT5) to capture both TF sequence and structure, and applies bidirectional cross-attention so DNA and protein features can refine each other. We also frame prediction as binary classification of individual <DNA bin, TF, cell type> triplets, allowing the model to generalize to new TFs and cell types. Across 690 human ChIP-seq experiments covering 161 TFs and 91 cell types, TransBind2 achieves a macro AUROC of 0.9648 and AUPR of 0.4215, outperforming TransBind and other baselines, with a [&ge;]12.67% relative AUPR gain. The model trained on human data also performs well in cross-species zero-shot prediction on mouse data. Saliency analysis shows that it can identify TF-binding peaks with a median error of 12-38 base pairs (bps) despite being trained on window-level labels. Ablation studies further show that TF structure, chromatin accessibility, and bidirectional attention each improve performance. Overall, these results show that combining TF structure with chromatin context leads to more accurate and generalizable TF-DNA binding predictions.

</details>

---

## 2. LucaCell: a sequence-centric foundation model for cross-species single-cell analysis

- **期刊**: bioRxiv
- **作者**: Sun, Y., He, Y., Ren, M. et al. (11 authors)
- **机构**: Yong He @ Token Foundry, Alibaba Token Hub, Alibaba Group, Hangzhou, China
- **日期**: 2026-09-14
- **ID**: DOI: 10.64898/2026.09.08.750024  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.08.750024v1
- **相关分数**: 7/10
- **一句话推荐**: 序列中心化的单细胞基础模型，用mRNA序列嵌入替代固定基因ID，与epigenetic foundation model、virtual cell和representation learning for biological sequences高度相关。
- **方法**: 采用预训练mRNA序列嵌入替代固定基因ID，结合离散化基因表达与Transformer编码器构建序列驱动的单细胞基础模型。
- **主要发现**: 基于序列的基因表示使模型无需手动映射即可实现跨物种、跨数据类型（含染色质可及性与微生物）的泛化，并在基因表达重建与病毒载量预测等任务上表现更优。
- **对我的启发**: 其以序列嵌入替代固定注释的范式，启发我在游离型增强子活性预测中探索基于序列的动态特征表征以提升跨细胞类型泛化能力，并提示需系统评估变长序列处理中的padding策略对预训练模型表征质量的影响。

<details><summary>Abstract</summary>

Single-cell foundation models have transformed transcriptomic analysis, yet most rely on fixed gene identifiers that limit transfer across species and data types. Here we present LucaCell, a sequence-centric foundation model that represents genes through pre-trained mRNA sequence embeddings rather than static gene annotations. Gene expression is discretized into bins and modeled with a Transformer encoder, enabling sequence-informed cell representation without a fixed gene-ID vocabulary. Pre-training on 85 million human and mouse single cells, LucaCell is evaluated on human, mouse and lemur gene expression profiles, human chromatin accessibility data, unaligned reads from more than 50 prokaryotic taxa, and five influenza A virus genomes. LucaCell enables manual-mapping-free cross-species cell type annotation and an alignment-free microbial embedding framework that simultaneously distinguishes bacterial species identity and intra-species physiological states. It also improves gene expression reconstruction by incorporating donor-specific exonic SNP information into mRNA sequence embeddings, and predicts cellular viral load across influenza A virus strains while highlighting infection-like transcriptional states in mock-infected cells. These results show that sequence-informed gene representation can improve the generalization of single-cell foundation models across species, data types, and predictive tasks.

</details>

---

## 3. pydreg: a fast Python package for identifying active cis-regulatory elements from nascent transcription

- **期刊**: bioRxiv
- **作者**: He, A. Y., Danko, C. G.
- **机构**: Charles G Danko @ Cornell University
- **日期**: 2026-09-13
- **ID**: DOI: 10.64898/2026.09.06.745329  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.06.745329v1
- **相关分数**: 6/10
- **一句话推荐**: 从新生RNA测序数据识别活跃顺式调控元件（增强子/启动子），与enhancer activity prediction直接相关，但本质是已有方法的Python移植而非新模型。
- **方法**: 将基于支持向量机（SVM）的新生RNA测序顺式调控元件识别工具（dREG）迁移至现代Python计算栈的工程实现。
- **主要发现**: pydreg在复用原版预训练模型与峰值调用逻辑的前提下，通过现代数值计算库实现了4.5倍加速和5.4倍内存优化，且预测结果与原版高度一致。
- **对我的启发**: 在部署或迁移预训练基因组学模型时，保留核心模型权重而仅重构底层计算后端，可在保证预测一致性的同时大幅降低内存开销，这对优化大模型推理时的内存占用（如padding处理）具有工程参考价值。

<details><summary>Abstract</summary>

Background: Active promoters and enhancers generate characteristic patterns of RNA transcription that can be measured through nascent RNA sequencing. dREG is a leading method that uses these patterns to identify active cis-regulatory elements across the genome, allowing regulatory activity and gene transcription to be profiled in the same experiment. However, its reference implementation was developed around an R-based workflow and a legacy GPU-accelerated support vector machine library that have become increasingly difficult to maintain and deploy. Findings: To improve future usability of dREG, we developed pydreg, a Python port of dREG. pydreg preserves the original pretrained models and peak calling procedure from dREG while using contemporary numerical libraries for CPU and GPU computation. pydreg achieves 4.5 and 5.4-fold reductions in runtime and peak host memory, respectively, compared to dREG while producing near identical peak calls. Conclusions: pydreg reduces practical barriers to running dREG locally, improves runtime and memory usage, integrates readily with Python-based genomics workflows, and provides a maintainable foundation on modern computing infrastructure. Availability and Implementation: pydreg is implemented in Python 3.11+ and is freely available under the GPL-3 license at https://github.com/adamyhe/pydreg and from PyPI via pip install pydreg[gpu] (for CUDA acceleration) or pip install pydreg[mlx] (for Apple Metal acceleration).

</details>

---

## 4. Codon language model scores provide information beyond protein language models for missense variant interpretation

- **期刊**: bioRxiv
- **作者**: Chen, R., Palpant, N., Foley, G., Boden, M.
- **机构**: Mikael Boden @ The University of Queensland
- **日期**: 2026-09-14
- **ID**: DOI: 10.1101/2025.03.12.642937  |  URL: https://www.biorxiv.org/content/10.1101/2025.03.12.642937v1
- **相关分数**: 5/10
- **一句话推荐**: 密码子语言模型用于变异效应预测，涉及DNA language model和representation learning for biological sequences，但聚焦编码区missense变异而非调控元件。
- **方法**: 基于密码子语言模型与蛋白质语言模型特征集成的错义变异效应预测范式。
- **主要发现**: 密码子语言模型能捕获蛋白质语言模型未涵盖的适度但可重复的变异效应信息，二者特征互补且互补程度具有基因和功能上下文依赖性。
- **对我的启发**: 该研究通过聚合同义密码子排除序列简并性干扰的消融设计，启发我在评估预训练基因组学模型 padding 影响时，需设计控制实验以剥离位置偏置与序列语义特征的混淆。

<details><summary>Abstract</summary>

Predicting variant effects remains a central challenge in genomics. Protein language models (PLMs) capture amino-acid-level sequence constraints, whereas codon language models operate on coding sequences and may retain information that is lost upon translation. Here, we tested whether scores from the codon language model CaLM provide predictive information beyond protein-level representations for missense-variant interpretation. Across 71,436 ClinVar missense variants from 11,554 genes, adding CaLM to PLM baselines produced modest but reproducible improvements under gene-held-out cross-validation. PLM-only ensemble controls and explicit mutational-context analyses indicated that this improvement could not be explained solely by generic ensembling or simple codon-substitution features. Aggregating CaLM probabilities across synonymous codons attenuated codon-degeneracy-associated discordance while preserving most of the broader differences between CaLM and PLM scores. Gene-level analyses further showed that CaLM contribution varied continuously across genes and depended partly on the protein-model background. Across ClinMAVE functional assays, however, improvements were less consistent, indicating that codon-protein complementarity is context dependent rather than universal. Together, these results identify a modest but reproducible component of variant-effect information in CaLM-derived codon-level scores that is not fully captured by protein-level language-model representations.

</details>

---

## 5. PHACTn enables training-free, context-independent inference of nucleotide variant tolerance across the genome

- **期刊**: bioRxiv
- **作者**: Yildirim, C., Kuru, N., Adebali, O.
- **机构**: Ogun Adebali @ Sabanci University
- **日期**: 2026-09-14
- **ID**: DOI: 10.64898/2026.09.08.750126  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.08.750126v1
- **相关分数**: 5/10
- **一句话推荐**: 非编码区变异耐受性预测，涉及regulatory genomics的非编码变异，且明确以基因组语言模型为对比对象，但方法本身是系统发育而非ML。
- **方法**: 基于系统发育树遍历与概率建模的无参数训练变异耐受性推断方法（PHACTn）。
- **主要发现**: 仅用4个可解释参数且无需训练或GPU，PHACTn在非编码变异预测上超越了现有工具及大规模序列模型，证明概率系统发育建模能捕获大模型遗漏的进化约束信号。
- **对我的启发**: 在评估预训练基因组学模型预测增强子活性的表征能力时，可将基于系统发育树的进化保守性特征作为轻量级基线，以探究大模型在进化约束信号上的表征盲区。

<details><summary>Abstract</summary>

Accurate prediction of single-nucleotide variant (SNV) tolerability across the entire human genome remains a fundamental challenge in computational genomics, particularly for non-coding regions where the regulatory landscape is vast and poorly understood. Machine learning classifiers suffer from data circularity and demographic bias, while genomic language models demand massive computational resources and offer little biological interpretability. Here, we present PHACTn (Phylogeny-Aware Computing of Tolerance for nucleotide variants), a training-free, parameter-minimal method that infers nucleotide variant tolerability by traversing the mammalian phylogenetic tree and explicitly modeling the evolutionary independence of observed substitutions and their distance from the query species. With only 4 interpretable parameters, no training and no GPU requirement, PHACTn outperforms all evaluated tools on non-coding variants curated from both the ClinVar, and on non-coding variants potentially responsible for selected Mendelian diseases curated from OMIM. Additionally, it achieves state-of-the-art performance on variants within the informative range of alignment-based inference. These results establish that principled probabilistic phylogenetic modeling captures evolutionary constraint signals that large-scale sequence models fail to recover, offering a powerful, accessible, and mechanistically transparent alternative for genome-wide variant effect prediction.

</details>

---

## 6. Benchmarking CUT&RUN analysis using motif enrichment

- **期刊**: bioRxiv
- **作者**: Tan, L., Viner, C., Li, X. H. et al. (9 authors)
- **机构**: Michael M. Hoffman @ University Health Network
- **日期**: 2026-09-14
- **ID**: DOI: 10.64898/2026.09.09.749495  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.09.749495v1
- **相关分数**: 5/10
- **一句话推荐**: 涉及CUT&RUN表观基因组数据的预处理和峰检测基准测试，与表观基因组特征处理相关。
- **方法**: 基于motif富集度的基准测试方法，评估CUT&RUN数据预处理策略（片段长度过滤与spike-in校准）及主流peak caller的性能。
- **主要发现**: 过滤≤120bp的片段普遍提升了目标motif富集度；酵母DNA spike-in校准显著提升MACS2的motif识别效果但对SEACR无益，而大肠杆菌spike-in常因污染导致结果失效。
- **对我的启发**: 在提取CUT&RUN等表观遗传信号作为预训练模型输入或虚拟特征时，可参考其≤120bp片段过滤策略以提升结合位点信号分辨率。

<details><summary>Abstract</summary>

Background. Cleavage under targets and release using nuclease (CUT&RUN) maps the genome-wide locations of chromatin-associated proteins and provides an improved alternative to chromatin immunoprecipitation sequencing (ChIP-seq) for profiling sequence-specific transcription factor binding sites. Identifying these binding sites plays a critical role in understanding gene regulation, and transcription factors provide a useful setting for benchmarking because their well-defined sequence motifs serve as built-in controls for evaluating performance. Compared with ChIP-seq, CUT&RUN achieves higher resolution and lower background by avoiding cross-linking and bulk precipitation. Its distinct fragment length and cleavage characteristics, however, limit the direct transfer of existing computational tools, which primarily target ChIP-seq data. The performance of these tools on CUT&RUN can depend strongly on preprocessing choices. In this work, we investigate preprocessing strategies for transcription factor CUT&RUN, focusing on fragment length filtering and spike-in calibration. We aim to improve peak detection and provide practical guidance for analysis. Results. We designed a benchmarking method to evaluate peak-calling procedures for CUT&RUN data and the effects of preprocessing approaches, including fragment length filtering and spike-in calibration. We benchmarked the two most widely used peak callers, MACS2 and SEACR, by assessing motif enrichment---the degree to which identified peaks contain the expected transcription factor binding motifs. Filtering for fragments with a length [&le;]120 bp generally improved target motif enrichment. Spike-in calibration using heterologous Saccharomyces cerevisiae DNA improved motif elucidation substantially for MACS2, with little benefit for SEACR. By contrast, using Escherichia coli DNA as a spike-in control often failed to produce valid results unless we could meticulously control E. coli contamination. MACS2 performed robustly across samples. SEACR performed especially well on clean, sparse-background datasets, but performed poorly on some datasets with denser background signal and often produced numerous apparent false positives. While MACS2 provided robust results under minor perturbations in fragment length filtering, SEACR exhibited greater sensitivity to such changes. Discussion. Our benchmarking highlights how both peak caller choice and preprocessing strategy shape the analysis of transcription factor CUT&RUN data. By comparing the robustness and limitations of two widely used peak callers, we provide practical guidance on fragment length filtering, spike-in calibration, and tool selection. These findings help improve the processing and interpretation of CUT&RUN data, allowing researchers to more rapidly and reliably utilize this new technology. We expect that our work will guide more informed choices in CUT&RUN analysis and support the development of improved computational methodologies.

</details>

---

## 7. Heterogeneous epigenetic regulatory patterns link mammalian aging, development, and mortality

- **期刊**: bioRxiv
- **作者**: Tikhonov, S., Dmitriev, S. E.
- **机构**: Stanislav Tikhonov @ Faculty of Bioengineering and Bioinformatics, Lomonosov Moscow State University, 119234, Moscow, Russia
- **日期**: 2026-09-14
- **ID**: DOI: 10.64898/2026.09.08.750031  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.08.750031v1
- **相关分数**: 5/10
- **一句话推荐**: 涉及DNA甲基化和表观遗传时钟预测模型，与表观遗传基础模型兴趣间接相关。
- **方法**: 基于跨物种血液DNA甲基化元分析构建预测死亡率的表观遗传时钟模型。
- **主要发现**: 基因间区CpG位点的甲基化水平随年龄呈U型变化且与死亡率曲线平行，揭示了衰老、发育与疾病间异质性的表观调控规律。
- **对我的启发**: 基因间区（游离型增强子富集区）甲基化的非单调动态变化提示，在预测增强子活性的虚拟表观特征中可引入年龄或发育阶段作为上下文先验。

<details><summary>Abstract</summary>

Aging is often described as a monotonic accumulation of cellular damage, yet all-cause mortality follows a U-shaped trajectory with age, suggesting non-monotonic molecular changes. We investigated links between early childhood development, aging, and chronic diseases by analyzing DNA methylation in mammalian blood. A meta-analysis of 16 human chronic diseases revealed heterogeneous methylation signatures that formed 2 major disease clusters distinguished by their associations with development and sex-related methylation changes. Although epigenetic entropy increased monotonically across the lifespan, several diseases reduced blood DNA methylation entropy independently of blood cell composition. Across mammals, many CpG sites, particularly in intergenic regions, followed U-shaped age-related methylation changes that paralleled mortality curves. Based on these patterns, we developed epigenetic clocks that predict expected mortality across species and tissues and are effective in detecting a range of disease models. Overall, our findings reveal fundamental links between epigenetic regulation during development, aging, and chronic diseases.

</details>

---

## 8. Mechanistic Interpretability of Protein Language Models Reveals Encoded Structural and Functional Properties of Intrinsically Disordered Proteins

- **期刊**: bioRxiv
- **作者**: Naworski, L. E., Good, L. L., Scrutton, R., Knowles, T. P. J.
- **机构**: Tuomas P.J. Knowles @ University of Cambridge
- **日期**: 2026-09-13
- **ID**: DOI: 10.64898/2026.09.10.750691  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.10.750691v1
- **相关分数**: 4/10
- **一句话推荐**: 对蛋白质语言模型(ESM-2)做机制可解释性分析，方法论上与DNA语言模型的表示学习可类比，但研究对象是蛋白质而非DNA调控序列。
- **方法**: 基于机制可解释性分析蛋白质语言模型（ESM-2）在内在无序蛋白上的注意力分布与表征提取。
- **主要发现**: ESM-2对无序区域注意力虽低，但仍编码了疾病相关残渣及动态结构特征等有意义的生物学信号。
- **对我的启发**: 可借鉴其机制可解释性方法，分析预训练基因组学模型对游离型增强子及padding序列的注意力分布，验证其是否捕获真实表观遗传特征而非序列偏置。

<details><summary>Abstract</summary>

Protein language models (PLMs) such as ESM-2 encode protein sequences as embeddings for downstream tasks. PLMs are trained on a masked learning objective that leverages evolutionary constraints. While interpretability studies of ESM-2 have focused on folded proteins, their behavior on intrinsically disordered proteins (IDPs), which constitute a substantial fraction of the human proteome and are implicated in numerous diseases, remains understudied. Because IDPs experience different types of evolutionary constraints on their amino acid sequences, we hypothesized that PLMs would behave differently on disordered versus folded regions. Here we show that ESM-2 exhibits reduced attention on disordered regions, yet still encodes meaningful biological signals. The model assigns heightened attention to disease-relevant residues even at high levels of disorder. Moreover, we show that both the radius of gyration and individual dynamic contact maps, key characteristics of IDPs, can be obtained from the model logits and embeddings. These findings suggest PLMs capture valuable information relevant to IDP biology despite their bias toward structured residues.

</details>

---

## 9. ImmuneLens: linking transcriptional states and TCR clonotypes through disentangled multimodal learning

- **期刊**: bioRxiv
- **作者**: Duan, Z., Wang, Y., Li, C., Li, G., Cao, Y., Bai, X., Yang, F., Song, S.
- **机构**: Shuhui Song @ Beijing Institute of Genomics, Chinese Academy of Sciences/ China National Center for Bioinformation
- **日期**: 2026-09-14
- **ID**: DOI: 10.64898/2026.09.08.749998  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.08.749998v1
- **相关分数**: 4/10
- **一句话推荐**: 多模态表示学习框架整合转录组和TCR序列，方法论上与多模态生物序列表示学习有共通之处，但应用领域是免疫学而非调控基因组学。
- **方法**: 提出基于解耦多模态学习的单细胞转录组与TCR序列联合表示学习框架。
- **主要发现**: GEX与TCR信息的互补性提升了抗原特异性预测稳定性，并揭示了克隆扩增与CD8 T细胞功能状态的关联。
- **对我的启发**: 无明显直接启发

<details><summary>Abstract</summary>

Single-cell multi-omics technologies simultaneously capture the transcriptome and TCR sequence of T cells, providing an opportunity to study the relationship between transcriptional states and clonal architectures. However, jointly modeling the relationships between transcriptional states and TCR sequences while preserving modality-specific information remains challenging. Here, we present ImmuneLens, an interpretable multimodal representation learning framework designed for paired single-cell transcriptome and TCR sequence data. ImmuneLens supports the construction of a transferable multi-cohort immune reference atlas and enables unsupervised mapping of external query data. The complementarity between GEX and TCR information improves the stability of antigen-specificity prediction. In neoadjuvant immunotherapy cohorts, ImmuneLens resolves response-associated T cell heterogeneity and reveals links between clonal expansion and CD8 T cell functional states. Overall, ImmuneLens provides a

</details>

---

## 10. Heterogeneous graph neural networks with biological prior knowledge for interpretable drug repurposing in triple-negative breast cancer

- **期刊**: bioRxiv
- **作者**: Fernandez-Lozano, C., Ferreiro, D., V.-del-Rio, P.
- **机构**: Carlos Fernandez-Lozano @ Department of Computer Science and Information Technologies, Faculty of Computer Science, Universidade da Coruna, A Coruna, Spain
- **日期**: 2026-09-14
- **ID**: DOI: 10.64898/2026.09.08.750045  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.08.750045v1
- **相关分数**: 4/10
- **一句话推荐**: 使用图神经网络整合转录因子调控网络进行药物重定位，涉及调控网络建模。
- **方法**: 融合转录因子调控网络、蛋白质互作与药物-靶点边构建异构知识图谱，采用异构图神经网络进行药物敏感性预测，并利用Integrated Gradients进行机制归因。
- **主要发现**: 该模型在全局预测上与ML基线持平，但通过IG归因稳定识别出介导药物响应的关键TF，并在多队列临床数据中验证了预测敏感性与生存期的关联，筛选出7个潜在重定位药物。
- **对我的启发**: Integrated Gradients对GNN进行稳定机制归因的范式，可借鉴用于解析预训练基因组学序列模型中特定序列特征对增强子活性预测的贡献度。

<details><summary>Abstract</summary>

Drug repurposing offers a cost-effective path to new therapies for triple-negative breast cancer (TNBC), a subtype with limited targeted treatment options. We present PRECISION, a framework integrating transcription factor (TF) regulatory networks, protein-protein interactions, and drug-target edges into a heterogeneous graph neural network (GNN) to identify TFs mediating drug sensitivity and prioritize repurposing candidates. The knowledge graph has 23,498 nodes and approximately 830,000 edges from CollecTRI, OmniPath and the PRISM screen. In a fair cell-line hold-out evaluation, the GNN matches ML baselines in global prediction (Pearson r = 0.76). Per-drug mechanistic attributions via Integrated Gradients on the trained GNN, replicated across three independent training seeds and robust to baseline choice (Spearman's rho = 0.94 between the mean and the random Gaussian baselines), highlight stress-response (CREB3L1), epithelial-mesenchymal transition (EMT; KLF8, ZEB1), stromal/TNBC-specific (AEBP1, MZF1), and epithelial (SPDEF) regulators as stable mediators of drug response. Multi-cohort validation in SCAN-B (n = 7,397), METABRIC (n = 1,979), and TCGA-BRCA (n = 1,072) shows that predicted drug sensitivity is associated with overall survival in 623 drugs in SCAN-B and 74 in METABRIC (FDR < 0.05). Fisher's meta-analysis identifies 551 drugs at FDR < 0.05, validated by positive controls paclitaxel (p_adj = 8.6x10-3), docetaxel (3.1x10-2), epirubicin (3.2x10-6), and talazoparib (1.4x10-4). Paired Wilcoxon tests in 39 AURORA-US patients with matched primary and metastatic samples confirm that 4 of the 10 IG-identified TFs (CREB3L1, KLF8, AEBP1, SPDEF) are significantly altered during metastatic progression after Bonferroni correction. An explicit rule applied to the PAM50-adjusted Cox multivariate results (penalizer = 0.1) selects seven candidates (osimertinib, saracatinib, erlotinib, brigatinib, pelitinib, entinostat, trametinib), revealing pharmacological convergence on the EGFR signaling axis.

</details>

---
