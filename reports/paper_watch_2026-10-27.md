# Paper Scout 日报 2026-10-27

共筛选出 **5** 篇推荐论文。
📊 抓取 biorxiv 98/pubmed 28 → 粗筛 25 篇 → LLM 选中 5 篇

## 1. Evaluating the added value of sequence models in noncoding RNA assays: a baseline-aware framework

- **期刊**: bioRxiv
- **作者**: Guo, R., Shan, W., Liu, R., Yang, L., Mu, D., WANG, H.
- **机构**: HONG WANG @ the First Hospital of Jilin University
- **日期**: 2026-10-25
- **ID**: DOI: 10.64898/2026.10.22.760090  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.22.760090v1
- **相关分数**: 8/10
- **一句话推荐**: 系统评估AlphaGenome、RNA-FM等序列基础模型在非编码RNA任务中的增量贡献，直接关联基因组基础模型评估和sequence-to-function研究兴趣。
- **方法**: 基线感知评估框架，通过固定序列组成、正则化强度与身份聚合策略等控制变量，量化预训练序列模型相对显式基线的残差增量贡献。
- **主要发现**: 经基线校正后，预训练序列模型（RNA-FM、AlphaGenome等）在非编码RNA任务上的增量普遍极小甚至为负；负或近零增量不能等同于信息缺失或模型等价，需在解释残差前严格检验基线构成与正则化。
- **对我的启发**: 评估预训练基因组学模型padding对增强子活性预测的影响时，应先固定序列组成与虚拟表观遗传特征基线，再量化不同padding策略的残差增量，避免将padding引入的微小性能波动误判为模型信息差异。

<details><summary>Abstract</summary>

Sequence models are evaluated against non-coding RNA assay read-outs, but prediction alone does not show what their features add to an explicit baseline. We estimated model-added-last changes in AUROC for lncRNA labels and cross-validated Spearman correlation for miRNA repression, fixing members and chromosome folds across available sources. In cross-cell CRISPRi (n = 2961), AlphaGenome increased AUROC from 0.6426 to 0.7551; adding K562 accessibility changed these values to 0.7282 and 0.7534. Corrected-source Cas13 increments ranged from -0.0161 to +0.0130 (n = 871). Separate post-audit comparisons tested fixed sequence composition, broader regularization and TargetScan aggregate identity. With expanded regularization, composition improved four baselines but reduced Cas13 AUROC by 0.0365. RNA-FM's increment was -0.0014 for CRISPRi and +0.000044 for HEK293FT after composition adjustment; small signs changed with regularization. On the same 1227 HeLa members, replacing a seed-family aggregate with an identity-supported mature-miRNA aggregate increased baseline Spearman from 0.4140 to 0.4799. RNA-FM then added 0.0170, or 0.0014 after composition adjustment. These source-row aggregates lack experimental transcript/site alignment. The results support testing baseline content, identity and regularization before interpreting residual model increments. Negative or near-zero increments do not establish absent information or equivalence. Resampling summaries remain conditional descriptions or non-joint sensitivities; calibrated confirmation, justified practical-size thresholds and pretraining-overlap verification were unavailable.

</details>

---

## 2. AlphaGenome informed machine learning for pathogenicity prediction of germline mutations

- **期刊**: bioRxiv
- **作者**: Kumar, P., Singh, S., Garai, S. et al. (11 authors)
- **机构**: Kanaka KK @ ICAR- Indian Institute of AGricultural Biotechnology, Ranchi, India
- **日期**: 2026-10-25
- **ID**: DOI: 10.64898/2026.10.20.760593  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.20.760593v1
- **相关分数**: 7/10
- **一句话推荐**: 直接使用AlphaGenome（我的代表性论文之一）的细胞类型特异性功能基因组分数作为下游特征进行变异致病性预测，与sequence-to-function和基因组基础模型应用高度相关。
- **方法**: 融合群体等位基因频率、VEP变异注释与AlphaGenome细胞类型特异性功能基因组特征的梯度提升树致病性分类器。
- **主要发现**: AlphaGenome衍生的111个功能特征为致病性预测提供了显著的增量性能（Delta AUC = 0.1539），且模型对非编码区及非错义变异实现了100%的覆盖评分。
- **对我的启发**: AlphaGenome提供的细胞类型特异性功能基因组特征在变异效应预测中具有强互补性，这提示我在增强子活性预测中可探索引入此类预训练模型的细胞特异性特征作为下游机器学习模型的输入。

<details><summary>Abstract</summary>

