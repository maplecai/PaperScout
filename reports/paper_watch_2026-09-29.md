# Paper Scout 日报 2026-09-29

共筛选出 **9** 篇推荐论文。
📊 抓取 biorxiv 74/pubmed 26 → 粗筛 40 篇 → LLM 选中 9 篇

## 1. scLDM: a conditional diffusion framework for single-cell perturbation prediction.

- **期刊**: Bioinformatics (Oxford, England)
- **作者**: Boyang Wu, Yuhang Liu, Yue Cheng, Xiangrong Liu, Quan Zou, Leyi Wei, Lei Xu
- **机构**: Lei Xu @ School of Electronic and Communication Engineering, Shenzhen Polytechnic University, Shenzhen 518055, China.
- **日期**: 2026-09-28
- **ID**: DOI: 10.1093/bioinformatics/btag727  |  PMID: 42804716  |  URL: https://pubmed.ncbi.nlm.nih.gov/42804716/
- **相关分数**: 7/10
- **一句话推荐**: 提出基于扩散模型的条件生成框架预测单细胞扰动响应，直接契合研究兴趣中的single-cell perturbation方向。
- **方法**: 基于变分自编码器降维与条件潜在扩散模型（LDM）的单细胞扰动响应生成范式。
- **主要发现**: 该模型在跨物种、多场景的扰动预测中优于SOTA，且其学习到的扰动嵌入与已知生物学机制高度对齐，具备强可解释性。
- **对我的启发**: 可借鉴其利用条件扩散模型将细胞类型作为显式引导条件的范式，预测不同细胞类型特异性的游离型增强子活性状态。

<details><summary>Abstract</summary>

MOTIVATION: Accurate prediction of single-cell responses to external stimuli is pivotal for deciphering gene regulatory mechanisms and accelerating data-driven drug discovery. However, effectively capturing the complex, non-linear mapping between intrinsic cell states and external stimuli remains an open problem. RESULTS: We propose scLDM, a generative framework based on latent diffusion models for predicting single-cell perturbation responses. scLDM first compresses high-dimensional gene expression into a compact latent space via a variational autoencoder, followed by a conditional diffusion process to generate post-perturbation states, explicitly guided by pre-perturbation cellular state, cell type, and perturbation type. Systematic evaluations on six datasets across diverse biological settings, spanning pharmacological stimulation, viral infection, helminth infection, genetic perturbations, and multi-species immune response contexts, demonstrate that scLDM achieves superior predictive accuracy compared to state-of-the-art methods. Furthermore, the model exhibits strong interpretability, as the learned perturbation embeddings show high functional alignment with known biological mechanisms. Overall, scLDM provides a robust and biologically consistent strategy for in silico perturbation screening. AVAILABILITY: The code is available at https://github.com/samrogers1233/scLDM and archived on Zenodo at https://doi.org/10.5281/zenodo.22658164. SUPPLEMENTARY INFORMATION: Supplementary data are available at Bioinformatics online.

</details>

---

## 2. CheckAMG: Accurate Identification of Auxiliary Viral Genes with Genome-Language Models

- **期刊**: bioRxiv
- **作者**: Kosmopoulos, J. C., Martin, C., Wainaina, J. M., Bolduc, B., Urvoy, M., Sullivan, M. B., Anantharaman, K.
- **机构**: Karthik Anantharaman @ University of Wisconsin-Madison
- **日期**: 2026-09-27
- **ID**: DOI: 10.64898/2026.09.23.753886  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.23.753886v1
- **相关分数**: 6/10
- **一句话推荐**: 使用微调的基因组语言模型识别病毒辅助基因，与DNA语言模型研究兴趣间接相关。
- **方法**: 结合基于注释的规则评分与微调基因组语言模型进行不依赖同源序列的辅助病毒基因识别。
- **主要发现**: 该方法在跨生态系统基准测试中优于现有工具，不仅提升了AMG识别可靠性，还扩展至生理和调控基因，并在百万级病毒基因组中发现了大量无参考序列相似性的新基因。
- **对我的启发**: 其利用微调基因组语言模型捕获无同源性序列功能特征的范式，启发我在增强子活性预测中探索预训练模型对缺乏表观遗传特征序列的泛化能力，并评估不同padding策略对短片段增强子特征提取的影响。

<details><summary>Abstract</summary>

