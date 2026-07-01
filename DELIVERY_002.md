# Delivery 002 — Product 1, the review experiment

**Delivery question:** *Does the organisation behave well when quality is uncertain?* —
tested by introducing a **Reviewer** role and a genuine review + approval process.
→ **Yes, and it exposed its first organisational gap.**

**Reality interaction:** EXTERNAL (published). **Date:** 2026-07-01
**Article:** "Recover Before You Build" (a topic with genuine judgement calls, chosen so the
Reviewer had real work).

## New this delivery

- **Reviewer role** (organisational, not an engine): `tools/review.py` — verdict only
  (Publish / Revise / Reject), **never rewrites**. Driven through Spark inference.
- **Blind review**: Spark self-review produced *before* the independent human review; neither
  saw the other until both were fixed. Metrics in `content/reviews/*.comparison.md`.
- **Revise = factory regenerates**, not human-rewrites (`tools/revise.py` from a
  Reviewer→Builder guidance handoff). One cycle: 404 → 616 words.
- **Findings categorised**: Accuracy / Communication / Evidence / Readability / Editorial.

## Result

- Round 1 verdict: **Revise** (agreed by both reviewers; agreed headline gap = **Evidence**).
- Revision resolved every blocker/major.
- Round 2: only *minor* findings — but **Spark said Revise, human said Publish**.
- **Final decision: PUBLISH** (rule: publish when no blocker/major remains; minors logged).

## Blind-review maturity metrics (round 1)

- **Spark found itself:** the Evidence gap (major, exact match + severity), weak structure,
  and *sensed* the off-topic drift.
- **Human-only:** the *cause* of the drift (brief-leak), incomplete reasoning, empty metadata,
  underlength vs brief.
- **False positives:** one **misdiagnosis** (Spark blamed the title; the body was at fault) —
  **zero hallucinated findings.**
- **Read:** the reviewer is *directionally right but shallow*; reliable on "is it publishable?"
  (verdict + headline gap), unreliable on *why* and blind to mechanical/brief-compliance checks.

## The organisational finding (the point of the experiment)

The reviewer has **no publication-threshold policy** — it escalated *minor* issues to a
blocking Revise, disagreeing with the human's Publish. That is an **organisational** capability
gap (a severity→verdict policy), not a technical one. It is the first real Capability Debt this
product produced, and it validates the thesis: *Spark's hard, defensible value is accumulated
engineering judgement and repeatable delivery practices — not model orchestration.*

## Two-question scorecard (Constitution 19)

- **Product better?** Yes — a second, reviewed, published article.
- **Org more capable?** Yes, materially — the organisation now has a *building vs approving*
  separation, a blind-review measurement, and its first **organisational** debt to watch for
  recurrence (→ Policy). Quadrant: **P✓ / S✓.**
