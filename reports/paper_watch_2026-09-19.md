# Paper Scout 日报 2026-09-19

共筛选出 **10** 篇推荐论文。
📊 抓取 arxiv 18/biorxiv 118/pubmed 53 → 粗筛 42 篇 → LLM 选中 10 篇

## 1. Predicting cellular responses to perturbation across diverse contexts with State.

- **期刊**: Cell
- **作者**: Abhinav K Adduri, Dhruv Gautam, Beatrice Bevilacqua et al. (32 authors)
- **机构**: Yusuf H Roohani @ Arc Institute, Palo Alto, CA, USA. Electronic address: yusuf.roohani@arcinstitute.org.
- **日期**: 2026-08-31
- **ID**: DOI: 10.1016/j.cell.2026.07.052  |  PMID: 42673963  |  URL: https://pubmed.ncbi.nlm.nih.gov/42673963/
- **相关分数**: 8/10
- **一句话推荐**: 提出State模型预测跨细胞环境的单细胞扰动效应，与跨细胞类型泛化及单细胞扰动预测高度相关。
- **方法**: 基于1.67亿单细胞转录组数据预训练细胞嵌入，构建预测跨细胞上下文扰动效应的机器学习模型（State）。
- **主要发现**: State在预测遗传、信号和化学扰动效应上准确率显著优于基线，并能泛化至未见扰动的细胞上下文；同时提出了综合评估框架Cell-Eval。
- **对我的启发**: 利用大规模观察性数据预训练上下文嵌入以实现跨上下文泛化的范式，可启发在增强子活性预测中结合细胞类型特异性的虚拟表观遗传特征嵌入，以提升模型在不同细胞类型间的泛化能力。

<details><summary>Abstract</summary>

While machine learning models offer potential for predicting transcriptomic effects of perturbation, they currently struggle to generalize across cellular contexts. Here, we introduce State, a machine learning model that predicts perturbation effects while accounting for cellular heterogeneity within and across experiments. State is trained using single-cell gene expression data to predict perturbation effects across sets of cells. State improved discrimination of effects on large datasets by more than 30% and identified differentially expressed genes across genetic, signaling, and chemical perturbations with significantly improved accuracy compared with baselines. Its cell embeddings trained on observational data from 167 million cells enable the identification of strong perturbations in cellular contexts where no perturbations were observed during training. We further introduce Cell-Eval, a comprehensive evaluation framework that can be used to evaluate future models. Overall, the performance and flexibility of State set the stage for scaling the development of AI models of cell state.

</details>

---

## 2. Virtual Cell Challenge 2026: Benchmarking zero-shot generalization across cellular contexts.

- **期刊**: Cell
- **作者**: Hani Goodarzi
- **机构**: Hani Goodarzi @ Arc Institute, Palo Alto, CA, USA; University of California, San Francisco, San Francisco, CA, USA. Electronic address: hani.goodarzi@arcinstitute.org.
- **日期**: 2026-08-26
- **ID**: DOI: 10.1016/j.cell.2026.08.004  |  PMID: 42648290  |  URL: https://pubmed.ncbi.nlm.nih.gov/42648290/
- **相关分数**: 8/10
- **一句话推荐**: 虚拟细胞挑战赛聚焦跨细胞环境的零样本扰动预测，直接契合跨细胞类型泛化与单细胞扰动的研究兴趣。
- **方法**: 构建基于零样本泛化范式的基因敲降响应预测模型，评估跨细胞环境的泛化能力。
- **主要发现**: 提出2026年虚拟细胞挑战赛，通过在未见细胞系上预测基因敲降响应，检验现有模型能否缩小临床前预测与人类生物学间的差距。
- **对我的启发**: 可借鉴其跨细胞环境零样本泛化的基准测试设计，评估不同padding策略对预训练基因组学模型在未见细胞类型增强子活性预测上的泛化影响。

<details><summary>Abstract</summary>

