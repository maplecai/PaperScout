# Paper Watch 日报 — 2026-09-06

共筛选出 **3** 篇推荐论文。

## 1. [P2] Design and experimental characterization of specificity-switching mutational paths of WW domains

- **作者**: Rehan, A., Mauri, E., Fernandez-De-Cossio-Diaz, J. et al. (7 authors)
- **来源**: biorxiv  |  **日期**: 2026-09-04
- **ID**: DOI: 10.64898/2025.12.08.693000  |  URL: https://www.biorxiv.org/content/10.64898/2025.12.08.693000v1
- **相关性分数**: 4 / 10  |  **优先级**: P2  |  **值得精读**: 是
- **为什么相关**: 使用RBM进行蛋白质序列的表征学习与突变路径设计，与生物序列表征学习间接相关。
- **对我而言的新意**: RBM在蛋白质序列表型景观设计中的应用思路可能对序列模型有启发。

- **核心方法**: 结合受限玻尔兹曼机（RBM）无监督学习与路径采样方法，设计蛋白质特异性转换的突变路径。
- **主要发现**: 基于RBM设计的突变路径中绝大多数中间序列具有功能，而随机顺序突变则丧失功能，凸显了上位性相互作用建模在功能设计中的核心地位。
- **对我研究的启发**: 利用生成模型探索序列功能转换路径的思路，可启发在增强子活性预测中通过设计虚拟表观遗传特征或序列突变的扰动路径，评估预训练模型对非加性调控效应的捕捉能力。

<details><summary>Abstract (原文)</summary>

Specific interactions between proteins and other biomolecules are ubiquitous in cellular processes.How specificity is encoded in the protein sequence and can be modified through a minimal set of concerted mutations is a complex issue. In this work, we focus on the WW protein domain, whose variants specifically bind to different classes of proline-rich peptides. Combining unsupervised learning of homologous WW sequence data with Restricted Boltzmann Machines (RBM) and path-sampling methods, we design mutational paths of putative WW domains interpolating between two natural WW domains with either distinct or similar specificities. Sequences along the designed paths are then experimentally validated with high-throughput in-vitro binding assays against 3 peptides of different classes. The vast majority (93%) of intermediate sequences along the designed paths are responsive to the initial or/and final peptides. On the contrary, domains along scrambled paths, in which the same mutations are introduced in random order are not functional, emphasizing how successful design crucially depends on the ability to model epistatic interactions. Switch in specificity between classes I and IV, whose representative peptides bind to different pockets on the WW domain takes place through intermediates displaying some level of binding cross-reactivity with the tested peptides, contrary to the transition from class I to II, which are associated with the same binding pocket. Lastly, we show that the RBM paths share a high identity with internal nodes obtained from ancestral sequence reconstruction based on the seed WW domains.

</details>

---

## 2. [P2] Adding layers of information to scRNA-seq data using pre-trained language models

- **作者**: Krissmer, S. M., Menger, J., Rollin, J. et al. (6 authors)
- **来源**: biorxiv  |  **日期**: 2026-09-04
- **ID**: DOI: 10.1101/2025.08.23.671699  |  URL: https://www.biorxiv.org/content/10.1101/2025.08.23.671699v1
- **相关性分数**: 4 / 10  |  **优先级**: P2  |  **值得精读**: 是
- **为什么相关**: 使用预训练语言模型（文本）增强scRNA-seq数据，虽非DNA语言模型但涉及单细胞与预训练模型结合的范式。
- **对我而言的新意**: 将外部知识库与单细胞数据对齐的思路可能对虚拟细胞模型构建有参考价值。

- **核心方法**: 微调轻量级encoder-only生物医学语言模型，将scRNA-seq数据与文献文本对齐以学习共享表示。
- **主要发现**: 该方法在保留细胞身份的同时，为单细胞数据注入了稳健且可解释的功能、疾病及发育上下文信息。
- **对我研究的启发**: 无明显直接启发

<details><summary>Abstract (原文)</summary>

Pre-trained language models promise to enrich single-cell analyses with contextual information from large biomedical text corpora, but it remains unclear how to optimally align this knowledge with quantitative scRNA-seq data. To address this, we construct text-based training datasets from both scRNA-seq data and biomedical literature targeted to the experimental setting at hand. We then fine-tune lightweight encoder-only biomedical language models to learn a shared, literature-enriched representation. Controlled evaluations across immune and developmental datasets show that this representation preserves cell identity while adding robust and interpretable contextual layers of functional, disease-associated, and developmental information to single-cell analysis workflows.

</details>

---

## 3. [P2] RNA plasticity emerges as an evolutionary response to fluctuating environments

- **作者**: Garcia-Galindo, P., Ahnert, S. E.
- **来源**: biorxiv  |  **日期**: 2026-09-04
- **ID**: DOI: 10.1101/2024.10.02.614758  |  URL: https://www.biorxiv.org/content/10.1101/2024.10.02.614758v1
- **相关性分数**: 4 / 10  |  **优先级**: P2  |  **值得精读**: 是
- **为什么相关**: 使用计算 genotype-phenotype map 建模RNA序列到二级结构的功能映射，与sequence-to-function概念有间接关联。
- **对我而言的新意**: RNA序列可塑性进化模拟的思路可能对理解序列-功能映射的鲁棒性有启发。

- **核心方法**: 基于RNA二级结构的基因型-表型映射与玻尔兹曼分布，进行周期性环境切换的进化模拟。
- **主要发现**: RNA在环境波动下能进化出最优表型可塑性，表现为不同环境下的最优二级结构具有近等概率的玻尔兹曼分布，且自然功能RNA亦具备此特征。
- **对我研究的启发**: 无明显直接启发

<details><summary>Abstract (原文)</summary>

Phenotypic plasticity refers to the ability of a single genotype to produce multiple distinct phenotypes. Using the computationally tractable genotype-phenotype (GP) map of RNA secondary structures, we model RNA phenotypic plasticity using the Boltzmann distribution of secondary structures for each genotype. Through evolutionary simulations that involve periodic environmental switching on the GP map, we reveal that RNA phenotypes can adapt to these fluctuations towards an optimal plasticity. The optimal phenotypes exhibit dominant near-equal Boltzmann probabilities of distinct structures, each representing the fittest structure for each alternating environment. Our findings demonstrate that phenotypic plasticity, a widespread biological phenomenon, is a fundamental evolutionary response to changing environments for RNA secondary structure. We also find naturally evolved functional RNAs that exhibit optimal plasticity unlikely to arise by neutral drift alone, suggesting functional relevance in fluctuating environments.

</details>

---
