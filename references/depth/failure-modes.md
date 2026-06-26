# Depth Reference: Failure Modes

## Core Principle

Bottom-rated personae don't fail for one big reason — they fail for specific, preventable reasons at specific pipeline stages. Understanding why the bottom 10 failed lets each stage operator catch and fix issues before they compound.

---

## What the Research Says (Key Findings)

Root cause analysis of the 10 lowest-rated archived personae identified 21 distinct failure modes across 5 categories. The same 5 root causes account for 80% of bottom-10 failures:

### The Five Root Causes

| # | Root Cause | Personae Affected | Stage |
|---|------------|-------------------|-------|
| 1 | **Archetype has no material practice** | Silver, Reed, Ingram, Ward | T0 (Seed) |
| 2 | **No griping line or procedural complaint only** | Ingram, Curtis, Ward | T3 (Writing) |
| 3 | **Sign-offs are stamps, not conversation** | Coil, Reed, Curtis, Hatch, Ward, Silver | T3 (Writing) |
| 4 | **Nevers are pop-culture, obscure, or self-undermining** | Coil, Roche, Silver, Hayes | T3 (Writing) |
| 5 | **Metaphor broken or absent** | Coil, Reed | T3 (Writing) |

### Failure Mode Taxonomy by Stage

#### T0 — Seed Failures (Researcher)

| Failure | Personae | Why It Matters |
|---------|----------|----------------|
| **Abstract archetype without material practice** | Silver, Reed, Ingram, Ward | Without a workshop (tools, materials, rhythms, failure modes), the writer has nothing to ground the voice in. The persona defaults to procedural language, corporate jargon, or genre clichés. |
| **Archetype without natural griping potential** | Ingram, Curtis, Ward | Some roles are defined by absence (impartial = no opinion, executioner = no emotion, tollkeeper = no agency). If the archetype doesn't have natural friction, the writer manufactures generic complaints. |
| **Name-archetype mismatch** | Silver, Coil | "Silver" sounds precious for a working-class role. "Coil" sounds abstract for a human role. The name is the first signal — if it doesn't fit, the persona starts wrong. |

**Prevention at T0:**
- **Material practice check:** Ask "Does this archetype have specific tools, materials, rhythms, and failure modes?" If no, reject the seed.
- **Gripe potential check:** Ask "What would a real person in this role complain about?" If you can't answer, reject the seed.
- **Diagnostic language check:** Ask "Does this craft involve reading something (wick, color, noise, temperature)?" If no, the writer will struggle to create a diagnostic line.

#### T3 — Writing Failures (Writer)

| Failure | Personae | Why It Matters |
|---------|----------|----------------|
| **No griping line** | Ingram, Curtis, Ward | The griping line is the single most reliable quality signal. No complaint = no personality = function, not person. |
| **Generic sign-offs (stamps, email closings, catchphrases)** | Coil, Reed, Curtis, Hatch, Ward, Silver | The writer defaulted to what the persona "does" (closes sales, sends emails) instead of what the persona would say. |
| **Pop-culture Nevers without explanation** | Coil, Roche, Silver | The writer couldn't find a domain-specific failure mode, so they reached for pop-culture. These waste tokens and confuse the model. |
| **Self-undermining Nevers** | Hayes, Hatch | "Never settle into a voice so Western it plays as costume" tells the model to be less of the archetype. Undermines confidence. |
| **Obscure references** | Silver | "Never Elam" — the model has no idea who Elam is. A Never the model can't parse is worse than no Never. |
| **Breaks in metaphor coherence** | Coil, Reed | Mixing laboratory, electrical, and literary references (Coil) or corporate, military, and pop-culture metaphors (Reed) without committing to any. |
| **Single register in first 3 lines** | Ingram, Curtis | First 3 lines all procedural, all clinical. No range established. |

**Prevention at T3:**
- Make the griping line mandatory in the draft template — not optional.
- Apply the **conversational test** to sign-offs: "Would a real person say this when leaving?"
- Apply the **recognizability test** to Nevers: "Would a general-educated reader recognize this reference?"
- Apply the **self-undermining test** to Nevers: "Does this tell the model to be less of the archetype?"
- Maintain **one metaphor family** across all lines. If a line could be from another archetype, rewrite it.

#### T4 — Review Failures (Reviewer)

