# Paper Scout 日报 2026-10-14

共筛选出 **6** 篇推荐论文。
📊 抓取 biorxiv 140/pubmed 36 → 粗筛 16 篇 → LLM 选中 6 篇

## 1. A high-resolution protein-RNA binding atlas for structure-aware interaction prediction and post-transcriptional regulatory modeling

- **期刊**: bioRxiv
- **作者**: Karimzadeh, M., Fish, L., Karner, H. et al. (13 authors)
- **机构**: Hani Goodarzi @ Arc Institute, University of California, San Francisco
- **日期**: 2026-10-13
- **ID**: DOI: 10.64898/2026.10.12.758580  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.12.758580v1
- **相关分数**: 8/10
- **一句话推荐**: 开发了基于Borzoi的sequence-to-function模型预测RNA调控和变异效应，与你的序列到功能预测及表示学习兴趣高度相关。
- **方法**: 结合高通量ecCLIP数据与结构感知神经网络（Pythia，利用上下文无关文法启发的固定卷积编码RNA二级结构）进行RBP结合预测与转录后调控建模。
- **主要发现**: ecCLIP图谱增强了序列到功能模型对RNA稳定性及变异效应的预测能力；Pythia能准确预测RBP结合，并成功将结合机制分解为序列与结构依赖组件且经高通量实验验证。
- **对我的启发**: Pythia利用上下文无关文法启发的固定卷积显式编码RNA二级结构的思路，可启发我在预训练基因组学模型中设计特定卷积核或位置编码策略，以显式捕捉DNA三维结构或染色质状态等虚拟表观遗传特征，并优化padding区域的特征表达。

<details><summary>Abstract</summary>

RNA-binding proteins (RBPs) control post-transcriptional gene expression by regulating RNA processing, localization, stability, and translation. However, our understanding of RNA regulation remains limited by the resolution, scale, and uniformity of available RBP binding maps. Here we introduce eclair CLIP (ecCLIP), a high-throughput CLIP-seq platform that combines endogenous protein tagging for uniform affinity capture with ligation-free library preparation to generate high-resolution RNA-protein binding profiles. We applied ecCLIP to 67 endogenously tagged RBPs in HEK293T cells, generating a high-quality transcriptome-scale atlas that recovered known binding preferences and captured post-transcriptional regulons linked to RNA half-life. To test the utility of the atlas, we incorporated ecCLIP into Borzuki, a Borzoi-derived sequence-to-function model trained on complementary RNA degradation, expression, CLIP, and Perturb-seq data. Inclusion of ecCLIP data improved RNA half-life prediction and assessment of 3' UTR variant effects on RNA stability, demonstrating that our atlas helps capture RNA dynamics. To directly model the cis-regulatory grammar underlying these RBP-RNA interactions, we developed Pythia, a structure-aware neural network architecture that incorporates context-free grammar-inspired fixed convolutions to explicitly encode RNA base-pairing features. Pythia predicted RBP binding from sequence and structural context and decomposed predictions into sequence- and structure-dependent components. We tested this decomposition for five RBPs using massively parallel reporter CLIP (MPRC) binding assays in cells, using synthetic RNA libraries containing mutations designed to preserve or disrupt predicted RNA structures across nominated binding sites. We used the same MPRC strategy to confirm allele-specific binding effects for variants prioritized by Pythia. Together, ecCLIP and Pythia provide a resource for structure-aware decoding of RNA-protein interaction grammar and interpretation of post-transcriptional regulatory variation.

</details>

---

## 2. Dynamic Graph Prior-Guided Latent Adaptation for Generalizable Single-Cell Perturbation Response Prediction.

