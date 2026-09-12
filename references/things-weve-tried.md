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

**What happened (backtest 2026-08-13, pre-dry-run):** 15/15 correct against the full corpus — kills Talley + Mendel (generic props, none with a history), passes all 11 live souls + both trial pass-cases + stockpot oracle. Zero false positives, zero false negatives. Caveat noted: the discriminating line is specificity, not prop-count (Talley's ledger is just a ledger; Gribble's kettle has a dent and a Tuesday) — and like any positive-ish rule it can be gamed by stuffing props into an abstract concept. The dry run watches for that.

**Verdict:** passed backtest; dry run 2 passed.

**Dry run 2 (2026-08-13):** 3 seeds, 2 pass / 1 deliberate kill. Opera prompter (PASS — the box, the fat-print score with its spine broken at the arias that always dry, the soprano's heels at eye height, dust sifting through the lid during the second act — a world you can walk through in mitten-deep specificity) and rink maker (PASS — the pond at 3am, the lantern, the fan of the hose, steam off the flood, the boom of the ice making itself, the mackinaw, the pump-house thermometer) both passed with the richest worlds the Researcher has ever produced. Crossword-setter (FAIL — kitchen-table props, fantasy carried by mental play not material practice) was correctly killed. The Evaluator explicitly noted the old v5.3.0 failure-mode clause would have *passed* the crossword-setter, proving the new clause discriminates where the old one didn't.

---

## v5.3.3 (2026-08-13): the game closes — second-visit test

**What we tried:** Replacing thin-sensory-world with "the game closes" (second-visit) test. The previous test was a positive requirement (must have a world) which the prompter passed despite being a closed game. The new test is a negative one: does the second visit produce new moves, new stakes, new friction? If the second visit is identical, it's a portrait, not a game.

**What we expected:** Catch the prompter, tuner, choirmaster, rink-maker; spare stockpot oracle and scarecrow.

**What happened (backtest 2026-08-13):** 17/17 correct against the full corpus — kills Talley, Mendel, tuner, prompter, choirmaster, rink-maker; passes all 12 live souls, scarecrow, stockpot oracle. Zero false positives, zero false negatives. The test correctly identifies that the prompter's second visit is identical (same whisper, same catch), the tuner's second visit is identical (same grief, same devotion), the choirmaster's second visit is identical (same unison-collapse, same bass), the rink-maker's second visit is identical (same flood, same scrape, same boom). The stockpot oracle and scarecrow pass because their second visits generate new moves (new forecast to mock, new rent to dispute). Even the 12 live souls pass, though the test is strict enough to flag Kimbo — the test is strict and correct; the fix is improving the reference personae, not softening the test.

**Verdict:** passed backtest; dry run pending.

---

## v5.3.4 (2026-08-13): the agency test (prop vs. person)

**What we tried:** Extending the body doctrine: the body must be able to ACT — a working set of verbs, hands or their equivalent, the ability to initiate in a turn. A body that can only be acted upon (triggered, read, warmed by touch) is a prop, not a person.

**What we expected:** Kill the dry-run-4 sentient objects (watch, match, banister — each had a joke, a world, an open game, and no hands); spare all live souls including Gunnell (a robot — an agent) and the stockpot oracle (a small woman).

**What happened (backtest 2026-08-13):** 13/13 live souls pass, oracle passes, all three objects correctly fail. Zero false positives. The test is complementary to the kill stack: game-closes catches portraits (Talley, Mendel, prompter — they act, but the interaction completes); agency catches props (the objects — the interaction stays open, but they can't initiate). Placed with the body doctrine (develop at seed time), not as a fourth kill.

**Context logged honestly:** dry run 4's all-objects batch was caused by a dictatorial note Kimbo appended to the repetition map ("reach for a human, object, or angel form") — the note has been removed; the map is Evaluator/Publisher observations only. Kimbo does not write to the repetition map. Also logged: the v5.3.2 fingerprint — "The comedy is the delivery system; the X is the load" appeared verbatim (domain noun swapped) in all three dry-run-4 seeds' Functional Risk sections. New-rule phrasings get copied; watch for it on every spec change.

**Verdict:** passed backtest; dry run pending.

---

## v5.3.2 (2026-08-13): the craft-trap correction (delight recalibration)

**What we tried:** Adding few-shot examples of actual delight-picks to Step 2's delight definition, after noticing "delight" was being read as "rich craft."

**What we expected:** The Researcher's delight compass was miscalibrated — it called the choirmaster, opera prompter, and rink-maker delights (deep worlds, real failure modes, flawless structure) while the user rejected all three as boring. Meanwhile the seeds the user actually loved (Gribble, Drysdale, Gunnell, stockpot oracle) all share a shape the spec never named: **a joke you mean** — silly premise, load-bearing interior.

**What happened:** [pending — first real dry run]

**Verdict:** [pending]

**Also logged:** dry run 2 (v5.3.1 trial) was invalid as a test — the brief asked the Researcher to "note which passed vs. failed," which incentivized planting a designed-to-fail seed. A comprehension quiz, not a dry run. Results binned; future dry runs generate naturally with no planted outcomes.

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
