# Paper Scout 日报 2026-10-05

共筛选出 **4** 篇推荐论文。
📊 抓取 arxiv 37/biorxiv 61/pubmed 26 → 粗筛 15 篇 → LLM 选中 4 篇

## 1. Kidzoi Enables Cell-Type-Specific Regulatory Activity and Variant Effect Prediction in Kidney

- **期刊**: bioRxiv
- **作者**: Rather, A. A., Lee, D.
- **机构**: Dongwon Lee @ Boston Children's Hospital & Harvard Medical School
- **日期**: 2026-10-04
- **ID**: DOI: 10.64898/2026.09.28.746288  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.28.746288v1
- **相关分数**: 9/10
- **一句话推荐**: 使用预训练S2F模型Borzoi通过迁移学习预测细胞类型特异性染色质可及性，直接关联跨细胞类型调控活性预测及序列到功能建模。
- **方法**: 基于预训练S2F模型Borzoi的迁移学习，结合单核染色质可及性数据构建细胞类型特异性序列到功能预测模型。
- **主要发现**: 迁移学习得到的Kidzoi模型在预测肾脏细胞特异性调控活性和变异效应上优于现有模型；消融实验表明仅需32-64kbp侧翼序列即可实现准确的变异效应预测。
- **对我的启发**: 论文中的侧翼序列消融实验直接对应我关注的预训练基因组学模型padding问题，可借鉴其量化局部上下文对预测性能贡献的评估方法，优化增强子活性预测模型的输入序列长度设置。

<details><summary>Abstract</summary>

Sequence-to-function (S2F) deep learning models predict genome-wide functional profiles directly from DNA sequences and have significantly advanced our understanding of gene regulation. However, existing S2F models are fundamentally constrained by their initial training datasets, and no single model encompasses the full spectrum of cell types, clinical conditions, and cellular states, while training new models de novo is nontrivial. Here, we develop Kidzoi, a kidney cell-type-specific S2F model obtained by transfer learning from the pretrained model Borzoi using single-nucleus chromatin accessibility data from human kidney tissue. Kidzoi accurately predicts cell-type-specific chromatin accessibility and improves regulatory variant effect prediction by 10-23% over existing models. Furthermore, Kidzoi effectively prioritizes genome-wide association study (GWAS) fine-mapped causal variants associated with kidney function (estimated glomerular filtration rate based on both creatinine and cystatin C; eGFRcr-cys) while resolving their cell-type specificity. Systematic ablation of flanking sequence indicates that a local context of 32-64kbp, representing only 6-12% of the full model input, is sufficient for accurate variant effect prediction. Finally, we show that a multi-task model achieves comparable performance to single-task models at a substantially reduced computational cost.

</details>

---

## 2. G4SCOPE identifies sequence features and epigenetic contexts of chromatin G-quadruplexes

- **期刊**: bioRxiv
- **作者**: Sarvar, A., Esain-Garcia, I., Melidis, L. et al. (11 authors)
- **机构**: Samuel Aparicio @ BC Cancer Research Institute, 675 W10th Avenue, Vancouver, V5Z 1L3, Canada
- **日期**: 2026-10-04
- **ID**: DOI: 10.64898/2026.09.28.748631  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.28.748631v1
- **相关分数**: 7/10
- **一句话推荐**: 从DNA序列直接预测染色质G4占据和CUT&Tag表观遗传谱，属于sequence-to-function和调控基因组学范畴。
- **方法**: 结合CNN基序学习与Transformer自注意力的多任务深度学习框架，直接从DNA序列预测染色质G4占据并重建CUT&Tag图谱。
- **主要发现**: 模型能从序列解码内源性G4占据规律并跨细胞系泛化；发现BRCA1/2缺失分别导致G4密度全局膨胀和染色体级结构耗竭，且不同序列定义的G4拓扑具有独特的局部表观遗传特征。
- **对我的启发**: 利用模型提取的潜在序列表征进行无监督聚类以解析不同调控元件亚类及其表观遗传上下文的范式，可借鉴用于我研究中虚拟表观遗传特征的生成与不同细胞类型增强子活性上下文的解析。

<details><summary>Abstract</summary>

Cancer-associated epigenetic remodeling involves a complex interplay between DNA secondary structures and covalent cytosine modifications, yet predicting endogenously folded, chromatin-constrained G-quadruplex (G4) dynamics remains challenging. Here, we develop G4SCOPE, a multi-task deep learning framework that models chromatin-associated G4 occupancy and reconstructs quantitative high-resolution CUT&Tag profiles directly from primary DNA sequence alone. We initially trained G4SCOPE on genotype-stratified G4 enriched cut&tag landscapes generated across an isogenic series of human breast epithelial cells (WT, TP53-/-, TP53-/-;BRCA1-/-, and TP53-/-;BRCA2-/-). G4SCOPE integrates convolutional motif learning with transformer self-attention to decode long-range sequence contexts. The model robustly distinguishes chromatin-associated G4s from GC-matched loci with intrinsic in vitro folding potential, generalizes across distinct breast lineages, and transfers accurately to an independent K562 cellular context. Strikingly, genotype-resolved mapping reveals a profound divergence in genome maintenance states: BRCA1 deficiency indicated a global inflation of chromatin-embedded G4 density, whereas BRCA2 loss was associated with systemic, chromosome-wide structural depletion. Furthermore, unsupervised clustering of model-derived latent sequence representations identified distinct biological G4 subclasses that occupy unique regulatory class genomic environments associated with distinct local 5-methylcytosine and 5-hydroxymethylcytosine landscapes. Together, our framework decodes the primary sequence grammar governing cell-based G4 occupancy and demonstrates that sequence-defined G4 topologies harbor intrinsic and distinct local epigenetic features.

