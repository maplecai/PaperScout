# Paper Scout 日报 2026-09-12

共筛选出 **10** 篇推荐论文。
📊 抓取 arxiv 20/biorxiv 755/pubmed 65 → 粗筛 100 篇 → LLM 选中 10 篇

## 1. Causal variant underestimation is a major overlooked driver of sequence-to-function model underperformance

- **期刊**: bioRxiv
- **作者**: Drusinsky, S., Pollard, K. S.
- **机构**: Shiron Drusinsky @ Gladstone Institutes
- **日期**: 2026-09-11
- **ID**: DOI: 10.64898/2026.09.08.750172  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.08.750172v1
- **一句话推荐**: 直接评估了state-of-the-art的sequence-to-function模型（AlphaGenome）在变异效应和增强子活性预测上的系统性不足。
- **方法**: 基于最先进的序列到功能（S2F）模型AlphaGenome，系统比较精细定位eQTL与邻近非因果SNV的预测效应大小，以评估模型精细定位因果变异的能力。
- **主要发现**: S2F模型普遍低估因果变异效应，主要归因于未能检测到变异对增强子活性的局部效应及增强子-基因连接不足；但最显著的0.1%预测高度富集真实因果变异且方向可靠。
- **对我的启发**: 在评估基于虚拟表观遗传特征的增强子活性预测模型时，需特别关注模型对远距离增强子-基因连接及局部变异效应的捕捉能力，避免因padding或上下文截断导致因果变异效应被低估。

<details><summary>Abstract</summary>

Deep learning sequence-to-function (S2F) models represent tremendous promise for functionally fine-mapping causal variants associated with traits and disease. Yet it remains unclear precisely how effective they are at this task. Generally, S2F models perform well at classifying putatively causal expression quantitative trait loci (eQTL) SNVs, yet dramatically underperform linear baselines at ranking different individuals' gene expression values from their whole genome sequence, which directly calls into question their ability to fine-map a locus by properly weighting the effects of variants onto gene expression. Here, using the state-of-the-art S2F model AlphaGenome, we systematically compared predicted effect sizes for fine-mapped eQTLs to nearby putatively non-causal SNVs, finding that AlphaGenome pervasively underestimates the effects of most causal variants and fails to successfully fine-map eQTLs in most loci for this reason. We show that misdirected variant effect predictions and negative cross-individual correlations, widely cited as major challenges facing S2F expression modeling, are not egregious errors but a chance consequence of weak, noisy attributions when causal variants are underestimated. Our results suggest that a failure to detect local variant effects onto enhancer activity is a cause of underestimation. Additionally, we find that underestimated variants are enriched far from their target gene, suggesting inadequate enhancer-gene linking causes underestimation even when local effects are well-detected. Finally, our results clarify when S2F models are reliable for fine-mapping objectives: while they pervasively underestimate most causal variants, demonstrating limited fine-mapping utility for most loci, the top 0.1 most prominent variant effect predictions are strongly enriched for causal variants with directionally correct predictions that are consistent across model replicates, suggesting extremely strong predictions are broadly trustworthy. Our results demonstrate that causal variant underestimation is a core issue facing S2F expression predictors, with future improvements dependent on better local activity detection and enhancer-gene linking.

</details>

---

## 2. DNT: Diploid Genomic Foundation Model

- **期刊**: bioRxiv
- **作者**: Leib, G., Zinger, T., Ofer, D. et al. (21 authors)
- **机构**: Guy Leib @ Cancer Research Center and Wohl Institute of Translational Medicine, Sheba Medical Center, Tel Hashomer, Israel
- **日期**: 2026-09-11
- **ID**: DOI: 10.64898/2026.09.05.749576  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.05.749576v1
- **一句话推荐**: 属于基因组基础模型（DNA language model）范畴，探讨了二倍体基因型的输入表示和tokenizer设计。
- **方法**: 基于参考对齐的二倍体编码与相位保留分词器，结合对比相位损失（CPL）对Nucleotide Transformer进行持续预训练。
- **主要发现**: 将二倍体基因型及相位信息编码为单序列输入，显著提升了模型对复合杂合子变异的判别能力，而未区分相位的模型表现接近随机。
- **对我的启发**: 在构建增强子变异序列输入时，可借鉴其单序列二倍体编码策略以保留等位基因特异性信息，避免因单倍体拆分或padding截断丢失顺式作用元件的协同效应。

