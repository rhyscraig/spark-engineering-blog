"""Quality gate for generated articles — the 'run tests' stage of the production run.

Deterministic checks a human would otherwise eyeball. Exit non-zero fails the delivery.
"""

from __future__ import annotations

import pathlib
import sys

POSTS = pathlib.Path(__file__).resolve().parent.parent / "content" / "posts"
MIN_WORDS = 300
REQUIRED_FM = ("title:", "date:", "summary:")
BANNED = ("lorem ipsum", "todo", "as an ai language model", "i cannot")


def check(md: pathlib.Path) -> list[str]:
    text = md.read_text()
    errs: list[str] = []
    if not text.startswith("---"):
        errs.append("missing front-matter block")
    head, _, body = text.partition("\n---\n") if text.startswith("---") else ("", "", text)
    for key in REQUIRED_FM:
        if key not in head:
            errs.append(f"front-matter missing '{key}'")
    words = len(body.split())
    if words < MIN_WORDS:
        errs.append(f"too short: {words} < {MIN_WORDS} words")
    if not any(line.lstrip().startswith("#") for line in body.splitlines()):
        errs.append("no Markdown heading in body")
    low = body.lower()
    for b in BANNED:
        if b in low:
            errs.append(f"banned phrase present: {b!r}")
    return errs


def main() -> int:
    posts = sorted(POSTS.glob("*.md"))
    if not posts:
        print("FAIL: no posts to check")
        return 1
    failed = False
    for p in posts:
        errs = check(p)
        if errs:
            failed = True
            print(f"FAIL {p.name}:")
            for e in errs:
                print(f"  - {e}")
        else:
            print(f"PASS {p.name} ({len(p.read_text().split())} words)")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
