# Paper Scout 日报 2026-11-19

共推荐 **6** 篇论文。

## 1. GENECraft: A Function- and Prior-Constrained Discrete Dynamical System for Controllable Regulatory DNA Design

bioRxiv · 预印本 · 2026-11-18 · 相关性 9/10

**研究关联：方法可借鉴**

- **为什么值得看**：将基因组语言模型与sequence-to-function预测器（AlphaGenome）结合用于调控DNA设计，直接命中enhancer design和sequence-to-function研究方向。
- **任务与验证范围**：输入：目标调控功能与约束条件 → 输出：满足功能且符合基因组先验的DNA序列；研究物种/细胞体系：摘要未说明；验证范围：2,185个位点（涵盖启动子、多约束增强子和18个转录因子），是否跨细胞类型摘要未说明
- **核心方法**：提出无需训练的推理时优化离散动力学系统（FP-DDS），通过融合功能效用、双向上下文先验和组成质量惩罚的复合向量场，耦合基因组语言模型与序列到功能预测器进行序列生成。
- **主要发现与证据**：在2,185个位点上，GENECraft的联合成功率达62.70%（启动子）、65.23%（增强子）和94.56%（TFs），远超7个基线（增强子最高仅2.15%）；消融实验表明引入gLM引导使二核苷酸差异降低7.8-11.5%，增强子上下文敏感性降低10.5%。
- **可借鉴点（研究建议）**：论文在推理时耦合gLM与序列到功能预测器以平衡功能与序列合理性的思路，启发我在增强子活性预测任务中，可探索利用预训练模型的上下文先验来约束或校准序列到功能预测器的输出。
- **迁移边界**：原论文聚焦于生成式设计任务（推理时优化序列生成），而我的任务是判别式预测已知序列的增强子活性及评估padding影响；原论文未验证跨细胞类型泛化，其生成框架中的先验约束机制不能直接等同于预测任务中padding对模型性能的影响。
- **阅读时核实**：在FP-DDS框架的推理时优化过程中，功能预测器和基因组语言模型是如何处理不同长度输入序列的？是否涉及padding操作，且该操作对生成序列的功能评估和上下文先验打分有何影响？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.16.767190v1) · [DOI](https://doi.org/10.64898/2026.11.16.767190)

作者：Wang, J., Xu, T., Tan, C., Zhong, W., Guo, G., Zhang, L., Qiu, Z., Li, S. Z.
来源标注的末位/通讯作者：Jue Wang
机构：Westlake University

### 英文摘要

Designing regulatory DNA requires reconciling two complementary modeling paradigms: genomic language models (gLMs) capture evolutionary syntax without guaranteeing targeted regulatory activity, whereas sequence-to-function predictors provide explicit functional supervision without enforcing native-like sequence plausibility. We introduce GENECraft, a training-free Function- and Prior-Constrained Discrete Dynamical System (FP-DDS) that couples a genomic language model (Carbon) and a functional oracle (AlphaGenome) during inference-time optimization to balance predicted regulatory activity and consistency with genomic sequence priors. GENECraft evolves continuous latent nucleotide logits while evaluating strictly decoded discrete DNA sequences under a time-dependent composite vector field that fuses normalized functional utility, bidirectional contextual prior guidance, and compositional quality penalties, followed by feasibility-first trajectory readout. Across 2,185 loci spanning promoters, multi-constraint enhancers, and 18 transcription factors (TFs), GENECraft achieves full-joint success rates of 62.70%, 65.23%, and 94.56% (macro-averaged), substantially outperforming seven optimization, evolutionary, and generative baselines (which reach at most 2.15% on enhancers). In matched 336-locus ablations, in-loop Carbon guidance reduces native-relative dinucleotide divergence by 7.8--11.5%, enhancer context sensitivity by 10.5%, and TF mutation sensitivity by 11.0%, establishing FP-DDS as a principled framework for controllable regulatory DNA design.

---

## 2. Regulatory grammar design of tissue-specific enhancers across species

bioRxiv · 预印本 · 2026-11-18 · 相关性 9/10

**研究关联：方法可借鉴**

- **为什么值得看**：利用sequence-to-function oracle设计跨物种组织特异性增强子，直接命中enhancer design和cell-type-specific enhancer研究方向。
- **任务与验证范围**：输入：motif词汇表与序列到功能预测模型 → 输出：具有组织特异性的增强子序列；研究物种/体系：跨物种（小鼠、人类、斑马鱼、果蝇）；验证范围：跨组织/细胞类型，含转基因小鼠胚胎、人类细胞等实验验证。
- **核心方法**：提出REGAL框架，利用强化学习在序列到功能预测模型的指导下，显式编程增强子的调控语法（转录因子motif的组合与空间排布）以生成序列。
- **主要发现与证据**：REGAL设计的增强子在转基因小鼠中驱动了预期的谱系特异性表达，在人类细胞中优于核苷酸级优化器，并在斑马鱼和果蝇中以更短长度达到或超越现有设计；实验证明组织特异性依赖于motif组成与空间组织。
- **可借鉴点（研究建议）**：REGAL所依赖的序列到功能预测模型在处理多细胞类型特异性时的特征利用方式，或许能为我的虚拟表观遗传特征预测模型提供特征工程或输入表示上的参考。
- **迁移边界**：原论文属于序列生成任务，核心是强化学习结合oracle模型；我的任务属于判别式预测及预训练模型padding分析。原论文跨物种、跨组织的生成有效性不能直接等同于预测模型在跨细胞类型上的泛化能力，且两者在模型架构和输入处理上存在本质差异。
- **阅读时核实**：REGAL所依赖的序列到功能oracle模型的具体网络架构是什么？它在处理不同物种或组织输入时，如何对序列长度进行对齐或padding处理？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.17.767007v1) · [DOI](https://doi.org/10.64898/2026.11.17.767007)

作者：Yao, L., Tran, M. N., Ruffus, A. S. et al. (9 authors)
来源标注的末位/通讯作者：Liangqi Xie
机构：Department of Microbial Sciences in Health, Cleveland Clinic Research, Cleveland Clinic, 9500 Euclid Avenue, Cleveland, OH 44195, USA

### 英文摘要

Enhancers encode tissue-specific gene expression through the combinatorial identity, number, and arrangement of transcription factor motifs, collectively known as regulatory grammar. However, existing deep-learning methods directly optimize nucleotide sequences, leaving enhancer regulatory grammar implicit. Here we introduce REgulatory Grammar Architecture via reinforcement Learning (REGAL), a framework that explicitly programs enhancer grammar under sequence-to-function oracles. REGAL generated tissue-specific enhancers across species using the same placement architecture with interchangeable oracles and motif vocabularies. Experimental validation and perturbation revealed that tissue specificity requires coordinated target-tissue activation and off-target repression, depends on both motif composition and spatial organization, and employs distinct regulatory strategies across tissues. REGAL-designed enhancers drove predicted lineage-specific expression in transgenic mouse embryos, outperformed a nucleotide-level optimizer in human cells, and matched or exceeded leading designs in zebrafish and Drosophila at notably shorter length. Together, these findings establish regulatory grammar as a programmable and experimentally testable substrate underlying enhancer design and specificity.

---

## 3. MINA: Do frozen DNA encoders beat sequence composition? A homology-aware linear-probe benchmark

bioRxiv · 预印本 · 2026-11-17 · 相关性 8/10

**研究关联：方法可借鉴**

- **为什么值得看**：系统评估了冻结DNA编码器（如NT-v2, DNABERT-2）的表示能力，并重点探讨了pooling等评估策略对模型性能的影响，与你的活跃项目2（评估预训练基因组基础模型策略）高度相关。
- **任务与验证范围**：输入：人类基因DNA序列（CDS及TSS窗口） → 输出：蛋白质家族5分类及GenePT文本摘要嵌入回归；研究物种/细胞体系：人类基因（3,244个）；验证范围：摘要未说明跨细胞类型（聚焦于序列级基因功能，未涉及表观遗传或细胞特异性）
- **核心方法**：基于同源感知划分的线性探针基准测试，对比冻结预训练DNA编码器与序列组成基线在基因功能预测上的线性可分性。
- **主要发现与证据**：冻结DNA编码器在CDS上的表现仅略优于核苷酸组成（macro-F1 0.693 vs 0.639），远不及氨基酸组成或ESM-2；评估策略（如池化方法、序列区域选择、数据划分方式）对分数的影响极大，随机划分会因同源序列泄露导致分数虚高（0.693升至0.801）。
- **可借鉴点（研究建议）**：在评估预训练基因组学模型在增强子预测任务中的表现时，我应严格控制序列输入区域、池化策略和数据划分方式，并引入简单的序列组成基线，这对评估padding等输入预处理策略的独立影响具有方法论参考价值。
- **迁移边界**：原论文任务为基因级编码区同源性分类，我的任务为非编码区跨细胞类型增强子活性预测及padding影响评估。原论文关于同源泄露的结论不能直接等同于增强子任务中的motif泄露，但其“评估细节显著影响模型表现”的结论及控制变量的评估框架可跨任务迁移。
- **阅读时核实**：在对比不同池化策略导致模型性能大幅波动时，论文是否讨论了不同序列长度处理方式（如截断、补齐padding）对冻结编码器特征提取或线性探针性能的潜在影响？

[原文](https://www.biorxiv.org/content/10.64898/2026.05.25.727711v1) · [DOI](https://doi.org/10.64898/2026.05.25.727711)

作者：Wijaya, A. S., Leung, H.
来源标注的末位/通讯作者：Austin Senna Wijaya
机构：Columbia University

### 英文摘要

Frozen DNA encoders are widely used as feature extractors, but fine-tuning hides what their fixed embeddings already make linearly accessible. MINA is a lightweight benchmark that asks whether those embeddings beat sequence composition, with two linear probes on 3,244 human genes: 5-way classification into coarse protein families, and regression onto each gene's GenePT text-summary embedding. Mostly, they do not. On coding sequence (CDS) under a homology aware split, the validation-selected encoder, NT-v2, recovers coarse family signal at about the level of nucleotide composition (macro-F1 0.693 vs. 0.639; Holm p = 0.108) but does not reach amino-acid composition (0.767) or the protein language model ESM-2 (0.954). On GenePT, DNABERT-2 beats nucleotide composition (R2 0.065 vs. 0.039) but not amino-acid composition (0.080). Evaluation choices move scores as much as the encoder does: pooling alone takes NT-v2 from 0.504, below nucleotide composition, to 0.698; a mostly noncoding transcription-start-site window, where any signal is likely regulatory rather than family, drops NT-v2 from 0.694 to 0.300 on the same genes; and a random split inflates it from 0.693 to 0.801 through homologous genes leaking into the test set. Frozen DNA encoders thus recover little from coding sequence beyond nucleotide composition, and fair comparisons must use composition baselines and fix pooling, substrate, and split.

---

## 4. Fine-tuned DNA sequence language models for predicting gene expression in admixed population: A comparison with variant-based methods

bioRxiv · 预印本 · 2026-11-18 · 相关性 7/10

**研究关联：方法可借鉴**

- **为什么值得看**：评估并微调Borzoi和AlphaGenome等sequence-to-function模型用于个体基因表达预测，与基因组基础模型评估和sequence-to-function高度相关。
- **任务与验证范围**：输入：个人全基因组序列 → 输出：个体水平基因表达量；研究体系：人类全血细胞；验证范围：跨美洲印第安、欧洲、非洲血统群体，摘要未说明是否跨细胞类型
- **核心方法**：微调预训练的序列到功能模型（Borzoi和AlphaGenome）并结合预测的表观遗传特征进行基因表达预测。
- **主要发现与证据**：微调显著提升了预训练模型性能，但其整体表现仍与基于变异的弹性网模型相当；模型在不同血统群体间表现一致，同血统内训练评估略优；引入预测的表观遗传特征改善了启动子附近的预测性能。
- **可借鉴点（研究建议）**：论文发现引入预测的表观遗传特征能改善启动子区域预测，这提示我在增强子活性预测中可探索结合虚拟表观遗传特征作为辅助输入或多任务目标的策略。
- **迁移边界**：原论文任务为全血基因表达预测，未涉及序列padding策略；其跨血统的泛化表现不能直接等同于跨细胞类型的泛化能力，迁移至增强子活性预测需重新评估。
- **阅读时核实**：论文中引入的“预测的表观遗传特征”具体包含哪些特征，以及它们是如何与Borzoi或AlphaGenome模型架构结合的？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.17.767377v1) · [DOI](https://doi.org/10.64898/2026.11.17.767377)

作者：Liu, X., Huang, Y.-J., Lu, J. et al. (9 authors)
来源标注的末位/通讯作者：Xiaonan Liu
机构：Harvard University

### 英文摘要

Predicting gene expression from whole genome sequencing data is essential for elucidating regulatory mechanisms and interpreting functional consequences of non-coding variants to complex diseases. While traditional approaches rely on variant-based linear models, DNA sequence-based language models have gained increasing popularity for their ability to learn regulatory features directly from whole genome sequence data. Previous studies have evaluated models such as Enformer, but newer sequence-to-function models, including Borzoi and AlphaGenome, remain less well characterized for individual-level gene expression prediction, particularly in non-European and admixed populations. Here, we evaluated and fine-tuned Borzoi and AlphaGenome using personal genomes paired with whole-blood RNA-seq data from the Hispanic Community Health Study/Study of Latinos (HCHS/SOL). Fine-tuning substantially improved the performance of both sequence-based models compared with their pretrained versions; however, their performances remained similar to that of the variant-based linear models. Leveraging the ancestral diversity of HCHS/SOL, we found that Borzoi and AlphaGenome showed similar performance across Amerindian-, European-, and African-enriched groups. Fine-tuned Borzoi, fine-tuned AlphaGenome and elastic net performed modestly better when trained and evaluated in the same ancestry-enriched group. Finally, we explored strategies to improve prediction performance and found that incorporating predicted epigenetic features improved prediction near the promoter region. Significant progress remains needed before the full potential of sequence-based models is attained. Incorporating more biology-guided training approaches could be helpful to achieving better performance.

---

## 5. scUNVEIL: Learning scRNA-seq Cell Embeddings Through Measurement Enrichment

bioRxiv · 预印本 · 2026-11-18 · 相关性 7/10

**研究关联：研究兴趣拓展**

- **为什么值得看**：scUNVEIL是单细胞转录组基础模型，通过自监督next-UMI预训练学习细胞表征，与我的epigenetic foundation model和virtual cell研究兴趣高度相关。
- **任务与验证范围**：输入：scRNA-seq UMI计数向量 → 输出：细胞嵌入表征与测量增强后的基因表达估计；研究体系：约9200万人类细胞（跨多种组织）；验证范围：跨细粒度细胞类型注释，并拓展至肿瘤反应性、细胞形态等下游任务。
- **核心方法**：基于next-UMI预测的自监督残差多层感知机（Residual MLP），直接处理计数向量而无需基因token的注意力机制。
- **主要发现与证据**：模型在9200万人类细胞上预训练后，其zero-shot表征在细粒度细胞类型注释上表现最优，推理速度比最强Transformer基线快1000倍，且在仅使用12%输入UMIs时即可达到同等预测性能。
- **可借鉴点（研究建议）**：论文通过预测“更深测序深度下的虚拟状态”进行自监督预训练，这启发我思考在DNA序列建模中是否可通过预测“虚拟的更高分辨率特征”来提升表征学习，而非仅依赖padding处理变长序列。
- **迁移边界**：原论文针对scRNA-seq的UMI计数向量且基于UMI可交换性假设，而我的任务基于具有位置依赖性的DNA序列；其无注意力机制和测量增强策略无法直接迁移至增强子活性预测，跨模态泛化未经验证。
- **阅读时核实**：残差MLP在不使用注意力机制处理基因token的情况下，如何有效捕捉基因间的共表达网络和上下文调控关系？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.17.767296v1) · [DOI](https://doi.org/10.64898/2026.11.17.767296)

作者：Honzik, T., Kuhajda, L., Houdova, L., Georgiev, D.
来源标注的末位/通讯作者：Tomas Honzik
机构：University of West Bohemia in Pilsen

### 英文摘要

Large-scale pretraining can improve scRNA-seq representations through measurement enrichment: estimating what the same measurement would reveal at greater UMI depth under the same measurement process. We introduce scUNVEIL, a self-supervised model trained through next-UMI prediction. We show that the Bayes-optimal next-UMI predictor is the posterior mean of the transcriptome composition that arbitrarily deep sequencing would reveal. Because UMI identities are exchangeable conditional on transcriptome composition, scUNVEIL operates directly on count vectors using a residual multilayer perceptron, without attention over gene tokens. The measurement-enriched transcriptome composition is predicted from a single low-dimensional hidden state, which therefore serves naturally as the cell embedding. The same model provides both reusable cell representations and measurement-enriched gene-expression estimates. scUNVEIL was pretrained without labels or auxiliary metadata on approximately 92 million human cells spanning diverse tissues. Under linear evaluation on fine-grained cell-type annotation, its zero-shot representations achieved the best performance among the evaluated methods, while providing over 1000-fold faster inference than the strongest evaluated transformer-based foundation model and matching that model's predictive performance using 88% fewer input UMIs per cell. Further evaluations show that these representations improve prediction of tumor reactivity, mitochondrial membrane potential, cell morphology, and lineage-associated treatment outcomes.

---

## 6. Multimodal Structural and Regulatory Architecture of Coding and Non-Coding Variants Across the Orofacial Clefting TP63-IRF6-GRHL3 Network

bioRxiv · 预印本 · 2026-11-18 · 相关性 6/10

**研究关联：方法可借鉴**

- **为什么值得看**：该文章在调控变异分析中应用了AlphaGenome进行增强子调控建模和DNase预测，与你的调控基因组学及变异效应预测兴趣有间接交集。
- **任务与验证范围**：输入：编码/非编码变异序列及蛋白结构信息 → 输出：变异致病性分类与调控效应预测；研究物种/细胞体系：人类（斑马鱼体内验证）、角质形成细胞；验证范围：跨TP63-IRF6-GRHL3网络多基因，摘要未说明是否跨多种细胞类型。
- **核心方法**：整合AlphaFold 3结构预测、热力学稳定性计算（ΔΔG）与AlphaGenome调控建模的多模态变异效应预测范式。
- **主要发现与证据**：结合AF3结构和AlphaGenome调控建模，提升了编码区变异分类性能（如IRF6生物物理AUROC提升至0.8967），并在非编码区有效捕获增强子语法和上下文染色质效应（AlphaGenome剪接轨道AUROC达0.9876），预测结果与体内实验及MaveDB数据高度吻合。
- **可借鉴点（研究建议）**：AlphaGenome在1.049 Mb范围内捕获上皮染色质轨道和增强子语法的能力，提示在研究预训练模型padding影响时，可关注模型对长距离上下文依赖的捕捉机制。
- **迁移边界**：原论文聚焦特定基因网络的变异效应解析，而我的任务关注不同细胞类型的游离型增强子活性及padding影响。AlphaGenome在角质形成细胞中的表现不能直接泛化至其他细胞类型或游离型增强子任务，且原论文未探讨padding策略。
- **阅读时核实**：AlphaGenome在处理非编码区变异和增强子语法时，其输入序列的长度和padding策略是如何设定的，是否对1.049 Mb的上下文窗口有特殊处理？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.17.767356v1) · [DOI](https://doi.org/10.64898/2026.11.17.767356)

作者：Vono, F. M., Santos, V. G., Toledo, A. N. d.
来源标注的末位/通讯作者：Filipe Martins Vono
机构：Centro Universitário de Belo Horizonte (UniBH), Belo Horizonte, Minas Gerais, Brazil

### 英文摘要

Pathogenic variation across the TP63-IRF6-GRHL3 transcriptional network causes syndromic and nonsyndromic orofacial clefts (OFCs), yet scalar sequence predictors collapse distinct failure modes and leave isoform-specific coding variants, splice-altering indels, and distal enhancer alleles unresolved. Here, we integrate 29 AlphaFold 3 (AF3) assemblies (10 wild-type, 19 mutant), thermodynamic stability ({Delta}{Delta}G) calculations, and AlphaGenome regulatory modeling across clinical, saturation-mutagenesis, and reporter benchmarks. In strict leave-one-gene-out (LOGO) coding benchmarks, replacing paralog crystal templates with full-length human AF3 structures improves IRF6 classification (biophysical AUROC rising from 0.7844 to 0.8967; {Delta}{Delta}G from 0.6461 to 0.8516) and resolves canonical isoform gaps in the 602-residue MANE Select GRHL3 homodimer. Projecting IRF6 missense variants onto a two-dimensional stability-versus-interface phase plane separates dominant-negative popliteal pterygium syndrome (PPS) poisons from haploinsufficient Van der Woude syndrome (VWS1) alleles (VWS1-versus-PPS Quadrant I odds ratio [OR] = 0.0263 [reciprocal OR = 38.0], p = 4.652 x 10-3) and distinguishes DNA-contact poisons from dimer-unfolding alleles across 12 zebrafish in vivo assays. Atomistic base-readout contacts in the AF3 TP63-MCS9.7 tetramer mirror loss-of-function profiles in MaveDB ({rho} = 0.6048, p = 6.52 x 10-4) and AlphaGenome keratinocyte DNase predictions ({rho} = 0.6040, p = 6.65 x 10-4). Across non-coding benchmarks, AlphaGenome splicing tracks reach an AUROC of 0.9876 while prioritizing cryptic splice variants of uncertain significance, and epithelial chromatin tracks capture enhancer grammar, plasmid-cloning artifacts, and context-dependent ARHGAP29, FOXE1, and local 8q24 chromatin effects within AlphaGenome's 1.049-Mb horizon.

---

中文笔记基于标题和摘要生成，未核验全文；研究建议不代表论文已验证的结论。相关性分数不是论文质量评分。

检索统计：窗口 [2026-11-16 00:00, 2026-11-19 00:00) UTC；抓取 biorxiv 198/pubmed 73 → 粗筛 47 篇 → LLM 选中 6 篇
