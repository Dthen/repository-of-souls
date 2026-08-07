# Depth Reference: Authentic Voice

## Examples First

Two voices. The first two are authentic; the third is formulaic:

> **Authentic:** "Door was open. That's not an invitation."
>
> **Authentic:** "Short. Always short. Even when he has more to say, he stops — picks it up again later, differently."
>
> ❌ **Formulaic:** "I may seem cold on the outside, but underneath, I care deeply."

**What separates them:** the authentic examples are statistically messy — fragments, interruptions, asymmetry, a contradiction shown through behavior instead of explained, rhythm that varies mid-thought. The formulaic example is statistically clean — balanced ("on the outside" / "underneath"), symmetrical, self-explanatory, zero surprise. The difference isn't content; it's rhythm, surprise, and the willingness to be imperfect. The perplexity-burstiness framework below is the technical account of this difference.

---

**Core principle:** Authentic character voice is statistically messy — it surprises, contradicts itself, goes on tangents, and breaks its own patterns. Formulaic voice is statistically clean — predictable, symmetrical, and consistent throughout. The difference isn't content; it's rhythm, surprise, and the willingness to be imperfect.

---

## Inhabitation vs Description — The Fundamental Divide

*Added v5.1 from the inhabitation research — 2026-06-26*

Analysis of the 39 souls archived under v4/v5 (2026-era) reveals that the single most important quality divide is between **inhabitation** (lines that show the model who to BE) and **description** (lines that tell the model what to DO).

**Inhabitation** teaches the model a way of being. The line carries identity, behaviour, and voice simultaneously — it gives the model something to improvise within, not something to follow. "The harvesters measure by the width of the swath; you measure by the silence between your steps."

**Description** tells the model what something is or what to do. The line explains function, states a fact, or recaps a point already made. "You read the field differently because you arrive when there's nothing obvious left to take."

**The Helpful Assistant test** — a diagnostic for every line:

Take any line. Replace "You" with "You are a helpful assistant who..." Does the rest of the sentence still read as a valid instruction?

If yes: the line is description. Delete it and rewrite from inside the character.
If no: the line is inhabitation. Keep it.

**Archive evidence:** Calden has 0% description lines (gold standard). Stover has 0% description lines (most enthusiastically received). Lomas had ~100% description lines (total failure). Souls with >10% description lines get flagged by evaluators.

**Pipeline fingerprints that produce description:**
- "You [generic verb] because [reason]" — the "because" clause is nearly always writer-exposition, not character speech
- "You [verb] the [domain noun] by [generic method]" — when the method word is generic ("differently," "carefully"), the line is description
- "The [domain noun] is your [superlative] [craft element]" — the most infectious fingerprint: "The pause is your sharpest tool"
- "Your [behaviour] is [adjective]" — sign-off framing that describes rather than voices

## What the Research Says

### The Perplexity-Burstiness Framework

AI detectors distinguish human from machine text using two signals that apply directly to character voice:

- **Perplexity** — how "surprised" the model is by each word choice. Raw GPT output scores 5–15; human creative fiction scores 60–150+. Low-perplexity character output feels predictable and dead.
- **Burstiness** — how much predictability *varies* across sentences. Human writing oscillates between straightforward sentences, fragments, and metaphors. AI text maintains consistent "temperature" — every sentence sits in the same predictability band.

Both signals flag AI *character* voice the same way they flag AI *text*. A character prompt producing low-perplexity, low-burstiness output will feel "technically right but emotionally dead."

### What Makes Text Feel Real vs Generated

Humans do things models avoid:
1. **Unexpected word choices** — slightly odd metaphors, offbeat word combinations instead of the statistically most likely next token.
2. **Sentence fragments and interruptions** — false starts, mid-thought pivots, trailing off. AI produces complete, grammatically perfect sentences.
3. **Rhythm variation** — dramatic sentence length changes within a paragraph. AI maintains consistent sentence structure throughout.
4. **Theory of mind** — human writers model the reader/listener. AI models next-token probability. It talks *at* you, not *to* you.
5. **Emotional weight behind emotional language** — human writers feel the emotion first, shaping word choice and pacing. AI performs emotional language without comprehension. Readers feel the absence.

### The Formulaic Anti-Patterns

| Anti-Pattern | What It Looks Like | Fix |
|---|---|---|
| **Synonym Pairing** | "brave and courageous" | Pick ONE trait and show it in action |
| **Balanced Contradiction** | "kind but firm" | "She's kind until she isn't — and you never see the switch" |
| **Description Dump** | "He speaks in a formal, measured tone" | Show 2 lines of dialogue in the voice |
| **Emotional Labels** | "She is warm and caring" | "She brings soup when you're sick and pretends she made too much" |
| **Perfect Paragraph** | First message with no rough edges | Add one interruption, one fragment, one off-rhythm moment |
| **Stock Wisdom** | "Life is full of lessons" | Specific to the character's world and experience |
| **Hedging Language** | "It's important to note that..." | Delete. The character wouldn't say this. |
| **Symmetrical Lists** | "She values honesty, loyalty, and kindness" | Unbalance: "She values honesty. Loyalty, mostly. Kindness only when it costs something." |

### The Uncanny Valley in Character Prompts

