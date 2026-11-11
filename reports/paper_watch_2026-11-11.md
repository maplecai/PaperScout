# Paper Scout 日报 2026-11-11

共推荐 **6** 篇论文。

## 1. Long-range regulatory sequence models reveal a phylogenetic boundary in vertebrate genome evolution

bioRxiv · 预印本 · 2026-11-10 · 相关性 8/10

**研究关联：方法可借鉴**

- **为什么值得看**：直接使用sequence-to-function模型研究长程调控序列，且系统比较长上下文vs短上下文对调控预测的贡献，与我的核心研究高度契合。
- **任务与验证范围**：输入：20kb或1kb基因组序列 → 输出：调控活性二分类；研究物种/体系：6种脊椎动物（跨4.35亿年进化）；细胞体系摘要未说明；验证范围：跨物种泛化（跨细胞类型摘要未说明）
- **核心方法**：训练长上下文序列到功能二分类模型（FunFormer，读取20kb），与架构和参数匹配的1kb读取模型对照，结合跨物种迁移与计算机模拟侧翼序列替换评估长程信息贡献。
- **主要发现与证据**：种内长上下文模型比3个已发表的1kb分类器提升1.0-3.8个百分点；跨物种时长程信息贡献随进化距离衰减并在320-435 Mya反转，而局部序列仍可转移到鱼类；替换为GC匹配侧翼序列在哺乳动物间损失8个百分点，但哺乳动物模型用于鱼类时源侧翼与目标侧翼效果无异。
- **可借鉴点（研究建议）**：论文中替换侧翼序列为GC匹配序列以剥离长程信息贡献的干预实验范式，可推测并建议用于评估预训练模型中 padding 序列对预测结果的真实影响，但需注意 padding 与真实侧翼序列的本质差异。
- **迁移边界**：原论文探究的是跨物种真实侧翼序列的进化共享边界，而我的研究关注跨细胞类型增强子活性及预训练模型 padding（非真实侧翼）的影响。跨物种的泛化衰减规律不能直接等同于跨细胞类型泛化，padding 的作用机制也与真实侧翼序列的调控互作不同。
- **阅读时核实**：FunFormer模型在处理20kb上下文时，对超出中心1kb的侧翼序列是否采用了特定的位置编码或注意力机制约束？这关系到长程信息是如何被模型捕获并区分于局部信息的。

