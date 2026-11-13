# Paper Scout 日报 2026-11-13

共推荐 **3** 篇论文。

## 1. An integrative single-cell epigenomic atlas annotates the regulatory genome of the adult mouse brain.

Cell · 期刊文献 · 2026-11-12 · 相关性 7/10

**研究关联：当前课题直接相关**

- **为什么值得看**：构建了大规模单细胞表观基因组图谱并开发了从DNA序列预测细胞类型特异性表观基因组特征的深度学习模型，直接命中sequence-to-function和细胞类型特异性调控预测。
- **任务与验证范围**：输入：DNA序列（整合多模态表观组数据） → 输出：细胞类型特异性表观特征与基因表达；研究物种/细胞体系：成年小鼠大脑（100多个细胞亚类）；验证范围：跨100多个大脑细胞亚类，候选增强子功能验证方式摘要未说明
- **核心方法**：基于多模态单细胞表观图谱，采用sequence-to-function深度学习范式从DNA序列预测细胞类型特异表观特征。
- **主要发现与证据**：构建了覆盖100多个大脑细胞亚类、81%基因组的表观图谱；发现组合组蛋白修饰比单用染色质可及性更能有效提名具功能支持的候选增强子。
- **可借鉴点（研究建议）**：其组合组蛋白修饰定义活跃增强子的策略，可启发我构建更精细的虚拟表观遗传特征标签用于增强子活性预测。
- **迁移边界**：原模型泛化仅限小鼠大脑组织，未涉及预训练模型padding策略评估；迁移至其他组织或游离型增强子预测任务时需重新验证。
- **阅读时核实**：其深度学习模型在处理DNA序列输入时，具体的序列长度截断与padding策略是什么？是否对游离型增强子区域的预测性能进行了单独评估？

