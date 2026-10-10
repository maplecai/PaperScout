# Paper Scout 日报 2026-10-10

共筛选出 **8** 篇推荐论文。
📊 抓取 biorxiv 121/pubmed 57 → 粗筛 27 篇 → LLM 选中 8 篇

## 1. Cerberus: bidirectional state space blocks improve accuracy and efficiency of regulatory sequence models

- **期刊**: bioRxiv
- **作者**: Kelley, D. R., Yuan, H., Huang, X., Linder, J.
- **机构**: David R Kelley @ Calico Life Sciences LLC
- **日期**: 2026-10-09
- **ID**: DOI: 10.64898/2026.10.02.756377  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.02.756377v1
- **相关分数**: 9/10
- **一句话推荐**: 提出基于双向状态空间模型的序列到功能预测架构Cerberus，直接改进了Borzoi等基因组功能预测模型。
- **方法**: 采用基于Mamba-2的双向状态空间模型（Hydra）替换Transformer自注意力机制，构建卷积-SSM架构的序列到功能预测模型。
- **主要发现**: 线性复杂度的双向SSM在大幅提升长序列处理效率的同时，以更高分辨率实现了比Transformer模型更准确的调控活性及变异效应预测，且模型交互范围随网络深度显著扩展。
- **对我的启发**: 可探索用双向状态空间模型替代Transformer处理长序列，以缓解预训练基因组学模型中padding引入的噪声与计算冗余，从而更精准地捕捉游离型增强子的长程调控相互作用。

<details><summary>Abstract</summary>

Sequence-to-function models predict regulatory activity and variant effects from DNA sequence alone, and leading models such as Borzoi compute long-range interactions with self-attention. The reference genome caps unique training sequences, and new assays add labels, not sequences. This constraint favors architectures that learn more from limited sequence diversity. We compared long-range blocks with the rest of the architecture and the training data held fixed, replacing Borzoi's transformer blocks with Hydra, a bidirectional state space block built on Mamba-2. Hydra blocks ran 5.7-fold faster on 8,192-token inputs, and models built on them predicted binned coverage on held-out sequences and classified fine-mapped eQTLs more accurately. Hydra's linear cost in sequence length let us run the blocks at 32 bp resolution and remove the U-net decoder, leaving a convolution-SSM model smaller and more accurate than the one it replaced. Scaling this architecture up on an augmented track collection produced Cerberus, an ensemble of eight models over 786 kb of input. We evaluated it on GTEx v11 fine-mapped eQTL, sQTL, and paQTL benchmarks with negatives matched on allele frequency, gene expression, and phenotype-specific positional annotations to reduce confounding by these properties. Cerberus is more accurate than Borzoi on all three phenotypes, 0.692 versus 0.668 mean eQTL AUPRC across 48 tissues, and estimates eQTL effect sizes better, 0.379 versus 0.321 Spearman $\rho$. Against AlphaGenome, it trades leads in eQTL classification, ahead on variants 3 to 100 kb from the transcription start site and behind in coding sequence and within 3 kb. Interpretation of the trained blocks shows interaction range growing with block depth, from a 0.9 kb median half-life in the first block to 79 kb in the seventh, and the deepest heads anchoring on promoters, enhancers, and CTCF peaks. We release the models, the training data, the training and evaluation code, and the benchmark sets, supporting variant scoring and transfer learning.

</details>

---

## 2. gRely: Relyability for genome trained sequence-to-expression models

- **期刊**: bioRxiv
- **作者**: Rafi, A. M., Eraslan, G., Fletez-Brant, K.
- **机构**: Kipper Fletez-Brant @ Genentech
- **日期**: 2026-10-08
- **ID**: DOI: 10.64898/2026.05.23.727431  |  URL: https://www.biorxiv.org/content/10.64898/2026.05.23.727431v1
- **相关分数**: 9/10
- **一句话推荐**: 提出gRely元模型框架评估序列到功能模型（如Borzoi, AlphaGenome）变异效应预测的可靠性，直接相关于基因组基础模型评估。
- **方法**: 提出gRely，一种基于目标变异、基因及模型输出等多维特征的元学习框架，用于量化序列到功能模型变异效应预测的可靠性。
- **主要发现**: 该框架在低效应量区域仍能高精度识别可靠的变异预测，其判别依据从预测效应量转变为基因表达水平和跨重复信号浓度，且可跨模型架构泛化。
- **对我的启发**: 在评估预训练模型padding对增强子活性预测的影响时，可借鉴gRely的元学习思路，构建基于模型输出和序列特征的置信度评估框架，以区分不同padding策略下预测结果的可靠性。

