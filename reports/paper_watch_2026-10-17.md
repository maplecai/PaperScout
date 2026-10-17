# Paper Scout 日报 2026-10-17

共筛选出 **7** 篇推荐论文。
📊 抓取 biorxiv 122/pubmed 84 → 粗筛 40 篇 → LLM 选中 7 篇

## 1. GEMS (GWAS Effect Mechanisms via Sequence-to-Function): Unveiling cell type-specific mechanisms for GWAS variants

- **期刊**: bioRxiv
- **作者**: Xie, X., Qian, S., Chang, D., Bhangale, T., McCarthy, M. I., Eraslan, G., Fletez-Brant, K.
- **机构**: Kipper Fletez-Brant @ Genentech Inc
- **日期**: 2026-10-16
- **ID**: DOI: 10.64898/2026.10.14.759213  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.14.759213v1
- **相关分数**: 9/10
- **一句话推荐**: 利用sequence-to-function模型预测细胞类型特异性的变异效应，直接关联你的跨细胞类型调控元件活性预测研究。
- **方法**: 基于序列到功能模型（Borzoi）的多模态变异效应预测，结合监督分类器与SHAP归因解析GWAS变异的细胞类型特异性机制。
- **主要发现**: GEMS能准确关联GWAS风险变异与疾病相关细胞类型，且预测的变异-细胞类型关联在独立实验数据中显著富集，并能将疾病风险变异聚类为机制不同的细胞类型特异性调控模块。
- **对我的启发**: 可借鉴其利用预训练sequence-to-function模型生成虚拟表观遗传特征（ATAC/RNA），并结合SHAP归因解析变异在特定细胞类型增强子上的调控机制，同时评估模型在训练集峰外区域的泛化能力。

<details><summary>Abstract</summary>

Genome-wide association studies (GWAS) have linked thousands of loci to common diseases, yet for non-coding variants, which constitute the vast majority of the signal, the cell types and states through which individual risk variants act remain largely unknown. Here, we develop GEMS (GWAS Effect Mechanisms via Sequence-to-Function), a framework that trains supervised classifiers on multimodal variant effect predictions (ATAC-seq and RNA-seq) from the sequence-to-function model Borzoi and applies SHAP-based attribution to associate individual GWAS variants with the cell types most relevant to their disease association. Applied to asthma, LDL cholesterol, multiple sclerosis, and type 2 diabetes, GEMS prioritizes known disease-relevant cell types concordant with stratified LD-score regression. At the variant level, GEMS associates a median of 58.7% of fine-mapped variants with at least one cell type via ATAC-seq and 65.9% via RNA-seq, extending cellular annotation beyond the chromatin accessibility peaks in the single-cell atlas used for model training. ATAC-seq variant-cell-type associations are significantly enriched in cis-regulatory elements from independent experimental studies not used in model training, and enrichment persists after excluding variants overlapping training atlas peaks. For multiple sclerosis, hierarchical biclustering of variant--cell-type associations partitions risk variants into immune and CNS modules driven by distinct transcription factor families, recapitulating the immune-mediated and neurodegenerative components of the disease and demonstrating that integrative analysis of sequence-to-function predictions can stratify phenotype-associated variants into mechanistically distinct, cell-type-specific regulatory programs.

</details>

---

## 2. Spatiotemporal AI-based modeling of gene regulation and variant effects in the developing human brain using Seal.

- **期刊**: Nature neuroscience
- **作者**: Yun Hao, Christopher Y Park, Chandra L Theesfeld, Olga G Troyanskaya
- **机构**: Olga G Troyanskaya @ Center for Computational Biology, Flatiron Institute, New York, NY, USA. ogt@princeton.edu.
- **日期**: 2026-10-15
- **ID**: DOI: 10.1038/s41593-026-02470-2  |  PMID: 42881222  |  URL: https://pubmed.ncbi.nlm.nih.gov/42881222/
- **相关分数**: 8/10
- **一句话推荐**: 提出基于AI的序列到功能迁移学习框架，预测跨细胞类型和发育阶段的基因表达及变异效应。
- **方法**: 基于迁移学习的AI框架（Seal），结合基因组序列实现跨时空、细胞类型的基因表达与变异效应建模。
- **主要发现**: Seal能在数据受限的瞬时发育阶段和细胞类型中预测变异的调控效应，并成功揭示自闭症队列中瞬时胎儿兴奋性神经元的从头调控变异负担。
- **对我的启发**: Seal利用迁移学习克服特定细胞类型数据稀缺问题并实现时空特异性预测，启发我在预测不同细胞类型游离型增强子活性时，可引入迁移学习策略结合虚拟表观遗传特征，以提升模型在数据匮乏细胞类型上的泛化能力。

