# Paper Scout 日报 2026-10-08

共筛选出 **10** 篇推荐论文。
📊 抓取 biorxiv 101/pubmed 75 → 粗筛 100 篇 → LLM 选中 10 篇

## 1. Limitations of Genomic Foundation Models for Decoding Regulatory Mechanisms in ALS

- **期刊**: bioRxiv
- **作者**: Talukder, A., Kaplan, A.
- **机构**: Arghamitra Talukder @ Columbia University
- **日期**: 2026-10-07
- **ID**: DOI: 10.64898/2026.10.01.756029  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.01.756029v1
- **相关分数**: 9/10
- **一句话推荐**: 评估AlphaGenome在解码调控机制和变异效应上的局限性，直接契合你对基因组基础模型性能评估的研究兴趣。
- **方法**: 零样本评估预训练基因组基础模型（AlphaGenome）在多层级调控机制解析中的能力与局限。
- **主要发现**: 该模型虽能识别少量高置信度局部调控变异，但无法准确恢复群体效应量、区分疾病相关组织特异性，且远距离变异到靶基因的归因能力随距离急剧衰减。
- **对我的启发**: 在评估预训练模型对游离型增强子活性的预测时，需特别关注其长距离调控信号归因能力随序列距离急剧衰减的缺陷，这提示模型的上下文窗口或padding设置对远距离效应捕获具有决定性影响。

<details><summary>Abstract</summary>

Genomic foundation models promise to infer regulatory consequences of genetic variants directly from DNA sequence, but how well these predictions translate to clinical utility remains unclear. To probe this question, we evaluate AlphaGenome (AG) for understanding amyotrophic lateral sclerosis (ALS) genetics without any disease-specific fine-tuning across three settings of increasing difficulty: recovering measured variant effects, reconstructing a known splicing mechanism, and generating de novo regulatory hypotheses at unresolved loci. At population scale, AG failed to recover measured effect sizes across 1,254 spinal-cord splicing quantitative trait loci (QTL) (Spearman = 0.041, Pearson = 0.104) and was precise only at negligible recall (precision = 1.00 at 1.3% recall). At a mechanistically resolved locus of UNC13A cryptic-exon event, AG predicted the intronic risk variant's splice-site usage opposite its known risk effect (Delta approx. -2 x 10^-6), showed near-identical effects in disease-relevant and disease-irrelevant tissues (cerebellar effects reached approximately 60% of neural magnitude), and recovered only a partial cis-regulatory signature. Finally, AG showed limited gene-level resolution across seven ALS genome-wide association study (GWAS) loci, with predicted effects declining sharply as a gene lay farther from the variant (a 10-fold increase in distance cost 0.95 standard deviations of signal; p = 2.7 x 10^-23). In summary, AG can identify a small set of high-confidence regulatory variants, but cannot reliably rank variants by biological effect, or assign regulatory signals to the correct effector gene at unresolved loci. Thus, although AG captures meaningful local regulatory effects, these predictions do not resolve the effect sizes and effector genes needed to connect ALS-associated variants to their causal mechanisms.

</details>

---

## 2. DeCTCF: Decoding CTCF binding sequences by leveraging predicted epigenomic features.

- **期刊**: PLoS computational biology
- **作者**: Lu Chai, Jie Gao, Tinghe Guo, Teer Ba, Zihan Li, Junjie Liu, Yong Wang, Lirong Zhang
- **机构**: Lirong Zhang @ School of Physical Science and Technology, Inner Mongolia University, Hohhot, China.
- **日期**: 2026-10-05
- **ID**: DOI: 10.1371/journal.pcbi.1014848  |  PMID: 42832579  |  URL: https://pubmed.ncbi.nlm.nih.gov/42832579/
- **相关分数**: 8/10
- **一句话推荐**: 利用预训练模型预测的表观基因组特征（虚拟特征）来解码调控元件（CTCF结合序列），与你的虚拟表观基因组特征预测项目直接相关。
- **方法**: 基于预训练序列模型（Sei）提取虚拟表观遗传特征，结合无监督聚类与多组学关联分析解析顺式调控元件功能模块。
- **主要发现**: 利用预测的表观遗传特征可将CTCF结合位点聚类为具有不同3D染色质结构和谱系特异性的功能模块，且其ChIP-seq信号峰型与染色质环偏好性显著相关。
- **对我的启发**: 启发我利用预训练模型输出的多维虚拟表观遗传特征作为中间表征，对不同细胞类型的游离型增强子进行无监督聚类以识别功能模块，而非仅限于端到端的活性预测。

