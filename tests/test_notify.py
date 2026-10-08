import unittest
from unittest.mock import patch

import notify


class EmptyEmailTests(unittest.TestCase):
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
