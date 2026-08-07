# Depth Reference: Failure Modes

Three lines, three distinct ways a persona dies — each at a different stage:

> "You are a facilitator. You streamline processes and ensure stakeholder alignment." (T0: no workshop, no materials, no craft — the writer defaults to jargon)
> "Never be like Deadpool — you take no shortcuts." (Writer: pop-culture Never — the reference does the work that domain vocabulary should do)
> "Your sign-offs close the transaction: 'Receipt issued.' 'Logged.' 'Filed.'" (Writer: stamps, not conversation — the user carries nothing away)

Each of these lines fails for a reason a stage operator can name and catch — that is what makes the failure preventable.

**Core principle:** Bottom-rated personae don't fail for one big reason — they fail for specific, preventable reasons at specific pipeline stages. Understanding why the bottom 10 failed lets each stage operator catch and fix issues before they compound.

**What doesn't work:** the repair that misses the mode — "You care deeply about quality and always strive to do your best." It passes a naive "is there a value?" check, but it voices nothing: no craft, no metaphor, no person. A fix that doesn't fix is just a new failure mode.

---

## What the Research Says (Key Findings)

Root cause analysis of the 10 lowest-rated archived personae identified 21 distinct failure modes across 5 categories. The same 5 root causes account for 80% of bottom-10 failures:

### The Five Root Causes

| # | Root Cause | Personae Affected | Stage |
|---|------------|-------------------|-------|
| 1 | **Archetype has no material practice** | Silver, Reed, Ingram, Ward | T0 (Seed) |
| 2 | **No vitality line (no inner-life channel at all)** | Ingram, Curtis, Ward | Writer |
| 3 | **Sign-offs are stamps, not conversation** | Coil, Reed, Curtis, Hatch, Ward, Silver | Writer |
| 4 | **Nevers are pop-culture, obscure, or self-undermining** | Coil, Roche, Silver, Hayes | Writer |
| 5 | **Metaphor broken or absent** | Coil, Reed | Writer |

### Failure Mode Taxonomy by Stage

#### T0 — Seed Failures (Researcher)

| Failure | Personae | Why It Matters |
|---------|----------|----------------|
| **Abstract archetype without material practice** | Silver, Reed, Ingram, Ward | Without a workshop (tools, materials, rhythms, failure modes), the writer has nothing to ground the voice in. The persona defaults to procedural language, corporate jargon, or genre clichés. |
| **Archetype without a natural vitality source** | Ingram, Curtis, Ward | Some roles are defined by absence (impartial = no opinion, executioner = no emotion, tollkeeper = no agency). If the archetype doesn't have natural friction, the writer manufactures generic complaints. |
| **Name-archetype mismatch** | Silver, Coil | "Silver" sounds precious for a working-class role. "Coil" sounds abstract for a human role. The name is the first signal — if it doesn't fit, the persona starts wrong. |

**Prevention at T0:**
- **Material practice check:** Ask "Does this archetype have specific tools, materials, rhythms, and failure modes?" If no, develop the world at seed time — a world with its own nouns and verbs is one of the no-pulse essentials (stage-researcher.md Step 4, Kill 3).
- **Vitality check:** Ask "What would this person carry inner life about — a complaint, a quiet pride, a protectiveness?" If you can't answer, develop it at seed time; the channel is the character's choice (v5.2.1).
- **Diagnostic language check:** Ask "Does this craft involve reading something (wick, color, noise, temperature)?" If no, the writer will struggle to create a diagnostic line — develop a way of seeing at seed time.

#### Writer — Writing Failures

| Failure | Personae | Why It Matters |
|---------|----------|----------------|
| **No vitality line** | Ingram, Curtis, Ward | No inner-life channel — no complaint, no quiet pride, no protectiveness — the persona reads as function, not person. Vitality may ride any channel (v5.2.1); what matters is that a line carries awareness + standards + investment + expertise + tension in world language. |
| **Generic sign-offs (stamps, email closings, catchphrases)** | Coil, Reed, Curtis, Hatch, Ward, Silver | The writer defaulted to what the persona "does" (closes sales, sends emails) instead of what the persona would say. |
| **Pop-culture Nevers without explanation** | Coil, Roche, Silver | The writer couldn't find a domain-specific failure mode, so they reached for pop-culture. These waste tokens and confuse the model. |
| **Self-undermining Nevers** | Hayes, Hatch | "Never settle into a voice so Western it plays as costume" tells the model to be less of the archetype. Undermines confidence. |
| **Obscure references** | Silver | "Never Elam" — the model has no idea who Elam is. A Never the model can't parse is worse than no Never. |
| **Breaks in metaphor coherence** | Coil, Reed | Mixing laboratory, electrical, and literary references (Coil) or corporate, military, and pop-culture metaphors (Reed) without committing to any. |
| **Single register in first 3 lines** | Ingram, Curtis | First 3 lines all procedural, all clinical. No range established. |

**Prevention at the Writer stage:**
- Require a vitality line in the draft template — complaint, quiet pride, protectiveness, whimsy, any channel — but never mandate complaint specifically (v5.2.1).
- Apply the **conversational test** to sign-offs: "Would a real person say this when leaving?"
- Apply the **recognizability test** to Nevers: "Would a general-educated reader recognize this reference?"
- Apply the **self-undermining test** to Nevers: "Does this tell the model to be less of the archetype?"
- Maintain **one metaphor family** across all lines. If a line could be from another archetype, rewrite it.

#### Evaluator — Review Failures

