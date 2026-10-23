# Paper Scout 日报 2026-10-23

共筛选出 **4** 篇推荐论文。
📊 抓取 arxiv 37/biorxiv 153/pubmed 40 → 粗筛 36 篇 → LLM 选中 4 篇

## 1. Systematic mapping of the prokaryotic noncoding sequence space with a genomic language model

- **期刊**: bioRxiv
- **作者**: Sun, G., Hudelmaier, T., Gilligan, J. C. et al. (13 authors)
- **机构**: Patrick D. Hsu @ Arc Institute; Palo Alto, CA, USA
- **日期**: 2026-10-22
- **ID**: DOI: 10.64898/2026.10.21.760802  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.21.760802v1
- **相关分数**: 8/10
- **一句话推荐**: 使用基因组语言模型对原核非编码序列进行表示学习和大规模聚类，直接命中你的DNA语言模型和生物序列表示学习研究方向。
- **方法**: 基于微调的基因组语言模型提取原核非编码序列嵌入，进行大规模无监督聚类与功能挖掘。
- **主要发现**: 模型成功将数亿原核基因间区序列聚类，通过token熵周期性揭示序列内部架构，并发现了大量新型结构化RNA及变体。
- **对我的启发**: 利用语言模型token熵的周期性分析序列内部架构的思路，可启发对增强子序列内部motif排布特征及padding效应的可解释性分析。

<details><summary>Abstract</summary>

Prokaryotic genomes encode a vast repertoire of noncoding elements such as ribozymes, riboswitches, and CRISPR RNAs. The sequence-level diversity of these intergenic elements precludes alignment-based clustering that would enable annotation and discovery of novel noncoding RNA families. Here, we show that a genomic language model fine-tuned on prokaryotic intergenic sequences learns representations of noncoding elements from DNA sequence. We used these embeddings to organize 376 million intergenic regions from 1.3 terabase pairs of prokaryotic genomes and metagenomes into 5.14 million clusters. This approach nominated 20,149 clusters of putative structured RNAs with a candidate protein partner. Periodicity in token entropies revealed internal architecture, recovering CRISPR, TIGR and VIPR arrays together with their cognate effector proteins from sequence alone. Targeted clustering of bridge recombinase-adjacent sequences identified bridge RNA variants with longer guide recognition sequences than any characterized ortholog. Finally, we directed teams of AI agents to mine the database under researcher-defined criteria, uncovering divergent riboswitches, ribozymes, and other structured RNAs with biological hypotheses for their function. We release a publicly available database that transforms the dark matter of prokaryotic genomes into an explorable resource for human-agent molecular discovery.

</details>

---

## 2. Foundation Models Improve Perturbation Response Prediction

- **期刊**: bioRxiv
- **作者**: Cole, E., Huizing, G.-J., Addagudi, S. et al. (20 authors)
- **机构**: Elijah Cole @ GenBio AI
- **日期**: 2026-10-22
- **ID**: DOI: 10.64898/2026.02.18.706454  |  URL: https://www.biorxiv.org/content/10.64898/2026.02.18.706454v1
- **相关分数**: 8/10
- **一句话推荐**: 系统评估预训练嵌入（含生物基础模型）在单细胞扰动响应预测中的效用，直接命中single-cell perturbation和foundation model研究方向。
- **方法**: 系统性基准测试多种预训练嵌入（含基础模型与先验知识特征）在扰动响应预测中的效用，并开发多嵌入融合方法。
- **主要发现**: 预训练基础模型表现不一，部分优于简单基线，但基于先验知识的嵌入特征表现最佳；整合多种预训练嵌入能进一步提升细胞行为预测的准确性。
- **对我的启发**: 在评估预训练基因组学模型预测增强子活性时，应将基于先验知识的特征（如已知motif或表观图谱）作为强基线对比，并探索多嵌入融合策略以提升预测性能。

<details><summary>Abstract</summary>

Predicting cellular responses to genetic or chemical perturbations is a long-standing goal in biology. Recent applications of foundation models to this task have yielded contradictory results regarding their superiority over simple baselines. We conducted an extensive analysis of the utility of pretrained embeddings (including but not limited to biological foundation models) for perturbation response prediction, covering over 600 embedding-task pairs. While some foundation models fail to outperform simple baselines, others yield consistent improvements. However, the strongest pretrained embeddings are those derived from prior knowledge. We also developed methods for integrating multiple pretrained embeddings to make better predictions. Our results confirm that pretrained embeddings can enable more accurate simulations of cellular behavior.

</details>

---

## 3. Predicting Pre-treatment Resistance or Post-treatment Effect? A Systematic Benchmarking of Single-Cell Drug Response Models

- **期刊**: bioRxiv
- **作者**: Shen, L., Sun, X., Zheng, S. et al. (11 authors)
- **机构**: Jing Tang @ University of Helsinki
- **日期**: 2026-10-22
- **ID**: DOI: 10.64898/2026.04.10.717709  |  URL: https://www.biorxiv.org/content/10.64898/2026.04.10.717709v1
- **相关分数**: 7/10
- **一句话推荐**: 系统基准测试单细胞药物响应预测模型，与single-cell perturbation预测和计算模型评估高度相关。
- **方法**: 基于大规模多癌症单细胞转录组数据及谱系追踪验证标签，对多种单细胞药物响应预测模型进行系统性基准测试与消融分析。
- **主要发现**: 模型在细胞系中表现优于组织样本且无普适最优模型；预处理抗性信号微弱，模型性能受标签定义与架构设计的双重影响。
- **对我的启发**: 其关于标签定义与架构设计交互影响的消融分析思路，可启发我在评估预训练基因组学模型padding策略时，系统考察增强子活性标签阈值与模型架构的交互效应。