Viruses shape microbial metabolism through auxiliary viral genes (AVGs) that reprogram host metabolism, physiology, and gene regulation during infection. Identifying AVGs is complicated by ambiguous viral versus cellular assignment, inconsistent curation, and reliance on sequence homology that misses divergent functions. Here we present CheckAMG, which pairs annotation-based AVG prediction, curated with a per-gene viral scoring system and ontological mapping of metabolic function, with a finetuned genome-language model for annotation-independent discovery. Benchmarked against DRAM-V and VIBRANT across three ecosystems, CheckAMG produced more strongly supported auxiliary metabolic gene (AMG) calls, and uniquely among AMG tools reports auxiliary physiological (APGs) and regulatory (AReGs) genes. Applied to 1,005,980 fragmented or complete soil and human-gut viral genomes, CheckAMG identified 541,199 AVGs tracking biome-specific protein clusters and functions, including 109,107 proteins with no detectable sequence similarity to any reference database. CheckAMG thus provides a reproducible, scalable framework for identifying the genes through which viruses reprogram host biology.

</details>

---

## 3. Analyzing Genomic Foundation Models for Viral Sequence Identification

- **期刊**: bioRxiv
- **作者**: Buzkova, V., Dvorsky, B., Komarkova, M., Kollinova, K., Krupicka, R., Klempir, O.
- **机构**: Ondrej Klempir @ Czech Technical University in Prague, Faculty of Biomedical Engineering
- **日期**: 2026-09-28
- **ID**: DOI: 10.64898/2026.09.25.754388  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.25.754388v1
- **相关分数**: 5/10
- **一句话推荐**: 评估了基因组基础模型（如NT和DNABERT）的序列嵌入在分类任务上的表现，与评估预训练基因组基础模型的项目在方法论上存在间接关联。
- **方法**: 利用预训练基因组基础模型（Nucleotide Transformer与DNABERT）提取序列嵌入，结合多种池化策略与最近邻搜索进行无比对病毒序列分类。
- **主要发现**: 冻结参数的NTv3-650M在病毒序列分类上准确率接近BLAST，且在长序列上表现更优；但所有基础模型对碱基掩码的鲁棒性均显著弱于传统比对方法。
- **对我的启发**: 该文对mean/max/CLS等不同池化策略在序列表征上的效果评估，启发我在处理增强子序列时，可系统探究不同池化方式及padding策略对预训练模型提取虚拟表观遗传特征及下游活性预测的影响。

<details><summary>Abstract</summary>

Rapid and accurate identification of viral sequences underpins clinical diagnostics, epidemiological surveillance, and the safety testing of biological products, yet the established alignment-based methods such as BLAST are inherently closed-set, with accuracy tied to how well a query is already represented in the reference database. Recent advances in genomic foundation models (GFMs) have enabled alignment-free approaches to sequence classification. However, their performance relative to traditional methods remains incompletely characterised. We evaluated GFMs, specifically the Nucleotide Transformer (NT) and DNABERT families, for viral sequence classification using a dataset derived from the Reference Viral Database (RVDB). Sequence embeddings were generated with mean, max, and CLS pooling, classified by nearest-neighbour search in an embedding index and compared with BLAST as a reference. Matching BLAST provided a particularly stringent benchmark here, because as a closed-set method it compares each query directly against the exact reference sequences it stores, whereas a foundation model must rely on representations shaped by broad, general-purpose pre-training. On sequences of standard length, the best model, NTv3-650M, reached an accuracy of 0.93, approaching the 0.97 achieved by BLAST. On long genomic sequences, evaluated on a much smaller test set, the difference narrowed further, with NTv3-650M reaching 0.95 against 0.98 for BLAST. Robustness analyses showed that all GFMs were markedly more sensitive to base masking than BLAST. Both methods indexed the same labelled reference sequences, and BLAST compared queries with them directly at the nucleotide level, so approaching it from frozen, general-purpose representations without any parameter update is a meaningful result. NTv3-650M emerged as the most promising candidate for further optimisation and deployment in bioinformatics applications.

</details>

---

## 4. Single-cell multiomics across nine mammals reveals cell-type-specific regulatory conservation in the brain.

