# Paper Scout 日报 2026-09-18

共筛选出 **6** 篇推荐论文。
📊 抓取 arxiv 38/biorxiv 122/pubmed 63 → 粗筛 88 篇 → LLM 选中 6 篇

## 1. HyCoSeq: Contextual Hyperbolic Representation Learning for Genomic Sequences

- **期刊**: arXiv
- **作者**: Chenhao Zeng, Zhibin Pu, Shufei Ge
- **日期**: 2026-09-15
- **ID**: arXiv: 2609.16925  |  URL: https://arxiv.org/abs/2609.16925
- **相关分数**: 8/10
- **一句话推荐**: 属于生物序列的表示学习和DNA语言模型范畴，与你的研究兴趣高度契合。
- **方法**: 提出 HyCoSeq 框架，结合多曲率洛伦兹编码、加权洛伦兹残差聚合与双向 LSTM，实现基因组序列的双曲几何上下文表示学习。
- **主要发现**: 无需大规模预训练，该模型通过双曲几何与上下文建模即可在多种基因组任务上超越现有双曲基线，并达到与大型预训练 DNA 语言模型相媲美的性能。
- **对我的启发**: 双曲几何的归纳偏置与轻量级上下文建模可作为预训练大模型的高效替代方案，在增强子活性预测中捕捉层级与长程依赖，从而规避预训练模型 padding 带来的计算开销与潜在偏差。

<details><summary>Abstract</summary>

Hyperbolic geometry provides a natural inductive bias for genomic representation learning, but existing hyperbolic genomic models primarily use Lorentz convolutions to learn local sequence representations, while their residual pathways do not directly aggregate full Lorentz representations. We propose HyCoSeq, a contextual hyperbolic representation learning framework for genomic sequences. HyCoSeq incorporates weighted Lorentzian residual aggregation into multi-curvature Lorentz encoding, allowing full Lorentz representations to participate directly in geometry-consistent local aggregation. It further introduces a bidirectional long short-term memory network that integrates information from both sequence directions to learn contextual relationships among local representations at different positions within a genomic sequence, thereby extending local hyperbolic convolutional encoding to sequence-level contextualized representations. Extensive experiments across diverse genomic tasks show that HyCoSeq outperforms existing hyperbolic baselines and, without large-scale genomic pretraining, achieves competitive performance against substantially larger pretrained DNA language models.

</details>

---

## 2. CellRFT: Reinforcement Fine-Tuning for Single-Cell Perturbation Modeling

- **期刊**: arXiv
- **作者**: Jie Yan, Li Liu, Hanze Guo et al. (10 authors)
- **日期**: 2026-09-17
- **ID**: arXiv: 2609.19970  |  URL: https://arxiv.org/abs/2609.19970
- **相关分数**: 8/10
- **一句话推荐**: 直接涉及单细胞扰动建模，并使用强化学习微调优化生物学指标，与AI4LifeScience高度相关。
- **方法**: 提出基于策略梯度的强化微调框架（CellRFT），将不可微的生物学评估指标作为直接奖励信号来优化单细胞扰动预测模型。
- **主要发现**: 将生物学评估直接作为强化学习奖励可显著提升扰动预测性能；不同生物学指标间存在竞争或互补关系，分层聚合互补奖励能提升模型在未直接优化指标上的表现。
- **对我的启发**: 对于增强子活性预测任务，若下游评估指标（如特定细胞类型的游离型增强子活性相关性）不可微，可借鉴此强化微调思路，将生物学评估直接作为奖励信号优化预训练基因组学模型，而非仅依赖代理损失。

<details><summary>Abstract</summary>

Predicting cellular responses to perturbations supports the study of gene function, disease mechanisms, and therapeutic strategies. Despite advances in single-cell perturbation modeling, existing models typically optimize surrogate losses that do not directly reflect the biological criteria used for evaluation, so better data fitting need not yield better biological predictions. To address this mismatch, we introduce \textbf{CellRFT}, a reinforcement fine-tuning framework that uses biological evaluation as direct training feedback. CellRFT uses policy-gradient optimization to learn from non-differentiable evaluations of generated cell populations and integrates multiple biological rewards through hierarchical reward aggregation. Comprehensive experiments demonstrate CellRFT's applicability across different pretrained models and effectiveness in improving perturbation prediction, reveal that optimizing one biological criterion can help or hinder others, and show that complementary rewards can improve criteria beyond those directly optimized, offering a way to probe how biological metrics shape model behavior, with the potential to inform evaluation design. Code will be made available.

</details>

---

## 3. GIA: Germline-Informed Aging with AlphaGenome Finds Genetically Regulated CpGs

