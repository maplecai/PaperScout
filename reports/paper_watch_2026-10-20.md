# Paper Scout 日报 2026-10-20

共筛选出 **5** 篇推荐论文。
📊 抓取 biorxiv 87/pubmed 18 → 粗筛 21 篇 → LLM 选中 5 篇

## 1. Comprehensive molecular impact mapping of common and rare variants at GWAS loci

- **期刊**: bioRxiv
- **作者**: Balderson, B., Tule, S., Okino, M.-L. et al. (11 authors)
- **机构**: Graham McVicker @ Salk Institute for Biological Studies, La Jolla CA, USA
- **日期**: 2026-10-19
- **ID**: DOI: 10.1101/2025.06.05.658079  |  URL: https://www.biorxiv.org/content/10.1101/2025.06.05.658079v1
- **相关分数**: 10/10
- **一句话推荐**: 提出DNACipher序列到功能模型预测跨细胞类型变异效应，直接对标AlphaGenome，命中序列到功能和跨细胞类型泛化。
- **方法**: DNACipher是一种基于深度学习的sequence-to-function模型，输入524kb基因组序列以预测变异在跨38,582种细胞类型/assay组合中的分子效应，并结合DVIM方法对变异进行优先排序。
- **主要发现**: 该模型在90%以上的GWAS位点中识别出影响变异，其常见变异预测与统计精细映射高度一致，罕见变异富集于已知关联，并在1型糖尿病中获多实验验证。
- **对我的启发**: 模型采用524kb超长序列输入以捕获跨细胞类型的变异效应，提示在评估预训练基因组学模型padding影响时，可探究超长上下文窗口对增强子活性预测及虚拟表观遗传特征提取的依赖性。

<details><summary>Abstract</summary>

Deep learning sequence to function models can predict the molecular effects of genetic variants, but their predictions are limited to the cell types and assays they are trained on. Here we describe DNACipher, a deep learning model that predicts the effects of genetic variants across diverse biological contexts-including those not directly measured. DNACipher takes 524 kb of genome sequence as input and predicts variant effects across 38,582 cell type/assay combinations, > 6 times as many contexts as AlphaGenome. We also introduce DNACipher Deep Variant Impact Mapping, a method to prioritize variants within trait-associated loci based on elevated predicted molecular effects relative to non-trait-associated variants. Applied to 590,604 common and rare variants at GWAS loci across 10 complex traits, DVIM identified imVars at > 90% of GWAS loci for 9 out of 10 traits. Common imVars were significantly concordant with statistical fine-mapping, and rare imVars were enriched for prior trait associations. For type 1 diabetes (T1D), imVars also had predicted effects that were supported by single-nucleus ATAC-seq, luciferase assays, and massively parallel reporter assays. DNACipher DVIM prioritises common and rare variants at GWAS loci by predicting molecular effects across cellular contexts.

</details>

---

## 2. Re-evaluating the benefit of pretraining scale in cell foundation models

- **期刊**: bioRxiv
- **作者**: Shakeel, M. H., Shen, M., Mangiola, S.
- **机构**: Muhammad Haroon Shakeel @ Adelaide University
- **日期**: 2026-10-18
- **ID**: DOI: 10.64898/2026.06.04.730272  |  URL: https://www.biorxiv.org/content/10.64898/2026.06.04.730272v1
- **相关分数**: 9/10
- **一句话推荐**: 重新评估单细胞基础模型的预训练规模与评估方法，与用户对基础模型评估（如padding策略影响）的关注高度相关。
- **方法**: 结合标准微调、完全冻结评估与零样本分析，重新评估单细胞基础模型预训练数据规模的scaling law。
- **主要发现**: 标准微调下的性能饱和掩盖了模型表征能力的真实上限；在完全冻结和零样本设定下，预训练规模对表征质量的提升依然显著。
- **对我的启发**: 在评估预训练基因组学模型（如预测增强子活性）时，应引入完全冻结或零样本评估范式，以避免微调掩盖padding等预训练设计对表征质量的真实影响。

<details><summary>Abstract</summary>

