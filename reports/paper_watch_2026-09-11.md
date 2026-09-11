# Paper Scout 日报 2026-09-11

共筛选出 **2** 篇推荐论文。
📊 抓取 pubmed 86 → 粗筛 21 篇 → LLM 选中 2 篇

## 1. Decoding gene regulation in plant genomes with artificial intelligence.

- **期刊**: Journal of experimental botany
- **作者**: Niraj Rayamajhi, Tianyang Xu, Tianci Liu, Jing Gao, Kranthi Varala, Ying Li
- **机构**: Ying Li @ Department of Horticulture and Landscape Architecture, Purdue University, West Lafayette, IN 47907, USA.
- **日期**: 2026-09-10
- **ID**: DOI: 10.1093/jxb/erag323  |  PMID: 42717834  |  URL: https://pubmed.ncbi.nlm.nih.gov/42717834/
- **一句话推荐**: 综述了AI和LLM在植物调控基因组学中的应用，包括预测表观基因组特征和调控DNA元件，与你的研究兴趣有交叉。
- **方法**: 综述AI与大型语言模型（LLM）在植物基因组学中预测表观特征、调控元件及基因表达的方法范式
- **主要发现**: AI和LLM技术显著提升了从复杂植物基因组数据中解析表观特征、调控元件及基因调控网络等调控信息的能力
- **对我的启发**: 植物基因组中利用LLM预测表观特征和调控元件的范式，可为跨物种增强子活性预测及虚拟表观特征提取提供模型架构参考

<details><summary>Abstract</summary>

One of the central goals of plant functional genomics is to uncover regulatory mechanisms that shape agriculturally important traits to inform crop improvement. Recent advances in machine learning (ML) and artificial intelligence (AI), especially Large Language Models (LLMs), have greatly transformed our ability to derive regulatory information from complex genomics data. This review starts with a brief introduction of recent advances in AI and ML. We then present a plant-focused synthesis of emerging applications of AI- and LLM tools to: (i) predict epigenomic features, regulatory DNA elements, and gene expressions; (ii) infer gene regulatory network; and (iii) estimate post-transcriptional regulation.

</details>

---

## 2. An operational perturbation proteomics-based virtual cell model.

- **期刊**: Nature
- **作者**: Rui Sun, Liujia Qian, Yongge Li et al. (33 authors)
- **机构**: Tiannan Guo @ Affiliated Hangzhou First People's Hospital, State Key Laboratory of Medical Proteomics, School of Medicine, School of Future Biomedicine, Westlake University, Hangzhou, China. guotiannan@westlake.edu.cn.
- **日期**: 2026-09-09
- **ID**: DOI: 10.1038/s41586-026-11001-9  |  PMID: 42717098  |  URL: https://pubmed.ncbi.nlm.nih.gov/42717098/
- **一句话推荐**: 提出基于扰动蛋白质组学的虚拟细胞模型，与你研究兴趣中的virtual cell和single-cell perturbation概念相关。
- **方法**: 基于大规模时间分辨扰动蛋白质组学数据，采用预训练框架学习可迁移的动态蛋白质轨迹潜在表征，构建虚拟细胞模型。
- **主要发现**: 该模型通过学习蛋白质对扰动的条件响应，能高效预测药物疗效及患者分层，并在细胞系、类器官和临床活检间展现出强大的跨样本迁移能力。
- **对我的启发**: 其利用大规模扰动数据预训练动态潜在表征的范式，启发我在构建虚拟表观遗传特征时，可引入条件维度的表观扰动数据预训练，以提升跨细胞类型游离型增强子活性预测的泛化能力。

<details><summary>Abstract</summary>

Artificial intelligence-empowered virtual cell models represent an emerging approach for in silico drug discovery1-3, yet most existing approaches lack large-scale, time-resolved perturbation proteomics data and interpretable frameworks for predicting therapeutic responses. Here we generated more than 38 million temporal protein-abundance measurements from systematically perturbed breast cancer cell lines, and developed ProteinTalks, a virtual cell model. Central to ProteinTalks is the synergy of this large-scale dynamic proteomic resource and the model architecture, enabling a new pretraining framework that learns transferable dynamical latent representations from temporal proteome trajectories. By modelling how proteins respond conditionally to different perturbations, this approach enables the model to function as an operational tool for diverse drug discovery tasks: predicting drug efficacy and synergy, discovering new drug combinations, probing proteins associated with drug resistance, stratifying patient responses and prioritizing drug candidates for patient organoids. It also shows robust transferability, extending beyond cell lines to patient-derived organoids and clinical biopsies, generally achieving higher performance than the selected benchmark implementations under the evaluated protocols. Together, ProteinTalks shows how scalable pretraining of transferable dynamic representations enables operational, dynamics-aware, proteomics-based virtual cell models to advance in silico drug discovery.

</details>

---
