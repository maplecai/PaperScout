# Paper Scout 日报 2026-09-10

共筛选出 **9** 篇推荐论文。
📊 抓取 arxiv 43/biorxiv 630/pubmed 79 → 粗筛 100 篇 → LLM 选中 9 篇

## 1. Flexible use of conserved motifs constrains genome access in cell type evolution.

- **期刊**: Nature ecology & evolution
- **作者**: Chew Chai, Jesse Gibson, Pengyang Li, Brennan D McDonald, Anusri Pampari, Aman Patel, Anshul Kundaje, Bo Wang
- **机构**: Bo Wang @ Department of Bioengineering, Stanford University, Stanford, CA, USA. wangbo@stanford.edu.
- **日期**: 2026-09-08
- **ID**: DOI: 10.1038/s41559-026-03164-5  |  PMID: 42711533  |  URL: https://pubmed.ncbi.nlm.nih.gov/42711533/
- **一句话推荐**: 使用深度学习模型预测跨物种的细胞类型特异性染色质可及性，直接涉及sequence-to-function和细胞类型特异性调控的泛化问题。
- **方法**: 结合单核多组学与深度学习模型，跨物种解析染色质可及性序列并提取调控motif的组合语法。
- **主要发现**: 细胞类型家族的motif词汇表进化保守，但细胞类型特异性的motif组合语法进化迅速；跨物种深度学习模型在家族水平具泛化性，但在细胞类型水平失效。
- **对我的启发**: 评估预训练基因组学模型预测不同细胞类型增强子活性时，需警惕模型可能依赖不同的序列特征（或padding伪影）达到趋同预测，从而掩盖真实的细胞类型特异性调控语法。

<details><summary>Abstract</summary>

Cell types can be organized into related families, but the regulatory mechanisms that define and maintain these families across deep evolutionary time remain unknown. Here, combining single-nucleus multi-omic sequencing with deep learning to analyse the accessible genomes of two groups of vastly divergent animals including flatworms and vertebrates, we find that hundreds of accessibility-dictating sequence motifs partition into distinct yet conserved sets, or 'vocabularies', each associated with a specific cell type family. However, combinatorial relationships among these motifs preferred by individual cell types are largely species specific. Deep-learning models trained on one species accurately predict family-level chromatin accessibility in distantly related species, albeit frequently rely on different motifs from shared vocabularies to reach convergent predictions. By contrast, models trained on individual cell types within a family lose cross-species predictive power, indicating that the regulatory syntax governing cell type-level identity evolves rapidly. We propose a 'collective maintenance' model in which motif vocabularies defining cell type families are evolutionarily stable, while recombination of these motifs generates cell type-specific regulatory programmes. This suggests that family identity is maintained collectively by large, conserved pools of regulatory factors, analogous to the logic of developmental homology, where character identity persists through network-level conservation despite extensive rewiring.

</details>

---

## 2. PlantCAD2: A DNA foundation model for interpreting genomes across flowering plants.

- **期刊**: Cell genomics
- **作者**: Jingjing Zhai, Aaron Gokaslan, Sheng-Kai Hsu et al. (13 authors)
- **机构**: Edward S Buckler @ Institute for Genomic Diversity, Cornell University, Ithaca, NY 14853, USA; Section of Plant Breeding and Genetics, Cornell University, Ithaca, NY 14853, USA; USDA-ARS, Ithaca, NY 14853, USA. Electronic address: ed.buckler@usda.gov.
- **日期**: 2026-08-07
- **ID**: DOI: 10.1016/j.xgen.2026.101329  |  PMID: 42567165  |  URL: https://pubmed.ncbi.nlm.nih.gov/42567165/
- **一句话推荐**: 提出植物特异性DNA基础模型，涉及DNA语言模型预训练和染色质可及性预测，与基因组基础模型评估研究高度相关。
- **方法**: PlantCAD2，一种基于单核苷酸分辨率、具有8192bp扩展上下文窗口的植物特异性DNA基础语言模型，在65个被子植物基因组上预训练。
- **主要发现**: 该676M参数模型在零样本进化保守性任务上超越7B参数的Evo2，并在微调后的跨物种染色质可及性等任务上优于1B参数的AgroNT；其8192bp的长上下文窗口显著提升了大基因组（如玉米）的染色质可及性预测性能。
- **对我的启发**: 该模型证明长上下文窗口对远端调控建模至关重要，启发我在评估预训练基因组学模型的padding或截断策略时，需重点考察不同上下文长度对游离型增强子远端调控特征及虚拟表观遗传特征捕获能力的影响。

