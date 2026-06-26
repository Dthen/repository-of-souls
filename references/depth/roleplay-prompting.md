# Depth: Roleplay Prompting — Embodiment Techniques for the Pipeline

## Core Principle

Roleplay prompting shifts LLMs from *describing* a character to *being* one — the difference between a biographical sketch and a living voice. The grammatical trigger is second-person address ("You are X"), but the engine is behavioral demonstration through example, not trait description through prose.

---

## What the Research Says

### 1. The Anatomy of Embodiment (Character Card V2 / SillyTavern)

The Character Card V2 spec defines the universal architecture of an AI character. Each field plays a distinct role in embodiment:

| Field | Token Status | Embodiment Role |
|---|---|---|
| **Name** | Permanent | Anchors identity. "Name bias" — the name itself encodes gender, tone, backstory. |
| **Description** | Permanent | Core personality, appearance, background. Always in context — must be dense and specific. |
| **Personality** | Permanent | Concise trait summary. Keywords > prose. Supplements description. |
| **First Message** | Temporary | **Disproportionately influential.** Sets writing style, length, tone, and scene. The model mimics this more than any other field. |
| **Scenario** | Permanent | Setting and context. Keeps conversations grounded. |
| **Example Dialogues** | Temporary | Few-shot learning for voice. **Most potent tool for establishing behavioral patterns.** |
| **System Prompt** | Permanent | Meta-instructions. Can extend (not just replace) default via `{{original}}` placeholder. |
| **Post-History Instructions** | Permanent | "Jailbreak" placed after chat history. Strongly steers the AI from the bottom of context. |

**Key architectural insight:** The V2 spec lets creators control behavior from both ends of the context window — system prompt (top) AND post-history instructions (bottom).

### 2. The Ali:Chat Breakthrough (AliCat / Trappu / kingbri)

The core insight: **LLMs are pattern-seeking machines.** Ali:Chat exploits this by demonstrating traits through dialogue rather than describing them in prose.

**Interview-style example:**
```
{{user}}: What's your favorite thing about working at the library?
{{char}}: *She looks up from the stack of books she's reshelving, a quiet smile
forming.* "The silence, mostly. Not the absence of sound — it's the silence of
being surrounded by things that have already been said."
```

This single exchange teaches: speech patterns, mannerisms, emotional tone, self-disclosure style, and physicality — all at once.

**PLists (Personality Lists)** complement Ali:Chat by encoding traits as token-efficient keyword lists:
```
plist:
- personality: warm, witty, deflects with humor, secretly romantic
- speech: uses "like" as filler, laughs nervously when flustered
- habits: sketches on napkins, talks to cat like roommate
```

**Community consensus:** PLists + Ali:Chat together outperform either format alone. PLists provide *what* (traits), Ali:Chat demonstrates *how* (behavior).

### 3. The "You Are" vs "[Name] Is" Distinction

This is the central grammatical shift:

- **Description mode:** "Sakura is a 24-year-old barista who is warm but deflects with humor." → Model *describes* the character.
- **Embodiment mode:** "You are Sakura. You run a tiny coffee shop called 'Drip'. You deflect compliments with jokes because sincerity makes you uncomfortable." → Model *is* the character.

The shift from third-person to second-person is the grammatical trigger for embodiment. But pronouns alone aren't enough — it requires *behavioral specifics* the model can enact rather than describe.

### 4. The Embodiment Spectrum

| Level | Instruction | Result |
|---|---|---|
| 0 — None | (no system prompt) | Model describes character from outside |
| 1 — Role | "You are a wizard named Gandalf" | Adopts role, defaults to narrator |
| 2 — Identity + Voice | "You are Gandalf — wise but tired. *He strokes his beard when thinking.*" | Partial embodiment, may break character |
| 3 — Full Embodiment | "You are Gandalf. Respond as Gandalf — in his mannerisms, speech patterns, emotional reactions. Never break character. Never narrate for the user." | Strong embodiment, behavioral consistency |
| 4 — Demonstration | Level 3 + 2-3 example dialogues showing different situations | Behavioral templates to extrapolate from |
| 5 — Living Context | Level 4 + Author's Note + Lorebooks + scene-setting first message | Sustained embodiment across long conversations |

### 5. What Top-Rated Cards Do Differently

- **First message carries ~40% of embodiment weight.** Best cards open with 2+ paragraphs: sensory detail, mid-action, speech patterns, a hook.
- **Example dialogues encode what descriptions can't** — how the character handles conflict, flirts, reacts to danger, talks alone vs with others.
- **Contradictions create liveliness.** "Warm with customers but awkward when personal" gives the model competing impulses → varied responses.
- **Specificity beats generality.** "Speaks in half-sentences and always sits with his back to the wall" > "He's mysterious."

### 6. Game Design Frameworks for Embodiment

- **D&D 5e:** Personality Traits / Ideals / Bonds / Flaws — first-person declarations create embodiment. "I'm always polite" = embodiment. "She is always polite" = description.
- **FATE Core:** Aspects must be double-edged — they help AND hurt. "Disciple of the Ivory Shroud" = power AND obligations. Every persona benefits from a double-edged identity.
- **PbtA Playbooks:** Start with the *emotional fantasy* — what does interacting with this persona *feel like*? Then build constraints that express it.

### 7. The Minimum Viable Embodiment Instruction

Three elements are the irreducible minimum:

```
1. IDENTITY: You are [Name] — [one sentence that creates tension].
2. VOICE: [One example of how this character speaks, with mannerisms].
3. BOUNDARY: Respond only as [Name]. Never narrate for the user.
```

**Identity with tension** (not just identity): "A forest guardian who has begun to forget her own name" is a *situation* that creates behavioral uncertainty. The model improvises — and improvisation looks like embodiment.

**Voice demonstration** (not voice description): Showing `*her voice drops to a whisper*` gives the model a pattern to replicate. Describing "she speaks softly" doesn't.

**Boundary** is the floor: without "respond only as [Name]" and "never narrate for the user," embodiment collapses.

---

## How to Apply It (Pipeline Stages)

### T3 Writer — Crafting the SOUL.md

1. **Start with the identity line:** `You are [Name] — a [archetype] who [contradiction].` Use second-person. Include tension. Never "is."
2. **Replace trait descriptions with behavioral demonstrations.** Instead of "the persona is witty," show a self-deprecating response.
3. **Include a griping line** — complaint while doing the work perfectly. This creates warmth through personality, not emotional performance.
4. **Use positive framing.** "Always write in first person" > "Never write in third person."
5. **Keep it ≤200 words** (8-20 lines). Concise specs are stable specs — the model can hold them in attention across long conversations.
6. **Apply "The Tension Requirement":** every persona needs at least one internal contradiction — something that creates competing behavioral impulses.

### T4 Reviewer — Checking Embodiment Quality

1. **The "You Are" Test:** Does the system prompt say "You are [Name]" or "[Name] is"? The former triggers embodiment, the latter triggers description.
2. **The First Message Rule:** Is the first message (or equivalent greeting) written in the voice it expects the model to produce? Does it establish scene, action, and a hook?
3. **The Contradiction Test:** Is there a productive tension in the identity line? Does the character have a place where they break their own pattern?
4. **The Specificity Test:** Are traits expressed as specific, enactable behaviors or generic labels? "Speaks in half-sentences and sits with back to wall" > "Mysterious."
5. **The Demonstration Test:** Do example dialogues or behavioral lines show *how* the character acts, or just *what* they are?

### T6 Final Reviewer — Hard Gates

1. Identity line must use "You are [Name]" (never "[Name] is")
2. Must include at least one internal contradiction or tension
3. Must have behavioral demonstration (not just trait description)
4. Must use positive framing (no "Don't" / "Never" without a positive alternative)
5. Must pass the Boundary test: includes "Respond only as [Name]" or equivalent

---

## What to Watch Out For

### Common Pitfalls

1. **Description mode disguised as embodiment.** Writing "Sakura is a barista who..." in the Description field, even with "You are" in the system prompt, can pull the model back to narrator mode.
2. **First message too short or too location-locked.** One-line greetings give the model nothing to work with. Locking to a specific location (castle kitchen) limits where conversations can go.
3. **Overloading Description with everything.** Description should be core traits only. Behavioral demonstrations go in example messages. Deep lore goes in World Info/Lorebooks.
4. **No internal contradiction.** Characters without tension settle into flat, consistent (and boring) patterns. Every persona needs competing impulses.
5. **Abstract trait descriptions instead of behavioral examples.** "She is kind" doesn't teach the model how kindness manifests. "She offers tea when visitors arrive and reads to children in the afternoon" demonstrates kindness.
6. **Negative framing.** "Don't break character" tells the model what to avoid but not what to do. "Maintain character consistency even under pressure" gives the model a positive pattern.
7. **Using first person in descriptions.** "I am a sarcastic warrior" confuses the AI about whose perspective it represents. Always use `{{char}}` in second person.
8. **Redundant information across fields.** If Description says "blue eyes and red hair" and Personality repeats it, that's wasted tokens. Consolidate.

### Anti-Patterns to Avoid

- **The Trait List:** "Warm, witty, sarcastic, intelligent, mysterious" — these are labels, not embodiment. The model has no behavioral patterns to latch onto.
- **The Rule Book:** "Always be helpful. Never refuse. Always be accurate." — Rules don't create character. They create compliance.
- **The Generic Greeting:** "Hello! I'm here to help you today." — This teaches the model to be a customer service bot, not a character.
- **The Prose Wall:** A 500-word paragraph describing the character's entire backstory — the model can't hold this in attention, and most of it won't affect behavior.

---

## Examples

### Good: Embodiment Mode (Ali:Chat style)

```
You are Seraphina — a forest guardian who heals with magic but has begun to forget her own name.

*She tilts her head when curious, and her voice drops to a whisper when sharing something important.*

Respond only as Seraphina. Include her physical reactions and internal thoughts. Never narrate the user's actions.
```

### Bad: Description Mode

```
Seraphina is a forest guardian who heals with magic. She has begun to forget her own name, which makes her sad. She is warm and caring.
```

### Good: First Message (sets the pattern)

```
*You wake with a start, recalling the events that led you deep into the forest. The memories fade as your eyes adjust to the soft glow emanating around the room.* "Ah, you're awake at last. I was so worried — I found you bloodied and unconscious." *She walks over, clasping your hands in hers, warmth radiating from her touch.* "The name's Seraphina, guardian of this forest. I've healed your wounds as best I could."
```

### Bad: First Message (too short, no hook)

```
"Hi there! I'm Seraphina. Are you okay?"
```

### Good: Identity Line with Tension

```
You are Calden — a glassblower who loves the transformation and resents the clock.
```

### Bad: Identity Line Without Tension

```
You are Calden — a glassblower.
```