Accurate interpretation of germline variants remains a central challenge in clinical genomics. Existing in silico pathogenicity predictors often provide incomplete coverage or restricted to missense variants from the coding region, leaving the variants from splice sites, -UTR, and intronic regions under-scored. We present AGVarPred, a gradient-boosted classifier designed to predict the pathogenicity of germline mutants, with a broad consequence-class coverage across SNVs and indels. Here, the population allele frequency from gnomAD, functional consequence annotations from Ensembl VEP, and cell-type-specific functional genomic scores from the AlphaGenome platform were integrated to develop the classifier. Using a gene-level split of 134,002 high-confidence ClinVar variants across 9,222 genes, AGVarPred achieved an AUC-ROC of 0.9753 (95% CI 0.9731-0.9775) and a AUC-PR of 0.9606 on 12,385 scored internal test variants. A paired DeLong analysis showed that the full model significantly outperformed an allele-frequency-plus-VEP model ({Delta}AUC = 0.1539, 95% CI 0.1489-0.1589; p < 1 x 10-300), supporting a substantial incremental contribution from AlphaGenome-derived features. Performance remained strong when restricted to SNVs (AUC-ROC 0.9558) and was also high for indels (AUC-ROC 0.9532). On five external benchmarks, AUC-ROCs ranged from 0.528 on a functional-assay-derived benchmark to 0.977 on a clinically curated deafness database, reflecting its dependence on benchmark composition and label source. A separate analysis of the VIP Database, whose pathogenic labels are ClinVar-derived, showed consistent performance (AUC-ROC of 0.892) in held-out genes. AGVarPred scored 100% of evaluated variants in the external benchmarks, whereas AlphaMissense and REVEL covered only small fractions of non-missense variants. Model interpretation indicated that gnomAD allele frequency was the dominant individual predictor; the 111 AlphaGenome features provided complementary functional signal, with splicing and chromatin assays contributing to the largest share of the AlphaGenome SHAP mass. A web-based interface for AGVarPred is available at https://pankaj357.github.io/AGVarPred/ to facilitate the submission of normalized GRCh38 germline variants and retrieval of pathogenicity predictions using the frozen AGVarPred model.

</details>

---

## 3. Prediction transfer does not imply reliability transfer in single-cell foundation models

- **期刊**: bioRxiv
- **作者**: Park, H. J., Sriram, A., Luo, T., Zhang, L.
- **机构**: Hyun Jung Park @ University of Pittsburgh-Pittsburgh Campus
- **日期**: 2026-10-26
- **ID**: DOI: 10.64898/2026.10.21.760716  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.21.760716v1
- **相关分数**: 7/10
- **一句话推荐**: 系统研究单细胞基础模型在跨上下文扰动预测中的可靠性迁移问题，直接关联single-cell perturbation和基础模型评估两个研究兴趣。
- **方法**: 提出基于交叉拟合SHAP解释的可靠性归因指纹（reliability-attribution fingerprints），用于量化单细胞基础模型跨上下文迁移时的可靠性评估特征。
- **主要发现**: 预测迁移与可靠性迁移是两种不同的泛化形式，具有相似可靠性归因指纹的源上下文能实现更优的可靠性迁移，但该结构在严格跨家族迁移时部分依赖于共享的上下文信息。
- **对我的启发**: 在评估预训练基因组学模型跨细胞类型预测增强子活性时，不能仅依赖预测性能指标，可借鉴可靠性归因指纹（如基于SHAP的上下文级特征）来评估模型在不同细胞类型或padding策略下的置信度迁移能力。

<details><summary>Abstract</summary>

Single-cell foundation models are increasingly transferred across tissues, diseases, perturbation screens, and experimental platforms. Although substantial effort has focused on prediction transfer, it remains unclear whether a model's assessment of its own reliability transfers similarly across biological contexts. Here we define reliability transfer as the ability to transfer an accurate assessment of when model predictions are likely to be correct or incorrect and investigate its behavior across ten perturbation-prediction systems spanning multiple datasets, models, and evaluation settings. We find that reliability transfer varies substantially across source-target pairs and cannot be inferred from predictive performance alone, indicating that prediction transfer and reliability transfer constitute distinct forms of generalization. Analyses of biological annotations, network connectivity, target exposure, and contextual factors reveal that prediction reliability is associated with both shared and context-dependent signals, with their relative importance differing across systems. To characterize this variability, we introduce reliability-attribution fingerprints, context-level signatures derived from strictly cross-fitted SHAP explanations that summarize how reliability estimators combine biological and contextual information when assigning confidence. Across systems, contexts with similar attribution-magnitude fingerprints tended to transfer reliability more successfully, and fingerprint similarity identified transfer sources achieving higher reliability-transfer performance within the observed candidate set. However, these relationships weakened under stricter cross-family transfer settings, indicating that transferable reliability structure remains partly dependent on shared contextual information. Finally, transferred reliability estimators produced different perturbation rankings despite identical perturbation predictions, illustrating a practical consequence of reliability transfer for downstream prioritization. Together, these results establish reliability transfer as a distinct aspect of foundation-model generalization and introduce reliability-attribution fingerprints as a framework for characterizing transferable reliability structure across biological contexts.

</details>

---

## 4. Interpreting Short Tandem Repeat Variations with Plant Genomic Foundation Models in Olive