- **期刊**: Cell genomics
- **作者**: Ashlyn G Anderson, Brianne B Rogers, Erin A Barinaga et al. (16 authors)
- **机构**: J Nicholas Cochran @ HudsonAlpha Institute for Biotechnology, Huntsville, AL 35806, USA. Electronic address: ncochran@hudsonalpha.org.
- **日期**: 2026-09-28
- **ID**: DOI: 10.1016/j.xgen.2026.101367  |  PMID: 42805172  |  URL: https://pubmed.ncbi.nlm.nih.gov/42805172/
- **相关分数**: 5/10
- **一句话推荐**: 涉及跨物种细胞类型特异性顺式调控元件（CREs）和增强子功能分析，与增强子活性预测及调控基因组学背景间接相关。
- **方法**: 跨物种单细胞多组学联合多维保守性框架（整合序列、染色质可及性与增强子-基因关联），辅以MPRA和CRISPRi功能验证。
- **主要发现**: 揭示了大脑增强子在不同物种间的细胞类型特异性保守维度，并发现神经退行性疾病遗传风险局限于保守增强子，而神经精神疾病风险在保守及人类特异性增强子中均富集。
- **对我的启发**: 该研究生成的跨物种细胞类型特异性CRE序列及MPRA活性数据集，可作为评估预训练基因组学模型在跨物种增强子活性预测中序列对齐(padding)策略及泛化能力的基准。

<details><summary>Abstract</summary>

Understanding gene regulation in the brain is essential for defining the genetic basis of neurologic disease. Cis-regulatory elements (CREs) regulate gene expression, but their function and evolution depend on sequence and cis- and trans-regulatory context. We generated single-nucleus RNA- and ATAC-seq data from cortex across nine mammalian species and identified cell-type-specific candidate CREs. We developed a multidimensional conservation framework integrating sequence, chromatin accessibility, and enhancer-gene associations. Massively parallel reporter assays in human neural progenitor cells and neurons measured activity of conserved and human-specific CREs, while CRISPR interference validated enhancer function at conserved loci, including FAM181B. Motif enrichment identified transcription factors distinguishing conserved from evolved CREs. Linkage disequilibrium score regression showed that conserved and human-specific CREs were enriched for neuropsychiatric GWAS risk, whereas neurodegenerative risk was restricted to conserved elements. These findings define functional dimensions of enhancer conservation and reveal how regulatory evolution shapes brain biology and disease susceptibility.

</details>

---

## 5. Cognitive-Motor Dual Task Training Synergistically Improves Aging-related Cognitive Dysfunction By Reducing TMAO and Suppressing TXNIP/NLRP3 Pathway.

- **期刊**: Molecular neurobiology
- **作者**: Rong Zhang, Tengteng Dai, Ziman Zhu, Weijun Gong
- **机构**: Weijun Gong @ Department of Neurological Rehabilitation, Beijing Rehabilitation Hospital, Capital Medical University, Beijing, 100144, China. gwj197104@ccmu.edu.cn.
- **日期**: 2026-09-28
- **ID**: DOI: 10.1007/s12035-026-06228-6  |  PMID: 42804118  |  URL: https://pubmed.ncbi.nlm.nih.gov/42804118/
- **相关分数**: 5/10
- **一句话推荐**: 提出基于傅里叶和小波变换的核酸序列特征提取框架，属于生物序列表示学习的一种新尝试。
- **方法**: 采用D-半乳糖诱导衰老大鼠模型，结合认知-运动双任务训练干预与体内/体外分子生物学实验（UHPLC-MS/MS、Western blot、Co-IP），解析TMAO/TXNIP/NLRP3通路机制。
- **主要发现**: 认知-运动双任务训练（CMDT）较单一认知训练更显著改善衰老相关认知障碍，其优势在于同时降低外周及海马TMAO蓄积并抑制TXNIP/NLRP3炎症级联；单一认知训练可下调TXNIP/NLRP3但不影响TMAO水平。
- **对我的启发**: 无明显直接启发

<details><summary>Abstract</summary>