<details><summary>Abstract</summary>

Clinical interpretation of genetic variation depends on the diploid genotype, including zygosity, allele dosage and whether multiple variants occur in cis on the same homologue or in trans on different homologues. Most genomic language models process haploid sequences or combine independently encoded haplotypes downstream, so they do not directly represent the paired genotype in a single sequence. We introduce a reference-aligned diploid encoding for single-nucleotide variants (SNVs) and short insertions and deletions (indels), together with unphased and phase-retaining tokenizers that accept phased genotypes and convert them to single-sequence diploid representation. Using Nucleotide Transformer v3 backbones, we continue training 8-million- and 100-million-parameter models and evaluate an auxiliary Contrastive Phase Loss (CPL) designed to retain the phasing information of the variants in contextual representations. We evaluate on a novel compound-heterozygous benchmark containing 9,460 examples. Models whose inputs did not distinguish relative phase remained near chance, whereas our diploidic models improved discrimination with AUROC 0.649, compared to 0.506 for the vocabulary-adapted control. These findings establish a method for making diploid genotype information accessible to genomic language models, rather than a universal improvement in variant prediction; validation in naturally observed, accurately phased clinical cohorts remains necessary.

</details>

---

## 3. PHAROS: turning single-cell perturbation models into target-directed drug-combination screens

- **期刊**: bioRxiv
- **作者**: Bezney, J., Ruggeri, C., Borra, F., Qi, L. S., Buffa, F. M., Steinmetz, L. M.
- **机构**: Jon Bezney @ Stanford University
- **日期**: 2026-09-10
- **ID**: DOI: 10.64898/2026.09.08.749477  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.08.749477v1
- **一句话推荐**: 基于预训练单细胞扰动模型构建虚拟细胞级别的药物组合筛选框架，直接命中我的 single-cell perturbation 和 virtual cell 研究兴趣。
- **方法**: 基于预训练单细胞扰动模型的链式预测与搜索算法，实现无重训练的靶点导向药物组合虚拟筛选。
- **主要发现**: 该框架无需重训即可在体外及患者数据中准确恢复双药组合响应，并能显式识别模型分布外数据，实现逆向单细胞虚拟筛选。
- **对我的启发**: 预训练模型显式识别分布外数据的机制，可启发我在评估不同padding策略对增强子预测影响时，量化模型对未见细胞类型的泛化边界。

<details><summary>Abstract</summary>

Combination therapies are central to cancer treatment, but exhaustive screening is impractical. We introduce PHAROS, a framework that turns a pretrained single-cell perturbation model into a target-directed search engine for drug combinations. PHAROS predicts how a cell population changes under a drug, one drug at a time, then chains these predictions together to simulate drug combinations. It scores each simulated outcome against the desired target state and uses a search algorithm to find the most promising combinations, all without retraining the underlying model. Across two independent combinatorial perturbation datasets, PHAROS recovered exact or mechanism-matched two-drug responses in cell lines, both seen and unseen during model training. Its rankings were specific to the requested conversion and were not explained by single-drug effects, additive effects, or shared mechanism of action. In exploratory analyses of patient-derived metastatic HR+/HER2$-$ breast tumors and basal cell carcinoma (BCC), PHAROS prioritized FDA-approved regimens, distinguished combinations by their predicted tumor-versus-immune objective profiles, and nominated pathway-level hypotheses, while explicitly identifying both tumor cohorts as outside the model's supported distribution. PHAROS provides a modular route from pretrained virtual-cell models to inverse, single-cell combination-screening platforms.

</details>

---

## 4. Looplook: Integrating multiomics refinement and graph clustering for target assignment and functional inference of chromatin regulatory networks

