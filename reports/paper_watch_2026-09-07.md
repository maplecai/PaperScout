# Paper Scout 日报 2026-09-07

共筛选出 **6** 篇推荐论文。
📊 抓取 arxiv 8/biorxiv 348/pubmed 21 → 粗筛 100 篇 → LLM 选中 6 篇

## 1. Global tree encoding of atlas-scale single-cell genomics

- **期刊**: bioRxiv
- **作者**: Kiyota, B., Lee, C., Yao, H., Yachie, N.
- **机构**: Nozomu Yachie @ The University of British Columbia
- **日期**: 2026-09-04
- **ID**: DOI: 10.64898/2026.08.31.747971  |  URL: https://www.biorxiv.org/content/10.64898/2026.08.31.747971v1
- **一句话推荐**: 提出大规模单细胞数据的树状表示框架，支持foundation model benchmarking和生成模型训练，与virtual cell和表示学习兴趣相关。
- **方法**: 提出MILK框架，通过构建全局树状层级结构对大规模单细胞基因组数据进行编码与代表性子采样。
- **主要发现**: 该方法在保留稀有细胞群信息的前提下实现数据降维，支持深度生成模型训练和基础模型基准测试，并能捕获多分辨率的细胞全局发育轨迹与跨组织扰动。
- **对我的启发**: 在训练或评估预训练基因组学模型时，可借鉴其层级化代表性子采样策略处理大规模异质性数据，避免随机下采样导致稀有细胞类型增强子特征信息的丢失。

<details><summary>Abstract</summary>

The rapid expansion of single-cell genomic datasets has led to the compilation of biological resources comprising hundreds of millions of cells across tissues, developmental stages, and disease states. This has underscored the need for scalable and interpretable data representations that preserve the complex relationships and multi-scale organization of cellular states, while remaining computationally tractable at atlas scale. Existing approaches based on discrete abstractions have enabled cell annotation, clustering, and trajectory inference, but are often optimized for local inference tasks and may obscure continuous cellular relationships and multi-resolution structure within complex transcriptional and other genomic landscapes. Moreover, increasing dataset sizes often require information-reduction strategies such as random downsampling, limiting the resolution of rare cell populations and heterogeneous cellular states. Here, we present MILK, a scalable computational framework that organizes high-dimensional single-cell populations into unified tree representations. Across large-scale transcriptomic atlases, MILK enables representative subsampling with preserved information, supporting the tractable application of existing algorithms for tasks including deep generative model training and foundation model benchmarking. Additionally, MILK enables holistic, multi-resolution analyses that capture global developmental trajectories, characterize disease-associated cellular perturbations across tissues, and facilitate comparison of transcriptional programs across species within a coherent hierarchical framework. Together, these results establish the hierarchical organization of biological data as a scalable and unifying representation of cellular identity, enabling integrative analysis of single-cell genomic data across diverse contexts.

</details>

---

## 2. Design and experimental characterization of specificity-switching mutational paths of WW domains

- **期刊**: bioRxiv
- **作者**: Rehan, A., Mauri, E., Fernandez-De-Cossio-Diaz, J., Brun, P.-G., Monasson, R., Ribezzi-Crivellari, M., Cocco, S.
- **机构**: Simona Cocco @ ENS
- **日期**: 2026-09-04
- **ID**: DOI: 10.64898/2025.12.08.693000  |  URL: https://www.biorxiv.org/content/10.64898/2025.12.08.693000v1
- **一句话推荐**: 使用RBM等无监督学习方法进行蛋白质序列的表示学习与功能设计，与生物序列表示学习及序列到功能映射有间接方法学关联。
- **方法**: 结合受限玻尔兹曼机（RBM）无监督学习同源序列特征与路径采样方法，设计并验证蛋白质特异性转换的突变路径。
- **主要发现**: RBM设计的突变路径中绝大多数中间序列保持功能且优于随机突变，证明了上位性相互作用建模在功能转换中的关键作用，且该路径与祖先序列重建结果高度一致。
- **对我的启发**: RBM对序列上位性相互作用的建模思路，可启发在评估预训练基因组学模型时，探究padding等序列扰动如何影响局部上下文的非线性特征提取与功能预测。

<details><summary>Abstract</summary>

Specific interactions between proteins and other biomolecules are ubiquitous in cellular processes.How specificity is encoded in the protein sequence and can be modified through a minimal set of concerted mutations is a complex issue. In this work, we focus on the WW protein domain, whose variants specifically bind to different classes of proline-rich peptides. Combining unsupervised learning of homologous WW sequence data with Restricted Boltzmann Machines (RBM) and path-sampling methods, we design mutational paths of putative WW domains interpolating between two natural WW domains with either distinct or similar specificities. Sequences along the designed paths are then experimentally validated with high-throughput in-vitro binding assays against 3 peptides of different classes. The vast majority (93%) of intermediate sequences along the designed paths are responsive to the initial or/and final peptides. On the contrary, domains along scrambled paths, in which the same mutations are introduced in random order are not functional, emphasizing how successful design crucially depends on the ability to model epistatic interactions. Switch in specificity between classes I and IV, whose representative peptides bind to different pockets on the WW domain takes place through intermediates displaying some level of binding cross-reactivity with the tested peptides, contrary to the transition from class I to II, which are associated with the same binding pocket. Lastly, we show that the RBM paths share a high identity with internal nodes obtained from ancestral sequence reconstruction based on the seed WW domains.

