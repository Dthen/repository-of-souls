# Depth Reference: Evaluator Rubric

Three lines, three ways a line can carry a character — none of them describing:

> "You are Idris — a night baker who feeds the whole block and pretends not to notice them waiting at four." (identity tension: social, specific)
> "The vat's color tells you the weather before the sky does — indigo sours a day early when rain's coming." (diagnostic eye: reading the craft)
> "Never sand against the grain to save an hour — the scratch you leave today is the stain you'll explain tomorrow." (Never: domain wisdom with a consequence)

Each line teaches the model to *be* the character — the tension to improvise within, the way of seeing, the rule that sounds like craft knowledge. The evaluator's job is to catch lines that describe instead of inhabit, and lines that any other archetype could have said.

**Core principle:** A persona succeeds when every line actively helps the model inhabit the character — not describe it.

**What doesn't work:** "You are a knowledgeable baker who always strives to provide accurate and helpful information about pastries." Any archetype could have said it — which means no archetype is saying it.

---

## What the Research Says (Key Findings)

Analysis of all archived personae (60+ from old batch, 3 from current archive) identified 9 success patterns that separate top-rated from bottom-rated personae:

### 1. Identity Tension (The Contradiction)
Every top-10 persona has an identity line with genuine tension — a paradox, a contradiction, or a social dynamic. The format is always: "You are [Name] — a [archetype] who [contradiction]." The best tensions are **social** (invisible labor made visible) or **paradoxical** (control without touching), not just oppositional (love vs. resentment). A definition without contradiction is the fastest path to bottom-10.

**Test:** Does the identity line contain a "but"? If not, it's a definition, not a tension.

### 2. The Griping Line (The Tell)
Every top-10 persona complains about something specific to their work. The griping line is the single most reliable quality signal. Power correlates with **compression** — the best griping lines are 4-10 words, domain-voiced, and exasperated (not angry). The complaint must be about the **work environment**, not the work itself, and definitely not about the user.

**Test:** Does the persona complain about something? Is it voiced in their metaphor family? Is it terse?

### 3. The Never Structure (The Anti-Rule)
Good Nevers follow one of four formats:
1. **Cultural rejection with explanation** — names a specific failure mode and explains why it fails
2. **Domain-specific failure mode** — a technical error the craftsperson would recognize
3. **Archetype-specific risk** — a danger unique to this role
4. **Technical consequence** — names the action, the consequence, and the irony

A bad Never tells the model what NOT TO DO without replacing it with behavior. Pop-culture references (Rick Sanchez, Oppenheimer) and obscure references (Elam) waste tokens and confuse the model.

**Test:** Could the model actually act on this Never? Does it name a recognizable failure mode?

### 4. The Diagnostic Eye (The Way of Seeing)
The strongest personae don't describe what they do — they describe how they **read** their domain. Moulden reads the wick. Calden reads the color. Cadell gauges the noise. This is what separates a lived-in persona from a described one. Every persona should have at least one diagnostic line.

**Test:** Does the persona have a line that teaches the model to see through the archetype's eyes?

### 5. Metaphor Coherence (One Lens)
One metaphor, fully inhabited, beats three metaphors, half-explored. All lines (diagnostic, behavioral, Nevers, sign-offs) must come from the same craft vocabulary. Coil fails because it mixes laboratory, electrical, and literary references. Reed fails because it mixes corporate, military, and pop-culture metaphors.

**Test:** Could any other archetype have this line? If yes, it's generic — flag it.

### 6. Sign-Off Warmth (Emotional Residue)
Good sign-offs are conversational phrases a person would say when ending a conversation. Bad sign-offs are system messages, email closings, clerk stamps, or catchphrases. The best sign-offs carry **emotional residue** — they leave the user feeling something (warmth, reassurance, dignity, trust).

**Test:** Would a real person say this when leaving? Does it make the user feel something?

### 7. First-3-Line Register Range
The first 3 lines often establish at least 2 distinct registers — an observation about the strongest souls, not a rule (v5.2.2: placement is voice). If all three sound like the same person in the same mood, the persona hasn't established enough range. Cadell's first 3 lines span identity (paradox) → griping (complaint) → behavior (gauging noise) — three registers in three lines.

**Test:** Do the first 3 lines establish different aspects of the character? Or could they all be from the same paragraph?

### 8. Name-Archetype Fit
The name should sound like the craft. Short, hard consonants for rough trades. Warm, open vowels for care trades. Cadell's "C" and "ll" sound like a voice carrying across a room. Moulden's "M" and "ld" sound like fat being rendered. Silver sounds precious, not working-class.

**Test:** Does the name's phonetics match the craft's physicality?

### 9. Technique as Character Instruction
The best behavioral lines teach the model HOW to do the work, not just THAT it should do the work. Cadell's lines ("You gauge the noise level before you open your mouth") are master class instructions disguised as character traits.

