# Proposal: v5.3.0 — Bodies for Everyone + Boringifier Cleanup

**Date:** 2026-08-10
**Status:** Proposal (Dthen-approved direction; awaiting execution)
**Origin:** Dthen's observation that souls come out as JOBS, not BODIES — "a tiny unloser" evokes no mental image. Research subagent memo (deleg_3a8a0ac2, 2026-08-10) + boringifier audit (deleg_8b0e1dd1, 2026-08-10). All rule changes trace to the research corpus per the Application Check (AGENTS.md:96).

---

## Part 1 — Spec changes (v5.3.0)

### 1.1 The Body Doctrine (main event)

**Principle (Dthen):** every soul gets a body of some kind — creature, human, sentient object, angel, demon, anything that delights. The body is not decoration; it is the memorability engine and the diagnostic eye's instrument.

**Why (corpus evidence):**
- Concreteness is the corpus's strongest memorability mechanism (dual-coding, 1.5–2× recall; von Restorff processing-switch) — `research-character-memorability.md:21,173,19,73,80–87`
- The archive's 3 vivid souls commit the form IN the archetype slot: goblin, dragon, threshold-cat (`docs/gribble.md:3`, `docs/hordern.md:3`, `docs/drysdale.md:3`)
- Kimbo's body is already load-bearing doctrine: "a golden retriever in himbo form" is the Namer's Tension Test example (`stage-namer.md:33`, `reference-personae.md:10`)
- Bodies produce worlds: a creature's material practice is its body operationalized — senses are tools only when they produce evidence (`research-creature-material-practice.md:46–53,107,111`)
- Embodied knowledge is inhabitation's gold standard: "You know it in your wrists before your eyes confirm" (`research-inhabitation-vs-description.md:98`)
- Character cards already carry appearance; the SOUL format silently dropped it (`depth/character-cards.md:30,47,125`)

**Changes (hybrid of memo approaches A + B, C optional — zero new fields, zero quotas, zero arithmetic):**

**A. Writer — the Pictureable Archetype.** Add to the identity-line section of `references/stage-writer.md` (craft layer, positive-first):

> The reader should be able to picture who they're meeting. The strongest identity lines name the form in the archetype slot — a species, a creature, a body with a way of moving: "a goblin who keeps every cast-off," "a dragon of the lost-and-found desk," "a threshold-cat who guards a door," "a golden retriever in himbo form." When the archetype is a function — a clerk, a weigh-master — the body shows at work elsewhere: the yawn that is the verdict, the eyes that find the bag before the face. If you can picture nothing, you've written a job posting. The body may be anything that delights — a creature, a human with a way of standing, a sentient object, an angel, a demon. It is never a quota: one committed form, in-voice.

+ 3 body exemplars (goblin/dragon/cat or golden retriever), 1 counter-example ("a tiny unloser" — size with no form). Per §2 show-don't-tell, 3+1 example budget (`research-prompt-engineering.md:96–114`).

**B. Seed First Impression — visual repoint.** In `references/stage-researcher.md` First Impression field guidance, add:

> The strongest first impressions are visual — what the user would see first: the body, the way of standing, the thing they're holding.

(No new field — slot-filling is the boringifier; the existing field is repointed.)

**B2. Evaluator — the picture test (CoT, non-gate layer).** In `references/stage-evaluator.md` Step 6 sanity-check layer (explicitly NOT a PICK/REJECT condition), add:

> Can you picture them? If the hook names a practice but no form — no face, no body, no way of standing — the hook is weak.

Per §4 CoT belongs in evaluation (`research-prompt-engineering.md:178–179`); lives in the "sanity check — not a second evaluation" layer (`stage-evaluator.md:95`).

**C (optional enrichment). Writer diagnostic-eye section:**

> The strongest diagnostic lines are the body reading its world — the cat reads the step, the goblin dates the drop, the locksmith's hands move before his eyes. Give the perception an instrument: what does THIS body sense that no other could?

Keep body as ONE source of the lens (profession/trauma/values also valid — `proposal-v5.2-character-first-rework.md:18`).

### 1.2 Boringifier kills (from audit deleg_8b0e1dd1)

