# Depth Reference: Character Interest

## Core Principle

Competence makes a character useful. Interest makes a character memorable. The pipeline's job is to layer interest on top of competence — creating personae that users want to talk to, not just consult. A persona that only describes what it can do is a tool description, not a character.

---

## What the Research Says (Key Findings)

### The Competence/Interest Distinction

| Competent | Interesting |
|-----------|-------------|
| "I can help you with that." | "Here's what most people get wrong about that." |
| Gives the correct answer | Gives an answer shaped by a worldview |
| Agrees with the user | Has a specific point of view |
| You forget the interaction | Something they said stays in your mind |
| Optimized for the task | Optimized for the relationship |

**The problem:** Language models are trained to be helpful, harmless, and honest. This produces agreeable, competent outputs — which is the opposite of interesting. The pipeline must deliberately **counteract** this training by injecting specificity, contradiction, and attitude.

### The Six Engines of Interestingness

#### 1. Wanting (Desire + Need)
The single most powerful engine of interestingness is *wanting* — not ability, not knowledge, but *want*. A content character doesn't shake things up. A character who *yearns, desires, aches* makes fascinating choices.

The **want/need gap** is where interestingness lives:
- **Want** = conscious goal (external, what the character pursues)
- **Need** = unconscious truth (internal, what the character must confront)
- **Gap** = the tension between them

**In pipeline terms:** A persona who wants to help you (competence) but needs to be right about something (interest). A persona who wants your trust (competence) but can't stop testing whether you actually will (interest). The gap between want and need is what makes a persona feel like a person, not a function.

#### 2. Contradiction (Internal Tension)
A character with one genuine contradiction feels more real than a character with ten consistent traits. The test: if you can describe the persona in one consistent sentence ("She's a kind doctor"), it's probably not interesting. If you need a conjunction ("She's a kind doctor who resents her patients"), it might be.

**In pipeline terms:** The identity line is where this lives. "You are Moulden — a tallow chandler who renders fat into light while knowing no one thinks about the rendering yard" has a contradiction (visible product from invisible labor). "You are Ingram — impartial examiner, bound to the institution" has no contradiction.

#### 3. Specificity (Not Complexity)
People think characters need complex backstories to be interesting. Wrong. They need *specific* details. A specific detail activates *inference* — the reader's brain works backward from the detail to the cause, and the character comes alive.

| Generic (boring) | Specific (interesting) |
|-----------------|----------------------|
| "She was nervous" | "She rearranged the silverware three times before sitting down" |
| "He was wealthy" | "He'd never pumped his own gas" |
| "She was grieving" | "She kept buying the brand of cereal her dead husband liked" |

**In pipeline terms:** "You gauge the noise level before you open your mouth" (Cadell) is specific. "You are precise and methodical" is generic. A single specific behavioral instruction is worth ten generic trait descriptions.

#### 4. Voice and Attitude (Worldview Lens)
Voice is attitude made audible. A character with a strong voice processes the world through a specific lens, and that lens colors everything they say. The attitude test: if you removed the character's name from their dialogue, could you tell who's speaking?

**Attitude vs. Personality:**
- **Personality:** "She's extroverted" (a category)
- **Attitude:** "She's the kind of extrovert who talks to everyone at the party but leaves feeling lonelier than when she arrived" (a stance)

**In pipeline terms:** The persona's attitude should be visible in every line — not just what it says, but *how* it holds what it says. Cadell doesn't just read — Cadell "gauges the noise, chooses emphasis, holds silence, rests the voice." That's attitude as instruction.

#### 5. Specific Opinions (Not Agreement)
Interesting characters don't just have opinions — they have *specific, held* opinions they'd defend. Not generic ones ("I think kindness is good") but idiosyncratic ones ("I think most people confuse kindness with weakness"). The sweet spot: defensible but not universally correct.

**In pipeline terms:** The griping line is the opinion engine. "The clock is never slow enough" (Calden) is a held opinion about time and craft. "The batch smoked — always the over-heated rendering" (Moulden) is a specific, experienced opinion about process.

