# Paper Scout 日报 2026-10-02

共筛选出 **7** 篇推荐论文。
📊 抓取 biorxiv 157/pubmed 254 → 粗筛 100 篇 → LLM 选中 7 篇

## 1. Scalable saturation mutagenesis reveals gene regulatory architecture and rare variant effects

- **期刊**: bioRxiv
- **作者**: Yuan, H., Huang, X., Auerbach, B., Linder, J., Srivastava, D., Kelley, D. R.
- **机构**: David R Kelley @ Calico Life Sciences LLC
- **日期**: 2026-10-01
- **ID**: DOI: 10.64898/2026.09.30.755794  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.30.755794v1
- **相关分数**: 9/10
- **一句话推荐**: 直接针对sequence-to-function模型的饱和突变扫描提出高效框架Multi-ISM，涉及增强子-基因优先排序和细胞类型特异性调控元件识别，与我的核心研究高度契合。
- **方法**: 将饱和突变扫描（ISM）重构为稀疏恢复问题，实现长上下文序列模型的高效且架构无关的核苷酸分辨率归因分析。
- **主要发现**: 该方法在减少45倍计算量的同时保持预测精度，成功构建大规模组织特异性增强子-基因调控图谱，并显著提升罕见变异的个性化表达预测效果。
- **对我的启发**: 在评估预训练基因组学模型（含padding序列）对增强子活性的归因时，可引入稀疏恢复范式替代逐个突变评估，大幅降低长上下文模型的计算成本。

<details><summary>Abstract</summary>

Long-context sequence-to-function models enable nucleotide-resolution prediction of regulatory variant effects, motivating comprehensive mutational interrogation across broad genomic contexts. Yet conventional in silico saturation mutagenesis (ISM) scores mutations one at a time, requiring millions of model evaluations for a single gene and billions to trillions at genome scales. Here, we introduce Multi-ISM, a scalable framework that reformulates ISM as a sparse recovery problem. Multi-ISM generates mutational maps using 45-fold fewer model evaluations than exhaustive single-variant ISM and matches or exceeds its accuracy on variant-effect benchmarks. Multi-ISM is architecture-agnostic and transfers across large-scale sequence-to-function models. We applied Multi-ISM to 5,000 protein-coding genes, including 3,317 OMIM disease genes, generating base-pair-resolution, tissue-resolved attribution maps across 500-kb windows. These maps supported enhancer--gene prioritization and identification of cell-type-specific regulatory elements. Gene-level summaries of the maps captured regulatory complexity and showed that more constrained genes had smaller predicted mutational effects. Aggregating Multi-ISM predictions into gene-level rare-variant burdens improved personalized expression prediction over a common-variant elastic net, with the largest gains at expression outliers. Multi-ISM makes nucleotide-resolution interpretation of long-context sequence models a routine computation rather than a dedicated effort, so that new architectures, functional readouts, and cellular contexts can be mapped as they appear.

</details>

---

## 2. Deep generative framework for modeling single-cell drug perturbation response.

- **期刊**: Neural networks : the official journal of the International Neural Network Society
- **作者**: Yongqing Zhang, Chenpeng Wu, Tianhao Li, Zhigan Zhou, Zhengxiao Huang, Aochen Zhang, Zixuan Wang
- **机构**: Zixuan Wang @ College of Electronics and Information Engineering, Sichuan University, Chengdu, 610065, China. Electronic address: zixuan98@stu.scu.edu.cn.
- **日期**: 2026-04-15
- **ID**: DOI: 10.1016/j.neunet.2026.109005  |  PMID: 42019216  |  URL: https://pubmed.ncbi.nlm.nih.gov/42019216/
- **相关分数**: 8/10
- **一句话推荐**: 直接讨论virtual cell模型的扰动响应预测能力边界，提出context geometry compression问题和可恢复分辨率评估标准，与我的virtual cell研究兴趣高度相关。
- **方法**: 提出scDPR框架，结合属性适应模块与基于最优传输（OT）的因果图学习模块，预测单细胞药物扰动转录组响应并解耦因果效应。
- **主要发现**: scDPR在预测未见药物转录组响应上优于现有SOTA，能识别导致治疗异质性的关键细胞亚群，且相比主流基础模型具有更高的训练效率。
- **对我的启发**: 利用最优传输（OT）解耦混杂因素以提取直接因果效应的思路，可启发我在跨细胞类型增强子活性预测中，利用OT解耦细胞特异性表观遗传背景噪声，提取纯粹的序列-功能映射关系。

