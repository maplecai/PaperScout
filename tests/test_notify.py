import unittest
from tempfile import TemporaryDirectory
from unittest.mock import patch

import notify


class ReportLayoutTests(unittest.TestCase):
    def test_article_first_layout_and_safe_html(self):
        paper = {"title": "A <B> study", "source": "biorxiv", "journal": "bioRxiv",
                 "url": "https://example.org/paper?a=1&b=2", "authors": ["A"],
                 "abstract": "Evidence <script>alert(1)</script> https://github.com/lab/model.",
                 "_rank": {"relevance_score": 8, "why_relevant": "推荐理由"},
                 "_summary": {"core_method": "方法", "task_scope": "RNA → ATAC",
                              "inspiration": "可以尝试", "applicability": "尚未验证序列任务"}}
        md = notify.build_report_md([paper], "2026-11-04", stats="抓取 10 篇")
        self.assertLess(md.index("为什么值得看"), md.index("作者："))
        self.assertLess(md.index("英文摘要"), md.index("检索统计"))
        self.assertNotIn("<details>", md)
        rendered = notify.render_report_html(md)
        self.assertIn('<strong>为什么值得看</strong>', rendered)
        self.assertIn('href="https://example.org/paper?a=1&amp;b=2"', rendered)
        self.assertIn('href="https://github.com/lab/model"', rendered)
        self.assertNotIn('<script>', rendered)
        self.assertEqual(rendered.count('<ul '), rendered.count('</ul>'))

    def test_report_json_retains_abstract_for_reformatting(self):
        with TemporaryDirectory() as directory:
            notify.write_report_json([{"abstract": "original abstract", "_kw_score": 0.4}], "2026-11-04", directory)
            papers, _, _ = notify.load_report("2026-11-04", directory)
            self.assertEqual(papers, [{"abstract": "original abstract"}])


class EmptyEmailTests(unittest.TestCase):
    def test_load_report_selects_requested_date_instead_of_latest(self):
        with TemporaryDirectory() as directory:
            for date in ("2026-10-04", "2026-10-08"):
                notify.write_report(date, date, directory)
                notify.write_report_json([], date, directory)
            self.assertEqual(notify.load_report("2026-10-04", directory), ([], "2026-10-04", "2026-10-04"))
            self.assertEqual(notify.load_report(reports_dir=directory), ([], "2026-10-08", "2026-10-08"))
            self.assertIsNone(notify.load_report("2026-10-07", directory))

    def test_empty_report_is_archived_and_emailed(self):
        with (
            patch("notify.write_report") as markdown,
            patch("notify.write_report_json") as structured,
            patch("notify.send_email", return_value=True) as email,
        ):
            self.assertTrue(notify.send_empty_notice("2026-10-04", "低于筛选阈值"))
            md, date = markdown.call_args.args
            self.assertIn("低于筛选阈值", md)
            structured.assert_called_once_with([], date)
            email.assert_called_once_with(md, date, 0)

    def test_no_notify_only_archives(self):
        with (
            patch("notify.write_report") as markdown,
            patch("notify.write_report_json") as structured,
            patch("notify.send_email") as email,
        ):
            self.assertFalse(notify.send_empty_notice("2026-10-04", "无推荐", no_push=True))
            markdown.assert_called_once()
            structured.assert_called_once_with([], "2026-10-04")
            email.assert_not_called()
