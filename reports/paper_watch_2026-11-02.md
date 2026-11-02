# Paper Scout 日报 2026-11-02

共筛选出 **4** 篇推荐论文。
📊 抓取 biorxiv 106/pubmed 214 → 粗筛 65 篇 → LLM 选中 4 篇

## 1. Cross-modal transfer enables zero-shot prediction of drug responses across cell types

- **期刊**: bioRxiv
- **作者**: Luo, C., Hu, M., Wu, Y., Guo, D., Wang, S., Lyu, Q. R., Liu, X.
- **机构**: Xiao Liu @ Tsinghua University
- **日期**: 2026-11-01
- **ID**: DOI: 10.64898/2026.10.27.762107  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.27.762107v1
- **相关分数**: 8/10
- **一句话推荐**: 跨模态和跨细胞类型的零样本扰动预测，与单细胞扰动和虚拟细胞概念高度契合。
- **方法**: 基于跨模态迁移学习（遗传扰动到化学扰动）与跨上下文预测的零样本药物转录反应推断框架。
- **主要发现**: 利用遗传与化学扰动共享的调控网络，该框架在无目标细胞药物测量数据下显著提升了药物转录反应预测的准确性和方向性一致性，并成功揭示了跨细胞上下文的药理特征与供体间差异。
- **对我的启发**: 跨模态迁移学习范式可启发利用易获取的虚拟表观遗传特征或遗传扰动数据，零样本预测不同细胞类型中难以直接测量的游离型增强子活性。

<details><summary>Abstract</summary>

Genetic perturbation responses capture the functional consequences of gene-level interventions, providing functional information for drug-response prediction beyond baseline gene expression. Within the same cellular context, genetic and chemical perturbations engage shared regulatory networks, providing a biological basis for transferring response information between perturbation modalities. Here we introduce GRAFT, a framework that combines genetic-to-chemical transfer with cross-context prediction to infer drug-induced transcriptional responses without drug measurements in the target context. Across benchmarked LINCS and external contexts, GRAFT improved response correlation, directional agreement and magnitude reconstruction over competing methods, particularly for drugs with context-dependent responses. GRAFT-Adapt further refines predictions of unmeasured responses using a small number of drug measurements from the target context. GRAFT-Atlas spans 13 cellular contexts and 7,856 drug catalog entries, comprising 102,128 predictions for drug-context combinations. The atlas captured recognizable pharmacological neighborhoods, shared functional programs, context-dependent transcriptional changes and structural-functional associations supported by molecular docking. Across ten iPSC lines from distinct donors, GRAFT identified candidate inter-donor differences, with functional support for selected candidates from measured genetic perturbation responses. Together, GRAFT enables perturbation-informed prediction and comparison of drug responses across cellular contexts.

</details>

---

## 2. Single-cell perturbation prediction near experimental reproducibility with GENESIS

- **期刊**: bioRxiv
- **作者**: Conci, R., D'Ascenzo, D., Cultrera di Montesano, S., Raghavan, S., Winter, P. S., Van Allen, E. M., Crawford, L., Lotter, W.
- **机构**: Sebastiano Cultrera di Montesano @ Untoken
- **日期**: 2026-11-01
- **ID**: DOI: 10.64898/2026.10.30.763081  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.30.763081v1
- **相关分数**: 8/10
- **一句话推荐**: 生成式模型预测单细胞扰动响应分布，直接属于单细胞扰动预测的研究兴趣。
- **方法**: 提出GENESIS，一种基于能量分数训练的轻量级生成式神经网络，直接从实验协变量预测单细胞扰动响应分布。
- **主要发现**: 该模型在预测单细胞扰动响应时接近实验重现性；且在同等训练预算下，覆盖更多实验条件的广度采样比深度采样能带来更准确的预测。
- **对我的启发**: 在构建虚拟表观遗传特征或采样训练数据时，应优先覆盖更多细胞类型和扰动条件（广度优先），而非对少数类型进行高深度测序，以提升增强子活性预测模型的泛化能力。

<details><summary>Abstract</summary>

Single-cell perturbation atlases now measure cellular responses across millions of cells, but the number of possible combinations of biological contexts, perturbations, doses and other experimental variables make exhaustive measurements infeasible. Here, we present GENESIS (Generative ENErgy-based Single-cell Intervention Simulator), a generative framework that predicts single-cell response distributions directly from the covariates defining an experimental condition. GENESIS uses a lightweight neural network trained with the energy score, a strictly proper scoring rule for distributions. We introduce an experiment-calibrated evaluation framework in which prediction error is interpreted relative to the reproducibility of repeated measurements of the same condition. Across the Tahoe-100M small-molecule atlas and a large PBMC cytokine atlas, GENESIS significantly outperforms existing generative models and statistical baselines and approaches experimental reproducibility on independently repeated conditions. Importantly, GENESIS remains accurate when trained on only a fraction of the available experimental conditions or cells, and generated profiles recover experimentally observed context-dependent transcriptional programs. At comparable training-cell budgets, GENESIS achieves more accurate predictions when measurements span more experimental conditions rather than profiling fewer conditions more deeply. Together, these findings suggest a complementary strategy for perturbation studies: broader, lower-depth measurements can expand experimental coverage, while GENESIS augments sparsely sampled populations and predicts responses in unmeasured conditions.

