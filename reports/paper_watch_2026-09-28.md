# Paper Scout 日报 2026-09-28

共筛选出 **2** 篇推荐论文。
📊 抓取 biorxiv 79/pubmed 20 → 粗筛 10 篇 → LLM 选中 2 篇

## 1. A single-nucleus multi-omic atlas of gene regulation across 21 adult human tissues

- **期刊**: bioRxiv
- **作者**: Fan, K., Sule, A., Guillaumet-Adkins, A. et al. (13 authors)
- **机构**: Kristin G Ardlie @ Epigenomics Program, Broad Institute of MIT and Harvard, Cambridge, MA 02142
- **日期**: 2026-09-27
- **ID**: DOI: 10.64898/2026.09.25.754561  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.25.754561v1
- **相关分数**: 9/10
- **一句话推荐**: 该论文构建了跨组织单细胞多组学图谱，并训练了sequence-to-function模型预测染色质可及性变异效应，与你的跨细胞类型增强子活性预测及调控基因组学研究高度契合。
- **方法**: 构建跨组织单核多组学图谱并训练序列到功能(sequence-to-function)模型预测变异的染色质可及性效应。
- **主要发现**: 构建了涵盖21种人体组织的单核多组学图谱，发现了大量新的顺式调控元件及其细胞特异性调控架构，并利用序列模型成功预测了数十万个变异对染色质可及性的影响。
- **对我的启发**: 该研究针对特定细胞亚型（如内皮细胞）训练序列到功能模型，提示在预测游离型增强子活性时，可利用大规模单核多组学数据构建不同细胞类型的特异性训练集，以提升模型对细胞上下文的解析能力。

<details><summary>Abstract</summary>

Diverse human cell types establish specialized functions through lineage- and context-specific regulatory programs. Interpreting non-coding genetic risk requires integrated multi-omic reference maps that directly connect regulatory DNA to cellular expression across human tissues. Here we present a single-nucleus multi-omic atlas comprising 459,856 transcriptomic and chromatin accessibility profiles from 21 adult human tissues and four donors, including paired measurements from 160,688 nuclei. The atlas resolves nine cell lineages, 61 broad cell types and 313 subclusters, and identifies 1,085,062 candidate cis-regulatory elements (cCREs), including 161,270 novel elements absent from ENCODE. Regulatory activity was dominated by cell identity but refined by tissue context. Joint profiling enabled 871,177 cCRE-gene associations and revealed lineage-specific regulatory architectures. Cross-tissue accessibility further identified lineage-restricted and constitutively inaccessible chromatin domains, the latter showing preferential hypomethylation across human cancers. Furthermore, we leverage this dataset to train sequence-to-function models to predict chromatin-accessibility effects for 548,656 fine-mapped variants, identifying 18,133 high-effect variants, including 1,120 broadly active variants. Models trained for eight endothelial subtypes further resolve predicted variant effects across vascular beds. Together, this atlas provides a comprehensive cellular and computational framework for interpreting regulatory sequence, context-dependent gene control, and complex trait genetics across the human body.

</details>

---

## 2. A meta-interaction basis for cell-cell communication in tissues

- **期刊**: bioRxiv
- **作者**: Tang, J., Liang, S., Alam, S., Cheng, W., Zhang, Y., Ma, J.
- **机构**: Jian Ma @ Carnegie Mellon University
- **日期**: 2026-09-27
- **ID**: DOI: 10.64898/2026.09.21.753369  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.21.753369v1
- **相关分数**: 5/10
- **一句话推荐**: 该研究提出表示学习框架从空间转录组学中提取细胞间通讯程序，与你的虚拟细胞及单细胞扰动兴趣有间接关联。
- **方法**: SpiderNet：基于空间转录组学的可解释表示学习框架，通过联合学习发送方调控因子、配体-受体对和接收方靶基因，将细胞间通讯分解为紧凑的元交互基础组件。
- **主要发现**: SpiderNet从580万+空间转录组细胞中识别出可复用的元交互程序，能追踪多细胞信号级联、预测扰动响应，并在独立队列中验证了与生存和免疫治疗响应相关的泛癌症成纤维细胞-肿瘤程序。
- **对我的启发**: 无明显直接启发

<details><summary>Abstract</summary>

Tissue function depends on signals exchanged between cells and the responses they elicit. Yet whether diverse cell-cell interactions in situ form recurrent sender-receiver programs remains unclear. We present SpiderNet, an interpretable representation-learning framework that discovers such directed programs as a compact basis of cell-cell meta-interactions (MIs) from spatial transcriptomics. SpiderNet jointly learns which sender regulators, ligand-receptor pairs, and receiver targets define each MI and where each program is active across neighboring cell pairs. The resulting representation traces multicellular relays and links communication to cell states, perturbation responses, and phenotypes. SpiderNet recovers ground-truth MIs and their molecular components in simulations and, in real tissues, shows stronger direction-specific agreement with independently curated regulatory programs in senders and receivers than alternative methods. Across more than 5.8 million spatially profiled cells, SpiderNet resolves an SPP1-THBS relay linking monocytes, fibroblasts, and tumor cells within an immune-suppressive ovarian cancer niche, predicts T-cell responses to held-out melanoma-cell perturbations, and identifies a T-cell-associated brain-aging program and age-predictive signals that transfer across regions and platforms. It reveals a recurrent pan-cancer COLLAGEN-linked fibroblast-tumor program whose projected abundance in independent cohorts is associated with poorer survival and non-response to immunotherapy. SpiderNet thus establishes MIs as a reusable organizational layer between molecular interactions and tissue phenotypes, providing a framework to resolve, compare, trace, and perturb multicellular regulation in situ.

</details>

---
