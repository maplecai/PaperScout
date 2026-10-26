# Paper Scout 日报 2026-10-26

共筛选出 **1** 篇推荐论文。
📊 抓取 biorxiv 88/pubmed 31 → 粗筛 16 篇 → LLM 选中 1 篇

## 1. Centered cross-context perturbation transfer on the public 2025 Virtual Cell Challenge benchmark

- **期刊**: bioRxiv
- **作者**: Luan, H., Chen, L., Yu, G., Yang, Y.
- **机构**: Yang Yang @ AGI Institute, School of Computer Science, Shanghai Jiao Tong University, Shanghai 200240, China
- **日期**: 2026-10-25
- **ID**: DOI: 10.64898/2026.10.20.760514  |  URL: https://www.biorxiv.org/content/10.64898/2026.10.20.760514v1
- **相关分数**: 8/10
- **一句话推荐**: 直接参与2025 Virtual Cell Challenge，解决跨细胞上下文的单细胞扰动响应预测问题，与research_interests中的virtual cell和single-cell perturbation高度吻合。
- **方法**: 结合公共扰动摘要与差异表达核，利用源中心化与保序回归进行跨上下文扰动转移的紧凑数值方法。
- **主要发现**: 该方法在2025 Virtual Cell Challenge基准上达到与历史冠军相当的复合得分，且源中心化策略显著提升了跨上下文的差异表达优先级预测性能。
- **对我的启发**: 无明显直接启发

<details><summary>Abstract</summary>

Predicting transcriptional responses across cellular contexts requires transferring both expression direction and differential-expression priority. We developed a compact numerical method that combines public perturbation summaries with a differential-expression kernel fitted to H1 CRISPRi training targets. The method centers an independent KOLF2.1J source on known training targets, transfers its response signs and magnitude ranks, and uses isotonic regression to render predicted expression means. We evaluated the frozen model retrospectively on the released public TEST100 of the 2025 Virtual Cell Challenge, using an external KOLF source released in 2026. The model achieved DES 0.371834, PDS 0.8614, and MAE 0.302206. With reconstructed historical anchors, its composite score was 0.341344, compared with the archived champion score of 0.340052, a difference of +0.001292. The comparison showed higher DES and lower PDS, with zero normalized MAE contributions for both methods. Source centering also improved development PDS across all three TRAIN folds and official VALIDATION. These results demonstrate a practical numerical approach to cross-context perturbation transfer and differential-expression ranking.

</details>

---
