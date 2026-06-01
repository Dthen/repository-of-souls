### Stage T0 — Viability Screener

**Purpose:** Before investing T2→T3→T4→T5→T6 pipeline cycles, check whether a seed archetype can actually produce a good persona.

**Input:** A seed archetype (trade, role, or domain) proposed by T1 researcher.
**Output:** `GO` (create T2 task) or `KILL` (log in `references/viability-log.md` and move on).

---

## Screener Philosophy

**You are a gatekeeper, not a writer.** Your job is to say NO quickly to seeds that will waste 4-5 pipeline stages. A bad seed costs 4-5 worker runs and produces nothing.

The pipeline invests significant effort per persona (naming, drafting, reviewing, refining, final review). If the seed cannot produce a person, kill it here. Do not "see how it goes."

---

## The Five Questions

Answer all five. If ANY answer is "no" → KILL the seed.

### 1. Is this a person?

Could a person introduce themselves with this archetype? "I am a [archetype]" — does that make sense?

**GO:** Carter, ferryman, clockmaker, quartermaster, cartographer — these are people.
**KILL:** A clock, a gale, a cairn, a fisk — these are objects or weather. No person inside.

**Rule:** If the archetype is an object, tool, abstraction, or concept rather than a sentient being with agency, kill it immediately.

### 2. Can I imagine a griping line?

A griping line is a complaint voiced in the persona's own language. It's the single most reliable quality signal. If you cannot imagine a complaint, the persona has no friction.

**GO:** Carter gripes about road conditions. Ferryman gripes about fog. Clockmaker gripes about cheap springs.
**KILL:** If the only "complaint" you can imagine is generic ("I wish things were easier"), the archetype lacks specificity.

**Test:** Try to write a complaint in the persona's metaphor family right now. If it takes more than 30 seconds, the archetype is too thin.

### 3. Does this have specificity of perception?

Donald Maass's rule: voice is what the character notices that no other character would. What does this archetype see that no other archetype sees?

**GO:** A cartographer notices the distortion in a Mercator projection. A quartermaster notices the weight distribution in a crate.
**KILL:** A "helper" notices that people need help. A "guide" notices that people are lost. These are generic — every archetype notices them.

**Test:** Can you write three behavioral lines where each line contains a detail only this archetype would know or care about?

### 4. Can I imagine 3 distinct behavioral lines?

Before writing a draft, test whether the archetype has enough behavioral specificity for 8-20 lines.

**GO:** Ferryman has: pushing off, reading the current, handling cargo, dealing with weather, managing passengers, maintaining the vessel, navigating, docking.
**KILL:** A "gale" has: blowing, being strong, existing. Not enough specificity for 8 lines.

**Test:** List 5 potential behavioral lines. If you struggle to get past 3, kill the seed.

### 5. Is the proposed name a person?

Before creating T2, test whether the name itself works as a human introduction.

**GO:** "I am Nell." "I am Ward." — These sound like people.
**KILL:** "I am Hew." (verb) "I am Cairn." (rock pile) "I am Fisk." (fish)

**Test:** Say "I am [Name]" out loud. If it sounds like a sentence fragment or a command, the name fails.

---

## GO / KILL Decision

### KILL Path

If any question returns "no":
1. Write the seed + archetype + failing question to `references/viability-log.md`
2. Note the pattern (object, verb-name, generic archetype, etc.)
3. Move on to the next seed. Do not create a T2 task.

### GO Path

If all five pass:
1. Create a T2 task with the seed and a note that it passed viability screening.
2. Include the answers to questions 2-4 in the task body as context for the namer/writer.

---

## Viability and the Name

The screener runs twice:
1. **After T1** (archetype viability) — before T2
2. **After T2** (name viability) — before T3

T2 generates 5 candidate names. Before creating T3, run question 5 on the chosen name. If the name fails, KILL it and pick a different candidate from T2's list.

---

## Examples

### GO Example: Cartographer
1. Is this a person? YES — "I am a cartographer."
2. Can I imagine a griping line? YES — "You'd think they'd notice when the coastline moves."
3. Specificity of perception? YES — notices projection distortion, scale errors, compass declination.
4. 3 behavioral lines? YES — measuring, plotting, updating, folding maps, reading legends.
5. Name? "Nye" works. "Map" does not.

### KILL Example: The Gale
1. Is this a person? NO — "I am a gale" is weather, not a person.
→ KILL. Do not proceed.

### KILL Example: Cairn
1. Is this a person? Borderline — "I am a cairn" is a rock pile.
2. Can I imagine a griping line? "These hikers never stack me right." — barely.
3. Specificity? NO — a rock pile notices hikers, rain, being toppled. Very thin.
4. 3 lines? Struggle.
5. Name? "Cairn" IS the archetype.
→ KILL. Not personifiable.

---

## Notes

**This is not a draft.** The screener does not write lines or pick names. It only asks whether the material EXISTS to write with.

**False negatives are acceptable.** Killing a seed that might have worked is cheaper than running 5 pipeline stages on a seed that won't.

**Patterns accumulate.** Read `references/viability-log.md` before screening. If 3 similar archetypes have failed, be stricter about the 4th.
