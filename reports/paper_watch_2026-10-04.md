# Paper Scout 日报 2026-10-04

共筛选出 **3** 篇推荐论文。
📊 抓取 arxiv 50/biorxiv 96/pubmed 265 → 粗筛 35 篇 → LLM 选中 3 篇

## 1. VCLMU: Mechanism-Centric Virtual Cell World Modeling for Perturbation Response

- **期刊**: arXiv
- **作者**: Yuwei Miao, Azim Dehghani Amirabad, Scott Oloff, Junzhou Huang, Tianyu Cui, Rui Liao
- **日期**: 2026-10-03
- **ID**: arXiv: 2610.04475  |  URL: https://arxiv.org/abs/2610.04475
- **相关分数**: 8/10
- **一句话推荐**: 直接命中virtual cell和single-cell perturbation研究方向，提出机制中心的虚拟细胞世界模型预测扰动响应。
- **方法**: 提出一种以机制为中心的虚拟细胞世界模型（VCLMU），将细胞状态表征为潜在机制单元（LMU），并将遗传扰动建模为对潜在状态的随机转移动作，通过两阶段预训练解码转录响应。
- **主要发现**: 该模型在六个未见扰动的基准测试中显著提升了特定扰动响应的恢复能力，且学习到的LMU能捕获结构化的生物响应程序，证明了机制级潜在状态转移建模的有效性。
- **对我的启发**: 可将不同细胞类型特异性的增强子活性变化视为对虚拟表观遗传特征的'扰动动作'，并构建可复用的潜在机制单元来解耦序列特征与表观遗传状态，以提升跨细胞类型游离型增强子活性预测的泛化能力。

<details><summary>Abstract</summary>

Predicting cellular responses to genetic perturbations is a central capability for virtual cells and a key step toward computational modeling of biological interventions. Most existing models directly map an unperturbed molecular profile and perturba- tion to the resulting observation without explicitly representing the latent cellular transition induced by the intervention. We introduce a mechanism-centric virtual cell world model that represents cellular state as a set of Latent Mechanism Units (LMUs) and treats genetic perturbations as actions on these latent states. Each LMU combines a reusable identity grounded in multimodal biological evidence with an observation-specific state, allowing a perturbation to induce mechanism- specific stochastic transitions before decoding the resulting transcriptional response. We train VCLMU through two-stage pretraining, first on around 200K pseudo-bulk perturbation profiles and then on gene-aligned single-cell perturbation data. Across six perturbation-disjoint benchmarks, VCLMU consistently improves perturbation- specific response recovery over strong baselines while maintaining competitive global response accuracy. We further analyze learned LMUs through enrichment between perturbation responses and LMU gene sets and show that they capture structured biological response programs. These results support mechanism-level latent state transition as a useful formulation for virtual cell models that aim to predict and interpret cellular responses to biological interventions.

</details>

---

## 2. LOAM: A family of genomic language models trained on long-read soil metagenomes

- **期刊**: bioRxiv
- **作者**: Ferry, Q. R., Frank, M., Jehn, J., Schaks, M., Steinkraus, B. R., Rajakumar, T.
- **机构**: Timothy Rajakumar @ Soilytix GmbH
- **日期**: 2026-10-02
- **ID**: DOI: 10.64898/2026.09.28.755120  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.28.755120v1
- **相关分数**: 8/10
- **一句话推荐**: 直接命中genomic foundation model和DNA language model研究方向，训练基因组语言模型并系统评估各层表征的生物学信息可线性提取性。
- **方法**: 基于长读长宏基因组数据预训练的 decoder-only 基因组语言模型族。
- **主要发现**: 长读长数据训练的小模型性能优于同等规模甚至更大模型，且任务相关信息在中间层更易线性提取，零样本预测效果受预训练语料同源序列影响显著。
- **对我的启发**: 在利用预训练模型预测增强子活性时，可探索中间层表征的线性可分性，并排查预训练语料中增强子同源序列对零样本评估的潜在偏差。

<details><summary>Abstract</summary>

