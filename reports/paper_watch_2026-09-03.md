# Paper Watch 日报 — 2026-09-03

共筛选出 **6** 篇推荐论文。

## 1. [P1] CFM-GP: unified conditional flow matching to learn gene perturbation across cell types.

- **作者**: Abrar Rahman Abir, Sajib Acharjee Dip, Liqing Zhang
- **来源**: pubmed  |  **日期**: 2026-08-10
- **ID**: DOI: 10.1093/nargab/lqag087  |  PMID: 42577751  |  URL: https://pubmed.ncbi.nlm.nih.gov/42577751/
- **相关性分数**: 7 / 10  |  **优先级**: P1  |  **值得精读**: 是
- **为什么相关**: CFM-GP用条件流匹配建模跨细胞类型的基因扰动响应，直接对应profile中的single-cell perturbation response modeling。
- **对我而言的新意**: 用连续向量场统一建模共享与细胞类型特异性扰动响应的思路，可启发虚拟细胞中扰动预测模块的设计。

- **核心方法**: 提出基于条件流匹配（Conditional Flow Matching）的生成式框架，以细胞类型为显式条件，学习从对照状态到基因扰动状态的连续向量场。
- **主要发现**: 该统一架构无需为每种细胞类型单独建模，即可同时捕捉共享与特异性的扰动响应，在预测精度和跨物种泛化上超越现有方法，且推断轨迹具有生物学可解释性。
- **对我研究的启发**: 其将细胞类型作为显式条件统一建模共享与特异响应的范式，可启发我在增强子活性预测中引入细胞类型或虚拟表观遗传特征作为条件变量，实现跨细胞类型的统一预测。

<details><summary>Abstract (原文)</summary>

Understanding how gene perturbations reshape cellular states across diverse contexts is fundamental to functional genomics and therapeutic discovery, yet experimental profiling across all perturbations and cell types remains infeasible. Computational approaches promise scalable inference but often rely on discrete mappings or per-cell-type models that fail to capture continuous and shared biological dynamics. We introduce CFM-GP, a conditional flow-matching framework that learns a continuous vector field transforming control expression profiles into perturbed states, explicitly conditioned on cell type. This unified design models both common regulatory programs and type-specific responses within a single architecture, removing the need to train separate models. Across five single-cell perturbation datasets, CFM-GP consistently outperformed existing methods in predictive accuracy, distributional alignment, and cross-species generalization. The inferred flow trajectories recovered canonical signaling pathways and context-dependent transcriptional cascades, demonstrating mechanistic interpretability. By coupling principled generative dynamics with biological conditioning, CFM-GP offers a scalable foundation for modeling cellular perturbation responses, enabling data-driven exploration of gene function and intervention strategies across heterogeneous cellular systems.

</details>

---

## 2. [P2] Virtual single-cell perturbation and genetic causal inference reveal CSF1R-dependent immunometabolic communication in iron metabolism-associated osteoarthritis.

- **作者**: Yue Zhou, Guohang Shen, Lijing Si et al. (7 authors)
- **来源**: pubmed  |  **日期**: 2026-08-27
- **ID**: DOI: 10.1002/ccs3.70107  |  PMID: 42662567  |  URL: https://pubmed.ncbi.nlm.nih.gov/42662567/
- **相关性分数**: 6 / 10  |  **优先级**: P2  |  **值得精读**: 是
- **为什么相关**: 使用了虚拟单细胞扰动建模方法，与我的重要方法之一间接相关。
- **对我而言的新意**: 虚拟扰动在免疫代谢通讯中的应用视角可能对单细胞扰动建模有参考价值。

- **核心方法**: 整合多组学计算框架，结合机器学习优先排序、孟德尔随机化因果推断与虚拟单细胞基因扰动，识别疾病关键调控基因及其下游通路效应。
- **主要发现**: CSF1R是铁代谢相关骨关节炎的核心调控基因，主要通过CD14+CD16+单核细胞-巨噬细胞重塑介导疾病进展；虚拟扰动显示其缺失增强抗原呈递、过表达激活软骨发育通路。
- **对我研究的启发**: 无明显直接启发。

<details><summary>Abstract (原文)</summary>

