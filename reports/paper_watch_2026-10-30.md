# Paper Scout 日报 2026-10-30

共筛选出 **6** 篇推荐论文。
📊 抓取 biorxiv 120/pubmed 76 → 粗筛 27 篇 → LLM 选中 6 篇

## 1. Scooby-2: fine-tuning AlphaGenome for single-cell genomic track prediction

- **期刊**: bioRxiv
- **作者**: Hingerl, J. C., Gagneur, J.
- **机构**: Johannes C Hingerl @ Technical University of Munich
- **日期**: 2026-10-29
- **ID**: DOI: 10.64898/2026.10.28.762238  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.28.762238v1
- **相关分数**: 9/10
- **一句话推荐**: 将AlphaGenome扩展到单细胞分辨率预测，直接涉及sequence-to-function和细胞类型特异性预测。
- **方法**: 采用参数高效微调（PEFT）策略将AlphaGenome骨干网络与细胞特异性解码器结合，实现单细胞分辨率的序列到功能预测。
- **主要发现**: 该方法在单细胞基因表达差异及eQTL变异效应预测上均显著优于前代Scooby（基于Borzoi），验证了更强预训练骨干网络在单细胞任务中的迁移优势。
- **对我的启发**: 其参数高效微调结合细胞特异性解码器的范式，可借鉴用于在预训练基因组学模型上引入虚拟表观遗传特征，从而预测不同细胞类型的增强子活性。

<details><summary>Abstract</summary>

Sequence-to-function models predict genomic tracks from DNA sequence. AlphaGenome has been shown to outperform previous models, including Borzoi, on most track-prediction and variant-effect benchmarks. However, like its predecessors, it predicts tracks only for predefined, mostly bulk-derived cell types and tissues. While Scooby has extended Borzoi to single-cell resolution, a single-cell adaptation of AlphaGenome is still lacking. We present Scooby-2, which combines AlphaGenome with a cell-specific decoder to predict single-cell RNA-seq coverage and chromatin-accessibility genomic tracks from DNA sequence. The package provides the implementation, the parameter-efficient fine-tuning setup, the training pipeline and inference scripts. When evaluated on the NeurIPS bone marrow single-cell dataset, Scooby-2 achieved a Pearson correlation of 0.56 when predicting cell-type-specific gene expression differences, compared with 0.53 for Scooby. When using the distilled AlphaGenome backbone, variant effect prediction concordance of fine-mapped eQTLs from the OneK1K cohort improved from 0.37 to 0.47 Spearman's rank correlation across all associations, an improvement consistent with that of AlphaGenome over Borzoi itself.

</details>

---

## 2. A multispecies foundation model for genome function prediction, gene annotation and sequence design

- **期刊**: bioRxiv
- **作者**: Boshar, S., Evans, B., Tang, Z. et al. (24 authors)
- **机构**: Thomas Pierrot @ InstaDeep
- **日期**: 2026-10-29
- **ID**: DOI: 10.64898/2025.12.22.695963  |  URL: https://www.biorxiv.org/content/10.64898/2025.12.22.695963v1
- **相关分数**: 9/10
- **一句话推荐**: 提出跨物种基因组基础模型NTv3，用于功能预测和增强子设计，高度契合DNA语言模型和增强子设计兴趣。
- **方法**: 提出Nucleotide Transformer v3 (NTv3)，一种基于长上下文（1Mb）跨物种Transformer的基础模型，结合多物种基因组预训练与多物种功能轨道后训练，并利用离散扩散进行序列设计。
- **主要发现**: 跨物种多基因组预训练结合多物种功能轨道后训练显著提升了功能轨道预测和基因从头预测性能，且该模型表征可通过离散扩散生成具有特定活性和启动子选择性的增强子序列。
- **对我的启发**: NTv3支持1Mb长上下文输入，其处理长序列的机制及多物种功能轨道后训练策略，可为评估预训练模型padding策略对游离型增强子活性预测的影响提供对比基线。

