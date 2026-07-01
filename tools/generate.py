"""Article generation — driven THROUGH Spark's inference capability (local Ollama).

Product-side driver (Constitution 15: product code lives in the product repo). It imports
Spark's Execution/Inference capability rather than calling `ollama` directly, so that this
production run genuinely exercises the factory. Produce -> review, two passes.

Run with Spark's venv + PYTHONPATH:
    PYTHONPATH=/Users/craighoad/Repos/ai-claude-mcp-spark \
      /Users/craighoad/Repos/ai-claude-mcp-spark/.venv/bin/python tools/generate.py
"""

from __future__ import annotations

import pathlib
import sys

from spark.adapters.runtime import HttpxClient, SystemClock
from spark.domain.models import InferenceRequest
from spark.inference import OllamaBackend

ENDPOINT = "http://localhost:11434"
MODEL = "mistral:latest"  # local; zero-token. (Model choice is manual — see Capability Debt.)

BRIEF = pathlib.Path(__file__).resolve().parent.parent / "content" / "BRIEF.md"
OUT = pathlib.Path(__file__).resolve().parent.parent / "content" / "posts" / "moon-robot-principle.md"


def _complete(backend: OllamaBackend, prompt: str, purpose: str, system: str) -> str:
    req = InferenceRequest(
        prompt=prompt, purpose=purpose, system=system, max_tokens=1600, deadline_s=180.0
    )
    c = backend.complete(req)
    print(f"  [{purpose}] {c.tokens_out} tokens out via {c.backend} in {c.latency_s:.1f}s")
    return c.text.strip()


def main() -> int:
    brief = BRIEF.read_text()
    backend = OllamaBackend(ENDPOINT, MODEL, HttpxClient(), SystemClock())

    print("Generate (pass 1: draft) ...")
    draft = _complete(
        backend,
        prompt=(
            "Write a ~800-word blog article in first-person engineering voice based on this "
            f"brief. Return ONLY the article body in Markdown (no front-matter).\n\n{brief}"
        ),
        purpose="article_draft",
        system="You are a principal software engineer writing a candid, practical blog post. "
        "Concrete, no filler, no fabricated statistics.",
    )

    print("Review (pass 2: tighten) ...")
    final = _complete(
        backend,
        prompt=(
            "Revise this draft: tighten prose, remove filler and repetition, ensure a clear "
            "arc (hook -> principle -> Spark example -> takeaway), keep ~800 words. Return "
            f"ONLY the revised Markdown body.\n\n---\n{draft}"
        ),
        purpose="article_review",
        system="You are a sharp editor. Improve clarity and flow without inventing facts.",
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    front_matter = (
        "---\n"
        'title: "The Moon Robot Principle: Build the Machine That Builds the Machine"\n'
        "date: 2026-07-01\n"
        'summary: "Why sequence beats destination when building complex systems — and how '
        'Spark was built as a factory, not a product."\n'
        "generated_by: spark-inference (ollama/mistral, local, zero-token)\n"
        "---\n\n"
    )
    OUT.write_text(front_matter + final + "\n")
    print(f"\nWrote {OUT} ({len(final.split())} words).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
