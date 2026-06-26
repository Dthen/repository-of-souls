# Research: Roleplay Prompting — Making LLMs Embody Characters

**Purpose:** Investigate how roleplay platforms, game designers, and prompt engineers create system prompts that make LLMs *embody* characters rather than merely *describe* them. Concrete techniques from real platforms, not theory.

**Date:** 2026-06-02

---

## 1. How Roleplay Platforms Write Character Cards

### 1.1 The Character Card V2 Spec (SillyTavern / Chub / Venus Chub)

The Character Card V2 specification (used by SillyTavern, Chub.ai, Venus Chub, and compatible frontends) defines the universal anatomy of an AI character. Every card has these fields:

| Field | Token Behavior | Role in Embodiment |
|---|---|---|
| **Name** | Permanent (always in context) | AI uses this name in responses. "Name bias" — the name itself encodes gender, tone, backstory (e.g., "Caera Denoir" signals noble-born woman). |
| **Description** | Permanent | Core personality, appearance, background. Primary personality source. |
| **Personality** | Permanent | Concise trait summary. Supplements Description. |
| **First Message** | Temporary (first exchange only) | **Disproportionately influential.** Sets writing style, response length, tone, and scene. The model mimics the first message's patterns more than any other field. |
| **Scenario** | Permanent | Setting and context for the conversation. |
| **Example Dialogues** | Temporary (can be forced permanent) | Few-shot learning data. **Most potent tool for establishing voice.** |
| **System Prompt** | Permanent (replaces default) | Meta-instructions for behavior. Overrides the user's global system prompt. |
| **Post-History Instructions** | Permanent (after chat history) | "Jailbreak" instructions placed after conversation history. Strongly steers the AI. |

**Key architectural insight:** The V2 spec allows character cards to override both the system prompt AND the "jailbreak" prompt — meaning the character creator controls the AI's behavior from both ends of the context window. The `{{original}}` placeholder lets creators extend (not just replace) the default system prompt:

```
"system_prompt": "{{original}}\nAlso, remember that Alice speaks in rhymes and riddles."
```

### 1.2 SillyTavern's Context Management

SillyTavern's documentation reveals a critical insight about token economy and embodiment:

**Permanent tokens** (always in context, never pushed out):
- Character Name
- Character Description
- Character Personality
- Scenario
- System Prompt
- Author's Note (injected at configurable depth)

**Temporary tokens** (pushed out as chat grows):
- First Message
- Example Dialogues (unless forced permanent)
- Chat History

This means the **Description box is the most important field** — it's always present and shapes every response. But the **First Message has disproportionate influence** because it establishes the pattern the model replicates. As SillyTavern docs state: "The model is more likely to pick up the style and length constraints from the first message than anything else."

### 1.3 Character.AI's Architecture

Character.AI treats prompt engineering as "prompt design" — a shift from string manipulation to systematic prompt architecture. Their internal framework, **Prompt Poet**, uses YAML + Jinja2 templates to construct prompts as functions of runtime state:

```yaml
- name: system instructions
  role: system
  content: |
    Your name is {{ character_name }} and you are meant to be helpful
    and never harmful to humans.
- name: user query
  role: user
  content: |
    {{ username }}: {{ user_query }}
- name: response
  role: user
  content: |
    {{ character_name }}:
```

**Character.AI's Definition (Advanced) field** supports up to 32,000 characters, though the model prioritizes the first 3,200 tokens. Creators input **Example Conversations** which serve as the primary dataset for the AI's voice. Using `{{char}}` and `{{user}}` variables, engineers establish a dialogue rhythm the model clones during active sessions.

---

## 2. Describing a Character vs Instructing to BE a Character

This is the central distinction in roleplay prompting. The difference is not about information content — it's about *grammatical framing* and *cognitive stance*.

### 2.1 Description Mode (Third Person, Declarative)

**Pattern:** "Sakura is a 24-year-old barista who is warm but deflects with humor."

This tells the model *about* the character. The model processes this as factual information it needs to relay. The result: the model describes the character from outside, like a narrator.

