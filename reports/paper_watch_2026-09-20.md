# Paper Scout 日报 2026-09-20

共筛选出 **1** 篇推荐论文。
📊 抓取 biorxiv 93/pubmed 44 → 粗筛 16 篇 → LLM 选中 1 篇

## 1. A diffusion model of viral evolution predicts mutation fitness and evolutionary trajectories

- **期刊**: bioRxiv
- **作者**: Wu, J., Ding, X., Wu, A.
- **机构**: Aiping Wu @ Suzhou Institute of Systems Medicine, Chinese Academy of Medical Sciences & Peking Union Medical College
- **日期**: 2026-09-18
- **ID**: DOI: 10.64898/2026.09.16.752245  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.16.752245v1
- **相关分数**: 4/10
- **一句话推荐**: 基于扩散模型的病毒蛋白序列进化预测，属于sequence-to-function和生物序列表征学习的范畴，但非基因组DNA层面。
- **方法**: 基于蛋白质序列训练的扩散模型，利用前向加噪模拟随机突变、反向去噪模拟自然选择，通过计算突变序列相对于野生型的重建难度来评估适应度。
- **主要发现**: 仅依赖序列数据训练的扩散模型即可高精度预测病毒突变适应度与进化轨迹，在免疫逃逸预测上误差大幅降低，并成功前瞻性预警了H1N1后续流行株及H5禽流感的受体结合演化趋势。
- **对我的启发**: 可借鉴该模型将序列功能预测转化为'重建难度评估'的范式，探索在增强子活性预测中，通过计算游离型增强子序列在预训练基因组学模型中的去噪/重建误差来表征其表观遗传活性强度。

<details><summary>Abstract</summary>

Viral evolution arises from random mutations and natural selection, yet computational approaches rarely model these two forces in a unified way. We present Viral Evolution Simulator (VES), a diffusion model-based framework that mirrors this duality by design: forward noise injection simulates stochastic mutation, and reverse denoising recapitulates selective filtering. Trained solely on viral protein sequences, VES predicts mutational fitness without functional data, measuring fitness as the reconstruction difficulty of a mutated sequence relative to its wild-type counterpart. Across immune escape, receptor binding, and deep mutational scanning datasets, VES outperforms state-of-the-art generative models, achieving a 31.78% error reduction over the best baseline in immune escape mutation fitting evaluation. When trained on sequences collected before June 2024 and evaluated against H1N1 strains that later emerged, VES assigned high scores to 16 of 20 mutations that subsequently showed the sharpest frequency shifts. Extending to avian influenza H5, the framework reveals a dynamic interplay between antigenic escape and human-type receptor binding. Both functions dropped sharply in 2021, followed by a sustained rise in receptor affinity that could connect to recent epidemiological trends. VES offers a generalizable, sequence-only foundation for tracing evolutionary trajectories and prioritizing mutations for surveillance and experimental validation, pointing toward where functional efforts might matter most.

</details>

---
