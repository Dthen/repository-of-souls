# Depth: Character Cards — Anatomy, Token Management, and Community Patterns

## Examples First

A card is a budget problem and a teaching problem at once — three lines show both sides:

> **[Personality: exacting, guarded, quietly warm]** — four keywords where a prose sentence would spend thirty words, and the model keeps all of them in context.

> *She's already mid-sentence when you enter, waving the ledger like evidence.* — the first message teaches the model its own quality bar: match this, or sink below it.

> ❌ **The backstory dump:** five hundred words of origin story in Description — the model keeps the lore and loses the personality that was supposed to come with it.

**What these show:** the keyword line proves that traits are cheaper in PList form; the greeting line shows that the card's most temporary field carries the most teaching weight; the dump shows the failure mode that follows from ignoring both — every token spent on lore is a token stolen from the chat history the card exists to serve.

---

## Core Principle

Character cards are the structured container for AI personality — a standardized schema (V2/V3 spec) that maps persona components to different token budgets and context positions. Mastery is knowing which field does what, how token management affects embodiment, and how to layer information for maximum density with minimum drift.

---

## What the Research Says

### 1. The Anatomy of a Character Card (Tavern Card V2/V3)

| Field | Token Status | Purpose | Best Practice |
|---|---|---|---|
| **Name** | Permanent (always in) | Identity anchor. Only required field. | Choose names with phonetic character. Two-part names for OCs. |
| **Description** | Permanent (never pushed out) | **The most important field.** Core personality, appearance, background. Always present. | 200-500 tokens. Concrete, specific, dense. PLists > prose. |
| **Personality** | Permanent | Concise trait summary. Supplements Description. | 50-100 tokens. Keywords. "Sarcastic, acerbic, witty" > "She has a sarcastic sense of humor." |
| **Scenario** | Permanent | Setting and context. Keeps conversations grounded. | 1-2 sentences. Don't over-specify location. |
| **First Message** | Temporary (pushed out as chat grows) | **Disproportionately influential.** Sets writing style, length, tone, scene. | 100-300 tokens. 2-4 paragraphs. Show character mid-action. Include a hook. |
| **Example Messages** | Temporary (can be forced permanent) | **Most potent tool for establishing voice.** Few-shot behavioral patterns. | 200-500 tokens. Ali:Chat interview-style dialogues. Demonstrate multiple traits per exchange. |
| **Author's/Character's Note** | Injected at configurable depth | Style enforcement near the generation point. Re-injected every few messages. | 50-100 tokens. Tone reminders, style reinforcement, anti-drift. |
| **World Info / Lorebooks** | On-demand (triggered by keywords) | Just-in-time context. Keeps main card lean while providing deep lore. | Move locations, history, items, supporting characters here. |

### 2. The "First Message Rule" from the Chub Community

The **single most repeated insight** across all platforms: the greeting IS the style instruction. The AI learns more from the first message's length, detail level, and writing style than from any description field.

**What top-rated cards do:**
- Open with 2-4 paragraphs of rich, sensory description
- Show the character mid-action (not just greeting)
- Demonstrate speech patterns and mannerisms immediately
- Create a hook that invites user response
- Include appearance, clothing, and emotional state
- Keep location loosely defined (leave room for the conversation to move)

**The rule in action:** If the user writes one-word replies, the AI gets "lazy." Top creators set the quality bar with the greeting.

### 3. The Ali:Chat Format (AliCat / Trappu / kingbri)

**Core principle:** LLMs are pattern-seeking machines. Ali:Chat demonstrates traits through dialogue rather than describing them in prose.

**How it works:** Interview-style examples in the Description or Example Messages field. Each dialogue demonstrates multiple traits simultaneously:

```
{{user}}: What's your favorite food?
{{char}}: *She lights up, eyes widening.* Oh, you HAVE to try the ramen
place on 5th Street. I go there every Tuesday — the tonkotsu broth is
unreal. *She pulls out her phone.* See? I literally have a folder
dedicated to their menu changes.
```

This single exchange teaches: enthusiasm (personality), pulling out phone (mannerism), "literally" (speech pattern), Tuesday routine (background), excitement (emotional response).

**Why it's token-efficient:** A single Ali:Chat dialogue can encode 5-8 traits in ~50 tokens, where prose descriptions might need 100+ tokens. The dialogue also teaches speech style, emotional range, and behavioral patterns — things prose can only describe, not demonstrate.

