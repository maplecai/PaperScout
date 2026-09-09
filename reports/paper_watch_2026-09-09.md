# Paper Scout 日报 2026-09-09

共筛选出 **10** 篇推荐论文。
📊 抓取 arxiv 28/biorxiv 510/pubmed 60 → 粗筛 100 篇 → LLM 选中 10 篇

## 1. EukaUTR: a foundation model for functional modelling and design of eukaryotic 3' UTRs

- **期刊**: bioRxiv
- **作者**: lang, M., Fang, X., Chen, M. et al. (9 authors)
- **机构**: Xiaolin Li @ Hangzhou Institute of Medicine, Chinese Academy of Sciences, Hangzhou, 310018, Zhejiang, China
- **日期**: 2026-09-08
- **ID**: DOI: 10.64898/2026.09.07.749809  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.07.749809v1
- **一句话推荐**: 提出了一个针对3' UTR的序列到功能再到设计的基础模型，与你的序列到功能预测和序列表示学习兴趣高度相关。
- **方法**: 基于跨进化谱系的大规模真核 3' UTR 序列预训练，构建统一预测、解释与设计的序列到功能基础模型。
- **主要发现**: EukaUTR 在 13 项转录后调控与表达预测任务上迁移性能显著优于基线（最高提升 27.45%），并具备生成功能性新序列及指导稳定性编辑的设计能力。
- **对我的启发**: 其跨谱系大规模预训练提升下游多任务迁移性的策略，可借鉴用于构建跨细胞类型增强子活性预测的预训练模型，以增强虚拟表观遗传特征预测的泛化能力。

<details><summary>Abstract</summary>

Eukaryotic mRNA 3' UTRs encode regulatory signals that shape post-transcriptional regulation, RNA fate and gene expression. However, a foundation model that spans broad eukaryotic 3' UTR sequence space while unifying prediction, interpretation and design within a single framework is still lacking. Here we present EukaUTR, a 3' UTR-specific foundation model trained on a large-scale eukaryotic 3' UTR sequence corpus spanning diverse evolutionary lineages. Across 13 prediction tasks of post-transcriptional regulation, RNA fate and expression output, EukaUTR showed strong transferability, achieving relative improvements of up to 27.45% over the strongest baselines. Extending these capabilities to sequence design, EukaUTR generated novel 3' UTRs that captured natural sequence patterns and regulatory features and EukaUTR-Guide extracted stability signals from small sets of 3' UTRs to guide editing toward enhanced predicted stability. Together, EukaUTR establishes a sequence-to-function-to-design framework that connects broad eukaryotic representation learning with transferable functional prediction and mRNA design.

</details>

---

## 2. A Transferable Genomic Language Model Framework for Fungal Gene Essentiality Prediction

- **期刊**: bioRxiv
- **作者**: Liao, C., Thomas, H.
- **机构**: Chen Liao @ Dartmouth College
- **日期**: 2026-09-08
- **ID**: DOI: 10.64898/2026.09.03.749190  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.03.749190v1
- **一句话推荐**: 评估了基因组语言模型在预测真菌基因必需性上的表现，与你的DNA语言模型和序列到功能预测兴趣直接相关。
- **方法**: 结合预训练基因组语言模型（Evo2）DNA嵌入与系统级特征（直系同源、PPI）的多模态迁移学习框架。
- **主要发现**: 预测性能瓶颈在于预训练DNA嵌入包含的生物信息量而非下游分类器复杂度；整合系统级特征的多模态方法可突破此瓶颈并实现跨物种迁移。
- **对我的启发**: 在评估预训练基因组学模型预测增强子活性时，需警惕DNA序列嵌入向高阶表观遗传特征映射时的信息衰减，可考虑整合虚拟表观遗传特征等多模态信息以突破瓶颈。

<details><summary>Abstract</summary>

