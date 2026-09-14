# Paper Scout 日报 2026-09-14

共筛选出 **2** 篇推荐论文。
📊 抓取 biorxiv 448/pubmed 28 → 粗筛 100 篇 → LLM 选中 2 篇

## 1. Massively parallel characterization reveals context-dependent and non-additive regulatory effects of closely spaced variant pairs

- **期刊**: bioRxiv
- **作者**: Kreevan, R., Pankratov, V., Yermakovich, D. et al. (9 authors)
- **机构**: Rita Kreevan @ Institute of Genomics, University of Tartu
- **日期**: 2026-09-11
- **ID**: DOI: 10.64898/2026.09.10.750584  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.10.750584v1
- **一句话推荐**: 通过MPRA大规模表征增强子中近距离变异对的非加性调控效应，直接关系到增强子活性预测和变异效应建模。
- **方法**: 基于大规模并行报告分析（MPRA）测定邻近变异对的四种单倍型调控活性，并量化评估其非加性效应与上下文依赖性。
- **主要发现**: 增强子内邻近变异的调控效应具有高度的上下文依赖性且多呈非加性，双突变联合效应常低于加性预期，且非加性变异对的物理距离显著更近。
- **对我的启发**: 在构建序列到功能的增强子活性预测模型时，需关注局部多态位点的非加性交互特征，这提示模型在局部序列特征提取或padding处理时，必须保留邻近碱基的联合依赖关系而非孤立看待变异。

<details><summary>Abstract</summary>

Precise control of gene expression relies in part on cis-regulatory elements (CREs), including enhancers. Genetic variation within enhancers can alter their regulatory activity and contribute to variation in gene expression, yet the effects of multiple nearby variants within the same enhancer remain poorly understood. To address this, we designed a massively parallel reporter assay (MPRA) to test the regulatory effect of 7,285 pairs of close-proximity single-nucleotide variants (SNVs) selected from blood-specific and broadly active enhancers. To enrich for functionality, we required at least one variant in each pair to be annotated as an eQTL in eQTLGen dataset. We measured the regulatory activity of all four haplotypes in K562 leukemia cells, where 57% of tested variant pairs had at least one derived haplotype that differed significantly in activity from the ancestral haplotype. The effects of individual variants frequently depended on the allelic background provided by the neighboring variant, with some variants showing opposite effects in different allelic backgrounds. Among a smaller, high-confidence subset selected for analysis of additivity, 59% (105/178) of variant pairs showed non-additive effects, and non-additive pairs were located closer together than additive pairs. Among pairs in which both single-derived haplotypes increased activity, the double-derived haplotype generally showed a smaller effect than expected under additivity. Together, our results demonstrate that nearby variants within the same enhancer can jointly shape regulatory activity and highlight the importance of considering local allelic context when interpreting the functional effects of regulatory variation.

</details>

---

## 2. OmniTCR: a foundation model unifying T cell receptor recognition prediction and conditional sequence generation

- **期刊**: bioRxiv
- **作者**: Zeng, F., Feng, D., Song, D., Ding, L., Tan, Z., Lei, Q., Lei, W., Guo, A.-Y.
- **机构**: An-Yuan Guo @ West China Biomedical Big Data Center, West China Hospital, Sichuan University
- **日期**: 2026-09-13
- **ID**: DOI: 10.64898/2026.09.10.750588  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.10.750588v1
- **一句话推荐**: 属于生物序列的基础模型，涉及序列表示学习与生成，与你的DNA语言模型研究有间接思路借鉴。
- **方法**: 提出一种基于序列类型token和互补组件顺序的自回归基础模型，统一处理异构免疫序列数据进行预训练。
- **主要发现**: 该模型在未见表位的TCR识别预测和泛癌repertoire分类上显著超越现有方法，并在条件序列生成任务中达到最高序列恢复率。
- **对我的启发**: 引入特定类型token统一异构数据联合学习的范式，可借鉴于整合不同细胞类型的增强子序列与虚拟表观遗传特征，以提升多模态基因组学预训练模型的表征能力。

<details><summary>Abstract</summary>

T cell receptor (TCR) recognition prediction and receptor generation are traditionally modelled separately, leaving vast TCR sequence collections disconnected from smaller TCR-peptide-MHC datasets. Here we present OmniTCR, a 113-million-parameter autoregressive foundation model pretrained on 328 million formatted human immune-sequence records. Sequence-type tokens and complementary component orders enable joint learning from individual TCR chains and partial or complete TCR-pMHC associations. On unseen epitopes, OmniTCR achieved AUPRCs of 0.7009 for peptide-TCR{beta}; recognition and 0.8235 for TCR-pMHC interaction prediction, exceeding the strongest evaluated comparators by 0.3396 and 0.3451, respectively. It distinguishes cancer from healthy repertoires across 11 independent pan-cancer cohorts (mean AUROC, 0.9436). The model achieved the highest sequence recovery on internal and external generation benchmarks. Structural modelling supported the plausibility of selected pMHC-conditioned CDR3{beta}; candidates. OmniTCR bridges heterogeneous immune sequence data, providing a foundation for computational immunology and receptor design.

</details>

---
