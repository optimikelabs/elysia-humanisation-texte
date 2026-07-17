#!/usr/bin/env python3
"""Run dependency-free structural checks for the public skill package."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"


def main() -> int:
    failures: list[str] = []
    text = SKILL.read_text(encoding="utf-8")

    if len(text.splitlines()) > 100:
        failures.append("SKILL.md exceeds 100 lines")
    for heading in ("## Quand l'utiliser", "## Navigation", "## Routage rapide", "## Workflow"):
        if heading not in text:
            failures.append(f"missing heading: {heading}")
    for token in ("module_route", "sortie_finale_autorisee", "Lire seulement `SKILL.md`"):
        if token not in text:
            failures.append(f"missing runtime contract token: {token}")

    for relative in re.findall(r"\[[^]]+\]\(([^)]+\.md)\)", text):
        if not (ROOT / relative).is_file():
            failures.append(f"broken Markdown reference: {relative}")

    source_map = (ROOT / "references" / "source-map.md").read_text(encoding="utf-8")
    if "https://babeleur.com/detecteur-ecriture-ia" in source_map:
        failures.append("obsolete Babeleur URL remains")

    fixtures = json.loads((ROOT / "tests" / "fixtures.json").read_text(encoding="utf-8"))
    ids = [case["id"] for case in fixtures]
    if len(ids) != len(set(ids)):
        failures.append("duplicate fixture ids")

    if failures:
        print("FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print(f"PASS: package structure, {len(fixtures)} fixtures")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