<details><summary>Abstract</summary>

Accurate characterization of cell-specific drug responses is a prerequisite for linking molecular mechanisms to patient-level therapeutic variability. Heterogeneous cellular responses substantially complicate the inference of drug effects from single-cell transcriptomic data. To address this, we introduce scDPR, the single-cell Drug Perturbation Responses framework. This framework predicts drug-perturbed single-cell transcriptomic states and decomposes observed responses into distinct causal effects. The framework consists of two modules: an attribute adaptation module that models drug-induced transcriptional shifts at the single-cell level; and a causal graph learning module that combining optimal transport (OT) infers direct drug effects while accounting for confounding influences. By integrating drug molecular features, dosage information, and cell-specific attributes, the model learns a latent representation that captures cell-specific transcriptional responses to drug perturbations. We conducted systematic evaluations on large-scale single-cell perturbation datasets, including L1000 and sci-Plex3. Experimental results demonstrate that scDPR outperforms state-of-the-art methods such as chemCPA, in forecasting transcriptome responses to unseen compounds and unknown pathways. It also offers insights into the cellular heterogeneity of drug responses, identifying key subpopulations that contribute to variability in treatment outcomes. In addition, compared to mainstream basic models, scDPR achieves better performance with shorter training time and fewer rounds, providing efficient computational support for large-scale drug screening and mechanism research.

</details>

---

## 3. Mendel, a foundation model of human genetic variation, prioritizes regulatory variants and improves gene expression prediction

- **期刊**: bioRxiv
- **作者**: Salman, A., Feng, H., Wei, P., Sun, R., Wu, L., Pan, W., Wu, C.
- **机构**: Chong Wu @ The University of Texas MD Anderson Cancer Center
- **日期**: 2026-09-30
- **ID**: DOI: 10.64898/2026.09.28.755183  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.28.755183v1
- **相关分数**: 8/10
- **一句话推荐**: Mendel是DNA基础模型，以变异为中心的训练目标学习调控变异特征并改进基因表达预测，直接命中基因组基础模型和序列到功能研究方向。
- **方法**: 提出以变异为中心的预训练目标函数，在全基因组序列上从头训练 DNA 基础模型以聚焦等位基因变异。
- **主要发现**: 该模型在 SNV 预测精度上远超现有模型，其预测残差能有效富集因果调控变异，并作为先验显著提升跨组织基因表达预测性能。
- **对我的启发**: 在评估预训练模型 padding 影响时，可重点关注不同 padding 策略对变异位点局部参考对齐上下文的破坏程度，及其对下游增强子活性预测的连锁干扰。

<details><summary>Abstract</summary>

Human genome-wide association studies have identified hundreds of thousands of variant trait associations, but interpreting their mechanistic consequences at allele resolution remains a central bottleneck. DNA foundation models pretrained on genomic sequence corpora learn features predictive of regulatory activity, yet their training objectives are dominated by the conserved background common to all individuals, rather than the sparse variant sites at which human genetic variation is concentrated. Here we introduce Mendel, a DNA foundation model trained from scratch on human whole genome sequences using a variant-centric objective that concentrates supervision on allelic events within reference aligned sequence context. On held-out individuals, Mendel attains 0.984 micro-averaged SNV allele-prediction accuracy, compared with 0.311 for Evo 2. Mendel residual difficulty is selectively enriched at cis-eQTL variants, prioritizes fine-mapped causal variants (AUROC 0.731), where Evo 2 residuals performed near chance, and when converted into a cis-expression prior for modelling, improves prediction relative to an unweighted baseline in all 50 GTEx tissues.