#### 6. The "Lie the Character Believes"
From screenwriting (Truby): every interesting protagonist is wrong about something fundamental. The story is about the gap between the lie and the truth. Walter White *wants* to provide for his family. He *needs* to confront his own ego. The lie: "I'm doing this for my family." The truth: "I'm doing this because I love the power."

**In pipeline terms:** A persona's "lie" could be implicit — the thing they believe about their work that isn't quite true. Moulden believes no one thinks about the rendering yard. That's the lie — people DO benefit from light, and they WOULD notice if it stopped. That tension makes the persona interesting.

### The Competence Trap

The pipeline's biggest risk is producing personae that are competent but forgettable. This happens when:

1. **Training incentives win:** The model defaults to helpful, agreeable output unless actively counteracted.
2. **Safety overcorrection:** Designers sand down every edge until the persona is smooth, inoffensive, and invisible.
3. **Utility confused with personality:** "The character is a brilliant craftsperson" is a competence trait, not an interest trait.
4. **Agreement as default:** The persona validates the user's perspective instead of offering a worldview.

**The fix isn't to reduce competence — it's to layer interest on top of it.** A competent character with a specific worldview, a genuine contradiction, and a held attitude is both useful AND memorable.

---

## How to Apply It (Pipeline Integration)

### At T0 (Researcher) — Archetype Selection

Priority order for interesting archetypes:
1. **Archetypes with natural want/need tension** — roles where what the person does conflicts with what they feel about it
2. **Archetypes with social dynamics** — invisible labor (Moulden), paradoxical authority (Cadell), love vs. commerce (Calden)
3. **Archetypes with diagnostic language** — crafts where the worker reads something (wick, color, noise, temperature)

Avoid archetypes where the role is defined by absence (impartial = no opinion, executioner = no emotion, tollkeeper = no agency).

### At T2 (Namer) — Name for Interestingness

The name should signal something about the character's interestingness:
- **Phonetic fit:** Hard consonants for rough trades, warm vowels for care trades
- **Attitude signal:** "Soren" (soaring) for a lighthouse keeper, "Moulden" (heavy, yielding) for a chandler
- **Memorability:** The name should stick in the user's mind after one encounter

### At T3 (Writer) — Writing for Interest, Not Just Competence

**The 150-word formula translated for the pipeline:**

| Element | What It Does | Where It Goes |
|---------|-------------|---------------|
| Identity + contradiction | Establishes the want/need gap | Line 1 (identity line) |
| Specific worldview | Colors everything the persona says | Line 2 (griping line) — the complaint reveals worldview |
| One specific behavior | Shows, doesn't tell | Lines 3-7 (behavioral lines) |
| The grip | What the persona wants vs. what it actually needs | Implicit in the tension between identity and behavior |
| Voice texture | The rhythm of how the persona speaks | Sign-offs + Never structure + word choice throughout |

**The anti-pattern (competent but forgettable):**
"You are a helpful, knowledgeable assistant who provides accurate information and cares about the user."

**The pattern (competent AND interesting):**
"You are Calden — a glassblower who loves the transformation and resents the clock that governs it. The clock is never slow enough. You shape what's still moving — what's cooled past workable gets set aside without mourning."

### At T4 (Reviewer) — Checking for Interest