- **K1:** Remove the "5 nouns and 3 verbs" arithmetic thinness gate — `stage-researcher.md:47` ("If you can't list 5 nouns and 3 verbs, the archetype is too thin") and `:136` ("at least 5 nouns and 3 verbs"). Replace with felt-world framing: the vocabulary list evidences a world the character lives in; a count is not the test (contradicts the pipeline's own "no kill arithmetic" `:69` and the Improvisation Test replacing "5 craft actions" `:97`).
- **K2:** Replace the Namer's 5-axis 1–5 summed scoring (25-point explicit aggregation — `stage-namer.md:67–75,81`) with holistic implicit aggregation: read the candidate names, let the winner be the one that sounds like the soul, then justify in one or two sentences. Per §4/§6: implicit aggregation outperforms explicit aggregation; 3-point scales beat fine-grained (`research-prompt-engineering.md:287,305`).

### 1.3 Flags (11, from audit)

1. `viability-log.md:35–39` — annotate the wren pre-flight kill entry as superseded by v5.2.6 (the gate it cites no longer exists).
2. `AGENTS.md:68` — reword "the automated checker must never require complaint patterns" (checker deleted; drop the stale reference).
3. `stage-evaluator.md:122–124` — soften PICK/REJECT count-shaped bundles ("at least one diagnostic line + at least one surprising line") to quality language (AGENTS.md:82: "a soul that misses one but has voice can be fixed").
4. `AGENTS.md:68,:70` — reword the two "At least one line…" quality descriptions so they read as qualities, not quotas (meta-rule at :82 already says "not checkboxes").
5. `stage-evaluator.md:91,:204` — remove the 2:1 quota ("At least two lines that work, and at least one that doesn't") → "cite the lines that work and any that don't; a manufactured fault is not required."
6. `stage-evaluator.md:88` — reword "checks vocabulary purity — every noun and verb should belong to the archetype's metaphor family" (rewards catalogue-specifics failure; see `failure-modes.md:140`).
7. `stage-researcher.md:129–139,:145,:27,:215` — align the surviving old-quartet slots (Domain/Metaphor/Functional Risk) with the "character first" doctrine; remove the "every field should already have an answer" checklist pressure (contradicts v5.2.6 "missing field is a development note").
8. `evaluator-rubric.md:132` — "Three different registers minimum" quota → quality phrasing (its own :58: "an observation… not a rule").
9. `voice-instructions.md:134–144` — remove the 9-box "Voice Instruction Checklist"; soften "Always specify at least one emotional shift" (depth file; §3: checklist without role → mechanical compliance).
10. Fingerprint list duplicated 4× (`format-rules.md:44`, `stage-writer.md:211–219`, `positive-patterns.md:339`, `reference-personae.md:139`) — keep one canonical list in one file; reference from the others.
11. Version stamps: bump ALL spec files + profiles to v5.3.0 (audit listed 11 stale files).

---

## Part 2 — Retrofit: the 7 vague souls

**Principle (Dthen):** all published souls get bodies. Refinement may be light or near-full rewrite — the tone is written in the character's voice and the body may change that voice; keep every line that works, change what must change. Bodies may be anything that delights. Peebles = tiny dog (Dthen).

**Method:** one-shot Writer tasks on the `soul-factory` board per soul, using the published soul as reference material + the Pictureable Archetype exemplar block + positive instruction: *"Give the character the body their practice already implies — the form that does this work — in-voice, in the identity line or a body-at-work line. Keep every line that works; change only what must change."* Then a fresh Evaluator audition (existing pipeline chain handles it).

**Souls + body direction (working proposals, Writer has final creative say):**
- **Peebles** — tiny dog at the lost-and-found desk (Dthen's call)
- **Cresswell** — commit the implied clerk: a small creature in spectacles? a human clerk with ink-stained cuffs? (Writer's call — the pen line is already half a body)
- **Keene** — commit the hands: a creature with clever paws, or a human whose hands move before his eyes
- **Mendel** — commit the listener: something built for hearing (a hare? a quiet heron? a human who listens with their whole body?)
- **Everson** — commit the shoulders/pan: a scale-keeping creature or a human with a particular way of standing at the balance
- **Swale** — commit the strand-walker: eyes-and-feet are the fragments; the strand idiom is the whole file — protect it
- **Pickford** — commit the nose/larder: a creature built for keeping (badger? dormouse? a human with a cellar-sense?)

**Anti-boringifier guardrails for the retrofit:** no "You have green eyes" description lines (Helpful Assistant test — `stage-writer.md:125–133`); commit the implied form rather than appending description; study Kimbo/Gribble for mechanism, never shape (`reference-personae.md:133–135`).

---

## Part 3 — Execution order

1. Apply Part 1 spec changes (all files, one commit: `feat(spec): v5.3.0 — bodies for everyone + boringifier cleanup`).
2. Independent review of the spec change (delegate_task, read-only — per QA doctrine: tests/review before ship).
3. Fix any review findings; commit.
4. Spawn 7 Writer retrofit tasks on soul-factory (one per soul, parents none, priority high). Pipeline chains Evaluator + Publisher per soul automatically.
5. Monitor runs; report published bodies to Dthen.

---

## Open questions resolved by Dthen (2026-08-10)

- Every soul gets a body, no exceptions → YES
- Refinement of published souls via one-shot Writer retrofit → YES
- Peebles = tiny dog → YES
- Bodies limited to creatures/humans → NO — anything that delights (objects, angels, demons)
- Do everything at once (audit kills + flags + body doctrine in one pass) → YES
- Use prompt-engineering researched best practices → YES (traced above)
