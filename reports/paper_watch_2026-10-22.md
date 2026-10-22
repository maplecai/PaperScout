# Paper Scout 日报 2026-10-22

共筛选出 **3** 篇推荐论文。
📊 抓取 arxiv 42/biorxiv 148/pubmed 42 → 粗筛 36 篇 → LLM 选中 3 篇

## 1. A genomic foundation model for interpreting human genetic diversity

- **期刊**: bioRxiv
- **作者**: Xu, Q., Wu, Z., Dong, M. et al. (14 authors)
- **机构**: Mulin Jun Li @ Guangzhou Women and Children's Medical Center, Guangzhou Medical University, Guangzhou, China; Department of Bioinformatics, The Province and Ministry Co-sponso
- **日期**: 2026-10-21
- **ID**: DOI: 10.64898/2026.10.19.760276  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.19.760276v1
- **相关分数**: 8/10
- **一句话推荐**: hEVO是一个在大量人类基因组变异上预训练的基因组基础模型，直接涉及DNA语言模型和调控变异效应预测。
- **方法**: hEVO，一种基于人类群体单倍型序列多样性进行无监督预训练的基因组基础模型。
- **主要发现**: 该模型以远小于十亿参数的规模，在无需任务特定微调的情况下，于功能注释、变异解释及实验测量的调控效应预测等19项基准中18项夺冠，证明了群体单倍型多样性可作为可迁移的生物学信息源。
- **对我的启发**: hEVO以较少参数实现优异调控效应预测，提示在增强子活性预测中可探索基于群体单倍型多样性预训练提取可迁移调控信息，而非单纯依赖扩大模型参数规模。

<details><summary>Abstract</summary>

Interpreting human genomes requires models that recognize shared biological functions while accounting for variation underlying traits, disease susceptibility and adaptation. Here we present hEVO, a genomic foundation model trained on 4.784 billion distinct haplotype sequences reconstructed from whole genome sequencing (WGS) data for 63,809 individuals selected from 550,237 samples across eight cohorts. Pretraining integrates shared sequence features and naturally occurring allelic differences without clinical or functional labels. Against representatives of the Evo 2, NT, GPN and other genomic model families, hEVO ranked first in 18 of 19 primary comparisons spanning functional annotation, variant interpretation and human evolution. Its pretrained allele scores generalized across all six complementary variant benchmarks without task-specific training, achieving the highest performance across clinical pathogenicity, fine-mapped causal variants and experimentally measured regulatory effects. Retrospective ClinVar reclassification further demonstrated improved identification of pathogenic classifications later downgraded, supporting reassessment of earlier clinical interpretations. Predictive strengths extended to ancestry inference, human accelerated sequences and preference for reported selected alleles. This breadth was achieved with substantially fewer parameters than billion-parameter comparators and low inference overhead in the evaluated workloads. These findings establish human haplotype diversity as a source of transferable biological information for interpreting both the disruption of genome function and the variation retained during human evolution.

</details>

---

## 2. Position-dependent variant effects reveal importance of context in genomic regulation

- **期刊**: bioRxiv
- **作者**: Aninta, S. I., Tewhey, R., de Boer, C. G.
- **机构**: Carl G de Boer @ The University of British Columbia
- **日期**: 2026-10-21
- **ID**: DOI: 10.64898/2026.03.17.712488  |  URL: https://www.biorxiv.org/content/10.64898/2026.03.17.712488v1
- **相关分数**: 8/10
- **一句话推荐**: 使用序列模型研究MPRA中变异位置对调控活性的影响，直接涉及增强子活性预测和序列到功能映射。
- **方法**: 基于序列到表达的深度学习模型，系统评估变异在MPRA探针中位置偏移对调控活性的影响。
- **主要发现**: 变异位置显著影响其表达变化幅度（主要由TF位置依赖性活性导致），可能导致MPRA低估变异效应，凸显了顺式调控语法的复杂性。
- **对我的启发**: 启发我在评估预训练基因组学模型 padding 策略时，需重点考察序列截断或填充位置对增强子内部转录因子结合位点相对位置及活性预测结果的偏置影响。

