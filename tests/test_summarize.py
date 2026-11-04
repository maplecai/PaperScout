import json
import unittest
from unittest.mock import Mock

import summarize


class SummaryTests(unittest.TestCase):
    def test_full_abstract_and_evidence_boundaries(self):
        fields = ("relevance_type", "task_scope", "core_method", "main_finding",
                  "inspiration", "applicability", "reading_question")
        response = {key: key for key in fields}
        llm = Mock()
        llm.chat_json.return_value = response
        paper = {"title": "test", "abstract": "a" * 2100 + "important evidence"}
        summarize.summarize_papers([paper], llm)
        self.assertEqual(paper["_summary"], response)
        payload = json.loads(llm.chat_json.call_args.args[1])
        self.assertEqual(payload["abstract"], paper["abstract"])
