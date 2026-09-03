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
- core_method: 核心方法/模型（一句话，具体到方法范式）
- main_finding: 主要发现（一两句）
- inspiration: 对我研究可能的启发（一句话，要具体，别空泛；如无关写"无明显直接启发"）
全部用中文，简洁、专业、不要复述 abstract 原文。
严格输出 JSON 对象，不要输出任何其它内容。
"""


def summarize_papers(papers: list[dict], llm: LLMClient) -> list[dict]:
    for p in papers:
        try:
            user = json.dumps({
                "title": p.get("title", ""),
                "abstract": p.get("abstract", "")[:2000],
                "authors": p.get("authors", [])[:5],
                "my_research": "增强子活性预测 / 虚拟表观遗传特征 / 预训练基因组学模型 padding / sequence-to-function",
            }, ensure_ascii=False)
            res = llm.chat_json(SYSTEM, user, temperature=0.3)
            if isinstance(res, dict):
                p["_summary"] = {
                    "core_method": res.get("core_method", ""),
                    "main_finding": res.get("main_finding", ""),
                    "inspiration": res.get("inspiration", ""),
                }
            else:
                p["_summary"] = {"core_method": "", "main_finding": "", "inspiration": ""}
        except Exception as e:
            log.error("总结失败 [%s]: %s", p.get("title", "")[:40], e)
            p["_summary"] = {"core_method": "", "main_finding": "", "inspiration": ""}
    return papers
