# Paper Scout 日报 2026-09-13

共筛选出 **2** 篇推荐论文。
📊 抓取 biorxiv 670/pubmed 49 → 粗筛 100 篇 → LLM 选中 2 篇

## 1. Environment-Aware DNA Language Model for Stress-Responsive Genomic Prioritization in Maize

- **期刊**: bioRxiv
- **作者**: Pal, D., Odell, A., Singh, A., Thompson, A. M., Ross, A., Thessen, A.
- **机构**: Debasmita Pal @ Michigan State University
- **日期**: 2026-09-12
- **ID**: DOI: 10.64898/2026.09.11.749989  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.11.749989v1
- **一句话推荐**: 直接涉及DNA语言模型和基因组基础模型，使用prompt token和参数高效微调学习条件化序列表示，与你的GFM/DNA-LLM研究兴趣高度契合。
- **方法**: 基于Transformer的植物基因组预训练模型，通过参数高效微调引入环境特异性提示token，结合嵌入偏移与注意力机制进行胁迫响应基因组区域优先排序。
- **主要发现**: 引入压力条件提示token的DNA语言模型能学习到环境特异性的序列表示，其注意力模式与嵌入偏移能有效识别出与胁迫响应及产量相关的功能基因组区域和调控基序。
- **对我的启发**: 可借鉴其引入“条件特异性提示token”的范式，在预训练DNA模型中注入“细胞类型或虚拟表观遗传特征token”以实现多细胞类型增强子活性预测，并利用注意力机制分析padding等序列区域对模型决策的影响。

<details><summary>Abstract</summary>

Abiotic stresses such as heat and drought severely reduce maize productivity, yet identifying genomic regions that confer stress resilience remains a challenge. Inspired by advances in Large Language Models (LLMs), Genomic Foundation Models (GFMs) have recently emerged as a promising approach for capturing regulatory patterns through large-scale pre-training on DNA sequences. However, their application to plant stress-response analysis remains unexplored. This study presents an environment-aware DNA-LLM that adapts AgroNT, a transformer-based GFM pre-trained on diverse plant genomes, by incorporating stress-specific prompt tokens. Through parameter-efficient fine-tuning, the model learns stress-conditioned sequence representations that form distinct clusters in the embedding space across environmental contexts. By combining stress-induced shifts in these sequence representations relative to control conditions with transformer attention patterns, we prioritized putative heat- and drought-responsive genomic regions associated with grain yield in the Genomes-to-Fields (G2F) panel. Prioritized regions were supported by spatiotemporal differential gene-expression evidence and overlap with stress-associated quantitative trait loci. They were further characterized through transcription-factor family analysis and regulatory motif enrichment. Attention-guided analysis additionally identified stress-associated motifs enriched within model-emphasized sequence regions. Overall, the prioritized loci were proximal to genes involved in transcriptional regulation, signaling, and metabolic pathways relevant to abiotic-stress adaptation, demonstrating the potential of stress-conditioned transformer-based sequence modeling for environment-aware genome-to-phenome analysis.

</details>

---

## 2. Sex differences in exploration-exploitation strategies during home-cage decision making

- **期刊**: bioRxiv
- **作者**: Murrell, C. L., Legaria, A. A., McCullough, K. B. et al. (14 authors)
- **机构**: Alexxai V Kravitz @ Washington University in St Louis
- **日期**: 2026-09-12
- **ID**: DOI: 10.64898/2026.04.02.716124  |  URL: https://www.biorxiv.org/content/10.64898/2026.04.02.716124v1
- **一句话推荐**: 使用单细胞RNA-seq基础模型耦合分子GPT进行细胞类型特异性药物设计，间接涉及单细胞基础模型和细胞类型特异性建模思路。
- **方法**: 基于家笼自动化觅食任务的行为学测试与计算行为建模分析范式。
- **主要发现**: 雄性小鼠在确定性环境中表现出更强的利用策略（赢-留行为），但在概率性环境中该策略不再带来准确性优势，揭示了两性在探索-利用权衡上的微小但显著差异。
- **对我的启发**: 无明显直接启发

<details><summary>Abstract</summary>

The exploration-exploitation trade-off refers to the conflict between using known strategies that reliably yield reward (exploitation) and sampling uncertain options that might yield better outcomes (exploration). Dysregulation of this balance is implicated in neuropsychiatric disease, and while sex differences in this balance have been described, the biological bases remain unclear. To quantify sex differences in this trade-off, we tested mice (n=74 male, 62 female) on four home-cage based foraging tasks with an operant pellet dispensing device, Feeding Experimentation Device 3 (FED3). Mice completed the tasks continuously over multiple days and the tasks were their only source of food. Across multiple tasks, males showed higher win-stay behaviour than females, indicating greater exploitation of previously rewarded actions, an effect that was modest in size but highly significant. Power analyses revealed that >30 mice per sex were needed to detect these modest but significant sex differences with 80% power. No consistent sex differences were observed in pellet intake, suggesting that differences in exploitation did not reflect differences in hunger drive or demand for pellets. Exploitation is a more efficient strategy when environmental parameters are fixed, while exploration can be more advantageous when parameters such as reward locations are changing and uncertain. We tested this idea by re-running our mice in a probabilistic foraging task, where actions led to uncertain probabilities of reward. While males continued to show higher levels of win-stay behaviour on this task, this no longer led to increases in accuracy. Behavioural modelling also supported this framework, demonstrating that stronger win-stay behaviour was most advantageous in deterministic models, and less advantageous in probabilistic models. Together, our findings demonstrate that male and female mice have small but significant differences in their exploration-exploitation balance, which leads to more accurate foraging in certain, but not uncertain, environments.

</details>

---