<details><summary>Abstract</summary>

Sequence-to-function (S2F) models predict molecular phenotypes from DNA sequence and are increasingly applied to variant effect prediction (VEP), where the goal is to quantify how genetic variants alter gene expression. However, S2F model predictions are not uniformly reliable: accuracy varies substantially across variants, genes, and tissues, and current practice relies on crude magnitude thresholding to enrich for trustworthy predictions, which discards the majority of variants where S2F models could still provide signal. We developed gRely, a meta-modeling framework that estimates the probability that a given Borzoi VEP correctly predicts eQTL direction, using 1,121 features derived from the target variant, gene, and model outputs. On held-out tissues, gRely achieves a mean average precision of 0.885 (random baseline 0.744). Critically, within the low-magnitude regime where thresholding fails entirely, gRely identifies a high-confidence subset with 76% accuracy compared to a 58% baseline, recovering reliable predictions that magnitude filtering would discard. Interpretation via SHAP reveals that in this low-magnitude regime, gene expression level and cross-replicate signal concentration replace VEP magnitude as the primary discriminators of reliability. gRely is the first framework to provide per-prediction confidence scores for S2F model VEPs, and generalizes across architectures, producing consistent improvements on AlphaGenome predictions. By making reliability quantifiable, gRely enables principled filtering rather than blanket thresholding, and marks a step toward trustworthy deployment of S2F models in genomic research and clinical applications.

</details>

---

## 3. Probing Genomic Foundation Models with Splice-Variant Perturbations

- **期刊**: bioRxiv
- **作者**: Alavi, M. V.
- **机构**: Marcel V Alavi @ 712 North Inc.
- **日期**: 2026-10-09
- **ID**: DOI: 10.64898/2026.10.02.756289  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.02.756289v1
- **相关分数**: 9/10
- **一句话推荐**: 通过剪接变异扰动系统探究并对比多种基因组基础模型（Evo2, NTv3, AlphaGenome等）的表示边界与计算分配策略。
- **方法**: 采用单核苷酸剪接变异扰动范式，对比探针评估自监督通用基础模型与特定任务专家模型的表征能力。
- **主要发现**: 通用模型可匹敌专家模型，但不同架构存在计算不对称性（大参数窄上下文 vs 小参数宽上下文），且位点特异性阈值比突变类别校准更能提升分类准确率。
- **对我的启发**: 不同基础模型对上下文窗口和计算分配的依赖差异，提示在评估预训练模型预测增强子活性时，需系统考察padding长度对模型表征边界及推理计算的影响。

<details><summary>Abstract</summary>

As benchmarks saturate, traditional validation methods fail to capture the probabilistic representations of genomic foundation models. This study probes self-supervised generalists (NTv3 650M, Evo2 40B, Genos 10B) alongside task-specific specialists (SpliceAI, AlphaGenome, Borzoi) using a mechanistically focused paradigm centered on expert-curated single-nucleotide substitutions within the splicing regions of the exon-rich OPA1 gene. Extending this analysis across the broader corpus of OPA1 mutations, variants of uncertain significance (VUS), and an independent 65-gene dataset of spliceogenic mutations demonstrates that generalists can match task-specific networks. Training data scale, genetic diversity, and evolutionary context are key for capturing RNA splicing syntax, whereas sparse routing may constrain performance. Mechanistically, foundation models exhibit a compute-asymmetry: the Evo2 40B model frontloads compute into massive parameter scale to resolve single-nucleotide variants within a narrow 425-bp context window, whereas the bidirectional NTv3 650M model and the Genos 10B mixture-of-experts (MoE) architecture backload compute to inference, requiring spatial logit aggregation and expansive context windows of up to 94 kb. Furthermore, classification accuracy across these foundation models benefitted from locus-specific thresholding rather than mutation-class calibration, exposing representation boundaries of the models.

</details>

---

## 4. Systematic mapping of enhancers, silencers, and topological elements with prime editing deletion screens