</details>

---

## 4. Cross-species single-cell atlas of the striatum defines cell-type and subregion disease vulnerabilities.

- **期刊**: Cell
- **作者**: Raleigh M Linville, Benjamin T James, Kyriaki Galani et al. (29 authors)
- **机构**: Myriam Heiman @ The Picower Institute for Learning and Memory, Massachusetts Institute of Technology, Cambridge, MA 02139, USA; Department of Brain and Cognitive Sciences, Massachusetts Institute of Technology, Cambridge, MA, USA. Electronic address: mheiman@mit.edu.
- **日期**: 2026-09-01
- **ID**: DOI: 10.1016/j.cell.2026.08.006  |  PMID: 42679819  |  URL: https://pubmed.ncbi.nlm.nih.gov/42679819/
- **相关分数**: 7/10
- **一句话推荐**: 深度生成模型预测单细胞药物扰动响应，直接对应我research interests中的single-cell perturbation和virtual cell方向。
- **方法**: 跨物种单细胞核RNA测序结合GWAS与药理学数据的多模态整合分析。
- **主要发现**: 构建了跨物种纹状体单细胞图谱，揭示了神经元亚群与亚区在神经退行性疾病中的特异性脆弱性及显著的跨物种表达差异。
- **对我的启发**: 无明显直接启发

<details><summary>Abstract</summary>

The striatum is critical for decision-making, movement, and reward processing, functions achieved through subregional cellular and molecular specialization. Striatal cell types and subregions are differentially implicated in neurodegenerative and neuropsychiatric disorders, but the mechanisms underlying these vulnerabilities are poorly understood. Using single-nucleus RNA sequencing across 109 human and 22 mouse samples spanning dorsal and ventral striatum, we provide a comprehensive atlas of subregional neuronal specialization. We define rare neuronal subpopulations and transcriptional gradients along the dorsolateral-ventromedial axis with notable differences between species, suggesting divergent pharmacological targets, connectivity, and disease mechanisms. Integration with genome-wide association and pharmacological studies identifies human-enriched sites of opioid receptor expression and ventral-biased chronic antipsychotic action. Lastly, paired single-cell transcriptomic and somatic trinucleotide repeat expansion measurements identify differences in subregion and neuronal subtype vulnerability in Huntington's disease. Our findings lay the foundation for understanding how striatal cell types and subregions contribute to brain function and neurological disorders.

</details>

---

## 5. Genetic risk and inflammatory signaling converge on cell type-specific regulatory programs in type 1 diabetes

- **期刊**: bioRxiv
- **作者**: Wang, L., Wei, Z.
- **机构**: Zong Wei @ Mayo Clinic Arizona
- **日期**: 2026-10-01
- **ID**: DOI: 10.64898/2026.09.25.753922  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.25.753922v1
- **相关分数**: 6/10
- **一句话推荐**: 使用ChromBPNet从scATAC-seq预测染色质可及性并评估变异对细胞类型特异性增强子的效应，与我的增强子活性预测项目间接相关。
- **方法**: 整合单细胞多组学与GWAS数据，利用ChromBPNet深度学习模型进行碱基分辨率染色质可及性预测及变异效应评估。
- **主要发现**: 发现T1D相关非编码SNP通过改变特定转录因子结合位点的染色质可及性，影响细胞类型特异性增强子活性，进而导致β细胞功能障碍。
- **对我的启发**: ChromBPNet在预测变异对染色质可及性影响中的应用，启发我在游离型增强子活性预测中可利用虚拟表观遗传特征（如碱基突变）来量化序列变异对细胞类型特异性调控的边际效应。

<details><summary>Abstract</summary>

