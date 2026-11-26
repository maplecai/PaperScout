# Paper Scout 日报 2026-11-26

共推荐 **3** 篇论文。

## 1. Sequence-to-function embeddings across individuals capture rare and common variant heritability

bioRxiv · 预印本 · 2026-11-24 · 相关性 8/10

**研究关联：方法可借鉴**

- **为什么值得看**：直接探讨序列到功能模型（Borzoi）的中间表示学习及其对变异遗传性的捕获，与DNA语言模型/基因组基础模型的表示学习高度相关。
- **任务与验证范围**：输入：个体DNA序列（经Borzoi模型提取中间层嵌入） → 输出：基因表达遗传力估计；研究物种/细胞体系：人类全血；验证范围：跨个体遗传变异验证，摘要未说明是否跨细胞类型
- **核心方法**：提出方差分量框架EMBHER，利用预训练序列到功能模型（Borzoi）的中间层嵌入来估计基因表达遗传力
- **主要发现与证据**：Borzoi嵌入能恢复全血中基因型解释的大部分遗传力，且表现远超模型最终预测；更深层嵌入更关注功能性和进化受限序列，同时比基因型编码更少祖先信息；嵌入比基因型解释了更多罕见变异遗传力
- **可借鉴点（研究建议）**：可借鉴该论文对预训练模型中间层嵌入的分析范式，推测在我的研究中也可通过评估不同层嵌入对增强子活性预测的贡献，或考察padding策略如何影响中间层表示的功能信息捕获
- **迁移边界**：原论文任务是基于个体间变异估计遗传力，我的任务是预测不同细胞类型增强子活性及评估padding影响；原论文仅在全血验证，未证明跨细胞类型泛化，且未涉及padding策略评估，迁移时需注意任务差异
- **阅读时核实**：Borzoi模型在生成嵌入时，输入序列的长度和padding策略具体如何设定？不同层嵌入对功能序列捕获能力的差异是否受输入上下文长度或padding影响？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.23.768687v1) · [DOI](https://doi.org/10.64898/2026.11.23.768687)

作者：Billeci, F., Anglada-Girotto, M., Gusev, A., Frazer, J., Dias, M.
来源标注的末位/通讯作者：Federico Billeci
机构：Centre for Genomic Regulation

### 英文摘要

Statistical genetics learns how DNA shapes gene expression from variation across individuals, whereas sequence-to-function models learn from variation along the genome. Because sequence-to-function models map sequence to molecular readouts through deep architectures, their intermediate representations could offer function-informed descriptions of genetic variation. Whether these representations capture differences between individuals, however, is unknown. Here we introduce Embedding-based Heritability (EMBHER), a variance-component framework that estimates the expression heritability captured by these representations. Applied to Borzoi, embeddings recover much of the whole-blood heritability explained by genotypes and far exceed the model's final predictions. Deeper layers increasingly prioritize functional, evolutionarily constrained sequence while encoding less ancestry information than genotypes. Embeddings also explain more rare-variant heritability than genotypes, consistent with sharing information across variants too rare to estimate individually. EMBHER integrates sequence-to-function models with statistical genetics, a first step towards population-to-function models.

---

## 2. SparseKG-Flow: A Virtual Cell Generative Architecture Unifying Structural Causal Models and Knowledge Graph Priors for Single-Cell Drug Perturbation Prediction.

Advanced science (Weinheim, Baden-Wurttemberg, Germany) · 期刊文献 · 2026-11-24 · 相关性 7/10

**研究关联：方法可借鉴**

- **为什么值得看**：直接涉及虚拟细胞建模和单细胞药物扰动预测，且关注未见细胞类型/药物的泛化，与研究兴趣高度契合。
- **任务与验证范围**：输入：药物、细胞类型及药物-靶点-通路知识图谱 → 输出：单细胞基因表达扰动响应预测；物种/细胞体系：摘要未说明具体物种，涉及A549细胞系及高级别浆液性卵巢癌患者数据；验证范围：跨未见药物与未见细胞类型，并在卵巢癌患者数据上进行冻结模型评估
- **核心方法**：融合Gumbel-Softmax稀疏门控、异构知识图谱适配器与机制引导残差流的生成式架构。
- **主要发现与证据**：在Tahoe-100M数据集上，Test-NewDrug和Test-NewCell设置下Pearson r分别达0.942和0.920，超越次优基线16.6%和14.8%；在卵巢癌患者数据上展现出初步的跨数据集迁移能力；消融实验表明分子知识适配器对OOD泛化贡献最大。
- **可借鉴点（研究建议）**：可借鉴其引入外部知识图谱先验以提升未见细胞类型泛化能力的思路，推测在增强子活性预测中引入转录因子调控网络先验可能有助于提升跨细胞类型的泛化表现。
- **迁移边界**：原论文任务为基于知识图谱与因果机制的药物扰动转录组响应预测，而我的任务为DNA序列到增强子活性的映射及padding影响评估；其跨细胞类型泛化策略不能直接平移至序列固有表观遗传特征预测，需区分扰动响应与序列基线活性。
- **阅读时核实**：模型在Test-NewCell设置下的跨细胞类型泛化能力，多大程度上依赖于异构知识图谱适配器提供的先验，而非细胞本身的表征？

[原文](https://pubmed.ncbi.nlm.nih.gov/43079208/) · [DOI](https://doi.org/10.1002/advs.78922)

作者：Chongxiao Peng, Menglong Gao, Xinkang Li, Ke Zhang, Hongliang Duan, Henry H Y Tong, Yuguang Mu, Jingjing Guo
来源标注的末位/通讯作者：Jingjing Guo
机构：Engineering Research Centre of Applied Technology on Machine Translation and Artificial Intelligence, Macao Polytechnic University, Macau, China

### 英文摘要

Predicting single-cell responses to new drugs is essential for mechanism-aware virtual cell modeling, yet existing models often fail on unseen drugs or cell types by relying on memorized correlations rather than transferable mechanisms. SparseKG-Flow addresses this out-of-distribution (OOD) challenge as a generative architecture integrating three inductive biases: a sparse drug-effect encoder with Gumbel-Softmax gating, a heterogeneous graph adapter for drug-target-pathway knowledge, and a mechanism-guided residual flow decoder. On Tahoe-100M, it achieves Pearson r of 0.942 and 0.920 under Test-NewDrug and Test-NewCell settings, respectively, outperforming the next-best baseline by 16.6% and 14.8%. It also reduces Δ expression error by 89.0% and 91.7%, respectively, and more than doubles held-out-drug top-gene recovery (Overlap@50 = 0.210). Frozen-model evaluation on high-grade serous ovarian cancer patient data provides preliminary evidence of transfer beyond the Tahoe-100M panel. Ablations confirm all components aid OOD generalization, with the molecular knowledge adapter contributing the most. SparseKG-Flow further reorganizes pharmacological priors into interpretable, task-trained representations and highlights Abemaciclib, Capmatinib, and Gemcitabine in A549 analysis. It thus serves as both an accurate perturbation predictor and a mechanism-grounded virtual cell platform for therapeutic prioritization.

---

## 3. A method to disentangle enhancer-gene interactions from latent factors in single-cell multi-omics data

bioRxiv · 预印本 · 2026-11-25 · 相关性 7/10

**研究关联：研究兴趣拓展**

- **为什么值得看**：提出CREMAP统计方法从单细胞多组学中推断增强子-基因相互作用，直接涉及单细胞调控基因组学计算方法。
- **任务与验证范围**：输入：单细胞多组学数据（染色质可及性与基因表达） → 输出：细胞类型特异的增强子-基因互作图谱；研究体系：人类骨髓、大脑、肾脏细胞及2种细胞系；验证范围：跨13种细胞类型，使用CRISPRi扰动和精细定位eQTL进行验证。
- **核心方法**：基于残差协方差的统计方法（CREMAP），通过从数据中估计潜在因子并予以调整后再检验peak-gene对的关联。
- **主要发现与证据**：相比现有方法，CREMAP在2种细胞系和13种细胞类型中提高了peak-gene连接推断的准确性，并在肾脏近曲小管细胞中保留了被标准协变量方法遗漏的eQTL支持的真实遗传调控连接。
- **可借鉴点（研究建议）**：该论文在推断调控关系前解耦潜在生物学或技术变异的思路，可启发我在基于序列预测增强子活性时，考虑如何分离非特异性的细胞状态或批次效应特征。
- **迁移边界**：原论文是基于单细胞多组学数据的统计推断方法，而我的研究是基于DNA序列的深度学习预测且关注padding影响；CREMAP的跨细胞类型泛化基于多组学数据统计，不能直接等同于序列模型在不同细胞类型上的预测泛化能力。
- **阅读时核实**：CREMAP提取的潜在因子是否包含与DNA序列特征（如特定基序）直接相关的信息，还是纯粹反映细胞状态和技术变异？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.24.768923v1) · [DOI](https://doi.org/10.64898/2026.11.24.768923)

作者：Nguyen, N. D., McNulty, M. T., Kim, G., Han, S. K., Sampson, M. G., Lee, D.
来源标注的末位/通讯作者：Dongwon Lee
机构：Boston Children's Hospital & Harvard Medical School

### 英文摘要

Mapping regulatory elements to their target genes in the cell types relevant to disease is essential for interpreting non-coding variants identified by genome-wide association studies. Single-cell multiome data, which simultaneously measure accessible chromatin and gene expression per cell, allow such peak-gene links to be inferred within individual cell types. However, shared technical and biological variation across genes and peaks, such as cell cycle, cell quality, and inter-sample differences, creates spurious links, while including sample covariates to control for this variation inadvertently removes true genotype-driven links. To address this trade-off, we developed CREMAP (Covariance-of-Residuals-based Enhancer-gene Mapping), a statistical method that estimates shared variation as latent factors from the data and adjusts for them before testing each peak-gene pair. Using CRISPRi perturbation experiments and fine-mapped eQTLs as validation benchmarks, we demonstrate that CREMAP improves the accuracy of inferred peak-gene links compared with existing methods across two cell lines and 13 cell types from human bone marrow, brain, and kidney. In kidney proximal tubule cells, CREMAP retains eQTL-supported and allele-specific links that standard approaches miss when samples are included as covariates. Furthermore, its latent factors capture previously unrecognized global signatures, including a tubular injury program. CREMAP thus enables accurate cell-type-specific peak-gene mapping from single-cell multiome data while preserving genuine genetic regulatory effects.

---

中文笔记基于标题和摘要生成，未核验全文；研究建议不代表论文已验证的结论。相关性分数不是论文质量评分。

检索统计：窗口 [2026-11-23 00:00, 2026-11-26 00:00) UTC；抓取 biorxiv 175/pubmed 78 → 粗筛 36 篇 → LLM 选中 3 篇