</details>

---

## 3. The mammalian genome is punctuated by regularly spaced nucleosome islands

- **期刊**: bioRxiv
- **作者**: Mozziconacci, J., Christophe, M., Altamirano-Pacheco, L., Navarro-Gil, P.
- **机构**: Julien Mozziconacci @ MNHN
- **日期**: 2026-10-04
- **ID**: DOI: 10.64898/2026.09.30.755582  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.30.755582v1
- **相关分数**: 6/10
- **一句话推荐**: 使用深度学习从DNA序列预测核小体占据并进行in silico mutagenesis，属于sequence-to-function范畴，对理解序列编码的染色质组织有启发。
- **方法**: 基于原始DNA序列训练深度学习模型预测体内核小体占据，并结合计算机模拟突变解析定位基序。
- **主要发现**: 哺乳动物核小体空间排布受DNA序列编码，短重复元件（如SINE/LINE内的特定基序及微卫星）是建立规则间隔核小体岛的关键组织者。
- **对我的启发**: 在构建增强子活性预测模型时，可关注重复序列对局部染色质可及性及增强子边界的潜在影响，并在评估预训练模型padding策略时考虑重复元件的上下文依赖性。

<details><summary>Abstract</summary>

Nucleosome positioning plays a fundamental role in regulating DNA accessibility and cellular activity, yet the precise rules by which mammalian sequences instruct this organization have remained incomplete. Prior work has established that intrinsic sequence preferences dictate nucleosome architecture in yeast, but in mammals, this sequence code is modulated by chromatin state and cell-type-specific factors. Here, we train a deep-learning model on genome-wide maps from mouse embryonic stem cells to predict nucleosome occupancy directly from the primary DNA sequence. Our model accurately predicts in vivo occupancy and captures shared biological signals while effectively denoising assay-specific technical biases. Through in silico mutagenesis, we identify specific nucleosome positioning regions comprised of short 5-to-20-base-pair motifs concentrated within dense regulatory windows. Furthermore, we demonstrate that repetitive DNA elements play a major role in establishing these highly organized nucleosome arrays on a genomic scale. Specifically, CCCTC-binding factor motifs embedded within short interspersed nuclear elements, zinc-finger-bound motifs within long interspersed nuclear elements, and microsatellite repeats act as potent organizers of nucleosome phasing. Together, our findings extend the concept of sequence-encoded nucleosome architecture to mammalian genomes and reveal that regularly spaced nucleosome islands are shaped by short, recurrent sets of DNA motifs that couple local sequence to chromatin structure.

</details>

---

## 4. Distinct sequence grammars of nucleosomal and linker DNA shape mutational and methylation landscapes in cancer

- **期刊**: bioRxiv
- **作者**: Masoudi-Sobhanzadeh, Y., Kumar, S.
- **机构**: Sushant Kumar @ University of Toronto
- **日期**: 2026-10-04
- **ID**: DOI: 10.64898/2026.09.28.755196  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.28.755196v1
- **相关分数**: 6/10
- **一句话推荐**: 使用可解释深度学习从序列区分核小体与连接DNA并关联突变和甲基化模式，属于sequence-to-function和计算表观遗传学。
- **方法**: 提出可解释深度学习框架DeepND，基于序列特征区分核小体与连接DNA并解析其与癌症突变及甲基化的关联。
- **主要发现**: 揭示了核小体与连接DNA截然不同的序列语法，且特定motif的癌症突变和甲基化模式显著依赖于核小体旋转定位及DNA小沟方向。
- **对我的启发**: DeepND利用可解释深度学习提取序列语法并关联表观遗传特征的方法，可启发在增强子活性预测中构建序列motif与虚拟表观遗传特征间的可解释映射机制。

<details><summary>Abstract</summary>

Nucleosomes regulate DNA accessibility and thereby influence gene expression, DNA repair, and mutagenesis. Although DNA sequence strongly determines nucleosome positioning, the higher-order sequence grammar underlying nucleosome organization and its relationship to cancer-associated mutational and epigenetic processes remain poorly understood. We developed DeepND, an interpretable deep learning framework that distinguishes nucleosomal from inter-nucleosomal DNA and identifies sequence features associated with nucleosome architecture. Our interpretable framework enabled analysis of sequence patterns and identified 210 sequence motifs of 2-16 bp length that were significantly enriched or depleted in nucleosomal DNA, substantially extending the previously characterized nucleosomal motifs. These motifs revealed distinct sequence grammars within nucleosomal footprints and linker regions, including patterns associated with inward- and outward-facing minor grooves. Forty-four of these motifs showed cancer-type-specific enrichment or depletion of somatic mutations, and six motifs were associated with differential DNA methylation levels. In lung and endometrial cancers, mutations exhibited a significant ~10-bp periodic enrichment pattern across distinct minor-groove orientations, consistent with differential sensitivity of mutational and DNA repair processes to nucleosomal rotational positioning. We further identified sequence-specific methylation patterns consistent with reduced accessibility of nucleosomal DNA to DNA methyltransferases, including differential methylation at inward- and outward-facing CpG motifs. Together, these findings provide a sequence-resolved characterization of nucleosome-level organization and its link to cancer-specific mutational processes and epigenetic landscapes.

</details>

---

> 补发日报：检索窗口 [2026-10-02 00:00, 2026-10-05 00:00) UTC。已排除此前日报及 2026-10-08 邮件中已推荐的论文；粗筛阈值 0.2，相关性至少 6/10。