<details><summary>Abstract</summary>

CTCF is a key architectural protein with diverse roles in genome organization and gene regulation, yet how it achieves these roles in different contexts remains unclear. Pretrained sequence-based models such as Sei provide predicted epigenomic features that can be used in downstream analyses of regulatory elements. Here, we developed DeCTCF, an integrative computational framework that uses pretrained Sei predictions to analyze 236,552 CTCF binding sequences by integrating CTCF ChIP-seq data from 118 human cell lines. By leveraging predicted epigenomic features from the Sei model, we grouped these CTCF binding sites into 20 clusters. These clusters can be annotated into distinct functional modules, including a major module associated with 3D chromatin architecture and three lineage-associated modules. The lineage-associated modules reveal associations between candidate co-factors and CTCF's context-dependent functions. For example, several clusters enriched in the three stem cell lines included in our dataset also showed enrichment of ZIC-family and were associated with gene sets related to pluripotency and neurodevelopment. We further observed associations between cluster-level CTCF ChIP-seq signal profiles and chromatin-loop annotations: single-peak profiles were reproducibly associated with higher loop interaction scores, whereas double- and triple-peak profiles showed distinct loop-pairing preferences. Overall, our study offers a systematic map of CTCF's modular organization by leveraging predicted epigenomic features and reveals context-associated regulatory patterns that underlie its regulatory diversity.

</details>

---

## 3. PIE: Generalizing perturbation effects across unseen perturbations, contexts and datasets

- **期刊**: bioRxiv
- **作者**: Verma, R., Adduri, A., Bevilacqua, B., Eraslan, B., Burke, D., Goodarzi, H., Roohani, Y.
- **机构**: Yusuf Roohani @ Arc Institute
- **日期**: 2026-10-05
- **ID**: DOI: 10.64898/2026.10.02.756297  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.02.756297v1
- **相关分数**: 8/10
- **一句话推荐**: 涉及单细胞扰动效应预测及跨未见上下文/数据集的泛化，与我的研究兴趣和跨细胞类型泛化问题高度相关。
- **方法**: 提出PIE模型，融合基线基因表达与外部生物知识等辅助输入，以群体水平扰动效应为优化目标预测基因差异表达。
- **主要发现**: PIE在跨未见上下文、扰动及数据集的泛化任务上全面达到SOTA，在联合未见上下文和扰动场景下，其AUPRC是最强基线的1.2至3.2倍。
- **对我的启发**: 在跨细胞类型预测增强子活性时，可借鉴PIE引入细胞特异性的基线表观遗传特征作为辅助输入，以提升模型对未见细胞类型的泛化能力。

<details><summary>Abstract</summary>

Predicting cellular response to perturbations is key to understanding biological mechanisms and selecting therapeutic targets. However, generalizing across cellular contexts, perturbations, and experimental datasets remains challenging due to incomplete representations of the system being perturbed and the difficulty of measuring true perturbation effects within that system. We introduce PIE, a model that addresses these limitations by reformulating the learning task around population level perturbation effects and incorporating auxiliary inputs that better characterize the biological system. PIE directly predicts differentially expressed genes and changes in gene expression for each (context, perturbation) pair, using external biological knowledge, baseline gene expression, and observed perturbation responses. Its architecture accommodates input sources with variable feature sets and predicts effects on genes seen and unseen during training. On the Replogle Nadig dataset, PIE achieves state of the art performance on most metrics across all tested generalization settings, including the most challenging setting where both the context and perturbation are unseen during training. For predicting differentially expressed genes, PIE achieves 1.2 to 3.2 times the AUPRC of the strongest baseline in each setting: across unseen contexts, perturbations, experimental datasets, and jointly unseen contexts and perturbations. Overall, PIE provides a framework for generalizing perturbation effects across diverse experimental conditions.

