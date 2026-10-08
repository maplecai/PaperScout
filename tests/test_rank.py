import unittest

import rank


class SelectionTests(unittest.TestCase):
    def test_score_floor_applies_to_every_priority(self):
        papers = [
            {"_rank": {"priority": priority, "relevance_score": score, "worth_reading": True}}
            for priority in ("P0", "P1", "P2", "EXCLUDE")
            for score in (5, 6, 9)
        ]
        selected = rank.select_top(papers, {"min_score": 6, "max_papers": 100})
        self.assertEqual(len(selected), 6)
        self.assertTrue(all(p["_rank"]["relevance_score"] >= 6 for p in selected))
        self.assertTrue(all(p["_rank"]["priority"] != "EXCLUDE" for p in selected))

    def test_priority_allowlist_and_count_limit(self):
        papers = [
            {"_rank": {"priority": priority, "relevance_score": 9, "worth_reading": True}}
            for priority in ("P2", "P1", "P0", "P1")
        ]
        selected = rank.select_top(papers, {"min_score": 6, "accept_priorities": ["P0", "P1"], "max_papers": 2})
        self.assertEqual(selected, papers[1:3])