Cognitive dysfunction is highly prevalent in older adults and severely impairs daily activities and quality of life. Rehabilitation training alleviates aging-related cognitive dysfunction (ARCD); however, the mechanisms underlying differential effects of different training regimens remain poorly understood. Motor training relieves TMAO-triggered neuroinflammation, while cognitive training (CT) improves ARCD via suppression of chronic inflammatory signaling. Cognitive-motor dual-task training (CMDT) yields more obvious cognitive protection than single-mode training, yet the molecular mechanisms accounting for its enhanced protective capacity have not been fully clarified. Thirty 18-month-old male SD rats were subjected to D-galactose injection to establish the ARCD model and randomly divided into five groups (n = 6 per group). Partial model rats received exogenous TMAO administration to verify its neurotoxicity. Animals were treated with CT or CMDT intervention separately. Novel object recognition (NOR) and Morris water maze (MWM) tests were adopted to assess cognitive function; UHPLC-MS/MS, Western blotting and Co-IP were used to detect peripheral and hippocampal TMAO as well as inflammatory protein expression. HT22 cell models were constructed for in vitro validation, with three independent biological replicates set for all molecular measurements. In vivo results showed that CT significantly alleviated cognitive deficits and downregulated hippocampal TXNIP and NLRP3 expression (P < 0.05), without changing circulating or hippocampal TMAO levels (P > 0.05). In contrast, CMDT generated more prominent cognitive improvements and simultaneously reduced TMAO accumulation together with TXNIP overexpression (P < 0.05). In vitro experiments showed that TMAO aggravated D-galactose-induced neuronal senescence and inflammatory activation, which was associated with up-regulation of the TXNIP-NLRP3 inflammatory cascade, and inhibiting TXNIP could reverse such pathological injury. Co-IP assays further showed that TMAO promoted the binding of NLRP3 to ASC, while the caspase-8-ASC binding showed no significant differences across all groups. CMDT exhibits relatively better therapeutic effects against ARCD compared with CT. The present observations reveal that CMDT-related cognitive improvement occurs alongside reduced TMAO accumulation and suppressed TXNIP-NLRP3 inflammatory pathway activation. Combined with our prior MT experimental data, the stronger intervention capacity of CMDT may be related to regulatory effects originating from its cognitive and motor components. This study provides experimental evidence supporting CMDT as a potential rehabilitation strategy for ARCD.

</details>

---

## 6. MuseDrift: Navigating Protein Evolutionary Manifolds with Conditional Discrete Diffusion

- **期刊**: bioRxiv
- **作者**: Wang, C., Wang, Y.
- **机构**: Yiquan Wang @ Department of Infectious Disease and Immunology, University of Florida, Gainesville, FL 32608, USA
- **日期**: 2026-09-28
- **ID**: DOI: 10.64898/2026.05.11.724439  |  URL: https://www.biorxiv.org/content/10.64898/2026.05.11.724439v1
- **相关分数**: 5/10
- **一句话推荐**: 蛋白质序列的条件离散扩散生成模型，与生物序列表示学习间接相关。
- **方法**: 提出一种基于条件离散扩散的蛋白质序列生成范式，利用预训练野生型表示作为上下文并结合序列同一性感知调制进行去噪。
- **主要发现**: 该模型在无特定属性引导下，能精准控制变体与野生型的序列同一性，且生成的变体在结构预测置信度和外部突变效应评分上均优于基线方法。
- **对我的启发**: 利用预训练表示作为上下文条件化去噪过程的思路，启发我在增强子活性预测中可探索将预训练基因组学模型的上下文特征（如针对padding区域的特定编码）作为条件输入，以增强序列到功能的表征能力。

<details><summary>Abstract</summary>

Protein engineering often requires variants that differ from a wild-type (WT) sequence by a specified amount while remaining structurally and functionally plausible. Controlling WT similarity alone does not specify which residues should change or how their substitutions should be coordinated. Here, we introduce MuseDrift, a conditional discrete diffusion model that generates variants from a WT sequence and a target sequence identity, without task-specific property guidance. Trained on WT-homolog pairs spanning different identities, MuseDrift uses pretrained WT representations as context and identity-aware modulation to condition denoising. Compared with editing baselines at the same requested identities, its variants achieve higher mean structural prediction confidence and greater similarity to predicted WT structures. On the CAMEO dataset, it tracks requested identities spanning 30%-95%, with mean absolute errors of 0.52-2.08 percentage points across targets. Its generated variants also receive more favorable scores from external mutation-effect predictors than those from the evaluated baselines. Together, these results support MuseDrift as a framework for controlled exploration of WT-centered protein sequence space.

</details>

---