Predicting biological function from genomic sequence remains a major challenge in computational and systems biology. Here, we tested whether the genomic language model Evo2, which encodes context-dependent DNA sequence patterns into embeddings, enables prediction of essential genes in fungi, a phenotype central to fungal biology and antifungal target discovery. We found that model performance was constrained not by the type or complexity of the downstream classifier, but by the biological information contained in Evo2 DNA embeddings. Specifically, the information recoverable from these embeddings progressively declined for biological features further downstream of DNA sequence, revealing a bottleneck for predicting higher-order cellular phenotypes. We alleviated this bottleneck by integrating Evo2 embeddings with two sequence-informed, system-level features: ortholog-based essentiality and protein-protein interactions. The multimodal framework demonstrated consistent performance both within and across three evolutionarily divergent yeasts (Candida albicans, Saccharomyces cerevisiae, and Schizosaccharomyces pombe), and its predictions were supported by published experimental evidence when transferred to the filamentous mold Aspergillus fumigatus. These results establish our framework as a transferrable tool for predicting essential genes across fungal genomes, including species with limited or no experimentally determined essentially data.

</details>

---

## 3. Plant cis-regulatory grammar: Decoding the multidimensional code of transcriptional regulation for programmable crop engineering.

- **期刊**: Journal of integrative plant biology
- **作者**: Libin Zhang, Maoteng Li
- **机构**: Maoteng Li @ Key Laboratory of Molecular Biophysics of the Ministry of Education, College of Life Science and Technology, Huazhong University of Science and Technology, Wuhan, 430074, China.
- **日期**: 2026-09-08
- **ID**: DOI: 10.1111/jipb.70386  |  PMID: 42708417  |  URL: https://pubmed.ncbi.nlm.nih.gov/42708417/
- **一句话推荐**: 综述了植物顺式调控元件的AI预测与设计，并提出了植物调控语法基础模型的构想，与你的增强子设计和基础模型兴趣有一定关联。
- **方法**: 综述提出结合单细胞表观基因组学与AI基础模型解码植物顺式调控语法并设计合成CREs的方法范式。
- **主要发现**: CRE功能不仅源于DNA序列，更依赖多维表观遗传上下文；构建植物调控语法基础模型可实现超越自然进化的基因表达预测与工程化。
- **对我的启发**: 论文强调CRE功能对多维表观上下文的依赖，启发我在游离型增强子活性预测中，将虚拟表观遗传特征作为核心上下文信息融入预训练基因组学模型，以提升跨细胞类型的预测精度。

<details><summary>Abstract</summary>

Cis-regulatory elements (CREs) orchestrate the spatiotemporal precision of gene expression that underlies plant development, adaptation, and domestication. Decoding the cis-regulatory grammar of plant genomes remains a central challenge in modern biology, with profound implications for programmable crop engineering. Here, recent conceptual and technological advances are synthesized to reshape our understanding of plant CREs. This review first argues that CRE function is not only an intrinsic property of DNA sequence alone but also emerges from a multidimensional context, including chromatin accessibility, histone modifications, three-dimensional genome topology, and cell type-specific regulatory landscapes. Furthermore, the convergence of single-cell epigenomics, high-throughput functional assays, and CRISPR-based dissection has begun to unravel this contextual grammar, revealing the computational principles governing transcriptional regulation. Critically, we propose that artificial intelligence (AI) platforms are catalyzing an ongoing transition from descriptive discovery to predictive engineering, wherein these platforms outperform natural evolution in designing synthetic CREs. Finally, a roadmap is outlined toward a plant regulatory grammar foundation model, which will enable truly predictive engineering of gene expression when fine-tuned for specific tasks. Collectively, the integration of single-cell resolution maps, precise genome editing, AI-driven design, and regulatory-compliant delivery systems promises to transform our ability to reprogram plant gene regulation for next-generation agriculture, bridging the gap between foundational regulatory biology and tangible crop improvement.

</details>

---

## 4. Is FFT window length a neutral preprocessing choice in CNN-based dolphin whistle detection? A cross-domain sensitivity analysis.