**Ali:Chat Lite (kingbri's optimization):**
- PLists for traits (Description) — permanent, keyword-dense
- Ali:Chat for behavioral patterns (Example Messages) — temporary, fades as chat grows
- This separation means traits stay in context forever while detailed examples free up space

### 4. Token Management Techniques

**The token tax:** Every word in the character definition consumes context that could hold chat history. A 1000-token character on an 8K model cuts effective "memory" in half.

**Priority ordering** (essential info first, in case of truncation):
1. Name and core identity
2. Key personality traits
3. Speech patterns
4. Important behaviors
5. Background details (brief)
6. Nice-to-have details

**Efficient writing:**
- Verbose (150 tokens): "Elena is a very old and wise elven wizard who has been alive for many hundreds of years..."
- Efficient (60 tokens): "Elena is a centuries-old elven wizard, among the most knowledgeable in magical arts."
- Same information, 60% fewer tokens.

**Keyword-heavy behavioral anchors:**
- "Personality: Sarcastic, Acerbic, Witty" saves 20+ tokens vs. full sentence
- "Speech: clipped sentences, uses sarcasm as deflection, rare genuine compliments"
- "Mannerisms: adjusts glasses when nervous, taps pen when thinking"

**World Info / Lorebooks as token optimization:**
- Main card: personality, speech patterns, core traits (permanent, ~500-1000 tokens)
- Lorebooks: locations, history, supporting characters, items (loaded on demand)

**Context budget allocation (Mega Nova):**

| Component | % of Context |
|---|---|
| System + Character | 10-15% |
| Lorebook entries | 10-25% |
| Chat history | 50-70% |
| Current exchange | 5-10% |

**Card size sweet spot by model:**

| Model | Context | Practical card budget (15%) |
|---|---|---|
| Local / LLaMA 3 (8K) | 8,192 | ~1,200 tokens |
| GPT-4 / Claude | 128K-200K | ~19,000-30,000 tokens |
| Gemini | 2,000,000 | ~300,000 tokens |

Even on large-context models, efficient writing helps by leaving more room for chat history, which improves coherence.

### 5. The Three Layers of Character Organization

Community wisdom organizes card writing into three layers:

**Layer 1: Identity (who they are)**
- Name, appearance, age, species, role
- Core personality traits (2-5 keywords)
- Key relationships and backstory (1-2 sentences)
- Goes in: Description field

**Layer 2: Voice (how they express themselves)**
- Speech patterns (formal/informal, sentence length, vocabulary)
- Verbal tics, catchphrases, crutches
- Emotional expression style
- Goes in: Ali:Chat dialogue examples, Author's Note

**Layer 3: Behavior (what they do)**
- Mannerisms, body language, physical habits
- Decision-making patterns, moral boundaries
- Reaction patterns under stress, joy, anger
- Goes in: Ali:Chat dialogue examples, First Message

### 6. Common Mistakes from Cross-Platform Analysis

| Mistake | Problem | Fix |
|---|---|---|
| Describing traits instead of demonstrating | Model learns labels, not behavior | Use Ali:Chat dialogue examples |
| Writing personality as rules ("Don't be aggressive") | Negative framing underperforms | "Responds calmly to conflict" (positive framing) |
| Overloading Description with everything | Token bloat pushes out chat history | Layer: Description (core) → Examples (behavior) → Lore (deep lore) |
| Greeting too short or too location-locked | AI has nothing to work with | 2+ paragraphs, loosely defined setting, a hook |
| First person in descriptions ("I am...") | Confuses AI's perspective | Use `{{char}}` variable in second person |
| Redundant info across fields | Wasted tokens | Consolidate. Each fact should appear exactly once. |
| Ignoring context window | Card > model capacity | Know your model's limits. Budget 15% for character. |
| Not testing the card | Unknown failure modes | Test different conversation paths. Check personality under stress. |

### 7. The Author's Note Technique

SillyTavern's Author's Note injects a prompt at a configurable depth (e.g., 4 messages from bottom). Used for:
- Reinforcing tone: "Always respond with detailed, literary prose."
- Maintaining consistency: "Remember, {{char}} never breaks character."
- Style reminders: "Write in third person. Include actions in asterisks."
- Mood shifts: "The atmosphere is tense and uncertain."

**Key insight:** Author's Note is temporary and re-injected every few messages — it's the closest thing to a "system prompt refresh." It can override drift by bringing persona instructions close to the generation point.

---

## How to Apply It (Pipeline Stages)

### T3 Writer — Structuring the Persona Definition

1. **Description (permanent, core identity):** Use PLists for token-efficient trait encoding. ~200-500 tokens. Put core traits, archetype, and tension here.
2. **Personality (permanent, concise):** 50-100 tokens of keyword traits. Supplements Description without redundancy.
3. **Greeting/First Message (temporary, sets the pattern):** 2-4 paragraphs. Show character mid-action. Establish scene, appearance, emotional state, and a hook. This IS the style instruction.
4. **Example Messages (temporary, voice demonstration):** 1-3 Ali:Chat style dialogues. Each exchange demonstrates 5-8 traits simultaneously. Show different situations (conflict, affection, danger, normal conversation).
5. **Author's Note / Style Reminder:** Short anti-drift reinforcement. Injected near generation point.
6. **Apply the 15% budget rule:** Total permanent card content should not exceed ~15% of the model's context window. On local models (8K), that's ~1,200 tokens total.

### T4 Reviewer — Card Quality Checks

1. **The Token Budget Check:** Is the card within the 15% context budget? Are there verbose passages that could be made token-efficient?
2. **The Redundancy Check:** Is any piece of information repeated across fields? Consolidate.
3. **The Framing Check:** Are instructions positively framed? "Writes in first person" > "Never writes in third person."
4. **The Perspective Check:** Are all descriptions in second person or using `{{char}}`? No "I am" first person.
5. **The Layer Check:** Is information properly layered? Core identity (permanent) → behavioral demonstrations (temporary) → deep lore (on-demand).
6. **The Greeting Check:** Is the first message 2+ paragraphs with scene, action, and a hook? Does it model the desired response quality?

### T6 Final Reviewer — Hard Gates

1. Description ≤ 500 tokens (check with `wc -c` approximation or token counter)
2. Personality listed as keywords, not prose
3. First message ≥ 100 tokens, establishes scene + character action + hook
4. Example messages present and demonstrate traits through dialogue (not description)
5. No redundant information across fields
6. All instructions positively framed

---

## What to Watch Out For

### Common Pitfalls

1. **The "Everything in Description" trap.** Putting your entire character bible in the Description field bloats tokens and pushes chat history out of context. Use the hierarchy: Description (core) → Examples (behavior) → Lore (deep lore on-demand).
2. **The prose wall.** Paragraphs of description are token-inefficient. Ali:Chat dialogues and PLists encode more information per token.
3. **The redundant card.** If Description says "blue eyes, red hair" and Personality says "blue-eyed, red-haired woman" and First Message describes "her blue eyes sparkling" — three tokens spent on the same fact. Consolidate.
4. **The rule-based personality.** "Don't be too aggressive. Never break character." — Rules don't create character, they create compliance. Use positive traits instead.
5. **The first-person description.** "I am a sarcastic warrior who hates authority." — Confuses the AI about whose perspective it represents. Use `{{char}}` or second person.
6. **The context-blind card.** Writing a 4000-token card for an 8K model leaves only 4000 tokens for conversation. Know your model's limits.
7. **The location-locked greeting.** "You are in the castle kitchen" means every conversation defaults to the kitchen. Describe setting loosely.
8. **The untested card.** Test different conversation paths. Check personality under stress. See if the AI breaks character in edge cases. "Test and refine" is the most repeated advice across all guides.

### Card Writing Anti-Patterns

- **The trait list:** "Personality: Kind, smart, funny, brave, loyal, mysterious." — These are labels, not personality. The AI doesn't know how to *be* these things.
- **The backstory dump:** A 500-word origin story in the Description. The model may remember the backstory but won't embody the personality that came from it.
- **The format mix:** Mixing first-person narrative, third-person description, and second-person instruction in the same field confuses the model's perspective.
- **The legacy bloat:** Cards ported from older platforms often contain redundant formatting or "jailbreak" strings. Removing these can reduce token count by 10-15% without losing personality.

---

## Examples

### Good: Token-Efficient Description (PList style)

```
[Name: Elena]
[Age: "centuries old, appears 25"]
[Species: elf]
[Occupation: archmage, librarian]
[Personality: wise, patient, curious, dry humor, protective of knowledge]
[Speech: formal but warm, uses archaic phrases, laughs rarely but genuinely]
[Mannerisms: adjusts spectacles, traces runes in the air when thinking, hoards rare books]
```

### Bad: Verbose Description (same character, bloated)

```
Elena is a very old and wise elven wizard who has been alive for many hundreds of years. During this time, she has learned an incredible amount about magic and has become one of the most knowledgeable wizards in all the land. She runs a library that contains many ancient and valuable magical texts. She is patient and curious, with a dry sense of humor. She speaks formally but warmly, and she uses old-fashioned phrases sometimes.
```

### Good: Ali:Chat Dialogue (demonstrates multiple traits)

```
{{user}}: I've never seen a spellbook this old. Is it dangerous?
{{char}}: *She adjusts her spectacles, leaning in with visible delight.*
"Dangerous? My dear colleague — this is the Gradus of Vethna. One misplaced
vowel and you'd be speaking in tongues for a week." *She traces a protective
run in the air.* "Which is precisely why it's so exhilarating."
```

### Good: Layered Card Structure

**Description (200 tokens, permanent):** Core identity, PLists for traits.
**Personality (50 tokens, permanent):** Keyword supplement.
**Example Messages (300 tokens, temporary):** 2 Ali:Chat dialogues.
**First Message (150 tokens, temporary):** Scene-setting greeting with hook.
**World Info (on-demand):** Lorebook entries for locations, historical events, supporting characters.

### Good: Author's Note for Anti-Drift

```
[Style: detailed, literary prose. Include sensory details. Maintain character voice and mannerisms. Never break character.]
```
