"""Article generation — driven THROUGH Spark's inference capability (local Ollama).

Product-side driver (Constitution 15). Imports Spark's inference rather than calling
`ollama` directly, so the run exercises the factory. Produce -> tighten, two passes.

    PYTHONPATH=<spark> <spark>/.venv/bin/python tools/generate.py <brief> <slug> "<title>"
"""

from __future__ import annotations

import pathlib
import sys

from spark.adapters.runtime import HttpxClient, SystemClock
from spark.domain.models import InferenceRequest
from spark.inference import OllamaBackend

ENDPOINT = "http://localhost:11434"
MODEL = "mistral:latest"  # local; zero-token. (Model choice is manual — see Capability Debt.)
ROOT = pathlib.Path(__file__).resolve().parent.parent

DEFAULTS = ("content/BRIEF.md", "moon-robot-principle",
            "The Moon Robot Principle: Build the Machine That Builds the Machine")


def _complete(backend: OllamaBackend, prompt: str, purpose: str, system: str) -> str:
    req = InferenceRequest(prompt=prompt, purpose=purpose, system=system, max_tokens=1600, deadline_s=180.0)
    c = backend.complete(req)
    print(f"  [{purpose}] {c.tokens_out} tokens out via {c.backend} in {c.latency_s:.1f}s")
    return c.text.strip()


def main(argv: list[str]) -> int:
    brief_rel, slug, title = (argv[1:4] + list(DEFAULTS[len(argv) - 1:]))[:3] if len(argv) > 1 else DEFAULTS
    brief = (ROOT / brief_rel).read_text()
    out = ROOT / "content" / "posts" / f"{slug}.md"
    backend = OllamaBackend(ENDPOINT, MODEL, HttpxClient(), SystemClock())

    print("Generate (pass 1: draft) ...")
    draft = _complete(
        backend,
        prompt=("Write a ~800-word blog article in first-person engineering voice based on this "
                f"brief. Return ONLY the article body in Markdown (no front-matter).\n\n{brief}"),
        purpose="article_draft",
        system="You are a principal software engineer writing a candid, practical blog post. "
        "Concrete, no filler, no fabricated statistics.",
    )
    print("Tighten (pass 2) ...")
    final = _complete(
        backend,
        prompt=("Revise this draft: tighten prose, remove filler and repetition, ensure a clear "
                "arc, keep ~800 words. Return ONLY the revised Markdown body.\n\n---\n" + draft),
        purpose="article_tighten",
        system="You are a sharp editor. Improve clarity and flow without inventing facts.",
    )

    out.parent.mkdir(parents=True, exist_ok=True)
    fm = (f"---\ntitle: \"{title}\"\ndate: 2026-07-01\n"
          'summary: ""\ngenerated_by: spark-inference (ollama/mistral, local, zero-token)\n---\n\n')
    out.write_text(fm + final + "\n")
    print(f"\nWrote {out} ({len(final.split())} words).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
