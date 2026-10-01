# Paper Scout 日报 2026-10-01

共筛选出 **8** 篇推荐论文。
📊 抓取 biorxiv 137/pubmed 60 → 粗筛 39 篇 → LLM 选中 8 篇

## 1. Evo 2 as a classification machine: evidence from in-context learning and mechanistic interpretability

- **期刊**: bioRxiv
- **作者**: Bertolini Agnoletto, L., Curion, F., Petrillo, M., Leoni, G., Ronco, M., Ruiz Serra, V., Consoli, S., Ceresa, M.
- **机构**: Lorenzo Bertolini Agnoletto @ European Commission, Joint Research Centre (JRC)
- **日期**: 2026-09-30
- **ID**: DOI: 10.64898/2026.09.30.755330  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.30.755330v1
- **相关分数**: 8/10
- **一句话推荐**: 直接研究基因组语言模型Evo 2的上下文学习能力与机制可解释性，与我的DNA语言模型/基因组基础模型研究兴趣高度契合。
- **方法**: 基于Evo 2基因组语言模型的上下文学习（ICL）范式，结合logit-lens和Jacobian Scope进行机制可解释性分析。
- **主要发现**: Evo 2在短序列二分类任务中具备上下文学习能力，但在千碱基长序列上性能崩溃且模型扩大无益；机制分析表明模型可能依赖提示结构而非内容信号。
- **对我的启发**: 预训练基因组学模型在长序列（如增强子）任务上存在性能崩溃风险，且可能依赖输入结构而非生物学信号，提示在增强子活性预测中需深入评估padding和序列长度对模型机制的真实影响。

<details><summary>Abstract</summary>

In-context learning (iCL) is an emergent capability of Large Language Models (LLMs), allowing them to perform new tasks at inference time using prompt-injected examples. While extensively studied in LLMs, the boundaries of its capabilities and underlying mechanisms remain poorly characterised in genomic Language Models (gLMs). Here, we map the operating regime of Evo 2, a nucleotide-level foundation gLM, across five binary classification tasks spanning biological and artificial sequences. We observe robust iCL on shorter natural sequences (F1=0.902 for miRNA, 0.785 for Toxins), degrading with sequence length, and collapsing at kilobase scale. Strikingly, we find no benefit in model scaling, as the 7B model systematically outperforms the 40B variant. We further find that perplexity, a widely used gLM performance proxy, poorly predicts accuracy. Mechanistic interpretability reconciles these observations: the logit-lens profiling suggests a prediction-generalisation trade-off, while Jacobian Scope indicates models might track prompts' structure rather than the signal-carrying content.

</details>

---

## 2. Disease relevance and replicability of deep learning gene expression prediction

- **期刊**: bioRxiv
- **作者**: Zhang, A., Tasaki, S., Connell, D., Ng, B., Gaiteri, C.
- **机构**: Chris Gaiteri @ SUNY Upstate
- **日期**: 2026-09-29
- **ID**: DOI: 10.64898/2026.09.24.753534  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.24.753534v1
- **相关分数**: 8/10
- **一句话推荐**: 系统评估了从DNA序列预测基因表达的DL模型在疾病和跨组织场景下的性能退化，与你的细胞类型特异性调控预测研究直接相关。
- **方法**: 对深度学习基因表达预测模型进行疾病相关性评估与代码可复现性基准测试。
- **主要发现**: 现有深度学习模型的高预测性能主要源于捕获基因表达的“开/关”双峰分布，而非疾病相关的精细表达水平变化，且存在代码与报告性能不一致的问题。
- **对我的启发**: 在评估预训练基因组学模型预测增强子活性时，需警惕模型是否仅捕获了基础的“开/关”状态，应设计更精细的评估指标以验证其在不同细胞类型间细微活性差异上的真实预测能力。

<details><summary>Abstract</summary>

Recent deep learning (DL) models predict average gene expression levels from DNA sequences with high overall correlation to measured values. We examine these DL models through the lens of disease research. The seemingly high overall performance of DL models is largely due to capturing whether genes are "On" or "Off", and to a lesser extent, disease-relevant expression level changes for "On" genes. Indeed, the more bimodal the gene expression distribution, the better the reported performance. We track the extent of this issue across tissues, molecular systems, and cancers. Compounding the model evaluation issue, we find inconsistencies between the published code and reported performance, highlighting the importance of versioning and publishing performance evaluation code. These findings indicate that the high reported performance of popular DL models falls unexpectedly short in disease applications, and that the problem of personalized genomic prediction remains far from solved in a disease context.

</details>

---

## 3. Generative modeling reveals the connection between nuclear morphology and gene expression