</details>

---

## 3. Gene function prediction from bulk coexpression is bounded by cell-type-level signal

- **期刊**: bioRxiv
- **作者**: Adrian-Hamazaki, A., Pavlidis, P.
- **机构**: Alexander Adrian-Hamazaki @ BC Cancer Research Center
- **日期**: 2026-09-04
- **ID**: DOI: 10.64898/2026.08.31.748380  |  URL: https://www.biorxiv.org/content/10.64898/2026.08.31.748380v1
- **一句话推荐**: 揭示了bulk共表达基因功能预测受限于细胞类型层面信号，与我关注的细胞类型特异性调控预测问题有方法论上的呼应。
- **方法**: 基于bulk共表达与细胞类型谱的基因功能预测模型解析与对比分析。
- **主要发现**: 基于bulk共表达的基因功能预测性能主要受限于细胞类型级别的分辨率，而非精细的生化功能；使用细胞类型谱能提升预测效果与可解释性。
- **对我的启发**: 在基于虚拟表观遗传特征预测增强子活性时，需警惕预训练模型是否仅捕获了粗粒度的细胞类型特异性信号而非精细的序列-功能映射，并评估padding策略对此分辨率的影响。

<details><summary>Abstract</summary>

It is widely accepted in genomics that coexpression of RNA transcripts suggests a commonality of function. This intuition is explicitly leveraged in machine learning methods that predict gene function, where it is often combined with other features such as protein interactions and sequence similarity. For example, including coexpression data from human tissue expression boosts performance for predicting Gene Ontology annotations. However, the biological underpinnings of this observation have not been well-investigated. Building on earlier results from our group, in this work we show that gene function is predictable from coexpression substantially because it reflects differences in expression between cell types, and these differences are also intrinsic to the ground truth labels. Using simulations and analyses of real data, we show that variance in the cellular composition of bulk samples impacts function learnability and attribute this to cell type marker gene content in the GO terms. We further show that cell type profiles, where the relationship between gene expression and cell type is made transparent, are effective for predicting gene function while increasing interpretability. These results indicate that function prediction models trained on bulk coexpression are largely limited to cell-type-level resolution rather than fine-grained biochemical function, with direct consequences for how such predictions should be interpreted.

</details>

---

## 4. Comparing phenotypic manifolds with Kompot: Cluster-free differential expression at single-cell resolution

- **期刊**: bioRxiv
- **作者**: Otto, D. J., Arriaga-Gomez, E., Thieme, E., Yang, R., Lee, S. C., Setty, M.
- **机构**: Manu Setty @ Fred Hutchinson Cancer Center
- **日期**: 2026-09-04
- **ID**: DOI: 10.1101/2025.06.03.657769  |  URL: https://www.biorxiv.org/content/10.1101/2025.06.03.657769v1
- **一句话推荐**: 提出无聚类差异表达分析框架用于多条件单细胞比较，与single-cell perturbation兴趣间接相关。
- **方法**: 提出Kompot统计框架，将细胞密度与基因表达建模为共享细胞状态流形上的连续函数，实现无聚类的单细胞多条件差异分析。
- **主要发现**: 该方法无需预定义聚类即可在单细胞分辨率下量化差异丰度与表达，在衰老与免疫治疗模型中成功捕获了连续的细胞状态转变与异质性转录重塑。
- **对我的启发**: 无明显直接启发

<details><summary>Abstract</summary>

Single-cell studies are frequently designed to compare across conditions such as health and disease. However, existing computational approaches typically rely on grouping cells into discrete populations before making comparisons, which can limit resolution for detecting state-dependent changes. Here, we introduce Kompot, a statistical framework for comparative analysis of multi-condition single-cell data. Kompot quantifies both differential abundance, capturing how cells redistribute across the phenotypic space, and differential expression, identifying condition-specific transcriptional changes that may be localized, heterogeneous, or oppositely regulated across states. By modeling cell density and gene expression as continuous functions over a shared cell-state representation, Kompot enables single-cell resolution inference with principled uncertainty estimates, without requiring predefined clusters or cell types. Applying Kompot to aging murine bone marrow, we identified a continuum of shifts in hematopoietic stem cell and mature cell states, transcriptional remodeling of monocytes independent of compositional changes, and divergent regulation of oxidative stress response genes across cell types. We demonstrate the utility of Kompot in disease settings by identifying cell-state and gene expression changes associated with improved efficacy of combinatorial immunotherapy in melanoma. Additionally, Kompot enables multi-sample comparative analysis by accounting for sample-to-sample heterogeneity. By capturing both global and cell-state-specific effects of perturbation, the Kompot framework is broadly applicable to dissecting condition-specific effects in complex single-cell landscapes.

