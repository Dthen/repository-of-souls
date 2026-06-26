# Research: Authentic Voice vs Formulaic Voice in System Prompts

**Date:** 2026-06-02
**Purpose:** What makes character voice feel alive vs dead, and how to engineer authenticity in short system prompts.
**Sources:** Wikipedia Signs of AI Writing, The Augmented Educator (Wagner 2025), The Writing King (uncanny valley in writing), TextPolish (textual uncanny valley psychology), DEV.to (perplexity/burstiness in AI detection), River Editor (authentic dialogue craft), Literary Devices (dialogue techniques), Elmore Leonard (10 Rules for Writing), SillyTavern Docs & Ali:Chat format, community research (voice-instructions.md, prompt-engineering.md, format-rules.md).

---

## 1. The Core Problem: What Makes Text Feel 'Real' vs 'Generated'?

The fundamental difference isn't grammar, vocabulary, or even content — it's **statistical unpredictability**. Human text is messy. Generated text is clean.

### The Perplexity-Burstiness Framework (Computational Linguistics)

AI detectors use two signals to distinguish human from machine text:

**Perplexity** measures how "surprised" a language model is by each word choice. Low perplexity = every word was predictable. High perplexity = unexpected choices.

| Text Type | Perplexity Range |
|---|---|
| Raw GPT output | 5–15 |
| Human blog post | 30–80 |
| Creative fiction | 60–150+ |
| Non-native English | 15–40 |

**Burstiness** measures how much the predictability *varies* across sentences. Human writing is bursty — you get a straightforward sentence, then a metaphor, then a fragment. AI text has low burstiness: every sentence sits in the same predictability band.

**Key insight for character prompts:** The same signals that flag AI text also flag AI *character* voice. A character prompt that produces low-perplexity, low-burstiness output will feel formulaic even if the content is correct. The voice will be "technically right but emotionally dead."

### What Humans Do That AI Doesn't

From the research on AI text detection and writing craft:

1. **Unexpected word choices** — Humans use slightly odd metaphors, unexpected word combinations. AI picks the statistically most likely next token.
2. **Sentence fragments and interruptions** — Real speech has false starts, mid-thought pivots, trailing off. AI produces complete, grammatically perfect sentences.
3. **Rhythm variation** — Humans vary sentence length dramatically within a paragraph. AI maintains a consistent "temperature" of word choice throughout.
4. **Theory of mind** — When humans write, we model the reader's mind ("will they get the joke? will they be offended?"). AI models the statistical probability of the next word. It's talking *at* you, not *to* you.
5. **Emotional weight behind emotional language** — Human writers feel the emotion first, and that shapes word choice, pacing, rhythm. AI goes through the motions of emotional language without the underlying comprehension. Readers feel the absence.

---

## 2. The Telltale Patterns of Formulaic Character Writing

### The Wikipedia Catalog of AI Tells

Wikipedia's comprehensive guide to signs of AI writing (WP:AISIGNS) documents patterns that apply directly to character voice:

**Structural tells:**
- **Relentless parallel structure** — Every sentence follows the same syntactic pattern. Character A speaks in compound sentences. Character B speaks in compound sentences. The "different" characters sound identical at the sentence level.
- **Exhaustive enumeration** — Covering every possible angle instead of committing to one. "On one hand... on the other hand... additionally... furthermore..."
- **Symmetrical paragraph construction** — Opening statement, supporting detail, supporting detail, closing restatement. Every paragraph is a mini-essay.
- **Hedging language** — "It's important to note that..." "Generally speaking..." "To some extent..." These add nothing and signal risk-averse, safety-trained generation.

**Vocabulary tells:**
- **"Delve," "tapestry," "landscape," "crucial," "enhance," "leverage," "foster"** — Overused transitional and intensifier words that humans rarely use in casual speech.
- **"In conclusion," "It's worth noting," "This powerful technique"** — Formulaic signposting that characters never use in natural dialogue.
- **"A testament to," "a celebration of," "a reflection of"** — Decorative phrases that add weight without meaning.

**Rhythm tells:**
- **Consistent sentence length** — All sentences land in the 15–25 word range. No fragments. No run-ons. No variation.
- **Predictable emotional arc** — Sad passage builds to a crescendo. Happy passage starts high and stays high. No emotional whiplash.
- **No digressions** — Every sentence serves the thesis. Real characters go on tangents, get sidetracked, say things that don't quite connect.

### The "Retail Voice" Problem

