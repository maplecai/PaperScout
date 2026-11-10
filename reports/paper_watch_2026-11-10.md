# Paper Scout 日报 2026-11-10

共推荐 **4** 篇论文。

## 1. Systematic promoter perturbation reveals limitations of AlphaGenome gene expression predictions

bioRxiv · 预印本 · 2026-11-09 · 相关性 9/10

**研究关联：方法可借鉴**

- **为什么值得看**：直接评估了AlphaGenome这一代表性基因组基础模型在启动子扰动下的序列到功能预测能力与局限性。
- **任务与验证范围**：输入：计算机模拟扰动的启动子序列（二核苷酸洗牌、GC调整随机碱基替换、N-masking） → 输出：预测的CAGE和RNA-seq信号；研究物种：摘要未说明；验证范围：跨20个组织。
- **核心方法**：采用计算机模拟序列扰动范式，结合AlphaGenome序列到功能（S2F）模型预测多组织基因表达读数。
- **主要发现与证据**：启动子扰动显著降低预测的CAGE活性（N-masking降低约三个数量级），但RNA-seq信号受影响较小，导致两种读数解耦；模型能识别启动子局部活性丧失，但无法将效应一致传播至下游外显子，尤其在长基因中。
- **可借鉴点（研究建议）**：可借鉴其系统序列扰动范式（如N-masking或洗牌）来评估预训练基因组学模型在增强子活性预测中的多轨道一致性和长距离依赖捕获能力。
- **迁移边界**：原论文聚焦启动子扰动对转录本全长的影响，而我的研究关注游离型增强子活性和padding影响；AlphaGenome在启动子-基因传播上的局限不能直接等同于其在增强子或padding任务上的表现，跨任务泛化未经验证。
- **阅读时核实**：AlphaGenome在处理输入序列时是否使用了固定长度的padding？如果是，padding策略是否影响了其对长基因下游外显子效应的传播能力？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.06.764851v1) · [DOI](https://doi.org/10.64898/2026.11.06.764851)

作者：Sreenivasan, V. K. A., Aksu, E. D., Spielmann, M.
来源标注的末位/通讯作者：Malte Spielmann
机构：Charite University Medicine Berlin

### 英文摘要

Sequence-to-function (S2F) models promise to facilitate the interpretation of noncoding variants by predicting their effects on gene regulation directly from genomic sequence. However, whether these models recapitulate fundamental principles of transcriptional biology remains unclear. Here, we tested whether AlphaGenome recognizes the expected consequences of promoter disruption on predicted gene expression. We systematically perturbed annotated promoter elements in silico for 2,111 promoter-gene pairs using dinucleotide shuffling, GC-adjusted random base substitution, and N-masking. We then compared AlphaGenome-predicted CAGE and RNA-sequencing signals across 20 tissues for reference and promoter-disrupted sequences. While CAGE and RNA-sequencing predictions were strongly correlated for reference sequences, promoter disruption markedly reduced predicted CAGE activity, with N masking producing reductions of approximately three orders of magnitude. By contrast, the predicted RNA-sequencing signals were substantially less affected, resulting in an uncoupling of two molecular readouts of gene expression. Exon-level analyses showed that AlphaGenome predicted reduced RNA-sequencing signal when exonic sequences are within the disrupted region, but frequently failed to propagate this effect to downstream exons. This divergence between the CAGE and RNA-sequencing readouts was apparent from the second exon onward and was more pronounced in longer genes. Although alternative transcription initiation and shared downstream exons may explain individual cases, it is unlikely to account for the systematic discordance between CAGE and RNA-sequencing predictions. These findings indicate that AlphaGenome can recognize the local loss of promoter activity without consistently capturing its consequences across the corresponding transcript. More broadly, our results show that predictions from individual S2F output tracks do not necessarily reflect a coherent model of transcription. Systematic biological benchmarking and experimental validation therefore remain essential before such predictions can be used to prioritize or classify noncoding variants in research or diagnostic settings.

---

## 2. MELD: Mutation Effect Learning through Differential embeddings

bioRxiv · 预印本 · 2026-11-09 · 相关性 8/10

**研究关联：方法可借鉴**

- **为什么值得看**：提出了一种直接基于野生型-突变体差异进行训练的变异效应预测新范式，与sequence-to-function模型高度相关。
- **任务与验证范围**：输入：野生型(WT)与突变型(SNV)DNA序列对 → 输出：变异功能后果预测；研究物种/细胞体系：摘要未说明（涉及人类ClinVar与BRCA1）；验证范围：跨数据集（ClinVar、BRCA1饱和基因组编辑），是否跨细胞类型摘要未说明
- **核心方法**：采用共享CNN-Transformer编码器提取特征，将突变型与野生型的logit差值（Δz）直接置于监督目标中进行训练，并辅以突变掩码增强、多尺度突变中心池化和自适应放大因子。
- **主要发现与证据**：MELD仅用1.9M参数，在ClinVar上AUROC达0.986，显著优于同等骨干的ISM基线（0.800）及参数量大3-1300倍的预训练模型（如AlphaGenome 0.924）；在仅5万训练样本下即超越全量训练的ISM基线，并在BRCA1饱和编辑数据上取得Spearman ρ=0.42（迁移后达0.45）。
- **可借鉴点（研究建议）**：可考虑将“差分监督”思想引入我的研究，例如通过直接学习不同padding策略或不同虚拟表观遗传特征下的序列特征差值，以提升模型对特定序列扰动或状态变化的敏感度与数据效率。
- **迁移边界**：MELD针对的是SNV变异效应预测，强调WT-Mutant对的差分学习；而我的任务是序列到增强子活性的绝对预测及padding影响评估，差分监督的迁移需重新定义“基准态”与“目标态”，且该模型在跨细胞类型泛化或长距离增强子调控上的能力尚未在摘要中体现。
- **阅读时核实**：MELD的“突变掩码增强”和“多尺度突变中心池化”具体如何实现？这种局部特征聚焦机制在处理长序列或非局部依赖的增强子活性预测时是否依然有效？

[原文](https://www.biorxiv.org/content/10.64898/2026.10.29.762727v1) · [DOI](https://doi.org/10.64898/2026.10.29.762727)

作者：Alajji, A., Jashil, R., Mall, R., Elshrif, M.
来源标注的末位/通讯作者：Mohamed Elshrif
机构：Qatar Computing Research Institute

### 英文摘要

We introduce MELD (Mutation Effect Learning through Differential Embeddings), a compact model for predicting the functional consequences of single nucleotide variants (SNVs) by training directly on the wild-type (WT) versus mutant differential. Interpreting SNVs is central to clinical genomics, yet experimental characterization cannot scale to millions of observed variants. Leading sequence-to-function models (Enformer, Borzoi, AlphaGenome) are trained on absolute genomic tracks and score variants post hoc through in-silico mutagenesis (ISM), so the WT-mutant difference never enters the training loss. MELD instead places the logit difference {Delta}z = zmut - zwt inside the supervised objective. It combines a shared CNN-Transformer encoder, a mutant-specific mutation-mask boost, multiscale mutation-centered pooling, and a learned adaptive amplification factor . On ClinVar (1.57M variants), MELD (1.9M parameters) reached an AUROC of 0.986 versus 0.800 for a same-data, same-backbone ISM baseline, with ablations confirming the contribution of each component. On a shared benchmark, it outperformed frozen foundation models with 3-1,300x more parameters (AUROC 0.967 vs. 0.924 for AlphaGenome and 0.936 for Nucleotide Transformer). With only 50, 000 training variants, it exceeded the ISM baseline trained on all 1.48M (AUROC 0.903 vs. 0.796) variants. On BRCA1 saturation genome editing, frozen MELD achieved a Spearman {rho} of 0.42, above Borzoi (0.40), and ClinVar transfer raised it to 0.45. These results demonstrate that direct differential supervision is a compact, data-efficient alternative to post-hoc ISM scoring with substantially larger pretrained models.

---

## 3. Uncertainty-Aware Personalised Gene Expression Prediction Improves Cell-Type-Specific Association Testing

bioRxiv · 预印本 · 2026-11-09 · 相关性 8/10

**研究关联：方法可借鉴**

- **为什么值得看**：结合个性化序列表示与不确定性感知，预测跨细胞类型的基因表达效应，契合细胞类型特异性调控预测的研究兴趣。
- **任务与验证范围**：输入：个性化基因组序列表示 → 输出：细胞类型特异性基因表达预测及不确定性量化；研究物种/体系：人类血液和脑细胞类型（OneK1K, ROSMAP）；验证范围：跨血液和脑细胞类型，并应用于系统性红斑狼疮和阿尔茨海默病的关联测试
- **核心方法**：结合个性化序列表示与不确定性感知预测的深度学习模型（ATTICUS），利用bulk表达预训练迁移至无需配对单细胞基因型的细胞类型特异性预测。
- **主要发现与证据**：在血液和脑细胞中，ATTICUS相比scPrediXcan将表达预测相关性提高约一倍并显著提升效应方向准确性；不确定性传播降低了TWAS统计膨胀，在疾病应用中识别出更多具有强方向一致性的细胞特异性关联。
- **可借鉴点（研究建议）**：可借鉴其将bulk预训练信息迁移至特定细胞类型预测的范式，以及引入不确定性量化提升预测可靠性的思路，推测可用于评估增强子活性预测模型的置信度。
- **迁移边界**：原论文聚焦于全基因组基因表达预测与TWAS应用，未涉及游离型增强子活性或序列padding策略的影响；其跨细胞类型泛化建立在无需配对数据的迁移学习上，不能直接等同于DNA序列基础模型在增强子任务上的表现。
- **阅读时核实**：ATTICUS在缺乏配对基因型与单细胞表达数据时，具体是如何构建个性化序列表示并实现从bulk到单细胞类型的迁移学习的？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.06.764604v1) · [DOI](https://doi.org/10.64898/2026.11.06.764604)

作者：Styll, P., Di, Y., Cai, N.
来源标注的末位/通讯作者：Na Cai
机构：ETH Zurich

### 英文摘要

Linking genetic variation to disease requires accurate prediction of its effects on gene expression in relevant cell types. Sequence-to-function models offer a way to predict these effects and, with training on personal genomes, have begun to capture inter-individual expression differences. However, effect sign accuracy remains limited, and predictive uncertainty is unquantified. Here we introduce ATTICUS, which combines personalised sequence representations with uncertainty-aware expression prediction. ATTICUS transfers regulatory information learned in bulk expression pretraining to cell-type-specific expression prediction without requiring genotypes paired with single-cell expression data. Across blood and brain cell types in OneK1K and ROSMAP, ATTICUS approximately doubles expression prediction correlations relative to scPrediXcan and substantially improves sign accuracy. Moreover, ATTICUS enables uncertainty-aware transcriptome-wide association studies (TWAS). Applied to systemic lupus erythematosus and Alzheimer's disease, ATTICUS identifies more associations, with greater cell-type specificity and stronger directional concordance, and reduced statistical inflation. Together, our results demonstrate that personalised training makes predictions more directionally consistent, and uncertainty propagation improves the calibration of TWAS and the prioritisation of disease genes. ATTICUS provides a framework for both, enabling the use of single-cell expression datasets without matched genotypes to inform uncertainty-aware TWAS, expanding their use in prioritising disease-associated genes and cell types.

---

## 4. BioMeme: biological response memory for virtual cells

bioRxiv · 预印本 · 2026-11-09 · 相关性 8/10

**研究关联：方法可借鉴**

- **为什么值得看**：提出了一种用于虚拟细胞预测扰动响应的新架构，直接命中virtual cell和single-cell perturbation研究兴趣。
- **任务与验证范围**：输入：测量的低剂量细胞状态及参考细胞系响应 → 输出：新细胞类型的下一剂量响应；细胞体系：U2OS、MCF7等细胞系（物种摘要未说明）；验证范围：跨细胞类型（U2OS到MCF7）及跨化合物。
- **核心方法**：采用生物响应记忆机制，用基于测量的实验记忆库（通过单次线性求解更新）替代神经网络中的状态到响应学习层，实现可检索、可解释的预测。
- **主要发现与证据**：在9项预注册比较中，该方法的响应方向预测优于其替代的学习器；在U2OS中优于ridge、chemCPA等基线，且匹配全面板网络（误差在3.4%内）；化合物特异性转移降低误差21.2%；拟合速度比神经网络快至少420倍。
- **可借鉴点（研究建议）**：对于跨细胞类型的增强子活性预测，可探索用“表观遗传特征记忆库”替代部分全连接层，以提升模型在未见细胞类型上的可解释性与少样本更新能力。
- **迁移边界**：原论文处理的是化学扰动下的细胞剂量响应，依赖化合物在不同细胞间的相似性进行记忆检索；而我的任务是DNA序列到增强子活性的映射，其跨细胞类型泛化机制不同，不能直接假设该记忆机制在序列到功能任务上同样有效。
- **阅读时核实**：BioMeme中“记忆”检索的相似度度量是如何定义的？其线性求解的数学形式是否对输入特征的分布有特定假设？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.07.765043v1) · [DOI](https://doi.org/10.64898/2026.11.07.765043)

作者：Bi, J., Zhu, C., Liu, H. et al. (9 authors)
来源标注的末位/通讯作者：Chenyang Zhu
机构：School of Electronics and Computer Science, University of Southampton, Southampton, SO17 1BJ, UK

### 英文摘要

Virtual cells predict responses to unmeasured perturbations, but neural models absorb measurements into weights, require retraining and cannot cite supporting experiments. Here we introduce biological response memory, replacing a learned state-to-response layer with a memory of measured experiments. BioMeme predicts next-dose responses in a new cell type from measured lower-dose states, recalling similarly responding compounds in that cell and the same compound in a reference cell line. Each prediction is an exact weighted sum of named measurements, and memory updates with one linear solve. In all nine preregistered comparisons across three screens, memory predicted response direction better than the learners it replaced. In U2OS, BioMeme outperformed input-matched ridge, adapted chemCPA and a neural layer in memory's place, and matched a full-panel network reading reference responses directly (error within 3.4%). Transfer was compound-specific, lowering error by 21.2% against at most 1.8% for wrong compounds, and replicated in reserved MCF7 data. With 20 references, fitting took seconds on one CPU thread, at least 420 times faster than neural tuning and fitting. Adding its prediction to one measured well cut that well's error by 27-31%. Biological response memory establishes a design principle for virtual cells any laboratory can update, inspect and run.

---

中文笔记基于标题和摘要生成，未核验全文；研究建议不代表论文已验证的结论。相关性分数不是论文质量评分。

检索统计：窗口 [2026-11-07 00:00, 2026-11-10 00:00) UTC；抓取 biorxiv 64/pubmed 24 → 粗筛 29 篇 → LLM 选中 4 篇
