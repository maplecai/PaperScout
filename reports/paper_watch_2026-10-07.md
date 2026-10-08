# Paper Scout 日报 2026-10-07

共筛选出 **1** 篇推荐论文。
📊 抓取 arxiv 45/biorxiv 102/pubmed 59 → 粗筛 31 篇 → LLM 选中 1 篇

## 1. Beyond the Transcriptome: Chromatin-Informed Prediction of Cell-State-Dependent Perturbation Responses

- **期刊**: arXiv
- **作者**: Jiafa Ruan, Chenyang He, Ruijie Quan, Fanglei Xue, Zongxin Yang, Yi Yang
- **日期**: 2026-10-06
- **ID**: arXiv: 2610.09054  |  URL: https://arxiv.org/abs/2610.09054
- **相关分数**: 7/10
- **一句话推荐**: 利用染色质可及性信息预测细胞状态依赖的扰动响应，与我的single-cell perturbation研究兴趣直接相关，且涉及跨状态泛化问题。
- **方法**: 提出ChromaPert框架，融合DNA位点先验与配对RNA-ATAC特征，通过染色质引导的响应路由器（CGRR）和条件传输流预测状态依赖的扰动响应。
- **主要发现**: 融合染色质可及性信息显著提升了未见靶点和跨状态的扰动响应预测精度，且正确的多组学配对对恢复染色质相关响应至关重要。
- **对我的启发**: 利用染色质可及性作为细胞上下文先验指导状态特异性预测的思路，可启发在增强子活性预测中引入虚拟表观遗传特征作为细胞类型特异性的条件约束。

<details><summary>Abstract</summary>

Predicting transcriptional responses to genetic perturbations is central to understanding gene function. Existing predictors primarily rely on transcriptomic measurements, although chromatin accessibility provides complementary information about the cellular context in which perturbations act. Using this information requires linking chromatin context to specific perturbations and accounting for baseline differences between independently sampled control and perturbed populations. We propose ChromaPert, a chromatin-informed framework for predicting state-dependent perturbation responses. ChromaPert combines molecular and DNA-informed locus priors with paired control RNA--ATAC features to jointly represent target identity and measured cellular context. Its Chromatin-Guided Response Router (CGRR) builds a source bank of control-derived expression offsets and retrieves relevant sources using perturbation/locus or control-ATAC similarity. These offsets account for baseline differences, while conditional transport flow learns the remaining response. Across three unseen-target and held-out-state settings on K562 CAT-ATAC and Perturb-Multiome, ChromaPert achieves the highest all-gene response correlation among evaluated methods. When transferring known perturbations to held-out states, it improves correlation by 23.2% across all genes and 46.2% for the twenty most responsive genes over the strongest respective baselines. Correct RNA--ATAC pairing improves recovery of chromatin-associated response slopes over shuffled pairing, while cross-state predictions retain state-specific responses to the same perturbation.

</details>

---

> 补发日报：检索窗口 [2026-10-04 00:00, 2026-10-07 00:00) UTC。已排除此前日报及 2026-10-08 邮件中已推荐的论文；粗筛阈值 0.2，相关性至少 6/10。