Iron dysregulation has emerged as a contributor to osteoarthritis (OA), yet the cell-communication mechanisms connecting iron-related genetic signals to joint degeneration remain insufficiently defined. Here, we established an integrative computational framework combining transcriptomic screening, machine learning, Mendelian randomization, immune and metabolite mediation analysis, single-cell transcriptomics, virtual gene perturbation, molecular docking, molecular dynamics simulation, and experimental validation to identify signaling regulators involved in iron metabolism-associated OA. By intersecting iron metabolism-related genes, OA differentially expressed genes, and eQTL-supported genes, we identified 27 shared candidates. Machine learning-based prioritization and genetic causal inference further highlighted CSF1R as a central regulatory gene. Single-cell analysis localized CSF1R expression predominantly to macrophages, indicating a macrophage-centered role in the osteoarthritic microenvironment. Mediation analysis integrating 731 immune-cell traits and 1400 circulating metabolites identified CD14+CD16+ monocytes as a significant cellular mediator linking CSF1R activity to OA susceptibility, suggesting that CSF1R may promote disease progression mainly through monocyte-macrophage remodeling rather than isolated metabolic alteration. Genetic colocalization further supported a shared regulatory signal between CSF1R expression and OA risk. Virtual single-cell perturbation revealed distinct downstream consequences of CSF1R modulation. Simulated CSF1R depletion enhanced antigen processing, major histocompatibility complex class II presentation, and phagosome-related programs, whereas simulated CSF1R overexpression preferentially activated extracellular matrix organization, integrin signaling, and cartilage development-associated pathways. Structural analyses identified stable interactions between CSF1R and candidate inhibitory compounds, and inflammatory stimulation of macrophages confirmed increased CSF1R protein expression. Collectively, this study identifies CSF1R as a macrophage-associated immunometabolic signaling hub linking iron dysregulation to OA. These findings provide a mechanistic basis for targeting CSF1R-mediated monocyte-macrophage communication and offer a computational strategy for prioritizing therapeutic targets in degenerative joint disease.

</details>

---

## 3. [P1] Sparse integrative dictionary learning resolves conserved drug-response states in multiple myeloma (MM).

- **作者**: Mingke Wu, Jin Lu, Qing Ge
- **来源**: pubmed  |  **日期**: 2026-08-08
- **ID**: DOI: 10.1016/j.cancergen.2026.08.002  |  PMID: 42600555  |  URL: https://pubmed.ncbi.nlm.nih.gov/42600555/
- **相关性分数**: 6 / 10  |  **优先级**: P1  |  **值得精读**: 是
- **为什么相关**: PRISM-MM使用稀疏字典学习分解药物扰动转录响应，与profile中single-cell perturbation response建模直接相关。
- **对我而言的新意**: 将scRNA-seq作为校准层保持细胞状态可解释性的扰动响应分解思路，可能对虚拟细胞扰动建模有启发。

- **核心方法**: 基于稀疏整合字典学习的可解释框架，结合单细胞转录组校准层解耦药物扰动下的转录组响应程序。
- **主要发现**: 在多发性骨髓瘤中识别出跨治疗方案的保守响应程序，揭示了分泌活性耗竭与炎症/应激免疫界面状态富集的共性重塑模式，并提名了RFXAP为核心的免疫调控轴。
- **对我研究的启发**: 论文中引入校准层剥离细胞状态背景的思想，启发我在预测不同细胞类型增强子活性时，可考虑引入解耦表示学习分离序列固有特征与细胞类型特异性的表观遗传状态，以提升虚拟特征的纯度。

<details><summary>Abstract (原文)</summary>

Multiple myeloma (MM) is a severe plasma-cell malignancy that continues to cause substantial morbidity and mortality despite major therapeutic advances. Although current therapies target distinct molecular processes, many patients eventually relapse, raising the question of whether diverse treatments impose different pressures that nevertheless converge on shared transcriptional adaptation programs. While many studies have profiled transcriptional changes before and after treatment, these responses are often analyzed within individual drugs, leaving recurrent programs across therapies insufficiently explored. Here, we developed PRISM-MM (Perturbation Response Inference by Sparse integrative Modeling for Multiple Myeloma), an interpretable sparse integrative dictionary-learning framework that decomposes drug-control transcriptional shifts into signed response programs while accounting for drug identity, study background and cell-source state. By incorporating paired scRNA-seq as a calibration layer, PRISM-MM preserved cell-state-level interpretability and outperformed representative perturbation-prediction models in recovering reproducible response structure. Applied to a curated multi-study MM perturbation compendium, PRISM-MM identified conserved treatment-associated programs validated in held-out bulk and external paired scRNA-seq datasets. These programs revealed a recurrent remodeling pattern characterized by depletion of plasma-cell-like secretory activity and enrichment of inflammatory, adhesion-associated and stress-tolerant immune-interface states. We further nominated state-maintaining genes and highlighted a RFXAP-centered immune-regulatory axis that may drive the Program 8 inflammatory adaptation state and shape MM drug response. Together, PRISM-MM provides an interpretable framework for discovering conserved drug-response programs and generating mechanistic hypotheses about treatment adaptation in MM.