Type 1 diabetes (T1D) is a complex autoimmune disease characterized by the destruction of insulin-producing pancreatic {beta} cells. Both genetic susceptibility and epigenetic dysregulation contribute to T1D risk. Recent studies have reported {beta}-cell dysfunction before disease onset, suggesting that {beta}-cell-intrinsic mechanisms contribute to pathogenesis. However, the mechanistic link between disease-associated variants and {beta}-cell dysfunction remains poorly understood. We hypothesized that a subset of T1D-associated variants directly influences cell type-specific candidate cis-regulatory elements (cCREs) by disrupting transcription factor (TF) binding and altering gene expression. To define cell type-specific cCREs in human islets, we integrated publicly available epigenomic datasets, including bulk histone modification profiles and single-cell multiomic data from human pancreatic islets. We combined these data with T1D genome-wide association study (GWAS) variants to identify disease-associated SNPs located within enhancer regions. Using multiomic datasets from PANC-DB, we characterized cell type-specific chromatin accessibility in nondiabetic and T1D islets and identified regulatory regions that may control gene expression in {beta} cells and other islet cell types. We then applied ChromBPNet, a deep learning model that predicts base-pair-resolution chromatin accessibility from scATAC-seq data, to evaluate how specific variants may alter local regulatory activity. In parallel, we used TF footprinting to nominate TFs likely to bind these variant-containing regions. These analyses identified several T1D-associated SNPs predicted to alter chromatin accessibility at candidate TF binding sites, suggesting mechanisms by which noncoding variants may contribute to {beta}-cell dysfunction and T1D susceptibility. Our findings link T1D-associated variants to cell type-specific enhancer activity and regulatory pathways and provide candidates for future mechanistic studies.

</details>

---

## 6. Population-scale immune multiome atlas reveals regulatory disease mechanisms.

- **期刊**: Nature
- **作者**: Masahiro Kanai, Toni M Delorey, Jarno Honkanen et al. (41 authors)
- **机构**: Ramnik J Xavier @ Center for Computational and Integrative Biology, Massachusetts General Hospital, Boston, MA, USA. xavier@molbio.mgh.harvard.edu.
- **日期**: 2026-09-30
- **ID**: DOI: 10.1038/s41586-026-11078-2  |  PMID: 42816628  |  URL: https://pubmed.ncbi.nlm.nih.gov/42816628/
- **相关分数**: 6/10
- **一句话推荐**: 大规模单细胞多组学揭示增强子-基因调控关系和变异对染色质到表达的级联效应，与调控基因组学和增强子功能理解高度相关。
- **方法**: 群体规模单细胞多组学QTL映射结合大规模并行报告分析（MPRA），构建从染色质可及性到基因表达的因果调控级联。
- **主要发现**: 发现进化保守基因存在多层调控缓冲机制：变异对染色质可及性的影响正常，但通过更弱、更分散的增强子-基因连接在向表达传递时被衰减，解释了疾病变异偏好靶向保守基因的现象。
- **对我的启发**: 论证了顺式调控元件的内在活性（MPRA测得）与下游染色质-表达传递机制的解耦，提示在基于序列预测游离型增强子活性时，需注意其与内源性细胞类型特异性表观遗传调控网络间的非线性映射关系。

<details><summary>Abstract</summary>

Most disease-associated genetic variants lie in non-coding regions1,2, yet mechanistic insights are limited by the lack of an empirical framework for characterizing the molecular consequences of regulatory variation. Single-cell molecular quantitative trait locus (QTL) mapping3,4 connects variants to gene regulation but lacks the power and simultaneous measurements to trace mechanisms from chromatin to expression5. Here we show that population-scale simultaneous profiling of chromatin accessibility and gene expression across immune cells reveals regulatory architectures connecting variants to disease. From paired single-nucleus assay for transposase-accessible chromatin-sequencing (snATAC-seq) and single-nucleus RNA-sequencing (snRNA-seq) analysis of 10 million peripheral blood mononuclear cells in 1,108 Finnish individuals6, we identify 51,083 cis-expression QTLs for 20,829 genes, 338,100 cis-chromatin accessibility QTLs for 210,584 peaks, 119,094 putative causal variants and 593,765 peak-gene links. Variants completing chromatin-to-expression cascades show twice the disease colocalization of chromatin-only effects, with massively parallel reporter assays7 validating 10,428 fine-mapped molecular QTLs. At evolutionarily constrained genes, we identify multilayered regulatory buffering, in which chromatin accessibility changes occur with normal effect sizes, but transmission to expression is attenuated through weaker, more numerous enhancer-gene links. This reconciles why disease variants preferentially target constrained genes despite apparent expression QTL depletion8-11. Analysis using a massively parallel reporter assay7 confirms that this buffering acts downstream of the regulatory element, with constraint operating at the chromatin-to-expression interface rather than on intrinsic cis-regulatory activity. Our atlas provides testable hypotheses for over half of immune disease associations, illustrated by cascades at autoimmune loci (TICAM1 and RHOH) and Finnish-enriched variants (TNRC18 and IL21R).