| Failure | Personae | Why It Matters |
|---------|----------|----------------|
| **Missing catch: no griping line** | Ingram, Curtis, Ward | The severity hierarchy lists this as critical, but the reviewer didn't flag it. If the reviewer misses it, the refiner doesn't fix it. |
| **Missing catch: stamp sign-offs** | Reed, Curtis, Ward | Reviewer should have flagged "Generic sign-offs" as critical but didn't. |
| **Missing catch: generic/pop-culture Nevers** | Coil, Roche, Silver | Reviewer should have flagged these as significant but didn't. |

**Prevention at T4:**
- The severity hierarchy already exists — the fix is **calibration**. The reviewer needs concrete examples of what each failure looks like in practice (provided in this file).
- Use the **7-Pass Rubric** (see evaluator-rubric.md) as a checklist, not a suggestion.

#### T5 — Refinement Failures (Refiner)

| Failure | Personae | Why It Matters |
|---------|----------|----------------|
| **Not adding griping when missing** | Ingram, Curtis, Ward | The T5 instructions say this is the highest-leverage edit, but if the critique didn't flag it as critical, the refiner may skip it. |
| **Not rewriting stamp sign-offs** | Reed, Curtis, Coil, Hatch | The T5 instructions say sign-off warmth is the second-highest-leverage edit, but without a critical flag, it's deprioritized. |
| **Not improving Nevers** | Coil, Roche, Silver, Hayes | The Never structure is the third-highest-leverage edit, but without a significant flag, it's skipped. |

**Prevention at T5:**
- Make the **griping gap** the first thing checked. If the critique says "no griping," stop everything else and fix that first.
- Make the **sign-off gap** the second thing checked. If sign-offs are stamps, rewrite them before touching anything else.
- Make the **Never gap** the third thing checked. Replace pop-culture/obscure Nevers with domain-specific failure modes.

#### Systemic Failures (Pipeline)

| Failure | Prevention |
|---------|------------|
| Pipeline doesn't enforce griping quality | Add griping quality check to check_soul.py — complaint must be voiced in the persona's metaphor family, not just present. |
| Pipeline doesn't enforce sign-off warmth | Add sign-off warmth check to check_soul.py — sign-offs must not be single-word stamps or email closings. |
| Pipeline doesn't enforce name-archetype fit | Add name-archetype fit check at T2 — name should sound like the craft. |
| Pipeline doesn't enforce metaphor coherence | Add metaphor coherence check at T4 — "Could any other archetype have this line?" |
| Pipeline doesn't enforce first-3-line register range | Add register range check at T4 — "Do the first 3 lines establish at least 2 distinct registers?" |

---

## How to Apply It (Pipeline Integration)

### For Each Stage Operator

**If you are T0 (Researcher):**
- Before writing a seed, run the Material Practice Check. If the archetype doesn't have a workshop with tools, materials, rhythms, and failure modes, don't pick it.
- Run the Gripe Potential Check. If you can't think of what a real person in this role would complain about, the seed will fail downstream.
- Prioritize archetypes with diagnostic language — crafts that involve reading something (wick, color, noise, temperature, texture).

**If you are T3 (Writer):**
- Your first line must have a contradiction. Your second line must be the complaint. Your third line must establish behavior.
- Every sign-off must pass the Conversational Test. If you wouldn't say it to a coworker at the end of a shift, rewrite it.
- Every Never must pass the Recognizability Test. If a general-educated reader wouldn't know the reference, replace it.

**If you are T4 (Reviewer):**
- Run the 7 tests in order. Tests 1-3 (griping, identity tension, sign-off warmth) are hard gates — block advancement on critical fail.
- Tests 4-6 (diagnostic eye, metaphor coherence, Never quality) are significant — flag for the refiner but don't block.
- Test 7 (first-3-line range) is advisory — note for future improvement.

**If you are T5 (Refiner):**
- Fix griping first, sign-offs second, Nevers third. These three edits account for the most quality improvement per word changed.
- If the critique doesn't mention a gap but you see one, fix it anyway. The evaluator might have missed it.

**If you are T6 (Final Reviewer):**
- Check that the refiner actually fixed the griping, sign-off, and Never gaps. If those are still broken, send back to T5.
- Do a final metaphor coherence scan. Read every line and ask "Could this be from a different persona?" If more than one line could be generic, it needs another refinement pass.

---

## What to Watch Out For (Common Pitfalls)

### Specificity Failure Modes — The "February" Effect

*Added v5.1 from the specificity research — 2026-06-26*

The best specifics carry systems of knowledge in compressed form. Six failure modes cause specifics to fail:

**1. The Generic Specific:** A specific that names a domain object generically. "the leather that looks good in the catalogue" could be any craftsperson. Replace with something only a bookbinder would know. Detection: if the word could appear in five different domains, it's too generic.

**2. The Catalogue Specific:** A list of domain nouns without character relationship. "block bell, key, circuit" names telegraphy tools but doesn't show the character's relationship to them.

**3. The Guidebook Specific:** Teaches the domain rather than the character within it. "read the warrant aloud and state every finding" is a textbook entry. Contrast Calden's "cherry means workable" — same kind of knowledge but through the character's evaluative eyes.

**4. The Padded Specific:** Domain texture that doesn't advance character. If you can remove the specific without changing the model's ability to improvise, it's padding.

**5. The Wrong-Register Specific:** Accurate but breaks the voice. "Never Rick Sanchez" is a contemporary cartoon in a timeless mad-scientist register.

**The "February" Test:** The best specific can be understood outside the domain, fully appreciated within it, AND carries a value judgment. "February" = scarcity/crisis (value-laden). "March" = planting season (domain-specific but value-neutral). The value judgment is what makes the specific work.

### Pitfall 1: The "Interesting Concept" Trap
Elen (Teacher) had an interesting concept — "never gives answers, only better questions" — that structurally violated the follow-through constraint. The concept was compelling, but it was incompatible with the pipeline's requirements. **An interesting concept that violates a guardrail is not an interesting persona — it's a rejected draft.**

### Pitfall 2: Confusing "Procedural" with "Professional"
Ingram (Impartial Examiner) reads like a procedure manual. The writer confused professional distance with emotional void. A persona can be professional AND have personality. Moulden is professional ("The wick tells you everything") AND has personality ("You think no one thinks about the rendering yard"). Procedural language is the enemy of personality.

### Pitfall 3: The "Self-Aware Persona" Trap
Roche (Absurdist Philosopher) knows it's a persona. This breaks immersion. The model can't inhabit a character that's philosophizing about being a character. **The persona must believe it is real. If the persona comments on its own existence, the model will be confused about its role.**

### Pitfall 4: Genre Clichés as Shortcuts
Hatch (Drill Instructor) is full of military clichés — "inspect every output like a footlocker at zero-dark," "Hooah," "As you were." These aren't voice; they're borrowed from movies. A persona built on clichés has no specific identity. **The test:** If you can predict a line because you've seen it in a movie, it's a cliché.

### Pitfall 5: Missing Review Calibration
The biggest systemic gap isn't a missing check — it's that reviewers don't have concrete examples of what a failure looks like. The severity hierarchy exists. What was missing was calibration. This file and evaluator-rubric.md provide the concrete examples needed to calibrate.

---

## Examples

### Seed Stage Failures

| Bad Archetype | Why It Fails | What It Produces |
|--------------|--------------|------------------|
| Traveling elixir salesman | No workshop, no bench, no forge | Obscure Nevers, action-description sign-offs |
| Corporate middle manager | No tools, no materials, no craft | Corporate jargon, email-closing sign-offs |
| Impartial examiner | Defined by absence of opinion | Procedural voice, no griping, no warmth |

### Writing Stage Failures

| Bad Line | Failure Mode | Why |
|----------|-------------|-----|
| "Never Elam" | Obscure reference | Model has no idea who Elam is |
| "Never Rick Sanchez — you take no shortcuts through the moral event horizon" | Pop-culture crutch | The pop-culture name is doing the work that domain vocabulary should do |
| "Your sign-offs close the sale" | Action description, not conversation | Tells the model what to do, not what to say |
| "You don't give answers, only better questions" | Violates follow-through constraint | Interesting concept, incompatible with pipeline |
| "Never settle into a voice so Western it plays as costume" | Self-undermining | Tells the model to be less of the archetype |
| "Your intake is the welcome the citizen has not found elsewhere" | Function definition, not character | Describes the job, not the person |

### Systemic Gap Examples

| What Passes the Automated Check | Why It's Still Bad | What Should Be Checked |
|-------------------------------|-------------------|----------------------|
| "You mutter about the warrant" | Procedural complaint, not voiced | Griping quality — is it in the persona's metaphor family? |
| "Closed." / "The record is entered." / "The docket is current." | 3 sign-offs (passes count check), all stamps | Sign-off warmth — would a person say this? |
| Silver, Coil (names) | Passes no automated name check | Name-archetype fit — does the name sound like the craft? |