- **期刊**: bioRxiv
- **作者**: Wen, S., Vinas, R., Bues, J. et al. (13 authors)
- **机构**: Maria Brbic @ EPFL
- **日期**: 2026-09-30
- **ID**: DOI: 10.64898/2026.01.22.700673  |  URL: https://www.biorxiv.org/content/10.64898/2026.01.22.700673v1
- **相关分数**: 5/10
- **一句话推荐**: 用生成模型连接核形态与基因表达，涉及跨模态表征学习与单细胞数据，与virtual cell概念间接相关。
- **方法**: 基于超大规模细胞核图像预训练的双向跨模态生成模型（COSMIC），用于联合建模单细胞转录组与细胞核形态。
- **主要发现**: 该模型能定量解析基因表达与细胞核形态间的双向信息流，并在癌症耐药性和胚胎发育中成功识别出受微环境影响的形态-表达协同变化基因。
- **对我的启发**: 无明显直接启发

<details><summary>Abstract</summary>

How transcriptional programs shape nuclear morphology, and how morphological features in turn reflect and influence cell identity and function, remains poorly understood. Here, we introduce COSMIC, a bidirectional generative framework that enables quantitative decomposition of transcriptional variance reflected in nuclear morphology and morphological variance explained by gene expression. Pretrained on over 21 million segmented nuclei, COSMIC models cross-modal relationships by using a multimodal dataset acquired with IRIS, a technology that captures high-resolution images and transcriptomes from the same single cells. COSMIC learns relationships between gene expression and nuclear morphology, enabling the identification of genes whose expression covaries with nuclear morphological variation. In prostate cancer cells, COSMIC distinguishes chemotherapy-responsive and -resistant cell states through coordinated morphological and transcriptional changes, revealing morphology-associated genes linked to tumour state. Applied to spatial transcriptomics of zebrafish embryogenesis, COSMIC reveals how local cellular neighborhoods influence morphology-expression relationships. These results demonstrate that generative modeling powered by paired single-cell measurements can quantify the information shared between nuclear morphology and gene expression, opening new avenues for mechanistic discovery in both basic and translational cell biology.

</details>

---

## 4. Snurportin-1 maintains muscle niche integrity and myogenic progenitor homeostasis

- **期刊**: bioRxiv
- **作者**: Saracoglu, H. P., Nashabat, M., Kutlu, D. N. et al. (10 authors)
- **机构**: Nathalie Escande-Beillard @ Koc University School of Medicine
- **日期**: 2026-09-29
- **ID**: DOI: 10.64898/2026.09.24.749599  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.24.749599v1
- **相关分数**: 5/10
- **一句话推荐**: 结合单细胞转录组与机器学习进行变异功能机制分类，与变异效应预测和单细胞扰动有间接关联。
- **方法**: 构建斑马鱼基因敲除模型结合转录组学分析探究肌肉稳态调控机制。
- **主要发现**: SPN1缺失会导致广泛的剪接异常和转录失调，进而破坏细胞外基质与肌源性祖细胞稳态，引发肌营养不良表型。
- **对我的启发**: 无明显直接启发

<details><summary>Abstract</summary>

Loss-of-function variants in SNUPN, encoding the nuclear import factor Snurportin-1 (SPN1) required for spliceosomal small nuclear ribonucleoprotein (snRNP) transport, cause a recently described form of limb-girdle muscular dystrophy (LGMD). However, the role of SPN1 in skeletal muscle homeostasis remains poorly understood, in part due to the lack of a suitable in vivo model. Here, we generated a zebrafish snupn loss-of-function model that recapitulates key features of the skeletal muscle phenotype observed in patients. Mutant larvae developed severe locomotor impairment by 6 days post-fertilization (dpf), accompanied by sarcomeric disorganization and impaired muscle fiber integrity. Transcriptomic profiling at 6 dpf revealed widespread alternative splicing and transcriptional dysregulation, with prominent alterations in extracellular matrix and basement membrane components, together with upregulation of stress- and inflammation-associated genes. Notably, these late-stage abnormalities were preceded by disruption of the muscle progenitor population at 2 dpf, with reduced Pax7 progenitor abundance and myogenic gene expression together with altered muscle differentiation and organization. Together, these findings identify SPN1 as a key regulator of skeletal muscle homeostasis linking RNA processing to extracellular niche integrity and myogenic progenitor maintenance. This zebrafish model provides an in vivo platform for dissecting LGMD-associated disease mechanisms and developing therapeutic strategies aimed at restoring muscle function and regenerative capacity.

</details>

---

## 5. A moving target: non-stationary selection governs unsupervised prediction of viral fitness