</details>

---

## 4. AntiCapt: Fine-Tuned Nucleotide Language Models for Predicting and Designing Anticancer Aptamers

- **期刊**: bioRxiv
- **作者**: Bajiya, N., Mehta, N. K., Raghava, G. P. S.
- **机构**: Gajendra P.S. Raghava @ Indraprastha Institute of Information Technology, Delhi (IIIT Delhi)
- **日期**: 2026-10-07
- **ID**: DOI: 10.64898/2026.09.28.754914  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.28.754914v1
- **相关分数**: 8/10
- **一句话推荐**: 使用微调的核苷酸语言模型（如HyenaDNA）进行序列功能预测和设计，与我的DNA语言模型和序列到功能研究兴趣高度相关。
- **方法**: 结合传统序列描述符与微调的核苷酸语言模型（如HyenaDNA）进行抗癌适配体序列的分类预测。
- **主要发现**: 微调的HyenaDNA嵌入在预测抗癌适配体上表现最佳（AUC 0.94），优于基于传统组成和结构特征的机器学习模型，且能有效区分抗癌适配体与一般适配体。
- **对我的启发**: 微调HyenaDNA在特定DNA序列功能预测上优于传统特征，启发我在增强子活性预测中对比微调预训练模型与传统表观遗传特征的性能，并关注HyenaDNA处理变长序列时的padding机制。

<details><summary>Abstract</summary>