<details><summary>Abstract</summary>

Flowering plants (angiosperms) exhibit extraordinary species diversity, ∼200-fold variation in genome size, and relatively compact coding regions, presenting both a unique challenge and opportunity for DNA language models. Here, we introduce PlantCAD2, an extended-context, plant-specific DNA language model with single-nucleotide resolution, pre-trained on 65 angiosperm genomes, together with a series of public benchmarks for evaluation. Comprehensive zero-shot testing shows that PlantCAD2 (676 million parameters) efficiently captures evolutionary conservation, surpassing the 7-billion-parameter Evo2 in 10 of 12 tasks. With parameter-efficient fine-tuning, PlantCAD2 outperforms the 1-billion-parameter AgroNT across seven cross-species tasks including chromatin accessible region, gene expression, and protein translation. Its 8,192-bp context window substantially improves accessible chromatin prediction in large genomes such as maize (area under the precision-recall curve [AUPRC] increasing from 0.587 to 0.711), underscoring the importance of long-range context for modeling distal regulation. These results establish PlantCAD2 as a powerful and versatile foundation model for plant genome annotation and interpretation across diverse species.

</details>

---

## 3. A systematic comparison of single-cell perturbation response prediction models.

- **期刊**: Science advances
- **作者**: Lanxiang Li, Yue You, Yunlin Fu et al. (14 authors)
- **机构**: Luyi Tian @ GMU-GIBH Joint School of Life Sciences, Guangzhou Medical University, Guangzhou, China.
- **日期**: 2026-09-09
- **ID**: DOI: 10.1126/sciadv.aed3414  |  PMID: 42715312  |  URL: https://pubmed.ncbi.nlm.nih.gov/42715312/
- **一句话推荐**: 系统基准测试单细胞扰动响应预测模型，涵盖跨细胞类型泛化任务，直接命中single-cell perturbation研究兴趣。
- **方法**: 大规模基准测试与系统评估框架，涵盖13种单细胞扰动响应预测模型（含基础模型）在多任务、多指标下的泛化能力评估。
- **主要发现**: 模型预测性能高度依赖扰动效应大小与评估指标视角，且普遍存在保守偏置（如基础模型压缩方差、低估协同效应），跨细胞类型泛化能力整体不足。
- **对我的启发**: 评估预训练基因组学模型在不同细胞类型增强子活性预测时，需警惕基础模型压缩分布方差的保守偏置，并采用多维度指标（如绝对值与相对变化指标）以避免单一视角的误导。

<details><summary>Abstract</summary>

Predicting single-cell transcriptional responses to perturbations is central to dissecting gene regulation and accelerating therapeutic design, yet the field lacks a rigorous, task-spanning assessment of model behavior. We present a large-scale benchmark of 13 representative methods and baselines across 25 datasets spanning diverse perturbation modalities and species, including two primary immune-cell drug-response resources. We evaluated three core tasks-generalization to unseen single-gene perturbations, prediction of combinatorial interactions, and transfer across cell types-using 24 metrics covering expression-level accuracy, relative changes, differential expression (DE) recovery, and distributional similarity. Across tasks, performance depended strongly on perturbation effect size and evaluation perspective: Expression-level agreement was the highest for small-effect perturbations resembling controls, whereas delta- and DE-based metrics improved with larger effects, providing clearer signals. Models shared a conservative bias, with fine-tuned foundation models compressing variance and underestimating synergistic effects in combinations. PerturbNet showed superior recovery of DE signatures in Tasks 1 and 2, while no method consistently generalized across cell types in Task 3, where biological consistency dominated outcomes. This benchmark establishes current methodological limits, clarifies that different metrics probe distinct biological signals rather than redundant summaries of the same prediction problem, and provides a foundation for developing virtual-cell models that more faithfully capture heterogeneous perturbation responses.