</details>

---

## 3. LIMBER: A Hybrid RNA Foundation Model for Predicting and Understanding RNA Structure and Function

- **期刊**: bioRxiv
- **作者**: Wang, Z., Qiu, Y., He, Y., Thompson, I., Wang, H., Porter, A., Li, A.
- **机构**: Yunrui Qiu @ University of Notre Dame
- **日期**: 2026-11-01
- **ID**: DOI: 10.64898/2026.10.28.762670  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.28.762670v1
- **相关分数**: 8/10
- **一句话推荐**: RNA基础模型，涉及序列到结构/功能预测及表征学习，与基因组基础模型研究高度相关。
- **方法**: 结合双向自注意力与选择性状态空间模型（Mamba）的混合RNA基础模型，并建立任务无关的内部表征评估框架。
- **主要发现**: 该模型在多项RNA结构与功能任务上表现领先，且模型不同层级展现出分层、任务依赖的生物学信息组织，结构、进化和功能能力呈现不同的缩放行为。
- **对我的启发**: 其任务无关的内部表征评估框架及层级信息组织分析，可借鉴用于探究预训练基因组学模型不同层级对虚拟表观遗传特征及增强子活性表征能力的差异。

<details><summary>Abstract</summary>

RNA foundation models offer a promising route to decoding the relationships between RNA sequence, structure and function, yet how model shapes the acquisition and organization of biological information remains poorly understood. Here we introduce Layer-Interleaved Mamba-Bidirectional Encoder for RNA (LIMBER), a hybrid foundation model integrating bidirectional self-attention with selective state-space modeling, pretrained on 40.5 million non-coding RNA sequences. Through task-specific fine-tuning, LIMBER achieves leading performance on secondary-structure prediction and non-coding RNA classification benchmarks, while demonstrating strong transferability to translation-related tasks and RNA--small-molecule interaction prediction. Beyond model development, we establish a unified, task-agnostic framework to systematically evaluate and interpret the biological knowledge intrinsically acquired by RNA foundation models. This framework validates LIMBER's strong capabilities in recovering RNA structures and predicting mutational effects, while uncovering a hierarchical, task-dependent organization of different biological information across model layers. By further systematically training and evaluating a broad panel of model variants spanning model capacity, training duration and dataset size, we uncover distinct scaling behaviors across structural, evolutionary and functional capabilities. Together, these findings establish LIMBER as a versatile RNA foundation model and provide broader insights into how architectural design, internal representations and scaling shape the learning of RNA sequence-structure-function relationships.

</details>

---

## 4. Gene Embedding Hub: a standardized resource for human gene representations

- **期刊**: bioRxiv
- **作者**: Tabares, D., Bohl, M., Boeva, V.
- **机构**: Valentina Boeva @ ETH Zurich
- **日期**: 2026-11-01
- **ID**: DOI: 10.64898/2026.10.29.762818  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.29.762818v1
- **相关分数**: 6/10
- **一句话推荐**: 提供标准化的基因表征资源，涉及多模态和调控基因组学嵌入，对表征学习有参考价值。
- **方法**: 整合多模态生物数据构建标准化人类基因嵌入资源库，并基于跨嵌入相似性与可预测性进行系统评估。
- **主要发现**: 汇集了67个涵盖序列、表达、网络等多模态的基因嵌入集，通过统一标识符与元数据格式解决了标准化缺失问题，促进了跨模态基因表示比较与下游应用。
- **对我的启发**: 该资源库提供的标准化DNA/RNA及调控基因组学嵌入，可作为评估预训练基因组学模型不同padding策略对增强子活性预测任务影响的特征基线或对比基准。

<details><summary>Abstract</summary>

Gene embeddings are vector representations of gene identity that provide machine-learning models with information from diverse biological sources. However, their use is hindered by a lack of standardization: inconsistent identifiers, formats, and preprocessing conventions. In this work, we present a unified resource of 67 human gene-embedding sets derived from protein, DNA and RNA sequences, biomedical text, bulk expression data, single-cell expression models, functional data, biological networks, knowledge graphs, regulatory genomics and multimodal models, covering up to 20,097 GENCODE-annotated protein-coding genes. The collection includes both published precomputed embeddings and representations generated or extracted from publicly available models and biological data. Each embedding set is organized in a folder containing the embedding matrix, the Ensembl gene identifiers, machine-readable metadata, and processing documentation. We validate the resource by measuring global and local similarity, cross-embedding consensus, and cross-embedding predictability. The collection is designed to allow community-contributed embeddings that meet predefined technical and documentation requirements, enables comparison of gene representations across modalities and provides standardized embeddings for training and downstream applications.

</details>

---
