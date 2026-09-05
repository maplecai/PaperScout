# Paper Watch 日报 — 2026-09-05

共筛选出 **2** 篇推荐论文。

## 1. [P1] AnnFlux: object-conditioned neural stochastic differential equations for single-cell perturbation dynamics

- **作者**: Choi, H., Byeon, G., Park, H. et al. (6 authors)
- **来源**: biorxiv  |  **日期**: 2026-09-03
- **ID**: DOI: 10.64898/2026.09.01.748703  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.01.748703v1
- **相关性分数**: 8 / 10  |  **优先级**: P1  |  **值得精读**: 是
- **为什么相关**: 提出基于神经SDE的单细胞扰动动态建模方法，直接契合用户关注的单细胞扰动响应建模方向。
- **对我而言的新意**: 将扰动建模为潜在空间中的连续漂移轨迹，并预测未见过的扰动组合，思路新颖。

- **核心方法**: 提出对象条件的神经随机微分方程（AnnFlux），在潜在细胞状态空间中学习扰动驱动的漂移场以建模单细胞动力学。
- **主要发现**: 该模型能准确插值未见时间点并预测未见扰动及其组合，提升了分布保真度，且预测的IFN特征在独立空间图谱中得到生物学验证。
- **对我研究的启发**: 无明显直接启发

<details><summary>Abstract (原文)</summary>

Single-cell perturbation profiling measures responses to genetic and chemical interventions, yet most models learn a static map, ignoring how populations move over time and how perturbations combine. AnnFlux, an object-conditioned stochastic differential equation, learns a drift field in latent cell-state space. Conditioning on the perturbing object makes the field queryable one object at a time, yielding per-object drifts comparable across genes and drugs. By learning a drift field tailored to each perturbation context, it interpolates a held-out timepoint in an epithelial-mesenchymal transition time course and predicts unseen perturbations. Beyond point estimates, AnnFlux improves distributional fidelity and predicts responses to held-out perturbation combinations. An IFN-response signature predicted by AnnFlux was associated with TLS proximity in an independent pan-cancer spatial atlas. This framework maps perturbation-driven cell-state evolution as continuous trajectories and represents unseen perturbations using prior-knowledge embeddings.

</details>

---

## 2. [P2] De novo designed single-domain antibodies protect against lethal cobra venom neurotoxicity in vivo

- **作者**: Overath, M. D., Lundquist, E. V. S., Björnsson, K. H. et al. (12 authors)
- **来源**: biorxiv  |  **日期**: 2026-09-03
- **ID**: DOI: 10.64898/2026.09.01.748349  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.01.748349v1
- **相关性分数**: 4 / 10  |  **优先级**: P2  |  **值得精读**: 是
- **为什么相关**: 使用生成式模型进行蛋白质从头设计，虽非基因组学但属于生物序列表征与设计范畴，有一定参考价值。
- **对我而言的新意**: 蛋白质生成模型的标准化评估与实验验证流程可能对序列设计模型有启发。

- **核心方法**: 基于生成式AI模型（Germinal等）从头设计单域抗体（VHHs）并结合AlphaFold3结构评估与体内外实验验证。
- **主要发现**: Germinal模型在生成高亲和力及体内中和蛇毒神经毒素的单域抗体方面表现最优，其设计的两个候选抗体在小鼠体内实现了100%存活保护。
- **对我研究的启发**: 无明显直接启发

<details><summary>Abstract (原文)</summary>

Generative protein design can now rapidly produce de novo binders with high affinity and functional activity against a wide range of targets, including lethal snake venom toxins. However, so far most reported successes rely on new-to-nature scaffolds with limited therapeutic precedent. Single-domain antibodies (VHHs) offer a clinically validated alternative scaffold that can bind and neutralize long-chain -neurotoxins, which are some of the most lethal components in snake venoms. Here we compare three recently established de novo design models with VHH-design capabilities (Germinal, RFantibody, and BoltzGen) for their ability to generate VHHs against the neurotoxin -cobratoxin from the monocled cobra (Naja kaouthia). Using standardized model inputs and evaluation criteria based on AlphaFold3 interface confidence (ipTM) and RMSD self-consistency, we find that Germinal was the only method to generate designs passing stringent in silico criteria for experimental testing. We therefore performed a larger Germinal design campaign employing three different VHH frameworks and experimentally validated 46 designs in vitro. Of these, 42 expressed as soluble proteins and we identified four binding hits derived from two of the three tested frameworks. Of the four binders, two lead candidates were further characterized and demonstrated high affinity (KDs of 4.1 nM and 10.8 nM), monomeric behavior and low polyreactivity, indicating favorable biophysical and developability properties, as well as functional toxin neutralization in vitro. To assess their therapeutic potential we investigated their ability to protect against -cobratoxin toxicity in vivo. Both candidates fully protected mice after -cobratoxin challenge, with 100% survival compared to a lethal control. One candidate also retained notable neutralization capacity against whole venom of Naja kaouthia with a survival of 56%, while the other protected 22% when tested in a rescue setting. Together, we demonstrate that de novo VHH design can generate high affinity single-domain antibodies with in vivo protection against lethal cobra venom neurotoxicity, and provide practical insights into method- and framework-dependent performance.

</details>

---