- **期刊**: bioRxiv
- **作者**: Aris-Brosou, S., Vilain, M.
- **机构**: Stephane Aris-Brosou @ University of Ottawa
- **日期**: 2026-09-30
- **ID**: DOI: 10.64898/2026.09.17.752359  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.17.752359v1
- **相关分数**: 4/10
- **一句话推荐**: 评估蛋白质语言模型在变异效应预测上的表现，与基因组基础模型评估及序列到功能有间接关联。
- **方法**: 构建组合式无监督流程，结合蛋白质语言模型与多序列比对模型评估病毒突变适应度。
- **主要发现**: 预训练蛋白质语言模型在病毒适应度预测上受限于训练数据分布偏差和进化非平稳性（时间漂移），简单比对模型在病毒抗原蛋白上表现更优；比对的时间段是预测准确率的关键决定因素。
- **对我的启发**: 评估预训练基因组学模型预测增强子活性时，需警惕预训练语料库分布偏差对特定细胞类型或序列家族预测的影响，并应与简单基线模型进行对比验证。

<details><summary>Abstract</summary>

Anticipating how mutations change viral fitness is central to genomic surveillance and vaccine design, yet the supervised phenotype data behind the most accurate variant-effect predictors are unavailable for most emerging pathogens. We ask how far label-free scoring can go using only sequences, their evolutionary history, and structure. We assemble a modular, fully unsupervised pipeline that estimates a few interpretable terms (intrinsic replicative fitness, antigenic escape, and realized growth), and that lets each term be produced by more than one estimator, so the estimator itself becomes a testable modeling choice. Benchmarking the intrinsic term on 21 viral deep-mutational-scanning assays from ProteinGym, we find that a 650-million-parameter single-sequence protein language model predicts viral mutational fitness weakly and heterogeneously (mean Spearman 0.15), whereas a trivial site-independent alignment model more than doubles it (0.39, better on 17 of 21 assays), with the largest gains on the antigenic surface proteins where the language model fails. Yet the ordering reverses across 186 non-viral ProteinGym assays, where the language model instead exceeds the alignment model, localizing the weakness to viral families under-represented in the model's training data. Alignment-conditioned language models (MSA Transformer, Tranception) recover this accuracy but do not clearly exceed the simple alignment, so the decisive feature is the family alignment, not model scale or architecture. Our central result is evolutionary. Using dated samples of SARS-CoV-2 spike and influenza H3N2 hemagglutinin, we show that the epoch of the alignment is itself a leading, virus-specific determinant of accuracy. This traces to non-stationary selection: the site-specific amino-acid preferences drift over time, abruptly for spike at the emergence of Omicron and gradually for H3N2 hemagglutinin. A phylogenetic mutation-selection estimator does not match the far cheaper alignment model, falling significantly below it on matched data. Unsupervised viral fitness prediction is, then, as much an evolutionary problem as a modeling one.

</details>

---

## 6. MGM2 as a Multimodal Foundation Model for Microbial Community States and Responses

- **期刊**: bioRxiv
- **作者**: Zhang, H., Zhang, Y., Qi, Y., Liu, T., Zhao, L., Yang, R., Ning, K.
- **机构**: Kang Ning @ Huazhong University of Science and Technology
- **日期**: 2026-09-30
- **ID**: DOI: 10.64898/2026.07.20.739063  |  URL: https://www.biorxiv.org/content/10.64898/2026.07.20.739063v1
- **相关分数**: 4/10
- **一句话推荐**: 整合DNA语言模型表示的多模态基础模型，与基因组基础模型和表示学习有一定交集。
- **方法**: 融合DNA语言模型表征、丰度数据与文本描述的多模态基础模型预训练及下游微调范式。
- **主要发现**: 大规模预训练的冻结表征在跨项目微生物群落状态及药物干预效应预测中表现出色，且通过稀疏分解成功解析了分类学、生态学等可解释特征。
- **对我的启发**: 借鉴其利用稀疏分解解析多模态表征的思路，可用于剥离并解释预训练基因组学模型中padding序列及虚拟表观遗传特征对增强子活性预测的具体贡献。

<details><summary>Abstract</summary>

Microbial communities sustain ecosystems and influence host health, yet connecting their molecular diversity to responses under intervention remains difficult. Here we introduce MGM2, a multimodal foundation model integrating DNA language-model representations of microbial sequences, quantitative abundances and sample descriptions. After pretraining on 1.8 million microbiomes, its frozen representations achieved a mean macro-AUROC of 0.91 on later MGnify projects absent from pretraining. These representations also supported fecal microbiota transplantation outcome prediction, recovering 68% of observed high-change taxa. Adding molecular structures enabled prediction of drug effects in nested five-fold evaluation, while measured perturbed states informed subsequent recovery. To interpret the learned representations, sparse decomposition resolved taxonomic, ecological and abundance-related features. Together, these results show how a shared representation of molecular identity and community context connects large-scale microbiome learning to the prediction and interpretation of community change.

