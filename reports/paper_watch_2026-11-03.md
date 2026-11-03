# Paper Scout 日报 2026-11-03

共筛选出 **2** 篇推荐论文。
📊 抓取 biorxiv 92/pubmed 231 → 粗筛 32 篇 → LLM 选中 2 篇

## 1. A single-cell multimodal foundation model enables cross modality analysis between transcriptome and chromatin

- **期刊**: bioRxiv
- **作者**: Bao, X., Zhu, J., Song, X. et al. (14 authors)
- **机构**: Jie Liu @ University of Michigan
- **日期**: 2026-11-02
- **ID**: DOI: 10.64898/2026.10.28.762297  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.28.762297v1
- **相关分数**: 8/10
- **一句话推荐**: 结合单细胞转录组和染色质可及性基础模型构建共享潜在空间，与表观遗传基础模型和虚拟细胞概念高度相关。
- **方法**: 冻结单细胞基础模型（scFoundation与EpiAgent）并提取模态线性摘要，通过对齐学习构建共享的RNA-ATAC潜在空间。
- **主要发现**: 该模型无需在目标数据集上重训练即可高精度匹配跨模态细胞谱，并能跨模态转移转录因子基序活性以准确预测细胞阶段性变化。
- **对我的启发**: 利用冻结的预训练基因组学模型嵌入结合轻量级线性映射构建跨模态对齐空间，为从单一序列特征预测虚拟表观遗传特征（如增强子活性）提供了低计算开销的迁移范式。

<details><summary>Abstract</summary>

Most single-cell studies measure either gene expression or chromatin accessibility, and connecting the two usually requires fitting a model to each study. Here we present MUTUAL (MUltiome Transfer in a Unified Aligned Latent space), which keeps the single-cell foundation models scFoundation and EpiAgent frozen, combines their embeddings with linear summaries of each modality and learns a shared RNA--ATAC space from 3.0 million paired cells of 400 public multiome datasets. Applied without refitting to ten datasets not used for training, MUTUAL matched cells' RNA and ATAC profiles more accurately than methods fitted on other donors of the same dataset, annotated ATAC-only cells more accurately and transferred transcription-factor motif activity to RNA-only cells beyond what cell-type assignment provides. In a maturation series of stem-cell-derived islets, motif activity predicted from RNA largely reproduced the measured stage-wise changes when other libraries of the series served as the reference. MUTUAL makes public multiome data directly usable by single-modality studies.

</details>

---

## 2. HiCP2GAN: a plug and play foundation model-based GAN for Hi-C enhancement.

- **期刊**: Briefings in bioinformatics
- **作者**: Samuel Olowofila, Oluwatosin Oluwadare
- **机构**: Oluwatosin Oluwadare @ Department of Computer Science, University of Colorado at Colorado Springs, 1420 Austin Bluffs Pkwy, Colorado Springs, CO 80918, United States.
- **日期**: 2026-11-02
- **ID**: DOI: 10.1093/bib/bbag610  |  PMID: 42969856  |  URL: https://pubmed.ncbi.nlm.nih.gov/42969856/
- **相关分数**: 6/10
- **一句话推荐**: 使用预训练Hi-C基础模型作为GAN判别器，与基因组基础模型和表示学习有一定关联。
- **方法**: 采用预训练视觉Transformer基础模型作为判别器构建即插即用GAN框架，用于低分辨率Hi-C数据增强。
- **主要发现**: 预训练基础模型作为GAN判别器能提供具生物学意义的梯度监督，优于传统从头训练的GAN，并提升了现有增强模型的重建质量与生物学可重复性。
- **对我的启发**: 在微调预训练基因组学模型预测增强子活性时，可借鉴本文冻结深层Transformer并微调浅层的策略，以在评估padding等输入扰动时更好地保留预训练的通用基因组特征。

<details><summary>Abstract</summary>

The 3D organization of chromatin shapes gene regulation and cellular function, and Hi-C has become the primary technique for mapping chromatin interactions genome-wide. However, high-resolution data remain costly and scarce, leaving many studies with sparse contact maps that limit downstream analysis. Deep learning methods, especially generative adversarial networks (GANs), have shown promise for enhancing low-resolution Hi-C data, but most existing GAN-based approaches rely on custom discriminators trained from scratch, which can yield unstable training and limited generalization. Hi-C foundation models pretrained on large-scale data capture rich, transferable representations of chromatin structure, yet their use as discriminators within adversarial enhancement frameworks had not been explored. We introduce HiCP2GAN, a plug-and-play GAN that employs a pretrained Vision Transformer-based Hi-C foundation model as its discriminator. The discriminator was pretrained on 118 million Hi-C patches across diverse species and cell types, providing biologically meaningful gradients for adversarial supervision. The framework is generator-agnostic: any compatible Hi-C resolution enhancement architecture can serve as the generator, enabling fair comparison across methods. The encoder phase of the foundation model was adapted as a discriminator backbone, finetuning the first few layers from the input while freezing the deeper transformer layers to preserve pretrained knowledge while allowing task-specific adaptation. Experiments across various cell lines show that HiCP2GAN outperforms traditional GAN-based methods in most settings and improves the reconstruction quality and biological reproducibility of existing Hi-C enhancement models in most evaluated cases. HiCP2GAN is publicly available at https://github.com/OluwadareLab/HiCP2GAN.

</details>

---
