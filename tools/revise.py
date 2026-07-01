"""Revision step — the factory regenerates from Reviewer guidance (no human rewrite).

Verdict 'Revise' sends the article back to generation with the Reviewer's actionable
guidance. The Reviewer never edits prose; the Engineering Engine does. One cycle.

    PYTHONPATH=<spark> <spark>/.venv/bin/python tools/revise.py <slug> "<title>" "<summary>"
"""

from __future__ import annotations

import pathlib
import sys

from spark.adapters.runtime import HttpxClient, SystemClock
from spark.domain.models import InferenceRequest
from spark.inference import OllamaBackend

ENDPOINT = "http://localhost:11434"
MODEL = "mistral:latest"
ROOT = pathlib.Path(__file__).resolve().parent.parent


def main(argv: list[str]) -> int:
    slug = argv[1] if len(argv) > 1 else "recover-before-you-build"
    title = argv[2] if len(argv) > 2 else "Recover Before You Build"
    summary = argv[3] if len(argv) > 3 else ""
    brief = (ROOT / "content" / "briefs" / "002.md").read_text()
    guidance = (ROOT / "content" / "reviews" / f"{slug}.revision-guidance.md").read_text()
    backend = OllamaBackend(ENDPOINT, MODEL, HttpxClient(), SystemClock())

    prompt = (
        "Rewrite this blog article to FULLY satisfy the revision guidance. Return ONLY the "
        "article body in Markdown (no front-matter). Do not describe any review/approval "
        "process. Include at least two concrete examples and explicitly answer the judgement "
        f"questions. 700-900 words.\n\nBRIEF:\n{brief}\n\nREVISION GUIDANCE:\n{guidance}"
    )
    req = InferenceRequest(
        prompt=prompt, purpose="article_revise", system="You are a principal software engineer "
        "writing a candid, example-rich blog post. Concrete examples, reasoned claims, no "
        "fabricated statistics, and never discuss the reviewing process itself.",
        max_tokens=2000, deadline_s=240.0,
    )
    body = backend.complete(req).text.strip()
    print(f"  [article_revise] {len(body.split())} words")

    out = ROOT / "content" / "posts" / f"{slug}.md"
    fm = (f'---\ntitle: "{title}"\ndate: 2026-07-01\nsummary: "{summary}"\n'
          "generated_by: spark-inference (ollama/mistral, local, zero-token) · revised\n---\n\n")
    out.write_text(fm + body + "\n")
    print(f"Wrote revised {out.relative_to(ROOT)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
