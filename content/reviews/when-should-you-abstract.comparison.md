# Blind-review comparison — when-should-you-abstract (sample #2)

## Verdicts

- **Spark:** Revise · **Human:** Publish → **DISAGREE** (reviewer more conservative — **2nd
  consecutive occurrence**, after 002 r2).
- **Decision: PUBLISH.** Rule: publish when no *real* blocker/major remains. Spark's one
  "major" (lacks structure) is a false positive (the article has 5 clear sections).

## Metrics

- **Major overlap:** n/a — human found no majors; Spark's sole "major" is a false positive.
- **False positives: 2** — (1) "no example of the rule not being absolute" (the DB-connection
  example *is* in paragraph 2); (2) "lacks structure and transitions" (5 well-formed sections).
  Reviewer reliability **degraded** vs 002 (which had 0 hallucinated findings).
- **Human-only real findings: 3** — underlength (438 vs 700–900), empty `summary`, title/heading
  mismatch. All minor.

## Two predictions, both confirmed

1. **"The builder will improve; the reviewer won't."** ✅ The builder improved sharply — Evidence
   dropped major → minor, all judgement questions answered, **no brief-leak** (the round-1 blocker
   did not recur). The reviewer did **not** improve; if anything it produced *more* false positives.
2. **"The organisation improved without changing any organisational roles."** ✅ The only thing
   changed was the **brief** (accumulated organisational guidance). Builder and Reviewer code are
   byte-for-byte identical to 002.

## Trend forming (Constitution 22 — 2 observations = possible pattern)

- **Reviewer more conservative than human:** 2 occurrences (002 r2, 003). One more → promote to
  Board as a publication-threshold investment. **Still do not codify a policy** (not yet 3).
- **Reviewer false positives:** rising (0 → 2). New watch item.
- **Evidence deficiency:** did **not** recur as a real gap (builder resolved it via the better brief).
- **Underlength / empty summary:** recurring product (not Spark) defects — the tighten pass
  over-compresses; `generate.py` doesn't set `summary`. Product-owned fixes, tracked here.