<details><summary>Abstract</summary>

Understanding how genetic variation shapes gene regulation in the developing human brain remains a central challenge in neuroscience, particularly in transient cell types and developmental stages where data are limited. We present Seal, an interpretable artificial intelligence (AI) transfer learning framework for genome-based modeling of gene expression and variant effects with spatiotemporal resolution across 26 regions, 30 cell types and 7 developmental stages. Seal predictions provide mechanistic interpretation by linking variants to transcriptional regulators in a spatiotemporal context. Applying Seal to genome-wide association studies, we identify shared and distinct regulatory architectures across six neuropsychiatric conditions that align with clinical trajectories. In the Simons Simplex Collection autism cohort whole-genome data, Seal uncovers a significant burden of de novo regulatory variants in transient fetal excitatory neurons, revealing cell-type-specific and stage-specific effects. By connecting genetic variation to spatiotemporal regulatory programs, Seal offers a general framework for uncovering mechanisms of human brain development and disease.

</details>

---

## 3. Sequence sensitivity of open chromatin reveals constrained regulatory elements underlying human traits

- **期刊**: bioRxiv
- **作者**: Tomizuka, K., Koido, M., Suzuki, A. et al. (13 authors)
- **机构**: Chikashi Terao @ RIKEN
- **日期**: 2026-10-16
- **ID**: DOI: 10.1101/2024.10.31.621195  |  URL: https://www.biorxiv.org/content/10.1101/2024.10.31.621195v1
- **相关分数**: 8/10
- **一句话推荐**: 使用机器学习量化序列扰动对染色质可及性的影响，跨细胞类型识别功能重要的调控元件。
- **方法**: 提出CAMBUS框架，利用虚拟序列扰动量化机器学习模型预测的染色质可及性敏感性，以此对功能重要的开放染色质区域进行优先排序。
- **主要发现**: 仅基于序列敏感性识别的调控区域在未使用任何遗传或进化先验的情况下，仍高度富集于进化约束区、超级增强子及复杂疾病因果变异，并呈现细胞类型特异性。
- **对我的启发**: 可借鉴虚拟序列扰动范式，通过评估序列突变对预训练模型预测虚拟表观遗传特征的影响，来检验不同padding策略下模型对增强子核心序列边界效应的捕捉能力与鲁棒性。

<details><summary>Abstract</summary>

Open chromatin regions (OCRs) delineate cell-type-specific regulatory landscapes across the genome, yet their functional importance varies considerably. Here, we introduce CAMBUS (Chromatin Accessibility Mutation Burden Score), a machine-learning framework that quantifies the sensitivity of predicted chromatin accessibility to sequence perturbation to prioritize functionally important OCRs. Applying CAMBUS to 29 immune cell types, we identified 66,043 CAMBUS-defined OCRs (cOCRs), without directly incorporating human genetic variation or existing evolutionary constraint metrics. Nevertheless, cOCRs were strongly enriched in independently defined constrained regions (odds ratio (OR)=11.45 (95% confidence interval (CI) 9.33-14.05), P=4.7 x 10-68), and active regulatory elements, with enrichment for super-enhancers remaining after adjustment for established constraint metrics and sequence features (OR=6.18 (95% CI 3.80-10.05), P=2.1 x 10-13). cOCRs also showed cell-type-specific enrichment for the heritability of immune-mediated diseases and for putative causal variants identified by statistical fine-mapping across European and East Asian ancestries, including rare variants. Integration with statistical fine-mapping further linked 1,533 putative causal variants across 70 complex traits to cell-type-specific cOCRs, revealing plausible regulatory mechanisms underlying complex traits. Together, CAMBUS provides a region-centered framework for identifying regulatory elements whose predicted activity is sensitive to sequence disruption and that are enriched for evolutionary constraint, complementing existing regulatory and constraint annotations for interpreting non-coding genetic variation.

</details>

---

## 4. A relational architecture of the human genome

