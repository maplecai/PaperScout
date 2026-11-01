# Paper Scout 日报 2026-11-01

共筛选出 **5** 篇推荐论文。
📊 抓取 arxiv 20/biorxiv 120/pubmed 62 → 粗筛 34 篇 → LLM 选中 5 篇

## 1. A comprehensive map of the sequence basis of transcription initiation in humans

- **期刊**: bioRxiv
- **作者**: He, A. Y., Tian, C., Kundaje, A.
- **机构**: Anshul Kundaje @ Stanford University
- **日期**: 2026-10-30
- **ID**: DOI: 10.64898/2026.10.29.762743  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.29.762743v1
- **相关分数**: 9/10
- **一句话推荐**: 直接从DNA序列预测转录起始位点，覆盖多种人体器官和癌症类型，与sequence-to-function和细胞类型特异性调控预测高度相关。
- **方法**: 基于200+转录起始实验数据训练的高效可解释深度学习模型，采用sequence-to-function范式预测局部DNA序列的转录起始模式。
- **主要发现**: 构建了跨人类主要器官和癌症类型的转录起始序列基础图谱，模型能准确预测不同细胞环境下的转录起始模式并解码其序列决定因素。
- **对我的启发**: 可将转录起始信号作为虚拟表观遗传特征用于游离型增强子活性预测，并利用其跨细胞类型的高效建模框架评估预训练模型在不同padding策略下对局部序列特征提取的鲁棒性。

<details><summary>Abstract</summary>

Transcription initiation is a key marker of active enhancers and promoters. Here we describe an atlas of efficient and interpretable deep learning models trained on over 200 transcription initiation profiling experiments representing all major human organs and many cancer types. We show that our models accurately predict initiation patterns from local DNA sequence and decode their sequence determinants across diverse cellular contexts.

</details>

---

## 2. ChAI-Net learns a regulatory code for chromatin co-accessibility

- **期刊**: bioRxiv
- **作者**: Lee, J., Zhang, K., Shurberg, E., Ramani, V. S., Pollard, K. S.
- **机构**: Katherine S. Pollard @ Gladstone Institutes & UCSF
- **日期**: 2026-10-31
- **ID**: DOI: 10.64898/2026.10.29.762938  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.29.762938v1
- **相关分数**: 8/10
- **一句话推荐**: 从DNA序列预测单分子染色质共可及性，属于sequence-to-function建模且聚焦cis调控元件的调控语法学习。
- **方法**: 采用深度神经网络（ChAI-Net）从DNA序列预测单分子分辨率的染色质共可及性图谱。
- **主要发现**: 模型提取了增强子等顺式调控元件中驱动共可及性的特定motif组合及排列规则（方向、间距等），这些协同结合特征在仅预测平均可及性时无法被捕获。
- **对我的启发**: 在构建增强子活性预测模型时，可将TF motif的协同排列规则（方向、间距、共现）作为虚拟表观遗传特征或模型可解释性分析的重点，以提升对细胞类型特异性增强子活性的刻画精度。

<details><summary>Abstract</summary>

The regulation of chromatin accessibility is critical for cell function and identity. Advances in single-molecule long-read footprinting have enabled near-nucleotide-resolution readout of chromatin fiber organization, capturing both coordination of transcription factor (TF) binding and variation in nucleosome positioning previously obscured by bulk methods. Here we combine this technique with deep learning to study how protein-DNA interactions are coordinated within different types of cis-regulatory elements in mouse embryonic stem cells. First, we quantify the frequency with which pairs of positions are simultaneously accessible on individual molecules. Then, we train ChAI-Net, a neural network that predicts these locus-specific chromatin co-accessibility maps from the underlying DNA sequence. Through model interpretation and in silico experiments, we show that ChAI-Net learns unique combinations of sequence motifs underlying co-accessibility within enhancers, promoters, and CTCF-bound sites. Many of these motifs are missed when modeling average accessibility, suggesting a specific role in coordinated binding. ChAI-Net's regulatory grammar also highlights the importance of TF motif orientation, spacing, positioning, and co-occurrence in driving co-accessibility. Thus, our framework for extracting regulatory rules from footprinting data expands understanding of TF cooperativity, while laying the groundwork to elucidate how these rules vary across cellular contexts as single-molecule genomics is deployed at scale.

