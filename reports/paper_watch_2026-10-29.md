# Paper Scout 日报 2026-10-29

共筛选出 **2** 篇推荐论文。
📊 抓取 biorxiv 127/pubmed 61 → 粗筛 17 篇 → LLM 选中 2 篇

## 1. Creator 1.0: Phylogeny-Guided Stagewise Pretraining for Plant Genome Foundation Models across 1,000 Species

- **期刊**: bioRxiv
- **作者**: Yang, L., Jiang, S., Li, Y. et al. (10 authors)
- **机构**: Zhiqiang Xia @ Hainan University
- **日期**: 2026-10-28
- **ID**: DOI: 10.64898/2026.10.22.761197  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.22.761197v1
- **相关分数**: 7/10
- **一句话推荐**: 植物基因组基础模型，采用系统发育引导的分阶段预训练，与基因组基础模型和DNA语言模型研究直接相关。
- **方法**: 采用系统发育引导的分阶段预训练（PGSP）范式构建植物基因组基础模型，并在不同训练阶段保留检查点。
- **主要发现**: 不同下游任务及数据量场景（如全量、少样本）下的最优模型表现分散在预训练的不同阶段检查点中，最终阶段模型并非普遍最优。
- **对我的启发**: 在评估预训练基因组学模型对增强子活性预测的表现时，除 padding 影响外，可系统考察不同预训练阶段检查点的表征差异，以寻找特定细胞类型虚拟表观遗传特征的最优适配点。

<details><summary>Abstract</summary>

Genomic language models have advanced DNA sequence analysis, but their applicability to plant-specific tasks and representation changes during pretraining remain poorly characterized. Here, we present Creator 1.0, a 2-billion-parameter parameter plant genome foundation model pretrained on 1,000 plant genomes using phylogeny-guided stagewise pretraining (PGSP). Training comprised 83 consecutive stages and produced 52 cumulative checkpoints associated with distinct plant orders. On GENEB, the stage 83 checkpoint ranked first among 46 models across 10 plant-related tasks, with a mean Matthews correlation coefficient (MCC) of 0.565, and fourth across all 100 tasks. Evaluation of 52 checkpoints on six plant lncRNA tasks identified different optimal stages under full-data, 10-shot and 1-shot settings, corresponding to stages 71, 72 and 29, respectively. Checkpoint performance varied across tasks, without consistent advantages for corresponding plant orders. These findings demonstrate the competitive performance of Creator 1.0 and highlight the potential of PGSP to provide task-adaptable checkpoints for plant genomic applications.

</details>

---

## 2. Oyster: A Neural Network for Modeling Genomic Sequences with Exact Position-Specific k-mer Contributions

- **期刊**: bioRxiv
- **作者**: Abdulnabi, H., Westwood, J. T.
- **机构**: Husam Abdulnabi @ University of Toronto Mississauga
- **日期**: 2026-10-28
- **ID**: DOI: 10.1101/2025.11.01.686014  |  URL: https://www.biorxiv.org/content/10.1101/2025.11.01.686014v1
- **相关分数**: 6/10
- **一句话推荐**: 提出一种可解释的k-mer位置贡献基因组序列建模方法，与sequence-to-function和表示学习有一定关联。
- **方法**: 提出一种忽略k-mer关联、仅学习k-mer组成与位置的玻璃盒神经网络，通过权重直接提取k-mer的精确位置特异性贡献。
- **主要发现**: 该白盒模型在蛋白质-DNA互作和增强子活性预测中性能略逊于黑盒模型，但预测结果高度一致，且能提取出与文献相符及具有新意的可解释生物学概念。
- **对我的启发**: 可利用该白盒模型精确解析序列位置特异性贡献的特性，量化评估预训练基因组学模型中padding操作引入的位置偏差对增强子活性预测的影响。

<details><summary>Abstract</summary>

Genomics data are sequences, and exploration in these data involves mapping these sequences to function and understanding that mapping. Analogous to a sentence composed of words, a sequence's function is understood through its constituent subsequences, or k-mers. The presence of k-mers, their positions, and their relationships with other k-mers (k-mer associations) all affect sequence function. Understanding the sequence function requires determining the contributions of each of its k-mers and the impacts of their positions and k-mer associations. k-mer associations are inherently combinatorial and may be hierarchical. Although these associations may be impactful for biological phenomena, k-mer associations cannot be understood by humans and severely obfuscate model analyses, yielding generalizations, simplifications, and approximations. Ignoring k-mer associations, however, yields concepts that are human-understandable and exact. To determine whether ignoring k-mer associations is appropriate, models that learn or ignore k-mer associations can be compared. Oyster is a novel NN that learns k-mer composition and k-mer positions while ignoring k-mer associations, the first with these abilities to our knowledge. Oyster is a glass-box model as the exact position-specific contributions of k-mers are directly extracted from the model weights. Oyster is compared with models that consider k-mer associations using two case studies spanning two important genomics topics: protein-DNA interactions and enhancer activity. Across these case studies it was found that while models that consider k-mer associations perform better than Oyster models, the predictions of the Oyster models were in strong agreement, serving as faithful proxies. Human-understandable concepts were extracted from the Oyster models revealing concepts that align with the literature as well as novel ones.

</details>

---
