# Paper Scout 日报 2026-11-09

共推荐 **1** 篇论文。

## 1. A fine-tuned genomic language model captures nucleotide-level information overlooked by missense variant impact predictors

bioRxiv · 预印本 · 2026-11-06 · 相关性 8/10

**研究关联：方法可借鉴**

- **为什么值得看**：直接涉及基因组语言模型的微调和核苷酸水平信息捕获，与DNA语言模型和序列表示学习研究高度相关。
- **任务与验证范围**：输入：含错义变异的DNA序列 → 输出：变异影响预测；研究物种/细胞体系：摘要未说明（涉及ClinVar和RAD51D数据，推测为人类）；验证范围：在留存ClinVar变异和独立RAD51D饱和基因组编辑数据上验证，未提及跨细胞类型验证。
- **核心方法**：通过系统优化预训练基因组语言模型的微调策略，构建用于错义变异影响预测的模型（GLM-Missense）。
- **主要发现与证据**：GLM-Missense在ClinVar和RAD51D数据上对七个现有预测器提供了最多的互补信息，该互补信号部分反映了剪接破坏（包括SpliceAI遗漏的外显子剪接调控元件）及密码子水平对mRNA稳定性的影响。
- **可借鉴点（研究建议）**：该研究展示了微调预训练基因组语言模型能捕捉被特定任务模型忽略的底层序列上下文信息，这提示我在增强子活性预测中，可探究模型是否同样捕捉了虚拟表观遗传特征之外的核苷酸级上下文依赖。
- **迁移边界**：原论文聚焦编码区错义变异的功能影响预测，而我的研究关注非编码区游离型增强子活性及padding策略。GLM在编码区变异任务上的互补性不能直接外推至跨细胞类型的非编码区增强子活性预测任务，且原论文未涉及padding影响的评估。
- **阅读时核实**：原文在系统优化微调策略时，输入序列的长度设定与padding处理方式是什么？这些序列处理细节是否影响了模型对核苷酸级上下文信息的捕捉？

[原文](https://www.biorxiv.org/content/10.64898/2026.05.06.723362v1) · [DOI](https://doi.org/10.64898/2026.05.06.723362)

作者：Su, Y., Lin, Y.-J.
来源标注的末位/通讯作者：Yaqi Su
机构：University of California, Berkeley

### 英文摘要

Established missense variant impact predictors primarily capture protein-level consequences, yet missense-annotated variants can also act through nucleotide sequence context. We developed GLM-Missense by systematically optimizing the fine-tuning of a genomic language model for missense variant impact prediction. GLM-Missense contributed the most complementary information to seven established predictors on held-out ClinVar variants and independent RAD51D saturation genome editing data. The complementary signal partly reflects splicing disruption, including disrupted exonic splicing regulatory elements largely missed by SpliceAI, and possibly codon-level effects on mRNA stability. These findings suggest fine-tuned genomic language models capture nucleotide-level information overlooked by current missense variant impact predictors.

---

中文笔记基于标题和摘要生成，未核验全文；研究建议不代表论文已验证的结论。相关性分数不是论文质量评分。

检索统计：抓取 biorxiv 86/pubmed 38 → 粗筛 12 篇 → LLM 选中 1 篇
