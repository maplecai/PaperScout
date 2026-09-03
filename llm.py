"""共享 LLM 客户端封装 —— 纯 requests 实现，走 OpenAI 兼容接口。

千帆的 "OpenAI 协议兼容" endpoint 就是标准的 POST {base_url}/chat/completions，
请求体/返回体与 OpenAI 一致，用 requests 直接调即可，无需 openai SDK。
GLM / OpenAI / DeepSeek 均可：endpoint / key / model 全部从环境变量读取。
"""
from __future__ import annotations

import json
import os
import re
import time
import logging

import requests

log = logging.getLogger("paper-scout")

MAX_RETRIES = 3
BACKOFF_BASE = 2.0  # 秒，指数退避


class LLMClient:
    def __init__(self, config: dict | None = None):
        cfg = (config or {}).get("llm", {})
        self.base_url = os.environ.get(
            cfg.get("base_url_env", "OPENAI_BASE_URL"), ""
        ).rstrip("/")
        self.api_key = os.environ.get(cfg.get("api_key_env", "OPENAI_API_KEY"), "")
        self.model = os.environ.get(cfg.get("model_env", "OPENAI_MODEL"), "")
        self.enabled = bool(self.base_url and self.api_key and self.model)
        if not self.enabled:
            log.warning(
                "LLM 未启用（缺少 OPENAI_BASE_URL / OPENAI_API_KEY / OPENAI_MODEL）。"
                "rank/summarize 将退化为占位输出。"
            )
            return
        # 国内 endpoint 不走代理：Clash 等代理会掐断长连接导致 SSL EOF。
        # GitHub Actions 上没有代理变量，此设置无副作用。
        self.session = requests.Session()
        if _is_domestic(self.base_url):
            self.session.trust_env = False
            log.info("检测到国内 endpoint，已禁用代理")
        log.info("LLM 启用: model=%s base_url=%s", self.model, self.base_url)

    # ---- 底层调用（带重试）-------------------------------------------
    def _chat(self, system: str, user: str, temperature: float = 0.2) -> str:
        if not self.enabled:
            return ""
        url = f"{self.base_url}/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            "temperature": temperature,
        }
        last_err = None
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                r = self.session.post(url, headers=headers, json=payload, timeout=120)
                if r.status_code == 429 or r.status_code >= 500:
                    # 限流/服务端错误值得重试
                    raise requests.HTTPError(
                        f"HTTP {r.status_code}: {r.text[:200]}", response=r
                    )
                r.raise_for_status()
                return r.json()["choices"][0]["message"]["content"] or ""
            except requests.HTTPError as e:
                # 4xx（除 429）是请求本身的问题，重试无意义
                code = getattr(e.response, "status_code", None)
                if code and 400 <= code < 500 and code != 429:
                    log.error("LLM 请求错误（不重试）: %s", e)
                    raise
                last_err = e
            except Exception as e:
                last_err = e
            if attempt < MAX_RETRIES:
                wait = BACKOFF_BASE ** attempt
                log.warning(
                    "LLM 调用失败 (第 %d/%d 次)，%.0fs 后重试: %s",
                    attempt, MAX_RETRIES, wait, str(last_err)[:150],
                )
                time.sleep(wait)
        log.error("LLM 调用最终失败（已重试 %d 次）: %s", MAX_RETRIES, last_err)
        raise last_err

    # ---- 结构化 JSON 输出 -------------------------------------------
    def chat_json(self, system: str, user: str, temperature: float = 0.2) -> object:
        """让 LLM 返回 JSON。防御性解析：去 markdown fence，提取第一个 JSON 对象/数组。"""
        raw = self._chat(system, user, temperature)
        return parse_json_defensive(raw)

    def chat_text(self, system: str, user: str, temperature: float = 0.3) -> str:
        return self._chat(system, user, temperature)


def _is_domestic(url: str) -> bool:
    """国内 LLM endpoint 判定：这些域名不该走境外代理。"""
    domestic = (
        "baidubce.com",      # 百度千帆
        "bigmodel.cn",       # 智谱
        "zhipuai.cn",
        "aliyuncs.com",      # 阿里通义
        "deepseek.com",
        "moonshot.cn",
        "volces.com",        # 火山方舟
        "tencentcloudapi.com",
    )
    return any(d in url for d in domestic)


def parse_json_defensive(raw: str):
    """从 LLM 输出里抠出 JSON。支持带 ```json fence、前后有解释文字的情况。"""
    if not raw:
        return None
    s = raw.strip()
    # 去 markdown code fence
    s = re.sub(r"^```(?:json)?\s*", "", s)
    s = re.sub(r"\s*```$", "", s)
    s = s.strip()
    # 先尝试整体解析
    try:
        return json.loads(s)
    except Exception:
        pass
    # 退化：截取第一个 { ... } 或 [ ... ]
    for opener, closer in [("[", "]"), ("{", "}")]:
        start = s.find(opener)
        end = s.rfind(closer)
        if start != -1 and end != -1 and end > start:
            try:
                return json.loads(s[start : end + 1])
            except Exception:
                continue
    log.error("LLM JSON 解析失败，原始输出前 500 字: %s", raw[:500])
    return None
