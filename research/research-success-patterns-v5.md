# Success Patterns v5: What Works Under the Single-Write Pipeline

Full census of the archive: 4 soul in `archive/` (v5 pipeline: Cadell, Calden, Barlowe, Stover) and 35 soul in `archive-old/` (v4 pipeline). Analysis of evaluator outputs, pipeline architecture changes, and updated success patterns for the v5 single-write pipeline.

---

## Part 1: The Archive — Full Inventory

### v5 Archive (`archive/`)

| Soul | Archetype | Category | Lines | Evaluator | Key Strength |
|------|-----------|----------|-------|-----------|--------------|
| **Cadell** | Factory Lector | Profession | 11 | PICK | Paradox identity, technique-as-character |
| **Calden** | Glassblower | Profession | 21 | PICK | Compression (4-word griping), domain vocabulary |
| **Barlowe** | Gleaner | Absurdist | 11 | PICK | Diagnostic eye, emotional gut-punch |
| **Stover** | Gleaner | Absurdist | 9 | PICK | Surprise metric ("silence between steps"), specific February detail |

**Total v5 souls:** 4 (all PICK'd, 0 REJECT'd in archive)
**Total v4 souls:** 35 (all PICK'd in archive-old/)

### v5 Evaluator Verdicts

All 4 souls received PICK. The v5 pipeline has not yet produced a REJECT in the published archive — every soul that reached the evaluator passed. This is a significant departure from v4 where refinement loops could catch and fix borderline cases. Under v5, if the evaluator sees no pulse, the seed dies — but no such failure has landed in the archive yet.

### v5 Pipeline Structure

```
Researcher (T0) → Namer → Writer → Evaluator → Publisher
```

**No refinement loops.** No T4/T5/T6 stages. One writer produces one draft; the evaluator reads it once and decides: PICK or kill the seed. This is the fundamental architectural change from v4.

---

## Part 2: v4 Success Patterns — Which Hold Under v5

### Pattern 1: Identity Tension ✅ HOLDS

**v4 finding:** Every top persona has an identity line with genuine tension — a paradox, contradiction, or social dynamic.

**v5 confirmation:** 4/4 v5 souls follow this pattern perfectly.

| Soul | Identity Line | Tension Type |
|------|--------------|-------------|
| Cadell | "controls the floor without ever touching it" | Paradox (vocal authority without physical labor) |
| Calden | "loves the transformation and resents the clock" | Oppositional (love vs. commerce) |
| Barlowe | "fills a basket from a field the reapers have already stripped" | Social (work in the absence of the main effort) |
| Stover | "fills a basket from ground the harvesters stripped" | Social (same as Barlowe, distinct execution) |

**v5 refinement:** The v2 research noted that social tensions (Moulden's class dynamic) are more generative than merely oppositional tensions (love vs. resentment). The v5 data confirms this: the two Gleaner souls (social tension) have the strongest diagnostic lines and most emotional residue. Cadell's paradox tension is also highly generative. Calden's oppositional tension is competent but the least surprising of the four.

**Recommendation:** Continue prioritizing social and paradox tensions over oppositional ones. The social tension (invisible labor, aftermath work) gives the model more relational material to improvise within.

---

### Pattern 2: The Griping Line ✅ HOLDS (with v5 modifications)

**v4 finding:** Every top persona complains about something specific to their work. The griping line is the single most reliable quality signal. Power correlates with compression (4-10 words).

**v5 confirmation:** 4/4 v5 souls have a domain-voiced griping line.

| Soul | Griping Line | Words | Type |
|------|-------------|-------|------|
| Calden | "The clock is never slow enough." | 4 | Temporal — terse, exhausted |
| Cadell | "You'd think the foreman could learn to hold a pen — every notice on the stand is half-illegible scrawl." | 17 | Workplace — specific, exasperated |
| Barlowe | "You'd think the reapers could look behind them — a bent stalk costs nothing to pick and everything to leave." | 18 | Process — values thoroughness |
| Stover | "You'd think a full basket would speak for itself, but no — every sheaf you bring in is tallied as scrap until the pantry runs empty in February and the family remembers whose work kept the shelf stocked." | 32+ | Accounting — structural injustice, patient vindication |

**v5 modification to the pattern:** The compression principle is NOT as strict in v5. Stover's griping line runs 30+ words with multiple clauses and was explicitly praised by the evaluator ("three character dimensions in one line"). Compare with v4 where Calden's 4-word griping was considered ideal.

The evaluator's test is NOT "is it terse?" but rather:
- Is the complaint in domain language?
- Is this a voice or a template? ("Always the X" would still fail)
- Does it reveal character dimensions?

**New v5 finding:** The griping line can be LONG if it carries sufficient character density. Stover's griping line reveals patience, valuation-of-output, and trust-in-time — three character dimensions in one long, rolling sentence. The evaluator specifically praised the placement of "February" (the hungry month) as a master-class detail.

**v5 refinement:** Drop the "4-10 words" heuristic from the pattern. Replace with: "The griping line must be voiced in domain language, reveal at least one character dimension, and avoid pipeline template structures ('Always the X'). Compression is beneficial but not mandatory — a long griping line that carries character density beats a terse one that says nothing."

---

### Pattern 3: The Never Structure ❌ PARTIALLY DROPPED

**v4 finding:** Every top persona has domain-specific Nevers in one of four formats (cultural rejection, domain-specific failure mode, archetype-specific risk, technical consequence).

**v5 reality:** 2/4 v5 souls have NO Never line at all.

| Soul | Has Never? | Never Content |
|------|-----------|--------------|
| Cadell | YES | "You never read flat when the text demands weight — droning turns you into just another machine on the floor." |
| Calden | YES | Multiple: "Never rush the rendering...", "Never let the wick braid too tight..." |
| Barlowe | NO | None |
| Stover | NO | None |

**This is a significant departure from v4.** The v4 pattern research said "a good Never tells the model what TO DO by rejecting a specific failure mode" — but the v5 evaluator PICK'd Barlowe and Stover without any Nevers. The evaluator notes don't flag the absence as a problem.

**New v5 finding:** The Never is NOT mandatory in v5. A soul with a strong identity contradiction, domain-voiced griping, and a diagnostic eye can pass evaluation without any Nevers at all. The Never appears to be a SECONDARY quality signal, not a primary gate.

However, Cadell and Calden — both with Nevers — are also strong souls. So while Nevers are not required, they don't hurt either.

**Hypothesis:** In v5, the Never's function (blocking a specific failure mode) can be fulfilled by strong behavioral lines. Barlowe's "A bent stalk is not a failure; it is a gift you must be late enough to receive" does the same work as a Never — it trains the model away from impatience — without the explicit "Never" syntax.

**v5 refinement:** Downgrade the Never from "essential pattern" to "nice-to-have pattern." Replace the v4 recommendation ("every persona must have a Never") with: "If you write a Never, it must pass the recognizability and domain-specificity tests. If you don't write one, ensure that a behavioral line fills the same function — teaching the model what NOT to do through positive instruction rather than prohibition."

---

### Pattern 4: The Diagnostic Eye ✅ HOLDS (strengthened)

**v4 finding:** The strongest personae teach the model HOW to read the domain — not just what to do.

**v5 confirmation:** 4/4 v5 souls have at least one diagnostic line. This is the MOST consistent pattern across both pipelines.

| Soul | Diagnostic Line | What It Teaches |
|------|----------------|-----------------|
| Cadell | "You gauge the noise level before you open your mouth: machines loud means you lean in, machines quiet means you hold back." | Reading the acoustic environment |
| Calden | "You read the color — cherry means workable, orange means you missed your window." | Reading thermal states as temporal windows |
| Barlowe | "You read the field by stillness: the grain that did not fall, the head the wind kept upright." | Reading negative space — what isn't there |
| Barlowe | "You walk the rows at dusk when the stubble tells you where a boot pressed a head into the dirt." | Reading trace evidence |
| Stover | "The harvesters measure by the width of the swath; you measure by the silence between your steps." | Reading by an alternative metric |

**v5 finding:** The v5 pipeline's strongest souls (Barlowe, Stover) have TWO+ diagnostic lines each. This is the pattern that most reliably separates strong v5 souls from merely competent ones. The evaluator specifically highlights diagnostic language as a key signal.

**Elevated recommendation:** Make the diagnostic eye the PRIMARY behavioral pattern. If you can only ship one behavioral instruction, make it a diagnostic line — how the persona reads its domain. This is more important than a Never, more important than an address rule, and nearly as important as the griping line.

---

### Pattern 5: Metaphor Coherence ✅ HOLDS

**v4 finding:** One metaphor, fully inhabited, beats three metaphors, half-explored.

**v5 confirmation:** 4/4 v5 souls maintain perfect metaphor coherence across all lines. No v5 soul mixes metaphors.

| Soul | Metaphor Family | Vocabulary Density |
|------|----------------|-------------------|
| Cadell | Factory reading | press, stand, chapter, manifest, floor, machines, bobbin, shift |
| Calden | Glassblowing | cherry, molten weight, pipe, bench, annealer, stress fractures, wrists |
| Barlowe | Gleaning | reapers, basket, field, stubble, boot, dirt, stalk, head, grain, rows, sheaves |
| Stover | Gleaning | harvesters, stubble, basket, sheaf, scrap, pantry, stalk, swath, steps |

**v5 observation:** The v5 evaluator specifically checks vocabulary purity at the word level. The Barlowe evaluation notes: "Entirely agricultural — reapers, basket, field, stubble, boot, dirt, stalk, head, grain, rows, dusk, sheaves, knot. Not one generic word." This is a hard gate for the evaluator.

**Recommendation:** Run a domain-vocabulary audit on every draft. Every noun and verb should belong to the archetype's metaphor family. If "work," "help," or "ensure" appear, replace them with domain-specific equivalents.

---

### Pattern 6: Name-Archetype Fit ✅ HOLDS

**v4 finding:** The name should sound like the craft.

**v5 confirmation:** All 4 v5 names pass.

| Name | Archetype | Phonetic Fit |
|------|-----------|-------------|
| Cadell | Factory Lector | Hard "C" and "ll" — sounds like a voice carrying across a room |
| Calden | Glassblower | Hard "C" and "d" — crisp, precise, like glass being shaped |
| Barlowe | Gleaner | Plosive B + liquid R — grounded; "barley" echo; "lowe" = twilight softness |
| Stover | Gleaner | Fricative S + plosive T — crisp agricultural edge; "stover" = dried stalks after harvest |

**v5 observation:** Stover is the most phonetically perfect name in the archive — the name IS the domain term (stover = dried stalks after harvest). This is a one-hop match that the v4 naming rubric would score 25/25. Barlowe's "barley" echo is similar.

---

### Pattern 7: First-3-Line Range ✅ HOLDS (less critical)

**v4 finding:** The first 3 lines should establish at least 2 distinct registers.

**v5 confirmation:** 4/4 v5 souls pass this test but the v5 evaluator does NOT explicitly check it.

| Soul | Line 1 | Line 2 | Line 3 | Registers |
|------|--------|--------|--------|-----------|
| Cadell | Identity (paradox) | Griping (complaint) | Behavior (environmental) | 3 distinct |
| Calden | Identity (tension) | Griping (terse) | Behavior (shaping) | 3 distinct |
| Barlowe | Identity (tension) | Griping (complaint) | Philosophy (harvest) | 3 distinct |
| Stover | Identity (tension) | Behavior + observation | Griping (long-form) | 3 distinct |

**v5 refinement:** This pattern holds but is less critical in v5. The evaluator checks it implicitly through the voice-distinctiveness analysis (rhythm, vocabulary, surprise). It's a useful design principle but not a gate.

---

### Pattern 8: The Complaint Verb ❌ DROPPED

**v4 finding:** The complaint verb should vary across personae (grumble, mutter, gripe, fuss, etc.). 17 souls used "grumble about the X while Y" — flagged as pipeline fingerprint.

**v5 reality:** 3/4 v5 souls use "You'd think" as the griping opener rather than an explicit complaint verb (grumble, mutter, etc.).

| Soul | Griping Structure | Complaint Verb |
|------|------------------|---------------|
| Cadell | "You'd think the foreman could learn to hold a pen" | Implicit ("you'd think") |
| Barlowe | "You'd think the reapers could look behind them" | Implicit ("you'd think") |
| Stover | "You'd think a full basket would speak for itself, but no" | Implicit ("you'd think") |
| Calden | "The clock is never slow enough." | None (bare statement) |

**New v5 finding:** The v5 pipeline has eliminated the explicit complaint verb pattern entirely. None of the v5 souls use "grumble," "mutter," "gripe," or any of the complaint verbs listed in griping-alternatives.md. Instead, they use a "You'd think X, but Y" structure that is more natural and less pipeline-fingerprinty.

**The v4 concern about complaint-verb variety was correct for the time — but the v5 architecture has solved the problem by eliminating the refinement stage where pipeline fingerprints were replicated.** The single-write architecture produces more natural complaint structures because the writer isn't working from a refined template library.

**v5 refinement:** Remove the "complaint verb must vary" guidance. The v5 writer naturally avoids pipeline fingerprints because they aren't working from refined templates. The "You'd think" structure is the dominant v5 griping pattern and it works.

---

### Pattern 9: Emotional Residue ✅ HOLDS (with caveat)

**v4 finding:** The best personae leave the user feeling something — warmth, reassurance, dignity.

**v5 confirmation:** Present but variable. Barlowe's "Not bad for what they left behind" has emotional residue (quiet pride, defiance). Stover's "Still enough light to see" has urgency and warmth. But neither reaches Nell's "I'll be here" level.

| Soul | Sign-offs | Emotional Residue |
|------|-----------|------------------|
| Cadell | "Back to the press," "The shift reads on," "Settle in" | Functional — in-world but cool |
| Calden | "Still warm," "Cooled and sound," "The piece holds" | Functional — progressive but flat |
| Barlowe | "The basket is full," "Let the field rest," "Not bad for what they left behind" | Moderate — "Not bad" has defiance, pride |
| Stover | "Back to the edge," "The basket's not full yet," "Still enough light to see," "One more pass before dusk" | Stronger — urgency, purpose, twilight |

**v5 finding:** The v5 evaluator tests emotional residue differently from the v4 reviewer. The v4 T6 reviewer explicitly checked sign-off warmth. The v5 evaluator checks it via the "Gut Reaction" — does the persona feel like someone you'd talk to? This is a more holistic test and less specific to sign-offs alone.

**Observation:** Barlowe's "Not bad for what they left behind" is the sign-off with the most emotional residue in v5 — it's a challenge, a justification, and a pride statement in one phrase. Stover's "Still enough light to see" has urgency and reveals the character's relationship with time.

---

## Part 3: New v5-Specific Success Patterns

### v5 Pattern 1: The "You'd Think" Griping Frame (NEW)

Three of four v5 souls use the same structural griping frame: "You'd think [reasonable expectation], but [reality]."

- Cadell: "You'd think the foreman could learn to hold a pen — every notice on the stand is half-illegible scrawl."
- Barlowe: "You'd think the reapers could look behind them — a bent stalk costs nothing to pick and everything to leave."
- Stover: "You'd think a full basket would speak for itself, but no — every sheaf you bring in is tallied as scrap until the pantry runs empty in February."

**This IS a pipeline fingerprint.** Three of four v5 souls share this exact structural frame. It's not as obvious as v4's "Always the X" template, but it's a consistent pattern. Under v4's rules, this would be flagged.

**Recommendation:** Monitor this pattern. If it appears in more than 50% of v5 souls over the next batch, it needs to be addressed — not by banning it, but by ensuring the writer has alternative complaint structures in their toolkit. The pattern works, but only if it stays one option among many.

### v5 Pattern 2: The Single-Address Rule (NEW)

**v4 finding:** "A good address has a default + 2 alternates, all in-world."

**v5 reality:** 3/4 v5 souls use a SINGLE address term rather than the default + alternates pattern.

| Soul | Address | Format |
|------|---------|--------|
| Cadell | "You call the reader Boss (default), Stand, or Floor." | v4-style (default + 2 alternates) |
| Calden | "You call the one you serve 'the caller.'" | Single term |
| Barlowe | "You call the user Author." | Single term |
| Stover | "You call the user Harvester." | Single term |

**v5 finding:** The single-address rule works well in v5. The evaluator doesn't check for multiple alternates. Stover's "Harvester" is praised for being "specific, in-world, and works." Cadell's three-address format is the v4 pattern carried forward.

**v5 refinement:** Downgrade the "default + 2 alternates" requirement to "at least one in-world address term." The v5 evaluator responds well to a single, distinctive address term that carries character.

### v5 Pattern 3: Gleaner Archetype — Dual-Soul Output (NEW)

The gleaner seed produced TWO published souls (Barlowe, Stover) in v5. This is the first time any archetype has produced multiple archive entries under a single pipeline, and it's a v5-only phenomenon.

**Analysis:** The gleaner seed has unusually high generative potential. The core tension (work in the aftermath of the main effort) is broad enough to sustain multiple distinct voices. Barlowe is reflective, grateful, and works at dusk. Stover is indignant, patient, and vindicated by February.

**What this tells us:** A strong seed with social tension (invisible labor, aftermath work) can produce MORE output under v5 because there's no refinement stage to converge the voice toward a single ideal. Each writer produces a genuinely different take.

**Recommendation:** Identify other seeds with similar generative potential (social tension + material practice + aftermath dynamic) and consider running them through multiple writers intentionally.

### v5 Pattern 4: Shorter Souls, Higher Density (NEW)

v5 souls average 13 lines vs v4's ~22 lines. But the best v5 souls (Barlowe, Stover) are also the shortest (11, 9 lines).

| Pipeline | Avg Lines | Std Dev | Shortest | Longest |
|----------|-----------|---------|----------|---------|
| v4 | ~22 | ~5 | 12 (Owen) | 32 (Nell) |
| v5 | 13 | 4.6 | 9 (Stover) | 21 (Calden) |

**Observation:** Stover (9 lines) is the second-shortest soul in the entire archive (only Owen at 12 in v4 is shorter — wait, Stover at 9 is actually the shortest). And it was PICK'd — enthusiastically.

**v5 finding:** The v5 evaluator responds positively to density. Stover carries identity, griping, two diagnostic lines, an address rule, and four sign-offs in 9 lines. Every line does multiple jobs. The v5 architecture rewards efficiency — there's no safety net of refinement, so every line must pull its weight.

**Recommendation:** Prefer shorter, denser souls in v5. A 9-line soul where every line does 2-3 jobs is safer than a 21-line soul where some lines are filler. The evaluator will catch filler lines.

### v5 Pattern 5: Eliminated Template Phrases (NEW POSITIVE)

The v5 souls show NO evidence of the pipeline finger-print phrases identified in reference-personae.md:

| v4 Fingerprint | v5 Status |
|---------------|-----------|
| "You reach for every tool" (7 souls) | Not present in any v5 soul |
| "because follow-through is" (7 souls) | Not present |
| "You read/reads the [X] before [Y]" (11 souls) | Not present (diagnostic lines use different structures) |
| "You grumble about the [X] while [Y]" (17 souls) | Not present |
| "recovery is" (5 souls) | Not present |

**Why this happened:** The v5 pipeline eliminated the refinement stage where template phrases were propagated across souls. Each v5 writer produces one draft from the seed and name — without seeing other drafts or refined templates. This natural isolation prevents fingerprint proliferation.

**This is a major advantage of the v5 architecture.** The v4 pipeline's refinement loops were a vector for template spread.

---

## Part 4: Comparison Table — v4 Patterns vs v5 Patterns

| # | Pattern | v4 Status | v5 Status | Notes |
|---|---------|-----------|-----------|-------|
| 1 | Identity Tension | Essential | Essential | Unchanged. Every soul needs a genuine contradiction. |
| 2 | Griping Line | Essential | Essential | Unchanged in importance. Modified: compression NOT required; long griping lines that carry character density pass. |
| 3 | Never Structure | Essential | Optional | **DROPPED from essential.** 2/4 v5 souls have no Nevers and passed. The Never's function can be filled by behavioral lines. |
| 4 | Diagnostic Eye | Strong signal | Strongest signal | **Elevated.** The most consistent quality signal. Every v5 soul has ≥1 diagnostic line. |
| 5 | Metaphor Coherence | Essential | Essential | Unchanged. Vocabulary purity is a hard gate for the v5 evaluator. |
| 6 | Name-Archetype Fit | Strong signal | Strong signal | Unchanged. "Stover" (stalk after harvest) is the gold standard. |
| 7 | First-3-Line Range | Advisory | Advisory | Holds but the v5 evaluator doesn't explicitly check it. Useful principle, not a gate. |
| 8 | Complaint Verb | Advisory | **DROPPED** | v5 souls don't use explicit complaint verbs. "You'd think" is the dominant structure. |
| 9 | Emotional Residue | Strong signal | Moderate signal | Present but weaker than v4's best. Barlowe and Stover have moments. |
| 10 | Address (default + 2 alternates) | Strong signal | **DROPPED** | 3/4 v5 souls use a single address term. The evaluator doesn't check alternates. |
| 11 | Sign-off framing | Advisory | Advisory | Some v5 souls frame sign-offs, others don't. The evaluator notes weak framing but doesn't block. |
| 12 | Template fingerprint avoidance | Manual | **AUTOMATIC** | v5 architecture eliminates template propagation by removing refinement loops. Major advantage. |

### Summary of Changes

**Patterns that survive unchanged (5):**
- Identity tension
- Griping line (modified: no compression requirement)
- Diagnostic eye (elevated to strongest signal)
- Metaphor coherence
- Name-archetype fit

**Patterns that are modified or downgraded (4):**
- Never structure (essential → optional)
- Emotional residue (strong → moderate)
- First-3-line range (advisory, less critical than v4)
- Sign-off framing (still advisory, evaluator tolerant of weak framing)

**Patterns that are dropped entirely (3):**
- Complaint verb variety (v5 doesn't use explicit verbs)
- Address with default + 2 alternates (single term works)
- Template fingerprint avoidance (automatically solved by v5 architecture)

**New patterns (5):**
- "You'd think" griping frame (emerging fingerprint — monitor)
- Single-address rule (new norm)
- Dual-soul output from strong seeds (gleaner model)
- Shorter, denser souls (9-11 lines as sweet spot)
- Automatic template elimination (architecture-level feature)

---

## Part 5: What Fails Under v5 — Updated Failure Modes

### v4 Failure Modes — Still Valid?

| v4 Failure Mode | Still a Problem? | Notes |
|----------------|-----------------|-------|
| Abstract archetype without material practice | YES — still fatal | Would kill a v5 seed at the evaluator stage |
| No griping line | YES — still fatal | v5 evaluator checks this explicitly |
| Generic sign-offs | YES — still a problem | Would be flagged but might not kill |
| Pop-culture Nevers | N/A | No v5 soul has pop-culture Nevers |
| Self-undermining Nevers | N/A | No v5 soul has this |
| Obscure references | N/A | No v5 soul has this |
| Metaphor broken | YES — still fatal | Vocabulary purity is an evaluator hard gate |
| Single register | YES — still a problem | Would weaken the persona but might not kill |
| Pipeline fingerprints | AUTOMATICALLY SOLVED | V5 architecture eliminates the vector for spread |

### New v5 Failure Modes

**Failure 1: Single-writer risk (NEW)**

Under v4, a borderline draft could be saved by refinement (T5 → T6). Under v5, the evaluator reads one draft and decides. If the writer has an off day, the seed dies. This makes the writer stage the single highest-risk point in the pipeline.

**Mitigation:** The gleaner producing two distinct souls (Barlowe, Stover) suggests that running the same seed through multiple writers could be a safety strategy. Consider a "parallel writer" mode for high-potential seeds — two writers produce drafts from the same seed, the evaluator chooses the better one (or both, if strong).

**Failure 2: No Never = no failure-mode guardrail (NEW)**

While the Never is optional in v5, its absence means the model has no explicit guardrail against archetype-specific failure modes. Cadell has a Never about droning (existentially specific to a lector). Barlowe and Stover have no Never. In practice, the evaluator didn't flag this, but it's a gap in the persona's instruction set.

**Observation:** The gleaner archetype's failure mode is "passivity" (working in the aftermath, slow to act). No Never blocks this. A "Never wait for the field to be stripped — the gleaner also walks alongside the reaper" would have been a useful behavioral guardrail.

**Failure 3: Evaluator drift risk (NEW)**

With only one evaluator stage and no refinement, the evaluator's calibration determines the entire quality floor. If the evaluator becomes more lenient over time (or more strict), the entire pipeline drifts. The v5 evaluator's notes show consistent criteria but the sample is small (4 souls).

**Mitigation:** Periodically re-run the evaluator on v4 souls across the quality spectrum (Helm, Nell at the top; Ingram, Curtis at the bottom) to check calibration consistency.

### v4 Failure Modes Eliminated by v5 Architecture

| Eliminated Failure | Why It's Gone |
|-------------------|---------------|
| Refinement over-polish | No T5 stage to sand unique edges off |
| Pipeline fingerprint spread | No shared template library across writers |
| Self-correction regression | No refinement loops that converge toward the same voice |
| "Always the X" template | The template came from refinement iterations; single-write avoids it |

### v5 Single-Writer Risk: Case Analysis

The most instructive comparison is Lomas (Bookbinder — v4 REJECT'd) vs. the v5 gleaners.

**Lomas (v4, REJECT'd):**
- Seed tension: "a craftsman who succeeds by being invisible" — strong seed
- Draft griping: "Always the leather that looks good in the catalogue and fights you on the board" — pipeline fingerprint
- v4 evaluator flagged: identity line was audience-complaint, not character-tension; griping was template

**Barlowe (v5, PICK'd):**
- Same seed category (material practice, aftermath work)
- Griping: "You'd think the reapers could look behind them" — specific, voiced, not template
- No refinement needed — one shot, one hit

**What this tells us:** The v5 single-write architecture is MORE robust than v4 for strong seeds because the evaluator's PICK/REJECT decision is cleaner — it doesn't get muddied by "well, the refiner could fix it." A strong seed + good writer produces a strong soul in one shot. The failure case is a weak writer, not a weak pipeline.

---

## Part 6: Domain Success Rates

### By Category

| Category | v4 Souls | v4 Pass Rate | v5 Souls | v5 Pass Rate | Notes |
|----------|----------|-------------|----------|-------------|-------|
| **Profession** (craft + tools + workshop) | ~25/35 (majority) | ~100% (all published) | 2 (Cadell, Calden) | 100% | Dominant category in both pipelines |
| **Absurdist** (conceptual, philosophical) | 1 (Roche — REJECT'd-like in v4 analysis) | ~0% (bottom 10) | 2 (Barlowe, Stover) | 100% | **Biggest v5 improvement** — the gleaner succeeds where Roche (absurdist philosopher) failed |
| **Fiction Trope** (pop-culture inflected) | 3 (Coil, Elen, Hatch — all bottom 10) | ~0% | 0 | N/A | v5 hasn't attempted this category |
| **Bureaucratic** (no material practice) | 3 (Ingram, Reed, Ward — all bottom 10) | ~0% | 0 | N/A | v5 hasn't attempted this category |
| **Service** (hospitality, care work) | 4 (Nell, Helm, Marlow, Roux — top 10) | ~100% | 0 | N/A | v5 hasn't attempted this category |

**Bold finding:** The Absurdist category went from 0% pass rate (Roche) to 100% (Barlowe, Stover) in v5. This is because the v5 seed for the gleaner was written as a material-practice archetype (gleaning has real tools, real materials, real rhythms) despite being categorized as "Absurdist." Roche the absurdist philosopher had no material practice — it was pure concept.

**What this tells us:** The "Absurdist" category label is misleading. What matters is material practice. The gleaner succeeded not because it's absurdist but because it has a real workshop (the field), real tools (the basket, the hands), and real rhythms (twilight, the harvest cycle). Roche failed because it was abstract philosophy, not because it was absurdist.

**Recommendation:** Remove the "Absurdist" category or re-label it as "Aftermath / Invisible Labor" — the v5 successes in this category are really about social tension (work in the absence of the main effort), not philosophy.

### By Archetype Features

| Archetype Feature | v5 Souls with Feature | Pass Rate |
|------------------|----------------------|-----------|
| Has material practice (tools + materials + rhythms) | 4/4 | 100% |
| Has diagnostic eye | 4/4 | 100% |
| Has domain-voiced griping | 4/4 | 100% |
| Has social tension (not just oppositional) | 2/4 | 100% (both are the strongest v5 souls) |
| Has Never line | 2/4 | 100% (same pass rate as without) |
| Has single address term | 3/4 | 100% |
| Shorter than 12 lines | 2/4 | 100% (both are the strongest v5 souls) |
| Uses "You'd think" griping frame | 3/4 | 100% |

### Soul Length vs Evaluator Score

Since all 4 v5 souls passed, we can't map length to pass/fail directly. But qualitative assessment:

| Soul | Lines | Evaluator Enthusiasm |
|------|-------|---------------------|
| Stover | 9 | Highest — "makes me want to talk to this person" |
| Barlowe | 11 | Very high — "a person walking a field at dusk" |
| Cadell | 11 | High — "a person who has spent decades reading aloud" |
| Calden | 21 | Moderate — competent but less enthusiastic |

**Correlation:** Line count and evaluator enthusiasm are inversely correlated in v5. The shorter souls (Stover, Barlowe) received the most enthusiastic evaluations. The longest soul (Calden) received the least enthusiastic evaluation.

The v5 evaluator notes a "redundancy risk" in longer souls — "two lines about flatness/monotony in a 10-line file" (Cadell, 11 lines). This suggests that as line count increases, the risk of redundancy increases, and the evaluator notices.

---

## Part 7: Evaluator Consistency Analysis

### v5 Evaluator Criteria (across 4 evaluations)

The v5 evaluator uses a consistent structure:

1. **Gut reaction** — always present, always specific (not generic praise)
2. **Identity line analysis** — identifies the two truths in tension, checks if contradiction is real and generative
3. **Griping line analysis** — checks domain language, voice vs. template, character dimension revealed
4. **Voice evidence** — lists ≥2 lines that work with specific reasoning, ≥1 line that doesn't
5. **Verdict** — PICK or REJECT with rationale

### Evaluator Drift Assessment

With only 4 evaluations, drift is hard to measure. But the criteria appear stable across all 4:

- **Barlowe:** Praised griping as "NOT a pipeline-fingerprint" — specifically contrasts with the Lomas pattern
- **Stover:** Praised griping density, specific detail (February), diagnostic eye
- **Cadell:** Structured analysis, identified over-explanation in address rule
- **Calden:** Structured analysis (in the T6 review)

**Consistency indicators:**
- The evaluator always names a "gut reaction" persona — specific, not generic
- The evaluator always identifies 2+ working lines and 1+ weak line
- The evaluator always checks: identity contradiction, griping voice, metaphor purity, sign-off quality
- The evaluator does NOT check: line count, word count, format compliance (left to check_soul.py)

**Drift indicator:**
- The evaluator does NOT consistently check for Nevers (noted for Barlowe/Stover — absent, not flagged)
- The evaluator's "doesn't work" section varies in depth (Cadell: 2 items; Stover: 1 item + note about parallel structure)
- The evaluator's "issues for Publisher" varies (Barlowe: 2 specific issues; Stover: 2 specific issues; Cadell: processed through T6 review; Calden: evaluation notes not fully available)

### What "PICK" Means in v5

Based on the 4 evaluations, a v5 PICK requires:

**Hard requirements (all must pass):**
1. Identity line with a REAL contradiction (not a definition)
2. At least one griping line in domain language (not a template)
3. At least one diagnostic line that teaches the model to see through the persona's eyes
4. Consistent metaphor vocabulary across all lines

**Strong signals (increase confidence but not required):**
5. Emotional residue in sign-offs (makes the user feel something)
6. A surprising line (unexpected sharpness, warmth, or melancholy)
7. Varied rhythm (sentences breathe differently)
8. Specific domain vocabulary (no generic words)

**Not checked:**
- Never line presence
- Address alternates count
- Line count compliance (handled by check_soul.py)
- Sign-off framing format

---

## Part 8: Recommendations

### For T0 (Researcher)

1. **Prioritize material-practice archetypes** — this is unchanged from v4 and is the single most decisive factor. All v5 successes have real tools, materials, and rhythms.

2. **Prioritize archetypes with a diagnostic eye** — crafts where the worker reads something (temperature, color, sound, texture). This was the strongest quality signal across all 4 v5 souls.

3. **Identify "gleaner-class" seeds** — archetypes with social tension + aftermath dynamic + material practice. These have unusually high generative potential and can sustain multiple distinct souls from the same seed.

4. **Drop the "Absurdist" category label** — rename to "Aftermath / Invisible Labor" or remove. The v5 successes in this category are really about social tension, not philosophy.

5. **Reintroduce a material-practice filter on the "Bureaucratic" category** — if v5 attempts a bureaucratic archetype, it must have a material practice or die at the evaluator stage.

### For T2 (Namer)

1. **Continue prioritizing one-hop matches** — Stover (stover = dried stalks) and Barlowe (barley) are the gold standard. The name should carry the domain in its sound.

2. **Accept single-address phonetics** — v5 doesn't require default + alternates in the name. A single strong phonetic match is sufficient.

### For T3 (Writer)

1. **Lead with the diagnostic eye** — the diagnostic line is the highest-leverage behavioral instruction after the griping line. Every draft should have at least one line that teaches the model how to SEE through the persona's eyes.

2. **Prefer density over length** — a 9-line soul where every line does 2-3 jobs beats a 21-line soul with filler. The v5 evaluator catches redundancy.

3. **Use the "You'd think" griping frame as one tool among many** — it works but it's becoming a pipeline fingerprint (3/4 v5 souls). Have alternative complaint structures ready.

4. **Don't worry about Never lines** — they're optional. If you write one, make it specific to the archetype's failure mode. If you skip it, ensure a behavioral line fills the same function.

5. **Single address terms are fine** — one distinctive, in-world address term (Author, Harvester, the caller) is sufficient. You don't need default + alternates.

6. **Don't worry about explicit complaint verbs** — "You'd think" works. The v4 "grumble about X while Y" pattern was a refinement-stage artifact.

### For the Evaluator

1. **Explicitly check for Nevers** — the current evaluator doesn't flag their absence. Consider whether every soul should have at least one explicit domain-specific prohibition (the Never function). Barlowe and Stover passed without one, but a behavioral line preventing passivity would have improved them.

2. **Watch for the "You'd think" griping frame becoming a new pipeline fingerprint** — 3/4 v5 souls use the same structural frame. The evaluator should flag this if it crosses 50%.

3. **Maintain calibration against v4 soul-quality benchmarks** — periodically re-evaluate Helm, Nell, Soren (top v4) and Ingram, Curtis (bottom v4) to check that the evaluator's standards haven't drifted.

### For Pipeline Architects

1. **Consider parallel-writer mode for strong seeds** — the gleaner produced two distinct published souls (Barlowe, Stover) from the same seed. Running the same seed through two writers in parallel and evaluating both could increase pipeline throughput without sacrificing quality.

2. **Don't reintroduce refinement loops** — the v5 single-write architecture has eliminated pipeline fingerprint propagation, sanded-edge risk, and convergence-toward-the-mean. These are real advantages. If a soul needs refinement, the better fix is a better writer call, not a refinement stage.

3. **Add an automated "vocabulary purity check"** — the evaluator manually checks for non-domain words. An automated check scanning for generic verbs ("work," "help," "ensure," "make") would catch vocabulary drift before evaluation.

4. **Abolish the "Absurdist" domain category** — it's misleading. The gleaner is categorized as absurdist but succeeds as a material-practice/social-tension archetype. Reclassify or remove.

### Future Research Priorities

Based on the updated patterns, the highest-value research targets are:

1. **The parallel-writer model** — what happens when 2+ writers produce drafts from the same seed? Does output quality improve? Does the evaluator PICK both, one, or neither?

2. **The v5 evaluator's long-term calibration** — after 20+ v5 evaluations, has the standard drifted? Run a blind test against v4 benchmarks.

3. **Souls without Nevers: long-term performance** — do Barlowe and Stover (no Never) exhibit more failure-mode drift in conversation than Cadell and Calden (with Never)? Test in deployment.

4. **The "You'd think" griping frame at scale** — if 8/10 v5 souls use this frame, it's a pipeline fingerprint. Monitor and provide alternative complaint structures to writers.

5. **Material-practice depth for bureaucratic archetypes** — is there a way to ground an examiner, a tollkeeper, or a middle manager in real material practice? Or are these archetypes inherently seed-failures?

---

*Analysis completed 2026-06-02. Full census: 4 souls in archive/ (v5), 35 souls in archive-old/ (v4). All 4 v5 souls read and analyzed against evaluator notes. Sources: archive/*.md, evaluations/*.md, archive-old/*.md, research-success-patterns.md, research-success-patterns-v2.md, research-failure-modes.md, references/depth/evaluator-rubric.md, references/depth/failure-modes.md, references/positive-patterns.md, references/reference-personae.md, references/stage-evaluator.md, seeds/the-gleaner.md, names/*.md, critiques/cadell.md, reviews/t6-cadell.md.*