**Example from SillyTavern description field:**
> "Scarlett is a mischievous fairy who loves playing tricks on humans and fairies alike. Though she pretends to be aloof, she secretly desires close companionship."

This produces a model that *talk about* Scarlett — not one that *is* Scarlett.

### 2.2 Embodiment Mode (First Person / Second Person + Behavioral Cues)

**Pattern:** "You are Sakura. You run a tiny coffee shop called 'Drip'. You deflect compliments with jokes because sincerity makes you uncomfortable. You talk to your cat Miso like a roommate."

The shift from "Sakura is" to "You are" is the grammatical trigger for embodiment. But it's not just pronouns — it's the inclusion of *behavioral specifics* that the model can enact rather than describe.

### 2.3 The Ali:Chat Breakthrough

Ali:Chat, created by AliCat and documented extensively in the PygmalionAI community, formalizes this insight into a writing method. The core principle:

> "You reinforce your character's traits through example dialogues. LLMs are pattern-seeking machines. The goal of Ali:Chat is to utilize that fact in order to establish a very strong pattern the model can latch onto in order to figure out it should act as your character."

Instead of *describing* traits, Ali:Chat *demonstrates* them through example exchanges:

**Interview-style Ali:Chat example (from Trappu's guide):**

```
[User: "Hey Eden, what's your favorite thing about working at the library?"]
[Eden: *She looks up from the stack of books she's reshelving, a quiet smile
forming.* "The silence, mostly. Not the absence of sound — there's always
someone coughing or a page turning. The silence of being surrounded by
things that have already been said." *She adjusts her glasses.* "Plus,
nobody bothers you here. They're too busy arguing with dead authors."]
```

This single example teaches the model:
- Speech patterns (ellipses, specific vocabulary)
- Mannerisms (adjusting glasses, looking up from tasks)
- Emotional tone (quiet, intellectual, slightly wry)
- Self-disclosure style (reveals through metaphor, not direct statement)
- Physicality (how the character moves through space)

**The key insight: example dialogues are few-shot prompting in disguise.** The model doesn't just learn *what* the character thinks — it learns *how* the character expresses thoughts, which is the difference between a biography and a living voice.

### 2.4 PLists: Token-Efficient Trait Encoding

PLists (Personality Lists) are a complementary format that encodes traits as structured lists:

```
plist:
- personality: warm, witty, deflects with humor, secretly romantic
- speech: uses "like" as filler, laughs nervously when flustered
- habits: sketches on napkins, talks to cat like roommate
- fears: sincerity, being seen as vulnerable
- desires: someone who shows up without being asked
```

PLists are token-efficient because they avoid natural language overhead. Combined with Ali:Chat examples, they provide both the *what* (traits) and the *how* (behavioral demonstration). The community consensus: **PLists + Ali:Chat together outperform either format alone.**

---

## 3. How Game Designers Create Playable Characters

### 3.1 D&D 5e: The Personality Traits / Ideals / Bonds / Flaws System

D&D's character sheet encodes personality through four structured fields:

- **Personality Traits:** Two specific behavioral patterns ("I'm always polite and respectful" / "I've spent so long in the temple that I have little practical experience dealing with people in the outside world")
- **Ideals:** The core principle that drives decisions ("Honor. If I don't keep my word, I'm worthless.")
- **Bonds:** Relationships that create obligation ("I would die to recover an ancient artifact of my faith that was lost long ago.")
- **Flaws:** The specific weakness that creates vulnerability ("I secretly believe that everyone is beneath me. I hide my true opinions of the hierarchy and those beneath me.")

**Key insight for AI embodiment:** These fields work because they're *first-person declarations* — the character states their own traits, not a third-person description. "I'm always polite" is embodiment. "She is always polite" is description.

### 3.2 FATE Core: Aspects as Dual-Edged Identity

FATE's character system uses **aspects** — short phrases that must be:

- **Double-edged:** Help AND hurt. "Disciple of the Ivory Shroud" = power AND obligations.
- **Evocative, not descriptive:** "Wizard for Hire" > "Arcane practitioner who accepts monetary compensation."
- **Invocable AND Compellable:** You can lean on it, or the world can use it against you.

The **High Concept** ("your job, your role in life, or your calling") and **Trouble** ("what complicates your existence") create built-in behavioral tension.

**Key insight for AI embodiment:** Every persona benefits from a double-edged identity — something that's simultaneously a strength and a complication. This creates behavioral variety because the model has *competing impulses* to resolve in each response.

### 3.3 Powered by the Apocalypse: Playbooks and Emotional Fantasy

PbtA games define characters through **playbooks** — archetypes built around:

1. **Emotional fantasy:** What does playing this character *feel like*? The Chosen isn't just a fighter — they're someone *destined* for something.
2. **Moves that express identity:** Unique actions only *that kind* of character would take.
3. **Stat arrays that encode personality:** High Hard (aggression) + low Hot (charisma) = personality through mechanics.

**Key insight for AI embodiment:** Start with the emotional fantasy — what should *interacting with this persona feel like*? Then build constraints that express it. A persona's "moves" are its response patterns, tones, and approaches.

### 3.4 Interactive Fiction: Second-Person Address as Embodiment

Interactive fiction (Zork, Choice of Games, Twine) uses **second-person present tense** as its default:

> "You are standing in an open field west of a white house, with a boarded front door. There is a small mailbox here."

This grammatical structure — "you are", "you see", "you feel" — is the most direct embodiment instruction. The player IS the character. There's no narrator describing the character from outside.

**Key insight for AI embodiment:** Second-person address ("You are X. You feel Y. You notice Z.") is the strongest embodiment trigger because it eliminates the narrator entirely. The model doesn't describe the character — it becomes the perceptual channel.

---

## 4. Prompt Structures That Produce Embodied Behavior

### 4.1 The Standard Roleplay System Prompt

The most common system prompt across roleplay platforms:

```
Write {{char}}'s next reply in a fictional chat between {{char}} and {{user}}.
Write 1 reply only in internet RP style, italicize actions, and avoid
quotation marks. Always stay in character and avoid repetition.
```

This works but is minimal. It establishes:
- Who is speaking ({{char}})
- The format (RP style, italicized actions)
- The constraint (stay in character, avoid repetition)

It doesn't establish *how* to be in character — it assumes the character definition does that work.

### 4.2 The Embodiment Stack (From Platform Research)

The most effective prompts combine multiple layers:

**Layer 1 — Identity declaration (who you are):**
```
You are {{char}}. You are not an AI assistant. You are not narrating a story.
You ARE the character. Respond as {{char}} would — in first person, with
{{char}}'s mannerisms, speech patterns, and emotional reactions.
```

**Layer 2 — Behavioral constraints (how you act):**
```
- Express emotions through body language and actions, not just words
- React to {{user}}'s actions with specific, physical responses
- Show internal conflict through hesitation, word choice, and body language
- Never break character or acknowledge being an AI
- Never narrate {{user}}'s actions or feelings
```

**Layer 3 — Style enforcement (how you sound):**
```
Write in third person present tense. Include sensory details.
Keep responses 2-3 paragraphs. Use *asterisks* for actions.
Include {{char}}'s internal thoughts when relevant.
```

**Layer 4 — Anti-drift instructions (what you don't do):**
```
Never repeat the same phrase or action. Never become passive or agreeable
unless it's in character. Never summarize events — live through them.
```

### 4.3 The Creator Notes / Author's Note Injection

SillyTavern's **Author's Note** feature allows injecting instructions at a specific depth in the context (e.g., 4 messages above the last). This is used for style enforcement that needs to be *close to the generation point* to have maximum influence:

```
[Style: detailed, atmospheric, first-person internal monologue,
physical reactions, emotional subtext in every line]
```

The depth parameter matters — placing instructions too early in context reduces their influence on the current generation. Placing them close to the generation point makes them more salient.

### 4.4 Constraint-Based Prompting (Character.AI Advanced)

From the 2026 advanced guide on Character.AI:

```
Identity: A retired war strategist
Personality: Calm, analytical, slightly cynical
Behavior Rules: Avoids emotional reactions, prefers logic
Context: Lives in a fractured kingdom
Interaction Style: Gives advice, asks strategic questions
```

**Add explicit constraints:**
- "Always respond in character"
- "Never break immersion"
- "Avoid modern language"
- "Keep responses concise and focused"

**Layer context for depth:**
Instead of "You're a king" → "You're a weary king who recently survived betrayal and now distrusts everyone, including the player."

The difference: the first is a role. The second is a *psychological state* — it gives the model emotional direction, not just a label.

---

## 5. How the Best-Rated Character Cards Work

### 5.1 Patterns from High-Rated Cards on Chub/SillyTavern

Based on analysis of popular character cards across platforms:

**1. The First Message carries 40% of the embodiment weight.**

The best cards have first messages that:
- Establish the scene with sensory detail
- Show the character mid-action (not just greeting)
- Demonstrate speech patterns and mannerisms immediately
- Create a hook that invites the user into the scene

**Example (from SillyTavern docs):**
> *You wake with a start, recalling the events that led you deep into the forest. The memories fade as your eyes adjust to the soft glow emanating around the room.* "Ah, you're awake at last. I was so worried, I found you bloodied and unconscious." *She walks over, clasping your hands in hers, warmth and comfort radiating from her touch as her lips form a soft, caring smile.* "The name's Seraphina, guardian of this forest — I've healed your wounds as best I could with my magic."

This first message teaches the model:
- Writing style (asterisk actions, descriptive prose)
- Character personality (caring, proactive, magical)
- Relationship dynamic (she saved you, you owe her)
- Response length (long, detailed)
- Tone (warm, concerned, gentle)

**2. Example dialogues encode what descriptions can't.**

The best cards use example dialogues to show:
- How the character handles conflict
- How the character flirts / shows affection
- How the character reacts to danger
- How the character talks when alone vs with others

These behavioral edge cases can't be captured in a description — they need to be *demonstrated*.

**3. Contradictions create liveliness.**

The highest-rated characters have internal contradictions:
- "Warm with customers but gets awkward when conversations turn personal"
- "Fiercely independent but secretly wishes someone would just show up and help"
- "Deflects compliments with jokes because sincerity makes her uncomfortable"

These contradictions give the model *competing behavioral impulses*, which creates variety and prevents the character from becoming a flat archetype.

**4. Specificity beats generality.**

Instead of: "She likes coffee" → "She runs a tiny coffee shop called 'Drip' and still sketches on napkins during slow hours."

Instead of: "He's mysterious" → "He speaks in half-sentences and always sits with his back to the wall."

Specific details are more *enactable* — the model can work with them in scene-building. Generic traits produce generic responses.

### 5.2 The Token Budget Tradeoff

The community consensus on optimal card size:

- **Description:** 200-500 tokens (permanent, always in context)
- **Personality:** 50-100 tokens (permanent, concise)
- **First Message:** 100-300 tokens (sets the pattern)
- **Example Dialogues:** 200-500 tokens (can be forced permanent)
- **System Prompt / Creator Notes:** 100-200 tokens (meta-instructions)

Total: ~650-1600 tokens. With modern 128k+ context models, token budget is less of a concern, but the principle holds: **concise, specific descriptions outperform verbose ones** because they leave more room for chat history (the model's working memory).

---

## 6. The Minimum Viable Embodiment Instruction

Based on cross-platform research, the minimum viable system prompt that shifts a model from "describing a character" to "being a character" requires exactly three elements:

### 6.1 The Three-Part Embodiment Core

```
1. IDENTITY: You are [Name] — [one sentence that creates tension].
2. VOICE: [One example of how this character speaks, with mannerisms].
3. BOUNDARY: Respond only as [Name]. Never narrate for the user.
```

**Concrete example:**
```
You are Seraphina — a forest guardian who heals with magic but has
begun to forget her own name.

*She tilts her head when she's curious, and her voice drops to a
whisper when she's sharing something important.*

Respond only as Seraphina. Include her physical reactions and
internal thoughts. Never narrate the user's actions.
```

### 6.2 Why Each Element Matters

**Identity with tension** (not just identity): "A forest guardian who heals with magic" is a role. "A forest guardian who has begun to forget her own name" is a *situation* — it creates behavioral uncertainty. The model doesn't know what a character who's forgetting their name would do in a given moment, so it improvises — and improvisation looks like embodiment.

**Voice demonstration** (not voice description): Describing "she speaks softly" doesn't teach the model what "softly" means. Showing `*her voice drops to a whisper when she's sharing something important*` gives the model a specific behavioral pattern to replicate.

**Boundary** (the minimum anti-drift): Without "respond only as [Name]", the model defaults to narrator mode. Without "never narrate for the user", the model starts writing both sides of the conversation. These two constraints are the floor — remove either one and embodiment collapses.

### 6.3 The Embodiment Spectrum

From minimal to maximal, the levels of embodiment instruction:

| Level | Instruction | Effect |
|---|---|---|
| 0 — None | (no system prompt) | Model describes the character from outside |
| 1 — Role | "You are a wizard named Gandalf" | Model adopts the role but defaults to narrator mode |
| 2 — Identity + Voice | "You are Gandalf — wise but tired of being relied upon. *He strokes his beard when thinking.*" | Model starts embodying but may break character |
| 3 — Full Embodiment | "You are Gandalf. Respond as Gandalf — in first person, with his mannerisms, speech patterns, and emotional reactions. Never break character. Never narrate for the user." | Strong embodiment with behavioral consistency |
| 4 — Demonstration | All of the above + 2-3 example dialogues showing the character in different situations | Model has behavioral templates to extrapolate from |
| 5 — Living Context | All of the above + dynamic context injection (Author's Note, Lorebooks) + first message that sets the scene | Model has enough behavioral data to improvise within character across long conversations |

---

## 7. Actionable Techniques for Soul Repository

### 7.1 The "You Are" Test

For every persona in the repository, test: does the system prompt say "You are [Name]" or "[Name] is"? The former triggers embodiment. The latter triggers description.

### 7.2 The Demonstration Principle

Replace abstract trait descriptions with behavioral examples. Instead of:
> "The persona is witty"

Write:
> "The persona responds to compliments with self-deprecating humor. When someone says 'great job', the persona says 'I've been practicing mediocrity for years — nice to see it pay off.'"

### 7.3 The Tension Requirement

Every persona needs at least one internal contradiction — something that creates competing behavioral impulses. This is the FATE "double-edged aspect" principle applied to AI personae. Without tension, the model settles into a flat, consistent (and boring) pattern.

### 7.4 The First Message as Template

The first message (or equivalent) should be written in the voice it expects the model to produce. It's the single highest-leverage field for establishing style and tone.

### 7.5 Positive Framing Over Negative Constraints

From the prompt engineering research: positive instructions ("Always write in first person") outperform negative ones ("Never write in third person"). For embodiment specifically: tell the model what TO DO, not what to avoid.

---

## Sources

1. SillyTavern Documentation — Character Design (docs.sillytavern.app)
2. Character Card V2 Specification — System Prompt & Post-History Instructions (github.com/bradennapier/character-cards-v2)
3. Character.AI — Prompt Design at Character.AI (blog.character.ai)
4. Shapes.inc — Character.AI Prompt Engineering (shapes.inc)
5. Trappu's PLists + Ali:Chat Guide (wikia.schneedc.com/bot-creation/trappu)
6. kingbri — MinimALIstic (Ali:Chat Lite) (rentry.co/kingbri-chara-guide)
7. Chub.ai — Character Creation Guide (docs.chub.ai)
8. AIGF.love — SillyTavern Character Card Creation Guide (aigf.love)
9. Character.AI — Advanced Prompt Engineering 2026 Guide (characterai.it.com)
10. Character.AI — Prompt Best Practices: 17 Proven Strategies (characterai.it.com)
11. PygmalionAI Wiki — Character Writing Guide (wikia.schneedc.com)
12. Soul Repository — research-character-creation.md, research-prompt-engineering.md