- **期刊**: bioRxiv
- **作者**: Cai, X. S., Montgomery, M. T., Nagano, M. et al. (17 authors)
- **机构**: Jesse M. Engreitz @ Department of Genetics, Stanford University School of Medicine, Stanford, CA, USA
- **日期**: 2026-10-09
- **ID**: DOI: 10.64898/2026.10.08.756856  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.08.756856v1
- **相关分数**: 8/10
- **一句话推荐**: 通过大规模删除筛选实验刻画增强子等调控元件，并使用该数据对序列到功能模型进行基准测试，发现其难以连接远端靶基因。
- **方法**: 结合池化双引物编辑与流式分选的Swap-seq技术，通过大规模内源序列删除筛选系统量化调控元件的因果效应。
- **主要发现**: 发现了一类通过HDAC抑制邻近增强子来调控远端基因的沉默子；基准测试表明现有sequence-to-function模型能预测调控元件局部活性，但无法建立与远端靶基因的关联。
- **对我的启发**: Swap-seq生成的增强子删除数据集可作为评估预训练基因组学模型预测游离型增强子局部活性的基准，并提示模型在远端调控建模上的局限。

<details><summary>Abstract</summary>

Noncoding regulatory elements in the human genome can control gene expression through distinct mechanisms, including acting as enhancers, silencers, or topological elements. However, we lack tools to identify all such classes systematically and quantify their effects on gene expression in an endogenous genomic context. Here we develop Swap-seq, a method that combines pooled twin prime editing with flow-sorting to delete hundreds of endogenous regulatory sequences and measure their quantitative effects on the expression of a nearby gene. We apply Swap-seq to dissect the regulatory elements that control PPIF expression in THP-1 monocytes. We quantify the effects of distal and intronic enhancers, characterize CTCF insulators, and discover a silencer that regulates distal genes through histone deacetylase (HDAC)-mediated repression of neighboring enhancers. Hundreds of other genomic elements share its chromatin signatures and transcription factor binding sites, suggesting that this silencer represents a broader class of repressive elements. We leverage Swap-seq data to benchmark sequence-to-function models and show that they often capture the local activity of regulatory elements but fail to link them to distal target genes. Swap-seq thus provides a generalizable tool to discover regulatory elements across mechanistic classes, characterize their effects on gene expression, and generate large-scale datasets for evaluating sequence-to-function models.

</details>

---

## 5. Fine-tuning genomic models on rare splicing events identifies a novel biomarker of TDP-43 pathology

- **期刊**: bioRxiv
- **作者**: Martin-Linares, C. P., Peethambaran Mallika, A., Sandal, P. S., Martin, T. W., Morris, M., Wong, P. C., Ling, J. P.
- **机构**: Cristina P. Martin-Linares @ Biomedical Engineering, Johns Hopkins University, Baltimore, MD, USA; Center for Computational Biology, Johns Hopkins University, Baltimore, MD, USA
- **日期**: 2026-10-09
- **ID**: DOI: 10.64898/2026.10.07.757366  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.07.757366v1
- **相关分数**: 8/10
- **一句话推荐**: 研究基因组基础模型AlphaGenome在微调后对罕见剪接事件的泛化能力，涉及DNA语言模型的序列到功能预测与微调策略。
- **方法**: 比较预训练基因组基础模型（AlphaGenome）与专门化模型（OpenSpliceAI）在罕见剪接事件上的微调策略（冻结骨干 vs 全参数微调）及泛化能力。
- **主要发现**: 冻结权重的最先进GFM无法泛化到罕见剪接事件，但全参数微调或使用专门化模型能够成功预测并发现新的细胞类型特异性生物标志物。
- **对我的启发**: 在利用预训练基因组学模型预测特定细胞类型增强子活性时，需系统评估全参数微调与冻结骨干网络等微调策略对捕获罕见或细胞特异性表观遗传特征的影响。

<details><summary>Abstract</summary>

Genomic foundation models (GFMs) are pretrained on large genomic datasets, but their ability to predict rare disease-associated events after fine-tuning remains unclear. We tested this using TDP-43 cryptic exons, well characterized splicing events linked to neurodegenerative disease that are poorly represented in standard annotations. We compared the state-of-the-art GFM AlphaGenome with OpenSpliceAI, a specialized splice site prediction model. Fine-tuned OpenSpliceAI detected held-out cryptic exons in human and mouse and captured allele-specific splicing effects at the disease-associated UNC13A locus. In contrast, a splicing prediction head trained on AlphaGenome's frozen pretrained backbone failed to predict cryptic exons. Unfreezing and fine-tuning all model weights, however, enabled AlphaGenome to generalize to held-out data. To investigate cryptic splicing in cell types that are difficult to study experimentally, we applied fine-tuned OpenSpliceAI across the genome to study cell type-specific genes. This led to the identification of new cryptic splicing events in CLDN11 and ARHGAP23, which were subsequently validated in FTLD-TDP brain tissue. Notably, the cryptic exon in CLDN11 is predicted to generate a neoepitope that could serve as an oligodendrocyte-specific biomarker of TDP-43 pathology. Our results show that even a state-of-the-art GFM can fail to generalize to rare splicing events, even with substantial pretraining. However, both foundation and specialized models that learn to generalize to rare biological events can have broad applications in biological discovery and medicine.