- **期刊**: bioRxiv
- **作者**: De Marco, R., Iurcev, M., Trebbi, A., Lagorio, S.
- **机构**: Rocco De Marco @ Institute of Biological Resources and Marine Biotechnology (IRBIM) - National Research Council (CNR)
- **日期**: 2026-09-08
- **ID**: DOI: 10.64898/2026.05.01.721665  |  URL: https://www.biorxiv.org/content/10.64898/2026.05.01.721665v1
- **一句话推荐**: 虽领域为声学，但其研究预处理参数对CNN跨域泛化影响的实验设计，与我评估基因组基础模型padding策略的研究在方法论上高度相似。
- **方法**: 基于声谱图的CNN分类模型结合跨域敏感性分析，评估FFT窗口长度这一预处理参数对模型泛化能力的影响。
- **主要发现**: 常规被视为中性的预处理参数（FFT窗口长度）在域内验证中表现一致，但在跨域评估中对模型泛化能力产生显著且系统性的影响，甚至导致无法被域内验证察觉的迁移失败。
- **对我的启发**: 该跨域敏感性分析范式可直接借鉴，用于系统评估预训练基因组学模型中不同padding策略对跨细胞类型增强子活性预测泛化能力的影响，避免仅依赖域内指标得出错误结论。

<details><summary>Abstract</summary>

Convolutional neural networks (CNNs) operating on spectrogram images are the established method for automated cetacean whistle detection in passive acoustic monitoring (PAM). The FFT window length (N_fft) used during spectrogram generation is routinely fixed without justification, yet it determines the time-frequency resolution and, consequently, how the resulting image is distorted when resized to a fixed CNN input dimension. This study presents a controlled sensitivity analysis of N_fft across five values (128, 256, 512, 1024, 2048) on binary Tursiops truncatus whistle detection, using 10-fold cross-validation on an in-domain dataset (Oltremare, 192 kHz) and cross-domain evaluation on an independent open-ocean benchmark (DCLDE 2022). All experiments were conducted within a formally defined, open-source pipeline (ai-pam-pipeline). In-domain performance is uniformly high across all configurations. Cross-domain results diverge: N_fft = 256 significantly outperforms 512, 1024, and 2048 in macro F1, while maintaining a false discovery rate (FDR) of exactly zero across all 10 folds and all tested classification thresholds. N_fft = 128 achieves comparable recall but produces FDR > 0 in all 10 folds, exhibiting a transfer failure that is undetectable by in-domain validation. These results show that a preprocessing parameter routinely treated as an implementation detail has a large, systematic effect on cross-domain generalization. The study does not aim to propose N_fft = 256 as a universal optimum; rather, it tests the common assumption that this parameter is neutral and safe under a fully specified representation regime, and demonstrates that it is not.

</details>

---

## 5. A Transformer-Based Delta Expression Encoder for Psilocybin Transcriptional Response: Architecture, Representations, and Biological Validation

- **期刊**: arXiv
- **作者**: Sai Jayakumar
- **日期**: 2026-09-08
- **ID**: arXiv: 2609.08165  |  URL: https://arxiv.org/abs/2609.08165
- **一句话推荐**: 使用Transformer编码器对单细胞转录组药物扰动进行建模，与你的单细胞扰动和表示学习兴趣间接相关。
- **方法**: 基于Transformer的差异表达编码器，在无先验监督下从单核RNA测序伪bulk数据中分类基因表达变化状态。
- **主要发现**: 模型在预测赛洛西宾转录响应时表现出细胞类型依赖的准确率，发现下调响应比上调更具跨个体一致性，且注意力机制可无监督恢复药物特异性基因共调控模块。
- **对我的启发**: 无明显直接启发

<details><summary>Abstract</summary>

