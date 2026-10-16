# Paper Scout 日报 2026-10-16

共筛选出 **4** 篇推荐论文。
📊 抓取 biorxiv 106/pubmed 77 → 粗筛 31 篇 → LLM 选中 4 篇

## 1. DNA-LLM2Vec: Architecture-Aware Task-Conditioned Adaptation of Decoder DNA Foundation Models

- **期刊**: bioRxiv
- **作者**: Liang, Y., Zhai, K., Gan, Y., Li, S., Shao, J., Watson, G. H., Poesio, M.
- **机构**: Yuan Liang @ Queen Mary University of London
- **日期**: 2026-10-14
- **ID**: DOI: 10.64898/2026.10.07.757259  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.07.757259v1
- **相关分数**: 9/10
- **一句话推荐**: 提出DNA-LLM2Vec框架改进DNA基础模型的表征学习，直接涉及基因组基础模型和序列到功能预测。
- **方法**: 提出DNA-LLM2Vec分阶段转换框架，结合掩码下一词预测与位置/链方向不变性对比学习，将单向Decoder DNA基础模型改造为双向编码器。
- **主要发现**: 模型转换收益高度依赖底层架构与任务结构；基于裁剪的位置对比学习对长上下文任务（如增强子-启动子互作）提升最大，双向上下文则特异性改善远距离变异效应预测。
- **对我的启发**: 针对增强子活性预测中的长序列padding问题，可借鉴其基于裁剪的位置对比学习策略，以增强模型对序列长度和位置偏移的鲁棒性，并提升对远距离调控上下文的建模能力。

<details><summary>Abstract</summary>

Decoder DNA foundation models pretrain with dense next-token prediction and scale to long sequences, but their representations are directional. This is a poor fit for genomic tasks that need sequence context both upstream and downstream of a locus. Bidirectional masked-language-model encoders supply this context, but they pretrain more sparsely and scale less easily to long windows. We introduce DNA-LLM2Vec, a staged decoder-to-encoder framework that opens bidirectional context, repairs the resulting mismatch with masked next-token prediction, and applies contrastive views encoding strand and positional invariance. We instantiate it on two architecturally distinct backbones, DNAGPT and HyenaDNA, and evaluate seven biological task families (grouped from GB, NT, GUE, and GUE+EPI) with frozen linear probing. The benefits of conversion are architecture-aware and task-conditioned rather than uniform. Crop-based positional contrastive learning helps most for the extended-context families (enhancer-promoter interaction and Virus-COVID), raising frozen Avg-EPI MCC to 27.5% for DNAGPT and 26.7% for HyenaDNA, whereas for shorter, local families the results depend on backbone and tokenisation. Beyond classification, bidirectional context and MNTP improve causal-eQTL variant-effect prediction specifically at distance, and a base-pair mutagenesis diagnostic shows that adaptation organises motif-aware contact structure while reverse-complement training imprints strand-consistent geometry, yet neither predicts the best downstream view. DNA-LLM2Vec therefore produces frozen bidirectional representations whose most effective adaptation view depends on the task structure and the backbone. Code and checkpoints are available at https://github.com/semi-nothing/dna-llm2vec.

</details>

---

## 2. Deep learning uncovers hidden power of low-affinity motifs.

- **期刊**: Cell genomics
- **作者**: Grace Bower, Evgeny Z Kvon
- **机构**: Evgeny Z Kvon @ Department of Developmental and Cell Biology, University of California, Irvine, Irvine, CA, USA; Department of Systems Biology, University of California, Irvine, Irvine, CA, USA. Electronic address: ekvon@uci.edu.
- **日期**: 2026-10-14
- **ID**: DOI: 10.1016/j.xgen.2026.101392  |  PMID: 42874569  |  URL: https://pubmed.ncbi.nlm.nih.gov/42874569/
- **相关分数**: 7/10
- **一句话推荐**: 使用 sequence-to-function 深度学习模型研究转录因子结合位点和染色质开放，与调控基因组学高度相关。
- **方法**: 基于sequence-to-function深度学习模型系统性映射低亲和力转录因子结合位点。
- **主要发现**: 发现低亲和力结合位点通过软语法核小体协同作用驱动染色质开放。
- **对我的启发**: 在预测游离型增强子活性时，可利用虚拟表观遗传特征探究低亲和力motif的协同作用，并评估预训练模型padding策略对弱信号motif特征提取的影响。

<details><summary>Abstract</summary>

Low-affinity transcription factor binding sites are functionally important but difficult to map and mechanistically poorly understood. In this issue of Cell Genomics, Weilert et al. leverage sequence-to-function deep learning models to systematically map low-affinity pioneer factor binding sites in mouse embryonic stem cells and reveal how these sites contribute to chromatin opening through soft-syntax nucleosomal cooperativity.

</details>

---

## 3. SVC: A Vision Transformer-based Spatially and Virtually Embedded Cell Model for Deciphering Subcellular Spatial Transcriptomic Heterogeneity

