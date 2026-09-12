# Things We've Tried

A running log of pipeline rules and what happened when we applied them. Each entry has: what we tried, what we expected, what actually happened, verdict.

The purpose: when you're about to try a new rule, read this first so you don't repeat a failure. When a rule fails, log it here so the next auditor understands the shape of the problem.

The pipeline is not a solved problem. This file is the evidence that we're converging.

---

## v5.3.0 (2026-08-12): failure-mode kill-clause

**What we tried:** Kill 2 in stage-researcher.md — reject any seed whose character cannot plausibly fail. "If nothing can genuinely go wrong in the world of the concept, the seed is word salad."

**What we expected:** Catch Talley/Mendel-shaped seeds (decorated abstraction) while sparing characters with real stakes.

**What happened:**
- First backtest: passed 11/11 live souls, correctly flagged Talley + Mendel. False-positive rate: 0%.
- Second trial (failure-mode-only test run): killed the stockpot oracle — the most creative, fun seed in the batch. The pot never curdles, the prophecy never misses. But you could *see* the kitchen, the pot, the ladle, the bread on the sill. The seed had a world. It just didn't have a failure mode.

**Verdict: too blunt.**

The rule conflated two things: "no failure mode" and "no material world." Talley had neither. Stockpot oracle had a world but no failure mode. The rule killed both. It's been replaced by the thin-sensory-world test (v5.3.1) which only kills the no-world case.

**Lesson:** a rule that catches the right duds can still kill the interesting-by-breaking-the-rules. When a rule's false-positive is a creative hit, the rule is too blunt — narrow it, don't keep it and add exceptions.

---

## v5.3.1 (2026-08-13): thin-sensory-world kill-clause

**What we tried:** Kill 2 — reject any seed whose character you cannot picture in a specific room with specific props. "A desk and a ledger" is too thin. "A kitchen with a pot that has a history" is enough.

**What we expected:** Catch Talley-shaped seeds while sparing stockpot oracle.

**What happened:** [pending — first trial not yet run]

**Verdict:** [pending]

---

## Earlier entries (compressed)

- **v5.2.4.6, v5.2.4.7:** not-relational kill, not-a-someone kill, no-pulse kill. The three-kills structure itself. Survived because the tests are about the character's shape (agent, relational, pulse), not their world's content.

- **v5.2:** character-first rework. Flipped discovery order from job → character to character → world. Survived because it's about *order*, not content.

- **v5.2.1:** vitality over griping. Removed the griping mandate. Survived because it removed a boringifier rather than adding a positive requirement.

- **v5.2.2:** reference-personae audit. Removed un-evidenced constraints. Survived because it removed rather than added.

- **v5.2.3:** depth-file restructure. Examples-first format. Survived.

- **v5.2.4.x:** the idea-time checklist, the brief contamination, the relational-verb requirement. Several iterations. The checklist-shaped ones were withdrawn (they produced checklist-shaped candidates). The delight-first reframing survived.

**Pattern that keeps working:** remove boringifiers, don't add positive requirements.

**Pattern that keeps failing:** add a positive requirement to catch duds, the model games it, the creative hit gets caught in the crossfire.

---

## Version

This file lives at the version of the spec it documents. When a rule lands, append the entry. When a rule is withdrawn, keep the entry and mark it withdrawn — the failure is evidence, not embarrassment.
