# Paper Scout 日报 2026-11-04

共推荐 **5** 篇论文。

## 1. xDecoder unlocks the potential of genomic foundation models for few-shot personal gene expression prediction.

Molecular systems biology · 期刊文献 · 2026-07-28 · 相关性 9/10

**研究关联：方法可借鉴**

- **为什么值得看**：利用基因组语言模型和S2F嵌入预测个体基因表达，直接涉及sequence-to-function和基因组基础模型的泛化性评估。
- **任务与验证范围**：输入：配对的个人基因组-转录组数据（含遗传变异） → 输出：个人基因表达变异预测；研究物种/细胞体系：摘要未说明；验证范围：跨个体（few-shot已见基因与zero-shot未见位点）
- **核心方法**：提出xDecoder统一解码框架，结合预训练基因组语言模型与序列到功能（S2F）嵌入，从配对数据中学习变异对表达的影响。
- **主要发现与证据**：在few-shot设置下，该框架使已见基因的跨个体表达预测变得可行；但在未见位点zero-shot预测不可靠，且实验表明仅基于DNA的模型未能完全捕获对未见位点预测重要的染色质可及性等调控状态信息。
- **可借鉴点（研究建议）**：推测其结合S2F嵌入与gLM的解码范式，以及关于DNA-only模型跨位点泛化局限的探讨，可为我评估预训练模型在增强子活性预测中的特征提取能力及序列处理策略提供参考。
- **迁移边界**：原论文聚焦个体基因表达变异预测及跨位点泛化，我的任务为跨细胞类型增强子活性预测及padding影响评估。原论文揭示的DNA-only模型跨位点瓶颈不能直接等同于跨细胞类型增强子预测的泛化失败，需区分任务边界。
- **阅读时核实**：xDecoder在处理输入序列时如何具体融合S2F嵌入，其序列长度截断或padding策略是否对未见位点的zero-shot预测性能产生影响？