## 7. Efficient genome-wide mapping of reproducible, context-dependent eQTLs at single-cell resolution

- **期刊**: bioRxiv
- **作者**: Alquicira-Hernandez, J., Dorans, E., Tomofuji, Y., Nathan, A., Raychaudhuri, S.
- **机构**: Soumya Raychaudhuri @ Brigham and Women's Hospital
- **日期**: 2026-09-28
- **ID**: DOI: 10.64898/2026.08.25.747138  |  URL: https://www.biorxiv.org/content/10.64898/2026.08.25.747138v1
- **相关分数**: 5/10
- **一句话推荐**: 单细胞分辨率的动态eQTL映射，涉及细胞状态特异的基因调控效应，与细胞类型特异性调控研究间接相关。
- **方法**: 提出Dynema，采用带聚类稳健方差估计量的泊松回归模型，在真实单细胞分辨率下进行全基因组上下文依赖性eQTL映射。
- **主要发现**: 该方法高效且统计校准良好，揭示了伪bulk策略遗漏的细胞状态依赖性eQTL（如TSPAN32等自身免疫位点），阐明了疾病变异的动态调控效应。
- **对我的启发**: Dynema识别出的细胞状态特异性eQTL数据集，可作为评估我序列到功能模型在特定细胞类型下变异效应预测能力的高质量基准。

<details><summary>Abstract</summary>

Single-cell technologies enable linking disease-risk variants to gene regulatory effects in specific cell-state contexts. However, most so called "single-cell eQTL" studies use a "pseudobulking" strategy to identify expression Quantitative Trait Loci (eQTLs), obscuring subtle dynamic regulatory effects of disease alleles. Here, we propose Dynema (Dynamic eQTL mapping in single cells) for fast and accurate genome-wide mapping of context-dependent and independent eQTL effects at true single-cell resolution. To identify eQTLs, Dynema uses a Poisson model with cluster robust variance estimators (CRVEs) to account for correlation of single-cell profiles from the same individual. In contrast to other common methods, Dynema achieves statistical calibration and scales to genome-wide analysis in large single-cell datasets in realistic timeframes. We applied Dynema to two independent T cell datasets and identified reproducible cell-state-dependent eQTL effects. Some cell-state-dependent eQTLs are missed by pseudobulking approaches, and many others are conditionally independent from lead eQTL effects. We show that TSPAN32 and other autoimmune loci colocalize with cell-state-dependent eQTLs. Mapping context-dependent eQTLs at single-cell resolution enables the definition of the molecular effects of complex disease alleles.

</details>

---

## 8. AtlasOT - The Fused Unbalanced Gromov-Wasserstein for Multimodal Integration of Disease Atlases

- **期刊**: bioRxiv
- **作者**: Peng, K., Ruiz, M., Caron, B., Kuppe, C., Nagai, J., Gesteira Costa Filho, I.
- **机构**: Ivan Gesteira Costa Filho @ RWTH Aachen University Hospital
- **日期**: 2026-09-28
- **ID**: DOI: 10.64898/2026.09.22.753496  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.22.753496v1
- **相关分数**: 4/10
- **一句话推荐**: 单细胞与空间多组学整合的最优传输方法，涉及空间调控动力学，对单细胞研究有一定启发。
- **方法**: 提出基于融合不平衡Gromov-Wasserstein最优传输（FUGW）的多模态整合框架，通过约束样本内传输并放宽质量守恒来对齐跨模态单细胞数据。
- **主要发现**: 该方法在scRNA-scATAC及空间转录组映射任务中优于现有SOTA，其传输计划可有效辅助稀有细胞检测、基因插补及调控网络重建等下游任务。
- **对我的启发**: 其放宽质量守恒以处理不平衡数据的思路，可启发我在sequence-to-function映射中利用不平衡最优传输处理padding引入的虚假序列质量分布，或对齐虚拟表观遗传特征与真实组学数据。

<details><summary>Abstract</summary>

