# Paper Scout 日报 2026-11-05

共推荐 **10** 篇论文。

## 1. Synthetic MPRA perturbation supervision improves variant-effect prediction in sequence-to-function models

bioRxiv · 预印本 · 2026-11-03 · 相关性 9/10

**研究关联：方法可借鉴**

- **为什么值得看**：直接探讨使用合成MPRA数据微调Borzoi等sequence-to-function模型以改进变异效应预测，与你的S2F模型和增强子活性研究高度契合。
- **任务与验证范围**：输入：含变异的DNA序列 → 输出：变异对基因表达的效应（MPRA标签）。物种/细胞体系：人类K562细胞系（MPRA数据）、GTEx全血。验证范围：CAGI5启动子变体、GTEx全血eQTL、未见基因的调控基序；是否跨细胞类型：摘要未说明。
- **核心方法**：基于集成模型蒸馏生成合成MPRA扰动标签，进而微调预训练的序列到功能（S2F）模型Borzoi。
- **主要发现与证据**：使用60万个合成样本微调Borzoi后，在CAGI5启动子变体上Pearson相关性从0.28提升至0.54，在GTEx全血eQTL上从0.39提升至0.46，同时保留了预训练在7,611个轨道上的性能，并能恢复未见基因的调控基序。
- **可借鉴点（研究建议）**：可借鉴其利用合成扰动数据微调预训练S2F模型以提升特定任务性能且不破坏原有能力的策略，推测可用于生成虚拟表观遗传特征或增强子活性的合成标签来微调模型。
- **迁移边界**：原论文任务为变异效应预测，我的任务为增强子活性预测及padding影响评估；合成标签策略在变异效应上的成功不能直接等同于在游离型增强子活性预测上的泛化，且padding对模型的影响机制可能与微调策略独立。
- **阅读时核实**：合成MPRA标签的生成过程是否依赖于特定的序列上下文长度，以及Borzoi在微调时如何处理序列padding以避免引入偏差？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.02.763699v1) · [DOI](https://doi.org/10.64898/2026.11.02.763699)

作者：Wang, L., Galvin, J., Vaz, E., Keener, R., Battle, A.
来源标注的末位/通讯作者：Alexis Battle
机构：Johns Hopkins University

### 英文摘要

Deep learning sequence-to-function (S2F) models learn to predict functional readouts, such as gene expression, from genetic sequence. However, these models are trained predominantly on the reference genome and struggle to accurately predict the effect of genetic variation on gene expression. Massively parallel reporter assays (MPRAs) explore the direct impact of genetic variation on gene expression, but saturation-mutagenesis MPRAs that measure variant effects directly remain limited, thereby restricting their use for fine-tuning S2F models. In this work, we investigate fine-tuning Borzoi, a state-of-the-art S2F model, on model-generated synthetic MPRA variant-effect data as a scalable alternative to overcome limits on the availability of supervised training data for genetic variation. First, we trained an ensemble of 16 models on 110,359 K562 MPRA measurements. Then, we distilled their predictions into a single student model using MPRA elements associated with 1,000 genes. The distilled model was subsequently used to generate synthetic variant-effect labels across increasing numbers of genes (50 to 1,000), with 600 variants per gene, to fine-tune Borzoi. Performance improved as we included more genes in training. In data-limited settings, training on more genes with fewer variants per gene performed better than training on fewer genes with more variants per gene, given the same number of total variants. Compared to pre-trained Borzoi, Borzoi fine-tuned on 600,000 synthetic samples across 1,000 genes increased Pearson correlation from 0.28 to 0.54 on CAGI5 promoter variants and from 0.39 to 0.46 on 903 GTEx fine-mapped whole-blood expression quantitative trait loci (eQTLs). Importantly, these improvements were achieved while preserving the pre-trained performance across all 7,611 output tracks. Furthermore, fine-tuned Borzoi recovered regulatory motifs identified by the MPRA model in genes unseen during training, suggesting that learned regulatory features can generalize across loci. Together, these results provide a proof of concept that model-generated synthetic supervision can improve variant effect prediction in S2F models while preserving their original pre-trained capabilities, offering a scalable strategy toward capturing the impact of genetic variation on gene regulation.

---

## 2. Decoding Cell-type Specific Gene Regulation with CellReg3D by Integrating DNA Large Language Models and 3D Genome Structure

bioRxiv · 预印本 · 2026-11-04 · 相关性 9/10

**研究关联：方法可借鉴**

- **为什么值得看**：结合DNA语言模型和3D基因组结构预测细胞类型特异性基因调控和表观遗传标记，直接命中你的核心研究兴趣。
- **任务与验证范围**：输入：DNA序列（DNA语言模型编码）+ Hi-C 3D染色质相互作用数据 → 输出：表观遗传标记、基因表达谱、非编码变异优先级及eQTL解释；研究物种：摘要未说明；验证范围：跨多种细胞类型
- **核心方法**：结合DNA大语言模型与Hi-C 3D染色质相互作用数据的多尺度多模态深度学习框架。
- **主要发现与证据**：模型在预测跨多种细胞类型的表观遗传标记和基因表达谱方面达到SOTA，并能识别细胞类型特异性调控机制及优先排序非编码变异（摘要未说明具体性能数字与基线）。
- **可借鉴点（研究建议）**：可借鉴其利用DNA语言模型提取序列特征以预测表观遗传标记的范式，推测这对我评估预训练模型在虚拟表观遗传特征预测中的表征能力有参考价值。
- **迁移边界**：原论文任务侧重长程基因调控并依赖3D基因组数据，而我的任务侧重游离型增强子活性及序列到功能映射并关注padding影响；其跨细胞类型泛化依赖于多模态数据，不能直接等同于纯序列模型在跨细胞类型上的表现。
- **阅读时核实**：原文是否详细说明了DNA语言模型输入序列的长度限制及处理方式（如截断或padding策略），以及这些处理对下游表观遗传特征预测的具体影响？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.01.763421v1) · [DOI](https://doi.org/10.64898/2026.11.01.763421)

作者：Wang, X., Zhang, Y., Chen, S. et al. (9 authors)
来源标注的末位/通讯作者：Jiangning Song
机构：Monash University

### 英文摘要

Gene regulation is a core biological mechanism crucial for organismal growth and development. Recent advances in deep learning, coupled with increasing computational resources, have enabled large-scale modelling of gene regulatory processes. While numerous models have been proposed, effectively capturing long-range genomic interactions remains a central challenge. Here, we introduce CellReg3D, a multiscale and multi-modal deep learning framework designed to model cell-type-specific gene regulation by integrating local sequence patterns with long-range genomic interactions. Existing approaches often overlook the contribution of 3D genome architecture and face limitations in combining sequence-based features with chromatin interaction data. Specifically, CellReg3D overcomes these gaps by leveraging a DNA language model to encode sequence-level information and incorporating Hi-C-derived 3D chromatin interactions to capture chromatin spatial organization. We demonstrate that CellReg3D effectively learns epigenetic patterns and chromatin activity states, achieving state-of-the-art performance in predicting epigenetic marks and gene expression profiles across multiple cell types. Using interpretable methods, we illustrate how the model identifies cell-type-specific regulatory mechanisms and prioritizes functional non-coding variants. Furthermore, we apply CellReg3D to enhance the interpretation of expression quantitative trait loci (eQTLs) and uncover novel potential gene regulatory interactions. Overall, CellReg3D offers a integrative framework for decoding regulatory genomics, unifying sequence and 3D genome structure data to advance variant prioritization, disease mechanism discovery, and personalized functional genomics.

---

## 3. Predicting single-molecule chromatin distribution from DNA sequence

bioRxiv · 预印本 · 2026-11-04 · 相关性 9/10

**研究关联：方法可借鉴**

- **为什么值得看**：提出sequence-to-distribution框架从DNA序列直接预测单分子染色质状态分布，是S2F范式在单分子层面的前沿延伸。
- **任务与验证范围**：输入：DNA序列 → 输出：单分子染色质状态的概率分布（可及性、甲基化等）；研究物种/细胞体系：摘要未说明；验证范围：摘要未说明是否跨细胞类型，但涉及单分子水平及遗传变异效应预测
- **核心方法**：采用sequence-to-distribution (S2d)框架，从DNA序列直接建模单分子染色质状态的概率分布。
- **主要发现与证据**：基于S2d训练的Mola模型揭示了转录因子与核小体结合的新模式（如ZNF146、YY1的作用），并发现了调控元件共可及性的序列基础，能预测遗传变异对单分子远端调控协调的影响。
- **可借鉴点（研究建议）**：S2d框架直接预测分布而非群体平均值的思路，以及其长上下文建模方法，或许可为增强子活性异质性预测及预训练基因组学模型padding策略评估提供参考。
- **迁移边界**：原论文侧重单分子染色质状态分布预测，而我的任务侧重游离型增强子活性预测及预训练模型padding影响评估；S2d框架在增强子任务上的泛化能力及长上下文对padding的具体影响需独立验证，不能直接等同。
- **阅读时核实**：S2d框架在处理长上下文序列时，其模型架构如何处理序列长度变化或padding，这对预测远端调控协调有何具体影响？

[原文](https://www.biorxiv.org/content/10.64898/2026.10.29.762992v1) · [DOI](https://doi.org/10.64898/2026.10.29.762992)

作者：Wang, R., Jin, J., Pott, S., Zhou, J.
来源标注的末位/通讯作者：Jian Zhou
机构：University Of Chicago

### 英文摘要

Genome regulation unfolds through dynamic and stochastic single-molecule events. Deep learning models that read gene regulatory activities from DNA sequences have markedly advanced our ability to predict cell-population-level averages. However, they cannot capture the full spectrum of heterogeneity and dynamics at the single-molecule level, which directly reflect the underlying mechanisms of genome regulation. Here, we introduce a sequence-to-distribution (S2d) framework that directly models the entire probabilistic distribution of single-molecule chromatin states from DNA sequence alone. We used this framework to train Mola, a model of single-molecule chromatin accessibility. We harness Mola to investigate sequence-based regulatory code and mechanisms for multiple aspects of chromatin regulation at the single-molecule level. By quantifying sequence-driven nucleosome regulation, we reveal distinct modes of transcription factor engagement with nucleosomes, including a novel nucleosome-trapping factor, ZNF146. We characterized the sequence determinants governing the +1 nucleosome after transcription start sites and identified YY1 as the strongest +1 nucleosome-positioning factor. Leveraging long-context single-molecule modeling, we further discovered a shared sequence basis for the co-accessibility of regulatory elements and the co-footprinting of transcription factors. Joint prediction of DNA methylation and accessibility reveals a sequence-driven bimodal state mediated by methylation-sensitive transcription factors. Beyond static single-molecule snapshots, the S2d framework can generate pseudo-dynamic trajectories of chromatin states and propose a roadmap toward genome-wide chromatin dynamics. Moreover, we showed that Mola can predict and interpret the effects of genetic variants at the single-molecule level, revealing how sequence changes reshape distal regulatory coordination. Together, this sequence-to-distribution framework lays the foundation for understanding how genomic sequence encodes stochastic and dynamic genome regulation, and how genetic variation changes it, one molecule at a time.

---

## 4. Spectral Adaptive Repositioning for Flow-Based Single-Cell Perturbation Modeling

bioRxiv · 预印本 · 2026-11-04 · 相关性 7/10

**研究关联：方法可借鉴**

- **为什么值得看**：提出一种用于单细胞扰动建模的生成框架，属于你明确列出的research_interests之一。
- **任务与验证范围**：输入：单细胞扰动数据（遗传、药理、细胞因子） → 输出：全转录组细胞响应预测；研究物种/细胞体系：摘要未说明；验证范围：跨遗传、药理和细胞因子扰动基准测试
- **核心方法**：基于流匹配的生成框架，结合图拉普拉斯谱位置编码与基于隐藏状态的自适应基因位置重定位机制。
- **主要发现与证据**：在多种扰动基准上有效恢复差异基因表达、分布结构和扰动特异性可识别性，且模型捕捉的潜在位置关系与已知转录因子-靶标相互作用高度一致。
- **可借鉴点（研究建议）**：其基于隐藏状态动态调整位置编码的机制，启发我推测在DNA序列模型中可探索自适应位置编码或动态padding策略，以缓解固定padding对增强子功能预测的边界效应，但这需进一步验证。
- **迁移边界**：原论文处理的是基因级共表达网络与扰动响应，而我的任务是DNA序列到增强子活性的映射。图拉普拉斯坐标无法直接迁移至一维DNA序列，且跨任务（扰动响应 vs 序列功能）的泛化能力未被证明，需谨慎评估动态位置机制在局部序列特征提取中的适用性。
- **阅读时核实**：SPEAR中的“自适应重定位”在每一层具体是如何从扰动条件隐藏状态推导并更新基因位置编码的？该机制在处理大规模数据时的计算开销如何？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.02.763678v1) · [DOI](https://doi.org/10.64898/2026.11.02.763678)

摘要提供的链接（未核验可用性）：[资源 1](https://github.com/shouryaverma/SPEAR%7D%7Bhttps://github.com/shouryaverma/SPEAR)

作者：Verma, S., Wang, M., Kadadi, S. D., Lanman, N. A., Mohammadi, S., Grama, A.
来源标注的末位/通讯作者：Shourya Verma
机构：Purdue University

### 英文摘要

Predicting transcriptome-wide cellular responses to genetic and biomolecular perturbations is central to functional genomics and therapeutic target discovery. Existing methods assign gene positional encodings derived from arbitrary orderings or static co-expression masks built from unperturbed cells, and cannot capture the functional rewiring induced by perturbations. We present SPEAR, a generative framework built on two complementary positional mechanisms. Spectral positional encoding grounds each gene's position in the geometry of the co-expression network via continuous coordinates derived from the graph Laplacian. Adaptive repositioning then derives each gene's position from its perturbation-conditioned hidden state at every layer, allowing the attention genes exert on one another to reorganize without explicit supervision. Evaluated on genetic, pharmacological, and cytokine perturbation benchmarks, SPEAR demonstrates excellent recovery of differential gene-expression, distributional structure, and perturbation-specific identifiability. SPEAR also captures latent positional relationships that closely map to known transcription factor-target interactions. https://github.com/shouryaverma/SPEAR}{https://github.com/shouryaverma/SPEAR

---

## 5. Resolving how genetic perturbations act through gene regulatory paths

bioRxiv · 预印本 · 2026-11-03 · 相关性 7/10

**研究关联：方法可借鉴**

- **为什么值得看**：利用参考表观基因组作为支架解析Perturb-seq中的基因调控路径，与单细胞扰动和调控基因组学高度相关。
- **任务与验证范围**：输入：Perturb-seq RNA 测量数据与参考表观基因组 → 输出：TF-调控元件-基因路径使用情况及TF-target关系；研究物种/细胞体系：摘要未说明；验证范围：跨三个CRISPRi筛选（总计240万细胞），与ChIP-seq比对，并预测未参与训练的TF靶标
- **核心方法**：结合参考表观基因组构建的TF-调控元件-基因路径支架，利用共享潜在程序汇集扰动响应以推断调控路径使用情况。
- **主要发现与证据**：在240万细胞的CRISPRi筛选中，推断的TF-target关系与ChIP-seq结合一致性增益比现有最佳方法高4倍以上；能区分直接/间接靶标，预测未见TF靶标，并揭示转录水平未反映的TF活性变化。
- **可借鉴点（研究建议）**：可借鉴其利用参考表观基因组作为先验支架约束模型推断的思路，推测在我的研究中可探索用虚拟表观遗传特征构建增强子-基因调控路径的先验结构。
- **迁移边界**：原论文任务是基于RNA扰动数据推断调控路径，我的任务是DNA序列到增强子活性的预测；原论文将表观组作为静态支架，跨任务迁移需验证表观先验在纯序列模型中的适用性，不能直接假设其泛化能力。
- **阅读时核实**：论文中使用的“参考表观基因组”具体包含哪些特征类型，在模型中是作为静态二值掩码还是连续特征输入？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.02.763749v1) · [DOI](https://doi.org/10.64898/2026.11.02.763749)

作者：Ren, L., Duren, Z.
来源标注的末位/通讯作者：Zhana Duren
机构：Indiana University School of Medicine

### 英文摘要

Perturb-seq measures transcriptional responses to thousands of genetic perturbations, but each gene's response mixes the contributions of many regulatory paths, so how a perturbation acts cannot be resolved from expression alone, however large the model. Here we present REGA-perturb, which supplies this missing information rather than adding model complexity: reference epigenomes define a scaffold of possible transcription factor (TF)-regulatory element-gene paths, and perturbation responses, pooled through shared latent programs, determine how each path is used, requiring only RNA measurements. Across three CRISPR interference screens totaling 2.4 million cells, REGA-perturb inferred TF-target relationships that agreed with ChIP-seq binding with a gain over random more than four times that of the best existing method, separated candidate direct from indirect targets, and predicted targets of TFs withheld from training. It also inferred perturbation-induced changes in TF activity not reflected in TF transcript levels, and resolved perturbation-specific regulatory rewiring in which opposing regulatory changes cancel at the expression level.

---

## 6. Where single-cell foundation models help: a benchmark of annotation, perturbation and regulatory inference against simple baselines

bioRxiv · 预印本 · 2026-11-04 · 相关性 7/10

**研究关联：方法可借鉴**

- **为什么值得看**：评估单细胞基础模型在细胞注释、扰动和调控推断中的表现，与单细胞扰动和基础模型评估高度相关。
- **任务与验证范围**：输入：单细胞转录组数据 → 输出：细胞类型注释、虚拟扰动预测、基因调控网络推断；研究物种/细胞体系：人/小鼠肺、K562细胞系、多种脑类器官及肺癌活检；验证范围：跨物种（人至小鼠）及跨细胞类型/组织体系。
- **核心方法**：对多种单细胞基础模型（如scGPT、Geneformer等）与任务匹配的简单基线（如PCA、共表达网络）进行系统基准测试与对照分析。
- **主要发现与证据**：跨物种标签迁移时基础模型优势显著（Nicheformer准确率0.98 vs 最佳基线0.68）；同物种内其嵌入与PCA注释准确率相当；类器官中预测敲除效应仅12-35%为基因特异性，微调改变分类准确率但不改变敲除排名。
- **可借鉴点（研究建议）**：评估预训练模型时，可借鉴其引入表达匹配对照测试以剥离非特异性效应的思路，这提示我在评估DNA序列模型padding影响时，也需设计严格对照以区分模型真实学习到的序列特征与位置偏置。
- **迁移边界**：原论文针对单细胞转录组基础模型（基因表达矩阵输入），而我的研究针对DNA序列基础模型（核苷酸序列输入）及增强子活性预测；其关于模型增益的结论不能直接平移至序列到功能任务或padding策略的评估上。
- **阅读时核实**：在评估虚拟扰动预测时，如何定义和量化扰动响应的“预期方向”，该评估是否依赖于特定先验知识或数据库？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.03.763968v1) · [DOI](https://doi.org/10.64898/2026.11.03.763968)

作者：Cupaioli, F. A., Merelli, I.
来源标注的末位/通讯作者：Ivan Merelli
机构：CNR-ITB

### 英文摘要

Single-cell foundation models (FMs) are proposed as general tools for cell-type annotation, in silico perturbation and gene-regulatory-network (GRN) inference. To identify where they add value, we benchmarked five FMs (scGPT, Geneformer V1 and V2, Nicheformer, scFoundation), CellOracle, supervised perturbation models including STATE, and task-matched simple baselines on the same data, from K562 Perturb-seq screens and primary cells to healthy-donor and isogenic leukodystrophy brain organoids, a public organoid CRISPR screen and lung cancer biopsies. FMs were most useful when labels had to be transferred across species: from human to mouse lung, Nicheformer reached 0.98 accuracy and Geneformer V2 and scFoundation about 0.90, against 0.68 for the best baseline. Zero-shot in silico perturbations captured the direction of real responses in K562, with up to 75% of perturbations shifted in the expected direction (scFoundation, p < 1e-8), and Geneformer V2 networks recovered patient-level tumour differential expression better than co-expression (fold enrichment 2.9 versus 2.0). Within a species, FM embeddings annotated cells as accurately as principal components. In organoids, predicted knockout effects were largely explained by where the target is expressed, and an expression-matched control test isolated the gene-specific part, 12 to 35% of the effects. Isogenic Canavan and Krabbe organoids and 4H patient organoids, with one library per line and time point, did not yet separate methods from differences between clones and donors, which defines the replication needed for future validation. Fine-tuning changed classification accuracy but not knockout rankings. We release the benchmark, baselines, pipeline checks and the isogenic reference task as the fmaudit package, so that new models can be evaluated on the tasks where FMs already help.

---

## 7. RAPTORGraph: graph-based pathway modeling for causal discovery in single-cell perturbations

bioRxiv · 预印本 · 2026-11-04 · 相关性 6/10

**研究关联：方法可借鉴**

- **为什么值得看**：涉及单细胞扰动建模和因果表示学习，属于你的研究兴趣范畴，但侧重于因果发现和通路建模。
- **任务与验证范围**：输入：单细胞扰动数据（如Perturb-seq） → 输出：未见扰动的下游分析预测及因果表征；研究物种/细胞体系：摘要未说明；验证范围：未见扰动的下游分析（如非加性相互作用），摘要未说明是否跨细胞类型
- **核心方法**：结合图通路编码器的β-变分自编码器（β-VAE），并采用最优传输对齐进行数据预处理以隔离扰动影响。
- **主要发现与证据**：RAPTORGraph在未见扰动的非加性相互作用等下游分析上优于现有SOTA，并在MSE和MMD等客观指标上表现具竞争力。
- **可借鉴点（研究建议）**：其利用最优传输对齐对照与扰动样本以稳定隐空间表征的思路，或许可为预训练基因组学模型在不同细胞类型或条件下的特征对齐提供参考。
- **迁移边界**：原论文处理的是单细胞基因表达扰动数据，而我的研究是DNA序列到增强子活性的预测及padding影响，数据模态和任务目标差异显著，其图编码器和因果发现框架不能直接平移到序列预测任务中。
- **阅读时核实**：摘要中提到的“preconditioning isolates the influence of perturbed genes”具体是如何实现的？它是否依赖于特定的扰动实验设计（如CRISPR敲低）？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.03.763980v1) · [DOI](https://doi.org/10.64898/2026.11.03.763980)

摘要提供的链接（未核验可用性）：[资源 1](https://github.com/sXperfect/RAPTORGraph)

作者：Adhisantoso, Y. G., Schröder, S. K., Gress, M., Hernaez, M., Voges, J.
来源标注的末位/通讯作者：Jan Voges
机构：Institute of Information Processing, Leibniz University Hannover, Hannover, Germany

### 英文摘要

Experiments involving the perturbation of individual cells are central to understanding cellular mechanisms and can accelerate drug discovery. Causal representation learning allows us to uncover the latent factors that regulate biological systems and predict the impact of novel perturbations. Unfortunately, existing methods fail to address intervention spillover in a closed-world setting where intervention targets are known a priori, such as in Perturb-seq experiments, due to their reliance on dense encoders. Furthermore, incorporating curated biological pathways into the model imposes a confirmatory bias, forcing it to explain the data through preexisting pathways and reducing the set of hypotheses the model can explore, while discarding novel signals that lie outside the annotated pathways. In this work, we introduce RAPTORGraph, a {beta}-variational autoencoder with a GraphPathway encoder that explicitly models complex gene-to-gene interactions within learned pathways. Moreover, our model's preconditioning isolates the influence of perturbed genes, yielding clean, single-node latent interventions required for identifiable causal discovery and eliminating spillover. Finally, we train the model on data preprocessed with optimal-transport alignment, which guarantees a well-defined mapping between control and perturbed samples and further stabilizes the learned latent representations. We demonstrate that RAPTORGraph improves state-of-the-art performance on downstream analyses of unseen perturbations, such as non-additive interactions, while performing competitively on objective metrics, such as mean squared error and maximum mean discrepancy. The source code is available at https://github.com/sXperfect/RAPTORGraph.

---

## 8. AdaGeneBudget: Cell-Adaptive Gene-Token Allocation for Efficient Single-Cell Foundation Models

bioRxiv · 预印本 · 2026-11-03 · 相关性 6/10

**研究关联：方法可借鉴**

- **为什么值得看**：探讨单细胞基础模型的基因token分配策略，与你评估基因组基础模型padding策略的项目在token/输入处理层面有概念相似性。
- **任务与验证范围**：输入：单细胞基因表达数据及参考集逆检测频率 → 输出：细胞自适应的基因token子集及嵌入提取结果；研究物种：摘要未说明；细胞体系：PBMC等；验证范围：跨scGPT、Geneformer、scPRINT等模型及Kang、PBMC数据集，涵盖细粒度及低支持细胞类型
- **核心方法**：提出AdaGeneBudget，一种无需训练的、基于表达特异性分数质量最短前缀截断的细胞自适应基因token选择方法。
- **主要发现与证据**：在四个骨干-数据集对中，吞吐量最高提升4.63倍并显著降低内存，同时保留原生注释效用且优于随机和Top-Expression基线；在scPRINT中虽HVG控制macro-F1更高，但本方法更忠实保留了刺激诱导的嵌入方向。
- **可借鉴点（研究建议）**：可借鉴其基于数据内在生物学特征动态决定输入序列长度而非固定截断的思路，推测在DNA序列增强子任务中也可探索基于序列功能特征的自适应padding或长度分配机制。
- **迁移边界**：原论文针对单细胞转录组学的离散基因token选择，而我的任务是基于连续DNA序列的增强子活性预测及padding策略；基因token的“重要性排序”机制不能直接等同于DNA序列的padding或截断，跨模态泛化未经验证。
- **阅读时核实**：摘要中提到的“目标表达特异性分数质量”的具体计算公式和截断阈值是如何设定的，其对极端高表达或极低表达细胞的鲁棒性如何？

[原文](https://www.biorxiv.org/content/10.64898/2026.08.06.743174v1) · [DOI](https://doi.org/10.64898/2026.08.06.743174)

作者：Kim, D., Hwang, U.
来源标注的末位/通讯作者：Uiwon Hwang
机构：Ewha Womans University

### 英文摘要

Single-cell foundation models (scFMs) represent each cell using sequences of gene-associated tokens, making embedding extraction increasingly costly as the number of cells and expressed genes grows. Existing input policies typically rely on fixed input budgets, with retained genes determined by random subsampling, model-native ranking, or a dataset-level highly variable gene (HVG) panel. However, they do not jointly determine, for each cell, which genes to retain and how many tokens to allocate. We introduce AdaGeneBudget, a training-free gene-token selection method that combines each gene's expression with reference-derived inverse detection frequency and retains the shortest ranked prefix that captures a target fraction of the cell's expression-specificity score mass. The resulting cell-specific budget is bounded by minimum and maximum lengths, requires no cell-type labels, and leaves the pretrained backbone unchanged. We evaluated AdaGeneBudget in a frozen-backbone inference setting using pretrained scGPT and Geneformer models on Kang and PBMC reference-mapping tasks, with an additional scPRINT comparison against its official HVG policy and an expressed-only HVG control. Across four scGPT and Geneformer backbone-dataset pairs, AdaGeneBudget substantially reduced mean gene-token counts and peak GPU memory while increasing embedding-extraction throughput by up to 4.63x. Despite this compression, it preserved native-level aggregate annotation utility and numerically outperformed token-matched random and Top-Expression baselines. AdaGeneBudget also preserved fine-grained and low-support cell identities and retained lineage-marker programs and stimulation-associated pathway genes under compression. In scPRINT, both HVG controls achieved higher annotation macro-F1, whereas AdaGeneBudget more faithfully preserved the stimulation-induced embedding direction. These results establish biologically informed, cell-adaptive gene-token allocation as a practical complement to architectural and systems-level efficiency methods for applying existing scFMs to new datasets. They also suggest that cell-adaptive input allocation may be a useful design principle for future models operating under finite token budgets.

---

## 9. Perturbation-induced gene programs map the hidden regulatory architecture of complex diseases

bioRxiv · 预印本 · 2026-11-04 · 相关性 6/10

- **为什么值得看**：开发计算框架学习Perturb-seq中的扰动诱导基因程序，与单细胞扰动及调控架构解析的研究兴趣契合。
- **中文笔记**：生成未成功，请参考下方原始摘要。

[原文](https://www.biorxiv.org/content/10.64898/2026.11.03.762080v1) · [DOI](https://doi.org/10.64898/2026.11.03.762080)

作者：Turhan, B., Lee, H., Liu, D. et al. (11 authors)
来源标注的末位/通讯作者：Kushal K. Dey
机构：Computational and Systems Biology Program, Sloan Kettering Institute, Memorial Sloan Kettering Cancer Center, New York, NY, USA; Physiology, Biophysics and Syst

### 英文摘要

Steady-state molecular profiles incompletely capture the regulatory programs through which genetic variation influences complex disease, particularly programs that emerge only when cells are perturbed. Here, we introduce Perturbscape, a computational framework that learns multiscale gene programs for individual perturbations in a CRISPR Perturb-seq screen using linear and nonlinear contrastive approaches alongside complementary program-learning methods, and integrates them with human genetics to prioritize disease-relevant genes, perturbations and downstream regulatory pathways. Across 15,859 perturbation-by-context profiles from 7 Perturb-seq systems and 53 complex diseases and traits (mean GWAS N=291K), perturbation-induced programs showed up to 4.3-fold higher heritability informativeness than analogous steady-state multi-tissue gene prioritization, and retained significant conditional heritability informativeness across all 34 matched cell system-trait comparisons after accounting for steady-state prioritization. Preserving perturbation-specific programs further yielded 2.5-5.3-fold higher trait relevance scores than programs derived from control cells, pooled perturbations or differential-expression summaries. In K562, Perturbscape-prioritized genes showed stronger enrichment for rare-variant burden genes than steady-state prioritization and were supported by orthogonal enhancer CRISPRi screens. In HepG2, LDL cholesterol-associated perturbation-induced programs specifically revealed statin-responsive pathways not significantly enriched by steady-state PoPS prioritization, supported by pharmacological transcriptional responses and population plasma proteomics. Perturbscape also recovered blood-related trait-conditioned trans-regulatory relationships that were specifically supported by population trans-eQTLs in IFN-gamma-stimulated monocytes (OR = 1.30, P=1.6e-05). Perturbscape further revealed developmental-stage-specific convergence between monogenic diabetes regulators and polygenic T2D risk during pancreatic islet differentiation, and neuronal-subclass-specific autism-associated regulatory programs in vivo. Together, these findings establish perturbation-induced gene programs as a complementary layer of disease-relevant regulatory information, revealing genetically informative pathways and context-specific regulatory relationships incompletely represented by steady-state molecular atlases.

---

## 10. The Segmentome: a novel representation of the DNA methylome identified by a Bayesian HMM framework

bioRxiv · 预印本 · 2026-11-04 · 相关性 6/10

**研究关联：方法可借鉴**

- **为什么值得看**：提出DNA甲基化组的片段级表示以捕获细胞身份，与跨细胞类型表观基因组特征研究间接相关。
- **任务与验证范围**：输入：WGBS数据（CpG甲基化水平、read-pattern熵等） → 输出：基因组甲基化分段表示及细胞类型生物标志物；研究体系：人类39种细胞类型（207个样本）；验证范围：跨细胞类型无监督聚类，并在cfDNA和白细胞样本中验证溯源能力。
- **核心方法**：无监督贝叶斯隐马尔可夫模型，融合多维度甲基化特征推断基因组甲基化状态分区。
- **主要发现与证据**：该方法无需预定义阈值即可有效划分甲基化区域，基于分段特征的无监督聚类能准确区分细胞类型（ARI 0.55, AMI 0.72），且筛选出的标志物可在cfDNA中实现细胞溯源。
- **可借鉴点（研究建议）**：将连续的表观遗传信号转化为离散的分段特征以表征细胞身份，这种特征降维与表示学习思路或许可为构建虚拟表观遗传特征提供参考。
- **迁移边界**：原论文聚焦WGBS数据的甲基化组分段与溯源，与基于DNA序列预测增强子活性的任务存在输入模态和预测目标的本质差异；其跨细胞类型的泛化仅限于甲基化组聚类，不能直接等同于序列模型在跨细胞类型增强子预测上的表现。
- **阅读时核实**：模型在推断“过渡区”时，read-pattern熵和局部CpG相关性具体是如何在HMM的发射概率中建模的？该建模方式对测序深度是否有依赖性？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.01.763464v1) · [DOI](https://doi.org/10.64898/2026.11.01.763464)

作者：Anvari, M., Torki, N., Mehrmohamadi, M.
来源标注的末位/通讯作者：Mahya Mehrmohamadi
机构：University of Tehran

### 英文摘要

Motivation: DNA methylation is organized along the genome into regions of relatively stable methylation (i.e. fully methylated or fully unmethylated regions), separated by transition zones. Differences in the boundaries of these methylation zones across cells can result from various regulatory and epigenetic mechanisms. Most DNA methylome studies, however, are focused on the detection of differentially methylated regions (DMRs), and this organization within a single methylome remains under explored. Furthermore it is unclear whether a segment-level descriptor can capture cell identity. Results: We introduce the segmentome, a segment-level representation of the methylome, and an unsupervised Bayesian hidden Markov model that infers it from WGBS data without predefined methylation thresholds or labels. The model combines CpG methylation levels with read-pattern entropy, local CpG correlation and CpG count to divide the genome into unmethylated, methylated and transition zones, the last characterized by heterogeneous read patterns. Applied to 207 samples of 39 human cell types, segmentome profiles grouped samples by cell type in an unsupervised manner (adjusted Rand index 0.55, adjusted mutual information 0.72). We next generated a segmentome atlas consisting of top segmentome biomarkers per human cell-type. These markers were capable of cell-of-origin determining in cell-free DNA and white blood cell samples. These results suggest that segmentation is a unique framework for analyzing DNA methylome.

---

中文笔记基于标题和摘要生成，未核验全文；研究建议不代表论文已验证的结论。相关性分数不是论文质量评分。

检索统计：窗口 [2026-11-02 00:00, 2026-11-05 00:00) UTC；抓取 biorxiv 213 → 粗筛 44 篇 → LLM 选中 10 篇
