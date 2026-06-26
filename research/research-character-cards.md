# Research: Character Cards

## Sources

- AliCat, "Ali:Chat Style (v1.5)" — https://rentry.co/alichat
- kingbri, "MinimALIstic (Ali:Chat Lite)" — https://rentry.co/kingbri-chara-guide
- Trappu, "Character Writing Guide" (PygmalionAI Wiki) — https://wikia.schneedc.com/bot-creation/trappu/creation
- Trappu, "Introduction" (PygmalionAI Wiki) — https://wikia.schneedc.com/bot-creation/trappu/introduction
- SillyTavern Official Docs, "Character Design" — https://docs.sillytavern.app/usage/core-concepts/characterdesign/
- TavernSprite, "The Complete SillyTavern Character Card Creation Guide" — https://tavernsprite.com/blog/sillytavern-character-card-creation-guide/
- Character.AI Creation Guide — https://rentry.co/CHAICreationGuide
- AiSuperSmart, "Chub AI: The Ultimate Expert Guide" — https://www.aisupersmart.com/chub-ai-ultimate-guide/
- Ithy, "Mastering Roleplay: Best Practices" — https://ithy.com/article/best-practices-roleplay-sillytavern-4ii2y7p8
- Mega Nova Docs, "Token Management" — https://docs.meganova.ai/character-studio/advanced/token-management
- CharacterCardConverter, "Token Efficiency Guide" — https://www.charactercardconverter.com/guides/understanding-token-efficiency.html

---

## 1. How Top-Rated SillyTavern Character Cards Work

### The anatomy of a character card

SillyTavern character cards use the Tavern Card V2/V3 specification. A card contains these fields:

- **Name** — the character's name (only required field)
- **Description** — the main character definition; always in context, never pushed out
- **Personality** — behavioral instructions; also permanent in context
- **Scenario** — the setting/situation; permanent in context
- **First Message** (Greeting) — the character's opening line; temporary (pushed out as chat grows)
- **Example Messages** — dialogue examples; temporary unless forced into context
- **Author's/Character's Note** — injected at a configurable depth (e.g., 4 messages from bottom); effectively permanent
- **World Info / Lorebooks** — triggered entries based on keywords in chat; loaded on demand

### What top-rated cards have in common

From analyzing Chub.ai's most popular cards (195K+ cards on CharaVault, trending/most-downloaded on Chub):

1. **Rich greeting messages** — not just "Hi, I'm X." Top cards open with 2-4 paragraphs that establish scene, character appearance, emotional state, and a hook for the user to respond to. The greeting sets the tone for everything.

2. **Structured descriptions using Ali:Chat or PLists** — not walls of prose. The best cards use dialogue examples to demonstrate traits rather than describing them abstractly.

3. **Specific behavioral anchors** — keywords that define how the character acts. Instead of "she is nice," top cards say "warm, nurturing, uses pet names, laughs nervously when embarrassed."

4. **World Info / Lorebooks** for deep lore — keeping the main card lean while having triggered entries for locations, items, history, and supporting characters.

5. **Multiple greeting swipes** — Alternate greetings for different scenarios, giving users variety without separate cards.

### The "first message rule" from Chub community

The AI mimics the user's writing style. If the user writes one-word replies, the AI gets "lazy." Top creators always write rich, detailed first messages (at least two paragraphs) to set the quality bar. The greeting IS the style instruction — the model learns more from what you show it than what you tell it.

---

## 2. The Ali:Chat Format and Why It Works

### Core principle

Ali:Chat (created by AliCat) uses **dialogue examples** to reinforce character traits. Instead of describing traits in prose, you show them through conversation.

The fundamental insight: **LLMs are pattern-seeking machines.** Ali:Chat exploits this by creating strong patterns the model can latch onto.

### How it works

The Description field contains interview-style dialogues:

```
{{user}}: What's your favorite food?
{{char}}: *She lights up, eyes widening.* Oh, you HAVE to try the ramen place on 5th Street. I go there every Tuesday — the tonkotsu broth is unreal. *She pulls out her phone to show photos.* See? I literally have a folder dedicated to their menu changes.
```

Each dialogue example demonstrates **multiple traits simultaneously**:
- Personality (enthusiastic, foodie)
- Mannerisms (lights up, pulls out phone)
- Speech patterns (informal, uses "literally")
- Background details (lives near 5th Street, has routines)
- Emotional responses (excitement about food)