<details><summary>Abstract</summary>

Intratumoral heterogeneity drives variable drug responses in cancer. Single-cell RNA sequencing (scRNA-seq) enables characterization of such heterogeneity and prediction of drug response at single-cell resolution. Accordingly, various computational models have been developed to infer drug response from scRNA-seq data. However, their performance, robustness, and generalizability across different biological contexts remain insufficiently evaluated. To address this gap, we benchmarked representative single-cell drug response prediction models using 26 curated datasets comprising over 760,000 cells across 12 cancer types and 21 therapeutic agents. We constructed balanced and imbalanced scenarios to explore model behavior under different label distributions. To address the lack of ground-truth labels in conventional scRNA-seq datasets, we incorporated two lineage-tracing datasets with experimentally validated drug-response annotations, enabling evaluation in a clinically relevant pre-treatment prediction setting. Our results show that prediction performance was markedly higher in cell lines than in tissue samples and varied substantially across datasets, treatment types, and imbalance levels. Under increasing class imbalance, several methods showed reduced performance, and no single method consistently dominated across all evaluation settings. In lineage-tracing datasets, treatment-associated states were more readily distinguished than lineage-defined pre-sensitive and pre-resistant states, while transcriptomic analyses indicated that pre-existing resistance-related signals were detectable but relatively subtle. For scDEAL, which showed competitive performance across several benchmark settings, label-substitution and ablation analyses further indicated that its performance was jointly influenced by training-label definition and architectural design. Application to an independent PDAC organoid dataset showed that scDEAL predictions were associated with treatment-related transcriptional state changes and biological programs. In summary, our study systematically characterizes the performance and limitations of current single-cell drug response prediction approaches across diverse evaluation settings. These results highlight the influence of dataset characteristics, class imbalance, training design, and the strength of resistance-associated signals on model performance, providing a reference for the evaluation and further development of single-cell drug response prediction methods.

</details>

---

## 4. Signature Recontextualization: Mapping perturbational signatures across biological contexts

- **期刊**: bioRxiv
- **作者**: Chen, A. D., Rappaport, N., Schork, N., Girke, T., Monti, S.
- **机构**: Stefano Monti @ Boston University
- **日期**: 2026-10-22
- **ID**: DOI: 10.64898/2026.08.14.744937  |  URL: https://www.biorxiv.org/content/10.64898/2026.08.14.744937v1
- **相关分数**: 6/10
- **一句话推荐**: 定义并系统基准化了跨生物上下文的扰动签名预测任务，与你的单细胞扰动和虚拟细胞研究兴趣直接相关。
- **方法**: 提出跨上下文扰动特征预测的基准测试框架，系统评估投影法、网络传播法与深度学习基础模型在三种目标数据可用性场景下的表现。
- **主要发现**: 投影和网络传播方法在跨上下文特征预测中表现出强灵活性和鲁棒性，在多种情况下优于深度学习基础模型。
- **对我的启发**: 其按目标上下文数据量分阶段评估模型性能的基准设计，启发我在评估预训练基因组学模型预测增强子活性时，可系统性构建不同细胞类型特征覆盖率场景，以更严谨地量化模型鲁棒性及padding策略的影响。

<details><summary>Abstract</summary>

Perturbational transcriptomics is a powerful tool for understanding gene function and drug effects, yet predicting how perturbations manifest across different biological contexts remains a central challenge, limiting translation from model systems to clinically relevant tissues. Despite growing interest in this problem, benchmarking efforts have been hindered by inconsistent evaluation tasks, heterogeneous metrics, and limited assessment across perturbation types and biological systems. Here, we introduce a benchmarking framework for cross-context perturbation-signature prediction (a task we define as signature recontextualization), grounded in explicit definitions of the prediction task, target-data availability, and evaluation metrics centered on signature recovery. The framework evaluates prediction performance across three target-context data regimes: (1) control only, where only control profiles from the target context are measured; (2) low coverage, where a limited subset of perturbations in the target context are measured; and (3) high coverage, where most perturbations in the target context are measured. This design enables systematic assessment of how prediction performance depends on target-context sample size while providing a standardized basis for comparing methods. We evaluate newly developed projection-based (projectCor) and network-based (netProp) methods alongside deep learning-based foundation models (scGPT, STACK) and statistical baselines. The benchmark spans diverse perturbational datasets: CRISPR knockdowns and drug perturbations in cell lines, plus in vivo chemical perturbations in rat tissues from DrugMatrix, extending evaluation beyond isolated cell-line models to tissue-level responses. For each method, evaluation was limited to the datasets, and perturbation types each model supports. Across tasks, projection and network propagation approaches show strong flexibility across perturbation types and biological contexts, and in several cases match or exceed the performance of deep learning and foundation models. We further show that perturbation predictability varies substantially with pathway conservation, transcriptional response strength, and baseline similarity between source and target contexts. All datasets, methods, and evaluation utilities are released as an open-source R package (sigRecon), providing a foundation for reproducible benchmarking and future method development.

</details>

---