</details>

---

## 5. From code to natural language: MErlin - a multiomics toolkit for bacterial epigenomics delivered as Claude agent skill.

- **期刊**: bioRxiv
- **作者**: Passeri, I., Pety, S., Giovannini, M., Fondi, M., Mengoni, A., Perrin, E.
- **机构**: Iacopo Passeri @ University of Florence
- **日期**: 2026-09-06
- **ID**: DOI: 10.64898/2026.09.02.748773  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.02.748773v1
- **一句话推荐**: 涉及表观基因组学多组学整合和LLM agent接口，虽非真核调控或深度学习基础模型，但在工具化思路上有一定参考价值。
- **方法**: 将多组学分析流程封装为结构化的 LLM Agent Skill，通过自然语言接口调用固定且经过审计的分析模块。
- **主要发现**: MErlin 工具包通过将自然语言作为操作接口而非替代科学软件，实现了细菌表观基因组多组学数据的连贯、可审计分析，并在合成与真实数据上验证了其有效性。
- **对我的启发**: 可借鉴其将自然语言作为固定分析操作接口的范式，将预训练基因组学模型的 padding 策略选择、虚拟表观特征提取与增强子活性预测封装为 LLM Agent Skill，提升模型调用与推理流程的可审计性。

<details><summary>Abstract</summary>

Interpreting a bacterial methylome is a multi-omics problem. It requires integrating modified-base calls with genome annotation, motif inventories, methyltransferase genotypes, transcript abundance, replichore position and, increasingly, chromosome conformation. These data types are commonly generated in incompatible formats, use inconsistent sequence and gene identifiers, and originate from different analytical workflows. The relevant algorithms are available, but assembling them into a coherent and statistically defensible analysis remains a substantial data-integration and interface problem. We present MErlin (Methylation-driven Expression & Regulation Linkage in Interacting Nuclear-domains), a multi-omics toolkit comprising seventeen composable modules, from basecalled modBAM files to ranked gene-level evidence and a self-contained HTML report. MErlin is distributed both as a conventional Python package and as an agent skill: a structured, version-controlled layer of procedural knowledge that enables a compatible large language model (LLM) assistant to select and operate the audited package without generating a new analysis implementation for each request. This design treats natural language as an interface to fixed analytical operations rather than as a substitute for tested scientific software. The skill encodes module-selection rules, mandatory preflight checks, questions that require human input, design-to-inference constraints, and interpretation guidance. We describe MErlin's architecture and statistics, validate it against a synthetic dataset with planted ground truth, and illustrate the conversational interface on a real methylome-transcriptome comparison in Pseudoalteromonas haloplanktis TAC125. MErlin is open source and available at https://github.com/IacopoPasseri/MErlin

</details>

---

## 6. Adding layers of information to scRNA-seq data using pre-trained language models

- **期刊**: bioRxiv
- **作者**: Krissmer, S. M., Menger, J., Rollin, J., Vogel, T. M., Binder, H., Hackenberg, M.
- **机构**: Maren Hackenberg @ Institute of Medical Biometry and Statistics (IMBI), Faculty of Medicine and Medical Center,  University of Freiburg, Germany
- **日期**: 2026-09-04
- **ID**: DOI: 10.1101/2025.08.23.671699  |  URL: https://www.biorxiv.org/content/10.1101/2025.08.23.671699v1
- **一句话推荐**: 使用预训练语言模型增强单细胞数据表示，虽非DNA语言模型，但在多模态表示学习思路上有间接启发。
- **方法**: 微调轻量级encoder-only生物医学语言模型，通过构建基于文本的训练数据集将scRNA-seq数据与文献语料对齐，学习共享的跨模态表征。
- **主要发现**: 该方法在保留细胞身份的同时，为单细胞分析工作流添加了稳健且可解释的功能、疾病和发育上下文信息。
- **对我的启发**: 无明显直接启发

<details><summary>Abstract</summary>

Pre-trained language models promise to enrich single-cell analyses with contextual information from large biomedical text corpora, but it remains unclear how to optimally align this knowledge with quantitative scRNA-seq data. To address this, we construct text-based training datasets from both scRNA-seq data and biomedical literature targeted to the experimental setting at hand. We then fine-tune lightweight encoder-only biomedical language models to learn a shared, literature-enriched representation. Controlled evaluations across immune and developmental datasets show that this representation preserves cell identity while adding robust and interpretable contextual layers of functional, disease-associated, and developmental information to single-cell analysis workflows.

</details>

---
