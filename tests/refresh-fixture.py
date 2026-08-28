#!/usr/bin/env python3
"""Refresh tests/fixture/ from a real generated cohort site.

The fixture is what `python3 -m dsl_course.site sync` actually writes, not a hand-written
approximation - re-run this after changing what the toolkit generates. Needs `gh`
authenticated with read access to the source site.

    python3 tests/refresh-fixture.py [owner/repo]

`tests/fixture/_config.yml` is NOT touched: it is this repo's own fixture config, not
generated output.
"""

from __future__ import annotations

import base64
import json
import subprocess
import sys
from pathlib import Path

DEFAULT_SITE = "hertie-dsl-demo-f2026/hertie-dsl-demo-f2026.github.io"
FIXTURE = Path(__file__).resolve().parent / "fixture"

# The generated site pages - each one exercises a different layout.
PAGES = (
    "index.md",
    "schedule.md",
    "lectures.md",
    "labs.md",
    "assignments.md",
    "project.md",
    "readings.md",
    "materials.md",
)
COLLECTIONS = ("_lectures/", "_assignments/", "_events/")


def gh(site: str, path: str) -> dict | list:
    out = subprocess.run(
        ["gh", "api", f"repos/{site}/{path}"],
        capture_output=True,
        text=True,
        check=True,
    )
    return json.loads(out.stdout)


def read(site: str, path: str) -> str:
    blob = gh(site, f"contents/{path}")
    return base64.b64decode(blob["content"]).decode()


def main() -> int:
    site = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_SITE
    blobs = [
        e["path"]
        for e in gh(site, "git/trees/main?recursive=1")["tree"]
        if e["type"] == "blob"
    ]

    # Clear what we regenerate, so a file the toolkit stopped writing does not linger.
    for stale in (
        list(FIXTURE.glob("_data/*"))
        + [p for c in COLLECTIONS for p in FIXTURE.glob(f"{c}*")]
        + list(FIXTURE.glob("pages/*"))
    ):
        stale.unlink()

    written = 0
    for path in blobs:
        if path.startswith("_data/") or (
            path.startswith(COLLECTIONS) and path.endswith(".md")
        ):
            dest = FIXTURE / path
        elif path in PAGES:
            dest = FIXTURE / "pages" / path
        else:
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(read(site, path), encoding="utf-8")
        written += 1
        print(f"  {dest.relative_to(FIXTURE)}")

    print(f"\n{written} file(s) from {site}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