<details><summary>Abstract</summary>

Massively Parallel Reporter Assays (MPRAs) provide a high-throughput framework for functionally characterizing how regulatory DNA sequences impact the expression of a model gene. MPRAs have also proven to be useful for measuring the effects of genetic variation, where each allele is typically tested in the center of ~200 bp of genomic context cloned into the MPRA; but the impact of variant position and local context remains largely unexplored. In this study, we systematically investigate how shifting the position of a variant within an MPRA probe influences its regulatory activity using models that predict expression in MPRAs from DNA sequence. We find that while the direction of variant effects is usually preserved across positions, the magnitude of expression changes can vary substantially depending on where the variant is placed within the construct. This positional bias appears to be largely explained by the strong position-dependent activity of TFs whose binding the variants perturb. In a subset of cases, interactions consistent with cooperativity between TFs also contribute to position-specific effects. ~1% of variants appear to disrupt RNA polymerase III (Pol III) promoters within Alu elements, resulting in position-specificity because both A and B boxes are required for function and exclusion of either motif due to window shifts disrupts the variants' effects. Consequently, this positional bias can lead to underestimating variant effect sizes from MPRAs, resulting in missed causal variants for downstream functional analyses. Our study demonstrates the complexity of cis-regulatory grammar and how regulatory assays used to study variants can confound their interpretation.

</details>

---

## 3. An autoencoder outperforms two transformers on prediction of gene expression from chromatin accessibility

- **期刊**: arXiv
- **作者**: Jesse G. Meyer
- **日期**: 2026-10-20
- **ID**: arXiv: 2610.28853  |  URL: https://arxiv.org/abs/2610.28853
- **相关分数**: 7/10
- **一句话推荐**: 系统比较了自编码器与Transformer在从染色质可及性预测基因表达上的性能，并探讨了跨细胞类型的泛化性问题。
- **方法**: 基于双变分自编码器（scButterfly-B）与多种Transformer架构在染色质可及性到基因表达预测任务上的严格基准测试与消融分析。
- **主要发现**: 双变分自编码器在基因级和细胞内相关性上全面优于Transformer且训练更快；在Transformer内部，Perceiver编码器优于全自注意力，而染色体感知注意力先验反而显著降低性能。
- **对我的启发**: 在评估预训练基因组学模型架构设计时，应警惕引入基于生物学先验的注意力机制（如染色体感知）可能带来的负面效果，并需与简单统计基线进行严格对比。

<details><summary>Abstract</summary>

Models that predict RNA abundance from chromatin accessibility are rarely compared under the same features, targets and metrics. We built one benchmark on 126,604 paired single-nucleus profiles from 19 human studies with a shared vocabulary of 50,000 peaks and 3,185 genes, ten 5x2 cross-validation folds and one scoring target, and compared seven implemented pipelines and two reference predictors across 70 trained runs; each pipeline keeps its own input normalisation and native training target. The scButterfly-B pipeline, built on dual variational autoencoders, outperformed every transformer pipeline, including an autoregressive Perceiver model (Omic Translator) and a support-free reformulation of Cisformer, on per-gene and within-cell Spearman correlation in all sixty paired fold comparisons, with 3.8 times shorter training. Transformer pipelines come within 0.02-0.04 on within-cell profile shape but lag by 0.10-0.24 on per-gene correlation. On two withheld cell types per-gene correlation is low; controls show the podocyte values are typical of within-type correlation for seen cell types of the same size, whereas Paneth values match a cell-agnostic shuffle for every Omic Translator arm. Within the transformer family, prespecified ablations show the Perceiver encoder was worth +0.0439 in within-donor per-gene correlation over full self-attention, a chromosome-aware genomic attention prior reduced it by 0.0096 (exact donor-level sign-flip test, Holm-adjusted p = 1.2e-4), and decoder output order had no detectable effect. A training-mean profile reaches 0.314 within-cell correlation with no input and a constant at the true expressed-gene positions reaches 0.996 per-gene correlation, so oracle-support protocols are reported only as diagnostics. Code, results and an audited release are provided.

</details>

---