Understanding why individuals respond differently to psilocybin requires modeling the drug's transcriptional perturbation signature at the cell-type level. I present a Transformer-based delta expression encoder that learns to classify differential gene expression status - upregulated, downregulated, or neutral - from single-nucleus RNA-sequencing data, without supervision from pathway annotations or prior biological knowledge. The model is trained on pseudobulk profiles from 623 examples spanning 18 cell types, 2 drug conditions, and 6 timepoints derived from the Liao et al. 2025 dataset, and achieves 69.4% weighted classification accuracy. Three principal findings are reported, alongside one direct test of a published hypothesis that returned a result inconsistent with that hypothesis. First, per-cell-type classification accuracy ranges from 28.3% (L2/3 IT, a primary HTR2A-expressing psilocybin target) to 99.6% (endothelial cells), consistent with known psilocybin response biology. Second, psilocybin-induced transcriptional downregulation is significantly more stereotyped across individuals than upregulation (Mann-Whitney U=18615.0, p<0.0001), a novel finding with a cortical depth gradient across excitatory subtypes. Third, attention-guided gene co-regulation analysis recovers drug-specific modules without pathway supervision. Separately, a direct test of whether baseline HTR2A expression predicts drug-response separability across cell types found a significant negative correlation (Spearman r = -0.7088, p = 0.0021), the opposite of what a simple HTR2A-gating account would predict.

</details>

---

## 6. A single-nucleus multiomic and spatial atlas of gene regulation in human spermatogenesis

- **期刊**: bioRxiv
- **作者**: Bhaskaran, J., Ing-Simmons, E., Balaguer Balsells, I. et al. (15 authors)
- **机构**: Juan M Vaquerizas @ MRC Laboratory of Medical Sciences, London, UK
- **日期**: 2026-09-08
- **ID**: DOI: 10.64898/2026.09.04.749409  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.04.749409v1
- **一句话推荐**: 构建了精子发生过程中的单核多组学和空间基因调控图谱，属于调控基因组学数据资源，但缺乏新的计算建模方法。
- **方法**: 整合单核多组学（snATAC-seq与snRNA-seq）与空间转录组数据，构建并推断阶段特异性的基因调控网络（GRN）。
- **主要发现**: 构建了人类精子发生的高分辨率时空基因调控图谱，揭示了生殖与体细胞发育阶段的特异性调控网络，并将非编码不孕症风险位点映射至特定细胞类型的候选增强子及靶基因。
- **对我的启发**: 该研究产生的单核ATAC-seq数据及推断的细胞类型特异性增强子-靶基因关联，可作为评估预训练基因组学模型在生殖细胞发育场景下预测游离型增强子活性的高质量基准验证集。

<details><summary>Abstract</summary>

Gametogenesis, the production of oocytes and sperm, ensures the faithful transmission of genetic material to the next generation. In males, spermatogenesis occurs within the testis, where germ cells progress through a highly ordered developmental programme in close association with supporting somatic cells. Defects in this process cause infertility, yet the gene regulatory mechanisms coordinating normal and dysfunctional human spermatogenesis remain incompletely defined. Here we generate a single-nucleus multiomic and spatial atlas of human spermatogenesis by profiling chromatin accessibility and gene expression in the same nuclei and integrating these data with spatial transcriptomics of intact testicular tissue. We infer high-confidence gene regulatory networks that resolve stage-specific activity of known and novel candidate regulators across germline and somatic compartments, and map spatially restricted signalling interactions within the seminiferous tubule niche. Integration with infertility-associated genetic variation links non-coding risk loci to candidate enhancers and target genes in cell-type-specific regulatory contexts. Finally, profiling clinical cryptozoospermia samples as in vivo perturbations supports the ability of this network to capture downstream transcriptional consequences of disease-associated regulatory disruption. Together, these data provide a spatially resolved regulatory framework for human spermatogenesis and a foundation for interpreting the molecular basis of male infertility.

</details>

---

## 7. MI-PEFT: Mixture-of-Experts Integrated Parameter-Efficient Fine-Tuning Protein Language Models Improves Acidophilic Proteins Classification

- **期刊**: arXiv
- **作者**: Honghan Shen
- **日期**: 2026-09-07
- **ID**: arXiv: 2609.08059  |  URL: https://arxiv.org/abs/2609.08059
- **一句话推荐**: 虽是语言模型PEFT方法，但针对蛋白质而非DNA基因组基础模型，仅有间接参考价值。
- **方法**: 基于ESM C-600M预训练蛋白语言模型，融合LoRA参数高效微调与DeepSeekMoE混合专家分类头的PEFT框架。
- **主要发现**: 该框架通过保留预训练表征并引入MoE分类头，在高度类别不平衡的嗜酸蛋白分类任务中显著提升了特异性与计算效率。
- **对我的启发**: 在多细胞类型增强子活性预测中，可借鉴MoE分类头建模不同细胞类型的特异性，并结合PEFT策略缓解小样本或类别不平衡问题。