<details><summary>Abstract</summary>

Comparative genomics and synthetic biology require models that can interpret, annotate, and design DNA sequences across species, yet genomic models have not combined these capabilities beyond a few well-characterized organisms. Here we introduce Nucleotide Transformer v3 (NTv3), a long-context cross-kingdom foundation model that provides a common backbone for functional prediction, gene annotation and controllable sequence generation across phylogenetically diverse species. NTv3 is pre-trained on more than 128,000 genomes using sequences up to 1Mb and post-trained on 16,262 functional tracks across 15 animal and plant genomes. NTv3 performs comparably to AlphaGenome on matched human assays and matches or exceeds evaluated published models for functional-track prediction across 19 species spanning mammals, birds, fish, plants, fungi and protists. Ablation experiments show that both genome pre-training and expanding functional supervision from human and mouse to 15 species improve track prediction. Leveraging these learned functional representations, NTv3 outperforms leading ab initio gene predictors across mammals, plants and insects, with fewer spurious gene models and improved recovery and reduced fragmentation of long genes. Finally, the same representations can be used with discrete diffusion to design regulatory DNA sequences with specific activity levels. We demonstrate this in plant and fly promoters and enhancers, and experimentally validate the activity and promoter selectivity of the generated fly enhancers. Together, NTv3 unifies genome interpretation, gene annotation and regulatory sequence design across the animal and plant kingdoms, with direct relevance to agriculture, biodiversity research and biotechnology.

</details>

---

## 3. AlphaGenome Enhances Personal Gene Expression Prediction but Retains Key Limitations

- **期刊**: bioRxiv
- **作者**: Kashyap, S., Ramakrishnan, A., Shen, L.
- **机构**: Li Shen @ Icahn School of Medicine at Mount Sinai
- **日期**: 2026-10-29
- **ID**: DOI: 10.1101/2025.08.05.668750  |  URL: https://www.biorxiv.org/content/10.1101/2025.08.05.668750v1
- **相关分数**: 8/10
- **一句话推荐**: 评估AlphaGenome在个体水平基因表达预测上的性能，直接涉及对预训练基因组基础模型的评估。
- **方法**: 对预训练序列到功能（S2F）模型（AlphaGenome与Enformer）在个体水平基因表达预测任务上进行基准评估，并与传统监督学习模型（弹性网络、随机森林）对比。
- **主要发现**: AlphaGenome在捕获个体特异性表达变异上显著优于Enformer，但其预训练性能仍大幅落后于直接基于个体数据训练的传统机器学习模型。
- **对我的启发**: 提示在利用预训练S2F模型预测特定细胞类型游离型增强子活性时，需警惕其在个体水平上的泛化瓶颈，可考虑将其作为特征提取器并结合下游微调，而非直接端到端预测。

<details><summary>Abstract</summary>

Recent years have seen rapid growth in sequence-to-function (S2F) models that predict diverse molecular readouts from DNA sequence alone. However, these models have faced criticism for their limited accuracy in predicting individual-level gene expression. AlphaGenome, a state-of-the-art S2F model, excels across a range of sequence-based prediction tasks, but its utility for personal expression prediction remains incompletely assessed. Here, we evaluate AlphaGenome's ability to predict tissue-specific, personal gene expression and find that it significantly outperforms its predecessor, Enformer. Across 1,000 genes and 11,471 eligible gene-tissue pairs, AlphaGenome significantly outperforms Enformer for 3,103 pairs, whereas Enformer significantly outperforms AlphaGenome for 828 pairs, yielding a win ratio of 3.75. This imbalance is supported by a global permutation test (P = 2.0e-4), with a median correlation difference of 0.046. Nevertheless, pretrained AlphaGenome substantially underperforms Elastic Net and Random Forest trained on individual-level data. These findings demonstrate that AlphaGenome better captures individual-specific gene expression variation than Enformer, while highlighting substantial room for improvement in sequence-based prediction of personal gene expression.