- **期刊**: bioRxiv
- **作者**: Zhang, Y., Huang, X., Chen, H., Xie, L., Chen, Y., Xu, L.
- **机构**: Liang Xu @ Institute of Biochemistry, College of Life Sciences, Zhejiang University, Hangzhou 310058, China
- **日期**: 2026-09-10
- **ID**: DOI: 10.64898/2026.04.03.715516  |  URL: https://www.biorxiv.org/content/10.64898/2026.04.03.715516v1
- **一句话推荐**: 开发了整合3D染色质拓扑与功能基因组学的计算框架，用于CRE-靶基因链接。
- **方法**: 整合连通分量图聚类与多组学数据精炼的3D染色质拓扑-功能基因组学联合计算框架。
- **主要发现**: 通过结合3D染色质互作与表达/表观特征精炼功能性染色质环，该方法在准确分配远端调控元件靶基因方面显著优于传统线性注释策略。
- **对我的启发**: 在构建增强子活性预测模型的训练标签时，可借鉴其表达/染色质感知的精炼策略，结合3D互作信息过滤无功能的游离型增强子，以提升ground truth质量。

<details><summary>Abstract</summary>

Deciphering target genes regulated by cis-regulatory elements (CREs) is critical for translating genetic and epigenomic findings into clinically actionable insights. However, linking distal CREs to their cognate target genes remains a fundamental challenge due to the limited availability of computational tools for spatial annotation and the oversimplified assignments inherent to conventional topology-only strategies. A flexible framework that integrates 3D proximity with transcriptional output is urgently needed. To address these limitations, we develop looplook, an integrated computational framework that bridges 3D chromatin topology with functional genomics to enable accurate, flexible, and user-driven CRE-target gene assignment. Looplook provides four core capabilities: (1) robust consensus building for denoising and consolidating replicated or multi-source chromatin loops by employing connected component clustering; (2) bidirectional spatial annotation between 3D chromatin loops and diverse linear genomic features, offering optional graph-based high-order discovery and a linear fallback for gapless network resolution; (3) an expression- or chromatin-aware refinement algorithm that selectively retains functional loops; and (4) automated downstream functional profiling seamlessly integrated with customizable multi-track visualization. Through case studies of the FOSL2 and BRD4 cistromes in liposarcoma cells, we demonstrate that looplook outperforms conventional linear annotation methods by integrating chromatin interactions with expression data and chromatin profiles, offering a powerful and valuable framework for distilling experimental omics data into functionally interpretable high-order gene regulation networks. looplook is freely available as an open-source R package, with source code and documentation hosted on GitHub, and will be distributed via the Bioconductor repository.

</details>

---

## 5. Disagreement-Informed Arbitration for Gene Regulatory Network Inference: A Score-Level Meta-Classifier and a Diagnostic Typology of Inter-Method Conflict.

- **期刊**: Bio Systems
- **作者**: Ihor Kendiukhov
- **机构**: Ihor Kendiukhov @ Institute of Medical Genetics and Applied Genomics, University of Tübingen, Tübingen, Germany. Electronic address: kenduhov.ig@gmail.com.
- **日期**: 2026-09-11
- **ID**: DOI: 10.1016/j.biosystems.2026.105937  |  PMID: 42727749  |  URL: https://pubmed.ncbi.nlm.nih.gov/42727749/
- **一句话推荐**: 涉及单细胞扰动数据上的基因调控网络推断和机器学习集成方法。
- **方法**: 基于梯度提升树的分数级元分类器，利用多种基因调控网络推断方法的边级原始分数进行逐边动态权重分配与集成仲裁。
- **主要发现**: 逐边仲裁集成优于简单平均，但评估协议比模型更重要：标准边级交叉验证因目标基因泄漏导致性能虚高，隐式参数化基因的图/嵌入方法在目标基因留出时性能断崖式下降。
- **对我的启发**: 在评估预训练基因组学模型预测增强子活性及padding影响时，需严格审查交叉验证协议，防止因序列重叠或同源区域未留出导致的数据泄漏，避免高估模型真实泛化能力。

<details><summary>Abstract</summary>