</details>

---

## 4. UniCure: A multi-modal model for predicting personalized cancer therapy response.

- **期刊**: Cancer cell
- **作者**: Zexi Chen, Saisai Tian, Jiazheng Pei et al. (23 authors)
- **机构**: Luonan Chen @ State Key Laboratory of Cell Biology, Center for Excellence in Molecular Cell Science, Shanghai Institute of Biochemistry and Cell Biology, Chinese Academy of Sciences, Shanghai 200031, China; School of Mathematical Sciences and School of AI, Shanghai Jiao Tong University, Shanghai 200240, China. Electronic address: lnchen@sjtu.edu.cn.
- **日期**: 2026-09-09
- **ID**: DOI: 10.1016/j.ccell.2026.07.010  |  PMID: 42716007  |  URL: https://pubmed.ncbi.nlm.nih.gov/42716007/
- **一句话推荐**: 涉及基础模型预测跨细胞类型的转录组扰动响应，与你的single-cell perturbation及跨细胞类型泛化兴趣间接相关。
- **方法**: 融合生物与化学基础模型的多模态预训练范式，通过大规模转录组扰动数据预训练并在患者衍生数据上微调以预测药物响应。
- **主要发现**: 该模型能准确预测剂量依赖及组合用药反应，跨bulk与单细胞数据泛化，并在真实临床数据上实现有效的患者级疗效预测与分层。
- **对我的启发**: 其利用大规模扰动数据预训练并在少量患者衍生数据上微调的范式，可启发我利用预训练基因组学模型结合少量特定细胞类型增强子活性数据进行微调，以提升游离型增强子活性预测的泛化能力。

<details><summary>Abstract</summary>

Predicting drug efficacy across diverse patient contexts remains a major challenge in oncology, as models trained on cancer cell lines often fail to capture patient-specific biology. Emerging biological foundation models and patient-derived technologies offer a promising solution. Here, we present UniCure, a multi-modal model that combines biological and chemical foundation models to predict drug-induced transcriptomic responses across diverse cell and tissue contexts, enabling individualized drug ranking. Trained on 1.9 million transcriptomic perturbation profiles spanning >22,000 compounds, 166 cell types, and 24 tissues, UniCure accurately predicts dose-dependent and combination responses and generalizes across bulk and single-cell data. We further fine-tune UniCure on 345 patient-derived tumor-like cluster (PTC) transcriptomic profiles and validate performance on 396 real-world clinical profiles, demonstrating effective patient-level prediction. The model supports response-based patient stratification and is experimentally validated in cell line and patient-derived models. Overall, UniCure provides a practical framework for translating preclinical data into personalized therapeutic strategies.

</details>

---

## 5. ProteinSage: From implicit learning to explicit structural constraints for efficient protein language modeling

- **期刊**: bioRxiv
- **作者**: Shen, L., Chao, L., Liu, T. et al. (10 authors)
- **机构**: Xiaoming Zhang @ BioMap
- **日期**: 2026-09-09
- **ID**: DOI: 10.64898/2026.03.17.712034  |  URL: https://www.biorxiv.org/content/10.64898/2026.03.17.712034v1
- **一句话推荐**: 蛋白质语言模型引入结构约束进行预训练，与你的representation learning for biological sequences兴趣相关。
- **方法**: 提出基于显式结构约束（结构引导掩码与长程因果目标）的蛋白质语言模型预训练框架。
- **主要发现**: 显式结构约束预训练能用更少数据与算力获得可迁移的蛋白质表征，并在基准测试及远缘同源蛋白发现任务中验证了其结构泛化能力。
- **对我的启发**: 启发我在预训练基因组学模型时引入显式染色质三维结构或表观遗传特征作为掩码约束，以提升少样本下增强子活性预测的泛化能力并缓解 padding 对长程依赖建模的干扰。