<details><summary>Abstract</summary>

Acidophilic proteins that remain stable and functional under highly acidic conditions, are important for industrial biocatalysis, acid-related bioprocessing, and the discovery of acid-stable enzymes. However, their identification relies heavily on time-consuming experimental screening methods. With the rapid growth of protein sequence databases, the need for computational identification methods that are both accurate and efficient has become stronger. The emergence of protein language models (PLMs) has significantly improved the sequence representation of downstream biological prediction tasks. This paper proposes MI-PEFT, a mixture-of-experts integrated parameter-efficient fine-tuning framework. Built on the ESM C-600M backbone, the framework incorporates LoRA-based PEFT methods and a DeepSeekMoE-based classification head to resolve the limitations of PEFT and significantly improve computational efficiency. Notably, this task is characterized by a significant class imbalance in the dataset, making high specificity particularly challenging. The experimental results demonstrate that MI-PEFT on PLMs, especially {\text{C}}^{\text{3}}\text{A}, serves as an efficient tool for identifying acidophilic proteins and a constrained pathway that helps resolve class-imbalance by preserving the pretrained representations.

</details>

---

## 8. Deep Barycentric Regression for Optimal Transport Map Estimation and its Statistical Optimality

- **期刊**: arXiv
- **作者**: Kunwoong Kim, Insung Kong, Yongdai Kim
- **日期**: 2026-09-06
- **ID**: arXiv: 2609.06598  |  URL: https://arxiv.org/abs/2609.06598
- **一句话推荐**: 提出了一种基于深度学习的最优传输图估计方法，并在单细胞扰动预测任务上进行了验证。
- **方法**: 提出BROT（两步深度重心回归法），先计算无正则化最优传输计划，再用深度神经网络通过最小二乘回归拟合传输映射。
- **主要发现**: 该方法在Lipschitz条件下具备minimax最优收敛率，规避了对抗训练的不稳定性，并在单细胞扰动预测等下游任务中提升了性能。
- **对我的启发**: 论文利用最优传输进行分布对齐与单细胞扰动预测，启发我在处理不同细胞类型间虚拟表观遗传特征的分布差异时，可引入BROT进行特征空间对齐，以提升跨细胞类型增强子活性预测的泛化能力。

<details><summary>Abstract</summary>

The optimal transport (OT) map provides a geometric transformation for aligning probability distributions and has become a useful tool in machine learning. However, existing estimators of the OT map still exhibit a gap between sharp statistical guarantees and practical parametric estimation based on stable training objectives. Theoretical estimators achieve minimax optimal convergence rates, but they are typically nonparametric and can incur demanding implementation design or inference costs. Practical estimators are parametric and scalable, but their statistical guarantees remain underexplored, and their min-max, adversarial-like training objectives can be sensitive to optimization algorithms. We propose BROT (Barycentric Regression for OT), a simple two-step method that first computes the unregularized OT plan and then fits a deep neural network (DNN) to the induced barycentric targets by least-squares regression. Under standard regularity conditions, we prove that the DNN estimator of BROT attains the minimax convergence rate, when the ground-truth OT map is Lipschitz. Numerical studies on synthetic datasets and an image dataset show that BROT provides accurate map estimates, strong target distribution matching, and competitive transport costs, compared to existing estimation methods. Experiments on two downstream tasks, single-cell perturbation prediction and unsupervised domain adaptation, further suggest that the accurate estimation of BROT can translate into stronger task performance.

</details>

---

## 9. scFLAME: a unified generative model for interpretable clustering, hierarchical structure discovery and marker-gene identification in single-cell RNA-seq data