- **期刊**: arXiv
- **作者**: Sean Lim
- **日期**: 2026-09-15
- **ID**: arXiv: 2609.17801  |  URL: https://arxiv.org/abs/2609.17801
- **相关分数**: 8/10
- **一句话推荐**: 直接使用AlphaGenome预测变异对染色质可及性和甲基化的调控效应，与序列到功能预测及表观调控变异效应高度相关。
- **方法**: 结合meQTL映射与AlphaGenome预训练序列模型，对表观遗传时钟CpG位点的遗传变异进行变异效应预测与染色质可及性评分。
- **主要发现**: 表观遗传时钟CpG位点显著富集受遗传调控的meQTL，且AlphaGenome预测的染色质效应能成功识别出影响甲基化与基因表达的关键顺式变异。
- **对我的启发**: AlphaGenome在预测变异对染色质可及性效应上的有效性，启发我在评估预训练基因组学模型padding策略对增强子活性预测的影响时，可引入变异效应预测作为模型序列上下文依赖性的基准测试维度。

<details><summary>Abstract</summary>

Epigenetic clocks estimate age and aging-related phenotypes from DNA methylation at selected CpG sites, but the extent to which these inputs are influenced by germline genetic variation is unclear. Because methylation at many CpGs is genetically regulated, some between-person variation in clock estimates may reflect inherited genetic differences rather than aging-related change alone. Here we developed GIA (Germline-Informed Aging), a framework that maps CpGs selected from 13 published epigenetic clocks to blood methylation quantitative trait loci (meQTLs) and scores associated genetic variants with AlphaGenome. We show that clock CpGs were enriched for blood meQTLs relative to matched unused Illumina 450k probes (62.7% versus 39.6%; OR 2.57), across multiple clock families, suggesting that age-informative methylation sites are heavily influenced by germline genetic variation. Ranking by predicted chromatin effect isolated rs10190186, a cis-acting variant at FHL2 predicted to increase blood chromatin accessibility (ATAC +1.00; DNase +1.64) and FHL2 RNA (+0.30). This locus illustrates how inherited variation may shape methylation features repeatedly used by epigenetic clocks, motivating direct tests of whether such variants shift baseline clock estimates or longitudinal aging trajectories.

</details>

---

## 4. Toward AI Virtual Cells for Hepatology: Representation, Generation, Dynamics, and Intervention in Single-Cell Models.

- **期刊**: Clinical and molecular hepatology
- **作者**: Youngseok Choi, In Gyeong Koh, Murim Choi, Joon-Yong An
- **机构**: Joon-Yong An @ Department of Integrated Biomedical and Life Science, Korea University, Seoul, Republic of Korea. joonan30@korea.ac.kr.
- **日期**: 2026-09-17
- **ID**: DOI: 10.3350/cmh.2026.0820  |  PMID: 42749352  |  URL: https://pubmed.ncbi.nlm.nih.gov/42749352/
- **相关分数**: 7/10
- **一句话推荐**: 综述了AI虚拟细胞（AIVC）在单细胞建模、扰动预测和基础模型迁移方面的思路，高度切题。
- **方法**: 综述了构建肝脏AI虚拟细胞的三种互补建模范式：生成式表示模型、动态状态转换模型与预训练基础模型，并以扰动响应预测作为交叉评估框架。
- **主要发现**: 现有单细胞模型虽能实现图谱整合与回顾性响应预测，但尚未构成前瞻性验证的细胞模拟器；需引入多维度留出法（供体、病因、阶段等）及校准不确定性进行严格评估。
- **对我的启发**: 在评估预训练基因组学模型预测增强子活性的泛化能力时，可借鉴其多维度留出法（如跨细胞类型、跨扰动条件）与校准不确定性指标，以更严谨地验证虚拟表观遗传特征的预测可靠性。

<details><summary>Abstract</summary>

``Single-cell and spatial atlases describe the healthy and diseased liver at high resolution, including lobular hepatocyte zonation, fibrotic macrophage-stellate niches, cholangiocyte reactions, immune remodeling, and hepatocellular carcinoma ecosystems. These maps show where cell states occur but do not, by themselves, predict whether liver injury will progress or how the liver will respond to an untested drug, toxicant, or genetic perturbation. In this review, we organize current approaches toward an AI Virtual Cell (AIVC) for the liver into three complementary modeling routes. Generative models represent cell states, dynamics and transport models infer state transitions, and pretrained or foundation models test whether learned representations transfer across donors, etiologies, disease stages, and platforms. Perturbation-response prediction serves as a cross-cutting assessment of whether these layers can predict responses to untested genetic, chemical, inflammatory, or metabolic interventions. Available evidence can be categorized as direct liver validation, liver-included benchmarks, general single-cell evidence, and conceptual applications. Published models demonstrate individual components, including atlas integration, inferred trajectories, transferable representations, and retrospective response programs. However, these models do not constitute a prospectively validated liver simulator. At minimum, evaluation should include donor-, etiology-, stage-, platform-, and perturbation-level hold-outs. Model performance should be reported using response direction, recovery of differentially expressed genes and rare states, and calibrated uncertainty. Claims about tissue- or function-level prediction additionally require independent spatial, histologic, metabolic, and functional readouts. Near-term use should prioritize experiment selection and hypothesis generation, whereas clinical decision support remains a longer-term objective.

