#!/usr/bin/env python3
"""Validate a model output against the deterministic humanisation fixtures."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


WORD_RE = re.compile(r"[\wÀ-ÖØ-öø-ÿ]+(?:['’\-][\wÀ-ÖØ-öø-ÿ]+)*", re.UNICODE)


def words(text: str) -> int:
    return len(WORD_RE.findall(text))


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: validate_outputs.py FIXTURES.json OUTPUT.json")
        return 2

    fixtures = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    payload = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
    results = {item["id"]: item["output"] for item in payload["results"]}
    failures: list[str] = []

    for case in fixtures:
        case_id = case["id"]
        output = results.get(case_id)
        if output is None:
            failures.append(f"{case_id}: missing output")
            continue

        lowered = output.casefold()
        for expected in case.get("required_exact", []):
            if expected.casefold() not in lowered:
                failures.append(f"{case_id}: required text missing: {expected}")
        for token in case.get("tokens", []):
            if token not in output:
                failures.append(f"{case_id}: token changed or missing: {token}")
        for forbidden in case.get("forbidden_exact", []):
            if forbidden.casefold() in lowered:
                failures.append(f"{case_id}: forbidden text present: {forbidden}")
        for block in case.get("unchanged_blocks", []):
            if block not in output:
                failures.append(f"{case_id}: stable block was modified")

        if output.count("—") > case.get("max_em_dash", 10**9):
            failures.append(f"{case_id}: em dash gate failed")
        if case.get("no_new_bold") and output.count("**") > case["input"].count("**"):
            failures.append(f"{case_id}: new Markdown bold added")
        if "max_expansion_pct" in case:
            source_words = words(case["input"])
            delta = ((words(output) - source_words) / source_words) * 100 if source_words else 0
            if delta > case["max_expansion_pct"]:
                failures.append(f"{case_id}: expansion {delta:.1f}% exceeds {case['max_expansion_pct']}%")

    unexpected = sorted(set(results) - {case["id"] for case in fixtures})
    if unexpected:
        failures.append(f"unexpected result ids: {', '.join(unexpected)}")

    if failures:
        print("FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"PASS: {len(fixtures)} cases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