</details>

---

## 3. Host genomic context determines the direction of an oracle-predicted sequence effect: a composition-preserving CpG intervention in Enformer and Borzoi.

- **期刊**: Functional & integrative genomics
- **作者**: Selahattin Alperen Uysal
- **机构**: Selahattin Alperen Uysal @ Department of Medical Biology and Genetics, Ege University School of Medicine, İzmir, Türkiye. dralperenuysal@gmail.com.
- **日期**: 2026-10-31
- **ID**: DOI: 10.1007/s10142-026-02097-3  |  PMID: 42963434  |  URL: https://pubmed.ncbi.nlm.nih.gov/42963434/
- **相关分数**: 8/10
- **一句话推荐**: 直接评估Enformer和Borzoi作为sequence-to-function oracle的可靠性，探讨序列效应是否跨宿主位点可迁移。
- **方法**: 以 Enformer 和 Borzoi 等 sequence-to-function 模型作为预言机，结合六阶马尔可夫链生成序列，评估跨宿主基因座的 CpG 编辑序列效应。
- **主要发现**: 预测的序列效应大小和方向高度依赖于宿主基因座上下文，而非仅由插入序列决定；局部评分虽降低宿主主导效应，但效应方向在不同位点不稳健，且与 lentiMPRA 实验活性不相关。
- **对我的启发**: 该研究揭示宿主上下文对模型预测效应的决定性影响，提示在评估游离型增强子活性时，必须严格量化预训练模型输入序列的 padding 或上下文截断策略对预测结果的系统性偏置。

<details><summary>Abstract</summary>

Sequence-to-function models are increasingly used as oracles to score designed regulatory elements, on the untested assumption that an effect measured at one locus holds at another. Taking chromatin and host loci from multiple sclerosis risk regions, we kept four questions apart: sequence realism, transfer of discrimination, edit stability, calibration. A sixth-order Markov chain reproduced the cell-type-specific motif enrichment a trained transformer missed, despite its lower held-out likelihood. Scores differ in level between loci far more than between inserts at one locus, yet inserts selected by an Enformer-derived index kept 85% of their advantage at four unseen loci. Once GC was matched, however, the index separated peak-derived from inaccessible sequence at none of 12 hosts, and from random sequence in opposite directions at different hosts. Placing identical inserts and an identical CpG edit at 24 host loci, the effect varied far beyond sampling noise on host identity alone ([Formula: see text]), unpredicted by 18 host properties. It survives scoring only the bins the insert occupies ([Formula: see text], and across 200 loci), so is no artefact of aggregation; the apparent host dominance, however, falls from 25-fold to 3-fold under that localised score, and the one locus positive under the whole-window score reverses under it. Borzoi reproduced the heterogeneity but not its amplitude, and the objective did not predict lentiMPRA activity. For these two oracles and this edit, the size of a predicted effect depends on where it is measured, and its direction at any one locus is not robust.

</details>

---

## 4. SMFnet reveals principles of combinatorial transcription factor assembly

- **期刊**: bioRxiv
- **作者**: Schwämmle, T., Diamant, N., Badayeva, Y., Kleinendorst, R., Kundaje, A., Krebs, A. R.
- **机构**: Arnaud R Krebs @ Genome Biology Unit, EMBL Heidelberg, Meyerhofstraße 1, 69117 Heidelberg, Germany
- **日期**: 2026-10-31
- **ID**: DOI: 10.64898/2026.10.30.762954  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.30.762954v1
- **相关分数**: 8/10
- **一句话推荐**: 用扩散模型从DNA序列预测单分子染色质可及性分布，直接属于sequence-to-function且聚焦cis调控元件TF组装。
- **方法**: 提出基于生成式扩散模型的SMFNet，从DNA序列预测单分子染色质可及性图谱的分布状态，并结合PRISM识别特定分子状态关联的序列特征。
- **主要发现**: 单分子染色质状态可映射至特定转录因子（TF）组合，不同TF及其基序组合（依赖伙伴与间距）在染色质开放宽度及核小体定位精度上表现出截然不同的特征，且该机制在体内遗传扰动实验中得到验证。
- **对我的启发**: 在预测不同细胞类型增强子活性时，可借鉴生成式扩散模型预测表观遗传特征分布状态的范式，以捕捉群体平均掩盖的染色质状态异质性，从而更精细地刻画增强子活性机制。