Single-cell foundation models are self-supervised neural networks pretrained on millions of cellular transcriptomes to learn representations that transfer across biological domains and downstream tasks. Recent benchmarks have questioned the training data scaling law for these models, showing early finetuning performance saturation on a fraction of available pretraining data. However, whether this trend holds for larger second-generation foundation models, and whether it reflects genuine saturation of foundation representations remains unclear. To resolve these aspects, we tested the performance of second- and first-generation cell foundation models across corpus sizes using the standard finetuning approach, and extended it with a comprehensive fully frozen evaluation. We revealed that the training-data scaling relationship becomes apparent under fully frozen finetuning, particularly for second-generation models. Zero-shot analyses similarly recovered dependence on pretraining scale. We conclude that finetuning performance saturation does not imply biological representations saturation, and that a shift in standards of cell foundation model evaluation is needed, complementing standard finetuning with fully frozen benchmarking to capture the quality of the foundation representations.

</details>

---

## 3. RegDesign-Bench: Benchmarking computational methods for cell-type-specific regulatory DNA design

- **期刊**: bioRxiv
- **作者**: Xu, J., Guo, Z., Zhong, C. et al. (9 authors)
- **机构**: Pan Deng @ Zhongguancun Academy
- **日期**: 2026-10-19
- **ID**: DOI: 10.64898/2026.10.18.759890  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.18.759890v1
- **相关分数**: 9/10
- **一句话推荐**: 系统基准测试细胞类型特异性顺式调控元件设计方法，直接命中增强子设计与细胞类型特异性调控元件预测的研究兴趣。
- **方法**: 构建标准化计算基准框架（RegDesign-Bench），系统评估细胞类型特异性顺式调控元件的从头设计方法。
- **主要发现**: 发现高预测活性与细胞类型选择性、基序信号及参考序列分布相似度之间缺乏一致性，揭示了现有设计方法在不同评估维度上存在应用依赖的局限性。
- **对我的启发**: 在评估游离型增强子活性预测模型时，不能仅依赖单一预测活性指标，需结合细胞特异性、基序富集等多维度验证模型在 sequence-to-function 映射上的真实性能。

<details><summary>Abstract</summary>

The de novo design of regulatory DNA sequences that drive cell-type-specific gene expression could enable precise gene control in synthetic biology, cell engineering and gene therapy. Various computational methods have been developed for this task, yet systematic comparisons that guide method selection for different design objectives remain limited. Here, we introduce RegDesign-Bench, a standardized framework for evaluating cell-type-specific cis-regulatory element design through a comprehensive set of computational analyses. Among the methods tested, strong predicted activity was not consistently accompanied by cell-type-selective accessibility or prominent cell-type-associated motif signals. Similarity to reference sequence distributions also did not ensure high predicted target-cell activity or specificity. These findings demonstrate that favourable performance on individual measurements does not necessarily extend across regulatory properties and library characteristics, revealing application-dependent strengths and limitations of current design methods. Overall, RegDesign-Bench offers a general-purpose computational framework for comparing and selecting methods to design regulatory DNA that drives cell-type-specific gene expression.

</details>

---

## 4. DCAF: Unifying Data Validity, Evaluation Validity and Predictive Modeling for Single-cell Perturbation Simulation

- **期刊**: bioRxiv
- **作者**: Xia, T., Lei, C., Chen, N. et al. (11 authors)
- **机构**: Yuxiang Li @ BGI Research, Wuhan
- **日期**: 2026-10-19
- **ID**: DOI: 10.64898/2026.10.13.758713  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.13.758713v1
- **相关分数**: 8/10
- **一句话推荐**: 提出单细胞扰动模拟框架DCAF，涉及跨细胞类型泛化和调控动力学建模，直接命中单细胞扰动兴趣。
- **方法**: 提出统一框架DCAF，结合最优传输重建单细胞扰动状态、改进的log fold change评估指标以及基于JEPA与显式调控动力学的预测模型。
- **主要发现**: DCAF在跨基因、跨细胞类型和跨区域泛化上超越SOTA及简单基线，并成功重现小鼠大脑中细胞类型特异性的调控异质性。
- **对我的启发**: DCAF利用JEPA学习潜在表示并显式建模调控动力学以提升跨细胞类型泛化能力，启发我在预测不同细胞类型增强子活性时可引入JEPA架构提取虚拟表观遗传特征的鲁棒表征。

<details><summary>Abstract</summary>