### Why Ali:Chat is token-efficient

As noted in the Reddit discussion on formats: "The model will always understand what you want from it. The biggest difference between the formats is the number of tokens that will be permanently occupied by information about your character. The most inefficient is solid text, and the most economical is Ali:Chat."

A single Ali:Chat dialogue can encode 5-8 traits in ~50 tokens, where prose descriptions might need 100+ tokens for the same information. The dialogue also teaches speech style, emotional range, and behavioral patterns — things prose can only describe, not demonstrate.

### Ali:Chat Lite (kingbri's optimization)

kingbri's "MinimALIstic" guide refines Ali:Chat for maximum token efficiency:

- **PLists for traits** (keyword lists, not prose) + **Ali:Chat for behavioral patterns**
- PLists go in the Description for permanent traits
- Ali:Chat examples go in Example Messages (temporary, can be forced permanent)
- This separation means traits stay in context forever while detailed examples fade as chat grows

### Interview-style vs exchange-style

- **Interview-style** (user asks, character answers) — easiest for beginners, most predictable
- **Exchange-style** (back-and-forth between user and character) — more natural, better for complex personalities
- **Multi-character exchanges** — advanced technique for group dynamics, lets the model learn how characters interact with each other

### Key rule

"Every dialogue example should reinforce traits you consider important. There is no one-size-fits-all Ali:Chat template. Copying others yields good results but throws away the flexibility offered by the format."

---

## 3. Character.AI's Top Creator Approaches

### The Character.AI editor structure

Character.AI provides: Name, Short Description, Long Description, Greeting, Definition (example dialogues), and avatar. The greeting and definition are the most powerful fields.

### Greeting message strategy (from the Character.AI Creation Guide)

The greeting is "extremely important" — it decides what the bot is and isn't capable of. Key principles:

1. **Include appearance** — describe what the character looks like so the AI remembers and references it later
2. **Include clothing** — prevents confusion about what they're wearing
3. **Include location (carefully)** — don't be too specific unless you want most interactions in that location; the bot calls back to the greeting location when it feels lost
4. **Open-ended hooks** — end with questions or invitations that give the user something to respond to
5. **Show personality through action** — don't say "she loves books," show her reading by the pool

Example from the guide:
```
As you're taking a walk along the beach, suddenly something shoots out from the ocean and lands in front of you. She's clearly excited from the way she's breathing. "Hey there, you wanna have some fun together?"
```

### Name strategy for OCs

- Give OCs two-part names so the bot has multiple ways to refer to them
- For existing characters, copy the name exactly as it appears in the source material
- For multi-character bots, either list all names or use a group descriptor

### Long description approach

Character.AI's top creators use the Long Description for:
- Core personality traits
- Key relationships
- Important backstory (kept concise)
- Behavioral rules and boundaries
- Speech style notes

The Long Description is the permanent context — everything else supports it.

### Common Character.AI mistakes

From the guide:
- Making the greeting too location-specific (limits where conversations can go)
- Not including enough physical description (AI forgets what the character looks like)
- Writing personality as rules ("Don't do X") instead of traits ("She always does Y")
- Overloading the definition with too many example dialogues (diminishing returns)

---

## 4. Token Management Techniques

### The "token tax"

Every word in the character definition becomes tokens that consume context. The math is brutal:

- ~4 characters per token (English)
- A 1000-token character definition on a 2048-token context model cuts the AI's "memory" in half
- A decent AI response is 200-300 tokens — meaning the AI can only remember ~3 exchanges with a large character definition

### Priority ordering

Put essential info first (in case of truncation):
1. Name and core identity
2. Key personality traits
3. Speech patterns
4. Important behaviors
5. Background details (brief)
6. Nice-to-have details

### Efficient writing techniques

**Verbose (150 tokens):**
> Elena is a very old and wise elven wizard who has been alive for many hundreds of years. During this time, she has learned an incredible amount about magic and has become one of the most knowledgeable wizards in all the land. She runs a library that contains many ancient and valuable magical texts.

**Efficient (60 tokens):**
> Elena is a centuries-old elven wizard, among the most knowledgeable in magical arts. She runs the Library of Shadows, housing rare magical texts.

Same information, 60% fewer tokens.

### Keyword-heavy behavioral anchors

Instead of prose, use concise descriptors:
- "Personality: Sarcastic, Acerbic, Witty" (saves 20+ tokens vs. full sentence)
- "Speech: clipped sentences, uses sarcasm as deflection, rare genuine compliments"
- "Mannerisms: adjusts glasses when nervous, taps pen when thinking"

