"""总结模块：对最终 Top 论文逐篇生成详细中文总结。

只对 5-10 篇做，控制成本。不读全文，只用 title + abstract。
"""
from __future__ import annotations

import json
import logging

from llm import LLMClient

log = logging.getLogger("paper-scout")

SYSTEM = """你是计算基因组学/机器学习领域的资深研究者，正在为一位研究
「基于虚拟表观遗传特征预测不同细胞类型游离型增强子活性、评估预训练基因组学模型 padding 影响」
的同行写论文阅读笔记。

请基于论文 title + abstract，用中文输出结构化笔记，字段：
- relevance_type: 从“当前课题直接相关”“方法可借鉴”“研究兴趣拓展”中选一个，不要强行关联增强子或 padding
- task_scope: 输入 → 输出；研究物种/细胞体系；验证范围（尤其是否跨细胞类型）。摘要没写的部分注明“摘要未说明”
- core_method: 核心方法/模型（一句话，具体到方法范式）
- main_finding: 主要发现与证据（一两句），优先保留摘要明确给出的数字、基线和实验验证，不编造性能指标
- inspiration: 可借鉴点（一句话），明确这是对我的研究的推测或建议，而非论文已证明的结论；如无关写“无明显直接启发”
- applicability: 迁移边界，区分原论文任务与我的 DNA 序列/增强子/padding 任务，不把跨任务或跨细胞类型泛化当成已证明
- reading_question: 阅读原文时最值得核实的一个具体问题；这是待核实的问题，不是已经发现的缺陷
全部用中文，简洁、专业、不要复述 abstract 原文。
严格输出 JSON 对象，不要输出任何其它内容。
"""


def summarize_papers(papers: list[dict], llm: LLMClient) -> list[dict]:
    for p in papers:
        try:
            user = json.dumps({
                "title": p.get("title", ""),
                "abstract": p.get("abstract", ""),
                "authors": p.get("authors", [])[:5],
                "my_research": "增强子活性预测 / 虚拟表观遗传特征 / 预训练基因组学模型 padding / sequence-to-function",
            }, ensure_ascii=False)
            res = llm.chat_json(SYSTEM, user, temperature=0.3)
            if isinstance(res, dict):
                p["_summary"] = {key: res.get(key, "") for key in (
                    "relevance_type", "task_scope", "core_method", "main_finding",
                    "inspiration", "applicability", "reading_question",
                )}
            else:
                p["_summary"] = {"core_method": "", "main_finding": "", "inspiration": ""}
        except Exception as e:
            log.error("总结失败 [%s]: %s", p.get("title", "")[:40], e)
            p["_summary"] = {"core_method": "", "main_finding": "", "inspiration": ""}
    return papers