<details><summary>Abstract</summary>

While protein language models typically rely on sequence-only pretraining objectives, this approach often fails to capture structural regularities and demands large datasets. To address this, we introduce ProteinSage, a pretraining framework that learns protein representations under explicit structural constraints. ProteinSage incorporates structural signals via structure-guided masking and a causal objective designed to model longrange dependencies. This structure-constrained pretraining equips ProteinSage with transferable representations using less data and computation, yet achieves competitive or superior performance across diverse structure-aware and general protein modeling benchmarks. To determine whether these gains stem from genuine structural generalization rather than task-specific fitting, we applied ProteinSage to a structure-driven protein discovery task, focusing on proteins with multi-pass transmembrane helical architectures such as distantly related microbial rhodopsins. The model successfully identified six previously unannotated microbial rhodopsin homologs. Together, our work establishes structure-constrained pretraining as an effective pathway toward data-efficient and structurally faithful protein representation learning.

</details>

---

## 6. EvSpark: Lossless Speculative Decoding for Hybrid DNA Foundation Models

- **期刊**: bioRxiv
- **作者**: Ding, H., Wu, N., Qiu, T.
- **机构**: Nannan Wu @ CreatiPhage Biotechnology Co., Ltd.
- **日期**: 2026-09-08
- **ID**: DOI: 10.64898/2026.09.02.749017  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.02.749017v1
- **一句话推荐**: 涉及DNA基础模型（如Evo2）的推理加速与系统优化，与基因组基础模型的工程实现间接相关。
- **方法**: 针对混合Hyena/attention架构DNA基础模型，提出基于状态切片回滚协议与蒸馏神经起草器的无损投机解码框架。
- **主要发现**: 该框架在零额外重计算下实现3.16倍端到端无损加速；实验表明蒸馏起草器的注入层选择在真实预算下无显著差异，但小预算下会系统性误判。
- **对我的启发**: 混合架构DNA模型中IIR递归状态具有无限记忆特性，提示在评估此类预训练模型padding对增强子预测的影响时，需警惕padding token对SSM状态递归的污染。

<details><summary>Abstract</summary>

DNA foundation models such as Evo2~7B adopt hybrid Hyena/attention architectures (StripedHyena2) whose single-stream autoregressive decoding is bounded by weight bandwidth at ${\sim}45$~\tokps. Speculative decoding on such hybrids faces a systems problem that prior SSM work solves only partially: after a draft is verified, rolling back model state cannot be reduced to truncating a KV cache, because the inference state mixes fixed-length FIR sliding windows, infinite-memory IIR recurrences, and append-only KV caches. We present \textbf{EvSpark}. (i)~A block-verification forward pass together with a per-position \emph{state-slicing} rollback protocol that handles all three state classes jointly with zero recomputation, reducing speculative overhead to 1.05--1.16$\times$ under an identity drafter and eliminating the second per-round forward pass of snapshot-and-replay schemes. (ii) A DSpark-style distilled neural drafter ported to a hybrid architecture ($\gam$-parallel trunk $+$ target hidden-state prefix $+$ full-matrix Markov head); controlled injection-layer comparisons at matched budget and two seeds find no layer-choice effect beyond seed noise at realistic budgets, while smoke-scale budgets systematically misrank layer types; the ${\sim}10^{11}$ residual magnitudes of late blocks require an fp32-scale distillation codec. (iii)~Under a 24-prompt $\times$ 1024-token $\times$ 2-seed protocol, EvSpark delivers \textbf{\speed{3.16}} end-to-end at its deployment configuration ($\gam{=}12$, 80M supervised positions) and \speed{2.88} on the reference model used for our deep-dive analyses ($\gam{=}7$, 150M), holding from 1k to 262k context and across 32k tokens of generation depth. In exact arithmetic the scheme preserves the target distribution; empirically, greedy decoding reproduces native outputs token-for-token (zero non-tie divergences across 24 prompts $\times$ 4 checkpoints), and the sampling path sits at the native bootstrap noise floor for 7/10 prompts with bounded bf16-level deviation elsewhere (${\le}1.7\times$ floor; worst-case unigram TVD 5.6\%). The budget-sweet-spot configuration adds \textbf{1.06 GPU-hours} of training on RTX~4090-class hardware and reaches \speed{3.03} (incremental to a one-off teacher-signal dump of ${\approx}19$ GPU-h shared by all configurations).