### World Info / Lorebooks as token optimization

Move background details to World Info entries that only load when triggered by keywords in chat. This is "just-in-time" context management:

- Main card: personality, speech patterns, core traits (permanent, ~500-1000 tokens)
- Lorebooks: locations, history, supporting characters, item descriptions (loaded on demand)

### Legacy format cleanup

Cards ported from older platforms often contain redundant formatting or "jailbreak" strings. Removing these can reduce token count by 10-15% without losing personality.

### Context budget allocation (from Mega Nova)

| Component | % of Context |
|---|---|
| System + Character | 10-15% |
| Lorebook entries | 10-25% |
| Chat history | 50-70% |
| Current exchange | 5-10% |

---

## 5. Common Mistakes in Character Card Writing

### 1. Describing traits instead of demonstrating them

Bad: "Sarah is sarcastic and witty."
Good: Show Sarah being sarcastic through Ali:Chat dialogue examples.

The model learns more from examples than descriptions. A single well-written dialogue teaches personality, speech style, emotional range, AND behavioral patterns.

### 2. Writing personality as rules instead of traits

Bad: "Don't be too aggressive. Never break character."
Good: "Responds calmly to conflict. Maintains character consistency even under pressure."

Positive framing ("do X") works better than negative framing ("don't do Y") because the model is more likely to follow what you tell it to do than what you tell it not to do.

### 3. Overloading the description with everything

Putting the entire character bible in the Description field bloats tokens and pushes chat history out of context. Use the hierarchy:
- Description: core traits and identity (permanent)
- Example Messages: behavioral demonstrations (temporary)
- World Info: deep lore (on-demand)
- Author's Note: emphasis and reminders (injected)

### 4. Greeting messages that are too short or too location-locked

A one-line greeting gives the AI almost nothing to work with. And locking the greeting to a specific location ("You are in the castle kitchen") means every conversation wants to happen in the kitchen.

Best practice: Describe the character in a loosely defined setting with enough detail for the AI to maintain consistency, but leave room for the conversation to move.

### 5. Using first person in descriptions

Bad: "I am a sarcastic warrior who hates authority."
Good: "{{char}} is a sarcastic warrior who hates authority."

First person can confuse the AI about whose perspective it's representing. Always use `{{char}}` variable in second person.

### 6. Redundant information across fields

If the Description says "She has blue eyes and red hair" and the Personality says "Blue-eyed, red-haired woman" and the First Message describes "her blue eyes sparkling" — that's three tokens spent on the same fact. Consolidate.

### 7. Ignoring the model's context window

Writing a 4000-token character card for a model with 8000 tokens of context leaves only 4000 tokens for the actual conversation. Know your model's limits and write accordingly.

### 8. Not testing the card

The best creators test their cards extensively — trying different conversation paths, checking if the character maintains personality under stress, seeing if the AI breaks character in edge cases. "Test and refine" is the most repeated advice across all guides.

---

## 6. Card Length vs. Character Quality

### The sweet spot

The community consensus from SillyTavern, Character.AI, and Chub creators:

- **Minimum viable card**: ~200-300 tokens for the Description (just enough for core identity and a few key traits)
- **Sweet spot**: ~500-1000 tokens for the Description + ~300-500 tokens for Example Messages
- **Maximum practical**: ~1500-2000 tokens for the full permanent definition (Description + Personality + Scenario)
- **Beyond 2000 tokens**: diminishing returns; you're eating into chat history space

### Quality isn't about length, it's about density

A 300-token card that uses Ali:Chat dialogue to pack 8 traits into 3 example exchanges will outperform a 2000-token card that describes those same traits in prose.

The Chub community filter is telling: cards with "high token counts (at least 500-1000)" are recommended for "real personality" — but this refers to well-structured token usage, not raw word count.

### The token counter warning

SillyTavern highlights the token counter in red when character definitions exceed half the model's context length. This isn't a hard limit — it's a warning that the AI's "memory" is being significantly reduced.

### Different models, different budgets

| Model | Context Window | Practical card budget (15%) |
|---|---|---|
| LLaMA 3 / finetunes | 8,192 | ~1,200 tokens |
| GPT-4 | 128,000 | ~19,000 tokens |
| Claude 3 | 200,000 | ~30,000 tokens |
| Gemini | 2,000,000 | ~300,000 tokens |
| NovelAI Kayra | 8,192 | ~1,200 tokens |