Single-cell perturbation profiling is limited by cost and throughput, while computational methods remain constrained by inconsistent evaluation and underperformance relative to simple baselines. Here we present DCAF, a unified framework for single-cell perturbation simulation that that jointly addresses data validity, evaluation validity and predictive modeling. Among its three components, DCAF-data addresses the single-measurement limitation by reconstructing pre- and post-perturbation status using entropy-regularized optimal transport, and is demonstrated on both cell line and multi-cell type datasets. DCAF-criterion evaluates log fold changes in non-silenced genes to improve sensitivity to model error and robustness to zero inflation noise, validated on synthetic datasets. DCAF-model combines JEPA with explicit modeling for regulatory-dynamics modeling for interpretable prediction. Across benchmarks, DCAF outperforms state-of-the-art deep-learning methods, as well as mean and linear baselines in cross-gene, cross-cell-type and cross-region generalization. In adult Mouse brain, DCAF recapitulates known cell-type-specific regulatory heterogeneity of Dgcr8 knockdown at both cell type and gene levels. DCAF thus provides a rigorous and biologically grounded foundation for reliable perturbation simulation across development, disease and therapeutic discovery.

</details>

---

## 5. Auditing Confidence-Calibrated Benchmarking of Single-Cell Perturbation Models

- **期刊**: bioRxiv
- **作者**: Gallone, M., Ravidath, S., Madireddy, S.
- **机构**: Shyam Ravidath @ Algoverse AI
- **日期**: 2026-10-19
- **ID**: DOI: 10.64898/2026.10.12.758706  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.12.758706v1
- **相关分数**: 8/10
- **一句话推荐**: 审计单细胞扰动模型的基准测试方法，揭示评估陷阱，与用户对模型评估和单细胞扰动的兴趣高度相关。
- **方法**: 基于零基线审计和诊断程序的单细胞扰动模型基准测试失效模式分析
- **主要发现**: 现有基准测试存在系统性评估漏洞（如身份预测器导致的“回声天花板”和未见扰动被静默替换），且不确定性量化方法的优劣排名高度依赖于评估指标选择（覆盖率与排序能力相悖）。
- **对我的启发**: 在评估预训练基因组学模型预测增强子活性时，需引入零基线（如恒定均值或序列打乱模型）验证模型是否真正学习了序列到功能的映射，而非依赖输入序列的冗余特征产生“回声”效应。

<details><summary>Abstract</summary>

Single-cell perturbation models are increasingly assessed for both predictive performance and calibrated uncertainty under distribution shift. We constructed such an evaluation harness (two datasets, Norman 2019 and Replogle 2022; four split types over six dataset-split combinations; three models, scVI, CPA and a linear Ridge baseline; three uncertainty quantification methods, MC dropout, quantile regression and split conformal prediction) and then audited it against null baselines it had never included. Most of its headline results measure something other than what their metric names claim. The harness supplied each test cell to the model as input and then scored the model on reproducing that same cell's expression, so an identity predictor returning the input unchanged attains a perturbation-effect correlation of 1.0 on all six splits: any model given the target cell is measured against this echo ceiling rather than against a null. Against a constant train-mean predictor, scVI wins on 99.7% of Norman cells but only 0.2% of Replogle cells. One split held out sequencing batches rather than perturbations; another scores no genuinely novel perturbation after label collapse; unseen perturbations are silently replaced with a negative-control sentinel at inference; and the most convention-sensitive decision-value entry moves 29.2 percentage points under a library-size convention that changes that row's all-gene MSE by 0.01%. Because a validation budget is spent on a ranked shortlist rather than on a marginal interval, we also score each uncertainty signal by the DE-gene error it avoids in the top k: the worst-calibrated method is the best ranker, and a benchmark reporting only coverage orders the two backwards. We document six failure modes, each with its mechanism, the diagnostic that exposes it, and a detection procedure transferable to other harnesses. One result survives, with a boundary condition: split-conformal coverage calibrated on K562 residuals under-covers on RPE1 (0.900 to 0.847), and marginal coverage at the nominal 0.900 is compatible with covering 0.271 to 0.342 of the DE-gene intervals a prioritization decision would rest on. We continue to recommend conformal prediction, recalibrated per cellular context and reported per gene set rather than marginally.

</details>

---