</details>

---

## 4. MultiFlow: coupled flow matching for predicting single-cell multiomic perturbation responses in unseen cellular contexts

- **期刊**: bioRxiv
- **作者**: Wang, H., Zhang, C., Zhang, M., Nie, X., Liu, Q.
- **机构**: Qiao Liu @ Yale University
- **日期**: 2026-10-28
- **ID**: DOI: 10.64898/2026.08.20.746112  |  URL: https://www.biorxiv.org/content/10.64898/2026.08.20.746112v1
- **相关分数**: 8/10
- **一句话推荐**: 使用耦合流匹配预测单细胞多组学扰动响应，直接涉及单细胞扰动和未见细胞类型泛化。
- **方法**: 提出MultiFlow，一种基于耦合流匹配的生成式框架，通过RNA与ATAC生成流的双向信息交换联合建模配对多组学状态及扰动响应。
- **主要发现**: 联合多组学建模在预测未见细胞类型的转录与染色质可及性扰动响应上优于单模态方法，且有效保留了peak-gene协同效应等跨模态结构。
- **对我的启发**: 其对peak-gene协同效应的跨模态建模思路，可启发在预测不同细胞类型增强子活性时，联合考虑虚拟表观遗传特征与转录组状态的耦合关系。

<details><summary>Abstract</summary>

Predicting cellular responses to perturbation requires resolving coordinated changes across molecular layers, yet most single-cell perturbation models focus on transcriptional responses alone. Here we present MultiFlow, a coupled flow-matching framework that unifies generation and perturbation prediction of paired gene expression and chromatin accessibility. Through bidirectional information exchange between RNA and ATAC generative flows, MultiFlow learns how their joint distribution depends on cellular context and perturbation identity. Across multiomic generation benchmarks, MultiFlow accurately reproduced paired RNA-ATAC states and their population distributions. In multiome perturbation benchmarks, MultiFlow achieved the strongest overall performance in predicting both gene-expression and chromatin-accessibility perturbation responses, outperforming modality-specific perturbation-prediction methods in cell types whose perturbed states were withheld from training. Joint multiomic modeling further preserved perturbation-induced coordination between modalities, including concordant peak-gene effects and cross-modal cellular neighborhood structure. These results establish MultiFlow as a unified generative framework for modeling paired molecular states and predicting their coordinated perturbation responses across cellular contexts. Code and tutorial of MultiFlow are available at https://github.com/liuq-lab/MultiFlow.

</details>

---

## 5. Efficient biological design via genomic in-context learning

- **期刊**: bioRxiv
- **作者**: Brixi, G., Hao, Y. A., Nori, D. et al. (9 authors)
- **机构**: Brian Hie @ Stanford University
- **日期**: 2026-10-29
- **ID**: DOI: 10.64898/2026.10.28.762643  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.28.762643v1
- **相关分数**: 8/10
- **一句话推荐**: 直接涉及基因组语言模型Evo 2的上下文学习能力用于生物序列设计，与我的DNA语言模型和基因组基础模型研究高度相关。
- **方法**: 基于基因组大语言模型（Evo 2）的上下文学习（ICL）与迭代式提示更新（基因组思维链）。
- **主要发现**: 仅需少量示例且无需微调，Evo 2即可生成高质量且多样化的蛋白质和噬菌体基因组，表现超越微调模型，且迭代更新提示能进一步提升设计多样性。
- **对我的启发**: 启发我在增强子活性预测中，可尝试将不同细胞类型的表观遗传特征作为上下文示例输入预训练模型进行少样本预测，并借此评估不同padding策略对长上下文示例建模的影响。

<details><summary>Abstract</summary>