- **期刊**: bioRxiv
- **作者**: Xia, F., Pakdel, M. H., Mazinani, M. H., Asadi, A., Zeng, Y., Zhang, J., Shariati, V., Anisimova, M.
- **机构**: Maria Anisimova @ Zurich University of Applied Sciences; Swiss Institute of Bioinformatics
- **日期**: 2026-10-26
- **ID**: DOI: 10.64898/2026.10.21.760403  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.21.760403v1
- **相关分数**: 6/10
- **一句话推荐**: 使用植物基因组语言模型评估STR变异对embedding的扰动，其中fixed-length input construction的鲁棒性分析与我的padding策略评估项目间接相关。
- **方法**: 利用多个植物基因组语言模型提取序列嵌入，量化短串联重复序列长度变异引起的嵌入扰动，并结合表型关联进行变异优先级排序。
- **主要发现**: 基因组语言模型能捕捉自然STR长度变异的规律性响应，且该响应在固定长度输入构建下具有鲁棒性，优于非重复序列indel。
- **对我的启发**: 论文验证了预训练模型对固定长度输入（padding）构建的鲁棒性，可为评估padding策略对增强子活性预测影响提供对照基准。

<details><summary>Abstract</summary>

Short tandem repeats (STRs) are highly mutable, multiallelic variants with distinctive mutation dynamics and have been associated with phenotypic variation across diverse species. However, genome-wide STR variation remains poorly characterized in olive, and the large number of naturally occurring alleles creates a challenge for variant interpretation. Genomic language models offer a potential way to assess how STR length changes alter learned sequence representations, but their responses to natural multiallelic STR series have not been systematically evaluated. Here, we identified 117,119 polymorphic STRs across 212 Iranian and Mediterranean olive accessions. STRs recovered the major SNP-defined ancestry axes while resolving additional geographically structured subcomponents. We then quantified STR-induced embedding perturbation using three plant genomic language models: AgroNT, PlantCAD2, and GPN. Across all three models, embedding distance generally increased with repeat-length difference from the reference allele, and 7,417 loci were embedding-sensitive in all three models. These signals were robust to fixed-length input construction and exceeded those of matched nonrepetitive indels at most tested loci. Integration with oil-composition associations prioritized four exploratory loci supported by all three models. Overall, we provide a genome-wide olive STR resource and show that plant genomic language models capture reproducible responses to natural STR length variation. Combining cross-model embedding evidence with phenotype association provides a potential framework for prioritizing candidate STRs for further investigation.

</details>

---

## 5. flodl-bio: First Rust data, transformers and model layer for entire deep learning on biological sequences

- **期刊**: bioRxiv
- **作者**: Sablok, G., de Stefanis, F.
- **机构**: Gaurav Sablok @ Alexanier Berlin Germany
- **日期**: 2026-10-26
- **ID**: DOI: 10.64898/2026.10.21.760383  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.21.760383v1
- **相关分数**: 6/10
- **一句话推荐**: Rust实现的生物序列深度学习框架，明确涉及padded sequences处理和alphabet-aware encoding，并在GUE基准上与Nucleotide Transformer、DNABERT-2等基因组基础模型对比，与我的padding策略评估和基因组DL项目相关。
- **方法**: 提出基于Rust和libtorch的生物序列深度学习库flodl-bio，集成序列编码、图构建工具及CNN、RNN与Transformer等多种模型架构。
- **主要发现**: 在GUE基准的转录因子结合预测任务中，使用该库从零训练的轻量级motif CNN（约1万参数）超越了所有CNN基线，并在部分数据集上优于超大规模预训练模型（如Nucleotide Transformer和DNABERT-2）。
- **对我的启发**: 该库支持padded sequences编码且具备位级实验复现性，可借鉴其确定性的序列填充策略与底层框架，以在评估预训练基因组学模型padding影响时精确控制变量并保证结果可复现。

<details><summary>Abstract</summary>

Python ecosystem dominates the deep learning framework. flodl-bio is a Rust crate that extends flodl, a libtorch-backed deep-learning framework, with deep learning on biological sequences. To our knowledge, flodl-bio is the first Rust crate that provides a comprehensive and practical deep learning for the biological applications, which includes the alphabet-aware sequence encoding, including one-hot and k-mer representations, padded sequences, and channels-first batches. It also includes several FASTA parsing and graph construction utilities for adjacency matrices, GCN-normalised adjacency matrices, graph Laplacians, residue contact maps, and de Bruijn graphs. Among the added functionalities, it includes AUROC and AUPRC with their associated curves; classification metrics, and the export of learned convolutional filters as MEME motifs and seeded splits. Deep biological learning includes a multi-width motif CNN, a dilated residual CNN, bidirectional LSTM and GRU architectures, and transformer encoder. On the five human transcription-factor-binding datasets in the GUE benchmark, a motif CNN with approximately 10,000 parameters, trained from scratch, outperforms all published CNN baselines. It also superseded the 2.5-billion-parameter Nucleotide Transformer on two datasets and DNABERT-2 on one. Given a fixed hardware configuration and software stack, experiments are reproducible at the bit level. See Supplementary Table S2 of Supplementary Material. flodl-bio is written in Rust and released under the MIT licence at https://github.com/sablokg/flodl-bio. The core builds with stable Rust and has no dependencies. The model tier is enabled with the flodl Cargo feature (cuda for NVIDIA GPUs) and requires libtorch and Rust 1.91 or later. The evaluation harness is in the repository's experiments directory, and the complete run outputs are archived at https://doi.org/10.5281/zenodo.23321850

</details>

---