</details>

---

## 4. [P2] Integrating heterogeneity into topologically associating domain boundary prediction in large genomic context in human.

- **作者**: Ying Sun, Lars Juhl Jensen, Niels Tommerup et al. (4 authors)
- **来源**: pubmed  |  **日期**: 2026-08-14
- **ID**: DOI: 10.1093/nargab/lqag092  |  PMID: 42602395  |  URL: https://pubmed.ncbi.nlm.nih.gov/42602395/
- **相关性分数**: 5 / 10  |  **优先级**: P2  |  **值得精读**: 是
- **为什么相关**: 基于序列的TAD边界预测，属于sequence-to-function范畴，且考虑了表观遗传异质性（active/inactive chromatin）。
- **对我而言的新意**: 将染色质异质性分层后分别建模的思路，对处理不同表观遗传状态下的序列功能预测有参考价值。

- **核心方法**: 提出一种基于序列组成与基因组元件的机器学习分类模型（TADBpred），针对GC-rich和AT-rich两类异质性TAD边界分别构建预测器。
- **主要发现**: 将TAD边界按染色质活跃状态分类并分别建模，能显著提升预测性能（AUC分别达0.91和0.80），且不同类型边界依赖不同的关键特征。
- **对我研究的启发**: 在预测不同细胞类型增强子活性时，可借鉴其按序列/表观异质性分类建模的思路，对增强子或虚拟表观遗传特征进行分型后分别训练模型，以提升预测精度。

<details><summary>Abstract (原文)</summary>

A fundamental understanding of genome organization relies on accurately annotating topologically associating domains (TADs) and their boundaries. This is crucial for understanding how cis-regulatory elements regulate gene expression. To go beyond calling TADs and boundaries from Hi-C data, several machine learning-based methods have been proposed to go the step further and predict TAD boundaries from genomic sequences. As the growing evidence of TADs and their boundaries, TADs have been proved exhibiting diverse properties, such as differences in replication timing and epigenetic patterns. However, existing methods do not take this heterogeneity into account. To address this, we propose a method called TADBpred for TAD boundary prediction in a large genomic context in humans. TADBpred focuses on TAD boundaries in active and inactive chromatin across cell-lines and tissues, which are GC-rich and AT-rich, respectively. By integrating genomic elements and sequence composition, we designed two models for GC-rich and AT-rich boundaries, respectively. When testing the performance on respective independent held-out datasets, we obtain AUC scores of 0.91 and 0.80. Our results indicate that TADBpred excels in TAD boundary prediction. Additionally, feature importance analysis highlights the essential features for different classes of TAD boundaries, thereby enhancing our understanding of these TAD boundaries.

</details>

---

## 5. [P2] Subcellularly Resolved Single-Cell Embedding Learning with Transcriptomic data, Protein Structure and Localization Information

- **作者**: Zhen Zhou, Jiachen Li, Yuan Liu et al. (5 authors)
- **来源**: arxiv  |  **日期**: 2026-09-02
- **ID**: arXiv: 2609.02344  |  URL: https://arxiv.org/abs/2609.02344
- **相关性分数**: 5 / 10  |  **优先级**: P2  |  **值得精读**: 是
- **为什么相关**: 涉及单细胞表征学习与多模态（序列/结构）整合，与生物序列表征学习间接相关。
- **对我而言的新意**: 亚细胞分辨率的多模态细胞嵌入思路可能对虚拟细胞模型的多模态整合有启发。