[原文](https://www.biorxiv.org/content/10.64898/2026.11.09.765190v1) · [DOI](https://doi.org/10.64898/2026.11.09.765190)

作者：Le, B., Nguyen, H., Gronvold, L., Sandve, S. R., Frei, O., Andreassen, O. A., Truong, T. T., Nguyen, D. T.
来源标注的末位/通讯作者：Dat Thanh Nguyen
机构：Institute of Clinical Medicine, University of Oslo, Oslo, Norway

### 英文摘要

Regulatory activity at a locus depends on local sequence and on long-range interactions with sequence further away, but how long each kind of information stays shared between genomes over evolution is unknown. Here we use sequence-to-function models as a comparative assay, training FunFormer, a long-context binary classifier that reads 20 kb, together with an architecture- and parameter-matched control that reads only the central 1 kb, in six vertebrates spanning 435 million years, and measuring what each retains when applied to another genome. Within species, the long-context model outperformed three published 1 kb classifiers by 1.0 to 3.8 percentage points in every genome, a gain that came from context rather than architecture. Across species, its contribution decayed with divergence, was near zero at the amniote split and reversed between 320 and 435 Mya, while local sequence still transferred into fish. Zebrafish and Atlantic salmon, which share their divergence from tetrapods but differ by the salmonid genome duplication, behaved alike, so the reversal is not explained by the salmonid duplication. An in silico flank intervention showed that replacing the flank with GC-matched sequence from the target genome cost 8 percentage points among mammals. When a mammalian model was applied to fish, a flank drawn from the source genome on average performed as well as the target's own flank, so the model drew nothing from the fish flank that an arbitrary source-genome flank did not provide. The long-range information that these models learn therefore stops being shared between vertebrate genomes well before the local information does. The same boundary sets a practical rule for reusing models in species without their own data, where long context helps among close relatives but is a liability across deep splits, and in variant scoring most foreign models matched a native model in data-limited pig but none did in human.

---

## 2. mRNABench: A curated benchmark for mature mRNA property and function prediction

bioRxiv · 预印本 · 2026-11-10 · 相关性 8/10

**研究关联：方法可借鉴**

- **为什么值得看**：直接评估核苷酸基础模型在序列到功能（mRNA属性预测）任务上的表现，高度契合DNA语言模型与序列到功能的研究兴趣。
- **任务与验证范围**：输入：成熟mRNA序列嵌入；输出：mRNA属性与功能预测；研究物种/细胞体系：人类转录本；验证范围：13个数据集和81个预测任务，跨细胞类型情况摘要未说明。
- **核心方法**：基于自监督核苷酸基础模型提取序列嵌入，在多任务基准上进行系统评估与对比。
- **主要发现与证据**：构建了涵盖13个数据集和81个任务的基准，对29个模型家族进行了75万次实验，揭示了参数缩放、序列压缩率、数据划分策略及自监督训练目标对预测性能的影响。
- **可借鉴点（研究建议）**：可借鉴其评估预训练模型时对序列压缩率与性能相关性的分析思路，推测这有助于探究不同padding策略对增强子序列表征质量的潜在影响。
- **迁移边界**：原论文聚焦人类成熟mRNA序列的属性预测，而我的研究聚焦DNA序列的增强子活性预测及虚拟表观遗传特征；mRNA与增强子在序列上下文和调控机制上存在本质差异，且原论文未直接评估padding策略，其泛化结论不可直接迁移至跨细胞类型的增强子任务。
- **阅读时核实**：原文在评估29个基础模型时，是否统一了输入序列的长度截断或padding处理方式，以排除预处理差异对下游mRNA属性预测性能的干扰？

[原文](https://www.biorxiv.org/content/10.1101/2025.07.05.662870v1) · [DOI](https://doi.org/10.1101/2025.07.05.662870)

摘要提供的链接（未核验可用性）：[资源 1](https://github.com/morrislab/mRNABench)

作者：Shi, R., Dalal, T., Fradkin, P. et al. (13 authors)
来源标注的末位/通讯作者：Quaid Morris
机构：Memorial Sloan Kettering Cancer Center

### 英文摘要

Messenger RNA (mRNA) is central to gene expression, and its half-life, localization, and translation efficiency drive phenotypic diversity in eukaryotic cells. While supervised learning has been used to study the mRNA regulatory code, self-supervised foundation models support a wider range of transfer learning tasks. However, the dearth of standardized benchmarks limits efforts to pinpoint the strengths of various models. Here, we present mRNABench, a benchmarking suite for mature mRNA biology, focused on human transcripts, that evaluates the representational quality of mature mRNA embeddings from self-supervised nucleotide foundation models. We curate 13 datasets and 81 prediction tasks that broadly capture salient properties of mature mRNA, and assess the performance of 29 families of nucleotide foundation models for a total of 750k experiments. Using these experiments, we study parameter scaling, correlations between sequence compressibility and performance, data-splitting strategies, and the effects of self-supervised training objective on mRNA property prediction. mRNABench can be found at: https://github.com/morrislab/mRNABench.

---

## 3. Disentangled generative modeling of single-cell perturbation responses across dynamic cellular states

bioRxiv · 预印本 · 2026-11-10 · 相关性 7/10

**研究关联：方法可借鉴**

- **为什么值得看**：解耦单细胞扰动响应的深度生成模型，直接对应research_interests中的single-cell perturbation方向。
- **任务与验证范围**：输入：单细胞扰动转录组数据（含批次、细胞周期等混杂因素） → 输出：解耦的细胞状态组成变化与状态门控的转录响应；研究体系：人类 CD8+ 和 CD4+ T 细胞；验证范围：跨细胞类型（CD4+/CD8+ T细胞）及模拟基准
- **核心方法**：PertVI，一种基于解耦变分推断的深度生成模型，将基线状态、批次效应与扰动效应分离至正交隐空间。
- **主要发现与证据**：PertVI 能准确解耦生物学轴并恢复微弱扰动特征；在人类 T 细胞筛选中，成功区分了记忆前体佐剂与毒性表型，解析了标准流程掩盖的双相反弹轨迹，并发现表型转变与广泛的转录扰动解耦，受状态特异性脉冲调控。
- **可借鉴点（研究建议）**：PertVI 将不同来源的方差解耦到正交隐空间的思想，可推测用于在多细胞类型增强子活性预测中分离细胞类型特异性表观遗传特征与序列固有特征。
- **迁移边界**：原论文处理的是单细胞转录组空间的扰动解耦，而我的任务是 DNA 序列到增强子活性的映射及 padding 评估；其解耦机制依赖于单细胞数据的隐空间结构，不能直接证明在 DNA 序列模型的 padding 或序列特征解耦上有效，跨任务迁移需重新设计编码器与解耦约束。
- **阅读时核实**：PertVI 的正交异常空间是如何在模型架构和损失函数层面实现的？这种正交约束是否对输入特征的维度或分布有特定要求？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.07.765083v1) · [DOI](https://doi.org/10.64898/2026.11.07.765083)

作者：Wang, Y., Zhao, Y., Li, S., Yang, D.
来源标注的末位/通讯作者：Yue Wang
机构：UNIVERSITY OF PITTSBURGH

### 英文摘要

Single-cell perturbation studies are increasingly conducted across complex, multi-condition biolog-ical systems, offering a powerful lens into how interventions reshape cell states and molecular pro-grams. However, standard computational models compress single-cell profiles into unified repre-sentations where treatment effects are obscured by cell division, lineage progression, donor varia-tion, and cellular stress. Here, we present Disentangled Variational Inference for Perturbation Re-sponse (PertVI), a deep generative model that separates baseline mitotic phase, cellular state, and batch effects from treatment-induced shifts while isolating aberrant off-manifold responses in or-thogonal anomaly space. This structured design tackles two intertwined tasks: (1) quantifying treatment-induced changes in cell-state composition, and (2) inferring state-gated transcriptional changes in response to treatment. Across simulated benchmarks, PertVI accurately disentangles coupled biological axes and recovers weak treatment signatures. In conditional chemical and genet-ic screens of primary human CD8+ and CD4+ T cells, PertVI separates memory-precursor adju-vants from toxic phenocopies, resolves co-clustered regulators into directional kinetic trajectories and biphasic rebounders obscured by standard workflows, and reveals that treatment-induced phe-notypic shifting is decoupled from broad transcriptional perturbation responses and instead gov-erned by state-specific impulses. Altogether, PertVI brings unique mechanistic granularity to sin-gle-cell perturbation response modeling, serving as a proof of principle for biology-informed, struc-ture-guided variance disentanglement in dynamic cellular systems.

---

## 4. CPDD: Adapting an autoregressive DNA language model for bidirectional phage genome modeling

bioRxiv · 预印本 · 2026-11-10 · 相关性 6/10

**研究关联：方法可借鉴**

- **为什么值得看**：DNA语言模型的双向化方法（自回归→扩散）与基因组基础模型和DNA语言模型研究直接相关，且涉及上下文条件建模。
- **任务与验证范围**：输入：含掩码或损坏的噬菌体DNA序列 → 输出：序列恢复/生成及下游表征预测；研究物种/细胞体系：噬菌体基因组；验证范围：522个噬菌体CDSs、infA fitness预测、七类毒粒蛋白亚型分类（摘要未说明跨细胞类型验证）
- **核心方法**：基于自回归DNA语言模型初始化的双向离散扩散模型，结合掩码和均匀替换训练，并采用多尺度上下文课程学习。
- **主要发现与证据**：CPDD在522个噬菌体CDSs上的随机掩码恢复精度优于可比扩散模型，混合损坏测试中恢复42.4%可见错误碱基；冻结表征支持fitness预测和蛋白亚型分类；长程序列恢复仍有改进空间。
- **可借鉴点（研究建议）**：其多尺度上下文课程学习及对可见上下文依赖性的评估思路，或可为探究预训练模型在不同序列长度或padding条件下的表征能力提供方法参考。
- **迁移边界**：原论文针对噬菌体长基因组序列的生成与恢复，与基于短游离型DNA序列预测增强子活性的任务存在本质差异；其上下文处理机制能否直接迁移至真核增强子序列及padding影响评估尚未经证明。
- **阅读时核实**：原文中“whole-source context curriculum”的具体实现方式，以及模型在处理不同长度上下文时是否涉及padding策略及其对长程序列恢复的具体影响？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.07.765118v1) · [DOI](https://doi.org/10.64898/2026.11.07.765118)

作者：ding, h., Wu, N., Qiu, T.
来源标注的末位/通讯作者：Nannan Wu
机构：CreatiPhage Biotechnology Co., Ltd

### 英文摘要

Autoregressive DNA language models generate sequences ef[fi]ciently from left to right, but many genome-analysis and sequence-editing problems are naturally conditioned on both [fl]anks. We introduce CreatiPhage, a 144.5M-parameter autoregressive DNA language model for bacteriophages, and its diffusion extension, CreatiPhage Diffusion DNA-LM (CPDD). CPDD is a 147.5M-parameter bidirectional discrete diffusion model initialized from the six-epoch CreatiPhage checkpoint. CPDD retains the pretrained Transformer, block attention residuals, and Engram conditional memory, while introducing non-causal attention, a MASK-aware base-5 Engram, centered depthwise convolution, and position-aligned nucleotide readout. Training combines masked and GIDD-style uniformly substituted bases with nucleotide- and amino-acid-level losses over a 10 kb, 32 kb, and whole-source context curriculum. On a screened panel of 522 phage CDSs, CPDD achieves higher random-mask restoration accuracy than a comparable diffusion model and performs well above codon-level references. In a mixed-corruption test, it restores 42.4% of visible incorrect bases. Frozen CPDD representations also support infA [fi]tness prediction and seven-class phage virion protein subtype classi[fi]cation. Controlled evaluations further characterize how restoration depends on visible context and identify opportunities to improve longer-range sequence recovery. Together, these results support scaffold-conditioned sequence modeling as a step towards modular design of phage genomes.

---

## 5. LingoCell interprets gene perturbations through natural language and tissue niches

bioRxiv · 预印本 · 2026-11-10 · 相关性 6/10

**研究关联：研究兴趣拓展**

- **为什么值得看**：涉及单细胞基础模型与计算扰动预测，与我的representation learning和single-cell perturbation兴趣间接相关。
- **任务与验证范围**：输入：单细胞与空间转录组数据及自然语言；输出：细胞注释、批次整合、描述生成及单基因/组合虚拟扰动读数；物种/体系：人肺腺癌与结直肠癌组织；验证范围：跨批次、跨组织（无单细胞参考的空间注释）。
- **核心方法**：结合单细胞与空间转录组的基础模型，采用多模态对齐范式将细胞表示与自然语言对齐并保持基因表达可编辑。
- **主要发现与证据**：在肺腺癌中揭示联合削弱肺泡分化与增强恶性程序的协同疾病响应；在结直肠癌中发现同一成纤维细胞状态向T细胞、巨噬细胞和肿瘤细胞传递不同程序。
- **可借鉴点（研究建议）**：无明显直接启发
- **迁移边界**：原论文聚焦转录组表达量与空间微环境的语言对齐及扰动，与基于DNA序列预测增强子活性的任务模态完全不同；其跨组织泛化能力不适用于评估序列模型中padding的影响。
- **阅读时核实**：模型在保持“基因表达可编辑”时，具体采用了何种架构设计来支持组合式虚拟扰动，且该机制是否依赖特定的基因token化方式？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.08.765157v1) · [DOI](https://doi.org/10.64898/2026.11.08.765157)

作者：Yang, Y., Xu, W., Zhang, Z., Cui, Y., Yu, X., Gu, W., Wang, J., Nakai, K.
来源标注的末位/通讯作者：Kenta Nakai
机构：Human Genome Center, The Institute of Medical Science, The University of Tokyo, Tokyo, Japan; Department of Computational Biology and Medical Science, The Unive

### 英文摘要

Single-cell foundation models are general tools for resolving cell identities and disease states, but struggle to interpret changes in expression magnitude in biological language, to transfer to sparse spatial measurements, and to explain cellular niches. We introduce LingoCell, a foundation model connecting single-cell and spatial transcriptomics. It aligns cell representations with language while keeping gene expression editable, supporting cell annotation, cross-batch integration, description generation, and disease-language readouts of single-gene and combinatorial in silico perturbations. Extended to tissues, it annotates cells without single-cell references, learns identity-conditioned niche embeddings, and performs spatial in silico perturbation by replacing and editing neighbor expression. In lung adenocarcinoma, LingoCell revealed synergistic disease responses to jointly weakening alveolar differentiation programs and strengthening malignant programs. In colorectal cancer, it revealed different programs conveyed by the same fibroblast state to T cells, macrophages, and tumor cells. LingoCell provides a unified framework for prioritizing target combinations and stromal intervention programs.

---

## 6. Simple models outperform single-cell foundation models on downstream benchmarks

bioRxiv · 预印本 · 2026-11-10 · 相关性 6/10

**研究关联：方法可借鉴**

- **为什么值得看**：对单细胞基础模型的批判性评估，在方法论精神上与评估基因组基础模型有效性的项目有相似之处。
- **任务与验证范围**：输入：scRNA-seq数据 → 输出：细胞类型分类、疾病状态预测等下游任务结果；研究物种/细胞体系：摘要未说明具体物种，但涉及跨物种；验证范围：包含跨细胞类型和跨物种的分布外（OOD）任务
- **核心方法**：基于仔细归一化与线性方法的简单可解释流水线，对比基于Transformer的单细胞基础模型。
- **主要发现与证据**：简单线性模型在多个单细胞基础模型基准测试上达到或接近SOTA，且在包含新细胞类型和生物体的OOD任务上优于基础模型，表明细胞身份可通过基因表达的简单线性表示捕捉。
- **可借鉴点（研究建议）**：在评估预训练基因组学模型在增强子预测等任务上的表现时，应引入基于简单统计特征或线性模型的严格基线，以验证深度模型带来的增益是否真实且不可替代。
- **迁移边界**：原论文针对scRNA-seq表达数据的统计结构，其“简单线性模型有效”的结论不能直接迁移至DNA序列到功能的映射任务；DNA序列的非线性语法结构可能无法被简单线性模型捕捉，故不可将此泛化结论直接套用于DNA序列预训练模型或padding策略的评估。
- **阅读时核实**：原文所使用的“仔细归一化”具体指什么流程？这些线性方法是否依赖于先验的基因注释或特征选择，从而在完全无监督的序列特征提取上缺乏可比性？

[原文](https://www.biorxiv.org/content/10.64898/2026.02.11.705358v1) · [DOI](https://doi.org/10.64898/2026.02.11.705358)

作者：Souza, H., Mehta, P.
来源标注的末位/通讯作者：Pankaj Mehta
机构：Boston University

### 英文摘要

Single-cell RNA sequencing (scRNA-seq) data exhibit strong and reproducible statistical structure. This has motivated the development of large-scale foundation models, such as TranscriptFormer, that use transformer-based architectures to learn a generative model for gene expression by embedding genes into a latent vector space. These embeddings have been used to obtain state-of-the-art (SOTA) performance on downstream tasks such as cell-type classification, disease-state prediction, and cross-species learning. Here, we ask whether similar performance can be achieved without utilizing computationally intensive deep learning-based representations. Using simple, interpretable pipelines that rely on careful normalization and linear methods, we obtain SOTA or near SOTA performance across multiple benchmarks commonly used to evaluate single-cell foundation models, including outperforming foundation models on out-of-distribution tasks involving novel cell types and organisms absent from the training data. Our findings highlight the need for rigorous benchmarking and suggest that the biology of cell identity can be captured by simple linear representations of single cell gene expression data.

---

中文笔记基于标题和摘要生成，未核验全文；研究建议不代表论文已验证的结论。相关性分数不是论文质量评分。

检索统计：窗口 [2026-11-08 00:00, 2026-11-11 00:00) UTC；抓取 biorxiv 112/pubmed 54 → 粗筛 34 篇 → LLM 选中 6 篇