</details>

---

## 5. A foundation model learns the sequence and functional grammar of fully human heavy-chain-only antibodies

- **期刊**: bioRxiv
- **作者**: Nona Biosciences AI4S Team,, Miao, H.
- **机构**: Hongjiang Miao @ Nona Biosciences (Shanghai)
- **日期**: 2026-09-15
- **ID**: DOI: 10.64898/2026.09.10.750553  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.10.750553v1
- **相关分数**: 5/10
- **一句话推荐**: 属于生物序列基础模型和表示学习，但针对的是抗体蛋白序列而非基因组DNA或调控元件。
- **方法**: 基于大规模全人源重链抗体库的领域特异性蛋白质语言模型预训练（HCAbLM）。
- **主要发现**: 专用抗体库预训练使模型学到了通用模型缺失的区域选择性序列兼容性先验，且其冻结表征能有效迁移至抗体理化性质预测。
- **对我的启发**: 在预测不同细胞类型增强子活性时，可探索针对特定细胞类型或表观状态的增强子序列进行源特异性预训练，以捕捉通用基因组模型遗漏的局部功能语法。

<details><summary>Abstract</summary>

Antibody language models learn from large natural repertoires, but whether generic representations capture the constraints of specialized antibody formats remains unclear. We first characterized fully human heavy-chain-only antibodies (HCAbs) independently of HCAb-trained models. Source-aware comparisons with conventional human VH domains revealed a reproducible distributional shift localized predominantly to CDR1/2, CDR3 architecture and, where supported, a restricted framework region rather than widespread framework remodeling. These model-independent differences motivated repertoire-specific pretraining. We developed HCAbLM, to our knowledge the first foundation model pretrained specifically on a large-scale fully human HCAb repertoire, using 31.8 million sequences from 73 independently immunized HCAb mice. HCAbLM learned a region-selective sequence-compatibility prior distinct from conventional antibody language models, and its frozen representations transferred to experimentally measured SEC purity, HIC behavior and thermal stability in grouped internal validation and retrospective cross-project evaluation. These findings identify repertoire composition as an important biological design variable for foundation models of specialized antibody formats.

</details>

---

## 6. scACORN: Context-engineered agent orchestration of specialized small language models for single-cell transcriptomic interpretation

- **期刊**: bioRxiv
- **作者**: Rasti-Meymandi, A., Nahali, S., Paramithiotis, E., Cheung, A. M., Dolatabadi, E.
- **机构**: Elham Dolatabadi @ York University; Vector Institute, Toronto, Ontario, Canada
- **日期**: 2026-09-16
- **ID**: DOI: 10.64898/2026.09.10.750801  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.10.750801v1
- **相关分数**: 5/10
- **一句话推荐**: 使用小型语言模型和代理编排进行单细胞转录组解释，与你的虚拟细胞和表示学习兴趣间接相关。
- **方法**: 提出一种基于上下文工程代理编排的专家小语言模型组合架构，通过领域对齐对比适应与几何保持特化两阶段构建专家，并由无梯度更新的语言模型代理进行动态选择与组合。
- **主要发现**: 专家模型专门化与代理编排机制有效应对了单细胞分析的任务异构性，显著提升了跨组织迁移准确率并大幅降低了无证据基因引用率。
- **对我的启发**: 在微调预训练基因组学模型预测不同细胞类型增强子活性时，可借鉴其“领域对齐+几何保持特化”的两阶段范式，以缓解下游任务微调导致的序列到功能特征空间退化问题。

<details><summary>Abstract</summary>

Single-cell atlases now exceed 66 million cells, but turning a ranked expression profile and a free-form biological question into a reliable, evidence-grounded answer remains unsolved. Scaling a single model does not resolve this, because single-cell interpretation is a heterogeneous family of tasks whose correct answer depends on tissue, cohort, perturbation and annotation resolution. Here we present scACORN, an agentic alternative to monolithic single-cell language models that combines specialized small language models with context-engineered agent orchestration for their selection and composition at inference time. Each expert is built in two stages: domain-aligned contrastive adaptation fits a pretrained cell-to-text backbone to the transcriptomic geometry of a target dataset, and geometry-preserving specialization learns question-conditioned biological completions without eroding that geometry. A fixed orchestrating language model agent then selects and combines experts under a natural-language playbook that is itself optimized from textual feedback, with no gradient updates to the orchestrator. Across 10 Tabula Sapiens tissues, domain alignment raised transfer macro-F1 from 0.36 to 0.64 and Recall@5 from 0.87 to 0.97; specialized experts reached 0.89 mean exact-match annotation accuracy; and playbook optimization reduced unsupported gene citations from 14.5% to 3.5%. Our findings support specialization and orchestration as complementary responses to the heterogeneity and evidentiary demands of single-cell analysis.

</details>

---