- **期刊**: Bioinformatics (Oxford, England)
- **作者**: Yunlong Bie, Peishan Fan, Qijin Yin, Li Xiao
- **机构**: Li Xiao @ Beijing University of Posts and Telecommunications, School of Artificial Intelligence, Beijing, 100876, China.
- **日期**: 2026-10-12
- **ID**: DOI: 10.1093/bioinformatics/btag747  |  PMID: 42865067  |  URL: https://pubmed.ncbi.nlm.nih.gov/42865067/
- **相关分数**: 7/10
- **一句话推荐**: 解决单细胞扰动响应预测中跨未见细胞类型的泛化问题，直接契合你的单细胞扰动和跨细胞类型泛化研究兴趣。
- **方法**: 提出DGP-LA框架，结合细胞状态条件转换模型与扰动特异性稀疏图细化，通过门控机制将动态图先验信号自适应注入潜在表示。
- **主要发现**: 通过动态整合生物学先验知识，模型在未见细胞类型的零样本药物扰动响应预测中表现出卓越的泛化能力，显著提升了预测精度及生物学可解释性。
- **对我的启发**: 其将先验知识动态条件化并作为门控信号注入隐藏层的范式，可启发我将虚拟表观遗传特征作为动态先验，通过门控机制自适应融入预训练基因组学模型的序列表示中，以增强跨细胞类型增强子活性预测的泛化能力。

<details><summary>Abstract</summary>

MOTIVATION: Predicting transcriptional responses to drug perturbations in unseen cellular contexts is a central challenge in single-cell perturbation modeling. This challenge creates a need for models that combine flexible state transitions with structured biological prior knowledge. Existing data-driven models often struggle to generalize across unseen cell types, while many prior-based models rely on static biological graphs without explicitly conditioning prior influence on perturbation-specific target support. RESULTS: We propose DGP-LA, a dynamic graph-prior latent adaptation framework that refines biological priors and injects them as gated latent corrections within a cell-state-conditioned transition model. DGP-LA couples a transition backbone with perturbation-conditioned sparse graph refinement. It propagates gene-aligned target support over the refined graph and selectively injects the resulting topology-aware signal into the hidden representation. On Tahoe and NeurIPS, DGP-LA improves Pearson Delta relative to State by 8.7% and 35.8% for generalization across unseen cell types. In zero-shot drug perturbation response prediction on unseen cell types, it improves Pearson Delta relative to CRISP by 79.1% and 67.6%. The model also improves DE-gene recovery, response discrimination, and Hallmark pathway recovery, supporting adaptive latent integration of biological priors for more generalizable and biologically interpretable perturbation modeling. AVAILABILITY: DGP-LA's source code and reproducibility materials are available at https://github.com/bieyl/DGP-LA and archived on Zenodo at https://doi.org/10.5281/zenodo.22155398. SUPPLEMENTARY INFORMATION: Supplementary data are available at Bioinformatics online.

</details>

---

## 3. BioMod: Biological Module Tokenization for Single-Cell Foundation Modeling

- **期刊**: bioRxiv
- **作者**: Meng, L., Zhu, J., Han, B. et al. (16 authors)
- **机构**: Jinchao Xu @ Shenzhen Loop Area Instutite
- **日期**: 2026-10-13
- **ID**: DOI: 10.64898/2026.10.12.758490  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.12.758490v1
- **相关分数**: 7/10
- **一句话推荐**: 提出基于生物模块tokenization的单细胞基础模型，与你的基础模型和生物序列表示学习兴趣相关。
- **方法**: 提出基于生物模块（通路和基因程序）的语义级Token化方法，结合高比例掩码与非对称解码器构建单细胞基础模型。
- **主要发现**: 使用660个生物模块替代单基因作为输入单元，大幅压缩了模型架构，在多项单细胞下游任务中达到SOTA，且保留了通路级别的生物学组织结构。
- **对我的启发**: 可借鉴其将低维特征聚合为高阶语义模块的Token化思路，探索将增强子序列或虚拟表观遗传特征聚类为共调控模块，以提升预训练模型在序列到功能预测中的表征效率。

<details><summary>Abstract</summary>