- **期刊**: bioRxiv
- **作者**: Kurth, I., Krause, J., Danner, M. et al. (9 authors)
- **机构**: Ingo Kurth @ RWTH Aachen, University Hospital
- **日期**: 2026-10-16
- **ID**: DOI: 10.64898/2026.10.15.759350  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.15.759350v1
- **相关分数**: 8/10
- **一句话推荐**: 利用基因组基础模型进行全基因组序列扰动以构建位置间依赖网络，与你的DNA语言模型和序列表示学习研究高度相关。
- **方法**: 基于预训练大语言模型（Nucleotide Transformer v3）的全基因组级单核苷酸系统性扰动与注意力依赖图谱构建。
- **主要发现**: 揭示了跨编码/非编码区的高阶基因组位置依赖网络（relons），该网络受进化约束并与致病性遗传变异高度关联。
- **对我的启发**: 该研究对序列进行逐位置扰动以提取依赖关系的方法，启发我在评估预训练模型padding对虚拟表观遗传特征及增强子活性预测影响时，可引入逐位置扰动分析来量化padding引入的伪依赖关系。

<details><summary>Abstract</summary>

Complex systems exhibit organization not only through their components but also via their interdependencies. Local nucleotide dependencies underpin regulatory motifs and RNA structures, yet principles governing a higher-order organization across the human genome remain unknown. Here we systematically perturbed every position of the com- plete telomere-to-telomere human genome using Nucleotide Transformer v3 with an ex- ascale compute cluster, generating nucleotide-resolution dependency maps that reveal a directed, weighted network of position-to-position genomic relationships. This network recapitulates known biological features and uncovers recurrent, directional architec- tures termed 'relons', spanning coding, non-coding, and unannotated regions. These re- lational modules reflect evolutionary and functional constraints and associate with hu- man genetic variation and pathogenic variants. Our findings suggest a higher-order rela- tional layer of genome organization, providing a framework to interpret DNA as a complex system of dependencies beyond linear and 3D structure, with implications for under- standing genetic variation and disease.

</details>

---

## 5. Emerging frontiers for AI in single-cell genomics.

- **期刊**: Molecular cell
- **作者**: Sneha Mitra, Jiaxin Li, Christina S Leslie
- **机构**: Christina S Leslie @ Computational and Systems Biology Program, Memorial Sloan Kettering Cancer Center, New York, NY 10065, USA. Electronic address: lesliec@mskcc.org.
- **日期**: 2026-10-15
- **ID**: DOI: 10.1016/j.molcel.2026.09.014  |  PMID: 42880218  |  URL: https://pubmed.ncbi.nlm.nih.gov/42880218/
- **相关分数**: 7/10
- **一句话推荐**: 综述AI在单细胞基因组学中的应用，涵盖虚拟细胞、单细胞扰动和表观基础模型，与你的研究兴趣高度相关。
- **方法**: 综述单细胞基因组学中的AI基础模型与嵌入方法，涵盖scRNA-seq/scATAC-seq预训练及基于Perturb-seq的“虚拟细胞”建模范式。
- **主要发现**: 早期单细胞基础模型缺乏实验生物学家关注，但大规模图谱数据与多组学/Perturb-seq技术的涌现，为利用AI整合海量先验数据并构建“虚拟细胞”模型提供了实质性契机。
- **对我的启发**: 在构建基于虚拟表观遗传特征的增强子活性预测模型时，可借鉴单细胞多组学调控基因组学的预训练范式，利用大规模图谱数据优化预训练基因组学模型的上下文表征与泛化能力。

<details><summary>Abstract</summary>

We are just over a decade into the single-cell revolution in biology, which has been coupled to the growing use of artificial intelligence (AI) in single-cell genomics. Most early single-cell RNA embedding models and subsequent "foundation models"-representational models pretrained on large single-cell datasets-did not gain wide traction among experimental biologists. However, as massive single-cell RNA-sequencing (scRNA-seq) atlas efforts ramp up, there is a clear rationale for exploiting AI models to interpret new datasets in the context of vast existing data resources. Meanwhile, the advent of single-cell epigenetic/multiomic assays and Perturb-seq technologies presents new opportunities for AI modeling. Here, we review AI embedding and foundation models for scRNA-seq and single-cell assay for transposase-accessible chromatin using sequencing (scATAC-seq), extensive machine-learning efforts to exploit single-cell multiome in regulatory genomics, and AI strategies to learn "virtual cell" models from Perturb-seq, ending with a description of current limitations of single-cell AI models and an outlook for future advances.

</details>

---

## 6. Analysis of single nucleotide substitution in CYP21A2 gene using Alphagenome