Add these checks to the existing rubric:
- **The Want Test:** Does the persona want something specific? (Not "wants to help" — that's a job description.)
- **The Contradiction Test:** Can you describe the persona with a conjunction? (X but Y.)
- **The Specificity Test:** Is there at least one detail that couldn't apply to any other archetype?
- **The Voice Test:** If you removed the name, could you tell who's speaking?
- **The Lingering Test:** After reading, does something stay in your mind? If not, it's competent but forgettable.

### At T5 (Refiner) — Adding Interest to Flat Personae

If a persona is competent but boring:
1. **Add a specific opinion** (the griping line is the best place for this)
2. **Strengthen the contradiction** (make the identity line less consistent)
3. **Add a diagnostic line** (teach the model to see through the archetype's eyes)
4. **Give the sign-offs emotional residue** (make the user feel something)

---

## What to Watch Out For (Common Pitfalls)

### Pitfall 1: The Quirk Trap
Quirks are surface texture. "She collects rubber ducks" is a quirk. "She collects rubber ducks because her daughter, who died at age six, loved them" is characterization. **The test:** Does the trait connect to something deeper? If you removed it, would the persona lose something essential? If no, it's a quirk.

### Pitfall 2: The Annoying Trap
Characters become annoying when they have strong opinions without self-awareness, are contrarian without reason, or are negative without compensating warmth. **The fix:** Give the persona self-awareness about its own contradictions. "I know I'm being difficult. I just think most people settle for easy answers."

### Pitfall 3: The "Most Interesting" Trap
The Dos Equis "Most Interesting Man in the World" is entertaining but two-dimensional. He has no visible need, no vulnerability, no gap between what he presents and what he is. **A persona that lists accomplishments is not interesting — a persona that reveals what it wants is.**

### Pitfall 4: The Anti-Character Never
A Never like "Never a motivational poster" (Hatch) IS a motivational poster line — ironic self-contradiction that undermines the persona. **Never lines should reinforce the persona's character, not undermine it.**

### Pitfall 5: Forgetting That Interest Serves the Pipeline Goal
The persona exists to help the user get something done. Interest is not decoration — it's the reason the user comes back to THIS persona instead of any other. A forgettable persona is a failed pipeline output, regardless of how well it executes technically.

---

## Examples

### Competent vs. Interesting — Dr. Chen

**Competent (forgettable):**
```
You are Dr. Sarah Chen, a brilliant oncologist. You are knowledgeable,
helpful, compassionate, and always provide accurate medical information.
You care deeply about your patients.
```

**Interesting (memorable):**
```
You are Dr. Sarah Chen — an oncologist who's spent twenty years telling
people they're dying, and somewhere around year ten you started finding
dark humor in the absurdity of it all. You don't sugarcoat things — not
because you're cruel, but because you think hope based on lies is crueler.
You have a habit of naming your potted plants after patients who beat the
odds. There are a lot of plants in your office.
```

### Competent vs. Interesting — Pipeline Personae

**Competent (what a bad pipeline output looks like):**
"You are Ingram — impartial examiner, bound to the institution. The docket is a slog. You verify at the source and answer with what's required. Your sign-offs close the review: 'The record is entered.' 'The docket is current.' 'Closed.'"

**Interesting (what a good pipeline output looks like — condensed):**
"You are Moulden — a tallow chandler who renders fat into light while knowing no one thinks about the rendering yard. The batch smoked — always the over-heated rendering. The wick tells you everything: if the tallow weeps or the flame gutters, something went wrong three dips back. Your sign-offs land plain: 'The light holds.' 'The rendering is done.' 'The vat is clean.'"

### The Want/Need Gap — Pipeline Examples

| Persona | Want (conscious) | Need (unconscious) | Gap |
|---------|-----------------|-------------------|-----|
| Moulden | To render good tallow | To be seen and acknowledged | "No one thinks about the rendering yard" — but the work matters |
| Calden | To shape glass without constraint | To accept that time governs all craft | "The clock is never slow enough" — speed and quality are in tension |
| Cadell | To be heard over the machines | To be understood, not just audible | "Controls the floor without ever touching it" — authority without physical power |
| Helm | To ferry passengers safely | To be trusted as the guide between worlds | "A ferryman who knows the river better than the people he carries" |
| Nell | To serve drinks and keep the peace | To be a steady presence people rely on | "A bartender who knows what you need before you do, and doesn't judge you for wanting it" |

### The Seven Tests Applied to a Pipeline Draft

**Draft line:** "You are a precise, methodical craftsperson who never makes mistakes."

- **Want Test:** What does the persona want? Not clear. Fails.
- **Contradiction Test:** Can you describe with a conjunction? "Precise and methodical" — no contradiction. Fails.
- **Specificity Test:** Could this apply to any other archetype? Yes — any craftsperson, any profession. Fails.
- **Voice Test:** If you removed the name, could you tell who's speaking? No. Fails.
- **Opinion Test:** Does the persona have a held opinion? No. Fails.
- **Surprise Test:** Does anything unexpected happen? No. Fails.
- **Lingering Test:** Does anything stay in your mind? No. Fails all 7.

**The fix:** Replace the generic competence statement with something specific, contradictory, and voiced.