Single-cell foundation models typically represent cells as flat sequences of individual genes, requiring higher-order biological organization to be inferred implicitly from sparse expression profiles. Similar to the evolution from character-level to semantic tokenization in natural language processing,we hypothesize that cellular states can be more efficiently represented using biologically meaningful intermediate units. Here we present BioMod, a 50-million-parameter single-cell foundation model that introduces biological modules as representation units between genes and cells. BioMod constructs an overlapping vocabulary of 660 biological modules derived from curated pathways and data-driven gene programs, replacing thousands of gene-level inputs with compact module representations. Pretrained on approximately 73 million human cells using high-ratio module masking with an asymmetric decoder, BioMod achieves state-of-the-art performance across cell-type annotation, zero-shot batch integration, perturbation-response prediction and drug-response forecasting while maintaining a compact architecture that enables efficient inference on a single GPU. Module-level analyses further demonstrate that BioMod captures biologically meaningful cellular programs and preserves pathway-level organization.

</details>

---

## 4. VirtualSkin integrates skin-cell identity with intervention-response prediction

- **期刊**: bioRxiv
- **作者**: Velland, M., Norwick, E., Ardene, S. et al. (10 authors)
- **机构**: Marcus Elian @ Center for Computational Dermatology, Northbridge Institute of Biomedical AI, Boston, Massachusetts, USA; Department of Biomedical Informatics, Halcyon Universi
- **日期**: 2026-10-13
- **ID**: DOI: 10.64898/2026.10.06.756877  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.06.756877v1
- **相关分数**: 7/10
- **一句话推荐**: 提出细胞语言模型用于干预响应预测，与你的virtual cell和单细胞扰动研究兴趣相关。
- **方法**: VirtualSkin，一种对齐单细胞转录组与生物学文本描述的细胞语言模型，支持干预条件下的响应预测。
- **主要发现**: 该模型在跨独立队列的细胞注释、文本检索及干预响应预测上均优于现有方法，且通过消融实验和不确定性估计验证了预测贡献来源及分布偏移下的可靠性。
- **对我的启发**: 论文中利用消融实验定位预测贡献和不确定性估计应对分布偏移的范式，可启发我在评估预训练基因组学模型padding影响时，通过消融实验精确定位padding策略对增强子活性预测的贡献，并引入不确定性量化来评估padding导致的序列分布偏移。

<details><summary>Abstract</summary>

Human skin atlases resolve a diverse set of cellular states, yet connecting these states to their responses to intervention remains difficult across independently sampled tissues. Here we present VirtualSkin, a cell language model that aligns skin transcriptomes with biological descriptions and supports intervention conditioned response prediction. We evaluated the model across independent atlas, disease, anatomical and perturbation cohorts, with donors, studies and perturbations withheld according to the experimental design. VirtualSkin improved inflammatory skin annotation by 0.056 macro F1 points and cell text retrieval by 0.12 Recall@10 points relative to the strongest corresponding comparators. The representation retained cell identity during study integration and transferred across ageing, systemic sclerosis, lymphoma and anatomical sites. Across five intervention cohorts, response prediction improved by 0.03 0.09 response-score points, with agreement at the levels of gene expression change, gene recovery and transcriptional programs. Paired tissue trajectories provided a complementary assessment in two donors per intervention. Component ablations and pairing controls localized the predictive contributions, while uncertainty estimates supported selective prediction under distribution shift. These results connect skin-cell recognition to intervention response prediction within a common evaluation framework and define the conditions under which predictions can inform experimental prioritization.

</details>

---

## 5. LOCALE: Local-Alignment Embeddings for Noise-Robust DNA Search at Scale

- **期刊**: bioRxiv
- **作者**: Synk, R., Pandey, P., Sahinalp, C., Duraiswami, R.
- **机构**: Ramani Duraiswami @ University of Maryland
- **日期**: 2026-10-13
- **ID**: DOI: 10.64898/2026.05.12.724581  |  URL: https://www.biorxiv.org/content/10.64898/2026.05.12.724581v1
- **相关分数**: 6/10
- **一句话推荐**: 涉及DNA序列的表示学习和密集检索，与你的DNA语言模型和序列表示学习兴趣间接相关。
- **方法**: 将DNA序列搜索转化为密集检索任务，采用InfoNCE损失结合生物学启发的数据增强（替换、插入、缺失）训练序列编码器，以学习对变异鲁棒的局部比对嵌入。
- **主要发现**: 该训练策略不依赖特定架构，能跨多种编码器和分词方案生成变异鲁棒表示，在10%基因组变异下召回率显著提升，并在大规模SRA基准上以更低延迟实现远超传统k-mer方法的检索精度。
- **对我的启发**: 利用生物学启发的序列变异（插入/缺失）作为数据增强训练编码器的范式，启发我在评估预训练基因组学模型padding影响时，可探索将不同padding策略与序列变异增强结合，以提升增强子活性预测模型对输入长度变化的鲁棒性。