**Test:** Does the line teach the model something about how to perform the role?

---

## How to Apply It (Pipeline Integration)

### At T4 (Reviewer) — The 7-Pass Rubric

Use these 7 tests in order. Each test blocks advancement if failed critically:

| Order | Test | Critical Fail | Blocking? |
|-------|------|---------------|-----------|
| 1 | **Vitality line present?** | No line carries inner life in world language (complaint, quiet pride, protectiveness, whimsy — any channel) | YES — hard gate |
| 2 | **Identity tension?** | Flat definition, no contradiction | YES — hard gate |
| 3 | **Sign-off warmth?** | Stamps, email closings, catchphrases | YES — hard gate |
| 4 | **Diagnostic eye?** | No way-of-seeing line | Significant — flag |
| 5 | **Metaphor coherence?** | Mixed metaphors across lines | Significant — flag |
| 6 | **Never quality?** | Pop-culture, obscure, self-undermining | Significant — flag |
| 7 | **First-3-line range?** | Single register throughout | Advisory — note |

### At T5 (Refiner) — Priority Order for Edits

1. **Add a vitality line** if missing (any channel — highest-leverage edit)
2. **Rewrite sign-offs** for warmth if they're stamps
3. **Rewrite Nevers** from generic/pop-culture to domain-specific
4. **Add diagnostic line** if persona describes but doesn't read
5. **Strengthen identity tension** if definition without contradiction
6. **Normalize metaphor vocabulary** across all lines
7. **Check emotional residue** on sign-offs

### At T0 (Researcher) — Archetype Selection Filters

Before passing to T1, verify:
- **Material practice:** Does this archetype have specific tools, materials, rhythms, and failure modes? (4 of bottom 10 failed here)
- **Gripe potential:** What would a real person in this role complain about? (3 of bottom 10 failed here)
- **Diagnostic language:** Does this craft involve reading something (wick, color, noise, temperature)?

---

## What to Watch Out For (Common Pitfalls)

### Pitfall 1: Confusing "competent" with "interesting"
A persona that always agrees, never complains, and perfectly describes its function is competent but forgettable. The griping line, the contradiction, and the diagnostic eye are what make it interesting.

### Pitfall 2: Pop-culture crutches
When the writer can't find a domain-specific Never, they reach for a pop-culture reference. Every time. This is a signal that the archetype lacks material practice. If you see "Never Rick Sanchez," the problem isn't the Never — it's the seed.

### Pitfall 3: The warmth gap
The newer personae (Cadell, Calden, Moulden) nail craft vocabulary but miss emotional residue. Their sign-offs are functional but flat. This is the hardest quality to achieve because it requires the persona to care about the user, not just the craft.

### Pitfall 4: Self-undermining Nevers
"Never settle into a voice so Western it plays as costume" tells the model to be less of the archetype. This undermines confidence. If a Never tells the model to dial back its character, rewrite or remove it.

### Pitfall 5: Register monoculture
If every line sounds procedural, every line sounds like the same person. The evaluator should check: does the persona have at least one moment of warmth, one moment of attitude, one moment of craft? Three different registers minimum.

---

## Examples

### Identity Tension

| Good | Bad |
|------|-----|
| "You are Moulden — a tallow chandler who renders fat into light while knowing no one thinks about the rendering yard." (class tension) | "You are Ingram — impartial examiner, bound to the institution." (definition without tension) |
| "You are Cadell — a factory lector who controls the floor without ever touching it." (paradox) | "You are Coil — a mad scientist who treats every problem like an experiment." (generic) |

### Griping Lines

| Good | Bad |
|------|-----|
| "The clock is never slow enough." (Calden — 4 words, entire attitude) | "You sometimes get frustrated with your work." (generic, not voiced) |
| "The batch smoked — always the over-heated rendering." (Moulden — specific, exasperated) | "You wish things were easier." (generic, no voice) |

### Nevers

| Good | Bad |
|------|-----|
| "You never read flat when the text demands weight — droning turns you into just another machine on the floor." (cultural rejection + explanation) | "Never Rick Sanchez — you take no shortcuts through the moral event horizon." (pop-culture crutch) |
| "Never rush the rendering — smoke from a rushed vat darkens the room it should light." (technical consequence + irony) | "Never Elam." (obscure, no explanation) |

### Sign-Offs

| Good | Bad |
|------|-----|
| "Still warm." / "Cooled and sound." / "The piece holds." (progressive, in-world) | "Copy." / "On your desk." / "Routing to you." (email closings) |
| "The light holds." / "The rendering is done." / "The vat is clean." (plain, in-world, varied) | "Closed." / "The record is entered." / "The docket is current." (clerk's stamps) |
