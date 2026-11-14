# Paper Scout 日报 2026-11-14

共推荐 **7** 篇论文。

## 1. ModBERT: a DNA modification and genetic variant-aware DNA large language model

bioRxiv · 预印本 · 2026-11-13 · 相关性 8/10

**研究关联：方法可借鉴**

- **为什么值得看**：ModBERT 是一种 DNA 语言模型，将 DNA 甲基化和遗传变异纳入预训练表示，直接关联我的 DNA language model 和表观遗传基础模型研究兴趣。
- **任务与验证范围**：输入：五字母概率基因组序列（含群体等位基因频率与CpG甲基化水平） → 输出：个体特异性功能基因组peak分类、染色质可及性及变异效应预测；研究物种：人类；细胞体系：摘要未说明；验证范围：跨个体及跨位点泛化，涵盖11种组蛋白标记和69个转录因子。
- **核心方法**：基于五字母概率基因组表示与软目标掩码语言建模预训练的DNA语言模型，结合概率微调实现个体特异的基因型与甲基化编码。
- **主要发现与证据**：ModBERT在组蛋白和TF ChIP-seq peak分类上优于从头训练及无甲基化预训练模型；在held-out个体和位点的染色质可及性预测达AUROC 0.88，预测变异效应与因果caQTLs相关性达Spearman 0.52。
- **可借鉴点（研究建议）**：将表观遗传特征以概率分布或软目标形式融入序列输入的思路，可推测对构建“虚拟表观遗传特征”的输入表示具有借鉴价值。
- **迁移边界**：原论文侧重个体间变异与甲基化联合建模及泛化，我的任务侧重跨细胞类型增强子活性预测及padding影响；其概率表示方法能否直接迁移到跨细胞类型虚拟特征建模及padding敏感性分析尚未被证明。
- **阅读时核实**：原文在处理不同长度输入序列时采用了何种padding策略，以及padding是否对模型注意力分布和下游预测性能产生显著影响？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.12.766258v1) · [DOI](https://doi.org/10.64898/2026.11.12.766258)

作者：Bolzan, D., Davuluri, R. V., Mahony, S., AY, F.
来源标注的末位/通讯作者：FERHAT AY
机构：La Jolla Institute for Immunology

### 英文摘要

The development of foundation models that learn a general grammar of DNA (DNA language models) has accelerated in recent years. The vast majority of DNA large language models (LLMs), such as DNABERT-2 and Nucleotide Transformer, are pretrained almost exclusively on reference genomes. They therefore cannot represent the two sources of variation most directly tied to regulatory differences between people: genetic variants and DNA methylation. Long-read sequencing (Nanopore and PacBio) now measures both from the same native DNA molecules, but no model is designed to use this joint readout. With this in mind, we developed ModBERT, a DNA language model built on a five-letter probabilistic genome representation in which each position is a distribution over A, C, G, T, 5mC (represented with M). In pretraining, these distributions encode population allele frequencies and CpG methylation levels from 242 individuals in the 1000 Genomes Long-Read Sequencing Consortium, learned with a soft-target masked language modeling objective. We further propose probabilistic fine-tuning, in which the same representation encodes one individual's genotype and methylation. A fine-tuned model can then make person-specific predictions from a single assay. Under this novel fine-tuning framework, we show that ModBERT effectively utilizes methylation information to classify peaks from functional genomic assays, including histone mark (n=11 different marks) and transcription factor binding (n=69 TFs) ChIP-seq data, outperforming ab initio trained models and ModBERT pretrained on sequences without methylation. In silico methylation perturbations yield TF sensitivities that correlate with independent methylation-aware motif models. Using an evaluation design that separates generalization to new loci from generalization to new individuals, ModBERT predicts chromatin accessibility at held-out loci in held-out individuals (AUROC 0.88). Its predicted variant effects agree with likely causal caQTLs (Spearman correlation = 0.52) but not with variants associated only through linkage, a traditionally challenging task. Overall, ModBERT establishes a framework for personal-genome language modeling, in which a model reads each individual's genetic and epigenetic sequence rather than a shared reference. This enables in silico dissection of variant and methylation effects on gene regulation and principled prioritization of candidates for experimental validation as population-scale long-read cohorts (e.g., 1KGP and Human Pangenome Reference Consortium) grow.

---

## 2. Chromatin accessibility predictions reveal lineage-structured effects of noncoding variants across hematopoiesis

bioRxiv · 预印本 · 2026-11-13 · 相关性 8/10

**研究关联：方法可借鉴**

- **为什么值得看**：使用 ChromBPNet（sequence-to-function 模型）预测跨造血细胞类型的非编码变异对染色质可及性的影响，直接涉及细胞类型特异性调控预测和变异效应预测。
- **任务与验证范围**：输入：DNA序列变异 → 输出：变异对染色质可及性的影响效应；研究物种/细胞体系：人类，17种造血细胞类型；验证范围：跨17种造血细胞类型，并与GWAS精细映射及K562 CRISPRi数据集进行对比验证
- **核心方法**：基于ChromBPNet（序列到功能的深度学习模型）预测非编码变异对染色质可及性的影响。
- **主要发现与证据**：在至少一种细胞中可及的242,307个变异中，5.6%被预测会改变染色质可及性，且预测效应反映了造血谱系结构（99.6%的亲子比较中效应方向一致）；模型预测与GWAS精细映射提供互补信息，但在K562 CRISPRi数据中，预测的可及性增加与靶基因验证关联有限。
- **可借鉴点（研究建议）**：可借鉴其跨多个相关细胞类型评估模型预测效应一致性与谱系结构的分析框架，用于推测和评估我的增强子活性预测模型在不同细胞环境下的生物学合理性。
- **迁移边界**：原论文聚焦于变异效应预测及谱系结构分析，而我的任务侧重于游离型增强子活性预测及预训练模型padding影响；不能将原论文跨造血细胞类型的泛化结论或靶基因验证结果直接迁移至我的任务，需独立评估padding策略对序列特征提取的影响。
- **阅读时核实**：ChromBPNet模型在处理输入序列时具体的padding策略是什么，该策略是否可能对边缘区域的变异效应评分产生系统性影响？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.12.766027v1) · [DOI](https://doi.org/10.64898/2026.11.12.766027)

摘要提供的链接（未核验可用性）：[资源 1](https://bloodnnet.ccbr.utoronto.ca/)

作者：Kazemi, M., Morris, J. A.
来源标注的末位/通讯作者：John A Morris
机构：University of Toronto

### 英文摘要

Background. Noncoding variants account for over 90% of genome-wide association study (GWAS) findings, but their mechanisms are often unclear. Sequence-to-function models provide one approach to variant interpretation by predicting the effects of genetic variation on molecular phenotypes. ChromBPNet predicts variant effects on chromatin accessibility, but how these predictions are organized across differentiation hierarchies and relate to orthogonal predictions remains unclear. Results. We trained ChromBPNet models for 17 hematopoietic cell types and scored 302,830 variants. Of 242,307 variants accessible in at least one cell type, 5.6% were predicted to alter chromatin accessibility. Variants active in more cell types had larger predicted effects. Predicted effects also reflected hematopoietic lineage structure, with sharing declining with lineage distance while effect direction was preserved in 99.6% of parent-child comparisons. ChromBPNet predictions agreed with GWAS fine-mapping but largely identified distinct variants. Fine-mapping-only variants were enriched for coding and transcript-associated variation, whereas ChromBPNet-only variants were enriched for regulatory elements, accessible chromatin, and trait-relevant activity. In K562 CRISPRi datasets, predicted accessibility gain showed limited association with target-gene validation. Regulatory elements containing CTCF motifs were less likely to have validated target genes, consistent with a role in chromatin organization rather than gene activation. Conclusions. ChromBPNet and fine-mapping provide complementary information about variant function. Predicted accessibility effects identify the cell types in which noncoding variants are likely to act and capture relationships across the hematopoietic hierarchy, but provide limited information about the genes they regulate. All predictions are available at: https://bloodnnet.ccbr.utoronto.ca/.

---

## 3. A systematic survey of distal element-gene regulatory interactions with Direct-Capture Targeted Perturb-seq

bioRxiv · 预印本 · 2026-11-13 · 相关性 8/10

**研究关联：研究兴趣拓展**

- **为什么值得看**：使用CRISPR扰动技术系统研究远端调控元件（增强子）对基因表达的影响，并指出当前预测模型的局限性。
- **任务与验证范围**：输入：远端调控元件-基因对 → 输出：元件对基因表达的扰动效应量及方向；研究物种/细胞体系：摘要未说明；验证范围：9666个随机远端元件-基因对，摘要未说明是否跨细胞类型
- **核心方法**：结合无偏靶标选择与统计功效评估管线的高通量CRISPR筛选方法（DC-TAP-seq）
- **主要发现与证据**：筛选9666对元件-基因发现，多数降低基因表达的元件效应量<10%（以往研究难以检测）；84个负效应互作中45个(53.6%)位于启动子100kb内；许多元件结合CTCF但缺乏经典增强子染色质特征
- **可借鉴点（研究建议）**：该研究指出预测模型忽略了小效应量元件，提示我在构建增强子活性预测模型时，可考虑将小效应量元件及非经典增强子特征（如CTCF结合）纳入评估体系或训练标签
- **迁移边界**：原论文通过CRISPR实验评估远端元件对基因表达的扰动效应，而我的任务是基于DNA序列和虚拟表观遗传特征预测增强子活性；其实验结论不能直接等同于序列预测任务中的特征有效性，且其单一体系下的结果未必能跨细胞类型泛化
- **阅读时核实**：摘要中提及的“预测模型的局限性”具体指哪些模型？是否涉及基于DNA序列的深度学习模型，还是仅指基于染色质特征的经典回归模型？

[原文](https://www.biorxiv.org/content/10.1101/2025.09.16.676677v1) · [DOI](https://doi.org/10.1101/2025.09.16.676677)

作者：Ray, J., Jagoda, E., Sheth, M. U. et al. (22 authors)
来源标注的末位/通讯作者：Jesse Engreitz
机构：Stanford University

### 英文摘要

Identifying the impact of distal regulatory elements on gene expression is a core challenge in human genetics. Large-scale CRISPR screens have not captured lower effect size element-gene interactions due to selection bias and limited statistical power. We developed a framework for highly powered CRISPR screens, consisting of Direct-Capture Targeted Perturb-seq (DC-TAP-seq), unbiased target selection, and a pipeline accounting for statistical power. Surveying 9,666 random distal element-gene pairs revealed that most elements that reduced gene expression had effect sizes <10%, which prior studies were underpowered to detect. Out of the 84 interactions with negative effects, 45 (53.6%) occurred within 100 Kb of the promoter of the target gene. Many elements were bound by CTCF without classical enhancer chromatin, and both housekeeping and non-housekeeping genes had similar frequencies of distal regulatory elements. We highlight limitations of predictive models and suggest that new models consider elements with smaller effect sizes. Our study provides an expanded view of distal regulatory elements and a framework for building more comprehensive maps of distal regulation.

---

## 4. Bloom unifies brain cell representations across modalities and contexts

bioRxiv · 预印本 · 2026-11-13 · 相关性 7/10

**研究关联：方法可借鉴**

- **为什么值得看**：Bloom 是多模态单细胞基础模型，整合基因表达和染色质可及性并融合基因组序列嵌入，与我的表观遗传基础模型和虚拟细胞研究兴趣高度相关。
- **任务与验证范围**：输入：基因表达、染色质可访问性及基因组序列嵌入 → 输出：细胞表征（用于细胞类型解析、注释、回归、标签转移）；研究物种/细胞体系：成年小鼠脑细胞；验证范围：跨全脑细胞类型及多项下游任务。
- **核心方法**：基于Transformer的模型，通过结合基因组序列嵌入与随机采样的多模态细胞视图学习细胞表征。
- **主要发现与证据**：在仅用30万细胞（比同类模型少约100倍）训练的情况下，Bloom在细胞类型解析及多项下游任务中优于单模态模型，且其注意力机制能揭示相隔数百万碱基对的细胞类型特异性基因组位点关联。
- **可借鉴点（研究建议）**：其结合基因组序列嵌入与表观遗传特征进行联合表征学习的思路，或可推测为增强子活性预测中融合序列与虚拟表观遗传特征提供参考。
- **迁移边界**：原论文聚焦小鼠脑细胞的多模态表征与注释/转移任务，与基于DNA序列预测增强子活性及评估padding影响的任务存在差异，其跨细胞类型或跨任务的泛化效果不可直接套用。
- **阅读时核实**：基因组序列嵌入与多模态细胞视图在模型架构中是如何具体融合的？处理长距离基因组序列时是否涉及截断或padding操作？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.11.765881v1) · [DOI](https://doi.org/10.64898/2026.11.11.765881)

作者：Gala, R., Convy, I., Marghi, Y. et al. (17 authors)
来源标注的末位/通讯作者：Rohan Gala
机构：Allen Institute, Brain Science, Seattle WA, USA

### 英文摘要

Multimodal genomic datasets now profile mammalian brain cells across anatomical regions, developmental stages, disease states, and species. Learning shared representations that capture cellular diversity across these heterogeneous observations remains a central challenge. Here, we introduce Bloom, a transformer-based model that represents cells using gene expression, chromatin accessibility, or both. Bloom is trained on 300,000 adult mouse brain cells with paired measurements, randomly sampled with broad-subclass balancing--approximately 100-fold fewer cells than used by comparable pre-trained models. By combining genomic sequence embeddings with randomly sampled multimodal cell views, Bloom outperforms unimodal cell models in resolving brain-wide cell types and in annotation, regression, and label-transfer tasks. Its attention patterns reveal cell-type-dependent associations among genomic loci, including pairs separated by millions of base pairs. These results establish Bloom as a data-efficient framework for integrating multimodal brain cell measurements and generating hypotheses about cell-type-specific genomic relationships.

---

## 5. Regional Signals Matter: Rethinking Global Pooling for mRNA Foundation Models

bioRxiv · 预印本 · 2026-11-13 · 相关性 7/10

**研究关联：方法可借鉴**

- **为什么值得看**：重新审视 mRNA 基础模型的 pooling 策略，提出区域感知的 readout 方法，与我的基因组基础模型 padding/readout 策略评估研究直接相关。
- **任务与验证范围**：输入：mRNA序列的token级嵌入；输出：mRNA翻译与稳定性等下游任务预测；研究物种/细胞体系：摘要未说明；验证范围：20个冻结模型，涵盖翻译、稳定性等回归与分类任务，摘要未说明是否跨细胞类型。
- **核心方法**：提出架构无关的区域感知读出方法，分别对5'UTR、CDS和3'UTR的token嵌入进行平均池化并拼接，用于线性探测。
- **主要发现与证据**：相比全局平均池化，区域感知池化在翻译和稳定性任务上平均提升11-25%的Pearson相关性，且控制实验证明增益非仅由维度、长度或GC含量解释；在内源转录本分析中，对uAUG相关差异的恢复能力约为全局均值探测的3倍。
- **可借鉴点（研究建议）**：在处理预训练基因组学模型的长序列输入时，可推测对不同功能区域（如增强子核心、侧翼序列或padding区）采用分段聚合策略，可能避免全局池化稀释局部调控信号。
- **迁移边界**：原论文针对mRNA明确的生物学分区（5'UTR/CDS/3'UTR）进行池化，而我的任务涉及DNA增强子及padding处理，增强子内部缺乏明确的先验分区边界，且padding区无生物学信号，直接迁移需重新定义区域划分逻辑；此外跨细胞类型泛化未在摘要中体现。
- **阅读时核实**：在区域感知池化中，对于不同长度或边界的mRNA转录本，模型是如何对齐或处理区域长度差异的？这对我处理变长序列和padding有何具体参考？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.12.766253v1) · [DOI](https://doi.org/10.64898/2026.11.12.766253)

摘要提供的链接（未核验可用性）：[资源 1](https://github.com/Sanford-Labs/rnaregionpooling)

作者：Na, S., Qi, Z., Goyal, D., Huang, J., Yeo, G. W., JIN, W.
来源标注的末位/通讯作者：WENHAO JIN
机构：Sanford Laboratories for Innovative Medicines

### 英文摘要

RNA foundation models with diverse architectures have shown promise for learning representations of messenger RNA (mRNA) sequences. However, existing benchmarks commonly reduce token-level embeddings to transcript-level representations through global mean pooling before fitting a downstream probe. This aggregation does not explicitly preserve the identities of biologically distinct mRNA regions. Consequently, signals associated with short regulatory regions may be diluted, confounding assessments of representation quality with the information preserved by the readout. We introduce an architecture-agnostic, region-aware readout that separately averages embeddings within the 5$'$ untranslated region (UTR), coding sequence, and 3$'$ UTR and concatenates the resulting representations for linear probing. We reproduce mRNABench evaluations for 20 frozen models from 18 families, with a median absolute score difference of 0.0009 across 380 model--dataset--target evaluations published for 19 models, and construct a region-aware benchmark using the same models, tasks, and splits. Relative to global mean pooling, region-aware pooling increases Pearson correlation, averaged across the 20 models, by 11--25\% on translation and stability tasks, with no statistically significant decreases detected for any model on the regression tasks. On classification tasks, relative changes in the area under the precision--recall curve range from $-3\%$ to $+11\%$. Boundary randomization and displacement generally reduce performance, while dimensionality-matched and sequence-composition controls indicate that the gains are not explained solely by increased feature dimensionality, region length, or guanine--cytosine (GC) content. Learned attention pooling approaches region-aware performance only when supplied with one query per region. In silico perturbations reveal stronger sensitivity to upstream AUGs (uAUGs) and their Kozak context, while analyses of endogenous transcripts show approximately threefold greater recovery of length- and GC-adjusted uAUG-associated differences than global-mean probes. Both readouts capture codon optimality. Model rankings averaged over the regression tasks remain largely stable, while within a task models move by several places. Our region-aware benchmark therefore provides a biologically structured and complementary evaluation of mRNA foundation models, revealing regulatory information that is less accessible to linear probes after global mean pooling. The code is available at \url{https://github.com/Sanford-Labs/rnaregionpooling

---

## 6. Graph-guided flow matching enables biologically informed prediction at single-cell resolution

bioRxiv · 预印本 · 2026-11-13 · 相关性 6/10

**研究关联：方法可借鉴**

- **为什么值得看**：使用流匹配+知识图谱预测单细胞扰动后转录组，与我的 single-cell perturbation 研究兴趣间接相关。
- **任务与验证范围**：输入：基因扰动信息、单细胞转录组及生物知识图谱 → 输出：扰动后单细胞转录组；研究物种/细胞体系：摘要未说明具体物种，涉及慢性髓系白血病体系；验证范围：多个大规模Perturb-seq数据集，包含未见单基因和双基因扰动预测
- **核心方法**：融合生物知识图谱与潜在流匹配的生成式框架，用于预测单细胞分辨率的扰动响应。
- **主要发现与证据**：GFM在未见单基因扰动预测上优于现有深度学习基线且训练速度提升30倍，在双基因扰动预测中表现具竞争力，并在慢性髓系白血病中准确预测了HSP90AA1失活的转录后果及新靶点。
- **可借鉴点（研究建议）**：可考虑将先验生物网络（如增强子-启动子互作图谱）作为图引导条件，引入到序列到功能的预测模型中，以约束潜在空间表征。
- **迁移边界**：原论文针对单细胞转录组扰动响应预测，我的任务聚焦DNA序列到增强子活性的映射及预训练模型padding评估，数据模态与预测目标不同，流匹配与知识图谱在序列级预测任务中的迁移效果未经证明。
- **阅读时核实**：知识图谱在模型中具体是如何与流匹配过程耦合的？是作为图神经网络编码器提取节点特征，还是直接作为流匹配轨迹的几何约束？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.12.766125v1) · [DOI](https://doi.org/10.64898/2026.11.12.766125)

作者：Liou, H.-Y., Sprang, M., Selby, D. A. et al. (10 authors)
来源标注的末位/通讯作者：Johnny Kim
机构：TRON - Translational Oncology at the University Medical Center of the Johannes Gutenberg University gGmbH, Mainz, Germany

### 英文摘要

Perturb-seq enables systematic interrogation of massively parallel genetic perturbations at single-cell resolution, yet exhaustive characterization of the full perturbation space remains impractical. Here, we present Graph-guided Flow Matching (GFM), a generative framework that integrates biological knowledge graphs with latent flow matching to predict post-perturbation single-cell transcriptomes. Across multiple large-scale Perturb-seq datasets, GFM outperforms a strong linear baseline and current deep-learning models in predicting unseen single-gene perturbations, while training up to 30x faster and remaining robust with limited training data. GFM also demonstrates competitive performance in the two-gene perturbation prediction task when neither perturbed gene is observed during training. Ablation experiments show that combining flow matching with knowledge graphs enables accurate prediction of perturbation responses. Finally, GFM accurately calculates transcriptional consequences of HSP90AA1 inactivation and identifies target candidates unseen by the model in chronic myeloid leukemia. Our study establishes GFM as a biologically informed generative framework that predicts single-cell perturbation responses for prioritization of therapeutic targets.

---

## 7. DeepRNAi: Predicting on- and off-target siRNA activity and establishing a benchmark

bioRxiv · 预印本 · 2026-11-13 · 相关性 6/10

**研究关联：方法可借鉴**

- **为什么值得看**：基于深度学习和生物基础模型从siRNA/mRNA序列预测on/off-target活性，直接涉及sequence-to-function和序列表示学习。
- **任务与验证范围**：输入：siRNA与mRNA序列 → 输出：on-和off-target敲低活性；研究物种/细胞体系：摘要未说明具体物种，但提及跨物种与细胞模型；验证范围：跨细胞模型、转录本、基因组和物种，并包含区分已批准药物与肝毒性候选药物的小型研究
- **核心方法**：融合生物基础模型提取的转录本上下文特征，构建深度学习模型从序列预测siRNA敲低活性
- **主要发现与证据**：该模型是首个接近实验精度的计算方法，能跨细胞模型和物种泛化；对2440万个siRNA的全基因组调查显示，100个最强效siRNA中有90.1%存在脱靶隐患
- **可借鉴点（研究建议）**：可借鉴其利用预训练生物基础模型提取序列上下文特征以提升下游序列-功能预测任务泛化能力的范式
- **迁移边界**：原论文针对RNA序列预测且跨物种/细胞泛化，我的任务是基于DNA序列及虚拟表观遗传特征预测增强子活性，两者序列模态与机制不同，其预训练特征提取策略在DNA增强子任务中的迁移效果需重新验证，不能直接假设跨任务有效
- **阅读时核实**：模型在融合生物基础模型提取转录本上下文特征时，针对不同长度的mRNA序列输入是如何处理对齐或截断的？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.12.766311v1) · [DOI](https://doi.org/10.64898/2026.11.12.766311)

作者：Masse, N. Y., Lau, T. T. Y., Wintersinger, J. et al. (21 authors)
来源标注的末位/通讯作者：Brendan J. Frey
机构：Deep Genomics Inc

### 英文摘要

Small interfering RNAs (siRNAs) silence target genes through RISC-mediated hybridization and cleavage, but can silence unintended transcripts and cause toxicity or complicate regulatory approval. In drug development, empirical assessment by qPCR and RNA-seq is slow, forces early candidate prioritization, and is limited by available species- and genome-appropriate cell models. While extensive empirical screening remains standard practice, there is a significant opportunity for modern AI methods to change this paradigm. We introduce DeepRNAi, a deep learning model that accurately predicts on- and off-target knockdown from siRNA and mRNA sequence. Trained on 16 million siRNA-transcript pairs from 2,031 siRNAs designed to interrogate known siRNA failure modes, and incorporating transcript context from biological foundation models, DeepRNAi is the first in silico method that approaches experimental accuracy. It generalizes across cell models, transcripts, genomes and species, and in a small study distinguishes approved therapeutics from hepatotoxic candidates. The value of DeepRNAi for prioritizing better candidates up front improving likelihood of success later in development is evidenced by a genome-wide survey of 24.4 million siRNAs targeting 7,946 genes, which indicates that 90.1% of the 100 most potent siRNAs have at least some off-target concerns. To support the community, we are publishing a training and benchmark dataset containing 1.84 million siRNA-transcript pairs from 240 siRNAs.

---

中文笔记基于标题和摘要生成，未核验全文；研究建议不代表论文已验证的结论。相关性分数不是论文质量评分。

检索统计：窗口 [2026-11-11 00:00, 2026-11-14 00:00) UTC；抓取 biorxiv 140/pubmed 82 → 粗筛 39 篇 → LLM 选中 7 篇