- **期刊**: bioRxiv
- **作者**: Rao, J., Jihad, M., Biffi, G., Kirk, P. D.
- **机构**: Jackie Rao @ MRC Biostatistics Unit
- **日期**: 2026-09-08
- **ID**: DOI: 10.64898/2026.09.04.749363  |  URL: https://www.biorxiv.org/content/10.64898/2026.09.04.749363v1
- **一句话推荐**: 提出单细胞转录组数据的统一概率生成模型，与你的single-cell perturbation和virtual cell兴趣有一定间接关联。
- **方法**: 结合负二项因子分析与高斯混合先验的统一概率生成模型，实现单细胞转录组数据的联合嵌入与聚类。
- **主要发现**: 该模型以单一可解释框架替代了多步分析流程，在聚类精度、跨平台鲁棒性及大规模数据扩展性上均优于现有方法。
- **对我的启发**: 无明显直接启发。

<details><summary>Abstract</summary>

Identifying cell types from single-cell RNA sequencing (scRNA-seq) data typically requires several separate and often uninterpretable steps: dimensionality reduction, batch-correction, clustering, marker-gene identification and the discovery of finer-grained structure. Here we introduce scFLAME (single-cell Factor Latent Analysis with Mixture Embeddings), a probabilistic generative model that unifies these tasks: a negative binomial factor analysis of the raw counts - which can be adjusted for batch - is coupled to a Gaussian mixture prior over the latent space, learning the embedding and clustering jointly, while a shared linear decoder provides cluster-specific marker genes directly from the fitted model, and a merging procedure recovers a probabilistic hierarchy of finer-grained partitions. On simulated and real data, scFLAME matches or exceeds state-of-the-art clustering accuracy, is robust across sequencing platforms, and scales near-linearly to hundreds of thousands of cells. scFLAME thus replaces a chain of separate tools with a single, interpretable model for single-cell analysis.

</details>

---

## 10. Toward De Novo Protein Design from Natural Language

- **期刊**: bioRxiv
- **作者**: Dai, F., You, S., Zhu, Y. et al. (26 authors)
- **机构**: Fajie Yuan @ Westlake University
- **日期**: 2026-09-08
- **ID**: DOI: 10.1101/2024.08.01.606258  |  URL: https://www.biorxiv.org/content/10.1101/2024.08.01.606258v1
- **一句话推荐**: 基于自然语言的蛋白质从头设计基础模型，与你的representation learning for biological sequences和foundation model兴趣间接相关。
- **方法**: 提出基于自然语言到蛋白质序列/结构的多模态基础模型（Pinal），通过大规模合成蛋白质-文本对进行预训练。
- **主要发现**: 该模型能直接从自然语言功能描述生成具有高可折叠性和功能多样性的全新蛋白质，且在多个实验任务中无需迭代优化即表现出预期催化或功能活性。
- **对我的启发**: 利用自然语言作为高级接口指导序列到功能映射的思路，可启发将虚拟表观遗传特征转化为语义表征，以指导增强子活性预测的预训练模型设计。

<details><summary>Abstract</summary>

Programming biological function-designing bespoke proteins to perform specified molecular tasks-is a foundational goal of molecular engineering. However, current design paradigms remain fundamentally limited: they typically require either natural proteins as starting points for optimization or manual reformulation of functional goals as geometric and sequence-level constraints to guide candidate generation. Here we introduce Pinal, a 16-billion-parameter foundation model that designs candidate proteins from natural-language descriptions of desired function. Trained on 1.7 billion synthetically annotated protein-text pairs, Pinal links functional intent to protein sequence and structure. In computational evaluations, generated candidates combined high predicted foldability with functional-description alignment and sequence diversity, providing a basis for prioritizing experimentally testable designs. We applied Pinal to four distinct design tasks-a fluorescent protein, a polyethylene terephthalate hydrolase, an alcohol dehydrogenase and a metabolic H-protein-and experimentally observed the intended function in each case, including catalytic activity for both designed enzymes. Crucially, without iterative experimental optimization, a Pinal-designed H-protein increased product titer by 1.7-fold relative to the corresponding native E. coli H-protein in a multi-enzyme CO2 fixation pathway. These findings support natural language as a high-level interface for candidate generation in protein design, enabling programmable exploration with reduced reliance on manually specified structural or sequence constraints.

</details>

---