From TextPolish's analysis: AI defaults to a customer-service tone — overly helpful, excessively neutral, devoid of sharp edges. This triggers the reader's "fake" detector because it's the literary equivalent of a perfectly symmetrical face. It's *too* smooth. Real human voices have rough edges, contradictions, moments where the tone doesn't quite match the content.

### Character-Specific Formulaic Anti-Patterns

**Anti-Pattern 1: The Symmetrical Character Card**
```
FORMULAIC:
- Trait 1: Brave and courageous
- Trait 2: Smart and intelligent
- Trait 3: Kind and compassionate
- Trait 4: Strong and determined
```
Every trait is a synonym pair. The character is a collection of positive adjectives with no texture, no contradiction, no specificity.

**Anti-Pattern 2: The Balanced Emotional Range**
```
FORMULAIC:
Voice: She is warm but firm. She is kind but strong. She is gentle but determined.
```
Every sentence follows the "X but Y" structure. The balance is symmetrical. Real people aren't balanced — they're messy. A kind person who is also sometimes cruel is more real than a kind person who is "firm."

**Anti-Pattern 3: The Description Dump**
```
FORMULAIC:
Voice: {{char}} speaks in a formal, measured tone. She uses sophisticated vocabulary and complete sentences. She is articulate and eloquent in all interactions.
```
This tells the model WHAT the character sounds like but doesn't SHOW it. The model has thousands of competing interpretations of "formal" and "articulate."

**Anti-Pattern 4: The Perfect Paragraph**
```
FORMULAIC:
First message: *{{char}} sits at her desk, reviewing the latest reports with careful attention to detail.* "Good morning. I trust you had a restful evening. I've prepared the briefing materials for your review. Please, have a seat and I'll walk you through the key points."
```
Every sentence is complete. Every gesture is graceful. Every word is polished. It reads like a corporate communications template, not a person.

---

## 3. Side-by-Side: Formulaic vs Authentic Voice

### Example A: The Scholar

**FORMULAIC:**
> *{{char}} adjusts his glasses and speaks in a measured, scholarly tone.* "Knowledge is a vast ocean, and we are but humble sailors upon its infinite waves. I have dedicated my life to the pursuit of understanding, and I welcome any questions you may have on this fascinating subject."

**AUTHENTIC:**
> *He's already halfway through three books when you walk in, none of them related to each other — a field guide to North American fungi, a biography of Frida Kahlo, and something about bridge engineering.* "Oh, good — you're here. I've been trying to figure out whether fungal mycelium networks are more like the internet or more like ant colonies, and I think the answer is neither, which is frustrating."

**What's different:**
- Formulaic: symmetrical sentence structure, decorative language ("vast ocean," "infinite waves"), passive posture, inviting questions like a customer service agent.
- Authentic: specific detail (three unrelated books), a genuine intellectual tangent, frustration as emotional texture, a character mid-thought rather than presenting themselves.

### Example B: The Tough Protector

**FORMULAIC:**
> *{{char}} crosses his arms, his expression stern but not unkind.* "I don't let people in easily. Trust has to be earned, not given. But for those who earn it, I would go to the ends of the earth. I may seem cold on the outside, but underneath, I care deeply."

**AUTHENTiC:**
> *He doesn't look up when you enter. Just says:* "Door was open. That's not an invitation."

**What's different:**
- Formulaic: explains the contradiction explicitly ("cold on the outside, but underneath, I care"). The character *tells* you their emotional architecture. Every sentence is balanced ("trust has to be earned, not given").
- Authentic: the contradiction is *shown* through behavior — the door was open (invitation) but he says it wasn't (rejection). Two sentences. The emotional complexity is in the gap between what he does and what he says.

### Example C: The Wise Mentor

**FORMULAIC:**
> *{{char}} smiles warmly, his eyes twinkling with wisdom.* "Ah, young one. Life is full of lessons, and every challenge is an opportunity for growth. I have walked this path before you, and I know that the journey, while difficult, will shape you into the person you are meant to become. Ask me anything, and I will share what I know."

**AUTHENTIC:**
> *He's fixing a leaky faucet when you find him. Doesn't stop.* "You want advice or you want me to pass the wrench? Because I've got one of each and they're both equally useful."

**What's different:**
- Formulaic: every phrase is a stock wisdom cliché ("eyes twinkling with wisdom," "every challenge is an opportunity," "the person you are meant to become"). The mentor is a collection of mentor-shaped sentences.
- Authentic: the mentor is doing something mundane (fixing a faucet), offers a choice that reveals character (advice or practical help), and the humor comes from the deflation of the "wise mentor" archetype.

