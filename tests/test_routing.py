import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from relayops.routing import route_case


class RoutingAcceptanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cases = json.loads((ROOT / "data" / "uat_cases.json").read_text(encoding="utf-8"))

    def test_all_structured_uat_cases(self):
        for case in self.cases:
            with self.subTest(case=case["id"], language=case["language"]):
                actual = route_case(case)
                self.assertEqual(case["expected_priority"], actual.priority)
                self.assertEqual(case["expected_owner"], actual.owner)
                self.assertEqual(case["expected_response_target"], actual.response_target)
                self.assertEqual(case["expected_guardrail"], actual.guardrail)
                self.assertEqual(case["expected_human_takeover"], actual.human_takeover)

    def test_incomplete_case_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Missing required fields"):
            route_case({"id": "NEG-01", "category": "life_safety"})

    def test_unknown_category_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Unsupported category"):
            route_case({"id": "NEG-02", "language": "EN", "category": "other", "description": "Unknown"})


if __name__ == "__main__":
    unittest.main()