The Virtual Cell Challenge returns in 2026 with a more demanding test of biological generalization: zero-shot prediction across multiple independent cellular contexts. Participants will build models to predict gene knockdown responses in a new Arc-generated dataset comprising unseen cell lines. The goal is to determine whether the best models can meaningfully close the gap between preclinical experimental predictions and human biology.

</details>

---

## 3. A world model of the virtual cell.

- **期刊**: Cell
- **作者**: Eric P Xing, Le Song
- **机构**: Le Song @ GenBio AI, Palo Alto, CA, USA; Mohamed bin Zayed University of Artificial Intelligence, Abu Dhabi, UAE. Electronic address: le.song@genbio.ai.
- **日期**: 2026-09-17
- **ID**: DOI: 10.1016/j.cell.2026.08.042  |  PMID: 42753692  |  URL: https://pubmed.ncbi.nlm.nih.gov/42753692/
- **相关分数**: 7/10
- **一句话推荐**: 提出虚拟细胞世界模型(VCWM)框架，与虚拟细胞、单细胞扰动及基础模型构建思路高度相关。
- **方法**: 提出虚拟细胞世界模型（VCWM），一种基于状态演化和动作条件干预的动态多尺度系统建模范式。
- **主要发现**: 相比仅针对特定任务优化的预测性基础模型，VCWM通过建模底层细胞系统并维持持续状态，能更连贯地模拟基因或化学干预下的多模态细胞演化结果。
- **对我的启发**: 其强调的“状态持续性”理念启发我在增强子活性预测中，可尝试将虚拟表观遗传特征作为细胞类型的隐式状态变量，以提升模型在跨细胞类型泛化时的表征稳定性。

<details><summary>Abstract</summary>

The prospect of an AI-driven digital organism (AIDO), such as a virtual cell, has recently captured growing excitement and imagination across the AI and biology communities. We envision a virtual cell as a multi-modal, multi-scale, dynamic, and stateful computational system capable of simulating the activity and behavior of a living cell. Such a system could shift cell biology from trial-and-error experimentation with cell-culture models in the wet lab toward systematic simulation of combinatorial interventions in a digital laboratory. In this paper, we propose the world model as an operational framework for realizing this vision-an emerging AI paradigm that supports action-conditioned simulation, counterfactual reasoning and long-horizon planning in complex dynamic environments. In this formulation, a virtual cell world model (VCWM) represents a persistent cellular state and simulates its evolution under genetic, chemical, environmental, and other biological interventions. In contrast to predictive foundation models optimized for specific tasks or endpoints, a VCWM seeks to model the underlying cellular system, allowing interventions to propagate through an evolving state and generate coherent molecular, structural, interactional, and morphological outcomes over time. We outline an architecture, a data framework, training strategy, and evaluation principles for realizing this vision and discuss how existing biological foundation models can serve as its building blocks. We envisage that VCWMs could transform biological discovery from exhaustive experimental search toward structured navigation of learned cellular worlds, enabling counterfactual exploration, rational intervention design, and ultimately more predictive, designable, and programmable cell biology.

</details>

---

## 4. Tahoe-100M: Mapping drug-induced molecular phenotypes at single-cell resolution.

- **期刊**: Cell
- **作者**: Jesse Zhang, Airol A Ubas, Valentine Svensson et al. (40 authors)
- **机构**: Johnny Yu @ Tahoe Therapeutics, South San Francisco, CA, USA. Electronic address: johnny@tahoebio.ai.
- **日期**: 2026-09-17
- **ID**: DOI: 10.1016/j.cell.2026.08.035  |  PMID: 42753697  |  URL: https://pubmed.ncbi.nlm.nih.gov/42753697/
- **相关分数**: 7/10
- **一句话推荐**: 大规模单细胞扰动图谱（100M细胞×1100药物条件），直接对应我的single-cell perturbation和virtual cell研究兴趣，且明确支持AI预测模型训练。
- **方法**: 基于多重化单细胞测序技术构建千万级药物扰动转录组图谱，并提取通路特征以训练细胞行为预测模型。
- **主要发现**: 构建了包含1亿单细胞的大规模药物扰动图谱，系统量化了药物诱导的细胞表型与转录组异质性，揭示了药物作用机制及耐药相关应激反应。
- **对我的启发**: 其利用大规模扰动数据训练AI预测模型的范式，可启发在增强子活性预测中引入CRISPRi等大规模增强子扰动数据集来预训练和评估sequence-to-function模型。

