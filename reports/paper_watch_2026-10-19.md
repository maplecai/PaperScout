# Paper Scout 日报 2026-10-19

共筛选出 **1** 篇推荐论文。
📊 抓取 biorxiv 107/pubmed 33 → 粗筛 12 篇 → LLM 选中 1 篇

## 1. DeepD enables efficient genome modeling and controllable long-context sequence generation across domains of life

- **期刊**: bioRxiv
- **作者**: Lai, J., Xin, B., Wang, Z. et al. (17 authors)
- **机构**: Jinsheng Lai @ China Agricultural University
- **日期**: 2026-10-18
- **ID**: DOI: 10.64898/2026.10.13.758170  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.13.758170v1
- **相关分数**: 9/10
- **一句话推荐**: DeepD是基因组基础模型，直接涉及sequence-to-function预测、顺式调控元件建模和启动子生成，与你的基因组基础模型和增强子设计研究高度契合。
- **方法**: 基于系统发育信息引导的稀疏混合专家（MoE）架构，支持百万级token长上下文的单核苷酸分辨率基因组基础模型。
- **主要发现**: 跨物种全基因组预训练的DeepD在调控区域变异预测上表现优异，专家路由能有效捕获远端顺式调控元件，并支持可控的基因组级序列生成。
- **对我的启发**: 其百万级长上下文能力为评估预训练模型padding影响提供了新视角（长上下文或减少游离型增强子的padding需求），且专家路由机制有助于解析远端顺式调控特征。

<details><summary>Abstract</summary>

Genome foundation models hold great potential for advancing biological research, but modeling diverse complex genomes and generating controllable genome-scale sequences remain challenging. We present DeepD, a phylogeny-informed sparse mixture-of-experts model operating at single-nucleotide resolution over a 1-million-token context while reducing active computation. Pretrained on unselected whole-genome sequences across all domains of life, DeepD learns genic and intergenic sequence features and supports broad sequence-to-function prediction across species. DeepD performs well in human protein fitness and disease variants effect prediction, such as BRCA1 and BRCA2, with particular strength in regulatory regions, such as promoter and transcription-factor binding sites. Expert routing captures exon-intron boundaries, transposable elements, and distal cis-regulatory elements. DeepD also generates experimentally validated core promoters with specified transcriptional strengths. Finally, the Context-Anchor-Body strategy enables generation of complete yeast chromosome sequences and megabase-scale Arabidopsis segments, preserving gene structure and order while introducing variations within natural ranges. Together, DeepD is an efficient genome foundation model that unifies accurate sequence-to-function prediction with controllable genome-scale generation, advancing predictive and generative design of complex genomes.

</details>

---
