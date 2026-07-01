# Product Brief — Article 001

**Product:** The Spark Engineering Story (a blog documenting the journey of building
Spark and the engineering principles discovered along the way).

**Production question (the objective):** *Can Spark produce one publishable engineering
article using its current organisational capability, while recording every friction
without immediately fixing it?* — a stronger, objective completion condition than "publish
a blog." Success is **honest** engineering coverage, not audience and not
coverage-for-coverage's-sake: only run a stage the product genuinely pulls (Constitution 21).
The natural path: plan → repo → generate → quality-check → build → publish → evidence →
capability-debt → close. If it does those honestly, it succeeded even if nobody reads it.

## Article 001

- **Working title:** The Moon Robot Principle: Build the Machine That Builds the Machine
- **Source:** `ziggy/logs/BLOGGING_LOG.md` (2026-06-13) — pre-ideated, no external research.
- **Audience:** Developers, tech leads, anyone building complex systems.
- **Hook:** NASA wouldn't send a robot to the moon and tell it to start building houses.
  Why do developers do the equivalent every day?
- **Core idea:** Evaluate every build decision by *what it enables*, not *what it does*.
  Sequence matters more than destination: power → tools → materials → construction.
  The bootstrap problem — you can't use the thing to build the thing until the thing exists.
- **Unique angle:** NASA mission-planning philosophy applied to software; concretely, how
  Spark was built as "the machine that builds the machine" (a factory, not a product).
- **Constraints:** ~700–1000 words. Markdown. Honest, practical, first-person engineering
  voice. No fabricated statistics.
