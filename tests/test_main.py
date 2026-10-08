import unittest
from unittest.mock import patch

import main
import rank


class DryRunTests(unittest.TestCase):
    def test_empty_fetch_has_no_side_effects(self):
        for errors in ([], ["fetch failed"]):
            for flags in (["--dry-run"], ["--dry-run", "--no-notify"]):
                with (
                    self.subTest(errors=errors, flags=flags),
                    patch("sys.argv", ["main.py", *flags]),
                    patch("main.fetch.fetch_all", return_value=([], errors)),
                    patch("main.notify.send_empty_notice") as notice,
                    patch("main.save_state") as save,
                    patch("main.LLMClient") as llm,
                ):
                    self.assertEqual(main.main(), 0)
                    notice.assert_not_called()
                    save.assert_not_called()
                    llm.assert_not_called()

    def test_all_llm_failures_do_not_send_empty_email_or_mark_seen(self):
        paper = {"id": "test:1", "source": "pubmed", "_kw_score": 1.0}
        ranked = [{**paper, "_rank": rank._placeholder_rank(paper)}]
        with (
            patch("sys.argv", ["main.py"]),
            patch("main.fetch.fetch_all", return_value=([paper], [])),
            patch("main.load_state", return_value={"seen": {}, "runs": []}),
            patch("main.rank.keyword_prefilter", return_value=[paper]),
            patch("main.LLMClient"),
            patch("main.rank.llm_rank", return_value=ranked),
            patch("main.notify.send_empty_notice") as notice,
            patch("main.notify.send_email") as email,
            patch("main.save_state") as save,
        ):
            self.assertEqual(main.main(), 1)
            notice.assert_not_called()
            email.assert_not_called()
            save.assert_not_called()

    def test_test_notify_sends_only_email_and_reports_failure(self):
        for papers in ([], [{"id": "test:1"}]):
            for sent in (True, False):
                with (
                    self.subTest(papers=papers, sent=sent),
                    patch("sys.argv", ["main.py", "--test-notify"]),
                    patch("main.notify.load_latest_report", return_value=(papers, "report", "2026-10-04")),
                    patch("main.notify.send_email", return_value=sent) as email,
                ):
                    self.assertEqual(main.main(), 0 if sent else 1)
                    email.assert_called_once_with("report", "2026-10-04", len(papers))


if __name__ == "__main__":
    unittest.main()