Gene regulatory network inference methods routinely disagree about individual edges, and practitioners resolve those conflicts by choosing one method or averaging them all. We ask whether the conflict can instead be arbitrated per edge. A gradient-boosted classifier is trained on the raw scores that ten inference methods-correlation-based, information-theoretic, sparse-regression and tree-ensemble, including GENIE3, GRNBoost2, CLR and ARACNe-assign to each candidate regulator-target pair, so that the weight given to each method varies from edge to edge. Across six single-cell perturbation screens spanning four cell types, arbitration improves on mean ensembling by +0.056 AUROC on Adamson and +0.083 on Shifrut under target-grouped cross-validation. The evaluation protocol turns out to matter more than the model. Edge-level cross-validation, standard in this literature, inflates apparent gains by 0.060 AUROC through target-gene leakage-comparable to the entire honest improvement. The effect is far larger for methods that represent genes implicitly: a supervised graph-attention link predictor trained on identical folds scores AUROC 0.930 under edge-level cross-validation, better than anything else we evaluate, and 0.533 once target genes are held out. Any method that parameterises genes is exposed, which covers most graph- and embedding-based approaches. A five-category typology of inter-method conflict localises where arbitration pays off, with the largest gains on edges where the methods disagree and the smallest where they already agree, while adding nothing as model input; we therefore report it as a diagnostic instrument rather than a modelling contribution. We also characterise what the ground truth measures: most perturbed genes in widely used screens are not transcription factors, and a mediation screen bounds how much of the perturbation response can be direct.

</details>

---

## 6. Biology-in-the-loop: Amortized Adaptive Hit Discovery in CRISPR Screens

- **期刊**: arXiv
- **作者**: Carl Edwards, Edward De Brouwer, Xiner Li, Namkyeong Lee, Ehsan Hajiramezanali, Anne Biton, Sara Mostafavi, Gabriele Scalia
- **日期**: 2026-09-10
- **ID**: arXiv: 2609.11877  |  URL: https://arxiv.org/abs/2609.11877
- **一句话推荐**: 涉及CRISPR筛选（扰动）中的自适应实验设计，结合了Transformer和LLM先验。
- **方法**: 提出AssayLoop框架，结合跨历史实验训练的Transformer获取策略与LLM生物学先验，进行自适应序列实验设计。
- **主要发现**: 跨历史CRISPR筛选数据学习获取策略并结合LLM先验，能显著提升自适应命中发现效率，且该策略随训练数据增加而提升并具备跨表型泛化能力。
- **对我的启发**: 跨历史实验数据学习策略的范式，启发我在增强子活性预测中利用跨细胞类型的历史表观数据预训练Transformer，以提升虚拟表观遗传特征在未见细胞类型上的泛化能力。

<details><summary>Abstract</summary>

Many biological discovery problems require experiments to be selected sequentially under constrained budgets. CRISPR screening is a prominent example, as exhaustive perturbation testing is often infeasible and candidate perturbations must instead be prioritized over multiple experimental rounds. Despite the importance of this problem, existing benchmarks for adaptive hit discovery remain limited in scale and diversity. Here, we introduce AssayBench-Loop, a large-scale benchmark for adaptive hit discovery comprising 1,389 CRISPR screens across five phenotype categories. Beyond enabling systematic evaluation, its scale makes it possible to learn acquisition strategies across historical experiments. Building on this resource, we introduce AssayLoop, a sequential experimental design framework combining AssayFormer, a transformer-based amortized acquisition policy trained across historical screens to adapt from experimental feedback, with LLM-derived biological priors through an adaptive handoff. In this view, completed experiments become training data for learning how accumulated evidence should guide what to test next, while LLMs provide prior biological knowledge to seed the search. We further introduce AssayLLM, showing that the same principle can be extended directly to an LLM through task-specific post-training. On temporally held-out screens, AssayLoop achieves a 5.67-fold enrichment over random selection and recovers 27.7% of hits after assaying approximately 5% of the candidate library, outperforming existing adaptive-design methods and standalone LLMs, and AssayFormer alone. Performance improves with increasing historical training data and transfers to phenotype categories excluded from training. These results demonstrate the value of learning acquisition policies across historical experiments and combining them with broad biological priors for efficient adaptive hit discovery.

</details>

---

## 7. Learning the Language of the Microbiome with Transformers

