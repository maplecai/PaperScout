# Paper Scout 日报 2026-11-07

共推荐 **8** 篇论文。

## 1. Learning Strand-Equivariant Tokenizations of DNA with MirrorDNA

bioRxiv · 预印本 · 2026-11-06 · 相关性 9/10

**研究关联：方法可借鉴**

- **为什么值得看**：探讨DNA语言模型的分词与序列处理策略（反向互补对称性），与评估基因组基础模型输入处理策略（如padding）的活跃项目直接相关。
- **任务与验证范围**：输入：DNA序列 → 输出：调控标签预测；研究物种/细胞体系：摘要未说明；验证范围：Genomic Benchmarks和Nucleotide Transformer任务，摘要未说明是否跨细胞类型。
- **核心方法**：提出MirrorDNA，一种具有学习型分词器的紧凑DNA语言模型，通过保证反向互补序列间的镜像对称分词边界实现链等变性。
- **主要发现与证据**：现有DNA语言模型在反向互补序列上预测不一致（改变25-31%预测），而MirrorDNA在标签不依赖链时给出相同答案，依赖链时能区分；仅计算双链均正确的预测时，其MCC比NT-v2等模型提高一倍多，且在2.3M参数下性能与百兆参数模型相当，并支持长序列外推。
- **可借鉴点（研究建议）**：在使用预训练基因组学模型预测增强子活性时，可考虑评估并缓解序列反向互补带来的预测不一致性，或借鉴其学习型分词器以保留关键功能motif。
- **迁移边界**：原论文主要针对通用的DNA调控标签预测任务（如TF结合、剪接），未直接验证跨细胞类型的增强子活性预测或padding策略的影响；其链等变性方法在应用于特定细胞类型增强子任务时，需验证是否仍能保持性能优势。
- **阅读时核实**：MirrorDNA的学习型分词器在处理不同长度的padding或截断序列时，是否能保持镜像对称性及预测一致性？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.04.764207v1) · [DOI](https://doi.org/10.64898/2026.11.04.764207)

摘要提供的链接（未核验可用性）：[资源 1](https://github.com/NIRJHOR-DATTA/MirrorDNA)

作者：Datta, N., Shatabda, S., Bayzid, M. S., Rahman, M. S.
来源标注的末位/通讯作者：M. Sohel Rahman
机构：Department of Computer Science and Engineering, Bangladesh University of Engineering and Technology, Dhaka, Bangladesh

### 英文摘要

DNA has two strands, and for most regulatory label prediction tasks a sequence and its reverse complement should get same answer. Yet DNA language models are tokenized, trained and tested on one strand at a time. We show that this makes them inconsistent. BPE and $k$-mer tokenizers split 92--100\% of transcription-factor motifs differently on the two strands, and NT-v2, DNABERT-2 and HyenaDNA change 25-31\% of their predictions when the test sequences are reverse-complemented. We introduce {\model}, a compact DNA language model with a learned tokenizer that guarantees mirror-symmetric token boundaries across reverse-complement sequences, regardless of its learned parameters. We prove that this symmetry holds through the whole model. As a result, the same model can give identical answers on both strands when the label does not depend on the strand, and can still tell the strands apart when it does, which no strand-blind model can learn. Counting only predictions that are correct on both strands, \model\ more than doubles the MCC of NT-v2, DNABERT-2 and HyenaDNA. With 2.3M parameters, it is more accurate than the Caduceus models trained on the same data, and not significantly different from NT-v2 (98M parameters) on Genomic Benchmarks or from DNABERT-2 (117M) on the Nucleotide Transformer tasks. It also stays accurate on inputs sixteen times longer than those it was trained on. The same model trained with reverse-complement augmentation instead still changes about one prediction in ten with the strand, unless its outputs are averaged over both strands. Without any annotation, the tokenizer learns to keep the splice-donor signal \texttt{AGGT} in a single token. Code: https://github.com/NIRJHOR-DATTA/MirrorDNA.

---

## 2. Predicting dynamic expression patterns in budding yeast with a fungal DNA language model

bioRxiv · 预印本 · 2026-11-05 · 相关性 8/10

**研究关联：方法可借鉴**

- **为什么值得看**：真菌DNA语言模型预训练结合RNA-seq微调进行序列到表达预测，直接契合DNA语言模型与sequence-to-function研究兴趣。
- **任务与验证范围**：输入：DNA序列 → 输出：基因表达模式及变异效应；物种/体系：芽殖酵母；验证范围：诱导时间序列RNA-seq、cis-eQTL分类、MPRA（摘要未说明是否跨细胞类型）
- **核心方法**：基于165个真菌基因组自监督预训练的masked DNA语言模型，并在酵母RNA-seq数据上微调进行序列到表达的预测。
- **主要发现与证据**：Shorkie在基因表达预测上显著优于无自监督基线，在cis-eQTL分类中优于领先模型，并与MPRA高度一致；可解释性分析表明其能捕捉启动子动态及调控motif使用的时间变化。
- **可借鉴点（研究建议）**：可借鉴其利用跨物种相关基因组进行自监督预训练以学习保守调控motif的范式，推测在增强子活性预测中引入多物种预训练可能提升模型对调控特征的提取能力。
- **迁移边界**：原论文针对酵母启动子及基因表达预测，物种为真菌；我的研究关注哺乳动物游离型增强子活性及预训练模型padding影响，跨物种与跨调控元件（启动子到增强子）的泛化能力以及padding策略的有效性尚未被该论文证明。
- **阅读时核实**：模型在处理不同长度的DNA序列输入时采用了何种padding或截断策略，该策略是否会影响模型对长程调控元件特征的捕捉？

[原文](https://www.biorxiv.org/content/10.1101/2025.09.19.677475v1) · [DOI](https://doi.org/10.1101/2025.09.19.677475)

作者：Chao, K.-H., Magzoub, M. M., Stoops, E. H., Hackett, S. R., Linder, J., Kelley, D. R.
来源标注的末位/通讯作者：Kuan-Hao Chao
机构：Johns Hopkins University

### 英文摘要

Predicting gene expression from DNA sequence remains challenging due to complex regulatory codes. We introduce a masked DNA language model pretrained on 165 fungal genomes related to budding yeast that learns conserved regulatory sequence motifs. Fine-tuning the LM on yeast RNA-seq data--including high-resolution transcriptional regulator induction time courses generated in this study--yielded Shorkie, a model that substantially improves gene expression prediction compared to baselines trained without self-supervision. Shorkie identified canonical transcription factor (TF) binding motifs and captured changes in their regulatory contributions across induction time courses. Furthermore, Shorkie accurately predicted variant effects, outperforming leading sequence-to-expression models in cis-eQTL classification and achieving high concordance with massively parallel reporter assays. Interpretability analyses revealed Shorkie's ability to resolve promoter dynamics, splicing signals, and temporal changes in regulatory motif usage. Together, these results support combining pretraining on related fungal genomes with RNA-seq fine-tuning to improve sequence-based prediction of gene expression in budding yeast and provide insights into noncoding variants.

---

## 3. Joint protein-DNA language modeling enables prediction and engineering of DNA recognition specificity

bioRxiv · 预印本 · 2026-11-06 · 相关性 7/10

**研究关联：方法可借鉴**

- **为什么值得看**：提出联合蛋白-DNA语言模型，与DNA语言模型和调控序列表示学习高度相关。
- **任务与验证范围**：输入：成对的蛋白质与DNA序列 → 输出：结合特异性分类、突变结合变化预测、碱基编辑活性预测及DNA motif预测；研究物种/细胞体系：摘要未说明；验证范围：跨下游任务及跨研究（碱基编辑活性）验证
- **核心方法**：基于ESM2继续预训练的蛋白质-DNA联合语言模型（PDLM），采用共享编码器与领域感知掩码策略学习跨分子交互依赖。
- **主要发现与证据**：PDLMs在蛋白质-DNA对分类上优于独立编码器基线；零样本评分可恢复已知DNA识别特异性变化并筛选高编辑活性变体；微调后能直接从蛋白质序列预测DNA motif。
- **可借鉴点（研究建议）**：可推测借鉴其“领域感知掩码”策略，在我的增强子活性预测预训练中，对已知调控核心区域（如特定motif）施加差异化掩码概率，以强化关键特征学习。
- **迁移边界**：PDLM聚焦于蛋白质-DNA双模态交互建模，而我的研究为DNA序列到增强子活性的单模态预测及padding影响评估。其共享编码器机制及掩码策略在纯DNA序列模型中的泛化性尚未被证明，不能直接等同。
- **阅读时核实**：PDLM在将蛋白质与DNA序列输入共享编码器时，如何处理不同模态序列的长度对齐与padding？padding token是否参与了注意力计算或掩码损失？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.05.763984v1) · [DOI](https://doi.org/10.64898/2026.11.05.763984)

作者：Xiong, Y., Ren, J., Wei, X., Li, X., Li, J., Wei, W.
来源标注的末位/通讯作者：Wensheng Wei
机构：Peking University

### 英文摘要

Protein-DNA recognition specificity underlies transcriptional regulation, DNA replication, chromatin remodeling and genome editing. Protein-DNA recognition depends on both interacting sequences, yet language models that learn this cross-molecular dependence explicitly during pretraining remain limited. Here, we developed the Protein-DNA Language Models (PDLMs), interaction-aware language models that jointly represent protein and DNA sequences. PDLMs were built by continued pretraining from ESM2 with masked language modeling on paired protein-DNA sequences. A shared encoder places amino acids and nucleotides in the same molecular context, enabling conditional sequence scoring and transferable pair representations. We further introduced a domain-aware masking strategy that increased masking probability within DNA-binding domains to strengthen learning of interaction-relevant regions. Across downstream tasks, PDLMs improved protein-DNA pair classification relative to independent-encoder baselines and supported prediction of mutation-associated binding changes. Zero-shot scoring recovered known changes in DNA-recognition specificity and prioritized variants with higher editing activity. Learned representations also supported cross-study prediction of base editor activity. After fine-tuning on transcription factor binding data, PDLMs predicted DNA motifs directly from protein sequences. Together, PDLMs provide a framework for interaction-aware biomolecular language modeling, with potential applications in protein engineering and genome editing.

---

## 4. scDisentangle: sequential disentanglement for single-cell perturbation response prediction

bioRxiv · 预印本 · 2026-11-06 · 相关性 7/10

**研究关联：方法可借鉴**

- **为什么值得看**：直接涉及单细胞扰动响应预测，属于我的研究兴趣之一。
- **任务与验证范围**：输入：单细胞表达数据及扰动条件 → 输出：预测的转录响应及细胞分辨的反事实状态。物种：摘要未说明。细胞体系：涉及免疫细胞、肝脏细胞、前列腺细胞等。验证范围：跨扰动条件（细胞因子、感染、遗传扰动）及跨细胞状态（外周血到心内T细胞）。
- **核心方法**：基于序列解耦的生成式模型，将单细胞表达分解为观察属性和残差成分以生成保留源细胞身份的反事实。
- **主要发现与证据**：在细胞因子刺激、肝脏感染和未见过的组合遗传扰动上优于现有模型和朴素基线；能从外周血预测供体特异性的心内CD8+ T细胞状态；其粗到细的潜在结构与造血谱系组织一致，早期水平捕获未分化核心并逐渐细化为细胞类型特异性程序。
- **可借鉴点（研究建议）**：论文通过“粗到细”的潜在结构解耦细胞类型特异性程序，这提示我在预测不同细胞类型增强子活性时，可探索将序列特征解耦为细胞类型不变的核心基序与细胞类型特异的调控残差。
- **迁移边界**：原论文处理单细胞转录组表达空间的扰动响应与反事实生成，而我的任务是基于DNA序列预测增强子活性并评估padding影响。两者数据模态（转录组 vs DNA序列）和任务目标（反事实生成 vs 序列到功能映射）差异显著，其跨细胞类型泛化能力不能直接等同于DNA序列模型在不同细胞类型间的泛化。
- **阅读时核实**：模型在分解“观察到的属性”和“残差成分”时，具体是如何定义和约束这些残差成分的生物学意义的？这种解耦机制是否依赖于特定的批次效应假设？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.04.764292v1) · [DOI](https://doi.org/10.64898/2026.11.04.764292)

作者：El Mejjad, S., Enezari, S., Bedraoui, A., El Hajji, F. Z., El Fatimy, R., Hofree, M., Daouda, T.
来源标注的末位/通讯作者：Tariq Daouda
机构：University Mohammed VI Polytechnic

### 英文摘要

Predicting the transcriptional response of single cells to perturbation is a central goal of single-cell modeling, with broad application to analysis and experimental design. Existing methods often fail to beat simple baselines and offer little insight into how biological variation is organized. We present scDisentangle, a model that decomposes single-cell expression into observed attributes and a sequence of residual components, generating counterfactuals that preserve source cell identity. scDisentangle outperformed current models and naive baselines on cytokine stimulation, liver infection, and unseen combinatorial genetic perturbations, on which accuracy was largely independent of how closely a response resembled the average perturbation effect. In an immune checkpoint inhibitor-associated myocarditis cohort, cell-resolved counterfactuals predicted donor-specific intracardiac CD8+ T cell states from peripheral blood. In a castration-regeneration prostate atlas, predictions recapitulated luminal dynamics and progenitor-marker kinetics upon androgen add-back. scDisentangle's coarse-to-fine latent structure aligned with hematopoietic lineage organization, with early levels capturing a less differentiated core progressively refined into cell-type-specific programs.

---

## 5. Towards universal modeling of transcript isoform expression levels

bioRxiv · 预印本 · 2026-11-05 · 相关性 6/10

**研究关联：方法可借鉴**

- **为什么值得看**：利用表观基因组特征跨组织预测转录本表达，与跨细胞类型表观调控预测间接相关。
- **任务与验证范围**：输入：位置特异性表观基因组特征与基因-基因关系 → 输出：转录本异构体表达水平；研究体系：人类样本；验证范围：29种组织类型的324个样本，进行跨组织泛化验证
- **核心方法**：基于图的方法，整合位置特异性表观基因组特征与多种基因-基因关系网络进行建模
- **主要发现与证据**：整合多组织样本信息训练的模型在推断特定样本转录本异构体表达时，始终优于仅用该样本自身数据训练的模型，支持跨组织“通用”模型的可行性
- **可借鉴点（研究建议）**：跨组织/细胞类型“通用”建模思路可借鉴，提示在增强子活性预测中可探索整合多细胞类型表观特征以提升单细胞类型预测性能
- **迁移边界**：原论文任务为转录本表达预测且依赖图结构与基因关系，与基于DNA序列的增强子活性预测任务范式不同；其跨组织泛化结论不能直接等同于跨细胞类型增强子活性预测的泛化能力，且未涉及序列模型或padding问题
- **阅读时核实**：图模型中整合的“基因-基因关系”具体包含哪些类型？是否涉及调控元件（如增强子）与靶基因的相互作用信息？

[原文](https://www.biorxiv.org/content/10.1101/2025.07.21.665977v1) · [DOI](https://doi.org/10.1101/2025.07.21.665977)

作者：Chow, S. H.-C., Shi, C. H., Deshpande, A., Cao, Q., Yip, K. Y.
来源标注的末位/通讯作者：Kevin Y. Yip
机构：Sanford Burnham Prebys Medical Discovery Institute

### 英文摘要

A holy grail in computational biology is accurate modeling of transcript expression levels using epigenetic features, which would provide a quantitative way to study gene regulation in normal and disease states. Previous studies relied heavily on immortalized cell lines that exhibit properties different from cells in natural tissue environments. Most studies also quantified the expression of each gene by a single expression level, which fails to capture separate expression levels of different transcript isoforms of the same gene. In this study, making use of the latest large-scale dataset of paired transcriptomic and epigenomic data of human samples produced by the International Human Epigenome Consortium (IHEC), we computationally modeled the expression levels of individual transcript isoforms in 324 samples from 29 tissue types. We constructed the models using graph-based methods that integrate both location-specific epigenomic features and multiple types of gene-gene relationships. We found that to infer transcript isoform expression levels in a sample, a model that integrates information from many samples of other tissue types consistently outperforms a model trained on data from this sample itself, providing strong support that it is possible to construct a "universal" model that can accurately infer transcript isoform expression levels across tissue types.

---

## 6. Inferring gene regulatory networks from single-cell perturbation data by optimizing causal reach of latent mediator dynamics

bioRxiv · 预印本 · 2026-11-06 · 相关性 6/10

**研究关联：研究兴趣拓展**

- **为什么值得看**：从单细胞扰动数据推断基因调控网络，与单细胞扰动的研究兴趣间接相关。
- **任务与验证范围**：输入：单细胞扰动数据（如Perturb-seq） → 输出：因果基因调控网络图；研究物种/细胞体系：摘要未说明具体物种，使用了CaRPool-seq和Norman et al.等数据集；验证范围：在模拟数据及真实数据集上验证，是否跨细胞类型摘要未说明
- **核心方法**：提出CausalODE，一个基于常微分方程（ODE）的可微框架，通过优化“因果可达性”指标并显式建模未观测的蛋白质潜在动力学来学习因果图。
- **主要发现与证据**：在模拟数据上提升了AUPRC和top-ranked edges的精确度；在真实数据集上，因果可达性指标比最强基线分别高出约60%（CaRPool-seq）和80%（Norman et al.），且推断的高置信边在匹配的ChIP-seq等证据中富集度更高。
- **可借鉴点（研究建议）**：无明显直接启发
- **迁移边界**：原论文处理的是单细胞转录组扰动数据到基因调控网络的因果推断，而我的任务是DNA序列到增强子活性的预测，两者数据模态和任务目标完全不同；CausalODE的ODE动力学和潜在蛋白质建模无法直接迁移到DNA序列或padding任务中。
- **阅读时核实**：CausalODE中显式建模的蛋白质潜在动力学ODE是如何在仅有RNA-seq读数的情况下进行参数估计和训练的？是否依赖于特定的扰动时间点设计？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.05.764481v1) · [DOI](https://doi.org/10.64898/2026.11.05.764481)

作者：Qian, W., Song, Y., Welch, J. D.
来源标注的末位/通讯作者：Joshua D Welch
机构：University of Michigan

### 英文摘要

Resolving the causal structure of gene regulatory networks is central to understanding cellular regulation. Pooled CRISPR screens with single-cell RNA readouts measure the transcriptional consequences of many interventions in parallel, providing a powerful resource for causal discovery. Combinatorial designs that perturb multiple regulators per cell increase throughput and can reveal responses that single-gene perturbations do not. However, inferring causal gene networks from these experiments remains challenging because gene regulatory interactions are nonlinear, dynamic, and often involve feedback. Thus, attributing the combined effect of several perturbations to individual regulators remains difficult. Additionally, transcriptional regulation is ultimately carried out by proteins, while single-cell perturbation datasets generally measure only RNA levels. Existing methods often simplify regulatory dynamics or rely on assumptions that conflict with gene regulation, such as acyclicity. Moreover, current evaluation practices usually rely on expression prediction error, which is readily computable in real datasets, but does not necessarily reflect graph quality. A complementary metric is needed to assess inferred regulatory connections using observed perturbation responses in real data. To address these challenges, we present CausalODE, a differentiable framework for learning causal graphs from single-cell perturbation data. Our approach incorporates three central insights to improve upon previous methods. First, genes that are differentially expressed when a gene is perturbed should be downstream of the target gene in the regulatory network; we quantify this property with a metric we term causal reach. Second, causal interactions involve transient cellular responses in RNA transcription, splicing, and degradation. Third, gene regulatory interactions are mediated by proteins, whose levels are not directly measured in single-cell RNA-seq experiments. Building on these insights, CausalODE learns a graph that optimizes the causal reach metric, captures transient cellular responses to perturbation, and explicitly models the latent dynamics of protein levels. Together, these components allow nonlinear responses, feedback loops, and time-lagged regulation. Across simulated Perturb-seq datasets with different sparsities and graph structures, CausalODE improves AUPRC and precision among top-ranked edges compared with baselines and competing methods, while achieving competitive AUROC. We introduce a metric to evaluate the causal reach of inferred graphs on real data by measuring how well the graphs explain differentially expressed genes in single-cell perturbation experiments. Using this metric, CausalODE outperforms the strongest competing method or baseline by approximately 60% on the CaRPool-seq knockdown dataset and 80% on the Norman et al. activation dataset. Its top-ranked edges generally show greater enrichment for high-confidence evidence from cell-type-matched ChIP-seq, CollecTRI, and regulatory STRING than those of other methods. The inferred graphs also distinguish non-additive from approximately additive genetic interactions in held-out perturbation pairs. Finally, ablation analyses show that optimizing causal reach improves performance on held-out perturbations, and the learned latent regulator activities track simulated protein dynamics, with median temporal correlations ranging from 0.79 to 0.99.

---

## 7. Virtual dynamics of spatiotemporal single-cell interactions

bioRxiv · 预印本 · 2026-11-06 · 相关性 6/10

**研究关联：研究兴趣拓展**

- **为什么值得看**：提出空间转录组虚拟细胞动力学重建方法，与“virtual cell”概念间接相关。
- **任务与验证范围**：输入：离散的空间转录组数据（含转录组与空间坐标） → 输出：连续的虚拟细胞动态（细胞状态、位置及种群大小轨迹）；研究物种/细胞体系：摘要未说明具体物种，涉及发育、再生和神经退行性变的组织；验证范围：五个数据集跨三个空间转录组平台，涵盖不同生物学过程，摘要未明确说明是否跨细胞类型验证。
- **核心方法**：采用非平衡平均场薛定谔桥公式，结合基于空间邻近性和配体-受体先验构建的时变相互作用图，学习细胞状态的随机轨迹。
- **主要发现与证据**：在五个跨平台数据集上，CytoBridge能准确生成未测量时间点的组织动态，追踪配体-受体信号变化，并支持生成性计算机扰动实验。
- **可借鉴点（研究建议）**：无明显直接启发
- **迁移边界**：原论文聚焦于空间转录组数据的时空动态轨迹重建，与基于DNA序列预测增强子活性及评估预训练模型padding影响的任务在数据模态（转录组空间坐标 vs DNA序列）和建模目标（轨迹推断 vs 序列到功能映射）上存在根本差异，其方法不可直接迁移。
- **阅读时核实**：薛定谔桥公式中速度的相互作用分量与内在背景分量是如何具体解耦和估计的，该解耦机制在时间外推时是否依赖特定的细胞类型假设？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.04.764438v1) · [DOI](https://doi.org/10.64898/2026.11.04.764438)

作者：Zhang, Z., Wang, Z., Tian, Q. et al. (12 authors)
来源标注的末位/通讯作者：Peijie Zhou
机构：Peking University

### 英文摘要

Building virtual cells and tissues requires reconstructing how interacting cell populations evolve in space and time, yet spatial omics experiments provide only sparse snapshots of this process. Here, we introduce CytoBridge, a computational method that reconstructs continuous virtual cell dynamics from discrete spatial transcriptomic data. Starting from a joint transcriptomic-spatial space, CytoBridge learns stochastic trajectories of cell states, positions, and population sizes through an unbalanced mean-field Schrodinger bridge formulation that explicitly incorporates cell-cell interaction as a dynamical driver. A time-varying interaction graph built from spatial proximity and ligand-receptor priors allows the velocity to be decomposed into an interaction component estimated from observed neighborhoods and ligand-receptor features, and an intrinsic-context component that captures intrinsic regulatory processes and unmeasured contextual influences. Applied to five datasets across three spatial transcriptomics platforms and spanning development, regeneration, and neurodegeneration, CytoBridge accurately generates tissue dynamics at unmeasured time points, follows ligand-receptor signaling through measured and unmeasured stages, and supports hypothesis-generating in silico perturbation. CytoBridge provides a general method for turning heterogeneous spatiotemporal transcriptomic measurements into continuously evolving virtual tissues.

---

## 8. Plate design confounds donor variation and model evaluation in single-cell perturbation screens

bioRxiv · 预印本 · 2026-11-06 · 相关性 6/10

**研究关联：方法可借鉴**

- **为什么值得看**：探讨单细胞扰动筛选中的模型评估问题，对我的模型评估思路有启发。
- **任务与验证范围**：输入：单细胞扰动筛选数据（含90种细胞因子筛选、两种化合物筛选、四个队列及模拟数据） → 输出：孔板设计混淆的量化分析及修正后的模型评估框架；研究物种/细胞体系：免疫细胞（摘要未说明具体物种）；验证范围：跨细胞类型（涉及三种细胞类型）。
- **核心方法**：结合实验设计分析、模拟与深度学习模型评估，提出设计感知估计器与扰动特异性评估范式。
- **主要发现与证据**：孔效应解释了大部分重复对照变异，相同对照孔在标准阈值下有数百个差异表达基因；在标准评估下得分低于扰动无关预测器的深度学习模型，在三种细胞类型中的两种的扰动特异性差异上优于简单基线（其中一种在严格对照下显著）。
- **可借鉴点（研究建议）**：在评估预训练基因组学模型预测增强子活性时，需警惕序列padding等技术性特征是否像“孔效应”一样被模型误当作生物学信号，并考虑引入“技术特征无关”的基线进行对比评估。
- **迁移边界**：原论文针对单细胞转录组扰动筛选中的孔板位置效应，与基于DNA序列预测增强子活性的任务存在本质差异；其关于跨细胞类型泛化的结论仅限于特定免疫细胞体系，不能直接等同于预训练模型在不同细胞类型增强子活性预测上的泛化能力。
- **阅读时核实**：论文中提到的“设计感知估计器”具体是如何在模型评估中剥离技术效应（如孔效应）的？其数学形式是否可迁移到序列模型中剥离位置/padding效应？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.04.764088v1) · [DOI](https://doi.org/10.64898/2026.11.04.764088)

作者：Ghajari, G., Thirunarayan, K., Amsaad, F.
来源标注的末位/通讯作者：Ghazal Ghajari
机构：Wright State University

### 英文摘要

Single-cell screens of immune cells from many donors are used to study why individuals respond differently and to benchmark response models. Each donor-perturbation combination typically occupies one well, controls are grouped, and donors share one layout, so technical effects can look biological. Using a 90-cytokine screen, two compound screens, four cohorts and simulations, we show that well effects explain most replicate-control variation in abundant cell types, controls carry a shared offset, and identical control wells differ by hundreds of differentially expressed genes at a standard threshold, about as many as two receptor-negative proteins do. Negative controls, design-aware estimators and perturbation-specific evaluation change the interpretation of four recent analyses. A deep-learning model that scores below a perturbation-agnostic predictor under standard evaluation outperforms a simple baseline on perturbation-specific differences in two of three cell types (significantly in one with stricter controls), but predicts less well the component shared with inert wells.

---

中文笔记基于标题和摘要生成，未核验全文；研究建议不代表论文已验证的结论。相关性分数不是论文质量评分。

检索统计：窗口 [2026-11-04 00:00, 2026-11-07 00:00) UTC；抓取 biorxiv 214/pubmed 69 → 粗筛 44 篇 → LLM 选中 8 篇