<details><summary>Abstract</summary>

Combinatorial assembly of transcription factors (TFs) opens chromatin at cis-regulatory elements (cREs) to establish cell-type-specific gene expression. Dissecting the role of individual TFs and their collective function has been limited by the diversity of TF binding-site arrangements across cREs. A single regulatory sequence can support multiple configurations of TF and nucleosome occupancy, raising the possibility that distinct chromatin states reflect different TF assemblies. Predictive models linking regulatory sequence to chromatin accessibility collapse these distinct molecular states into population averages, obscuring how TF assemblies shape accessible chromatin. Here, we introduce SMFNet, a generative diffusion model that predicts distributions of single-molecule chromatin accessibility profiles from DNA sequence, and PRISM, which identifies sequence features associated with individual molecular states. Together, these approaches enable us to systematically associate single molecule chromatin states at cREs with specific TF binding motifs. Experimental perturbation of these motifs redistributes the corresponding states as predicted by SMFNet, supporting their interpretation as TF-dependent configurations underlying chromatin opening. We then use controlled in silico motif screens to systematically dissect individual and combinatorial TF contributions to chromatin opening. Individual TFs show distinct chromatin-opening signatures, differing in accessible-region width and nucleosome-positioning precision even when associated with similar levels of chromatin accessibility. Combining motifs reveals partner- and spacing-dependent effects on chromatin accessibility, TF occupancy and nucleosome positioning. Genetic perturbation of TF binding sites using natural variation at endogenous cRE confirms that TF-specific properties shape chromatin accessibility in vivo. Together, our findings reveal sequence-encoded principles of combinatorial TF assembly during chromatin opening.

</details>

---

## 5. Single-cell foundation models transfer across deep evolutionary distances

- **期刊**: bioRxiv
- **作者**: Trnovec, L., Katoh-Kurasawa, M., Arey, R. N., Shaulsky, G., Zupan, B.
- **机构**: Blaž Zupan @ Faculty of Computer and Information Science, University of Ljubljana, Ljubljana, Slovenia
- **日期**: 2026-10-31
- **ID**: DOI: 10.64898/2026.10.28.762457  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.28.762457v1
- **相关分数**: 6/10
- **一句话推荐**: 评估单细胞基础模型跨物种的零样本泛化能力，与基因组/表观遗传基础模型的表示学习与评估间接相关。
- **方法**: 零样本评估单细胞基础模型（Geneformer、scGPT、UCE）在跨物种（跨越数亿年进化距离）发育图谱中的迁移学习能力。
- **主要发现**: 单细胞基础模型无需重训即可在超过十亿年的进化距离上产生有效的细胞嵌入；基于蛋白质序列的基因表征（UCE）比基于词汇表的模型更完整且通常更准确。
- **对我的启发**: 基于底层序列的表征比离散词汇表更具跨域鲁棒性，启发我在评估预训练基因组学模型处理游离型增强子时，可对比不同序列编码方式对padding和未知序列泛化能力的影响。

<details><summary>Abstract</summary>

Single-cell foundation models are trained mostly on human and other vertebrate cells, yet are proposed as general-purpose models. Whether they transfer far beyond their training species is unknown. We evaluated zero-shot embeddings from Geneformer, scGPT and UCE against PCA and scVI in developmental atlases of Dictyostelium discoideum and Caenorhabditis elegans, separated from humans by 1.2 billion and 600 million years. Without retraining, the models recovered developmental order and preserved organism-specific cell identities. UCE encodes genes by protein sequence and could use 97% of measured genes, whereas Geneformer and scGPT, after ortholog mapping, used under one-fifth. UCE performed most consistently, often exceeding species-native baselines. Restricted to ortholog-mappable genes, it still scored above vocabulary-based models on five of six annotation tasks, some narrowly. Foundation models can thus yield informative cell embeddings across more than a billion years of evolution, and protein-sequence gene representations make these embeddings more complete and often more accurate.

</details>

---