[原文](https://pubmed.ncbi.nlm.nih.gov/42521815/) · [DOI](https://doi.org/10.1038/s44320-026-00238-1)

作者：Shumin Li, Ruibang Luo, Yuanhua Huang
来源标注的末位/通讯作者：Yuanhua Huang
机构：School of Biomedical Sciences, University of Hong Kong, Hong Kong, China

### 英文摘要

Large-scale genomic language models (gLMs) hold promise for modeling gene regulation, yet their ability to capture personal gene expression variations remains unresolved. We developed xDecoder, a unified decoding framework that utilizes gLMs and sequence-to-function (S2F) embeddings to learn how personal genetic variation shapes gene expression from paired genome-transcriptome data. Compared to the pretrained genomic models, xDecoder with personalized DNA-RNA training makes cross-individual prediction tractable for seen genes in a few-shot setting. However, zero-shot prediction at unseen loci remains unreliable and gene-dependent, revealing a cross-locus transfer bottleneck of current sequence models. Experiments incorporating individual-level chromatin accessibility suggested that regulatory-state information important for unseen-locus prediction is not fully captured by current DNA-only models. Overall, these results highlight the potential utility of the few-shot setting, the limitations of DNA-only models, and point toward multi-omic, variant-aware frameworks as a promising direction for building personalized regulatory models.

---

## 2. Benchmarking DNA Foundation Models: Biological Blind Spots in Evo2 Variant-Effect Prediction

bioRxiv · 预印本 · 2026-11-03 · 相关性 9/10

**研究关联：当前课题直接相关**

- **为什么值得看**：严格基准测试Evo2等DNA基础模型在变异效应预测中的生物学盲点，直接契合我对基因组基础模型评估的研究兴趣。
- **任务与验证范围**：输入：含变异及侧翼序列的DNA片段 → 输出：变异效应预测（致病/良性分类）；研究物种/细胞体系：摘要未说明具体物种与细胞体系（涉及核与线粒体基因组）；验证范围：核与线粒体序列特征，摘要未说明是否跨细胞类型
- **核心方法**：基于已知核与线粒体生物学特征构建受控基准，评估Evo2等DNA基础模型的零样本变异效应预测能力。
- **主要发现与证据**：Evo2在线粒体变异上总体表现良好（AUROC=0.927），但对短程信号存在盲点，且对中性的侧翼序列变化表现出虚假敏感性，导致致病性tRNA变异被误判为良性。
- **可借鉴点（研究建议）**：该研究对侧翼序列敏感性的分析提示我，预训练模型可能将padding或上下文序列的统计规律误认为功能信号，在增强子活性预测中需检验模型对padding序列的依赖性。
- **迁移边界**：原论文聚焦零样本VEP分类任务，而我的任务是基于虚拟表观遗传特征预测增强子活性（序列到功能）。模型对侧翼序列的敏感性在增强子预测中的表现不能直接等同，需独立验证。
- **阅读时核实**：论文在测试侧翼序列敏感性时，具体是如何控制或生成这些中性上下文的？其长度和组成特征是否与常规模型输入的padding策略一致？

[原文](https://www.biorxiv.org/content/10.64898/2026.03.10.710786v1) · [DOI](https://doi.org/10.64898/2026.03.10.710786)

作者：Mathur, V., Sachidanandam, R.
来源标注的末位/通讯作者：Ravi Sachidanandam
机构：New York Medical College

### 英文摘要

DNA foundation models such as Evo2 and DNABERT-2 show promise for variant-effect prediction (VEP), yet rigorous benchmarks assessing their ability to capture established biological constraints remain limited. Here, we introduce controlled benchmarks based on well-characterized nuclear and mitochondrial sequence features. Although Evo2 achieves strong aggregate performance on mitochondrial variants (AUROC = 0.927), our analyses reveal systematic blind spots in short-range signals, including codon usage bias, as well as spurious sensitivity to biologically neutral sequence context. Notably, changes in flanking sequences can cause pathogenic tRNA variants to be misclassified as benign. These findings suggest that Evo2's predictive performance may rely more heavily on learned sequence regularities than on the biological constraints governing variant function, raising concerns about the clinical utility of zero-shot genomic foundation models.Our framework provides a principled basis for standardized model evaluation and for guiding the development of architectures better aligned with biological constraints.

---

## 3. A compact motif vocabulary is differentially interpreted across human cell types

bioRxiv · 预印本 · 2026-11-03 · 相关性 8/10

**研究关联：方法可借鉴**

- **为什么值得看**：开发可解释神经网络学习调控motif并预测跨细胞类型基因表达，与跨细胞类型增强子活性预测高度相关。
- **任务与验证范围**：输入：DNA序列（摘要未说明是否包含表观遗传特征） → 输出：跨116个人类生物样本的基因表达；研究物种/细胞体系：人类；验证范围：跨细胞类型泛化验证、ChIP-seq数据验证、基因组规模扰动验证。
- **核心方法**：CNN-CR，一种可解释的卷积神经网络，在跨多细胞类型预测基因表达的同时学习调控motif。
- **主要发现与证据**：几十个共享的motif家族即可保留大部分细胞类型特异性词汇的预测信息，并能跨细胞类型泛化；细胞环境通过染色质状态（决定motif可及性）和reader身份（决定可及motif的解读方式）两个层面调控基因表达。
- **可借鉴点（研究建议）**：该论文将细胞环境解耦为“染色质状态门控”和“reader身份解读”，这提示我在预测增强子活性时，可考虑将虚拟表观遗传特征作为门控机制，而非仅作为序列特征的简单拼接。
- **迁移边界**：原论文针对启动子调控和基因表达预测，且未涉及预训练模型的padding策略；其跨细胞类型泛化结论基于启动子motif词汇的压缩性，不能直接等同于增强子活性预测任务中的泛化能力。
- **阅读时核实**：CNN-CR模型在输入端是否仅使用DNA序列，还是结合了染色质可及性等表观遗传特征作为“染色质状态门控”的输入？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.01.763377v1) · [DOI](https://doi.org/10.64898/2026.11.01.763377)

作者：Shen, S., Wang, W.
来源标注的末位/通讯作者：Wei Wang
机构：University of California, San Diego

### 英文摘要

How a common genome generates diverse human cell types may depend less on distinct cis-regulatory vocabularies than on context-dependent use of a shared one. We have developed CNN-CR, an interpretable neural network that learns regulatory motifs while predicting gene expression across 116 human biosamples. Promoter regulation proves highly compressible: dozens of recurrent motif families retain most of the predictive information of much larger cell-type-specific vocabularies and generalize to cellular contexts excluded from their discovery. These motifs are conserved at their binding sites and enriched at fine-mapped regulatory variants. Cellular context acts at two levels: chromatin state gates which motif instances are available for regulatory use, whereas reader identity determines how accessible motifs are interpreted. ChIP-seq data reveal frequent shifts in reader occupancy across cell types, and genome-scale perturbations support corresponding context-dependent reader functions. Thus, regulatory diversity can emerge through differential access to and interpretation of a compact shared DNA vocabulary.

---

## 4. Unsupervised prioritization of gene-regulatory variants with isolation forests

bioRxiv · 预印本 · 2026-11-03 · 相关性 7/10

**研究关联：方法可借鉴**

- **为什么值得看**：使用孤立森林整合Enformer等深度学习模型的预测分数来优先排序调控变异，间接涉及sequence-to-function应用。
- **任务与验证范围**：输入：常见基因变异及Enformer模型的多维预测分数 → 输出：单一的基因调控变异优先级评分（eQIF）；研究物种/细胞体系：摘要未说明；验证范围：eQTL和GWAS变异，跨细胞类型情况摘要未说明
- **核心方法**：基于孤立森林的无监督机器学习方法，整合Enformer深度学习模型的多维输出为单一变异评分。
- **主要发现与证据**：eQIF在预测eQTL和基因调控GWAS变异上表现优异，高分变异富集于进化保守的TFBS足迹中且重现了基序信息内容；已预计算9,431,969个常见变异的评分并公开。
- **可借鉴点（研究建议）**：可考虑借鉴孤立森林方法来整合或降维预训练基因组学模型在序列不同位置或不同细胞类型上的多维输出，以提取核心功能特征。
- **迁移边界**：原论文聚焦于变异优先级排序，而我的任务是基于DNA序列预测增强子活性及虚拟表观遗传特征；孤立森林在此处的适用性依赖于Enformer输出特征的结构，不能直接假设其在增强子活性回归任务上同样有效。
- **阅读时核实**：Enformer输出的哪些具体特征维度被用作孤立森林的输入？这些输入是否涉及不同细胞类型的表观遗传特征？

[原文](https://www.biorxiv.org/content/10.64898/2026.10.29.762447v1) · [DOI](https://doi.org/10.64898/2026.10.29.762447)

作者：Schmidt, A. W., Rosendahl, J., Laumen, H., Ossowski, S.
来源标注的末位/通讯作者：Stephan Ossowski
机构：Institute of Medical Genetics and Applied Genomics, University of Tuebingen, Tuebingen, Germany

### 英文摘要

Most common variants occur in non-coding genomic regions. Numerous expression quantitative trait loci (eQTLs) can influence nearby gene expression. Across diverse traits and diseases, many genome-wide association study (GWAS) loci have been shown to colocalize with eQTLs, supporting gene-regulatory causal mechanisms. However, linkage disequilibrium (LD) obscures the identification of the causal variant(s), necessitating prioritization by functional annotations. Previously published variant prioritization tools relied on the machine-learning-based combination of diverse feature types like evolutionary conservation and chromatin information, whereas more recent deep learning tools learn and describe gene-regulatory DNA sequence grammar. However, the latter approaches often generate a large number of scores per variant. We designed a novel unsupervised machine-learning approach based on isolation forests to integrate the predictions from the broadly used Enformer deep learning model into a single gene-regulatory predictive score for each common variant. Our novel approach eQTL prediction with isolation forests (eQIF) demonstrates strong performance in predicting eQTLs and gene-regulatory GWAS variants. We show that top eQIF variants are located in evolutionarily conserved transcription factor binding site (TFBS) footprints, and that the frequency of top eQIF variants within overrepresented TFBS motifs recapitulates the motif information content. eQIF predictions are precomputed for 9,431,969 common variants and publicly available.

---

## 5. Top2All: Benchmarking sparse-to-transcriptome reconstruction from high-expression profiles across sex- and sex-steroid-defined conditions

bioRxiv · 预印本 · 2026-11-02 · 相关性 6/10

**研究关联：方法可借鉴**

- **为什么值得看**：使用预训练的Geneformer模型进行转录组重建，涉及基础模型在基因组数据上的表示学习和评估，与表观遗传/转录组基础模型的研究兴趣相关。
- **任务与验证范围**：输入：少量高表达基因的稀疏表达谱 → 输出：全转录组表达重建。物种/细胞体系：小鼠肾上腺束状带细胞。验证范围：8种性别/性类固醇条件，采用 replicate-wise out-of-fold 和 leave-one-condition-out 两种交叉验证策略，跨条件评估泛化。
- **核心方法**：基于 Mouse-Geneformer 预训练单细胞基础模型的稀疏到全转录组重建框架，对比条件感知与无条件两种建模策略，并引入最近邻检索作为基线。
- **主要发现与证据**：样本级相关性接近1，但简单参考谱同样达到高相关性；基因级评估才揭示方法间实质差异。条件信息未一致提升性能，说明条件信号已编码在稀疏输入中。最近邻检索优于学习式重建；增加输入基因数未单调改善性能。
- **可借鉴点（研究建议）**：该论文揭示的「样本级指标虚高、需基因级指标才能区分方法」这一评估陷阱，提示我在增强子活性预测中应警惕区域级/全局指标掩盖位点级差异，并建议引入强参考基线（如最近邻或均值谱）来检验预训练模型 padding 策略的真实增益。
- **迁移边界**：原论文为 RNA 表达谱重建任务（转录组→转录组），我的任务为 DNA 序列→增强子活性（sequence-to-function），输入模态与输出空间均不同。其评估方法论（多粒度指标、强基线、leave-one-condition-out）可迁移，但关于输入深度非单调改善、条件信息冗余等具体结论不可直接外推至序列模型或 padding 问题。
- **阅读时核实**：基因级评估中哪些基因类别或表达区间重建误差最大，且最近邻基线在基因级指标上优于学习式模型的具体幅度是多少——这关系到判断预训练模型在位点级预测中是否真正提供了超越检索的表达能力。

[原文](https://www.biorxiv.org/content/10.64898/2026.10.31.763361v1) · [DOI](https://doi.org/10.64898/2026.10.31.763361)

作者：Nishio, Y., Yamashita, T., Baba, T.
来源标注的末位/通讯作者：Takashi Baba
机构：Department of Molecular Biology, Graduate School of Medical Sciences, Kyushu University

### 英文摘要

Transcriptome-wide profiling at single-cell resolution is limited by sparse detection of gene expression, raising the question of how much transcriptomic information can be recovered from a small set of highly expressed genes. We developed Top2All, a Mouse-Geneformer-based framework for reconstructing transcriptome-wide expression from sample-specific sparse inputs. Using 24 cell-number-normalized RNA-seq profiles of mouse adrenal zona fasciculata cells across eight experimental conditions defined by sex and sex-steroid milieu, we evaluated condition-aware and no-condition models under replicate-wise out-of-fold and leave-one-condition-out validation. Top2All achieved near-unity sample-wise correlation with measured expression, but similarly high correlations were obtained using simple reference profiles, whereas gene-wise evaluation revealed substantially greater differences among methods. Explicit condition information did not consistently improve reconstruction, indicating that sex- and sex-steroid-associated condition information was already strongly encoded in the sparse expression profiles. Nearest-neighbor retrieval provided a stronger baseline than learned reconstruction, and input-depth analysis showed that increasing the number of input genes did not monotonically improve performance. These findings show that a relatively small set of highly expressed genes contains substantial information about transcriptomic state, while accurate reconstruction of gene-specific biological variation remains challenging. Sparse-to-transcriptome models should therefore be evaluated using gene-wise metrics, strong reference baselines, and tests of generalization beyond conditions represented during training.

---

中文笔记基于标题和摘要生成，未核验全文；研究建议不代表论文已验证的结论。相关性分数不是论文质量评分。

检索统计：窗口 [2026-11-01 00:00, 2026-11-04 00:00) UTC；抓取 biorxiv 139/pubmed 236 → 粗筛 41 篇 → LLM 选中 5 篇

> 抓取异常：arXiv 多次重试仍返回 HTTP 429，本期仅覆盖 PubMed 和 bioRxiv。本期可能不完整。