In-context learning (ICL), the ability to perform new tasks from a few examples supplied in a prompt, is a defining emergent capability of large language models. Here, we show that ICL emerges in the genome language model Evo 2 and enables biological design. With as few as four examples in the prompt and no additional training, Evo 2 generates realistic metal-binding proteins, de novo antibodies, protein-RNA systems, and entire bacteriophage genomes. For {Phi}X174-like bacteriophage design, ICL surpasses previously fine-tuned models on computational measures of design quality and diversity. Beyond {Phi}X174, conditioning the model with different phage prompts enables us to efficiently design MS2 and M13 genomes in silico without fine-tuning. Iteratively updating the prompt with newly generated phage genomes, which we refer to as genomic chain-of-thought, further improves the diversity of designs while maintaining quality metrics. Paired with an inference engine that accelerates generation up to 35-fold and extends practicable context to a megabase, these results establish ICL as a versatile and efficient paradigm for biological sequence design.

</details>

---

## 6. Ground-truth evaluation of sparse autoencoder features on spatial, single-cell and language-model embeddings

- **期刊**: bioRxiv
- **作者**: Shahsavand, A., Forghani, S., Akbarzadeh, S., Mahdavi Sabet, F.
- **机构**: Amirhossein Shahsavand @ Hematologic Malignancies Research Center, Research Institute for Oncology, Hematology and Cell Therapy, Tehran University of Medical Sciences, Tehran, Iran
- **日期**: 2026-10-29
- **ID**: DOI: 10.64898/2026.10.27.762296  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.27.762296v1
- **相关分数**: 6/10
- **一句话推荐**: 评估稀疏自编码器在生物基础模型（如Geneformer）嵌入上的特征提取，间接涉及表征学习。
- **方法**: 在多模态基础模型嵌入上，对比稀疏自编码器（SAE）共识拟合与Varimax旋转的特征可重复性及概念覆盖度评估。
- **主要发现**: 单次SAE拟合覆盖概念广但可重复性低，多次拟合的共识特征兼具高可重复性与高纯度，但仍会遗漏弱状态；仅靠可重复性不足以评估特征质量，需结合概念覆盖度和基因程序纯度指标。
- **对我的启发**: 在评估预训练基因组学模型提取的虚拟表观遗传特征时，可采用多次SAE拟合共识策略，并结合特征对已知细胞类型特异增强子概念的覆盖度与纯度，以更严谨地验证特征可靠性。

<details><summary>Abstract</summary>

Sparse autoencoders (SAEs) are increasingly used to extract interpretable features from the embeddings of biological foundation models. Because SAEs trained with different random seeds learn different features, reproducibility across seeds has become a common test of whether these features can be trusted. We asked whether reproducible features are also meaningful, using embeddings whose concepts are known: five spatial transcriptomics embeddings of two colorectal cancer sections and Geneformer embeddings of single-cell RNA profiles, with cell lineages as concepts; synthetic data with planted cell states; and the residual stream of a small language model, with token classes as concepts. Varimax rotations of the same embeddings were almost perfectly reproducible, yet rotation features (PCA, varimax and ICA) covered at most three of seven lineages and three of eight token classes. Single SAE fits showed the opposite profile: they covered most concepts with purer gene programs but reproduced only 27-46% of their features. A consensus over five SAE fits combined the two strengths. It was reproducible (78-98% across sources) and as pure as single fits: 11-40% of its features carried marker genes of another lineage, against 44-70% for varimax. Against the strongest baseline, varimax sparsified to the SAE's sparsity, the consensus covered as many concepts on PCA and Geneformer embeddings and more on learned spatial and text embeddings. The consensus also had costs. It covered fewer lineages than single fits and, like all SAEs, missed weak planted states that rotations recovered; neither a longer single fit nor a second SAE trained on the consensus residual recovered what it discarded. Reproducibility alone therefore ranks features poorly: SAE features should be reported with the number of known concepts they cover and the purity of their gene programs, against a rotation of the same embedding sparsified to the SAE's sparsity.

</details>

---