<details><summary>Abstract</summary>

Searching petabase-scale repositories of raw sequencing data such as the NIH Sequence Read Archive (SRA) could unlock biological insights that remain inaccessible. Existing sequence-search methods either do not scale well or rely on exact $k$-mer matching that is brittle to genomic variation, which is high both within and across species and is further compounded by sequencing error. We recast sequence search as dense retrieval: we learn sequence embeddings whose inner-product similarity ranks locally aligned sequences above unaligned ones. We introduce LOCALE, an encoder trained with an InfoNCE objective on biologically informed augmentations: overlapping crops of parent sequences corrupted with substitutions, insertions, and deletions. This training recipe, rather than a specialized architecture, consistently induces variation-robust representations across four encoders spanning three tokenization schemes, improving Recall@$R_q$ by 7--39 points at 10% genomic variation. On a 50-accession SRA benchmark LOCALE retains 63.2% Recall@$R_q$ at 10% variation while existing k-mer indexes and DNA embedding methods fall below 35%, and on the full 4,571-accession MetaGraph benchmark (296 Gbp, 2.06 billion vectors) it achieves 4.5x the AUPRC of MetaGraph, the state-of-the-art k-mer index, with a single-node GPU IVF-PQ index retaining a 3.6x advantage at MetaGraph's query latency. Our encoder and training strategy generalize to real biological variance: on a cross-genotype Hepatitis B task, querying reads from one genotype against accessions of another with >8% natural divergence, LOCALE reaches 0.813 Recall@R_q versus 0.518 for MetaGraph.

</details>

---

## 6. A split-control criterion for few-shot adaptation in single-cell perturbation prediction

- **期刊**: bioRxiv
- **作者**: Liang, W.-L., Yang, Y.-B., Zhang, Q.-Y. et al. (15 authors)
- **机构**: Rong-Rong He @ Macau University of Science and Technology, Macau, China; Jinan University, Guangzhou, China; Institute for Intelligent Bioinnovation, Knowledge Transfer Center
- **日期**: 2026-10-13
- **ID**: DOI: 10.64898/2026.10.05.756906  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.05.756906v1
- **相关分数**: 6/10
- **一句话推荐**: 关注单细胞扰动预测中的评估方法学问题，与你的单细胞扰动研究兴趣间接相关。
- **方法**: 提出 SafeDelta 分离控制准则，利用校准数据决定单细胞扰动预测中是否进行少样本自适应。
- **主要发现**: 传统评估因共享控制估计导致评分虚高并改变方法排名；采用独立控制评分结合 SafeDelta 能有效抑制误差传递，并在多数据集上保证非负增益。
- **对我的启发**: 在评估预训练基因组学模型 padding 或少样本微调对增强子活性预测的增益时，需采用独立基线对照以避免控制误差传递导致的性能虚高。

<details><summary>Abstract</summary>

Few-shot adaptation can help or harm single-cell perturbation prediction, but conventional evaluation shares a control estimate between calibration responses and held-out targets. We show how methods carry control error into their predictions and derive its contribution to score inflation. Nested control-depth experiments support inverse-depth scaling of inner-product inflation; correlation inflation also depends on the control noise-to-signal ratio. Independent-control scoring changed the rank of 40 of 52 configuration-dataset entries. We introduce SafeDelta, a split-control criterion that uses calibration data to decide whether to adapt. Across six datasets, mean gated gain was non-negative under the original two-control evaluation. On a deep plate, fixed predictions and decisions retained positive mean gains under three additional independent control references. The same reproducibility principle identified a fibrosis programme that localises to scar in human liver. These results inform adaptation decisions and control-depth planning.

</details>

---
