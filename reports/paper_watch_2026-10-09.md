# Paper Scout 日报 2026-10-09

共筛选出 **2** 篇推荐论文。
📊 抓取 biorxiv 136/pubmed 72 → 粗筛 37 篇 → LLM 选中 2 篇

## 1. Latent causal diffusions for single-cell perturbation modeling.

- **期刊**: Proceedings of the National Academy of Sciences of the United States of America
- **作者**: Lars Lorch, Jiaqi Zhang, Charlotte Bunne, Andreas Krause, Bernhard Schölkopf, Caroline Uhler
- **机构**: Caroline Uhler @ Laboratory for Information and Decision Systems, Massachusetts Institute of Technology (MIT), Cambridge, MA 02139.
- **日期**: 2026-10-08
- **ID**: DOI: 10.1073/pnas.2602630123  |  PMID: 42848419  |  URL: https://pubmed.ncbi.nlm.nih.gov/42848419/
- **相关分数**: 8/10
- **一句话推荐**: 提出潜在因果扩散模型用于单细胞扰动建模，与虚拟细胞和单细胞扰动预测高度相关。
- **方法**: 提出潜在因果扩散模型（LCD），将单细胞基因表达建模为带测量噪声的平稳扩散过程，并结合因果线性化方法（CLIPR）推断基因间的直接因果效应。
- **主要发现**: LCD在预测未见扰动组合的转录组分布偏移上优于现有方法，且CLIPR能在线性漂移假设下有效恢复基因因果结构并聚类出功能模块。
- **对我的启发**: 无明显直接启发

<details><summary>Abstract</summary>

Perturbation screens hold the potential to systematically map regulatory processes at single-cell resolution, yet modeling and predicting transcriptome-wide responses to perturbations remains a major computational challenge. Existing methods often underperform simple baselines, fail to disentangle measurement noise from biological signal, and provide limited insight into the causal structure governing cellular responses. Here, we present the latent causal diffusion (LCD), a generative model that frames single-cell gene expression as a stationary diffusion process observed under measurement noise. LCD outperforms established approaches in predicting the distributional shifts of unseen perturbation combinations in single-cell RNA-sequencing screens while simultaneously learning a mechanistic dynamical system of gene regulation. To interpret these learned dynamics, we develop an approach we call causal linearization via perturbation responses (CLIPR), which yields an approximation of the direct causal effects between all genes modeled by the diffusion. CLIPR provably identifies causal effects under a linear drift assumption and recovers causal structure in both simulated systems and a genome-wide perturbation screen, where it clusters genes into coherent functional modules and resolves causal relationships that standard differential expression analysis cannot. The LCD-CLIPR framework bridges generative modeling with causal inference to predict unseen perturbation effects and map the underlying regulatory mechanisms of the transcriptome.

</details>

---

## 2. Additive-input encoding fails operator-level target-held-out prediction on current Perturb-seq screens

- **期刊**: bioRxiv
- **作者**: Fullmer, K., Kutzen, D., Terooatea, T. W.
- **机构**: Tommy W Terooatea @ Brigham Young University
- **日期**: 2026-10-08
- **ID**: DOI: 10.64898/2026.09.30.755776  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.30.755776v1
- **相关分数**: 7/10
- **一句话推荐**: 严格评估Perturb-seq扰动模型在未见目标上的泛化性失败，与单细胞扰动及模型泛化性评估高度相关。
- **方法**: 基于目标分组嵌套交叉验证与匹配信噪比线性对照，评估Perturb-seq数据中加性输入线性稳态算子的目标泛化能力。
- **主要发现**: 现有Perturb-seq筛选中，加性输入编码在目标留出预测上未能超越预测基线，拟合的算子不可作为目标泛化的调控算子。
- **对我的启发**: 在评估预训练基因组学模型跨细胞类型增强子活性预测时，应引入严格的未见目标交叉验证与匹配几何特征的正向基线对照，以避免高估模型的泛化能力。

<details><summary>Abstract</summary>

Pooled Perturb-seq screens are often interpreted through a linear steady-state model in which each targeted gene supplies an additive perturbation input. Although this formulation identifies an operator on the observed response subspace in closed form, identifiability alone does not establish that inferred operators generalize to new perturbation targets. We evaluated fixed program-space additive inputs in three Perturb-seq screens -- Replogle K562 essential, Replogle RPE1 essential, and Jost 2020 -- using target-grouped nested cross-validation and matched signal-to-noise linear-truth controls. For inverse operator prediction, real held-out error remained at the predict-zero baseline (0.96, 1.00, and 1.00), whereas matched linear controls achieved 0.18, 0.53, and 0.72. This discrepancy persisted across random K562 target panels, an overdetermined Jost dimension sweep, direction-only fits, ridge and truncated-SVD estimators, and five linear ground-truth ensembles. Forward target-held-out prediction was more nuanced: fixed, footprint, and learned linear encodings modestly beat a predict-training-mean baseline in K562 but not in RPE1 or Jost, and the K562 gains recovered only about 7% of the gap to the matched linear control. On the tested screens, fitted fixed program-space operators should not be interpreted as validated target-generalizing regulatory operators. We release anchor-op, a reproducible toolkit for target-grouped evaluation, identifiability checks, and matched-geometry positive controls for perturbation-response models.

</details>

---