</details>

---

## 6. Evo2HiC: a multimodal foundation model for integrative analysis of genome sequence and architecture

- **期刊**: bioRxiv
- **作者**: Fang, T., Li, Y., Wang, X. et al. (11 authors)
- **机构**: Sheng Wang @ University of Washington
- **日期**: 2026-10-08
- **ID**: DOI: 10.1101/2025.11.18.689171  |  URL: https://www.biorxiv.org/content/10.1101/2025.11.18.689171v1
- **相关分数**: 8/10
- **一句话推荐**: 将大规模DNA基础模型蒸馏并融合Hi-C数据，以预测细胞类型特异性的3D基因组结构，属于表观遗传基础模型范畴。
- **方法**: 将超大规模DNA基础模型（Evo 2 7B）蒸馏为紧凑编码器，并结合Hi-C数据指导蒸馏过程，构建联合建模DNA序列与3D基因组结构的多模态基础模型。
- **主要发现**: 该紧凑模型在预测Hi-C接触矩阵和表观基因组信号上优于现有模型，且能通过联合嵌入Hi-C与序列信息识别细胞类型特异性序列motif，并具备跨物种泛化能力。
- **对我的启发**: 借鉴其将超大规模预训练基因组模型蒸馏为紧凑编码器的策略，可解决大模型在预测虚拟表观遗传特征和增强子活性时因序列长度不一或padding导致的极高算力成本与效率瓶颈。

<details><summary>Abstract</summary>

Understanding how genome sequences shape three-dimensional (3D) genome architecture is fundamental to interpreting diverse biological processes. Although previous studies have shown that sequence information can predict 3D genome architecture, these models fall short in capturing cell type-specific structures because they are trained solely on sequence inputs. The widely available Hi-C data, which contains rich structural information across biosamples, can provide complementary features to sequence data for studying cell type-specific architectures. Recently, DNA foundation models have demonstrated encouraging performance in capturing long-range genomic dependencies, holding promise for modeling chromatin interactions. However, the extremely high computational cost of running these models limits their applicability to Hi-C analysis, which requires genome-wide sequence embeddings. Here, we present Evo2HiC, a multimodal foundation model that jointly models genome sequences and structures to study cell type-specific chromatin structure. The key idea of Evo2HiC is to distill a large-scale DNA foundation model, Evo 2 (7B), into a compact encoder, while guiding the distillation with Hi-C data to preserve genomic features critical for 3D genome analysis. The model supports two types of encoders, one that operates directly on DNA sequences, and a second that additionally takes as input corresponding Hi-C data. Using the DNA-only encoder and predicting raw Hi-C contact matrices, Evo2HiC improved distance-stratified Spearman correlation by 10.9% over Orca. Moreover, by jointly embedding Hi-C and sequence information Evo2HiC achieved the best overall Pearson correlation when predicting five representative epigenomic assays. Interpretation analysis of Evo2HiC revealed its ability to identify cell type-specific sequence motifs that explain changes in epigenomic signals. Finally, we demonstrated the cross-species generalizability of Evo2HiC on 177 species from the DNA Zoo dataset for Hi-C resolution enhancement. In summary, Evo2HiC is a foundation model that integrates genome sequences and 3D chromatin structure information, substantially reduces computational cost while maintaining state-of-the-art accuracy on predicting various epigenomic signals and genome architecture, enables the identification of cell type-specific motifs, and demonstrates robust generalizability across species.

</details>

---

## 7. Mapping transcriptional responses to cellular perturbations with RNA fingerprinting.

- **期刊**: Cell
- **作者**: Isabella N Grabski, Junsuk Lee, John D Blair, Carol Dalgarno, Isabella Mascio, Alexandra Bradu, David A Knowles, Rahul Satija
- **机构**: Rahul Satija @ New York Genome Center, New York, NY, USA; Center for Genomics and Systems Biology, New York University, New York, NY, USA. Electronic address: rsatija@nygenome.org.
- **日期**: 2026-10-09
- **ID**: DOI: 10.1016/j.cell.2026.09.017  |  PMID: 42854686  |  URL: https://pubmed.ncbi.nlm.nih.gov/42854686/
- **相关分数**: 7/10
- **一句话推荐**: 提出一种统计框架将新的单细胞数据映射到参考扰动字典上，与单细胞扰动研究兴趣相关。
- **方法**: 提出一种基于统计学习的RNA指纹图谱框架，通过从单细胞数据中学习扰动表征，将查询细胞的转录状态概率性映射至参考扰动字典。
- **主要发现**: 该方法能在单细胞分辨率下准确识别扰动响应，具备全基因组筛选可扩展性及组合扰动解析能力，并在多种生物学场景中验证了其广泛适用性。
- **对我的启发**: 无明显直接启发

