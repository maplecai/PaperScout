# Paper Scout 日报 2026-09-08

共筛选出 **6** 篇推荐论文。
📊 抓取 biorxiv 337/pubmed 30 → 粗筛 100 篇 → LLM 选中 6 篇

## 1. BOTANIC-1: a series of long-context plant genomic foundation models in the agentic era

- **期刊**: bioRxiv
- **作者**: Barozet, A., Cabeli, V., Ogier du Terrail, J. et al. (10 authors)
- **机构**: Jean Ogier du Terrail @ Living Models
- **日期**: 2026-09-07
- **ID**: DOI: 10.64898/2026.09.04.749355  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.04.749355v1
- **一句话推荐**: 植物基因组语言模型，直接涉及DNA language model、基因组基础模型的自监督训练与可解释性分析，与你的genomic foundation model研究兴趣高度契合。
- **方法**: 基于自监督学习的植物基因组语言模型（gLM）系列，支持最高128kbp长上下文并可通过LLM代理调用的混合系统。
- **主要发现**: 该模型在较小预算下于多项植物基因组任务上超越现有模型，且机制可解释性分析揭示了其能学习到编码区边界和剪接位点等具有生物学意义的序列特征。
- **对我的启发**: 其对长上下文（最高128kbp）序列处理能力的探讨及机制可解释性分析方法，可为评估预训练基因组学模型在不同padding策略下对长序列增强子活性预测的影响提供参考。

<details><summary>Abstract</summary>

The development of climate-resilient crops would be greatly accelerated by models able to reason directly over plant genomic sequences and to pinpoint trait-associated regions or loci. Anticipating the impact of DNA base changes (variants) remains challenging, and understanding regulatory mechanisms is still an active area of research. Through self-supervised training on unannotated genomic data, genomic language models (gLMs) can learn DNA syntax and grammar that go beyond current annotations, thus complementing standard bioinformatics analyses that rely on rules established by decades of genomics research. Here we present our agent-powered Model Factory and its first outputs: the Botanic1 family of gLMs designed for plant research, which operates reliably on sequences from hundreds of base pairs up to 128 kbp. These models outperform all generalist and plant-specific gLMs (as well as specialised baselines) on one of the largest sets of plant genomics evaluation tasks reported to date, at a much smaller budget than concurrent models. Mechanistic interpretability analysis identifies features associated with biologically meaningful sequence properties including coding region boundaries and splice site motifs, demonstrating that these models are a source of biological insight beyond their benchmark performance. Finally, because a gLM only becomes practically useful when embedded in a broader workflow, we integrate Botanic1 as a specialised genomic layer callable by a generalist large language model (LLM) agent, illustrating how such hybrid systems could accelerate plant biology research. To support the plant genomics research community, we will release Botanic1-S, Botanic1-M and Botanic1-L for research use at https://huggingface.co/collections/living-models/botanic1-6a97f4e3c33f3d109a75057d

</details>

---

## 2. Motif-based model of transcription predicts effects of sequence variants in AR enhancers and reveals distinct functions for AR-associated transcription factors

- **期刊**: bioRxiv
- **作者**: Taeb, H., Safaeesirat, A., Tekoglu, E., Xiao, K., Huang, C.-C. F., Lack, N. A., Emberly, E.
- **机构**: Eldon Emberly @ Simon Fraser University
- **日期**: 2026-09-07
- **ID**: DOI: 10.64898/2026.09.02.748967  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.02.748967v1
- **一句话推荐**: 使用基于motif的可解释模型从STARR-seq数据预测AR增强子活性及序列变异效应，直接契合增强子活性预测与sequence-to-function研究。
- **方法**: 基于motif的物理生物学可解释模型，通过拟合STARR-seq数据预测增强子活性及变异效应。
- **主要发现**: 模型将转录因子功能解耦为激素依赖、组成型和双功能三类，发现增强子诱导性受组成型激活因子饱和效应的负向调控；在单碱基分辨率预测突变效应表现优异并成功筛选GWAS风险变异。
- **对我的启发**: 将增强子活性拆分为基线与诱导性分别建模以解耦调控因子功能的思路，可启发我在不同细胞类型或表观遗传状态下对增强子活性进行解耦分析。

<details><summary>Abstract</summary>