- **期刊**: bioRxiv
- **作者**: Wan, H., Yang, P., Hou, S., Wang, J., Zhou, X.
- **机构**: Xiang Zhou @ Yale University
- **日期**: 2026-10-14
- **ID**: DOI: 10.64898/2026.10.07.757371  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.07.757371v1
- **相关分数**: 7/10
- **一句话推荐**: 提出虚拟细胞模型(SVC)并支持in silico扰动，与我的“virtual cell”和“single-cell perturbation”研究兴趣高度契合。
- **方法**: 基于Vision Transformer的亚细胞转录本空间上下文学习模型，将基因定位转化为图像patch并利用同细胞内其他基因作为上下文进行表征。
- **主要发现**: SVC能准确预测细胞特异性亚细胞转录本定位并跨平台泛化，揭示了常规细胞级分析无法获取的亚细胞空间组织异质性，且其表征可迁移至细胞和组织级下游任务。
- **对我的启发**: 将目标特征转化为图像patch并利用同局部环境内其他特征作为上下文的表征范式，可启发我们在预测细胞类型特异性增强子活性时，构建基于局部序列上下文或虚拟表观遗传特征空间分布的Transformer输入策略。

<details><summary>Abstract</summary>

Subcellular transcript localization shapes gene regulation and cellular function, yet profiling it at scale remains difficult, limiting our ability to study subcellular heterogeneity across tissues and disease. Here, we present SVC, a Vision Transformer-based spatially and virtually embedded cell model that learns subcellular transcript organization within native tissue context directly from subcellular-resolution spatial transcriptomics. SVC represents each gene's subcellular localization as an image patch and uses other genes within the same cell as context, enabling subcellular contextual learning of spatial dependencies that govern intracellular organization. By integrating gene-function priors, cell morphology, spatial context, and, when available, cell identity, SVC captures unified, spatially grounded representations across genes and cells that connect subcellular organization to cellular state and tissue microenvironment. Across diverse subcellular-resolution spatial transcriptomics datasets, SVC accurately predicts cell-specific subcellular transcript localization and co-organization, generalizes across tissues and technical platforms, and supports subcellular imputation of unmeasured genes and in silico perturbation. Leveraging these capabilities, SVC highlights disease-associated patterns of intracellular transcript reorganization and spatially heterogeneous responses to gene perturbations. Beyond prediction, SVC reveals systematic variation in subcellular transcript organization associated with gene function, cellular states, and tissue microenvironments, uncovering de novo spatial biology that is not accessible by cell-level analysis. SVC's learned representations further transfer to cell- and tissue-level tasks, including cell-level expression imputation, cell clustering, and spatial domain detection. Together, SVC provides a general framework for modeling and interrogating subcellular transcript organization in situ, enabling scalable discovery of subcellular spatial biology.

</details>

---

## 4. Programmable design of functional RNAs through multimodal generative learning

- **期刊**: bioRxiv
- **作者**: Ma, J., Zhu, J., Huang, W. et al. (14 authors)
- **机构**: Qiangfeng Cliff Zhang @ State Key Laboratory of Membrane Biology, Beijing Advanced Innovation Center for Structural Biology & Frontier Research Center for Biological Structure, School 
- **日期**: 2026-10-15
- **ID**: DOI: 10.64898/2026.10.14.759035  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.14.759035v1
- **相关分数**: 7/10
- **一句话推荐**: 多模态生成模型学习RNA序列到功能的映射并进行可编程设计，与sequence-to-function和enhancer design高度平行。
- **方法**: 多模态条件化生成模型 RNAverse，联合学习 RNA 序列、实验结构探测谱与功能注释，通过 in-painting 与迭代优化实现从预测到生成式设计的统一范式。
- **主要发现**: 该模型在 16 项预测任务上达到 SOTA，并以 ≤20 个候选的极低实验成本生成跨四类 RNA 的功能性序列，包括提升基因治疗与疫苗 UTR 表达的临床级优化结果，显著优于理性设计与大规模筛选。
- **对我的启发**: 其将结构/功能注释作为条件模态注入序列模型的思路，可迁移至将虚拟表观遗传特征作为细胞类型条件输入增强子活性预测模型；in-painting 评估范式亦可借鉴用于量化预训练模型 padding 区域对序列功能预测的扰动影响。

<details><summary>Abstract</summary>

RNA engineering is bottlenecked by the tight coupling among sequence, structure, and function, leaving the field reliant on heuristics or screening. We introduce RNAverse, a multimodal generative model that learns a conditionable design grammar from RNA sequences, experimental structural probing profiles, and functional annotations. Beyond setting a new state of the art across 16 predictive modeling tasks, RNAverse inverts into generative design across four distinct RNA classes through three regimes, requiring experimental testing of no more than 20 candidates per-task. Zero-shot in-painting generates snoRNAs that promote premature termination codon (PTC) readthrough, and chimeric aptazymes for ligand-controlled gene regulation, exceeding rational design or large-scale screens. In both settings, RNAverse outperforms family-adapted sequence-only baselines. Fine-tuned in-painting extends to an unseen functional class, yielding IGFBP3-binding aptamers with picomolar affinity that outperform SELEX winners. Iterative optimization engineers 5' UTRs that outperform clinical benchmarks, enhancing protein production in cell-based assays for both the Zolgensma gene therapy and the BNT162b2 COVID-19 vaccine, and boosting antibody responses to BNT162b2 in mice. Together, these results establish multimodal generative learning as a route from predictive RNA modeling to programmable specification of functional RNAs.

</details>

---
