# Paper Scout 日报 2026-11-21

共推荐 **1** 篇论文。

## 1. Deep learning design and in vivo validation of Müller glia-specific cis-regulatory elements

bioRxiv · 预印本 · 2026-11-20 · 相关性 8/10

**研究关联：方法可借鉴**

- **为什么值得看**：使用深度学习设计细胞类型特异性的顺式调控元件，直接契合你的“enhancer design”和“cell-type-specific enhancer”研究兴趣。
- **任务与验证范围**：输入：单细胞染色质可及性数据 → 输出：紧凑且细胞特异的顺式调控元件（CREs）设计及活性预测；研究物种/细胞体系：人和小鼠视网膜Müller胶质细胞（MG）；验证范围：跨物种及数百种人类细胞类型/组织的计算机模拟验证，小鼠视网膜体内验证
- **核心方法**：基于物种特异性单细胞染色质可及性数据训练深度学习模型，预测细胞类型可及性并生成紧凑CREs。
- **主要发现与证据**：设计的CREs在跨物种和数百种细胞类型中表现出高MG特异性和低脱靶可及性，机制由LHX2基序驱动，并在小鼠视网膜体内验证中成功实现MG特异性表达。
- **可借鉴点（研究建议）**：其跨数百种细胞类型评估脱靶效应的验证策略，可为我研究增强子在不同细胞类型中的活性预测特异性评估提供参考。
- **迁移边界**：原论文侧重从头设计紧凑CREs并跨物种验证，未涉及游离型序列或padding策略；其跨细胞类型泛化能力不能直接等同于我的模型在游离型增强子活性预测及不同padding设置下的表现。
- **阅读时核实**：模型在预测不同细胞类型可及性时，对输入序列的长度处理机制是什么？是否涉及padding操作及其对预测结果的影响？

[原文](https://www.biorxiv.org/content/10.64898/2026.07.15.738785v1) · [DOI](https://doi.org/10.64898/2026.07.15.738785)

作者：Fornes, O., Koh, K. D., Marton, R. M. et al. (14 authors)
来源标注的末位/通讯作者：Oriol Fornes
机构：Genentech

### 英文摘要

Effective recombinant adeno-associated virus gene therapies require promoters that are compact and cell-type-specific. Ideally, promoters should also exhibit functional conservation when tested in model organisms to ensure that preclinical findings translate reliably to human patients. Here, we introduce a deep learning framework for designing cis-regulatory elements (CREs) meeting these criteria, applied to retinal Muller glia (MG). Using single-cell chromatin accessibility data from human and mouse retinas, we trained species-specific models to predict cell-type accessibility, and designed compact CREs using two complementary strategies. In silico validation predicted that the designed CREs exhibit high MG-specific accessibility (on-target) in both species with minimal off-target accessibility across hundreds of human cell types and tissues. Mechanistic analysis revealed that the predicted MG accessibility is driven by the creation of LHX2 motifs. In vivo validation confirmed that the designed CREs successfully restrict reporter expression to MG in the murine retina. Our deep learning framework is highly generalizable and enables the rapid design of compact, on-target, and species-conserved CREs for precision gene therapy.

---

中文笔记基于标题和摘要生成，未核验全文；研究建议不代表论文已验证的结论。相关性分数不是论文质量评分。

检索统计：窗口 [2026-11-18 00:00, 2026-11-21 00:00) UTC；抓取 biorxiv 166/pubmed 71 → 粗筛 34 篇 → LLM 选中 1 篇