Single-cell and spatial multiomics technologies are transforming disease atlas construction, but computational integration of unpaired modalities remains challenging, as existing methods overlook two biological constraints of data with matching samples. First, cells should only be mapped across modalities within the same donor or biospecimen, and second, cell recovery frequently differs substantially between modalities. To address these gaps, we present AtlasOT, an optimal-transport framework based on the fused unbalanced Gromov-Wasserstein (FUGW) formulation for multi-modal integration. AtlasOT jointly models a shared cross-modality feature space and modality-specific geometric structures while restricting transport to within-sample cell pairs. Moreover, AtlasOT relaxes strict mass conservation of the balanced optimal transport optimization to accommodate unbalanced cell numbers. We benchmark AtlasOT against state-of-the-art methods on scRNA-scATAC and scRNA-spatial transcriptomics mapping scenarios. Our results indicate that AtlasOT outperforms baselines and state-of-the-art methods in all considered scenarios. Moreover, we demonstrate that AtlasOT's transport plan can be used to improve several relevant tasks such as the detection of rare cell populations, spot-level cell-type deconvolution, spatial gene imputation, and reconstruction of transcription-factor-driven spatial regulatory dynamics. These results establish AtlasOT as a unified, biologically constrained framework for multimodal integration in disease atlas studies, with broad applicability to label transfer, imputation, and regulatory network analysis.

</details>

---

## 9. Where Tabular Foundation Models Falter on Genetic Data: Datasets That Expose and Provide a Path to Address the Gap

- **期刊**: bioRxiv
- **作者**: Das, A., Cui, Y.
- **机构**: Yan Cui @ University of Tennessee Health Science Center
- **日期**: 2026-09-28
- **ID**: DOI: 10.64898/2026.09.25.754520  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.25.754520v1
- **相关分数**: 4/10
- **一句话推荐**: 评估表格基础模型在基因型-表型数据上的泛化问题，涉及基础模型在遗传数据上的局限性分析。
- **方法**: 采用受控层次高斯过程应力测试与合成任务指令微调，评估并修复表格基础模型在基因型-表型预测中的祖先依赖效应漂移问题。
- **主要发现**: 表格基础模型在祖先分散度高的真实基因数据上性能显著下降；通过构建显式编码效应漂移的合成任务进行指令微调，可在不改变基础架构的前提下有效缓解该性能退化。
- **对我的启发**: 利用合成任务进行指令微调以弥补预训练分布与真实数据分布差异的范式，可启发我针对预训练基因组学模型在不同padding策略下引入的分布偏移问题，设计特定的微调任务进行修正。

<details><summary>Abstract</summary>

Tabular foundation models are used as off-the-shelf predictors for heterogeneous tabular tasks, but it remains unclear how they will perform on real genotype-to-phenotype tabular datasets, which carry unique challenges. One such challenge is ancestry-dependent non-stationarity in allele effect sizes (the effects of genetic variation on disease risk): the predictive contribution of a given genetic variant may change significantly across the ancestry spectrum. This is especially consequential for patients from ancestry groups that are underrepresented in existing datasets, because models that are unaware of this non-stationarity are more likely to perform poorly for them. The battery of synthetic tasks used to pretrain tabular foundation models does not capture this structure, and we show that it leads to systematic performance degradation. Using controlled hierarchical Gaussian-process stress tests, we demonstrate that both off-the-shelf TabICL and TabPFN are robust when ancestry dispersion in the data is low, but as dispersion grows, the latent ancestry-dependent non-stationarity of effect sizes becomes a first-order problem, and the predictive performance of both models deteriorates. We confirm the same pattern on All of Us (AoU) (a large biobank containing whole-genome sequencing and electronic health record (EHR) data spanning the ancestry spectrum) across an extensive panel of cancer phenotypes evaluated with the two leading tabular foundation models: TabICL and TabPFN. Holding the in-context training-set size, phenotype, and feature set fixed, ancestry-specific in-context tables, which are less dispersed in ancestry space, consistently outperform size-matched meta-ancestry tables, isolating ancestry dispersion as the driver of degradation. To address the failure without changing the base architecture, we construct two synthetic task families that explicitly encode ancestry-dependent effect drift and instruction-tune an off-the-shelf TabICL model on tasks sampled across both families. On held-out AoU evaluations covering cancer and respiratory disease phenotypes, the tuned model yields more stable performance across ancestry-distance bins and is especially strong in the bins farthest from the center of the in-context exemplars in ancestry space, that is, on subjects whose ancestry is most underrepresented among the provided exemplars. The paper contributes an evaluation protocol, a failure analysis, and two synthetic task families targeted at ancestry-dependent non-stationarity in precision-medicine tabular modeling.

</details>

---
