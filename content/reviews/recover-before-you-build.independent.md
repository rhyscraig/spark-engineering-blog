# Independent review (human/engineer, blind) — recover-before-you-build

Formed by reading the article only, before opening Spark's self-review.

| # | Category | Severity | Finding |
|---|----------|----------|---------|
| H1 | Accuracy | blocker | Paragraphs 3–5 describe the **review process itself** (publishability, accuracy, verdict Publish/Revise/Reject) — the brief's *review-dimension instructions leaked into the article body*. The article is partly about its own reviewing, not about Recover-vs-Build. |
| H2 | Evidence | major | No concrete example, data, or worked reasoning behind any trade-off claim; the brief explicitly required reasoned, not asserted, claims. Self-contradiction: the text *demands* claims be backed by evidence while providing none. |
| H3 | Communication | major | The genuine judgement calls the brief asked for (when is recovery a false economy? how to tell "almost works" from "looks like it works"?) are name-dropped but never answered — reasoning incomplete. |
| H4 | Readability | minor | The conclusion restates the introduction almost verbatim; repetition across paragraphs 2, 6, 7. |
| H5 | Editorial | minor | Filler openings ("In the realm of software development", "In conclusion"); generic voice, low signal. |
| H6 | Editorial | minor | Front-matter `summary` is empty (metadata defect introduced by the generalised generator). |
| H7 | Readability | minor | 404 words vs the brief's 700–900 target — underlength. |

**Verdict: REVISE.** The taxonomy (recover / complete / build) is correct and the skeleton is
sound, so not Reject. But the brief-leak (H1) and total absence of evidence (H2) are
disqualifying for an article whose whole subject is making evidence-based judgements — so not
Publish. Send back for regeneration with corrective guidance; do not hand-edit.
