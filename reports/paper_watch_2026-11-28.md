# Paper Scout 日报 2026-11-28

共推荐 **6** 篇论文。

## 1. Benchmarking sequence-to-function models and mapping enhancer-gene interactions with E2GScore

bioRxiv · 预印本 · 2026-11-26 · 相关性 10/10

**研究关联：当前课题直接相关**

- **为什么值得看**：直接评估sequence-to-function模型在enhancer-gene预测和跨细胞类型（K562与astrocytes）泛化中的表现，与你的跨细胞类型增强子活性预测项目高度契合。
- **任务与验证范围**：输入：DNA序列（通过预训练sequence-to-function模型） → 输出：增强子-基因归因得分及互作预测；研究物种/细胞体系：人类（K562细胞、原代人星形胶质细胞，及454个人类生物样本）；验证范围：跨细胞类型，基于CRISPRi筛选数据进行验证。
- **核心方法**：构建统一基准测试框架（E2GScore），系统比较不同归因评分协议（如基因读出归一化、输入梯度等）对sequence-to-function模型预测增强子-基因互作性能的影响。
- **主要发现与证据**：基因读出归一化和匹配细胞类型的表达轨迹是性能关键，且输入梯度计算成本低于计算机模拟诱变但效果相当；AlphaGenome 1和2在K562和星形胶质细胞中优于其他7个模型和3个实验预测器，尤其在远端增强子上；跨模型在星形胶质细胞中性能下降主要归因于基准数据集组成差异（如增强子-TSS距离）。
- **可借鉴点（研究建议）**：在评估预训练基因组学模型时，可借鉴其对归因评分协议的消融分析思路，推测模型输入端的 padding 策略可能同样作为预处理变量影响下游增强子归因得分的稳定性。
- **迁移边界**：原论文聚焦于增强子-基因互作的归因评分基准测试，而我的任务侧重于游离型增强子活性预测及 padding 机制评估；原论文证明了跨细胞类型泛化，但未涉及 padding 对模型性能的影响，不能将此结论直接迁移至 padding 任务。
- **阅读时核实**：在使用输入梯度计算归因得分时，不同 sequence-to-function 模型对输入序列边缘的 padding 处理方式是否一致，以及这是否会影响远端增强子的归因得分？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.24.769033v1) · [DOI](https://doi.org/10.64898/2026.11.24.769033)

作者：The-Tjoean, C., Alinejad-Rokny, H., Voineagu, I.
来源标注的末位/通讯作者：Irina Voineagu
机构：University of New South Wales (UNSW Sydney), Sydney, NSW, Australia

### 英文摘要

Sequence-to-function models predict gene expression and chromatin features directly from DNA sequence and are increasingly used to infer enhancer-gene regulatory interactions. However, differences in attribution procedures and benchmarking datasets complicate comparisons between models, while the biological information captured by their enhancer-gene scores remains poorly understood. Here we introduce E2GScore, a unified framework for extracting and benchmarking enhancer-gene predictions from sequence-to-function models. By systematically varying scoring protocols, we identify gene-readout normalization and cell-type-matched expression tracks as important determinants of performance, whereas in silico mutagenesis offers no advantage over less computationally demanding input gradients. We compare seven sequence-to-function models and three established enhancer-gene predictors against CRISPR interference screens in K562 cells and primary human astrocytes. AlphaGenome 1 and 2 outperformed all other sequence-to-function models, and matched or outperformed experimentally informed predictors, particularly for distal enhancers, without a statistically significant difference between AlphaGenome versions after multiple-testing correction. We further show that the apparent reduction in predictive performance in astrocytes relative to K562 cells observed across models results primarily from differences in benchmarking dataset composition, particularly enhancer-TSS distance and target-gene expression. Using the open-weight AlphaGenome 1, we then generated E2GMap, a genome-wide resource of enhancer-gene regulation comprising 14.7 billion enhancer-gene attribution scores across 454 human biosamples, 45% of which are absent from existing enhancer-gene maps such as those from ENCODE-rE2G and AlphaGenome 2. E2GMap is available at e2gscore.com. Together, E2GScore and E2GMap establish a framework for rigorous evaluation of sequence-based enhancer-gene predictions and provide an extensible resource for studying gene regulation across human cell types and tissues.

---

## 2. GRACE: Discrete Biological Sequence Optimization with Gradient-Resolved Adaptive Constrained Exploration

bioRxiv · 预印本 · 2026-11-27 · 相关性 8/10

**研究关联：研究兴趣拓展**

- **为什么值得看**：提出约束优化方法GRACE用于生物序列重设计，直接评估了细胞类型特异性增强子活性优化任务。
- **任务与验证范围**：输入：参考生物序列及目标/辅助属性约束 → 输出：满足约束且目标属性提升的优化序列；研究物种/细胞体系：摘要未说明；验证范围：跨14个任务（6蛋白质、5DNA、3RNA），DNA任务包含细胞类型特异性增强子等，但未明确具体细胞类型数量
- **核心方法**：基于直通估计器提取预测模型梯度进行离散序列优化，结合零空间投影与增广拉格朗日机制处理多属性约束
- **主要发现与证据**：在包含5个DNA任务（如细胞类型特异性增强子）的14个任务中，GRACE在目标属性改进上优于离散和连续基线，同时满足辅助约束
- **可借鉴点（研究建议）**：其将增强子活性与细胞特异性视为约束权衡的思路，可启发我思考预测模型是否在特征空间中解耦了这些属性，但这属于推测
- **迁移边界**：原论文为序列优化任务，依赖预测模型梯度；我的研究为序列到功能预测及padding评估，无序列生成环节，GRACE方法无法直接迁移，且其跨细胞类型泛化未在摘要中验证
- **阅读时核实**：GRACE在细胞类型特异性增强子任务中依赖的预测模型架构是什么？该模型是否使用了表观遗传特征，以及序列长度/padding如何处理？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.25.769355v1) · [DOI](https://doi.org/10.64898/2026.11.25.769355)

作者：Tahmid, M. T., Hoang, M., Singh, M.
来源标注的末位/通讯作者：Mona Singh
机构：Princeton University

### 英文摘要

Machine learning increasingly enables biological sequence redesign for therapeutic and biotechnological applications by optimizing sequences for desired properties. However, improving one property can compromise another: for example, increasing enzyme activity may reduce stability, while enhancing regulatory DNA activity may diminish cell-type specificity. We formulate sequence redesign as a constrained optimization problem guided by learned predictive models, where a reference sequence is mutated to improve a predicted target property while keeping predicted auxiliary properties within specified tolerances of their reference values. To solve this problem, we introduce GRACE (Gradient-Resolved Adaptive Constrained Exploration), a method that optimizes discrete biological sequences using gradients from property predictors via a straight-through estimator. GRACE combines two complementary mechanisms: null-space projection, which removes target-gradient components that interfere with active constraints, and an augmented Lagrangian mechanism, which encourages feasibility after constraint violations. We evaluate GRACE across fourteen diverse tasks, including six protein optimization tasks (spanning activity, stability, and solubility), five DNA tasks (spanning cell-type-specific enhancer activity, heat-shock-responsive promoters, and tissue-selective splicing), and three RNA design tasks (spanning translation efficiency, RNA folding, and toehold-switch function). Across these tasks, GRACE consistently achieves larger improvements in predicted target properties than discrete and continuous baselines while satisfying predicted auxiliary constraints. Together, these results establish GRACE as a general framework for machine-learning-guided biological sequence redesign under competing property constraints.

---

## 3. HapAdapter: A Transfer Learning Protocol for DNA Foundation Models Adapted to Diploid Personal Epigenomes

bioRxiv · 预印本 · 2026-11-27 · 相关性 7/10

**研究关联：方法可借鉴**

- **为什么值得看**：提出迁移学习协议HapAdapter，将DNA基础模型（如AlphaGenome）适配到二倍体个人表观基因组预测。
- **任务与验证范围**：输入：二倍体个人基因组序列 → 输出：跨测定的等位基因特异性效应预测；研究物种/细胞体系：摘要未说明；验证范围：跨九种测定，在DNABERT-2和AlphaGenome两个基础模型骨干上验证
- **核心方法**：在预训练DNA基础模型之上构建轻量级孪生网络适配器进行迁移学习，以处理二倍体基因组上下文。
- **主要发现与证据**：轻量级适配器显著提升了模型等位基因特异性辨别能力，使DNABERT-2和AlphaGenome的AUROC分别比随机水平平均提高130%和210%（跨九种测定）。
- **可借鉴点（研究建议）**：针对预训练基因组学模型在特定任务（如增强子活性预测）上的微调，可考虑引入轻量级适配器结构以低成本适应新输入特征或上下文，而非重新训练整个模型。
- **迁移边界**：原论文针对二倍体基因组的等位基因特异性预测，使用孪生网络处理双等位基因；我的研究关注不同细胞类型增强子活性和padding影响，任务设定不同，孪生网络结构未必直接适用，且原论文未验证跨细胞类型泛化或padding策略。
- **阅读时核实**：HapAdapter在处理二倍体序列输入时，是否对两条单倍型序列进行了对齐或padding操作？其输入长度和padding策略如何影响等位基因特异性预测的性能？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.25.769310v1) · [DOI](https://doi.org/10.64898/2026.11.25.769310)

作者：Rozowsky, J., Metrick, A., Wang, J., Onut, A., Cui, J., Li, T., Gerstein, M.
来源标注的末位/通讯作者：Joel Rozowsky
机构：Yale University

### 英文摘要

The rapid rise of large language models (LLMs) has spurred the development of genomic language models (gLMs) that capitalize on the key features of natural language present in biological sequences. Moreover, DNA foundation models, a sub-class of gLMs, have demonstrated impressive accuracy in predicting a wide range of functional tracks from DNA sequence input. However, current DNA foundation models are exclusively trained on haploid reference genome sequences -- despite personal and graph genomes becoming the new standard for genomic analyses. This is principally because the cost to train gLMs on a personal diploid genome for a single individual is not currently practical. To help reconcile this disconnect between the current available use-cases of DNA foundation models with the modern direction of genomic sequence analysis, we present HapAdapter, a transfer-learning protocol that builds a small Siamese network on top of any pre-trained foundation model to enable inference from full diploid personal genome context. To demonstrate the utility of this method, we train a set of HapAdapter heads to predict allele-specific effects across assays on two representative foundation model backbones: DNABERT-2 and AlphaGenome. We demonstrate that our lightweight adapter more than doubles DNABERT-2's allele-specific discrimination and triples AlphaGenome's (130% and 210% gain in AUROC above chance, respectively, averaged over nine assays).

---

## 4. A Framework for Identifying Determinants of Epigenomic State: Decoding Variable CTCF Occupancy and Contact Frequency

bioRxiv · 预印本 · 2026-11-27 · 相关性 7/10

**研究关联：方法可借鉴**

- **为什么值得看**：提出跨数百细胞/组织类型识别表观基因组状态决定因素的计算框架，涉及细胞类型特异性TF占据预测和增强子-启动子互作，与你的调控基因组学和跨细胞类型泛化研究高度相关。
- **任务与验证范围**：输入：跨细胞/组织的CTCF ChIP-seq结合数据及相关表观/表达特征 → 输出：CTCF结合变异的驱动机制分类及结合状态预测；研究物种：摘要未说明；细胞体系：数百种细胞/组织；验证范围：跨细胞/组织类型（held-out样本预测及染色质构象/基因表达验证）
- **核心方法**：提出一种通用计算框架，通过分析跨细胞类型多组学特征来聚类并识别驱动表观基因组状态变异的机制。
- **主要发现与证据**：识别出5种调控CTCF结合变异的机制，其中受CTCF表达水平调控的弱亲和力位点占比最大；该模型能有效预测held-out样本的CTCF结合，并关联预测染色质接触频率与基因表达差异。
- **可借鉴点（研究建议）**：将TF表达水平、侧翼共结合等特征与序列亲和力结合以解释跨细胞类型表观变异的思路，可为我构建虚拟表观遗传特征预测增强子活性提供特征工程参考。
- **迁移边界**：原论文聚焦于CTCF结合的跨细胞变异机制解析与预测，而我的任务是基于DNA序列/虚拟特征预测增强子活性及评估模型padding影响；其跨细胞类型泛化机制不能直接等同于增强子活性预测的泛化能力，且原论文未涉及序列模型架构层面的评估。
- **阅读时核实**：该框架在预测held-out样本的CTCF结合时，具体使用了哪些特征作为模型输入？是否利用了DNA序列特征？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.25.769053v1) · [DOI](https://doi.org/10.64898/2026.11.25.769053)

作者：Yang, Y., Beer, M. A.
来源标注的末位/通讯作者：Michael A. Beer
机构：Johns Hopkins Univ

### 英文摘要

CTCF binding is essential for delineating topologically associated domains, constraining enhancer-promoter interactions, and controlling gene expression. Many CTCF peaks are bound in all cell-types, but the mechanisms regulating cell-type-specific CTCF occupancy are not fully understood. Here, we present a general framework to comprehensively discover factors driving variable epigenomic state and TF occupancy. We apply this framework to CTCF ChIP-seq binding across hundreds of cell/tissues, and we identify five distinct mechanisms regulating CTCF occupancy. In addition to known mechanisms of DNA methylation and cell-type-specific TF co-binding, we find that the largest set of variable-occupancy sites is modulated by CTCF expression levels. Variable peaks have weaker-affinity, and their occupancy is modulated by either higher CTCF levels or flanking TFs. We evaluate the predictive power on CTCF occupancy in held-out samples. Finally, we show that variable CTCF binding predicts differential contact frequency, chromatin loop structure, and upregulation of gene expression.

---

## 5. GNEval: A Context-Specific Benchmark for Gene Network Inference with Single-Cell Foundation Models

bioRxiv · 预印本 · 2026-11-27 · 相关性 6/10

**研究关联：方法可借鉴**

- **为什么值得看**：评估单细胞基础模型在基因网络推断和Perturb-seq扰动响应中的表现，涉及单细胞扰动领域。
- **任务与验证范围**：输入：预训练单细胞模型的基因表示与关联得分；输出：基因网络推断结果及评估。物种：摘要未说明。细胞体系：跨多种细胞系统。验证范围：基于14个Perturb-seq数据集跨细胞系统、扰动类型和数据大小验证。
- **核心方法**：构建统一基准测试框架（GNEval），系统评估预训练单细胞基础模型衍生的静态嵌入、上下文嵌入及注意力得分在基因网络推断中的表现。
- **主要发现与证据**：评估任务与模型间存在显著异质性，基于GO和Perturb-seq证据的排名几乎不相关（Spearman rho = -0.05）；上下文无关表示在恢复功能关系上具优势（Delta AUROC = 0.13），上下文相关关联在恢复扰动相关差异表达关系上提升3.8倍；领域特定方法在两类证据上表现更均衡。
- **可借鉴点（研究建议）**：可借鉴其多维度评估框架，在评估预训练基因组学模型在不同细胞类型增强子预测或不同padding策略时，引入多视角证据进行对比，而非依赖单一指标。
- **迁移边界**：原论文针对单细胞转录组基础模型和基因网络推断任务，而我的研究聚焦DNA序列层面的增强子活性预测及padding影响，跨模态（RNA到DNA）和跨任务（网络推断到序列到功能）的结论不能直接迁移。
- **阅读时核实**：论文中“上下文相关”与“上下文无关”基因表示的具体提取方式是什么？在评估不同细胞系统时，模型是直接使用预训练输出还是经过了特定微调？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.25.769274v1) · [DOI](https://doi.org/10.64898/2026.11.25.769274)

作者：Hu, T., Wu, W., Qin, Z., Su, C.
来源标注的末位/通讯作者：Chang Su
机构：Emory University

### 英文摘要

Gene network (GN) inference plays a critical role in understanding gene relationships and their roles in biological functions and diseases. Existing single-cell GN inference methods often rely on limited data from individual studies. Single-cell foundation models, pretrained on large and diverse datasets, provide a range of gene-gene association signals that offer a promising basis for GN inference. However, it remains unclear which GN properties these signals capture and how they compare with domain-specific methods. To address this gap, we introduce GNEval, a unified benchmark for evaluating pretrained model derived gene associations for network inference. We benchmark 21 gene representations and association scores from 11 models, including static gene embeddings (S), contextual embeddings (C), and gene-gene attention scores (A). GNEval assesses inferred networks based on their consistency with functional and perturbational evidence, including 14 Perturb-seq datasets across diverse cell systems, perturbation types and data sizes. The results reveal substantial heterogeneity across evaluation tasks and models. Rankings based on Gene Ontology and Perturb-seq evidence were nearly uncorrelated (Spearman {rho} = -0.05). Context-independent representations showed a substantial advantage in recovering functional relationships ({Delta}AUROC = 0.13), whereas context-dependent gene associations improved recovery of perturbation-associated differential expression relationships by 3.8x. The domain-specific method achieves relatively strong performance on both evidence types, offering a better balance across the two evaluations than most foundation-model-derived networks. Overall, gene representations and association scores show task-specific strengths, highlighting the need for task-aware selection and integration with domain-specific methods.

---

## 6. Task-aligned foundation model representations enable single-cell cytokine response inference

bioRxiv · 预印本 · 2026-11-27 · 相关性 6/10

**研究关联：方法可借鉴**

- **为什么值得看**：利用冻结的单细胞基础模型嵌入进行扰动响应推断，与你的单细胞扰动研究兴趣直接相关，且涉及基础模型表示的适配策略。
- **任务与验证范围**：输入：单细胞转录组数据（结合供体调整的接收状态与匹配对照中心的偏差） → 输出：跨90种细胞因子的相对单细胞响应评分；研究物种/细胞体系：摘要未说明（涉及COVID-19队列）；验证范围：跨独立扰动数据集、体内数据集及未配对COVID-19队列，是否跨细胞类型摘要未明确说明
- **核心方法**：基于冻结的单细胞基础模型嵌入，结合供体调整的接收状态与匹配对照中心的偏差，通过共享分类器推断相对响应评分。
- **主要发现与证据**：基线相对表示在留出供体预测中优于直接使用基础模型嵌入（基于State SE和scFoundation）；在独立扰动和体内数据集中，CYTAP能将施加的细胞因子排在前十名；在COVID-19队列中，推断响应与疾病严重程度相关且IL-6响应评分与血浆浓度相关。
- **可借鉴点（研究建议）**：论文利用“相对于匹配对照中心的偏差”来适配冻结的预训练模型嵌入以适应下游任务，这种引入生物学定义的参考基线来微调表示的思路，可能启发我在增强子活性预测中探索引入特定参考状态来处理预训练基因组学模型的特征表示。
- **迁移边界**：原论文任务是基于单细胞转录组推断细胞因子响应，我的任务是基于DNA序列预测增强子活性并评估padding影响。原论文在转录组模态的跨细胞因子泛化不能等同于跨细胞类型泛化，其基于转录组特征的方法也不能直接迁移到DNA序列任务上，需注意模态与任务的根本差异。
- **阅读时核实**：CYTAP中“匹配对照中心”的具体构建方式是什么？在不同细胞类型或条件下，该对照中心是否需要重新计算？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.26.769597v1) · [DOI](https://doi.org/10.64898/2026.11.26.769597)

作者：Jeong, Y. L., Kim, J. K.
来源标注的末位/通讯作者：Jong Kyoung Kim
机构：Pohang University of Science and Technology (POSTECH)

### 英文摘要

Inferring cellular responses from single-cell transcriptomes requires interpreting changes relative to an appropriate baseline while retaining cell-type context. Here we present CYTAP, which adapts frozen single-cell foundation model embeddings for cytokine-response inference by combining donor-adjusted receiver states with deviations from matched control centroids. CYTAP uses a shared classifier to assign relative single-cell response scores across 90 cytokines and supports unpaired analyses using counterfactual control references. Baseline-relative representations improved held-out-donor prediction with both State SE and scFoundation. Across independent perturbation datasets, CYTAP prioritized applied cytokines, including when receptor transcripts were sparsely detected, and ranked administered cytokines among the top ten in both in vivo datasets. In an unpaired COVID-19 cohort, inferred responses were associated with severity, and IL-6 response scores correlated with plasma IL-6 concentrations. These findings support the use of biologically defined references to adapt pretrained representations for functional response inference.

---

中文笔记基于标题和摘要生成，未核验全文；研究建议不代表论文已验证的结论。相关性分数不是论文质量评分。

检索统计：窗口 [2026-11-25 00:00, 2026-11-28 00:00) UTC；抓取 biorxiv 150/pubmed 46 → 粗筛 37 篇 → LLM 选中 6 篇