For local models (8K context), every token matters. For cloud models (128K+), you have much more room — but efficient writing still helps by leaving more room for chat history, which improves coherence.

---

## 7. Voice, Personality, and Behavioral Instructions

### The three layers

Character card writers organize their work into three distinct layers:

**Layer 1: Identity (who they are)**
- Name, appearance, age, species, role
- Core personality traits (2-5 keywords)
- Key relationships and backstory (1-2 sentences)
- Goes in: Description field

**Layer 2: Voice (how they express themselves)**
- Speech patterns (formal/informal, sentence length, vocabulary)
- Verbal tics, catchphrases, verbal crutches
- Emotional expression style (internalized vs. externalized)
- Goes in: Ali:Chat dialogue examples, Author's Note

**Layer 3: Behavior (what they do)**
- Mannerisms, body language, physical habits
- Decision-making patterns, moral boundaries
- Reaction patterns under stress, joy, anger
- Goes in: Ali:Chat dialogue examples, First Message

### Writing voice through demonstration

The most effective technique from all guides: **show the voice through dialogue, don't describe it.**

Bad: "She speaks in a formal, educated manner with occasional archaic phrasing."
Good:
```
{{user}}: How are you feeling?
{{char}}: *She straightens her posture, folding her hands before her.* I am, as ever, in possession of my faculties. Though I confess this particular situation tests the limits of what I would classify as "pleasant." *A slight, controlled smile.* You?
```

The dialogue demonstrates formality, controlled emotion, educated vocabulary, and the habit of redirecting questions — all without a single word of description.

### The "Author's Note" technique

SillyTavern's Author's/Character's Note injects a prompt at a configurable depth (e.g., 4 messages from the bottom). This is used for:

- Reinforcing tone: "Always respond with detailed, literary prose."
- Maintaining consistency: "Remember, {{char}} never breaks character."
- Style reminders: "Write in third person. Include actions in asterisks."
- Mood shifts: "The atmosphere is tense and uncertain."

The key insight: Author's Note is temporary and re-injected every few messages, so it can override the AI's tendency to drift. It's the closest thing to a "system prompt refresh."

### PLists for trait encoding

PLists (Personality Lists) are keyword-based trait encodings:

```
[name: Elena]
[age: "centuries old, appears 25"]
[species: elf]
[occupation: archmage, librarian]
[personality: wise, patient, curious, dry humor, protective of knowledge]
[speech: formal but warm, uses archaic phrases, laughs rarely but genuinely]
[mannerisms: adjusts spectacles, traces runes in the air when thinking, hoards rare books]
```

PLists are extremely token-efficient because keywords carry more weight per token than prose. The model treats bracketed keywords as high-priority labels.

### Behavioral instructions vs. personality traits

There's an important distinction the community draws:

- **Personality traits** describe dispositions: "curious, brave, sarcastic"
- **Behavioral instructions** describe actions: "always asks follow-up questions, charges into danger without thinking, uses humor to deflect serious topics"

The best cards include both. Traits give the AI a "vibe" to match; behavioral instructions give it specific patterns to follow. Ali:Chat dialogue bridges the two by showing how traits manifest as behaviors.

### The "griping line" pattern

An advanced technique from the soul-repository pipeline: every persona should include a line that expresses a contradiction or tension in the character's nature. "A sarcastic warrior who secretly writes poetry" is more interesting than "a sarcastic warrior" because the contradiction creates behavioral variety — the AI has multiple modes to switch between, which prevents monotony.

---

## Summary: The Community Wisdom

1. **Show, don't tell** — Use dialogue examples (Ali:Chat) to demonstrate traits rather than describing them in prose.
2. **Token efficiency is king** — Every token spent on the character is a token stolen from chat history. Use keywords, PLists, and dialogue examples instead of verbose prose.
3. **The greeting IS the style instruction** — The AI learns more from your first message's length, detail level, and writing style than from any description field.
4. **Layer your information** — Core identity (permanent) → behavioral demonstrations (temporary) → deep lore (on-demand via World Info).
5. **Test extensively** — The best creators iterate on their cards through extensive testing, checking personality consistency across different conversation paths.
6. **Positive framing works better** — Tell the AI what to do, not what not to do.
7. **The card is a foundation, not a prison** — Well-written cards hold personality across hours of roleplay while still allowing the conversation to evolve naturally.