| Failure | Personae | Why It Matters |
|---------|----------|----------------|
| **Missing catch: no vitality line** | Ingram, Curtis, Ward | The severity hierarchy lists this as critical, but the reviewer didn't flag it. If the reviewer misses it, the Publisher doesn't fix it. |
| **Missing catch: stamp sign-offs** | Reed, Curtis, Ward | Reviewer should have flagged "Generic sign-offs" as critical but didn't. |
| **Missing catch: generic/pop-culture Nevers** | Coil, Roche, Silver | Reviewer should have flagged these as significant but didn't. |

**Prevention at the Evaluator stage:**
- The severity hierarchy already exists — the fix is **calibration**. The reviewer needs concrete examples of what each failure looks like in practice (provided in this file).
- Use the **seven diagnostic signals** in evaluator-rubric.md as reading lenses — the verdict stays a judgment, not a checklist.

#### Publisher — Scoped Fix Failures

| Failure | Personae | Why It Matters |
|---------|----------|----------------|
| **Missing fix: no vitality line** | Ingram, Curtis, Ward | The evaluator flagged the missing inner-life channel but the fix didn't land. Vitality may ride any channel (v5.2.1); the fix is a line carrying awareness + standards + investment + expertise + tension in world language. |
| **Missing fix: stamp sign-offs** | Reed, Curtis, Coil, Hatch | The evaluator flagged stamps but the published soul keeps the generic close. |
| **Missing fix: generic/pop-culture Nevers** | Coil, Roche, Silver, Hayes | The evaluator flagged them but they shipped unchanged. |

**Prevention at the Publisher stage:**
- Fix ONLY what was flagged, with the minimum changes necessary (stage-publisher: no open-ended improvement, no rewriting the character; "fix these 3 things" means exactly 3 changes).
- Each flagged issue gets one scoped fix; run `check_soul.py`, publish, and stop. There is no priority list beyond the flagged issues.

#### Systemic Failures (Pipeline)

| Failure | Prevention |
|---------|------------|
| Pipeline doesn't enforce vitality | check_soul.py must NEVER require complaint patterns — v5.2.1 removed the griping regex engine because it force-fed "always the X" fingerprints into every soul; vitality is Evaluator-judged, any channel. |
| Pipeline doesn't enforce sign-off warmth | Forbidden — check_soul.py must never enforce creative patterns (v5.2.1; see check_soul.py:91–96). Sign-off warmth is Evaluator territory, not a regex. |
| Pipeline doesn't enforce name-archetype fit | Add name-archetype fit check at the Namer stage — name should sound like the craft. |
| Pipeline doesn't enforce metaphor coherence | Add metaphor coherence check at the Evaluator stage — "Could any other archetype have this line?" |
| Pipeline doesn't enforce first-3-line register range | Add register range check at the Evaluator stage — "Do the first 3 lines establish at least 2 distinct registers?" |

---

## How to Apply It (Pipeline Integration)

### For Each Stage Operator

**If you are T0 (Researcher):**
- Run the Three-Kills Audit (stage-researcher.md Step 4) before committing to a seed: not-a-someone, not-relational, no-pulse. A workshop with tools, materials, rhythms, and failure modes is one of the no-pulse essentials — if thin, develop it at seed time.
- Run the Vitality Test: can you hear a line only this character could say — a complaint, a quiet pride, a protectiveness, a whimsy — any channel? If not, develop one at seed time.
- Develop a diagnostic way of seeing at seed time — crafts that involve reading something (wick, color, noise, temperature, texture) supply it naturally.

**If you are the Writer:**
- Your first line must have a contradiction. After that, ordering is voice (v5.2.2): the vitality line — a complaint, a quiet pride, a whimsy — sits where it belongs, and behavior lands where the character's voice puts it (ordering is voice — format-rules.md:41).
- Every sign-off must pass the Conversational Test. If you wouldn't say it to a coworker at the end of a shift, rewrite it.
- Every Never must pass the Recognizability Test. If a general-educated reader wouldn't know the reference, replace it.

**If you are the Evaluator:**
- Weigh the draft against the seven diagnostic signals in evaluator-rubric.md — lenses, not gates. No signal blocks advancement on its own; the verdict is judgment, not checkbox scoring (stage-evaluator: "not here to check boxes").
- Signals 1–3 (vitality, identity tension, sign-off warmth) are the ones most worth flagging — if weak, name them as fixable issues (a total absence of vitality is a hard rejection signal).
- Signals 4–6 (diagnostic eye, metaphor coherence, Never quality) — note them.
- Signal 7 (first-3-line range) — mention only if relevant.

**If you are the Publisher (scoped fixes):**
- Fix ONLY what was flagged — no open-ended improvement, no rewriting the character ("fix these 3 things" means exactly 3 changes). If the critique doesn't mention a gap, it is not in scope.

**If you are the Publisher (final verification):**
- Verify each flagged issue is actually resolved in the published file, then run `check_soul.py` and publish.
- If more fixes are needed after the FLAG path, there is no re-entry loop — the Publisher applies the flagged fixes and publishes (stage-publisher).

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
Ingram (Impartial Examiner) reads like a procedure manual. The writer confused professional distance with emotional void. A persona can be professional AND have personality. Moulden is professional ("The wick tells you everything") AND has personality ("knowing no one thinks about the rendering yard"). Procedural language is the enemy of personality.

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
| "You mutter about the warrant" | Procedural complaint, not voiced | Not a checker job — the Evaluator asks whether the vitality line sits in the persona's metaphor family (check_soul.py must never enforce creative patterns — v5.2.1; check_soul.py:91–96) |
| "Closed." / "The record is entered." / "The docket is current." | Sign-offs pass the presence check, all stamps | Sign-off warmth — would a person say this? |
| Silver, Coil (names) | Passes no automated name check | Name-archetype fit — does the name sound like the craft? |
