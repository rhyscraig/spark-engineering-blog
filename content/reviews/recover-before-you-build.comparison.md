# Blind-review comparison — recover-before-you-build

Spark self-review and the independent human review were produced **blind** of each other.
Verdicts were then compared. This measures *decision quality*, not capability.

## Verdict agreement

- **Spark verdict:** Revise · **Human verdict:** Revise → **AGREE.**
- Both independently identified **Evidence (missing examples)** as a major gap — the single
  most important substantive finding. Agreement on the headline problem *and* the verdict.

## The three maturity metrics

**1. Issues Spark found itself (real, matched by human):**
- Evidence — no concrete examples/case studies (Spark "Major" ≈ human H2 "major"). **Strong match, same severity.**
- Structure/readability could be clearer (Spark "Minor" ≈ human H4). Match.
- Off-topic content detected (Spark "Blocker: title doesn't match content") — Spark *sensed*
  the article is off-topic, matching human H1. **Detected, but misdiagnosed** (see false positives).

**2. Issues only the human found:**
- H1 *cause*: the body drifted because the **brief's review-dimension instructions leaked into
  the article** — Spark saw the symptom, not the cause.
- H3: the genuine judgement calls are **name-dropped but never answered** (reasoning incomplete).
- H6: front-matter `summary` is **empty** (Spark never inspected metadata).
- H7: **404 words vs the 700–900 brief target** (Spark never checked length against the brief).
- H5: filler/generic voice.

**3. False positives / misdiagnoses (Spark):**
- Spark's blocker remedy — "**revise the title**" — is wrong. The title *"Recover Before You
  Build"* is accurate and on-topic; the **body** drifted. Spark found a real problem but
  prescribed a fix that would damage a correct title. One misdiagnosis; **zero invented
  (hallucinated) issues.**

## What this says about organisational maturity

Spark's reviewer is **directionally right but shallow**: it agrees on *"is this publishable?"*
(verdict + headline gap) but is unreliable on **why** (misdiagnosed the off-topic cause) and
blind to **mechanical / brief-compliance checks** (length, metadata) and **reasoning
completeness**. Encouragingly, it produced no hallucinated findings — its error was a
misdiagnosis, not a fabrication.

## The policy seed (watch across articles)

**Evidence** was the agreed major gap here. If "missing evidence / no concrete example"
recurs in Article 003, it stops being a content note and becomes a **content standard**
("every trade-off claim needs a concrete example") → Engineering Memory → eventually Policy —
promoted by *repeated products*, not designed. This is the user's prediction (Capability Debt
is organisational, not technical) beginning to show: the substantive findings here were
Evidence, Readability, Editorial — **not one was a technical/plumbing gap.**

## Revision round + final decision

The verdict was **Revise**, so the *factory regenerated* from a Reviewer→Builder guidance
handoff (`*.revision-guidance.md`) — the human did **not** edit prose. One cycle: 404 → 616
words. The revision resolved every blocker/major:

| Round-1 finding | Resolved? |
|---|---|
| H1 brief-leak / off-topic | ✅ fully — no review-process text; on-topic throughout |
| H2 no evidence/examples | ✅ two concrete examples (reconnected API, 80%-built feature) + false-economy cases |
| H3 judgement calls unanswered | ✅ explicit sections answering both questions |
| H6 empty summary · H7 underlength | ✅ summary set; 616 words |

**Re-review disagreement (the maturity signal):** on the revised article both reviewers found
**only minor** issues, but **Spark verdict = Revise, human verdict = Publish.** Spark escalated
minor polish to a blocking verdict; it has **no publication threshold** (no severity→verdict
policy). Zero blocker/major findings remained by either reviewer.

**Decision: PUBLISH.** Applying the sane organisational rule — *publish when no blocker/major
findings remain; minors are logged, not blocking.* Spark's minors (unspecific "modern tools";
list-heavy section; "building a new solution" repetition) are recorded as future polish.

**The Policy seed, surfaced immediately:** the reviewer needs a **publication-threshold
policy**. That is an *organisational* capability, not a technical one — the first real piece of
Capability Debt this product produced, and precisely the kind the thesis predicts.
