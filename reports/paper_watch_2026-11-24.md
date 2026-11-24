# Paper Scout 日报 2026-11-24

共推荐 **2** 篇论文。

## 1. Genomic foundation models and complementary variant-scoring strategies in LGMD-associated genes: architecture, adaptation, and sequence context

bioRxiv · 预印本 · 2026-11-23 · 相关性 7/10

**研究关联：方法可借鉴**

- **为什么值得看**：直接比较多个基因组基础模型（含AlphaGenome、Evo2）并系统评估序列上下文长度对变异评分性能的影响，与你的基因组基础模型评估项目高度相关。
- **任务与验证范围**：输入：含单核苷酸变异的DNA序列（101-501 bp上下文） → 输出：变异致病性分类；研究物种/细胞体系：人类肢带型肌营养不良(LGMD)相关基因，摘要未说明具体细胞类型；验证范围：10个LGMD相关基因的ClinVar变异，包含gene-held-out测试，未涉及跨细胞类型验证。
- **核心方法**：对比评估六种预训练基因组基础模型在冻结嵌入、监督微调及不同序列上下文长度下的变异分类性能。
- **主要发现与证据**：将序列上下文从101bp扩展至501bp提升了5/6个冻结模型的分类性能（如Evo2的MCC从0.644升至0.864）；监督微调对3个模型有效但对另外3个有害；GPN-Star V100和AVI原生评分表现最佳（MCC分别为0.929和0.938）。
- **可借鉴点（研究建议）**：建议在我的增强子活性预测研究中，系统评估不同padding或上下文长度对预训练模型性能的影响，并对比冻结特征提取与微调策略的收益差异。
- **迁移边界**：原论文聚焦于SNV致病性分类且未涉及细胞类型特异性，其关于序列上下文长度的结论不能直接等同于在跨细胞类型增强子活性预测任务中的表现，需谨慎迁移。
- **阅读时核实**：在扩展序列上下文长度（101bp至501bp）时，不同模型对padding或截断机制的具体处理方式是什么？性能提升是否主要由特定基因区域或变异类型驱动？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.21.768324v1) · [DOI](https://doi.org/10.64898/2026.11.21.768324)

作者：Galgale, S., Vats, I., Wilson, J., Haldar, A.
来源标注的末位/通讯作者：Agnik Haldar
机构：REVA University

### 英文摘要

Genomic foundation models learn representations from DNA sequence, although their usefulness for variant classification depends on the architecture and downstream evaluation procedure. We compared six genomic foundation models using 6,960 ClinVar single-nucleotide variants from ten limb-girdle muscular dystrophy (LGMD)-associated genes, with 4,866 variants assigned to training and 2,094 to held-out testing. The analyses included frozen alternate-minus-reference embeddings at 101, 201 and 501 bp, supervised adaptation at 101 bp, and gene-held-out downstream classifier training. GPN-Star V100 and AlphaGenome Atlas AVI were evaluated separately using their native scores. At 101 bp, frozen Evo2 achieved the highest discrimination among the six foundation models (MCC 0.644; AUROC 0.879; AUPRC 0.818). Supervised adaptation increased MCC for three architectures and reduced it for the remaining three. Extending sequence context to 501 bp improved all three primary metrics in five of six frozen architectures, with Evo2 reaching an MCC of 0.864, AUROC of 0.964 and AUPRC of 0.952. Evo2 also led the frozen gene-held-out readouts (pooled MCC 0.641; AUROC 0.852; AUPRC 0.789). GPN-Star V100 and AVI achieved MCC values of 0.929 and 0.938, respectively, using distinct biological inputs and scoring procedures. The number of variants misclassified across all evaluated configurations decreased from five under the original 101-bp readouts to one after including longer contexts and native scores. An exploratory HGVS-category control identified substantial annotation-associated structure in the benchmark labels. The findings characterize classification performance against aggregate ClinVar labels within LGMD-associated genes. Disease-specific pathogenicity and clinical diagnostic utility remain untested.

---

## 2. Population-level learning of non-additive effects enables accurate and efficient prediction of combinatorial perturbation responses

bioRxiv · 预印本 · 2026-11-23 · 相关性 6/10

**研究关联：方法可借鉴**

- **为什么值得看**：预测组合扰动响应的轻量模型，与我的research interest中single-cell perturbation直接相关，且讨论了基础模型未能超越简单加性基线的现象。
- **任务与验证范围**：输入：单扰动响应测量数据与组合扰动信息 → 输出：组合扰动的伪批量响应预测；研究体系：包含白血病细胞等三个单细胞数据集（其余摘要未说明）；验证范围：跨三个数据集及多种泛化设置，是否跨细胞类型摘要未说明
- **核心方法**：提出轻量级模型GAIN，通过在群体水平上学习偏离加性的非加性交互项来预测组合扰动响应。
- **主要发现与证据**：GAIN在三个单细胞数据集上优于加性基线和细胞级方法，训练速度快3至64倍，并在白血病分化CRISPR筛选中实验验证了基因协同与FACT抑制作用。
- **可借鉴点（研究建议）**：在评估预训练基因组学模型时，可考虑引入基于简单生物学假设的基线模型进行对比，警惕复杂模型在特定任务上可能不如简单加性规律有效。
- **迁移边界**：原论文聚焦于组合扰动响应预测且依赖已有单扰动数据，与基于DNA序列/虚拟表观遗传特征预测增强子活性及评估padding影响的任务在输入模态和预测目标上存在本质差异，其非加性建模方法不能直接迁移。
- **阅读时核实**：GAIN模型中学习到的交互项具体是如何参数化和计算的？其是否依赖于特定的扰动表征或先验网络？

[原文](https://www.biorxiv.org/content/10.64898/2026.11.20.768136v1) · [DOI](https://doi.org/10.64898/2026.11.20.768136)

作者：An, s., Gong, Q., Cao, K.
来源标注的末位/通讯作者：Kai Cao
机构：Broad Institute of MIT and Harvard

### 英文摘要

Combinatorial perturbations are widely used to study genetic interactions and to develop drug combinations, but the number of possible combinations grows quadratically with the number of perturbations, and only a small fraction can be measured in a screen experiment. Despite their growing sophistication, deep-learning and foundation models often fail to outperform a simple additive baseline based on measured single-perturbation responses. This suggests a simpler approach that builds on these measurements and directly learns deviations from additivity at the population level. We therefore developed GAIN, a lightweight model that implements these principles by predicting the pseudobulk response to a combination as the sum of its two single-perturbation responses and a learned interaction term. Across three single-cell datasets of genetic and drug combinations, GAIN corrected deviations from additivity and outperformed the additive model and cell-level methods across generalization settings and metrics, while training 3- to 64-fold faster. Applied to a combinatorial CRISPR screen of leukemia differentiation regulators, GAIN revealed synergy between key regulators of the differentiation block and genes that restrain differentiation but have little effect alone. It also revealed dampening by the histone chaperone FACT, which supports the induction of differentiation genes. These results establish population-level modeling of the deviation from additivity as a simple, accurate and scalable approach to predicting combination responses.

---

中文笔记基于标题和摘要生成，未核验全文；研究建议不代表论文已验证的结论。相关性分数不是论文质量评分。

检索统计：窗口 [2026-11-21 00:00, 2026-11-24 00:00) UTC；抓取 biorxiv 71/pubmed 27 → 粗筛 27 篇 → LLM 选中 2 篇