<details><summary>Abstract</summary>

We present Tahoe-100M, a giga-scale single-cell perturbation atlas comprising 100 million transcriptomes from 50 diverse cancer cell lines treated with 1,100 drug-dose conditions. This parallel profiling of thousands of perturbations at single-cell resolution with minimal batch effects is enabled by the Mosaic platform, which multiplexes genetically distinct cell models into balanced "cell villages." Beyond cataloging transcriptomic shifts, Tahoe-100M systematically quantifies cellular phenotypes, including proliferation, cytotoxicity, lineage-specific vulnerabilities, and cell-cycle changes. It captures population-level transcriptomic heterogeneity, characterizing whether drug responses drive cells toward divergent fates or convergent states. Pathway-based signatures define drug-induced expression programs, classify mechanisms of action, reveal off-target activities, and expose adaptive stress responses associated with resistance. By unifying cellular and molecular readouts, this broadly applicable perturbation atlas advances our ability to model gene regulation, drug response, and network dynamics. Its public release enables the training of AI frameworks to advance predictive models of cell behavior.

</details>

---

## 5. An atlas of transcription factor cooperation reveals how motif readers shape regulatory output

- **期刊**: bioRxiv
- **作者**: Xiong, H., Liu, J., Wang, W.
- **机构**: Wei Wang @ University of California, San Diego
- **日期**: 2026-09-18
- **ID**: DOI: 10.64898/2026.09.14.751590  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.14.751590v1
- **相关分数**: 7/10
- **一句话推荐**: 跨10种细胞类型分析1552个TF结合数据集，研究motif-TF依赖机制与调控输出的关系，直接涉及细胞类型特异性调控和motif到功能的映射。
- **方法**: 利用多智能体系统（ARES）结合多组学数据，推断特定细胞类型中转录因子与基序依赖关系的竞争性机制。
- **主要发现**: 基序的调控结果并非由其序列本身决定，而是由实际读取该基序的蛋白（reader）决定；基序更像一个地址，其功能输出由反式作用蛋白塑造。
- **对我的启发**: 在基于序列预测增强子活性时，不能仅依赖基序序列特征，需考虑特定细胞类型下反式作用因子（reader蛋白）的丰度或虚拟表观遗传特征对基序功能输出的决定性影响。

<details><summary>Abstract</summary>

Regulatory motifs are conventionally associated with named transcription factors (TFs), yet a motif label need not identify the protein that reads the sequence or the regulatory consequence that follows in a given cell. We analyzed 1,552 TF binding datasets in 10 cell types using ARES, a multi-agent system that tests competing mechanisms of TF-motif dependencies in a specific cellular context against multi-omic data. We found that the inferred mechanisms converged on three operating routes: direct sequence recognition, protein-mediated recruitment or exclusion, and regulatory context. Importantly, the predictive motifs of the target TF binding were read by their conventionally "canonical" TFs in only one third of resolved dependencies, and these "canonical" TFs were expressed much less often than the inferred readers. Furthermore, we observed that motif similarity was associated with shared regulatory region type but not shared transcriptional outcome, whereas reader identity was associated with both and the only feature among the examined associated with outcome. In validation case studies where an inferred reader was perturbed, target TF occupancy fell in proportion to reader binding before perturbation, and a natural variant disrupting the predictive motif altered target TF binding at every intermediate step of the inferred mechanism. These observations were further supported by single-cell perturbation, in vitro cooperativity and evolutionary constraint. Together, these results separate motif identity from reader identity and regulatory output, suggesting that a motif acts as an address whose regulatory consequence is shaped in trans by the protein that interprets it.