- **期刊**: bioRxiv
- **作者**: Matveeva, A., Xu, Y., Pandey, A. V.
- **机构**: Amit V Pandey @ University of Bern
- **日期**: 2026-10-16
- **ID**: DOI: 10.64898/2026.10.15.759360  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.15.759360v1
- **相关分数**: 7/10
- **一句话推荐**: 直接使用AlphaGenome（我的代表性论文之一）对CYP21A2基因进行全位点饱和突变评分，涉及基因组基础模型的实际应用与变异效应预测。
- **方法**: 利用预训练基因组学模型 AlphaGenome 对特定基因进行全转录本跨度的单核苷酸饱和突变扫描，预测多组织转录与剪接效应。
- **主要发现**: AlphaGenome 可实现特定基因座全单碱基替换的评分，其调控预测评分能区分不同临床分类的变异，但部分已知剪接缺陷在预测总RNA水平上未表现出显著下降。
- **对我的启发**: 该研究利用预训练模型进行饱和突变扫描的范式，可启发我通过系统性序列截断或移位扫描，定量评估预训练基因组学模型在游离型增强子活性预测中对序列上下文及padding长度的敏感性。

<details><summary>Abstract</summary>

Context: CYP21A2 encodes steroid 21-hydroxylase, which supplies precursors for adrenal glucocorticoid and mineralocorticoid synthesis. Interpretation of its variants is complicated by a homologous pseudogene, complex alleles, heterogeneous functional assays and uncertain noncoding effects. We integrated observed variation with a reference-locus saturation analysis to distinguish transcriptional, splicing and protein-level mechanisms. Methods: The NM_000500.9 MANE transcript was reconstructed from GRCh38 genomic sequence and verified against RefSeq and UniProt P08686. ClinVar, gnomAD and UniProt records were retrieved with provenance, and a cutoff-limited PubMed search was reconciled against Entrez. AlphaGenome Atlas scores were obtained for every possible single nucleotide substitution across the 3,230-bp transcript span. Reported non-SNV alleles were analyzed by direct AlphaGenome inference. Adrenal, testis, ovary, placenta, liver and kidney expression predictions were calculated. Results: The results include 483 ClinVar records, 3,208 gnomAD records and 82 UniProt natural-variants. All 9,690 locus-wide substitutions were scored, comprising 6,018 exonic and 3,672 intronic substitutions. The coding set contained 3,201 missense, 1,098 synonymous, 147 stop-gained, nine start-lost, eight stop-lost and one stop-retained substitution. Direct inference was completed for 413 additional reported alleles and four context controls. Established splice defects, including c.293-13C>G and c.738+75C>T, showed appreciable splicing scores without corresponding large reductions in predicted total RNA. Clinical classification groups differed in AVI score distributions. Conclusions: A sequence-verified CYP21A2 catalogue connects clinical annotations, population observations, splicing predictions and measured enzyme function. Complete single-base coverage of the defined CYP21A2 transcript was achievable. Regulatory predictions should guide mechanistic experiments and remain separate from enzyme activity, tissue function and clinical classification.

</details>

---

## 7. Learning how single cells respond to perturbations.

- **期刊**: Molecular cell
- **作者**: Ekin Deniz Aksu, Bonnie Berger
- **机构**: Bonnie Berger @ Computer Science and Artificial Intelligence Laboratory, MIT, Cambridge, MA 02139, USA; Department of Mathematics, MIT, Cambridge, MA 02139, USA. Electronic address: bab@mit.edu.
- **日期**: 2026-10-15
- **ID**: DOI: 10.1016/j.molcel.2026.09.033  |  PMID: 42880214  |  URL: https://pubmed.ncbi.nlm.nih.gov/42880214/
- **相关分数**: 6/10
- **一句话推荐**: 评论单细胞扰动响应预测模型，与你的single-cell perturbation研究兴趣相关。
- **方法**: State模型，基于机器学习范式预测单细胞转录组对遗传或化学扰动的响应并实现跨细胞上下文泛化。
- **主要发现**: 该模型能够跨越不同细胞环境泛化，准确预测单细胞在受到基因或化学干扰后的转录组变化。
- **对我的启发**: State模型跨细胞上下文泛化的机制，可启发在增强子活性预测中如何有效编码不同细胞类型的虚拟表观遗传特征以提升跨上下文泛化能力。

<details><summary>Abstract</summary>

In a recent issue of Cell, Adduri et al.1 introduce State, a machine learning model that generalizes across different cellular contexts and predicts how single-cell transcriptomes respond to genetic or chemical perturbations.

</details>

---