</details>

---

## 7. CycloCross: Adversarial single-cell RNA-seq data translation across species

- **期刊**: bioRxiv
- **作者**: Hacquard, O., Tokuta, Y., Imoto, Y., Nakamura, T., Deguchi, S., Nagano, M., Saitou, M., Hiraoka, Y.
- **机构**: Olympio Hacquard @ Kyoto University
- **日期**: 2026-09-30
- **ID**: DOI: 10.64898/2026.09.24.754263  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.24.754263v1
- **相关分数**: 4/10
- **一句话推荐**: 基于生成对抗网络的跨物种单细胞数据翻译，与单细胞计算和虚拟细胞概念有间接关联。
- **方法**: 基于CycleGAN架构的跨物种单细胞转录组数据对抗性翻译模型。
- **主要发现**: 无需先验基因对应关系即可实现跨物种scRNA-seq数据的高效真实翻译，保留时间动态并支持缺失时间点的表达插值与外推。
- **对我的启发**: 利用真实数据而非纯噪声的对抗翻译范式，可启发跨细胞类型虚拟表观遗传特征及增强子活性的迁移预测与缺失状态补齐。

<details><summary>Abstract</summary>

Single-cell RNA sequencing (scRNA-seq) has transformed our understanding of cellular heterogeneity, yet most datasets are limited to a handful of model organisms, leaving critical gaps in cross-species biology. Existing computational methods for integrating multi-species scRNA-seq data often rely on one-to-one ortholog mapping, which fails to account for gene duplications, losses, or functional divergences. To address these challenges, we introduce CycloCross, an adversarial method based on the CycleGAN architecture, designed to translate scRNA-seq data between species without requiring a priori gene correspondences. Unlike generative models that synthesize data from noise, CycloCross leverages real data from a source species, enabling more realistic and data-efficient translations. We demonstrate its effectiveness in germ cell development, translating data between mouse, macaque, and human with conserved yet divergent transcriptional programs. CycloCross not only preserves temporal dynamics but also enables interpolation and extrapolation of gene expression at missing time points, offering predictions for experimentally inaccessible states. Furthermore, CycloCross generates biologically plausible samples even with limited data, outperforming traditional generative models.

</details>

---

## 8. CHACAM: a cell-cell interaction-guided hierarchical attention model for high-precision cell identity annotation of scRNA-seq data in early C. elegans embryogenesis

- **期刊**: bioRxiv
- **作者**: Chen, X., Ju, X., Murali, M., Li, H., Chen, M., Zhang, M. Q.
- **机构**: Michael Q Zhang @ The University of Texas at Dallas
- **日期**: 2026-09-30
- **ID**: DOI: 10.64898/2026.09.24.754260  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.24.754260v1
- **相关分数**: 4/10
- **一句话推荐**: 使用分层注意力模型进行单细胞转录组数据的细胞身份注释，属于AI4LifeScience，对单细胞表征学习有间接启发。
- **方法**: 结合配体-受体互作网络与细胞接触图的监督式分层注意力模型
- **主要发现**: 通过学习细胞间接触特征及参考细胞三角化策略，有效解决了早期胚胎单细胞转录组中近缘亚谱系细胞因转录组相似导致的注释模糊问题。
- **对我的启发**: 无明显直接启发

<details><summary>Abstract</summary>

Accurate cell identity annotation is essential for reconstructing cell lineages and gene-regulatory networks in embryogenesis. However, in Caenorhabditis elegans (C. elegans) single-cell RNA-sequencing (scRNA-seq) atlases, closely related sub-lineage cells often have near-identical transcriptomes, leading to merged labels and limiting downstream analyses. We present CHACAM (Cell-Cell Interaction-guided Hierarchical Attention-based Cell Allocation Model), a supervised machine learning framework that integrates gene expression, a curated C. elegans ligand-receptor (L-R) interaction database, and a high-resolution cell contact map to refine cell annotations. CHACAM learns interpretable "interaction signatures" that distinguish contacting vs. non-contacting neighbors and applies a triangulation strategy using reference cells to resolve ambiguous sister identities. Applied to the Tintori and Cole-Yanai embryo atlases, CHACAM achieves near-perfect annotation accuracy, resolving longstanding ambiguities of the AB lineage and other lineages. The model also identifies new discriminative marker genes and provides mechanistic hypotheses linking contact-specific signaling to fate specification.

</details>

---