Soil ecosystems represent a vast, largely uncharacterised reservoir of microbial diversity. Metagenomic assembly has unlocked access to this resource, and recent advances in long-read sequencing have improved the recovery and quality of microbial genomes from complex samples. While genomic language models have proven highly effective at capturing biological concepts from large sequence datasets, they have predominantly been trained on reference genomes or short-read assemblies. Here, we present LOAM, a family of decoder-only genomic language models ranging from 25 to 624 million parameters and trained exclusively on Oxford Nanopore long-read environmental metagenomes. LOAM model performance scales predictably with model size and training-token budget. Despite a relatively small training sequence corpus, LOAM models outperformed comparably sized models across biological benchmarks, and achieved performance competitive with substantially larger state-of-the-art models trained on much larger datasets. Context-intervention experiments further showed that LOAM models use genomic information over several kilobases, highlighting the potential value of increased contiguity provided by long-read metagenome-assembled genomes. For probe-based benchmark tasks, we systematically evaluated representations across hidden layers and revealed that task-relevant biological information was frequently more linearly accessible from intermediate than final model layers. Finally, we observed that variation in zero-shot variant-effect prediction was strongly associated with the presence of homologous target sequences in the pre-training corpus. Together, these results establish long-read environmental metagenomes as a viable foundation for training competitive genomic language models and demonstrate the importance of both model scale and training-corpus composition for biological generalisation.

</details>

---

## 3. Phenotypes of ultra-rare variant carriers benchmark variant effect scores

- **期刊**: bioRxiv
- **作者**: Londhe, S., Holtkamp, E., Tsitsiridis, G., Starovoit, A., Tomaz da Silva, P., Hingerl, J., Finucane, H., Gagneur, J.
- **机构**: Julien Gagneur @ School of Computation, Information and Technology, Technical University of Munich, Garching, Germany
- **日期**: 2026-10-02
- **ID**: DOI: 10.64898/2026.10.01.755962  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.01.755962v1
- **相关分数**: 7/10
- **一句话推荐**: 评估了非编码和转录调控变异效应评分，与调控基因组学及变异预测高度相关。
- **方法**: 提出基于UK Biobank极罕见变异携带者群体表型（血浆蛋白丰度与定量性状）构建的变异效应评分基准评估框架（UKBBGym）。
- **主要发现**: 发现编码与剪接变异评分在预测表型上显著优于转录调控评分，且实验测定在错义效应预测上未必优于计算评分，揭示了插入缺失和功能丧失变异预测仍有较大改进空间。
- **对我的启发**: 该研究指出转录调控评分在群体表型层面表现较弱，提示在构建基于虚拟表观遗传特征的增强子活性预测模型时，需更关注如何将序列到功能的预测与真实群体表型对齐，以提升调控变异评分的生理相关性。

<details><summary>Abstract</summary>

Human genetics needs benchmarks for evaluating variant scores against observed phenotypic consequences. We therefore present UKBBGym, which evaluates coding and non-coding scores against plasma protein abundance and quantitative traits observed in carriers of ultra-rare variants in the UK Biobank. This design avoids ascertainment biases of clinical labels, potential physiological mismatch of experimental assays, and confounding pertaining to common-variant associations. UKBBGym recapitulates relative performance on pathogenicity prediction while enabling comparison across variant classes and molecular mechanisms. This shows that scores designed for coding and splicing variants correlate more strongly with protein abundance and quantitative traits than scores modelling transcriptional regulation. Moreover, experimental assays do not consistently outperform computational scores for predicting missense effects. Comparing captured to detectable variance indicates scope for improvement, particularly for indels and loss-of-function variants. Finally, for coding variants, UKBBGym can be reproduced from public summary statistics, providing an accessible population-phenotype benchmark complementary to clinical labels and experimental assays.

</details>

---

> 补发日报：检索窗口 [2026-10-01 00:00, 2026-10-04 00:00) UTC。已排除此前日报及 2026-10-08 邮件中已推荐的论文；粗筛阈值 0.2，相关性至少 6/10。
