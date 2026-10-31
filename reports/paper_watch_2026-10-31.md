# Paper Scout 日报 2026-10-31

共筛选出 **3** 篇推荐论文。
📊 抓取 biorxiv 116/pubmed 64 → 粗筛 33 篇 → LLM 选中 3 篇

## 1. Digital twins forecast individual immune trajectories

- **期刊**: bioRxiv
- **作者**: Hu, C., Yu, C., Chen, C. Y.-C.
- **机构**: Calvin Yu-Chian Chen @ Peking University
- **日期**: 2026-10-30
- **ID**: DOI: 10.64898/2026.10.23.761347  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.23.761347v1
- **相关分数**: 8/10
- **一句话推荐**: 直接构建AI虚拟细胞数字孪生模型，从单细胞谱预测个体免疫轨迹，与virtual cell和single-cell perturbation研究兴趣高度吻合。
- **方法**: 基于单细胞数据对共享虚拟细胞模型进行个性化微调构建数字孪生，预测个体免疫轨迹。
- **主要发现**: 个性化数字孪生在预测免疫年龄和细胞变化方向上显著优于现有方法，且随观测积累误差降低，能揭示个体特异性免疫恢复与重塑特征。
- **对我的启发**: 在预训练基因组学模型预测增强子活性时，可借鉴“共享模型+个性化微调”范式，利用特定细胞类型的表观遗传观测数据更新虚拟特征，以提升跨细胞类型的预测精度。

<details><summary>Abstract</summary>

The human immune system differs markedly between individuals and changes in response to infection, vaccination and treatment. AI virtual cells are being built to simulate cellular responses to perturbation. Yet these models, like most immune-response predictors, describe each person by a single pre-challenge measurement and forecast change from patterns pooled across people. Digital twins, updated with every new observation of an individual, could forecast how that person's immune state changes. Here we present ImmuneTwins, which builds these twins from single-cell profiles by personalizing a shared virtual-cell model with each individual's observations. In two external populations, ImmuneTwins reduced immune-age error by 32% and 42% relative to the best existing method. During repeated influenza vaccination, its twins predicted the direction of immune-cell change 35% more accurately than the best published method, and their error fell by 27% as observations accumulated. The twins revealed that immune cells and plasma proteins recover about half their deviation from a persistent personal reference within 90 days, whereas response size varies between challenges. They further localized B-cell remodelling in exceptional longevity and anticipated patient-specific immune trajectories during myeloma treatment. These results establish virtual-cell digital twins for forecasting individual immune change and identifying each person's characteristic immune features.

</details>

---

## 2. An open structure-guided RNA foundation model for generalizable prediction

- **期刊**: bioRxiv
- **作者**: Zhu, H., Li, R., Chang, A. et al. (11 authors)
- **机构**: S Kevin Zhou @ USTC
- **日期**: 2026-10-29
- **ID**: DOI: 10.1101/2025.08.06.668731  |  URL: https://www.biorxiv.org/content/10.1101/2025.08.06.668731v1
- **相关分数**: 7/10
- **一句话推荐**: 结构引导的RNA基础模型，使用masked language modeling整合二级结构信息，与genomic foundation model和representation learning for biological sequences高度相关。
- **方法**: 提出structRFM，一种基于结构引导的RNA基础模型，通过将碱基配对相互作用整合进掩码语言建模（MLM）进行预训练。
- **主要发现**: 该模型通过结合序列与结构的多模态表征，在零样本分类、二级/三级结构预测及功能预测等任务上均达到SOTA，证明了结构引导预训练对RNA泛化能力的重要性。
- **对我的启发**: 该论文引入的动态掩码比例和多源结构集成（MUSES）以减少预测偏差的思路，可启发我在预训练基因组学模型中针对不同序列长度或padding策略设计自适应掩码机制，以降低虚拟特征预测中的偏差。

<details><summary>Abstract</summary>