</details>

---

## 6. DELPHAI predicts heterogeneous perturbation responses with learned single-cell fitness

- **期刊**: bioRxiv
- **作者**: Zhang, X., Wu, H., Liu, H.
- **机构**: Xian Zhang @ aiPTO TechBio
- **日期**: 2026-09-17
- **ID**: DOI: 10.64898/2026.07.01.735965  |  URL: https://www.biorxiv.org/content/10.64898/2026.07.01.735965v1
- **相关分数**: 7/10
- **一句话推荐**: DELPHAI预测单细胞扰动响应，直接命中我研究兴趣中的single-cell perturbation方向，且涉及fitness-gated最优传输与基因空间检索。
- **方法**: 联合训练适应度网络与最优传输网络，并在推理阶段结合适应度门控与基因空间直接检索的扰动响应预测范式。
- **主要发现**: 该模型在预测差异表达基因的基准测试中表现最优，且能准确揭示扰动对特定细胞谱系的耗竭效应，克服了传统模型细胞质量守恒的假设缺陷。
- **对我的启发**: 模型在推理时采用“直接基因空间检索”以避免隐空间解码丢失信息的思路，可启发我在sequence-to-function映射中评估直接检索表观特征空间而非过度依赖隐空间解码的有效性。

<details><summary>Abstract</summary>

Current perturbation response modelling in single-cell transcriptomics assumes conserved cell mass and loses gene expression information to latent-space decoding. We propose DELPHAI, training a fitness network and an optimal transport network jointly without biological priors, and during inference applying a fitness-gated transport with a direct gene-space retrieval. Demonstrated across two benchmark frameworks, DELPHAI ranks first in predicting differentially expressed genes, while revealing which cell lineages a perturbation depletes.

</details>

---

## 7. Machine learning reveals sequence and genomic context features underlying Alu-specific effects on genome folding

- **期刊**: bioRxiv
- **作者**: Zhang, S., Pollard, K. S.
- **机构**: Katherine S Pollard @ Gladstone Institutes
- **日期**: 2026-09-18
- **ID**: DOI: 10.64898/2026.09.16.752217  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.16.752217v1
- **相关分数**: 6/10
- **一句话推荐**: 使用深度学习对Alu元件进行in silico删除筛选预测其对染色质折叠的影响，属于sequence-to-function范式，涉及序列特征与基因组上下文对染色质结构的预测。
- **方法**: 基于深度学习的计算机模拟删除与诱变筛选，预测并解析转座元件对局部染色质三维结构的影响。
- **主要发现**: Alu元件对基因组折叠的调控取决于其内在序列与基因组上下文的协同，特定Alu能重塑CTCF介导的染色质边界与环。
- **对我的启发**: 其计算机模拟删除与突变筛选范式可启发我通过虚拟截断增强子序列或调整padding上下文，定量评估预训练模型对游离型增强子活性预测的上下文依赖性。

<details><summary>Abstract</summary>

The Alu transposable element is among the most abundant classes of mobile DNA in the human genome, and has been linked to gene regulation and chromatin organization. Yet how individual Alu insertions influence nearby chromatin interactions remains poorly understood. To investigate this, we used deep learning to perform a genome-wide in silico deletion screen of ~1.1 million Alus, predicting each element's importance to local genome folding. We identified a subset of high-scoring Alus that span multiple Alu subfamilies and are enriched in loci that are fast-evolving and gene-dense, especially loci encoding genes that are actively transcribed and/or related to Alu biology. We further found that polymorphic Alus preferentially occur in regions tolerant of sequence variation but predicted to be resistant to changes in chromatin structure. Targeted in silico mutagenesis showed that the importance of individual Alus to local chromatin interactions depends on both intrinsic Alu sequence properties and genomic context. Finally, we identified Alu sequences predicted to alter CTCF-mediated boundary strength and, in some cases, to promote the formation of new loops and boundaries. Together, these results position Alus as key modulators of genome architecture, while underscoring that the fate of a new Alu depends on where it inserts and how it interacts with other determinants of chromatin state and structure.