Androgen receptor (AR)-mediated transcription plays a central role in prostate cancer development and progression, yet the contributions of individual transcription factors (TFs) to AR-dependent enhancer activity remain incompletely understood. Here we use a biophysically motivated, interpretable motif-based model to dissect these contributions from STARR-seq data in LNCaP cells. By fitting the model separately to androgen inducibility and to baseline enhancer activity, we resolve TFs into three functional classes: hormone-dependent drivers, constitutive activators, and dual-role factors that contribute to both. These patterns suggest that inducibility is associated not only with the presence of AR and co-activator motifs, but also with the relative absence of constitutive activators that may saturate enhancer output. We validate the model against an independent saturation-mutagenesis dataset spanning 40 AR enhancers, predicting mutational effects at single-base resolution (AUC = 0.76), and show that direct fitting to these data independently recovers known AR regulators. Finally, we apply the model to prostate cancer GWAS risk alleles in AR binding site regions, prioritizing four candidate variants predicted to reduce the DHT/EtOH enhancer activity ratio at these loci.

</details>

---

## 3. PoolParty: streamlined design of DNA sequence libraries in Python

- **期刊**: bioRxiv
- **作者**: Liu, Z., Cordero, A., Kinney, J. B.
- **机构**: Justin Block Kinney @ Cold Spring Harbor Laboratory
- **日期**: 2026-09-05
- **ID**: DOI: 10.64898/2026.04.06.716802  |  URL: https://www.biorxiv.org/content/10.64898/2026.04.06.716802v1
- **一句话推荐**: PoolParty 专为 MPRA/DMS 序列库设计开发，直接服务于增强子活性预测和基因组AI模型探针实验。
- **方法**: 基于计算图范式的Python寡核苷酸池序列库设计工具包。
- **主要发现**: 通过提供丰富的内置操作和可视化审计功能，将复杂的序列库设计转化为结构化、可复现的流程，并支持系统性地探测基因组AI模型的响应。
- **对我的启发**: 可利用该工具包系统生成带有特定突变或序列插入的虚拟序列库，用于在计算机内探测预训练基因组学模型对padding或虚拟表观遗传特征变化的敏感性。

<details><summary>Abstract</summary>

Background: Computationally designed DNA sequence libraries are essential components of massively parallel reporter assays (MPRAs), deep mutational scanning (DMS) experiments, and other multiplex assays of variant effect (MAVEs). They are also increasingly used in silico to analyze genomic AI models. Designing these libraries, however, remains tedious and error-prone due to the scarcity of purpose-built software. Results: Here we describe PoolParty, a Python package that streamlines the design of complex oligo pools using a simple but flexible API. In PoolParty, each library is represented by a computational graph that can be specified in just a few lines of code. Over 50 built-in operations cover nucleotide- and codon-level mutagenesis, motif insertion, barcode generation, and more. PoolParty automatically generates informative names for each sequence and provides "design cards" detailing how each sequence was generated. Visualization methods let users quickly audit library content and inspect the underlying graph. PoolParty thus transforms oligo pool design from a tedious task requiring custom functions and scripts into a structured, transparent, and reproducible process. Conclusions: PoolParty streamlines the design of DMS, MPRA, and other multiplex assay libraries, and the design cards it provides can help researchers systematically probe and interpret genomic AI models. PoolParty can also be extended to support new assays and analysis strategies as they emerge.

</details>

---

## 4. RevPert: predicting candidate drivers of transcriptomic state transitions via gallery-native reverse perturbation

- **期刊**: bioRxiv
- **作者**: Liang, S., Yang, C., Wang, J., Li, y.
- **机构**: Shiyang Liang @ The No. 944 Hospital of Joint Logistic Support Force of PLA
- **日期**: 2026-09-06
- **ID**: DOI: 10.64898/2026.08.19.745674  |  URL: https://www.biorxiv.org/content/10.64898/2026.08.19.745674v1
- **一句话推荐**: 涉及基于Perturb-seq数据的转录组状态转变和反向扰动预测，与单细胞扰动研究兴趣相关。
- **方法**: RevPert是一种gallery-native反向扰动模型，通过结合带符号皮尔逊连通性先验与学习残差来对候选遗传扰动进行排序。
- **主要发现**: 该模型在多项Perturb-seq和基因敲除筛选中实现了最优的留出干预恢复效果，并在疾病耐药性对比中显著提升了预定义疾病锚点的排序准确性。
- **对我的启发**: 其将先验统计关系与学习残差相结合的范式，可启发在增强子活性预测中融合先验表观遗传特征与深度学习预测残差以优化模型性能。

<details><summary>Abstract</summary>

Cellular state transitions underlie adaptation, ageing and disease, yet prioritizing catalogued genetic perturbations whose expression signatures match an observed transcriptomic shift remains difficult. Most models predict phenotype from a nominated intervention, whereas genetic inverse benchmarks are largely restricted to within-screen identity recovery. Here we introduce RevPert, a gallery-native reverse perturbation model that ranks a fixed genetic catalog for a query contrast {Delta}Y* = YB - YA by combining signed Pearson connectivity with a learned residual. Across Replogle Essential Perturb-seq (four lines) and LINCS-KO screens (ten lines), RevPert recovered held-out interventions at leading performance relative to matched baselines. Applied to public drug-resistance contrasts in HCC and CML, dual-arm ranking placed pre-specified disease anchors far higher on the expected arms than ranking the same signatures by differential-expression magnitude alone (Essential residual model for HCC; a transductive GWPS residual for CML). RevPert therefore couples within-screen reverse ranking to a screen-external signed-geometry check; the latter calibrates literature anchors and is not claimed as held-out recovery.