RNA language models have achieved strong performance across diverse downstream tasks by leveraging large-scale sequence data. However, RNA function is fundamentally shaped by hierarchical structure, making structural information important for pre-training. Existing approaches often depend on noisy annotations or task-specific objectives that can limit generalizability. Here we present structRFM, a structure-guided RNA foundation model pre-trained on 21 million RNA sequence--structure pairs by integrating base-pairing interactions into masked language modelling through a pair-matching operation. We also introduce MUSES, a multi-source ensemble of secondary structures designed to mitigate predictor bias, and a dynamic masking ratio that balances structure-guided and nucleotide-level masking. structRFM learns joint sequence and structure representations as sequence-level, nucleotide-level and pairwise features for broad downstream adaptation. It ranks among the leading models in zero-shot homology classification and establishes new benchmarks for secondary-structure prediction. Its tertiary-structure adaptation, Zfold, consistently improves both three-dimensional predictions and their extracted secondary structures, with performance comparable to AlphaFold3 across CASP15-natural, CASP16 and RNA-Puzzles. structRFM also improves performance on function-prediction tasks and generalizes to newly released RNA families and long non-coding RNAs. Together, these results demonstrate the effectiveness of structure-guided pre-training and highlight multimodal RNA language models for robust structural and functional inference. The complete 21-million-pair dataset, model weights and source code are openly available to support multimodal RNA foundation-model development.

</details>

---

## 3. Does a map-level insulation constraint improve sequence-based prediction of 3D genome folding? A Stage 1 Registered Report with a reverse-complement-equivariant state-space model (HiFold-Mamba)

- **期刊**: bioRxiv
- **作者**: Malekpouri, M., Lotfi, S.
- **机构**: Mohammad Malekpouri @ IAU
- **日期**: 2026-10-30
- **ID**: DOI: 10.64898/2026.10.24.761502  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.24.761502v1
- **相关分数**: 7/10
- **一句话推荐**: 从DNA序列预测3D基因组折叠（sequence-to-contact-map），使用reverse-complement-equivariant Mamba架构，直接属于sequence-to-function范式。
- **方法**: 提出反向互补等变的双向状态空间模型（HiFold-Mamba）预测长序列到3D基因组折叠图谱，并引入图谱级绝缘与边界损失。
- **主要发现**: 预注册了三项假设：模型在SCC上超越基线，绝缘/边界损失提升边界和环预测精度，预训练加少样本适应优于从头训练；并指出基准测试需逐基线比较以保证统计功效。
- **对我的启发**: 其预训练结合少样本适应在held-out细胞系上的验证策略，可直接启发我利用预训练模型预测不同细胞类型的增强子活性；同时其处理1Mb长序列的架构设计对评估模型padding的边界效应有参考价值。

<details><summary>Abstract</summary>

Background. Sequence-to-contact-map models are trained with pixel-wise losses, although the features of interest (insulation, domain boundaries, loops) are summaries of the map. Insulationbased losses help Hi-C resolution enhancement. No pre-specified test has asked whether they improve sequence-based prediction, judged against annotations independent of the training data. Proposed study. HiFold-Mamba predicts 448 x 448 maps at 2,048 bp from 1,048,576 bp of DNA on the DNALongBench contact-map task. Every component is reverse-complement-equivariant: convolutional tower, bidirectional Mamba blocks, multi-scale mixer and symmetric pairwise head. We pre-register three hypotheses: >> H1: it exceeds each of three trained baselines (reproduced Akita, a parameter-matched Transformer and a parameter-matched CNN) by [&ge;]0.01 stratum-adjusted correlation (SCC). >> H2: an insulation and boundary loss, computed from the predicted map with the operator used on the observed map, improves boundary AUROC and loop AP against independent 4DN boundary calls and ENCODE CTCF ChIA-PET loops, at equal training steps and without loss of SCC. >> H3: pretraining plus few-shot adaptation beats training from scratch on four held-out cell lines.Tests use a paired bootstrap over 237 one-megabase test blocks (one-sided = 0.025). Pilot data. >> Verification. The benchmark target, the window coordinates and the networks equivariance were verified. >> Locus-shared reference. Copying other cell lines measured maps at the same locus matches published Akita on the benchmarks SCC (0.227 vs. 0.230). >> SCC weightings. Two weightings in common use weight distance strata in opposite directions and agree only moderately ({rho} = 0.54). >> Comparison rule. In simulations calibrated on the pilot data, a per-block-best comparison against several baselines has no power. We therefore test against each baseline, which gives [&ge;] 90 % power at a true gain of 0.02 when between-model correlation is [&ge;] 0.95. >> H2 positive control. On validation windows, observed maps recover the independent boundaries (AUROC 0.61 - 0.91) and loops (0.86 - 0.90). This fixed the insulation window and showed that these annotations are largely shared across cell types.

</details>

---
