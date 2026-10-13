# Paper Scout 日报 2026-10-13

共筛选出 **2** 篇推荐论文。
📊 抓取 biorxiv 131/pubmed 38 → 粗筛 23 篇 → LLM 选中 2 篇

## 1. Alignment-Aware Genomic Coordinate Encoding for Long-Range DNA Modeling

- **期刊**: bioRxiv
- **作者**: Yang, X., QIN, C., Wang, F., He, B., Zhao, Y., Wu, J., Zhang, Y., Yao, J.
- **机构**: Jianhua Yao @ AI for Life Sciences Lab, Tencent
- **日期**: 2026-10-12
- **ID**: DOI: 10.64898/2026.10.10.757278  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.10.757278v1
- **相关分数**: 8/10
- **一句话推荐**: 提出对齐感知的基因组坐标编码与位置编码策略改进GFM长程调控建模，与你的基因组基础模型和位置/填充策略研究直接相关。
- **方法**: 提出对齐感知的基因组基础模型USM-AA，通过非连续旋转位置编码与包含染色体/链/CIGAR的对齐嵌入模块，结合反向互补掩码预训练建模长程DNA序列。
- **主要发现**: 显式引入参考基因组坐标系的对齐感知表征能显著提升模型对长程调控元件的建模能力，在跨物种及群体变异数据上预训练后，于多项下游任务中优于现有模型。
- **对我的启发**: 在构建增强子活性预测模型时，可探索显式编码基因组坐标与比对信息以增强对远端调控的感知，并重新审视padding操作是否会破坏序列的坐标对齐与长程依赖关系。

<details><summary>Abstract</summary>

Existing genomic foundation models (GFMs) are adept at capturing local, sequential dependencies in DNA. However, their architectures often struggle to efficiently model gene regulation features, such as sparse motifs and distal regulatory elements that operate beyond linear proximity. Moreover, standard positional encodings fail to fully exploit the reference genome coordinate system. Therefore, we present USM-AA, an alignment-aware genomic foundation model that incorporates reference genome coordinates through a non-contiguous positional encoding, Alignment-Aware Rotary Position Embedding, and an alignment embedding module encoding chromosome, strand, and Compact Idiosyncratic Gapped Alignment Report (CIGAR) information. To improve long-range sequence modeling, USM-AA leverages a reverse-complement masked learning strategy. Pretrained on alignment-aware genomic sequences spanning cross-species evolution and human population variation, USM-AA consistently outperforms existing models across multiple downstream tasks, highlighting the importance of alignment-aware representations for genomic sequence modeling.

</details>

---

## 2. Epigenetic Silencing of CYYR1 Promotes Lung Adenocarcinoma Progression Through TRIM21-Dependent Regulation of HMMR Stability.

- **期刊**: Advanced science (Weinheim, Baden-Wurttemberg, Germany)
- **作者**: Fengsheng Dai, Jingyi Tang, Huan Rong et al. (16 authors)
- **机构**: Tingxiu Xiang @ Chongqing Key Laboratory for the Mechanism and Intervention of Cancer Metastasis, Chongqing University Cancer Hospital, Chongqing University, Chongqing, China.
- **日期**: 2026-10-11
- **ID**: DOI: 10.1002/advs.77890  |  PMID: 42860388  |  URL: https://pubmed.ncbi.nlm.nih.gov/42860388/
- **相关分数**: 7/10
- **一句话推荐**: 系统评估单细胞基础模型不同层嵌入在细胞类型和扰动预测中的表现，与你的基础模型评估和单细胞扰动研究兴趣高度相关。
- **方法**: 整合多组学与机器学习分析筛选靶基因，结合分子生物学与类器官模型进行机制验证。
- **主要发现**: CYYR1在肺腺癌中因启动子高甲基化而表观遗传沉默，其通过TRIM21介导的泛素化途径降解HMMR并抑制CDC20致癌信号，从而发挥抑癌作用并增强顺铂敏感性。
- **对我的启发**: 无明显直接启发。

<details><summary>Abstract</summary>

Lung adenocarcinoma (LUAD) remains a leading cause of cancer-related mortality. Integrative multi-omics and machine-learning analyses across independent cohorts identified CYYR1 as a frequently downregulated transmembrane protein in LUAD, with low expression associated with poor prognosis and promoter hypermethylation. CYYR1 restoration suppressed LUAD cell proliferation, migration, invasion, tumor growth, and metastasis. Mechanistically, CYYR1 facilitated TRIM21-dependent ubiquitination and proteasomal degradation of HMMR, thereby reducing CDC20-associated oncogenic signaling. Biochemical and cellular analyses supported this CYYR1-TRIM21-HMMR regulatory relationship, while a patient-derived LUAD organoid model provided proof-of-concept evidence that CYYR1 restoration inhibited organoid growth and reduced HMMR, CDC20, and Ki67 expression. CYYR1 restoration also increased cisplatin sensitivity. Genistein treatment was associated with CDC20 modulation and enhanced cisplatin response, and cellular thermal shift assays provided evidence consistent with CDC20 engagement, although CDC20 dependence of the Genistein response remains unproven. Collectively, these findings identify CYYR1 as an epigenetically dysregulated tumor-suppressive factor that regulates HMMR stability through a TRIM21-dependent mechanism and reveal a potential therapeutic vulnerability in CYYR1-deficient LUAD.

</details>

---
