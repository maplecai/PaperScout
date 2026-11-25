# Paper Scout 日报 2026-11-25

共推荐 **3** 篇论文。

## 1. FiberTron enables regulatory variant effect prediction and testing from multi-omic long reads of a single sample

bioRxiv · 预印本 · 2026-11-24 · 相关性 9/10

**研究关联：方法可借鉴**

- **为什么值得看**：FiberTron是轻量级sequence-to-function模型，从参考序列预测染色质可及性和转录覆盖度，并与AlphaGenome在变异效应预测上直接对比，高度契合你的研究兴趣。
- **任务与验证范围**：输入：524 kb参考序列 → 输出：CpG甲基化、染色质可及性及链特异性转录本覆盖度（碱基分辨率）；物种/体系：人类（HG002、黑色素瘤细胞系、透明细胞肉瘤样本）；验证范围：跨样本验证变异效应预测（如黑色素瘤和肉瘤样本）。
- **核心方法**：基于单样本多组学长读长数据从零训练的12M参数卷积-Transformer模型，采用长序列输入预测多组学特征。
- **主要发现与证据**：仅用单样本数据从零训练的轻量级模型，在留出染色体上预测多组学特征中位Pearson r达0.85-0.97，在dsQTL/eQTL变异预测上媲美AlphaGenome等大模型；并在独立样本中成功识别79%等位基因特异性可及性变异及致癌增强子突变。
- **可借鉴点（研究建议）**：可借鉴其524 kb长序列输入的模型架构设计，推测其长序列处理方式可用于评估预训练基因组学模型中padding策略对边缘序列特征预测的影响。
- **迁移边界**：原论文聚焦单样本多组学特征预测及变异效应测试，而我的研究关注跨细胞类型增强子活性及预训练模型padding影响；其单样本训练范式能否泛化至跨细胞类型虚拟表观遗传特征预测及padding评估尚需验证。
- **阅读时核实**：模型在处理524 kb输入序列时采用了何种padding或截断策略？该策略是否对序列边缘的增强子活性或表观遗传特征预测产生显著的边缘效应？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.13.762587v1) · [DOI](https://doi.org/10.64898/2026.11.13.762587)

作者：Eftychiou, M., Lambrechts, L., Vande Velde, J. et al. (10 authors)
来源标注的末位/通讯作者：Jonas Demeulemeester
机构：VIB-KU Leuven

### 英文摘要

State-of-the-art sequence-to-function models are trained on large compendia of public data to predict regulatory activity across hundreds of cell types. However, they are not designed to interpret individual genomes, effects in under-sampled cell types, or provide a comprehensive view of how genetic variation influences complex diseases. Here we show that a single sample profiled with Fiber-seq and Nanopore direct RNA-seq contains enough information to train such a model from scratch. FiberTron, a 12M parameter convolutional-transformer model, takes 524 kb of reference sequence and predicts CpG methylation, chromatin accessibility and strand-specific transcript coverage at base-pair resolution (median Pearson's r of 0.85-0.97 on held-out chromosomes). Trained in under a day on a single four-GPU node, our HG002 model performs on par with models such as AlphaGenome on dsQTL and eQTL variant effect prediction tasks, despite being over an order of magnitude smaller. As training uses reference sequence only, each sample's phased multi-omic long reads remain available to test its variant-effect predictions. FiberTron recapitulates OAS1 splicing variation associated with COVID-19 risk, recovers 79% of allele-specific accessibility variants in a melanoma line, identifies oncogenic TERT promoter and TAL1 enhancer mutations, and predicts EWSR1::ATF1 fusion transcript expression and its unique chromatin imprint in a rare clear cell sarcoma patient sample. Lightweight single-sample training brings base-resolution interpretation of non-coding variation within reach of individual laboratories.

---

## 2. BQDNA: Multi-Head Binary Spherical Quantization for Genomic Sequence Modeling

arXiv · 预印本 · 2026-11-22 · 相关性 8/10

**研究关联：方法可借鉴**

- **为什么值得看**：提出基于向量量化的DNA分词器BQVAE和自回归基因组语言模型BQDNA，直接关联DNA语言模型与生物序列表示学习。
- **任务与验证范围**：输入：长DNA序列 → 输出：离散化序列表示及下游任务预测；研究物种/细胞体系：多物种（含hg38等），具体细胞类型摘要未说明；验证范围：跨物种泛化，是否跨细胞类型摘要未说明
- **核心方法**：采用上下文感知的向量量化变分自编码器（BQVAE）进行DNA标量量化，并构建支持多头码本的自回归基因组语言模型（BQDNA）。
- **主要发现与证据**：BQVAE优于k-mer、BPE等手工分词器和普通VQVAE；BQDNA仅用0.1B多物种数据训练并在hg38上训练1个epoch，即超越预训练数据量多10~100倍的gLM，具备出色的跨物种泛化能力。
- **可借鉴点（研究建议）**：推测将学习型向量量化tokenizer引入增强子序列建模，可能比传统手工分词更有利于提取调控元件特征，从而提升基于序列的增强子活性预测性能。
- **迁移边界**：原论文聚焦通用DNA序列表示与跨物种泛化，未直接涉及特定细胞类型的增强子活性预测或虚拟表观遗传特征；其tokenizer在跨细胞类型功能预测任务中的效果，以及对预训练模型padding策略的依赖性，均未在文中证明。
- **阅读时核实**：BQVAE的向量量化过程对输入DNA序列的长度和padding方式是否有特定敏感性？在处理不同长度或含padding的增强子序列时，量化码本的分配是否会产生偏差？

[原文](https://arxiv.org/abs/2611.29395)

摘要提供的链接（未核验可用性）：[资源 1](https://github.com/Sophie10001b/BQDNA)

作者：Xudong Wang, Siwei Cheng, Haozhe Hu
机构：当前 API 未提供机构信息

### 英文摘要

Decoding biological information from long, repetitive DNA remains challenging. Genomic language models (gLMs) often follow the conventional language-model pretrain-and-adapt paradigm. However, the lack of inherent semantic segmentation and prior rules makes hand-crafted tokenizers like k-mer and BPE suboptimal. We introduce context-aware \textbf{BQVAE} for scalar quantization of DNA and \textbf{BQDNA}, an autoregressive gLM supporting multi-head codebooks. Comprehensive experiments reveal that: (1) unique training dynamics of vector quantization in DNA space, including the importance of alignment between training corpus and downstream data. (2) superior performance of BQVAE over hand-crafted tokenizers and vanilla VQVAE. (3) remarkable cross-species generalization capability of BQDNA, which achieves state-of-the-art performance with merely 0.1B multi-species training for BQVAE and 1 epoch training on hg38 for BQDNA, outperforming gLMs pretrained with 10$\sim$100x more tokens. Our findings underscore the potential of learned vector quantization for genomic sequence representation. Code is available at https://github.com/Sophie10001b/BQDNA

---

## 3. Multi-omics causal deep learning reveals regulatory structure while interventions refine perturbation predictions

bioRxiv · 预印本 · 2026-11-24 · 相关性 6/10

**研究关联：方法可借鉴**

- **为什么值得看**：用因果VAE从单细胞多组学数据推断基因调控结构并改进扰动预测，与单细胞扰动研究兴趣相关。
- **任务与验证范围**：输入：单细胞多模态观测数据（CITE-seq）与CRISPR扰动数据 → 输出：基因/蛋白调控网络及扰动响应预测；研究物种/细胞体系：摘要未说明；验证范围：涵盖3个CRISPR筛选及约1000个训练扰动的Perturb-seq，摘要未明确说明是否跨细胞类型。
- **核心方法**：提出跨模态因果变分自编码器（CMC-VAE），在潜在空间构建基因与蛋白的稀疏因果网络，并利用无扰动标签的对照细胞或干预数据微调潜在网络以优化预测。
- **主要发现与证据**：模型在809,130个观测CITE-seq数据上训练后，在3个CRISPR筛选中预测knockout响应基因优于相关性和潜在VAE基线；在约1000个扰动的Perturb-seq上微调潜在网络，能学习到可迁移至held-out基因的特异性效应，并在模拟中恢复观测训练无法解决的因果边方向。
- **可借鉴点（研究建议）**：利用少量干预数据仅微调预训练模型的潜在网络以学习可迁移效应的策略，或许可启发我在预训练基因组学模型中通过微调特定网络层来适应不同细胞类型的增强子活性预测任务。
- **迁移边界**：原论文处理单细胞多组学表达数据与扰动响应预测，而我的任务是基于DNA序列/虚拟表观遗传特征预测增强子活性及评估padding影响。两者数据模态与预测目标存在本质差异，原论文在跨基因上的迁移效果不能等同于跨细胞类型或跨序列任务的泛化能力。
- **阅读时核实**：CMC-VAE在潜在空间构建跨模态因果网络时，如何确保潜在特征与具体测量特征（如RNA和蛋白）之间的映射具有生物学可解释性，而非虚假的统计关联？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.22.768440v1) · [DOI](https://doi.org/10.64898/2026.11.22.768440)

作者：Goudarzi, S., Nandi, V., Liu, N., Goodarzi, H.
来源标注的末位/通讯作者：Hani Goodarzi
机构：Arc Institute

### 英文摘要

Inferring gene regulation from single-cell data is difficult because observational measurements cannot distinguish correlation from causation and access to perturbational data, especially with multiple modalities, remains limited. Here we present the Cross-Modal Causal Variational Autoencoder (CMC-VAE), which learns a network linking genes and proteins (gene-gene, protein-protein and gene-protein) in the latent space and maps each connection back onto measured features. Trained on 809,130 observational CITE-seq profiles, CMC-VAE recovers co-expression, transcription factor regulons and immune signalling programs, and learns a sparse cross-modal map enriched for transcript-protein cognate pairs. On three CRISPR screens used during development, it ranks knockout-responsive genes better than correlation and latent-VAE baselines. Fitted to a screen's unperturbed control cells, without perturbation labels, the model translates measured knockout RNA responses into protein responses better than a correlation map and cognate transcripts. The direction of gene-to-gene regulation, however, is not recovered from observational data. On the CITE-seq screens, fine-tuning only the latent network improves held-out response correlation, mainly by learning a response shared across knockouts. On larger Perturb-seq screens, with about 1,000 training perturbations, fine-tuning the latent network learns gene-specific effects that transfer to held-out genes, more so than a gene-level causal model fine-tuned on the same cells, and in simulation, such interventions also restore edge orientations that observational training leaves unresolved.

---

中文笔记基于标题和摘要生成，未核验全文；研究建议不代表论文已验证的结论。相关性分数不是论文质量评分。

检索统计：窗口 [2026-11-22 00:00, 2026-11-25 00:00) UTC；抓取 arxiv 50/biorxiv 125/pubmed 52 → 粗筛 47 篇 → LLM 选中 3 篇