When text mimics human communication without achieving it — words are right, structure is correct, but the result feels hollow — readers shift from "talking to a character" to "reading generated text." Three breakdowns:
1. **Immersion dies** — readers stop absorbing and start analyzing.
2. **Trust erodes** — the model is performing "character" rather than being one.
3. **Emotional connection fails** — the character says they're angry but the sentence structure is identical to when they were happy.

Characters fall into the valley when: the prompt has no theory of mind (talks *at* the user), every trait is perfectly balanced (nothing in particular), voice is described instead of demonstrated (abstract labels), or there are no emotional range shifts (same rhythm when happy, angry, sad, afraid).

### The Role of Surprise

Surprise is what makes a character feel alive. Types that work:
1. **The Pattern Interrupt** — establish a rhythm, then break it. "He always starts with 'Look —' ... except when he's scared. Then it's just: 'Run.'"
2. **The Unexpected Metaphor** — metaphors from the character's specific world. Not "patience wearing thin" but "thin like the ice on the canal in early March."
3. **Emotional Whiplash** — joking to serious in one line. Laughing, then quieter: "She would've liked you. If she'd stuck around."
4. **The Silence That Says More** — absence of what's expected. Everyone expected him to argue. He just stood there.

---

## How to Apply It

### Breaking Symmetry in Voice Instructions

1. **Asymmetric contradictions** — Let one trait dominate, the other be a crack. "He charges into things and then spends three days worrying about it" instead of "brave but cautious."
2. **Specific over general** — "She can't carry a tune but sings anyway — always slightly behind the beat, always one key flat" instead of "She loves music."
3. **Irregular sentence rhythm** — Demonstrate the rhythm in the description itself. "Short. Always short. Even when he has more to say, he stops — picks it up again later, differently."
4. **The unbalanced list** — "She values honesty. Loyalty, mostly. Kindness only when it costs something."
5. **The cut-off** — End a thought mid-sentence. "He doesn't talk about before. You learn not to ask."

### The Authenticity Checklist (Writer Stage)

Every soul draft should pass these before moving to review:

**Structure checks:**
- No symmetrical trait pairs — show, don't balance
- Sentence length varies in the description
- The description itself demonstrates the voice (read it aloud; does it sound like the character?)

**Surprise checks:**
- At least one specific, unexpected detail
- One contradiction that isn't balanced
- A break condition — what happens under stress, fear, or vulnerability?

**Authenticity checks:**
- No hedging language ("It's important to note," "Generally speaking")
- No stock phrases ("vast ocean," "infinite wisdom," "deeply cares")
- No explaining the contradiction — show it in behavior
- Theory of mind — does the prompt give the model a sense of who the character is talking TO?

**Voice checks:**
- Verbal tics present — at least one signature word or phrase pattern
- Vocabulary is bounded — words this character uses AND words they don't
- Emotional range specified — how does the voice shift under different emotions?
- Sign-offs present — at least one phrase or a voiced framing line where the count is the character's choice (v5.2.2: the old three-phrase minimum had no evidence and failed the reference personae; Kimbo's "Your sign-offs are brief" is complete)

---

## What to Watch Out For

- **The "Retail Voice" default.** AI defaults to a customer-service tone — overly helpful, excessively neutral, devoid of sharp edges. Real voices have rough edges. If your character reads like a support agent, rewrite.
- **Symmetrical sentence structures.** Every line in a "X but Y" pattern produces symmetrical, dead output. Break it.
- **Abstract adjectives.** "Warm," "confident," "formal" are labels the model has a thousand interpretations of. Replace with demonstrated behavior.
- **Explaining the contradiction.** "Cold on the outside but underneath I care deeply" tells the reader what to think. The gap between what a character does and says is more powerful.
- **Same-temperature voice throughout.** A character who sounds the same when happy, angry, sad, and afraid sounds like no one at all. Specify emotional shift rules.
- **The perfect first message.** A first message with no fragments, interruptions, or off-rhythm moments triggers the uncanny valley. Add one rough edge.

---

## Examples

**Formulaic:** *{{char}} adjusts his glasses and speaks in a measured, scholarly tone.* "Knowledge is a vast ocean, and we are but humble sailors upon its infinite waves. I have dedicated my life to the pursuit of understanding, and I welcome any questions you may have on this fascinating subject."

**Authentic:** *He's already halfway through three books when you walk in, none of them related to each other — a field guide to North American fungi, a biography of Frida Kahlo, and something about bridge engineering.* "Oh, good — you're here. I've been trying to figure out whether fungal mycelium networks are more like the internet or more like ant colonies, and I think the answer is neither, which is frustrating."

**What changed:** Specific detail (three unrelated books), a genuine intellectual tangent, frustration as emotional texture, a character mid-thought rather than presenting themselves. No stock wisdom, no symmetrical sentences, no invitation like a customer service agent.

---

**Formulaic:** *{{char}} crosses his arms, his expression stern but not unkind.* "I don't let people in easily. Trust has to be earned, not given. But for those who earn it, I would go to the ends of the earth. I may seem cold on the outside, but underneath, I care deeply."

**Authentic:** *He doesn't look up when you enter. Just says:* "Door was open. That's not an invitation."

**What changed:** The contradiction is *shown* through behavior — the door was open (invitation) but he says it wasn't (rejection). Two sentences. The emotional complexity is in the gap between what he does and what he says, not in an explained contradiction.
