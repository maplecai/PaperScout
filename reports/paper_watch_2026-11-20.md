# Paper Scout 日报 2026-11-20

共推荐 **1** 篇论文。

## 1. Weight locking as a safeguard for open-weight biological foundation models

bioRxiv · 预印本 · 2026-11-19 · 相关性 7/10

**研究关联：研究兴趣拓展**

- **为什么值得看**：直接讨论基因组/蛋白质基础模型（Evo家族、ESM3）的权重安全与微调行为，与基因组基础模型研究兴趣高度相关。
- **任务与验证范围**：输入：预训练生物基础模型权重 → 输出：施加权重锁定后的模型及其抗微调攻击评估；研究体系：病毒基因组与蛋白质序列（摘要未说明具体物种/细胞体系）；验证范围：针对不同知识水平的攻击者（朴素与知情）进行微调攻击测试
- **核心方法**：基于谱形变与网络重缩放对称性的权重锁定方法，用于防御生物基础模型的恶意微调。
- **主要发现与证据**：权重锁定可防御朴素攻击者（使其微调后病毒建模能力低于预训练水平），但无法防御知情攻击者（通过补偿矩阵恢复性能）；无补偿锁也可被标准重平衡破解，表明防御障碍在于知识而非算力。
- **可借鉴点（研究建议）**：无明显直接启发
- **迁移边界**：原论文聚焦生物基础模型的权重安全与微调防御，与基于DNA序列预测增强子活性及评估padding影响的任务在目标上完全不同。其关于微调对模型能力影响的结论不能直接迁移至增强子活性预测的跨细胞类型泛化或序列长度处理任务中。
- **阅读时核实**：谱形变权重锁定在Evo等基因组学模型上的具体实现机制是什么？施加锁定后是否会影响模型对正常非病毒DNA序列的表征能力或常规下游任务的微调效果？

[原文](https://www.biorxiv.org/content/10.64898/2026.07.07.736795v1) · [DOI](https://doi.org/10.64898/2026.07.07.736795)

作者：Karatzikos, A., Vasilopoulou, A., Chan, C., Mouratidis, I., Georgakopoulos-Soares, I.
来源标注的末位/通讯作者：Ilias Georgakopoulos-Soares
机构：The University of Texas at Austin

### 英文摘要

Biological foundation models can accelerate research, but their open weight release raises biosecurity concerns. A common safeguard excludes eukaryotic viral genomes from training, but fine-tuning on public viral data reverses it. We confirm that fine-tuning improves held-out viral language modelling, and that the gain comes from the viral data itself. Weight locking by spectral deformation, proposed to prevent fine-tuning, is untested in biological models. We applied it to two Evo-family models and the protein model ESM3-open, against attackers of increasing knowledge. The lock defends against the naive attacker, whose fine-tuning drives capability below pretrained on all three models. It does not defend against an informed attacker, who freezes or fuses the compensation matrix to restore near-unlocked performance. A compensation-free lock we build from the network's own rescaling symmetries again defeats the naive attacker, but canonical rebalancing removes it without knowledge of the lock. The barrier is one of knowledge, not compute.

---

中文笔记基于标题和摘要生成，未核验全文；研究建议不代表论文已验证的结论。相关性分数不是论文质量评分。

检索统计：窗口 [2026-11-17 00:00, 2026-11-20 00:00) UTC；抓取 biorxiv 190/pubmed 63 → 粗筛 18 篇 → LLM 选中 1 篇
