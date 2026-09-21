# Paper Scout 日报 2026-09-21

共筛选出 **1** 篇推荐论文。
📊 抓取 biorxiv 58/pubmed 32 → 粗筛 14 篇 → LLM 选中 1 篇

## 1. Multi-model biological and sequence information fusion for gene regulatory network inference from single-cell transcriptomics

- **期刊**: bioRxiv
- **作者**: zhong, l., Yan, B., Wang, J., xie, m.
- **机构**: minzhu xie @ hunan normal university
- **日期**: 2026-09-19
- **ID**: DOI: 10.64898/2026.09.13.751326  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.13.751326v1
- **相关分数**: 6/10
- **一句话推荐**: 使用了预训练DNA语言模型和图注意力整合基因序列与单细胞转录组数据，与我的序列表示学习兴趣有部分重叠。
- **方法**: 提出scMGFGRN框架，结合去噪自编码器、图注意力网络与预训练DNA语言模型，融合单细胞转录组、GO层次及基因序列特征，通过门控多头注意力预测基因调控网络。
- **主要发现**: 该模型在多物种数据集上显著优于现有GRN推断方法，能准确识别新型转录因子-靶基因互作并重构细胞特异性调控网络，且可解释性分析验证了多源信息融合的有效性。
- **对我的启发**: 其利用预训练DNA语言模型提取序列特征并结合门控注意力融合多模态信息的范式，启发我在增强子活性预测中采用门控机制融合预训练序列特征与虚拟表观遗传特征。

<details><summary>Abstract</summary>

Identification of transcription factor target gene interactions and construction of the gene regulatory networks (GRNs) are essential for understanding the molecular mechanisms underlying transcriptional gene regulation. Large scale single cell transcriptomics across different tissues offers unprecedented resolution of cellular diversity and regulatory dynamics by capturing gene expression heterogeneity. However, existing methods often lack effective multimodal integration and fail to fully exploit the hierarchical structure in Gene Ontology (GO) and gene sequence level representations, which limits their ability for predictive performance and biological interpretability. We present scMGFGRN, a multi-model deep learning framework that integrates single-cell transcriptomic profiles with GO hierarchical relationships, gene sequences by leveraging denoising auto encoders, graph attention feature extraction and pertained DNA language model to capture multi-source dependencies within multi-model biological knowledge, while its gated multi head attention module effectively identifies informative regulatory signatures and integrate complementary features from different sources to predict accurate gene regulatory networks. Benchmarking on the seven datasets of human and mouse demonstrates that scMGFGRN outperforms state of the art methods in identifying GRNs. Further analyses reveal that scMGFGRN effectively identifies novel TF gene interactions (TGIs) and reconstructs cell type specific GRNs. Interpretability analysis reveals the contribution patterns of heterogeneous biological sources, demonstrating the ability of scMGFGRN to integrate transcriptomic profiles with multi model structure information.

</details>

---