[原文](https://pubmed.ncbi.nlm.nih.gov/43020033/) · [DOI](https://doi.org/10.1016/j.cell.2026.10.022)

作者：Zhaoning Wang, Songpeng Zu, Ethan J Armand et al. (29 authors)
来源标注的末位/通讯作者：Bing Ren
机构：Department of Cellular and Molecular Medicine, University of California, San Diego School of Medicine, La Jolla, CA, USA; Department of Genetics and Development, Columbia University Irving Medical Center, New York, NY, USA; New York Genome Center, New York, NY, USA; Department of Systems Biology, Columbia University Irving Medical Center, New York, NY, USA; Department of Biochemistry and Molecular Biophysics, Columbia University Irving Medical Center, New York, NY, USA. Electronic address:

### 英文摘要

Histone modifications underpin the cell-type-specific gene regulatory programs that drive the remarkable cellular diversity of the mammalian brain. Here, we jointly profiled four histone modifications and the transcriptome in 2.5 million nuclei from the adult mouse brain. By integrating these data with chromatin accessibility, DNA methylation, and three-dimensional genome organization, we constructed a unified epigenomic atlas spanning over 100 brain cell subclasses and assigned active, primed, and repressive chromatin states across 81% of the genome. Active chromatin states marked by combinatorial histone modifications better nominate candidate enhancers with functional support than chromatin accessibility alone, while H3K27me3- and H3K9me3-marked chromatin states delineate distinct modes of cell-type-specific gene repression. Finally, this multimodal resource enables the development of deep learning models that predict cell-type-specific epigenomic features and gene expression from DNA sequence, providing a comprehensive framework for annotating the brain regulatory genome and interpreting non-coding disease risk variants.

---

## 2. Single-cell multimodal atlas reveals regulatory programs in the human brain.

Cell · 期刊文献 · 2026-11-12 · 相关性 7/10

**研究关联：方法可借鉴**

- **为什么值得看**：开发了sequence-to-function模型预测细胞类型特异性变异效应，涵盖160种细胞类型和500K+候选调控元件，与我的增强子活性和调控预测研究高度相关。
- **任务与验证范围**：输入：DNA序列及多模态表观基因组数据 → 输出：细胞类型特异性神经疾病变异效应预测及调控程序解析；研究物种：人类（含跨物种比较）；细胞体系：18个成人脑区，160种细胞类型；验证范围：跨160种细胞类型及跨物种比较
- **核心方法**：结合单细胞多模态图谱构建与序列到功能的深度学习模型，预测细胞类型特异性的变异效应
- **主要发现与证据**：构建了覆盖18个脑区、160种细胞类型、超75万细胞核的多模态图谱，解析了超50万候选调控元件状态；其序列模型实现了细胞类型特异性变异效应预测，并发现活跃调控程序跨物种保守而抑制性程序存在分歧
- **可借鉴点（研究建议）**：其跨160种细胞类型的多模态表观遗传数据集及序列到功能建模思路，可为评估预训练基因组学模型在不同细胞类型间的泛化能力提供参考基准
- **迁移边界**：原论文聚焦于人脑组织的疾病变异效应预测，而我的研究关注游离型增强子活性预测及预训练模型的padding影响，不能直接将其跨细胞类型泛化能力或模型架构等同于我的任务表现
- **阅读时核实**：其sequence-to-function模型在处理DNA序列输入时采用了何种具体的序列长度对齐或padding策略，该策略是否对细胞类型特异性预测结果产生显著影响？

[原文](https://pubmed.ncbi.nlm.nih.gov/43020026/) · [DOI](https://doi.org/10.1016/j.cell.2026.08.012)

作者：Yang Xie, Lei Chang, Guojie Zhong et al. (57 authors)
来源标注的末位/通讯作者：Bing Ren
机构：New York Genome Center, New York, NY 10013, USA; Department of Cellular and Molecular Medicine, University of California, San Diego, La Jolla, CA 92093, USA; Center for Epigenomics, Department of Cellular and Molecular Medicine, University of California, San Diego, La Jolla, CA 92093, USA; Department of Genetics and Development, Columbia University Irving Medical Center, New York, NY 10032, USA; Moores Cancer Center, Institute for Genomic Medicine, School of Medicine, University of California, San Diego, La Jolla, CA 92037, USA; Systems Biology, Biochemistry and Molecular Biophysics, Columbia University Irving Medical Center, New York, NY 10032, USA. Electronic address:

### 英文摘要

Direct measurement of chromatin states together with transcription is essential for understanding how cell-type-specific regulatory programs are established and maintained in the adult human brain. Here, we present a large-scale single-cell multimodal atlas by jointly profiling the transcriptome with active (H3K27ac) or repressive (H3K27me3) histone modifications across 18 adult brain regions. We targeted over 750,000 nuclei spanning 160 cell types and integrated these data with chromatin accessibility, DNA methylation, 3D genome architecture, and spatial transcriptomes. This framework resolved chromatin states for over 500,000 candidate regulatory elements, identified enhancer-gene links and regulatory programs, revealed Polycomb-associated ultra-long-range contacts, and uncovered brainwide epigenomic heterogeneity. We further developed a sequence-to-function model to predict cell-type-specific effects of candidate neurological disease variants. Finally, comparative analyses across species reveal conservation in active regulatory programs but divergence in repressive programs. Together, this study provides a comprehensive epigenomic reference for interpreting regulatory principles and epigenetic memory underlying human brain organization and disease.

---

## 3. Aberrant splicing prediction during human organ development

bioRxiv · 预印本 · 2026-11-11 · 相关性 7/10

**研究关联：方法可借鉴**

- **为什么值得看**：基于序列的模型预测跨发育阶段的异常剪接，直接涉及sequence-to-function和跨组织/细胞类型的调控变异效应预测，且与AlphaGenome对比。
- **任务与验证范围**：输入：单核苷酸变异和插入缺失 → 输出：异常剪接事件预测评分；研究体系：人类器官发育（胚胎、儿童、成人组织）；验证范围：跨发育阶段和跨组织（如脑组织），并在Solve-RD和Genomics England罕见病队列中验证。
- **核心方法**：扩展AbSplice框架，引入剪接位点连续表示并整合基于序列的模型Pangolin的预测，以建模跨发育阶段的剪接动态。
- **主要发现与证据**：改进后的模型优于原模型及纯序列模型（如AlphaGenome），发现超过18,000个早期发育特异（尤其脑部）的剪接破坏变异；预测的剪接破坏发育时间与临床发病年龄相关，并在罕见病队列中鉴定出26个相关变异及FGFR1新候选诊断。
- **可借鉴点（研究建议）**：可借鉴其通过整合多个序列模型预测并引入连续表示来提升跨组织泛化能力的思路，推测对增强子跨细胞类型活性预测的模型融合有参考价值。
- **迁移边界**：原论文聚焦剪接变异预测，我的任务为增强子活性预测及预训练模型padding分析。剪接与增强子调控机制不同，其跨组织泛化策略不能直接等同于增强子跨细胞类型的泛化，需注意任务边界。
- **阅读时核实**：AbSplice框架在引入剪接位点连续表示时，具体是如何将发育阶段的动态变化编码进模型输入的？

[原文](https://www.biorxiv.org/content/10.1101/2025.07.16.665183v1) · [DOI](https://doi.org/10.1101/2025.07.16.665183)

作者：Wagner, N., Neverov, A. M., Martin-Geary, A. C., Londhe, S., Schröder, C., Yepez, V. A., Whiffin, N., Gagneur, J.
来源标注的末位/通讯作者：Julien Gagneur
机构：Department of Informatics, Technical University of Munich, Garching, Germany; Helmholtz Association - Munich School for Data Science (MUDS), Munich, Germany; Co

### 英文摘要

Developmental disorders constitute a major class of genetic diseases, yet tools to identify splicing-disruptive variants during development are lacking. To address this need we extended the AbSplice framework to incorporate splicing dynamics across developmental stages. Moreover, we introduced several improvements including a continuous representation of splice site usage and integration of the rich set of predictions from the sequence-based model Pangolin. These advances improve the performance of the original model at predicting aberrant splicing events and help outperform purely sequence-based models including AlphaGenome, enabling predictions across embryonic, childhood, and adult tissues. Genome-wide scores for all single-nucleotide variants and a web interface to score indels are available to facilitate the exploration of the predictions. Our genome-wide predictions reveal a class of variants with splicing-disruptive effects confined to early development, particularly abundant in the brain (>18,000 variants). These variants are enriched in loss-of-function intolerant genes and neurodevelopmental disorder genes. Within the rare-disease cohort Solve-RD, high-impact brain-specific predictions are significantly enriched in individuals affected by neurodevelopmental disorders (NDD) in NDD-linked genes. Furthermore, the predicted developmental timing of the splicing disruption correlates with the clinical age of onset. Analysis of genomes of individuals with a suspected Mendelian disorder from Genomics England identified 26 unique variants in disease-linked genes, with stronger predicted effects during development than in adulthood, including a candidate new diagnosis in the gene FGFR1. Altogether, these results improve the accuracy of splice-disruptive variant prediction and provide tissue and developmental context to aid interpretation in rare disease diagnostics.

---

中文笔记基于标题和摘要生成，未核验全文；研究建议不代表论文已验证的结论。相关性分数不是论文质量评分。

检索统计：窗口 [2026-11-10 00:00, 2026-11-13 00:00) UTC；抓取 biorxiv 142/pubmed 93 → 粗筛 32 篇 → LLM 选中 3 篇
