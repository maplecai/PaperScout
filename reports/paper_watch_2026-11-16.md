# Paper Scout 日报 2026-11-16

共推荐 **1** 篇论文。

## 1. Is the Bitter Lesson coming to genomic prediction? An untuned tabular foundation model matches or beats specialized methods

bioRxiv · 预印本 · 2026-11-15 · 相关性 6/10

**研究关联：方法可借鉴**

- **为什么值得看**：探讨通用表格基础模型在基因组预测中超越专用模型的现象，与你对基因组基础模型的评估和研究兴趣间接相关。
- **任务与验证范围**：输入：标记基因型 → 输出：表型预测值；研究物种/细胞体系：6种植物物种（含大豆、水稻、云杉等）；验证范围：跨18个性状，包含留家族交叉验证（跨家族泛化）
- **核心方法**：直接将标记基因型输入未经调优的通用预训练表格基础模型TabPFN-3.5进行表型回归预测。
- **主要发现与证据**：TabPFN-3.5在18个性状中11个排名第一；在相同数据划分下，12个性状优于GBLUP等最优基线，仅1个性状显著落后；但在留家族交叉验证中，其准确率下降且仅与GBLUP和RKHS持平。
- **可借鉴点（研究建议）**：推测在评估预训练基因组学模型时，可借鉴其对比通用预训练模型与领域特化基线的方法论，并重点关注模型在分布外（如跨家族/跨细胞类型）泛化时的性能衰减现象。
- **迁移边界**：原论文处理的是表格型基因型数据预测植物表型，而我的任务是DNA序列到增强子活性的映射。TabPFN的表格输入范式无法直接迁移至序列任务，且植物跨家族泛化不等同于跨细胞类型的增强子活性泛化。
- **阅读时核实**：在留家族交叉验证中，TabPFN-3.5性能下降至与基线持平，是因为其预训练机制缺乏对群体结构和连锁不平衡的建模能力，还是由于表格模型对未见基因型组合的泛化存在固有局限？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.03.764067v1) · [DOI](https://doi.org/10.64898/2026.11.03.764067)

作者：Flagel, L.
来源标注的末位/通讯作者：Lex Flagel
机构：Gencove Inc

### 英文摘要

Genomic prediction (GP) is dominated by models designed around assumptions about how genetic variation affects phenotypes. Here we asked how well a general-purpose pretrained tabular foundation model called TabPFN-3.5 does with no genetics-specific modeling and no tuning when given marker genotypes directly. We benchmarked TabPFN-3.5 using a published comparison of 18 GP methods on 18 traits in six plant species. Against the published means, TabPFN-3.5 ranked first on 11 of 18 traits and had the best median rank. Because the published benchmark did not identify its test sets, we reran GBLUP, RKHS and elastic-net models on the same splits as TabPFN-3.5. Against the best of these, TabPFN-3.5 was significantly behind on only one trait, spruce wood density, and ahead on 12 of 18, with significant gains on all three soybean traits and rice flowering time. In the soybean panel, which had the largest number of lines, its advantage was clearest. In leave-families-out cross-validation, where models were trained on some soybean families and used to predict lines from other families withheld from training, every model lost accuracy and TabPFN-3.5 performed on par with GBLUP and RKHS. That a general-purpose learner matches or exceeds decades of specialized GP models is consistent with Sutton's Bitter Lesson, which holds that methods that scale with computation eventually overtake those built on human knowledge of the domain.

---

中文笔记基于标题和摘要生成，未核验全文；研究建议不代表论文已验证的结论。相关性分数不是论文质量评分。

检索统计：窗口 [2026-11-13 00:00, 2026-11-16 00:00) UTC；抓取 biorxiv 82/pubmed 40 → 粗筛 4 篇 → LLM 选中 1 篇