</details>

---

## 8. Pretrained gene representations transfer mean expression more broadly than spatial patterns in virtual spatial transcriptomics

- **期刊**: bioRxiv
- **作者**: Chen, T., Hicks, S. C.
- **机构**: Stephanie C Hicks @ Johns Hopkins Bloomberg School of Public Health
- **日期**: 2026-09-18
- **ID**: DOI: 10.64898/2026.09.15.751768  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.15.751768v1
- **相关分数**: 6/10
- **一句话推荐**: 系统评估预训练基因表示（scGPT、Decima）在空间转录组预测中的迁移能力，直接涉及foundation model表示学习的泛化性分析，与我的基因组基础模型评估兴趣相关。
- **方法**: 通过解耦基因平均表达与空间变异模式，评估预训练基因表示在虚拟空间转录组学中的跨基因泛化能力。
- **主要发现**: 预训练基因表示主要成功转移了基因的平均表达水平，而对空间表达模式恢复的提升有限且具有选择性。
- **对我的启发**: 在评估预训练基因组学模型预测增强子活性的迁移效果时，需解耦序列基线活性与细胞类型特异性活性，避免将均值预测的成功误认为上下文特异性预测的成功。

<details><summary>Abstract</summary>

Models that combine tissue images with pretrained gene representations aim to predict spatial expression for genes not used to fit the downstream predictor. Yet success on held-out genes can reflect two capabilities: estimating a gene's mean expression across tissue locations and recovering its spatial variation. Across four cohorts spanning three human brain regions and HER2-positive breast cancer, we evaluated held-out genes in held-out individuals and separated these components. For spatial predictors using fixed gene representations from Decima or scGPT, reductions in gene-mean error accounted for more than 91% of the reduction in mean squared error relative to matched random vectors. Independently fitted mean-only models using the same representations but no tissue images retained 90-99% of the corresponding gain in full-matrix correlation. Spatial gains were smaller on average, increased with expression variation in training tissue and differed across cohorts and representations. Across these settings, pretrained gene representations broadly transferred mean expression but selectively improved spatial recovery, showing that cross-gene generalization in virtual spatial transcriptomics is not a single capability.

</details>

---

## 9. Beyond the drug-centric view: Advancing AI virtual cell platforms for environmental perturbation modelling.

- **期刊**: ALTEX
- **作者**: Daniel Ukaegbu, Victor Curean, Andreas Bender, Alexandra Maertens
- **机构**: Alexandra Maertens @ Center for Alternatives to Animal Testing (CAAT), Johns Hopkins Bloomberg School of Public Health, Baltimore, MD, USA.
- **日期**: 2026-09-17
- **ID**: DOI: 10.14573/altex.2606062  |  PMID: 42758091  |  URL: https://pubmed.ncbi.nlm.nih.gov/42758091/
- **相关分数**: 4/10
- **一句话推荐**: 讨论了AI虚拟细胞平台在扰动建模中的扩展，与虚拟细胞和扰动预测的研究兴趣间接相关。
- **方法**: 综述探讨基于深度学习与基础模型架构的AI虚拟细胞平台在环境扰动建模中的范式演进与多模态整合。
- **主要发现**: 当前虚拟细胞模型过度侧重药物与遗传扰动，缺乏对环境扰动（剂量、时序、混合物）的标准化表征与多模态整合；需构建标准化数据集与不确定性感知评估框架以拓展其在公共卫生领域的应用。
- **对我的启发**: 在构建基于预训练基因组学模型的sequence-to-function映射时，可将环境扰动特征作为虚拟表观遗传特征的条件输入，并探究不同padding策略对模型捕捉此类长程扰动上下文依赖性的影响。

