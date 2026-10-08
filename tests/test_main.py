import unittest
from unittest.mock import patch

import main


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


if __name__ == "__main__":
    unittest.main()
