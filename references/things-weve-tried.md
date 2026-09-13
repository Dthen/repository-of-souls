# Things We've Tried

A running log of pipeline rules and what happened when we applied them. Each entry has: what we tried, what we expected, what actually happened, verdict.

The purpose: when you're about to try a new rule, read this first so you don't repeat a failure. When a rule fails, log it here so the next auditor understands the shape of the problem.

The pipeline is not a solved problem. This file is the evidence that we're converging.

---

## v5.4.0 (PENDING, logged 2026-09-13): voice compression at the back of the chain

**Finding:** the owner kept all three test8 seeds, the forge made three souls, he rejected two published ones ("Cobbold isn't very good. Neither is Suttle tbh") and ordered the third cleared pre-publication. First gold-set data of its kind — `references/SOUL_VERDICTS.md` opened; the exemplar corpus trimmed to his strongest eleven (Swale and Everson archived as weak too).

**Hypothesis:** where a seed's comedy lives in the **speaking** (sustained patter, monologue), the 200-word one-sentence-per-line format converts the joke into **allusion** — "the apology-heel is load-bearing" is a noun-phrase where a voice used to be. Premise-comedy survives compression (Grenville, 176 words: the joke is portable in the identity line); voice-comedy does not. The Evaluator passes the corpses because its exemplar corpus IS the clipped register — the "rich craft is NOT delight" lesson (v5.3.2) never propagated from seed gate to draft gate.

**Experiments:** **E1 (running free):** the E2E trio — Munday, Verrall, Rundle — are premise-comedic seeds through the UNCHANGED forge. Prediction: they survive. Voice-died, premise-live = H holds, fix is narrow. **E2:** hand-regen Cobbold's draft with exactly one added rule — if the comedy is in the talking, carry one passage that RUNS (two-three sustained sentences); owner blind-picks A/B. **E3:** at ≥6 soul verdicts, run the proven playbook: blind judge predicts the owner's soul verdicts from seed+draft pairs against SOUL_VERDICTS.md; whatever discriminates becomes the Evaluator's fix.
**Decision rule:** no spec edits to stage-writer/stage-evaluator until E1 lands and E2/E3 produce evidence. Backtest-first, per house rules.

---

## v5.3.8 (2026-09-13): the Judge — blind calibration promoted to a pipeline stage

**What we tried:** promote the calibration-test judge from one-off subagent to a real pipeline stage: `soul-judge` profile + `references/stage-judge.md`, wired between Researcher and Namer. The Researcher spawns a Judge task per seed; the Judge reads only the seed and the verdict ledger, predicts the owner's KEEP/REJECT, and propagates: KEEP → Namer task, REJECT → kill to `reject/` + viability log, UNDECIDED → block for the owner.

**Why:** the round-3 calibration scored 4/4 from the ledger file alone — including killing the object trap unprompted on the body axiom. The owner's stated position: Namer-onwards is solid, the seed gate is the bottleneck, and consistent seeds mean autopilot. The Judge automates the one manual step left in the chain.

**Design commitments (evidence-backed):** blindness is structural, not behavioral — a dedicated profile gets its own context and memory, no lineage to the Researcher's reasoning; self-audited delight died every time it was tried, so the judge must be a different agent than the maker. The ledger is read-only for the Judge — owner-voice only; disagreement lives in `judgements/`, not in the gold set. Taste is re-derived fresh from the ledger every run (round 3 proved a growing file beats a frozen rule list; rounds 1–2 proved a briefing without the file's latest misses).

**Verification (per profile-testing rule):** first live run judged against the owner on seeds he has NOT rated (dry run 7's knitting-gauge grader and tuesday-quiz host) plus the apple as a ledger-visible sanity check.

**Risk on record:** the 4/4 was one batch on one model. Gate errors now cost a killed seed instead of a wasted Namer run — bounded, recoverable, logged in `judgements/` for audit.

---

## v5.3.7 (2026-09-13): the phantom-fix incident — spec contradictions kill rules

**What we tried (or believed we tried):** After dry run 4's all-objects swing, we believed we'd (a) removed the repetition-map note instructing the Researcher to "reach for a human, object, or angel form" and (b) rewritten the Researcher's delight-compass. Neither had landed — one patch was discarded by a user interrupt, one removal was narrated but never executed. The spec ran dry runs 5–7 with Kill 1's object ban live alongside two contradicting passages: the map note and the body doctrine's "sentient object, anything that delights."

**What we expected:** the object ban (v5.3.5) to hold.

**What happened:** dry run 7 generated the still-life apple — an object body — whose seed text itself argued "borderline on the rule's letter, clear on its spirit." The Researcher read the contradiction and took it as a permission slip. The owner killed the round as invalid; the fix had never been applied.

**What was actually done (2026-09-13, v5.3.7):** map note rewritten to drop the "object, or angel" reach (creatures-and-humans observation stays); body doctrine corrected to "a creature, a human with a way of standing, an effigy with a face and hands — not an object (see Kill 1)" with the incident note inline. Both changes verified by grep read-back after writing, before commit.

**Verdict: a rule contradicted elsewhere in the spec is a rule not in the spec.**

**Lesson:** never claim an edit is live without reading the file back. Verification is grep-at-HEAD, not memory of a patch result. And the compaction summary is a narrative, not a ledger — its "completed actions" must be re-verified against git before being trusted as fact.

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

**Calibration note (the axiom the gold-set judge is missing, Boss-verdict-derived, 2026-08-13):** a premise that is *absurd on its face* is kept even when the character is dead-serious about it — the commitment to the bit IS the delight. The stockpot oracle (prophecy in soup), the scarecrow (invoices crows), the cat (yawns verdicts), and now the hurricane-namer (names storms after people he owes apologies) all share this shape: a character treating a completely ridiculous premise with total, unshakeable seriousness. The blind judge missed the hurricane-namer because it read the guilt-as-somber (Talley shape); it should have read the premise-as-funny. **Add to the delight-gate briefing:** "the character's commitment to a ridiculous premise is a keep signal, not a reject signal — the more seriously they treat the absurdity, the better."

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