<details><summary>Abstract</summary>

Single-cell perturbation dictionaries measure how cells respond to genetic and chemical perturbations, creating the opportunity to assign causal interpretations to observational data. We introduce RNA fingerprinting, a statistical framework that maps transcriptional responses from new experiments onto reference perturbation dictionaries. RNA fingerprinting learns perturbation representations, or "fingerprints," from single-cell data, then probabilistically assigns query cells to one or more candidate perturbations. We benchmark on ground-truth datasets, demonstrating accurate assignments at single-cell resolution, scalability to genome-wide screens, and the ability to resolve combinatorial perturbations. We demonstrate broad utility across diverse biological settings: identifying context-specific regulators of p53 under ribosomal stress, characterizing dose-dependent drug mechanisms of action, and uncovering cytokine-driven B cell heterogeneity during secondary influenza infection in vivo. Together, these results establish RNA fingerprinting as a versatile framework for interpreting single-cell datasets by linking cellular states to their underlying perturbations.

</details>

---

## 8. STEER-seq: a recombinase based platform for pooled multimodal single-cell perturbation screening

- **期刊**: bioRxiv
- **作者**: Migliori, V., Suo, C., Dufva, O. et al. (18 authors)
- **机构**: Andrew R Bassett @ Wellcome Sanger Institute, Wellcome Genome Campus, Hinxton, Cambridge, UK
- **日期**: 2026-10-09
- **ID**: DOI: 10.64898/2026.10.08.757551  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.08.757551v1
- **相关分数**: 6/10
- **一句话推荐**: 提出一种单细胞扰动筛选平台，结合RNA和染色质可及性多模态 profiling，与单细胞扰动研究兴趣相关。
- **方法**: 基于Bxb1重组酶介导的定点单拷贝整合与无启动子供体文库，结合单细胞多模态测序（RNA与染色质可及性）的池化功能获得性筛选平台。
- **主要发现**: 该平台消除了随机病毒整合的位置效应，实现了转录因子过表达的高定量评估；在hiPSC中系统揭示了特定TF驱动造血、成骨等细胞状态转变及伴随的染色质重塑与基因调控网络变化。
- **对我的启发**: STEER-seq生成的TF扰动单细胞ATAC数据可作为评估虚拟表观遗传特征预测增强子活性变化的高质量基准数据集，用于验证TF过表达驱动的局部染色质重塑预测。

<details><summary>Abstract</summary>

Pooled gain-of-function screening is a powerful method for screening for transcription factors whose overexpression leads to changes in cellular identity. However, variable transgene copy number, integration site and genomic context from random viral integration can confound quantitative comparisons between perturbations. We present STEER-seq (Single-cell Transgene Expression via Exchange Recombination sequencing), a virus-free platform for pooled ORF gain-of-function screening in human induced pluripotent stem cells (hiPSCs). STEER-seq combines irreversible Bxb1-mediated integration at a defined genomic safe-harbour locus with promoterless donor libraries and barcode-enabled perturbation tracking, enabling single-copy expression from a common promoter and genomic context and direct recovery of perturbation identity by single-cell sequencing. In a focused haematopoietic screen, SPI1 expression alone was sufficient to drive differentiation towards HSC/MPP-like progenitors in the absence of exogenous cytokines, with transient induction generating progenitors that retained multilineage haematopoietic differentiation potential. Joint RNA-chromatin accessibility profiling linked transcription factor-induced transcriptional responses to chromatin remodelling and enabled reconstruction of perturbation-induced gene regulatory networks, including a RUNX2-driven osteoblast programme. Scaling STEER-seq to around 2,000 human coding sequences enabled systematic discovery of transcription factors capable of inducing distinct cell-state programmes, including neural progenitor-, melanocyte- and vascular smooth muscle-like states, as well as maintenance of pluripotency. STEER-seq provides a scalable, quantitative framework for single-cell and multimodal gain-of-function screening, enabling functional discovery and engineering of human cell identity.

</details>

---
