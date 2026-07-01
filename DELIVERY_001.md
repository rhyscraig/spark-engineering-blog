# Delivery 001 — Product 1, first production run

**Delivery question:** *Can Spark take one product idea from nothing to a published,
evidence-backed artifact?*  → **Yes.**

**Reality interaction:** EXTERNAL (a real public site on the internet).
**Date:** 2026-07-01

## The chain (every stage ran)

| # | Stage | Through the factory? | Evidence |
|---|-------|----------------------|----------|
| 1 | Plan the work | Manual brief (no plan CLI) | `content/BRIEF.md` |
| 2 | Create repository | **Spark Execution Engine** (`GhExecutor`, as E004) | `rhyscraig/spark-engineering-blog` created |
| 3 | Generate article | **Spark inference** (local Ollama/mistral, zero-token) | `content/posts/moon-robot-principle.md`, 737→662 tok, ~39s |
| 4 | Quality check | product gate | `tools/quality_check.py` → PASS (519 words) |
| 5 | Build site | product build (adapted static-html pattern) | `docs/` |
| 6 | Publish | **Spark Execution Engine** (`gh`) + Pages `main:/docs` | Pages build = **built** |
| 7 | Capture evidence | `gh repo view` + this doc | HTTP **200** on `/` and `/moon-robot-principle.html` |
| 8 | Capability Debt | recorded in Spark | `docs/CAPABILITY_DEBT.md` (5 entries) |

**Primary evidence:** https://rhyscraig.github.io/spark-engineering-blog/ (live, HTTP 200).
**Secondary evidence:** repo public + pushed; Pages HTTPS-enforced; generation delegated to
local Ollama (0 API tokens); repo-create + publish delegated to `gh` (Spark held no creds).

## Two-question scorecard (Constitution 19)

- **Did the product become better?** **Yes** — it now exists and has its first published
  article.
- **Did the organisation become more capable?** **Yes, on learning, not on new code** —
  no capability was added to Spark. The gain is *calibration*: the whole chain is now
  proven to run end-to-end, and we know precisely where it's strong vs weak (below). That
  is the product doing its real job — calibrating the organisation. Quadrant: **P✓ / S✓(learning)**.

## What the run taught us (calibration)

- **Strong:** repository creation (Spark Execution Engine, second clean use after E004);
  deployment/publish (Pages reliable, first try); local generation *works* and is free.
- **Weak / friction:** no callable way to drive planning or generation (had to hand-write a
  brief and a product-side inference driver); model selection is manual (only one backend);
  local-model prose is coherent but generic and made a factual slip (miscounted its own
  list) that the quality gate didn't catch.

None of these were fixed. They are recorded as evidence. The Board decides if/when any
becomes a Spark investment — and only after a *second* product hits the same wall.
