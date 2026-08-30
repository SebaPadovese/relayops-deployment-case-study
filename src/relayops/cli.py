import json
import sys
from pathlib import Path

from .routing import route_case


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python -m relayops.cli PATH_TO_UAT_JSON")
        return 2

    cases = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    passed = 0
    for case in cases:
        actual = route_case(case)
        ok = all(
            getattr(actual, field) == case[f"expected_{field}"]
            for field in ("priority", "owner", "response_target", "guardrail")
        ) and actual.human_takeover == case["expected_human_takeover"]
        passed += int(ok)
        print(f"{case['id']} | {case['language']} | {actual.priority} | {'PASS' if ok else 'FAIL'}")

    print(f"\nResult: {passed}/{len(cases)} passed")
    return 0 if passed == len(cases) else 1


if __name__ == "__main__":
    raise SystemExit(main())