<details><summary>Abstract</summary>

Environmental exposures contribute substantially to global morbidity and mortality, with their biological effects shaped by factors such as dose, exposure duration, life-stage timing, and cumulative or sequential exposure patterns. With rapid advances in AI based virtual cell (VC) technologies, current frameworks emphasize genet-ic and pharmacological perturbations, leaving environmental perturbations insufficiently modelled. This imbal-ance is due to fundamental structural limitations in data availability, chemical space coverage, and representa-tional design, as well as lacking standardized annotation of dose, timing and mixtures, which are core deter-minants of environmental perturbations. This review argues that incorporating environmental perturbations as a foundational component of virtual cell development is necessary to extend these models toward environ-mental and public health applications. We review the evolution of these perturbation predictive models from mathematical models to deep learning and foundation model architectures, evaluate the status of virtual cell efforts across genomic, transcriptomic, proteomic, metabolomic and phenomic modalities, and show the sys-tematic gaps that currently limit their applicability to environmental health. We outline key challenges, includ-ing data scarcity and bias, inadequate representation of environmental perturbations, limited multimodal inte-gration, and weak benchmarking practices. To address these issues, we propose the development of stand-ardized environmental perturbation datasets, integrated and standalone multimodal architectures, uncertainty-aware evaluation metrics, and regulatory-aligned benchmarking frameworks which are all geared toward ad-vancing in silico perturbation and non-animal testing, promoting the 3Rs paradigm.

</details>

---

## 10. Setting the SCENE for Interpretable Cell-Gene Embeddings in Single-Cell RNA-seq

- **期刊**: bioRxiv
- **作者**: Moberg, O. L., Petersen, M. B., Herlau, T., Kristensen, L. E., Jessen, L. E., Morup, M.
- **机构**: Oscar Lauritz Møberg @ DTU (Technical University of Denmark)
- **日期**: 2026-09-18
- **ID**: DOI: 10.64898/2026.09.12.750699  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.12.750699v1
- **相关分数**: 4/10
- **一句话推荐**: 提出单细胞转录组数据的可解释细胞-基因嵌入方法，与表示学习和单细胞分析间接相关。
- **方法**: 提出SCENE模型，一种结合零膨胀计数似然与欧几里得潜在距离的概率图表示学习方法，将scRNA-seq计数矩阵建模为细胞-基因二部图。
- **主要发现**: 该模型在原生2D/3D低维空间中即可达到SOTA性能并保留主要生物结构，且能通过基因空间扰动分析捕捉超越细胞类型分离的生物学调控程序。
- **对我的启发**: 将稀疏高维计数矩阵视为二部图并结合零膨胀似然解耦信号检测与强度的思路，可启发在构建单细胞虚拟表观遗传特征时，对稀疏的增强子活性信号进行解耦建模与低维几何嵌入。

<details><summary>Abstract</summary>

Single-cell RNA sequencing measures cellular states at high resolution, but sparse high-dimensional count data remain difficult to model interpretably. We introduce the Single-Cell Euclidean Network Embedding (SCENE), a probabilistic latent-distance model that jointly embeds cells and genes from Unique Molecular Identifier (UMI) counts. SCENE treats the count matrix as a weighted bipartite cell-gene graph, where Euclidean distances represent transcriptional affinity, and combines this geometry with a zero-inflated count likelihood that separates gene detection from expression magnitude. Across real and simulated scRNA-seq datasets, SCENE recovers biologically structured cell and gene embeddings with state-of-the-art performance. Surprisingly, major biological structure is preserved in native two- and three-dimensional latent spaces, enabling directly interpretable visualization. Perturbation analyses show that SCENE organizes glucocorticoid-response genes and T-cell receptor regulatory programs coherently in gene space, capturing biology beyond cell-type separation. SCENE provides a transparent representation learning framework in which low-dimensional Euclidean geometry supports accurate modeling and biological interpretation.

</details>

---
