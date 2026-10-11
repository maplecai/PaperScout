# Paper Scout 日报 2026-10-11

共筛选出 **1** 篇推荐论文。
📊 抓取 biorxiv 129/pubmed 51 → 粗筛 21 篇 → LLM 选中 1 篇

## 1. Expanding the DNA Motif Lexicon of the Transcriptional Regulatory Code

- **期刊**: bioRxiv
- **作者**: Fan, J., Chaudhri, V. K., Bisht, D. et al. (15 authors)
- **机构**: Harinder Singh @ University of Pittsburgh
- **日期**: 2026-10-10
- **ID**: DOI: 10.1101/2025.07.09.662874  |  URL: https://www.biorxiv.org/content/10.1101/2025.07.09.662874v1
- **相关分数**: 8/10
- **一句话推荐**: 使用深度学习模型GRACE在MPRA数据上预测cis调控元件活性及变异效应，直接命中增强子活性预测与调控编码研究。
- **方法**: 结合计算挖掘与MPRA实验，构建单核苷酸分辨率的深度学习模型（GRACE）学习复合元件词典并预测转录调控活性。
- **主要发现**: 模型能预测未在实验设计中的变异及立体特异性配置活性，并通过对比染色质可及性等正交特征模型，解析了单个motif对转录与染色质状态的不同贡献。
- **对我的启发**: 其通过对比正交特征模型解耦序列motif对转录与染色质可及性贡献的范式，可启发我在增强子预测中分离预训练序列特征与虚拟表观遗传特征的独立效应。

<details><summary>Abstract</summary>

Cis-regulatory sequences in metazoan genomes contain elaborate combinations of transcription factor (TF) motifs. Stereospecific arrangements of simple motifs constitute composite elements (CEs) that enhance DNA-protein interaction specificity and enable combinatorial regulatory logic. Despite their importance, CEs remain underexplored. We integrate genome-scale computational discovery (CEseek) with customized massively parallel reporter assays (MPRAs) to uncover cell type-specific and shared CEs, corroborated by coincident and/or cooperative TF binding in vivo and in vitro. A deep learning model, GRACE, trained on MPRA data at single-nucleotide resolution, learns the CE lexicon and predicts activities of variants and alternative stereospecific CE configurations not included in the experimental design. Comparative analysis with models trained on orthogonal features such as chromatin accessibility, demonstrates convergence within the CE lexicon while resolving how individual motifs contribute to transcription versus chromatin accessibility. The expanded lexicon enables CE-aware predictions and interpretation of the impact of disease-associated non-coding variants in. the human genome.

</details>

---