Over the past decade, aptamers have emerged as promising therapeutics, with cancer therapeutics as a major research area. Existing computational methods, however, either predict aptamer-target pairs or design aptamers against a specific target. In this study, we present AntiCapt, a computational method for identifying single-stranded DNA (ssDNA) anticancer aptamers (ACAs) using sequence descriptors and fine-tuned nucleotide language models. The main dataset comprises 1,021 experimentally validated ACAs and an equal number of non-aptamer sequences. Comparative analysis revealed distinct patterns in the nucleotide, dinucleotide, and trinucleotide compositions associated with ACAs. We developed machine learning (ML) models using composition, autocorrelation, binary profiles and structural features. Among these, the best-performing composition-based model achieved an AUC of 0.93 on an independent dataset, while chemical descriptor-and structural feature-based models achieved a maximum AUC of 0.89. ML models using pretrained and fine-tuned NLM embeddings were also developed, with fine-tuned HyenaDNA embeddings achieving the highest performance, with an independent AUC of 0.94. Furthermore, we developed a model for discriminating anticancer aptamers from general aptamers. The best-performing models were integrated into AntiCapt, a web server and a standalone tool for predicting, designing, and genome-scale scanning anticancer aptamers (https://webs.iiitd.edu.in/raghava/anticapt/).

</details>

---

## 5. A generative language model decodes contextual constraints on codon choice for mRNA design

- **期刊**: bioRxiv
- **作者**: Faizi, M., Sakharova, H., Borrmann, H., Parsa, M. S., Lareau, L. F.
- **机构**: Liana F Lareau @ University of California, Berkeley
- **日期**: 2026-10-05
- **ID**: DOI: 10.1101/2025.05.13.653614  |  URL: https://www.biorxiv.org/content/10.1101/2025.05.13.653614v1
- **相关分数**: 7/10
- **一句话推荐**: 使用生成式编码器-解码器语言模型学习密码子选择并设计mRNA，与序列到功能预测及生物序列表示学习高度相关。
- **方法**: 基于编码器-解码器架构的生成式语言模型（Trias），在天然脊椎动物CDS序列上预训练以学习密码子选择的上下文约束。
- **主要发现**: 该模型无需显式的功能标签监督，其零样本预测即可与mRNA稳定性和蛋白产量高度相关，且生成的合成序列在实验中表现出优于现有方法的蛋白表达水平。
- **对我的启发**: 预训练语言模型能从纯序列中隐式捕捉长程上下文依赖与进化约束，这启发我们在增强子活性预测中探索生成式预训练模型对虚拟表观遗传特征及序列上下文约束的零样本建模能力。

<details><summary>Abstract</summary>

Synonymous codon choice affects mRNA fate and protein output, posing a challenge for mRNA technology. Design of therapeutic mRNAs requires a model that captures biological nuance from natural sequences while identifying constraints relevant to synthetic expression. We present Trias, a generative encoder-decoder language model trained on millions of vertebrate coding sequences that successfully designs mRNAs with high protein output. Trias learns codon usage rules directly from sequence data, integrating local and global dependencies to generate species-specific codon sequences that reflect biological constraints. Without explicit training on protein expression, its zero-shot predictions correlate strongly with experimental measurements of mRNA stability and protein output. Moreover, we show experimentally that novel sequences generated by Trias for a therapeutically relevant target produce more protein than existing methods, demonstrating that preferences learned from natural sequences can lead to high output from synthetic sequences. Released open source with full code and weights, Trias provides a reproducible framework for synthetic mRNA design that reveals molecular and evolutionary principles behind codon choice.

</details>

---

## 6. Pervasive Backdoor Vulnerabilities in Genomic Foundation Models

- **期刊**: bioRxiv
- **作者**: Ni, S., Wang, Q., Wei, C. et al. (12 authors)
- **机构**: Min Yang @ Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences
- **日期**: 2026-10-05
- **ID**: DOI: 10.64898/2026.07.30.741642  |  URL: https://www.biorxiv.org/content/10.64898/2026.07.30.741642v1
- **相关分数**: 6/10
- **一句话推荐**: 探讨基因组基础模型和DNA语言模型在微调过程中的后门漏洞，属于基础模型安全性研究。
- **方法**: 针对基因组基础模型微调阶段的后门攻击及基于局部单核苷酸突变敏感性的两阶段无监督审计框架。
- **主要发现**: 微调时仅需投毒少量短DNA motif即可在多种架构和规模的模型中植入高成功率后门且不损及正常性能，模型规模无法防御，但可通过预测的局部突变敏感性检测出投毒序列。
- **对我的启发**: 在评估预训练模型padding对增强子活性预测的影响时，可借鉴其单核苷酸突变敏感性分析方法，审计padding序列是否作为短DNA motif引入了非预期的预测偏差或后门效应。

<details><summary>Abstract</summary>

Genomic foundation models are revolutionizing biological research and biotechnology, yet their vulnerability to data poisoning remains poorly characterized. Here we show that backdoor attacks can be reliably implanted during fine-tuning across diverse model architectures, tasks and model scales by poisoning only a small fraction of training data with short DNA motifs, including triggers derived from transposon terminal inverted repeats (TIRs). Attack success rates are generally high across encoder-based and autoregressive models, while clean-task performance remains almost unchanged. Increasing model scale does not confer measurable resistance. To detect such threats, we develop a two-stage auditing framework that flags potentially poisoned sequences through localized single-nucleotide mutation sensitivity in model predictions, without prior knowledge of trigger sequences. These results identify downstream fine-tuning as an attack surface for genomic foundation models and motivate stronger data provenance, adversarial evaluation and post-training security auditing.

</details>

---

## 7. Slide-level batch structure limits histology-guided supervision of transcriptomic foundation models

- **期刊**: bioRxiv
- **作者**: McConnell, U., Nonchev, K., Koelzer, V. H., Raetsch, G.
- **机构**: Kalin Nonchev @ ETH Zurich
- **日期**: 2026-10-05
- **ID**: DOI: 10.64898/2026.09.30.755585  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.30.755585v1
- **相关分数**: 6/10
- **一句话推荐**: 评估空间转录组学基础模型的跨模态监督效果，涉及基础模型的表示局限性和批次效应。
- **方法**: 评估H&E组织学作为训练期监督信号对空间转录组学基础模型表征学习的跨模态引导效果。
- **主要发现**: 玻片级批次效应主导了基因表达嵌入，导致组织学引导的跨模态监督无法恢复预训练表征中未保留的生物学信息，反而广泛降低了基因预测能力。
- **对我的启发**: 评估预训练基因组学模型时需警惕padding等非生物学特征对表征的主导作用，跨模态或辅助监督仅能重组已有信息而无法弥补表征固有缺陷。

<details><summary>Abstract</summary>

Spatial transcriptomics pairs spatially resolved gene expression with tissue morphology in the same tissue section. Transcriptomic foundation models encode such expression profiles into general-purpose representations, but these representations can retain slide- and cohort-specific variation that obscures biological signal. Here, we test whether matched H\&E histology can improve these representations as a training-time supervisory signal that is discarded at inference. Across three transcriptomic foundation models, histology-guided supervision provides no consistent aggregate improvement in cross-donor annotation transfer, despite substantially stronger transfer from histology alone. We find that gene-expression embeddings from spot-based spatial transcriptomics are low-dimensional and strongly structured by slide identity, limiting the shared gene--morphology signal available for cross-modal transfer. Guidance benefits some morphologically distinctive classes but reduces held-out gene predictivity broadly across the transcriptome. These results suggest that cross-modal supervision can reorganize information already encoded in a frozen representation but cannot recover information the representation does not retain, highlighting the importance of diagnosing slide-specific structure before applying such supervision. Code availability: https://github.com/ratschlab/vision-guided-transcriptomics-fm-2026

</details>

---

## 8. How many cells resolve a perturbation direction? A closed-form, control-aware cell quota for single-cell perturbation screens

- **期刊**: bioRxiv
- **作者**: Tran, L. T. H., Nguyen, V. T.
- **机构**: Loc Thai Huu Tran @ Hong Hung Hospital
- **日期**: 2026-10-05
- **ID**: DOI: 10.64898/2026.10.02.754788  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.02.754788v1
- **相关分数**: 5/10
- **一句话推荐**: 为单细胞扰动筛选提供了确定所需细胞数量的理论框架，与你的单细胞扰动研究兴趣间接相关。
- **方法**: 基于噪声各向异性推导闭式细胞配额公式，结合Lean 4机器验证，用于控制单细胞扰动方向估计的角误差。
- **主要发现**: 扰动方向的角误差主要由垂直于效应的噪声和对照池规模决定；在多个公共图谱中，多数扰动条件受对照池规模限制而非处理细胞数不足。
- **对我的启发**: 论文中区分噪声方向（平行于效应仅改变长度，垂直于效应改变方向）的思路，可启发在评估预训练基因组学模型padding对增强子序列表征的影响时，量化padding噪声是改变特征向量的幅度还是方向。

<details><summary>Abstract</summary>

Single-cell perturbation screens increasingly infer mechanism from the direction of a treatment's displacement in a shared transcriptomic embedding, yet no sample-size rule states how many cells that direction needs. We derive a closed-form, anisotropic cell quota for the treated cells required to hold the angular error of an estimated perturbation direction at a chosen tolerance. Because noise aligned with the effect changes only its length, the quota depends on the noise perpendicular to the effect, on the effect magnitude and on the control-pool size, and it diverges below a magnitude floor set by the control alone. The deterministic core is machine-checked in Lean 4. Across four public atlases (six screens) reprocessed through one embedding, the per-cell noise variance is near 1.0 on chemical and genome-wide genetic platforms. On Tahoe-100M, referenced to its plate-shared DMSO vehicle of about 3,100 cells, 55% of 56,827 conditions are control-pool-limited and only 11% are over-sampled at a 5.7-degree tolerance. Genome-wide CRISPRi knockdowns are instead detection- and depth-limited. A downsample-and-measure test on every atlas recovers the parameter-free angular-error slope. The calculator turns a pilot covariance, an effect magnitude and a control design into a per-condition cell budget and flags conditions that no treated depth can resolve.

</details>

---

## 9. methylTFR: Computational quantification of transcription factor activity from DNA methylation

- **期刊**: bioRxiv
- **作者**: Gunduz, I. B., Nitsch, R., Murugan, S. K., Mueller, F.
- **机构**: Fabian Mueller @ Saarland University
- **日期**: 2026-10-05
- **ID**: DOI: 10.64898/2026.09.29.755279  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.29.755279v1
- **相关分数**: 5/10
- **一句话推荐**: 利用DNA甲基化数据计算量化转录因子活性，涉及表观遗传特征与细胞类型特异性调控。
- **方法**: 提出methylTFR算法，基于转录因子结合位点周围的DNA甲基化模式，通过统计推断量化并降维提取低维可解释的TF活性谱。
- **主要发现**: 该方法能从bulk及单细胞甲基化组中有效识别细胞类型特异性的TF活性，并可与基因表达及染色质可及性数据整合，揭示细胞谱系发育的调控机制。
- **对我的启发**: 在构建基于虚拟表观遗传特征的增强子活性预测模型时，可借鉴其将位点特异性甲基化信号转化为低维TF活性特征的方法，作为预训练序列模型的辅助特征或解释性中间表征。

<details><summary>Abstract</summary>

DNA methylation modulates transcription factor (TF) binding, and plays an important role in regulating gene expression. We developed methylTFR, an R package for quantifying TF activity from DNA methylation across TF-binding sites, providing a low-dimensional and interpretable activity profile. Across 147 human immune cell methylomes, methylTFR identified cell-type-specific regulators, including CEBP and ETS family activity in myeloid cells. In CD4+ T cells, TF activity scores resolved the naive-to-memory trajectory and highlighted AP-1 factors as important memory regulators. We applied methylTFR to sparse single-cell methylome data, and we integrated derived activity scores with gene expression and accessibility into joint factor models yielding multimodal views of lineage regulators.

</details>

---

## 10. sORF-Trans2MS: a two-module deep learning framework for sORF translation and MS-supported microprotein prediction

- **期刊**: bioRxiv
- **作者**: He, J., Sui, J., Chen, Q., Hu, H., Tan, C. S. H.
- **机构**: Chris Soon Heng Tan @ Southern University of Science and Technology
- **日期**: 2026-10-06
- **ID**: DOI: 10.64898/2026.09.29.755517  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.29.755517v1
- **相关分数**: 5/10
- **一句话推荐**: 使用预训练RNA语言模型（RNA-FM）和Transformer进行序列到功能（sORF翻译）预测，与你的representation learning兴趣间接相关。
- **方法**: 结合RNA-FM与ESM-2预训练表征，采用Transformer和多尺度CNN构建的双模块深度学习预测框架。
- **主要发现**: 该框架有效提升了核糖体支持的sORF翻译预测的泛化能力，并成功扩展至质谱支持但无核糖体数据的微蛋白预测；消融分析揭示了上游RNA上下文及蛋白N端的关键作用。
- **对我的启发**: 论文通过消融分析精确定位了上游RNA上下文的关键区域（AUG前50nt），这启发我在评估预训练基因组学模型padding时，可设计类似实验量化特定上下文窗口长度对增强子活性预测的贡献。

<details><summary>Abstract</summary>

Ribosome profiling is widely used to identify translated small open reading frames (sORFs), but existing prediction models often generalize poorly to newly collected sORF datasets. In addition, many microproteins with strong mass spectrometry (MS) evidence lack support in public Ribo-seq resources, suggesting that Ribo-supported sORF and MS-supported microprotein detection may represent complementary prediction tasks. Here, we developed sORF-Trans2MS, a two-module deep learning framework for predicting Ribo-supported sORFs and MS-supported microproteins. Module I uses RNA-FM representations for upstream, ORF, and downstream regions with a Transformer encoder for Ribo-supported sORF translation prediction. Module II integrates pretrained RNA-FM representations of RNA context with ESM-2 protein representations using multi-scale CNN encoders for predicting translated microproteins supported by MS but not Ribo-seq data. Module I was trained on 9,579 Ribo-supported sORFs and matched background sORFs, while Module II used 14,697 MS-supported (MS++Ribo-) microproteins and matched backgrounds. Module I achieved an AUROC of 0.870 internally and 0.930 on an independent GENCODE dataset. Ablation analysis highlighted upstream RNA context, including a distinct signal around 50 nt upstream of AUG. Module II achieved an AUROC/AUPR of 0.804/0.797 internally and 0.785/0.773 on an independent mass spectrometry dataset. Model interpretation highlighted upstream RNA context and the protein N terminus, while literature-supported microproteins further illustrated the complementary roles of the two modules. Overall, sORF-Trans2MS improves prediction and generalization of Ribo-supported sORFs and extends computational discovery to MS-supported candidates that are not represented in current public Ribo-seq resources.

</details>

---