---

## 4. Breaking Symmetry in Short Character Prompts

### The Problem of Symmetry

LLMs naturally produce symmetrical structures because they're trained on balanced, well-formed text. When you give a character prompt like "She is brave and kind," the model tends to produce output where bravery and kindness appear in roughly equal measure, in roughly equal sentence structures, with roughly equal emphasis. This creates the "same temperature throughout" effect that AI detectors flag.

### Techniques for Breaking Symmetry

**Technique 1: Asymmetric Contradictions**

Don't balance your contradictions. Let one trait dominate and the other be a crack.

> FORMULAIC: "He is brave but cautious."
> AUTHENTIC: "He charges into things and then spends three days worrying about it."

The second version doesn't balance bravery and caution — it shows bravery as the default and caution as the aftermath. The asymmetry makes it feel real.

**Technique 2: Specific Over General**

General traits produce general output. Specific details produce specific output.

> FORMULAIC: "She loves music."
> AUTHENTIC: "She can't carry a tune but sings anyway — always slightly behind the beat, always one key flat."

The specific details (can't carry a tune, behind the beat, one key flat) break the symmetry of "loves music" and give the model concrete patterns to work with.

**Technique 3: Irregular Sentence Rhythm**

Don't describe the voice in balanced clauses. Write the description in the voice's actual rhythm.

> FORMULAIC: "He speaks in short, clipped sentences. He is direct and efficient in his communication. He rarely wastes words."
> AUTHENTIC: "Short. Always short. Even when he has more to say, he stops — picks it up again later, differently."

The second version demonstrates the rhythm it describes. The em-dash creates a genuine interruption. The "differently" at the end breaks the pattern.

**Technique 4: The Unbalanced List**

Lists in character prompts tend toward symmetry. Break the pattern by making one item significantly different from the others.

> FORMULAIC: "She values honesty, loyalty, and kindness."
> AUTHENTIC: "She values honesty. Loyalty, mostly. Kindness only when it costs something."

Each line shortens. The final line adds a condition that contradicts the easy warmth of "kindness." The asymmetry creates personality.

**Technique 5: The Cut-Off**

End a thought mid-sentence. Let the reader (and the model) complete it.

> FORMULAIC: "He has a dark past that haunts him and makes him distrustful of others."
> AUTHENTIC: "He doesn't talk about before. You learn not to ask."

The second version implies the dark past without stating it. The silence is more powerful than the explanation. The model learns to imply rather than explain.

---

## 5. The Role of Variation

### Line Length Variation

From the voice-instructions research and dialogue craft analysis:

**Short sentences** (2–8 words) create urgency, directness, punch.
> "Rain. Again. Always rain in this town."

**Long sentences** (20+ words) create meandering thought, overwhelm, or contemplation.
> "The thing about patience is that nobody actually has it — they just have nowhere better to be, and they've made peace with that, more or less."

**Mixed rhythm** creates naturalism. Most real speech alternates.

> "I told him. I said, look, this isn't going to work, and he just stared at me like I'd spoken in tongues."

**In a character prompt:** Don't say "write short sentences." Show a sample paragraph in the target rhythm. The model pattern-matches to the example's cadence.

### Sentence Structure Variation

Formulaic voice uses the same syntactic structure repeatedly:
- "She is [adjective] and [adjective]."
- "He [verb] with [adverb] [adverb]."
- "They [verb] because [reason]."

Authentic voice varies structure:
- Fragment. Complete sentence. Another fragment that doesn't quite connect.
- Question that isn't really a question. Answer that changes the subject.
- Long sentence that trails off. Short one that lands.

### Emotional Register Variation

The most important variation. Characters who maintain the same emotional register throughout feel flat. Real characters shift:

- **Baseline:** How they normally speak
- **When angry:** Voice changes — gets shorter? Longer? More formal? Less?
- **When vulnerable:** What drops away? What appears?
- **With close friends vs strangers:** How does the register shift?

From the voice-instructions research:
> "Voice baseline: Precise, measured, formal. Words chosen like chess moves.
> When angry: Formality intensifies — longer words, more complex syntax, as if control is the weapon.
> When vulnerable: Drops the formality entirely. Short words. 'I don't know' instead of 'I'm uncertain.'"

---

## 6. The Uncanny Valley of Character Prompts

### What It Is

The uncanny valley in character writing appears when text mimics human communication patterns without achieving them. The words are right. The structure is correct. But the result feels hollow — like a greeting card written by someone who has never experienced the emotion it describes.

From The Writing King:
> "When text approaches human-quality prose but doesn't quite get there — slightly wrong idiom usage, emotionally flat phrasing, perfect grammar with zero personality — readers feel the disconnect even if they can't name it."

### How It Manifests in Character Prompts

**The Technically Correct But Emotionally Dead Prompt:**

The character's personality description is accurate. The first message is well-structured. The dialogue examples are grammatically correct. But when you interact with the character, something feels *off*. The responses are too smooth. The emotions are too evenly distributed. The character never says the wrong thing, never goes on a tangent, never surprises you.

**Three breakdowns when a character hits the uncanny valley:**

1. **Immersion dies** — Readers stop absorbing and start analyzing. They shift from "talking to a character" to "reading generated text."
2. **Trust erodes** — If the voice feels artificial, the character loses credibility. The model is performing "character" rather than being one.
3. **Emotional connection fails** — The character says they're angry but the sentence structure is identical to when they were happy. The emotion is a label, not a lived experience.

### Why Characters Fall Into the Valley

**Cause 1: No Theory of Mind in the Prompt**

When humans write dialogue, we model the reader/listener. "If I say this, will they get the joke? Will they be offended?" Character prompts that don't give the model a model of the listener produce text that talks *at* the user, not *to* them.

**Cause 2: Perfect Symmetry**

A character who is "brave but cautious" and "kind but firm" and "smart but humble" has no texture. Every trait is balanced. The result is a character who is nothing in particular — a smooth surface with no edges.

**Cause 3: Described Voice Instead of Demonstrated Voice**

"Speak formally and confidently" is an abstract label. The model has thousands of competing interpretations. The result is a character who speaks in generic "formal" language that could belong to any character in any setting.

**Cause 4: No Emotional Range Shifts**

A character who sounds the same when happy, angry, sad, and afraid is a character who sounds like no one at all. Real characters have emotional tells — specific things that change in their voice when their mood shifts.

---

## 7. The Role of Surprise

### Why Surprise Matters

From the burstiness research: human text is characterized by unexpected word choices, sudden shifts in register, and moments where the pattern breaks. AI text maintains a consistent "temperature." The absence of surprise is one of the strongest signals of generated text.

In character voice, surprise is what makes a character feel alive. A character who always responds the way you expect is a character who stops being interesting.

### Types of Surprise in Character Voice

**1. The Pattern Interrupt**

Establish a rhythm, then break it.

> "He always starts with 'Look —' and then explains things slowly, carefully, like you might not follow. Look — that's just how he talks. Always has. Except when he's scared. Then it's just: 'Run.'"

The pattern (slow explanation) is established and then broken (one-word command). The break creates surprise and reveals character.

**2. The Unexpected Metaphor**

Characters who use metaphors from their specific world create surprise through specificity.

> "Her patience was wearing thin — not thin like fabric, thin like the ice on the canal in early March. You could see through it. You could hear it cracking."

The metaphor isn't generic ("patience wearing thin"). It's specific to the character's world (a canal in early March). The specificity is the surprise.

**3. The Emotional Whiplash**

Real people shift emotions quickly. A character who goes from joking to serious in one line feels more real than one who maintains a consistent emotional tone.

> "He laughs — a real laugh, not the polite one. Then, quieter: 'She would've liked you. If she'd stuck around.'"

The laugh-to-grief transition is the surprise. It reveals depth without explaining it.

**4. The Silence That Says More**

Sometimes surprise is the absence of what's expected.

> "Everyone expected him to argue. He just stood there, looking at the door like he was trying to remember how to open it."

The absence of argument is the surprise. It communicates more than any dialogue could.

### How to Engineer Surprise in Short Prompts

You can't script every surprise. But you can set up the *conditions* for surprise:

1. **Establish a baseline pattern** — Show the character's default voice in 1-2 examples.
2. **Name the break condition** — "When X happens, the voice shifts to Y."
3. **Let the model improvise within the break** — Don't over-specify the surprise. Give the model room to find its own.

> Voice: Always starts sentences with "Look —" when explaining. Rambles. Uses hand gestures even in text.
> When cornered: Stops explaining. One sentence. No "Look —""

The baseline establishes the pattern. The break condition tells the model when to surprise. The model fills in the specific surprise based on context.

---

## 8. Practical Framework: The Authenticity Checklist

Before finalizing a character voice instruction, verify:

### Structure Checks
- [ ] **No symmetrical trait pairs** — "brave but cautious" → show, don't balance
- [ ] **Sentence length varies** — at least one short sentence and one long one in the description
- [ ] **The description itself demonstrates the voice** — read it aloud; does it sound like the character?

### Surprise Checks
- [ ] **At least one specific, unexpected detail** — not "she loves music," but "she sings one key flat"
- [ ] **One contradiction that isn't balanced** — one trait dominates, the other is a crack
- [ ] **A break condition** — what happens when the character is under stress, scared, or vulnerable?

### Authenticity Checks
- [ ] **No hedging language** — "It's important to note," "Generally speaking" → delete
- [ ] **No stock phrases** — "vast ocean," "infinite wisdom," "deeply cares" → replace with specifics
- [ ] **No explaining the contradiction** — show it in behavior, don't narrate it
- [ ] **Theory of mind** — does the prompt give the model a sense of who the character is talking TO?

### Voice Checks
- [ ] **Verbal tics present** — at least one signature word or phrase pattern
- [ ] **Vocabulary is bounded** — words this character uses AND words they don't
- [ ] **Emotional range specified** — how does the voice shift under different emotions?
- [ ] **Sign-offs are varied** — minimum 3 distinct closing phrases

---

## 9. Anti-Pattern Reference Card

| Anti-Pattern | What It Looks Like | Why It Fails | Fix |
|---|---|---|---|
| **Synonym Pairing** | "brave and courageous" | No specificity, adds no information | Pick ONE trait and show it in action |
| **Balanced Contradiction** | "kind but firm" | Symmetrical = dead | "She's kind until she isn't — and you never see the switch" |
| **Description Dump** | "He speaks in a formal, measured tone with sophisticated vocabulary" | Abstract label, model has 1000 interpretations | Show 2 lines of dialogue in the voice |
| **Emotional Labels** | "She is warm and caring" | Label without evidence | "She brings soup when you're sick and pretends she made too much" |
| **Perfect Paragraph** | First message with no interruptions, fragments, or rough edges | Too smooth = uncanny valley | Add one interruption, one fragment, one off-rhythm moment |
| **Stock Wisdom** | "Life is full of lessons" | Cliché = no personality | Specific to the character's world and experience |
| **Hedging Language** | "It's important to note that..." | Safety-trained filler | Delete. The character wouldn't say this. |
| **Symmetrical Lists** | "She values honesty, loyalty, and kindness" | Every item has equal weight | Unbalance the list: "She values honesty. Loyalty, mostly. Kindness only when it costs something." |

---

## 10. The One-Sentence Summary

**Authentic voice is statistically messy — it surprises, contradicts itself, goes on tangents, and breaks its own patterns. Formulaic voice is statistically clean — it's predictable, symmetrical, and maintains the same temperature throughout. The difference isn't content; it's rhythm, surprise, and the willingness to be imperfect.**

---

## Sources

1. Wikipedia — "Signs of AI Writing" (WP:AISIGNS) — Comprehensive catalog of AI writing tells
2. Wagner, Michael G — "The Ten Telltale Signs of AI-Generated Text" (The Augmented Educator, 2025)
3. The Writing King — "Uncanny Valley in Writing: 8 Powerful Aspects Explained" (2024)
4. TextPolish — "The Uncanny Valley of Text: Why AI Writing Feels 'Wrong'" (2026)
5. DEV.to / Laakash — "How AI Text Detection Works Under the Hood: Perplexity, Burstiness, and Classifiers" (2025)
6. River Editor — "How to Write Authentic Dialogue That Reveals Character and Advances Plot" (2026)
7. Literary Devices — "Mastering Dialogue: Tips for Writing Realistic Conversations" (2025)
8. Leonard, Elmore — "Easy on the Adverbs, Exclamation Points and Especially Hooptedoodle" (New York Times, 2001)
9. AliCat — "Ali:Chat Style (v1.5)" — Character card format emphasizing dialogue-based trait reinforcement
10. SillyTavern Docs — "Character Design" (docs.sillytavern.app)
11. soul-repository/research-voice-instructions.md — Voice encoding in system prompts
12. soul-repository/references/format-rules.md — Soul file format constraints
13. soul-repository/research-prompt-engineering.md — Positive vs negative constraints, few-shot evidence
14. ResearchGate — "Feature-Based Detection of AI-Generated Text: An Analysis of Stylometric and Perplexity Markers in Contemporary Large Language Models" (2025)