- **核心方法**: 基于交叉注意力机制的多模态融合框架，结合转录组、蛋白质序列与结构信息进行亚细胞分辨率的单细胞嵌入学习。
- **主要发现**: 该框架首次在亚细胞水平整合多模态分子信息生成细胞嵌入，有效保留了空间组织生物学信息并捕获了分子表达模式与蛋白质功能特性。
- **对我研究的启发**: 在预测增强子活性时，可考虑利用交叉注意力机制将虚拟表观遗传特征与转录因子蛋白质结构/序列特征进行多模态融合，以提升序列到功能的预测精度。

<details><summary>Abstract (原文)</summary>

Existing cell embedding methods predominantly rely on transcriptomic or proteomic measurements and represent each cell as a holistic entity, thereby overlooking the subcellular localization of individual molecules. Moreover, they rarely incorporate protein structural information, despite its fundamental role in determining molecular interactions and functions. In this work, we propose a multimodal framework for learning subcellularly resolved cell embeddings by jointly leveraging RNA expression profiles, protein sequence representations, and protein structural information. Specifically, we employ a cross-attention architecture to integrate transcriptomic, sequence, and structural modalities and model their interactions within distinct subcellular compartments. The resulting embeddings represent each cell through its fine-grained subcellular organization, capturing both molecular expression patterns and the functional properties of the associated proteins. By learning cell representations at subcellular resolution, our framework preserves spatially organized biological information while integrating complementary signals across multiple molecular levels. To the best of our knowledge, this is the first framework that produces subcellularly resolved cell embeddings by jointly incorporating transcriptomic information, protein sequence representations, and protein structural knowledge within a unified cross-modal learning paradigm.

</details>

---

## 6. [P2] A critical evaluation of Gene Ontology priors in biologically-informed neural networks

- **作者**: Verlaan, T., Lieftinck, M. A., Mwine, W. et al. (4 authors)
- **来源**: biorxiv  |  **日期**: 2026-09-01
- **ID**: DOI: 10.1101/2025.11.06.686983  |  URL: https://www.biorxiv.org/content/10.1101/2025.11.06.686983v1
- **相关性分数**: 4 / 10  |  **优先级**: P2  |  **值得精读**: 是
- **为什么相关**: 评估生物先验知识在神经网络中的作用，其方法论思路对评估基因组学模型中的设计选择（如padding策略）有间接启发。
- **对我而言的新意**: 提供了一种系统评估模型先验知识有效性的实验设计视角。

- **核心方法**: 提出并评估了 GONNECT，一种将 Gene Ontology (GO) 先验知识嵌入自编码器架构的生物信息神经网络（BINN），并引入软链接机制以缓解先验约束。
- **主要发现**: GO 先验结构对模型重构或潜在空间组织性能提升有限，其核心价值在于将编码器节点激活组织成具有生物学意义的可解释单元；引入的软链接虽能恢复性能但稳定性差，主要起补偿先验约束的作用。
- **对我研究的启发**: 在将虚拟表观遗传特征作为先验约束引入增强子活性预测模型时，应区分评估其对预测性能与特征可解释性的影响，并考虑引入软约束机制以补偿先验可能带来的信息损失。

<details><summary>Abstract (原文)</summary>

Biologically-informed neural networks (BINNs) embed prior knowledge such as the Gene Ontology (GO) into their architecture to produce structurally interpretable representations, yet whether and how this prior improves performance or interpretation remains unclear. Here, we introduce GONNECT, a BINN incorporating GO into an autoencoder. We evaluate GO constraints in the encoder, decoder, or both on RNA-seq tumour samples from The Cancer Genome Atlas (TCGA), comparing against published BINNs (OntoVAE and VEGA), randomized-prior controls, and an unconstrained baseline. Across metrics, GO structure adds little to reconstruction or latent-space organization, frequently matched by randomized or unconstrained models. Its value lies in node activations, particularly in the encoder, where they correlate with a gene set enrichment analysis (GSEA)-derived reference. GONNECT-SL introduces regularized connections outside GO, but these soft links are unstable across seeds and concentrate where the ontology is sparse, appearing to compensate for the priors constraints rather than reveal new biology. They recover near-unconstrained reconstruction, keeping encoder activations interpretable. We identify the soft-link encoder as most promising. Our results clarify what biological priors contribute: their value lies not in the identity of the imposed connections or in improved performance, but in organizing activations into biologically meaningful units that can be interrogated directly.

</details>

---
