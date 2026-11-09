import unittest
from unittest.mock import Mock, patch

import fetch
import notify


class ArxivAffiliationTests(unittest.TestCase):
    def test_optional_affiliations_stay_paired_with_author(self):
        for affiliations in ("<arxiv:affiliation>Institute A</arxiv:affiliation><arxiv:affiliation>Institute B</arxiv:affiliation>", ""):
            with self.subTest(affiliations=affiliations):
                xml = f'''<feed xmlns="http://www.w3.org/2005/Atom" xmlns:arxiv="http://arxiv.org/schemas/atom">
                  <entry><id>https://arxiv.org/abs/2611.00001v1</id>
                  <title>Test paper</title><summary>Abstract</summary><published>2026-11-08T00:00:00Z</published>
                  <author><name>Alice</name>{affiliations}</author>
                  <author><name>Bob</name></author></entry></feed>'''
                with patch.object(fetch, "_get_backoff", return_value=Mock(text=xml)):
                    papers = fetch.fetch_arxiv({}, 3, end_date="2026-11-09")
                self.assertEqual(len(papers), 1)
                paper = papers[0]
                self.assertEqual(paper["authors"], ["Alice", "Bob"])
                md = notify.build_report_md(papers, "2026-11-09")
                if affiliations:
                    self.assertEqual(paper["corr_author"], "Alice")
                    self.assertEqual(paper["corr_affiliation"], "Institute A; Institute B")
                    self.assertIn("末位带机构信息的作者：Alice", md)
                    self.assertNotIn("通讯作者", md)
                else:
                    self.assertEqual(paper["corr_author"], "")
                    self.assertEqual(paper["corr_affiliation"], "")
                    self.assertIn("机构：当前 API 未提供机构信息", md)