- **期刊**: bioRxiv
- **作者**: Treloar, N. J., Ur-Rehman, S., Yang, J.
- **机构**: Neythen J Treloar @ Outpost Bio
- **日期**: 2026-09-10
- **ID**: DOI: 10.64898/2026.05.02.722381  |  URL: https://www.biorxiv.org/content/10.64898/2026.05.02.722381v1
- **一句话推荐**: 微生物组领域的 GPT 式基础模型，涉及 tokenization 策略、预训练 scaling behavior 和下游任务泛化，与我的基因组基础模型/padding 策略研究有方法论上的间接关联。
- **方法**: 基于GPT-2架构的自监督因果语言模型预训练，构建微生物组基础模型。
- **主要发现**: 大规模自监督预训练能显著提升下游任务性能，且在数据量超1万时Transformer稳定优于传统方法；分词策略和数据规模对模型质量有关键影响。
- **对我的启发**: 论文强调tokenization策略对模型质量有显著影响，这启发我在处理变长增强子序列及padding策略时，需系统评估不同序列离散化或分词方式对预训练基因组学模型表征能力的影响。

<details><summary>Abstract</summary>

Self-supervised pretraining has become central to biological machine learning, yet microbiome data remains comparatively underexplored in terms of both modeling approaches and evaluation frameworks. To address this gap, we present Atlas, a pretraining dataset of 539,308 microbiome datapoints from the MGnify database. Using Atlas, we train the Waypoint family of microbiome foundation models: a series of GPT-2 style causal language models ranging from 6M to 170M parameters. We also introduce Compass, a curated benchmark of eight predictive tasks spanning biome classification, drug-microbiome interactions, drug degradation, and infant gut development. Using this benchmark, we compare the performance of Waypoint models against classical baselines and the existing MGM foundation model. Our results show that pretraining leads to consistent and significant improvements in downstream task performance, that both dataset scale and tokenization strategy impact model quality, that pretraining is essential for achieving favorable scaling behavior and that representations learned during pretraining generalise between microbiome domains. Furthermore, pretrained transformer models begin to reliably outperform classical methods once training data exceeds roughly 10,000 examples - a threshold that is attainable for modern microbiome studies. Finally, we demonstrate that the Waypoint models achieve state-of-the-art performance among microbiome foundation models. Overall, our work highlights the importance of large-scale self-supervised pretraining in this domain and establishes Atlas, Compass, and the Waypoint models as valuable resources for the research community in this emerging field.

</details>

---

## 8. Source of genome-wide deleterious variation in a global cattle cohort

- **期刊**: bioRxiv
- **作者**: Gao, J., Derks, M., Schipstal, J. v. et al. (13 authors)
- **机构**: Richard P. M. A. Crooijmans @ Wageningen University & Research
- **日期**: 2026-09-11
- **ID**: DOI: 10.64898/2026.09.07.749866  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.07.749866v1
- **一句话推荐**: 开发了类似CADD的变异致病性预测工具，结合了表观遗传和调控注释，属于计算基因组学。
- **方法**: 基于逻辑回归整合进化约束、表观遗传及调控等多维特征，构建牛基因组核苷酸级变异有害性评分模型（BovCADD）
- **主要发现**: 该模型能有效区分致病变异并对非编码区变异进行评分，揭示了特定群体和性状相关位点的有害遗传负荷
- **对我的启发**: 该研究在非编码区变异评分中整合了表观遗传和调控注释，提示在预测增强子活性时，可考虑将虚拟表观遗传特征与进化约束等先验生物学特征结合以提升预测性能

<details><summary>Abstract</summary>

Background Identifying deleterious DNA changes underpins efforts to improve animal health, welfare, and sustainable breeding. In cattle, current variant prioritization focuses on coding changes, uses single annotation types, and gives limited resolution in non-coding sequence. Results We developed BovCADD (bovine Combined Annotation-Dependent Depletion), a nucleotide-level deleteriousness score for substitutions in Bos taurus and Bos indicus, combining evolutionary constraint, sequence context, epigenetic and regulatory annotations, and gene and protein features. A logistic regression model trained on 41.9 million high-frequency derived alleles from about 3,700 cattle, contrasted with context-matched simulated variants, scored all 8.1 billion possible substitutions. BovCADD distinguished known pathogenic variants from background variation, discriminated among variants within the same consequence class, and scored intronic and intergenic sites. Aggregating scores identified genes carrying rare deleterious variation and revealed elevated genetic load at trait-relevant loci and in bottlenecked, intensively selected populations. Conclusions BovCADD provides the first genome-wide, nucleotide-resolution measure of deleteriousness in cattle, extending variant interpretation to non-coding sequences and linking variant-level prioritization to population-level patterns of mutational burden. Precomputed scores for all substitutions are publicly available.