</details>

---

## 7. Stable epigenetic states set single-cell activation thresholds in mammalian expression systems

- **期刊**: bioRxiv
- **作者**: Costa, E. J., Rios-Martinez, C., Andrews, C. J., Ferrell, J. E., Bintu, L.
- **机构**: Lacramioara Bintu @ Stanford University
- **日期**: 2026-09-09
- **ID**: DOI: 10.64898/2026.09.04.749524  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.04.749524v1
- **一句话推荐**: 研究表观遗传状态如何决定单细胞水平的转录激活阈值，与你跨细胞类型增强子活性预测项目中关于细胞类型特异性的生物学理解有间接关联。
- **方法**: 结合单细胞分选、单分子足迹法与转录调控数学建模的实验计算联合范式。
- **主要发现**: 群体水平呈梯度的转录响应在单细胞水平实为“全或无”开关，其源于染色质编码的TF占据率与激活强度的长期变异性，而非转录爆发或双稳态。
- **对我的启发**: 在构建虚拟表观遗传特征预测增强子活性时，需考虑TF占据率的染色质异质性及单细胞激活阈值效应，避免仅依赖群体平均特征导致预测偏差。

<details><summary>Abstract</summary>

Quantitatively relating transcription factor (TF) input to gene expression output is central to understanding mammalian gene regulation and essential for designing predictable synthetic expression systems. However, even minimal synthetic systems often exhibit unexplained behaviors. In a widely used inducible mammalian expression system, we show that transcriptional responses appear graded and sigmoidal at the population level but are largely all-or-none at the single-cell level. By combining single-cell sorting and single-molecule footprinting with mathematical modeling of transcriptional regulation, we found that this behavior is not caused by bursty transcription or bistability, but by long-lived, chromatin-encoded variability in TF occupancy and activation strength. This variability produced a range of activation thresholds in switch-like single-cell responses that were stable over time, resulting in bimodal gene expression across the population. These results advance our basic understanding of how TFs interact with chromatin to modulate quantitative features of single-cell and population level transcriptional responses.

</details>

---

## 8. Empirical Evaluation of Single-Cell Foundation Models for Predicting Cancer Outcomes

- **期刊**: bioRxiv
- **作者**: Roman, A., Johri, S., Conci, R., Van Allen, E., Elmarakeby, H.
- **机构**: Eliezer Van Allen @ Dana Farber Cancer Institute
- **日期**: 2026-09-09
- **ID**: DOI: 10.1101/2025.10.31.685892  |  URL: https://www.biorxiv.org/content/10.1101/2025.10.31.685892v1
- **一句话推荐**: 系统评估单细胞基础模型在临床任务上的表现，其基础模型评估方法论（zero-shot、fine-tuning）可能对评估基因组基础模型有间接启发。
- **方法**: 提出一种基于代理（agentic）的自动化评估框架，系统评测12个单细胞基础模型在7项癌症临床任务（零样本、持续训练、微调）中的表现。
- **主要发现**: 当前单细胞基础模型在肿瘤微环境细胞注释等任务上表现优异，但在预测患者临床结局方面相比简单基线模型优势有限。
- **对我的启发**: 在评估预训练基因组学模型预测增强子活性的效用时，应引入简单基线模型进行严格对比，并可借鉴其自动化评估框架系统测试不同padding策略对模型性能的影响。

