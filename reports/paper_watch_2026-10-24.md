# Paper Scout 日报 2026-10-24

共筛选出 **1** 篇推荐论文。
📊 抓取 biorxiv 147/pubmed 55 → 粗筛 30 篇 → LLM 选中 1 篇

## 1. GBactPro: cross-species bacterial promoter prediction using element-resolved promoter definitions

- **期刊**: bioRxiv
- **作者**: Han, H.-Y., Kao, Y.-C. V., Kuo, S.-T., Chou, H.-H. D., Chang, J.-M.
- **机构**: Jia-Ming Chang @ Department of Computer Science, National Chengchi University; Institute of Neuroscience, National Chengchi University
- **日期**: 2026-10-23
- **ID**: DOI: 10.64898/2026.10.18.759981  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.18.759981v1
- **相关分数**: 7/10
- **一句话推荐**: 基于序列的启动子预测（sequence-to-function），且关注跨物种泛化与序列窗口定义对模型性能的影响，与我的增强子预测跨细胞类型泛化及padding策略评估有直接方法论共鸣。
- **方法**: 基于启动子功能元件（-35、间隔区、-10）解析定义的CNN-BiLSTM跨物种预测模型。
- **主要发现**: 采用元件解析的变长序列定义训练模型，相比固定长度窗口显著提升了跨物种预测性能，并能识别被转录抑制的潜在启动子。
- **对我的启发**: 该研究凸显了序列结构定义对模型性能的影响，启发我在评估预训练基因组学模型padding策略时，可探索基于增强子核心基序或功能元件边界进行变长对齐，而非简单的固定长度截断或padding。

<details><summary>Abstract</summary>

Accurate bacterial promoter prediction remains challenging across species, partly because conventional models often use fixed-length promoter windows that do not explicitly account for promoter architecture. Using promoter annotations derived from the Promoter Architecture Scanner (PAS), we found that training on sequences comprising the -35 element, spacer, and -10 element improved cross-species prediction compared with fixed-length promoter windows. Based on this element-resolved promoter definition, we developed GBactPro, a convolutional neural network-bidirectional long short-term memory (CNN-BiLSTM) model jointly trained on curated promoter data from 43 bacterial species. The jointly trained model achieved a mean AUROC of 0.9943 on held-out test sequences. Under matched-length benchmarking, GBactPro outperformed Promotech, iPro-MP, Prompt, and iPro-WAEL by 0.066-0.314 in mean AUROC. Genome-wide scanning of Escherichia coli achieved an AUROC of 0.979 and an AUPRC of 0.160 under stringent one-to-one promoter-site matching, increasing to 0.997 and 0.323, respectively, with a 100-bp positional tolerance. Unmatched predictions were enriched for H-NS binding, and independent H-NS-knockout data further supported the possibility that some predicted promoter-like regions are transcriptionally repressed. Together, these findings highlight the importance of promoter-sequence definition for cross-species prediction and demonstrate the potential of GBactPro for genome-wide promoter identification and biological interpretation.

</details>

---
