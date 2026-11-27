# Paper Scout 日报 2026-11-27

共推荐 **1** 篇论文。

## 1. RIPPLE: learning nucleotide relations in an RNA foundation model

bioRxiv · 预印本 · 2026-11-26 · 相关性 8/10

**研究关联：方法可借鉴**

- **为什么值得看**：RNA基础模型，通过序列学习核苷酸间长程关系，与你的基因组/DNA语言模型和序列到功能研究高度相关。
- **任务与验证范围**：输入：RNA序列 → 输出：核苷酸关系表示及下游任务预测；研究物种/细胞体系：摘要未说明；验证范围：5个下游任务（RNA家族分类、核糖体载入预测、二级结构预测、三维接触预测、剪接位点识别），未明确跨细胞类型验证
- **核心方法**：基于成对预测效用指导关系学习的RNA基础模型，推理时仅依赖序列输入
- **主要发现与证据**：在3240万RNA序列上预训练，RIPPLE在5个下游任务上整体性能提升；机制分析表明效用引导学习改善了信息交互的恢复并增强了表示的可迁移性
- **可借鉴点（研究建议）**：可借鉴其通过“成对预测效用”显式学习序列中远距离核苷酸关系的方法范式，推测该方法可用于显式建模DNA序列中远距离增强子-启动子相互作用或padding引入的伪关系
- **迁移边界**：原论文针对RNA序列建模，我的研究针对DNA增强子活性预测及padding影响。RNA二级结构约束与DNA顺式调控元件机制不同，且padding对长序列注意力机制的影响在RNA和DNA模型中可能存在差异，不能将RNA上的关系学习结论直接等同于DNA增强子任务
- **阅读时核实**：RIPPLE在处理输入序列时是否使用了padding？其“成对预测效用”机制如何处理或过滤padding引入的虚假核苷酸关系？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.23.768763v1) · [DOI](https://doi.org/10.64898/2026.11.23.768763)

作者：Hao, Y., Guo, X., Ran, Z., Yang, Y., Zhao, C., Coin, L. J. M., Sweeney, C. J., Li, F.
来源标注的末位/通讯作者：Fuyi Li
机构：Adelaide University

### 英文摘要

RNA function depends on interactions between nucleotides that can be widely separated in sequence, yet capturing these relationships remains challenging for RNA language models. Existing approaches primarily learn nucleotide relationships implicitly from individual nucleotide reconstruction or rely on external structural information to model nucleotide interactions. Here we introduce RIPPLE, an RNA foundation model that learns to identify and represent sparse, predictively useful nucleotide relationships directly from sequence. Pretrained on 32.4 million RNA sequences, RIPPLE uses pairwise predictive utility to guide relational learning, transferring training-time supervision into a sequence-only model without requiring structural inputs at inference. RIPPLE improves overall performance across five downstream tasks spanning RNA family classification, ribosome loading prediction, secondary-structure prediction, three-dimensional contact prediction, and splice-site recognition. Mechanistic analyses further show that utility-guided learning improves the recovery of informative interactions and enhances the transferability of learned RNA representations.

---

中文笔记基于标题和摘要生成，未核验全文；研究建议不代表论文已验证的结论。相关性分数不是论文质量评分。

检索统计：窗口 [2026-11-24 00:00, 2026-11-27 00:00) UTC；抓取 arxiv 41/biorxiv 151/pubmed 64 → 粗筛 23 篇 → LLM 选中 1 篇