</details>

---

## 7. The next-generation virtual cell: From spatiotemporal transcriptomic modeling to closed-loop target discovery in complex diseases.

- **期刊**: Life sciences
- **作者**: Mengya Zhao, Xiaofeng Ma, Wei Shi, Yulong Sun
- **机构**: Yulong Sun @ School of Life Science and Technology, Key Laboratory for Space Biosciences & Biotechnology, Institute of Special Environmental Biophysics, Research Center of Special Environmental Biomechanics and Medical Engineering, Engineering Research Center of Chinese Ministry of Education for Biological Diagnosis, Treatment and Protection Technology and Equipment, Northwestern Polytechnical University, Xi'an, Shaanxi Province, 710072, China. Electronic address: yulongsun@nwpu.edu.cn.
- **日期**: 2026-07-24
- **ID**: DOI: 10.1016/j.lfs.2026.124600  |  PMID: 42498177  |  URL: https://pubmed.ncbi.nlm.nih.gov/42498177/
- **相关分数**: 5/10
- **一句话推荐**: 综述讨论下一代虚拟细胞概念，与我的'virtual cell'研究兴趣有概念性关联，但侧重药物发现应用而非序列建模方法。
- **方法**: 综述性论述基于大规模单细胞与空间多组学数据构建“下一代虚拟细胞”的范式，并强调计算预测与高通量湿实验验证的闭环整合。
- **主要发现**: 虚拟细胞的发展不能仅依赖计算规模扩张，需深度解码复杂疾病的生物学上下文，并通过整合类器官等高通量湿实验验证来弥合转录组与蛋白质组间的转化鸿沟。
- **对我的启发**: 启发我在预测游离型增强子活性时，可引入MPRA等高通量实验数据构建“预测-验证”闭环，并关注虚拟表观遗传特征向下游转录/蛋白功能映射的验证鸿沟。

<details><summary>Abstract</summary>

Drug discovery for complex diseases has long been constrained by high developmental costs and suboptimal clinical transition rates. To bridge the "translational gap" between in vitro target screening and in vivo therapeutic efficacy, life science and pharmacological research are undergoing a profound methodological paradigm shift: transitioning from traditional, static biochemical pathway models to "Next-Generation Virtual Cells" predicated on large-scale single-cell and spatial multi-omics data. However, the application of virtual cells should not rely solely on the unconstrained expansion of computational scale. Rather, it necessitates the precise deciphering of the biological context within complex diseases, including tissue-level spatial heterogeneity, multicellular communication networks, and the intricate tumor microenvironment (TME). This work reviews the recent advancements of next-generation virtual cells, focusing on their capacity for high-throughput resolution of drug mechanisms of action (MoA) through transcriptomic perturbation and the decoding of mechanisms underlying immune evasion and acquired resistance. We suggest that to dismantle the barriers between computational prediction and physiological response, it is necessary to deeply integrate in silico predictions with high-throughput wet-lab validation-such as organoid screening and cellular arrays-to establish a rigorous verification loop. By enhancing mechanistic interpretability and addressing the validation gap between transcriptomics and proteomics, the next generation of virtual cells is expected to accelerate the discovery of pharmacological targets and may provide new technological pathways for precision medicine.

</details>

---