<details><summary>Abstract</summary>

Foundation models pretrained on large-scale single-cell RNA sequencing data present a promising opportunity to advance translational cancer research. However, their utility in clinically relevant, patient-level single-cell applications remains underexplored. Here, we developed an agentic strategy to systematically evaluate twelve emerging single-cell foundation models (scFMs) and three alternative baseline approaches across seven cancer-specific tasks, including cell-type annotation, cancer subtype classification, and treatment response prediction. We assessed model performance under zero-shot, continual training, and fine-tuning conditions, conducting 1,530 supervised model-fitting runs and 200 unsupervised subsample evaluations. We found that while current scFMs excelled at certain analysis tasks, such as tumor microenvironment cell annotation, they offered limited advantages in predicting clinical and biological outcomes of cancer patients compared to simpler baseline models. These insights highlight the critical role of scFM evaluation on biologically and clinically relevant tasks for precision oncology. Beyond identifying current limitations, this assessment reveals principles that can guide future methodological innovation and the use of expanded cancer single-cell cohorts to build more biologically informed and translationally effective scFMs. The resulting agentic framework supports the autonomous discovery of emerging scFMs and facilitates their standardized integration and evaluation across cancer-related tasks.

</details>

---

## 9. Are You Learning Biological Signal or Shortcuts? Auditing and Mitigating Bias in Protein-Protein Interaction Datasets

- **期刊**: arXiv
- **作者**: Judith Bernett, Anton Spannagl, Joel Ås, Markus List, David B. Blumenthal
- **日期**: 2026-09-09
- **ID**: arXiv: 2609.10193  |  URL: https://arxiv.org/abs/2609.10193
- **一句话推荐**: 系统审计生物ML数据集中的shortcut learning和数据划分偏差，方法论对评估基因组基础模型的泛化性和数据泄漏有间接启发。
- **方法**: 基于整数线性规划的相似性感知数据集划分与偏差最小化负样本采样框架。
- **主要发现**: PPI数据集存在多种隐蔽偏差导致模型学习捷径，且直觉性的高置信度负样本采样反而会放大功能相关性偏差；通过优化算法进行数据划分和负采样可有效缓解。
- **对我的启发**: 在构建增强子活性预测的正负样本集时，可借鉴基于优化的负样本采样策略以平衡序列特征（如GC含量、长度）分布，防止预训练基因组学模型利用padding或序列捷径而非真实表观遗传特征进行预测。

<details><summary>Abstract</summary>

Protein-protein interaction (PPI) databases do not faithfully reflect biological realities. Instead, they are influenced by study and technical biases that distort certain protein and interaction attributes. Machine learning models can exploit these as learning shortcuts if the negative dataset is not constructed with care. So far, the shortcuts introduced during PPI dataset construction have only been examined in isolation. Here, we systematically characterize both reported and, to our knowledge, previously unreported biases in PPI datasets that lead machine learning models to learn shortcuts instead of biological signal. We analyze HIPPIE, IntAct, and STRING, dedicated PPI databases, as well as two datasets derived from 3D-structural information in the Protein Data Bank (PDB). We show that random data splitting introduces strong topological shortcuts. When train-test protein overlap is removed, the resulting datasets still retain usable shortcuts stemming from self-interactions, taxonomic identity, and functional relatedness, whose prevalence interestingly depends on the data source. We further show that sampling negatives from a set of high-confidence non-interactors, an intuitively appealing choice, can amplify the shortcut stemming from functional relatedness. To detect and mitigate these biases, we provide an open Nextflow pipeline that combines similarity-aware, data-loss-minimizing dataset splitting with bias-minimizing negative sampling, both formulated as integer linear programs. Its key concept of quantifying biases to minimize them through optimization-based negative sampling can, in principle, be extended to any machine learning problem where the pool of negative candidates is much larger than the positives and is thus of interest also beyond PPI prediction.

</details>

---
