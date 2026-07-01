"""Reviewer role — an organisational role, driven THROUGH Spark inference.

The Reviewer does NOT rewrite. It judges publishability and lists categorised findings,
then returns a verdict: Publish / Revise / Reject. This is the 'approving' half of an
engineering organisation, distinct from 'building'.

Findings format (one per line):  CATEGORY | SEVERITY | specific finding
  CATEGORY  in {Accuracy, Communication, Evidence, Readability, Editorial}
  SEVERITY  in {blocker, major, minor}
Final line: VERDICT: Publish|Revise|Reject — <one sentence>

    PYTHONPATH=<spark> <spark>/.venv/bin/python tools/review.py <slug>
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

SYSTEM = (
    "You are a Reviewer in an engineering organisation. Your job is to APPROVE or not — "
    "you never rewrite the article. Be specific and skeptical: flag inaccurate or "
    "unsupported claims, incomplete reasoning, and unnecessary complexity."
)


THRESHOLD = (
    "\n\nApply this PUBLICATION THRESHOLD when deciding severity and verdict: a finding is "
    "'blocker' or 'major' ONLY if it would genuinely mislead the reader or seriously harm the "
    "article's correctness. Stylistic, structural, or polish issues are 'minor'. Set VERDICT = "
    "Revise ONLY if at least one blocker or major finding exists; otherwise VERDICT = Publish and "
    "list the minors as non-blocking notes."
)


def main(argv: list[str]) -> int:
    args = [a for a in argv[1:] if not a.startswith("--")]
    threshold = "--threshold" in argv
    slug = args[0] if args else "recover-before-you-build"
    article = (ROOT / "content" / "posts" / f"{slug}.md").read_text()
    backend = OllamaBackend(ENDPOINT, MODEL, HttpxClient(), SystemClock())

    prompt = (
        "Review the article below. Output ONE line per issue in exactly this format:\n"
        "CATEGORY | SEVERITY | specific finding\n"
        "CATEGORY must be one of: Accuracy, Communication, Evidence, Readability, Editorial.\n"
        "SEVERITY must be one of: blocker, major, minor.\n"
        "Do NOT rewrite the article. After the findings, output a final line:\n"
        "VERDICT: Publish OR Revise OR Reject — one sentence why."
        + (THRESHOLD if threshold else "")
        + f"\n\nARTICLE:\n{article}"
    )
    req = InferenceRequest(prompt=prompt, purpose="reviewer", system=SYSTEM, max_tokens=1200, deadline_s=180.0)
    out = backend.complete(req).text.strip()

    suffix = ".selfreview.threshold.md" if threshold else ".selfreview.md"
    dest = ROOT / "content" / "reviews" / f"{slug}{suffix}"
    dest.parent.mkdir(parents=True, exist_ok=True)
    mode = "threshold" if threshold else "baseline"
    dest.write_text(f"# Spark self-review ({mode}) — {slug}\n\n{out}\n")
    # Neutral confirmation only — do NOT echo findings (keeps the human review blind).
    print(f"Spark self-review [{mode}] written to {dest.relative_to(ROOT)} ({len(out.splitlines())} lines).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