</details>

---

## 9. Sequence-Informed Geometric Evaluation of RNA 3D Structures

- **期刊**: arXiv
- **作者**: Andrea Zerio, Yighua Yao, Alessandro Micheli, Roland G. Huber, Mile Sikic, Samir Bhatt, Andres R. Masegosa, Yuangang Pan
- **日期**: 2026-09-09
- **ID**: arXiv: 2609.10644  |  URL: https://arxiv.org/abs/2609.10644
- **一句话推荐**: 使用预训练RNA语言模型的核苷酸嵌入进行结构评估，属于生物序列表示学习的交叉应用。
- **方法**: 提出SIRGE评估器，通过融合预训练RNA语言模型的核苷酸嵌入对3D几何结构表示进行条件化评估。
- **主要发现**: 序列条件化能纠正纯几何模型的评估错误，预训练序列表征可为RNA 3D结构评估提供互补的排序信息，显著提升Top-1/Top-3等排名指标。
- **对我的启发**: 预训练序列表征对结构/功能评估具有互补增益，这启发我在基于序列预测增强子活性时，可探索将预训练语言模型的嵌入与虚拟表观遗传特征进行条件化融合，以纠正单一模态的预测偏差。

<details><summary>Abstract</summary>

Computational RNA structure pipelines generate many candidate conformations for the same sequence. Reliable evaluation therefore requires more than recognising plausible geometry, it requires determining whether that geometry is compatible with the sequence. We introduce SIRGE, a sequence-informed geometric evaluator that conditions structural representations on nucleotide embeddings from a pretrained RNA language model. Early results show that SIRGE outperforms established evaluators in Kendall--$τ$ alignment, Top-1 selection, and Top-3 ranking. Controlled comparisons further show that sequence conditioning corrects errors made by an otherwise matched geometric model and improves target-level rank structure. These findings provide initial evidence that pretrained sequence representations supply ranking information that complements geometric reasoning.

</details>

---

## 10. Reference-guided pseudotime inference across species and biological contexts

- **期刊**: bioRxiv
- **作者**: Rittenhouse, N., Dannenfelser, R., Filippova, G. N., Yao, V., Deng, X., Disteche, C. M., Zhang, R.
- **机构**: Ran Zhang @ University of North Carolina - Chapel Hill
- **日期**: 2026-09-10
- **ID**: DOI: 10.64898/2026.09.04.749461  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.04.749461v1
- **一句话推荐**: 跨物种/条件的单细胞伪时间推断框架，其跨上下文迁移学习的思路对跨细胞类型泛化有间接启发。
- **方法**: 提出Cavebear框架，基于参考物种/条件的单细胞转录组时间序列数据，通过迁移学习指导查询物种/条件的伪时间推断。
- **主要发现**: 该框架能跨物种和条件转移时间信息，在缺乏可靠时间标签的生物背景下实现更准确的发育伪时间推断及疾病进展映射。
- **对我的启发**: 其参考引导的跨域知识迁移范式，可启发在跨细胞类型增强子活性预测中利用高资源细胞系的表观特征作为参考，指导低资源细胞类型的功能映射。

<details><summary>Abstract</summary>

Cells collected at the same chronological age can vary substantially in biological age due to the heterogeneity in the timing of differentiation, speed of maturation, and degeneration. However, existing pseudotime inference methods either disregard chronological time information, or rely on accurate time-series labels within similar species or biological conditions of interest. As a result, both types of strategies often fail to faithfully order cells from biological contexts without reliable time labels, along the desired axis of interest such as human embryonic development or disease progression. Here, we propose Cavebear, a machine learning framework that enables pseudotime inference in a query species or condition guided by scRNA-seq time-series profiles from a reference species or condition. Cavebear achieves more accurate developmental pseudotime inference than existing methods and provides in vivo temporal mapping for in vitro experiments. Furthermore, we illustrate the potential of Cavebear to study cellular-level disease progression in human patients using mouse cancer development models as references. By transferring temporal information across species and conditions, Cavebear enables systematic investigation of biological variation in contexts where such annotations were previously unattainable.

</details>

---