</details>

---

## 5. Capsid-specialized protein language models reveal higher-order viral architecture from sequence

- **期刊**: bioRxiv
- **作者**: Liu, S., Xia, S., Wang, H.
- **机构**: Hong Wang @ Tongji university
- **日期**: 2026-09-07
- **ID**: DOI: 10.64898/2026.09.06.749605  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.06.749605v1
- **一句话推荐**: 蛋白质语言模型用于病毒衣壳序列表示学习，与你的DNA language model和representation learning for biological sequences有方法论上的类比性。
- **方法**: 基于预训练蛋白质语言模型微调构建衣壳专用模型 ESMCapsid，并利用稀疏自编码器对表征进行语义 motif 分解与三维结构映射。
- **主要发现**: 模型在宏基因组规模识别出大量同源性暗区衣壳蛋白，并证明语言模型表征能捕获超越序列相似性的高阶几何约束与结构谱系信息。
- **对我的启发**: 稀疏自编码器分解预训练表征以提取可解释语义 motif 的范式，可借鉴用于解析预训练基因组学模型在增强子序列上学习到的功能语法特征。

<details><summary>Abstract</summary>

Viral capsid proteins preserve information on higher-order shell architecture and deep evolutionary history, yet current capsid annotation relies predominantly on homology-based methods that have reduced sensitivity across highly divergent environmental sequences. Here we develop ESMCapsid, a capsid-specialized protein language model for remote capsid detection and architecture-aware representation learning. Screening 343 million representative metagenomic protein clusters revealed a large homology-dark capsid repertoire, with approximately 62% of candidates lacking matches to existing reference databases. Sparse autoencoder decomposition identified recurrent semantic motifs linking homology-dark proteins to known structural lineages, suggesting that interpretable higher-order architectural information can be recovered directly from capsid sequences at metagenomic scale. Mapping conserved motif cores onto resolved viral shells showed spatial clustering and restricted radial positions, indicating that ESMCapsid captures geometric constraints beyond sequence similarity alone. Together, our findings establish a sequence-based route to organize homology-dark viral diversity through conserved architectural principles, extending viral discovery beyond sequence homology.

</details>

---

## 6. Learning from tandem mass spectra at scale with a self-supervised foundation model for proteomics

- **期刊**: bioRxiv
- **作者**: Nieuwoudt, M., Reverenna, M., Patel, D. et al. (12 authors)
- **机构**: Konstantinos Kalogeropoulos @ Technical University of Denmark
- **日期**: 2026-09-07
- **ID**: DOI: 10.64898/2026.09.03.747733  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.03.747733v1
- **一句话推荐**: 虽然是蛋白质组学质谱的基础模型，但其自监督掩蔽重建的训练范式对DNA语言模型有一定参考价值。
- **方法**: 基于物理感知掩码重建目标训练的仅编码器Transformer自监督基础模型。
- **主要发现**: 该模型无需标签即可编码质谱的实验与生物学属性，并在从头测序等下游任务中实现跨数据集和仪器的鲁棒迁移。
- **对我的启发**: 其物理感知的掩码重建范式可启发在基因组学预训练中引入表观遗传调控先验以设计掩码目标。

<details><summary>Abstract</summary>

Mass spectrometry-based proteomics increasingly relies on machine learning, yet existing models are trained for defined supervised tasks such as peptide identification, de novo sequencing or fragment intensity prediction, limiting transfer across datasets, instruments and acquisition methods. Here we present InstaNovo-FM, a self-supervised foundation model for bottom-up proteomics trained to reconstruct masked regions of tandem mass spectra. We assemble a diverse training corpus spanning 1.47 billion MS/MS spectra and 184.6 million high-confidence annotations. We train an encoder-only transformer on the annotated tier using a physics-aware masked reconstruction objective. We demonstrate that the InstaNovo-FM embeddings encode fundamental experimental and biological properties, including fragmentation method, sequence properties and post-translational modifications, without requiring peptide labels. Furthermore, this foundation model directly enables diverse downstream applications, including de novo peptide sequencing, database-free identification and analytical run classification. InstaNovo-FM establishes a unified representation space for peptide fragmentation spectra, enabling robust transferability across the proteomics ecosystem.

</details>

---
