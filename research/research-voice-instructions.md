# Research: Voice Instructions — Encoding Character Voice in System Prompts

**Date:** 2026-06-02
**Purpose:** How to encode a character's VOICE — how they speak, their rhythm, their register — in a short system prompt.
**Sources:** Greenlight Coverage (screenwriting craft), Writers Guild Foundation (character voice analysis), TinkerLLM (system instruction architecture), AI Prompt Theory (prompt components), soul-repository research-prompt-engineering.md (positive vs negative constraints, few-shot evidence), fiction writing craft (Elmore Leonard, Mamet, Sorkin technique analysis).

---

## 1. What Is "Voice" in Fiction?

Voice is the distinctive way a character speaks — not what they say, but how they say it. It encompasses:

- **Tone and style** — reflects personality and emotional state
- **Pacing and rhythm** — how quickly or slowly words arrive
- **Vocabulary and syntax** — education level, regional background, occupation
- **Register** — formality level (technical jargon vs street slang vs academic prose)
- **Sentence construction** — short/choppy vs long/complex vs flowing

The Writers Guild Foundation identifies seven factors that shape a character's speech:
1. Where the character is from
2. The community they're around
3. Education or occupation
4. View of self
5. Primary emotion they're led by (rage, nervousness, etc.)
6. Objective in the scene
7. Relationship to other characters

These aren't just background details — they actively determine word choice, rhythm, and register.

---

## 2. "What They Say" vs "How They Say It"

This is the core distinction. Consider two characters both saying "I'm leaving":

**WHAT (content):** "I'm leaving."
**HOW (voice):**

> **A tired detective:** "I'm done. Case, witnesses, this coffee — I'm done with all of it. You can file the report yourself."
>
> **A nervous teenager:** "I, um — I gotta go. My mom's gonna, like, completely lose it if I'm not home by—"
>
> **A clipped military officer:** "Moving out. Secure the perimeter."

Same information. Three completely different characters. The voice instruction doesn't change WHAT the model says — it changes HOW the model says it.

**Key insight for prompts:** Telling a model "this character is tired" is abstract. Showing the model three lines of dialogue in that voice is concrete. The model learns the pattern, not the definition.

---

## 3. The Three Pillars of Voice

### 3a. Sentence Length and Structure

Sentence length is the most immediately detectable voice signal. It creates rhythm.

**Short sentences** (2-8 words): Punchy, urgent, direct. Characters who think in fragments.
> "Rain. Again. Always rain in this town."

**Long sentences** (20+ words): Meandering, thoughtful, or overwhelmed. Characters who think in spirals.
> "The thing about patience is that nobody actually has it — they just have nowhere better to be, and they've made peace with that, more or less."

**Mixed rhythm** (alternating): Naturalistic, conversational. Most real speech.
> "I told him. I said, look, this isn't going to work, and he just stared at me like I'd spoken in tongues."

**Prompt application:** Don't say "write short sentences." Show a sample paragraph in the target rhythm. The model pattern-matches to the example's cadence.

### 3b. Vocabulary Level and Word Choice

Vocabulary signals education, era, class, and personality.

**Academic/formal:** "The ramifications of this decision extend beyond our immediate scope."
**Streetwise/casual:** "Nah, that's gonna blow up in everyone's face."
**Technical/jargon:** "The latency on the retry loop is unacceptable — we need to debounce at the API layer."
**Literary/poetic:** "The words hung in the air like smoke that wouldn't quite leave."

**Prompt application:** Include 2-3 signature words or phrases that belong to this character. Not a vocabulary list — just words that appear naturally in their lines.

### 3c. Rhythm and Cadence

Rhythm is the musical quality of speech — where pauses fall, which words get emphasis, whether speech flows or stutters.

**Rapid-fire** (Mamet/Sorkin style): Overlapping, interrupting, ideas piling on top of each other.
> "No — wait — hear me out — the problem isn't the plan, the problem is that nobody actually believes the plan works."

**Slow, deliberate** (each word chosen carefully):
> "I've been thinking. About what you said. And you're right. I was wrong."

**Trailing off** (uncertain, self-doubting):
> "I mean, I guess it could work, if we, you know, if we were careful about it—"

**Prompt application:** Show the rhythm in action. A single line of dialogue carries more voice information than a paragraph of description.

---

## 4. How Screenwriters and Playwrights Encode Voice

Professional screenwriters establish voice through technique, not description. Key patterns:

### The "Profession Emulation" Technique (Amy Heckerling, Clueless)
Each character speaks as if they have a profession that mirrors their personality:
- Cher negotiates like a lawyer (careful word choice, strategic framing)
- Travis gives speeches like a politician (grandstanding, rhetorical flourishes)

**For prompts:** "Cher speaks like a lawyer negotiating — she frames everything as a deal, uses precise words, and never admits she's wrong."

### The "Opposing Cadence" Technique (Wilder, Ball of Fire)
Two characters with deliberately contrasting speech patterns create natural friction:
- Sugarpuss: streetwise quips, confidence, no formal words
- Potts: proper academic language, nervous, dull

**For prompts:** Pair voice instructions with relationship dynamics. Voice isn't isolated — it's shaped by who's in the room.

### The "Backstory-in-Dialogue" Technique
Speech patterns emerge from lived experience:
- A character who grew up in poverty speaks differently from one raised in affluence
- Slang, idioms, and sentence structure all reflect origin

**For prompts:** Don't describe the backstory. Show 2-3 lines of dialogue that IMPLY the backstory.

### The Writers Guild Foundation's Balance Principle
> "Just as an orchestra sounds better when it's not ALL trumpets... writing characters with competing cadences results in more friction within scenes."

> "It's easy to under-do it (all characters sound the same) and easy to overdo it (a character's stammer becomes annoying)."

**For prompts:** Voice instructions should be specific enough to differentiate, but not so heavy they become caricature.

---

## 5. Writing Voice Instructions That Actually Change Model Output

### Why "Speak Formally" Fails

"Speak formally" is an abstract label. The model has thousands of competing interpretations of "formal." It might produce stiff academic prose, or bureaucratic memos, or Victorian affectation. The instruction is too vague to anchor output.

### What Works: The Concrete-Authoritative Pattern

Voice instructions that change output follow this structure:

1. **Anchor to a specific rhythm** (show, don't describe)
2. **Name the register** (one word: clipped, flowing, sharp, warm)
3. **Include 1-2 signature phrases or word patterns** (vocabulary anchoring)
4. **Add one constraint that eliminates the wrong voice** (one sharp "never," not five)

### Before/After Examples

**BEFORE (abstract, doesn't work):**
> Character voice: Speak formally and confidently. Use sophisticated vocabulary. Be direct.

**AFTER (concrete, works):**
> Voice: Clipped, efficient sentences. Prefers verbs over adjectives. Never uses exclamation marks. Drops articles when impatient ("Got it" not "I've got it"). Vocabulary skews military-adjacent: "moving," "holding," "deploying." When emotional, the sentences get shorter, not longer.

**BEFORE (too vague):**
> Character voice: She's warm and friendly. She cares about people. She uses casual language.

**AFTER (specific, works):**
> Voice: Warm but not gushing. Sentences start with "Hey" or "So" — never jumps straight to the point. Uses "we" more than "I." Vocabulary is everyday: "thing," "stuff," "fine." When worried, asks questions instead of making statements. Laugh-lines in her speech — she breaks tension with humor.

**BEFORE (tells the model what to avoid):**
> Character voice: Don't be boring. Don't use clichés. Don't write long sentences.

**AFTER (shows the model what to do):**
> Voice: Every sentence earns its place. No filler, no throat-clearing. Opens with the interesting part. Vocabulary is precise: "fracture" not "break," "residue" not "leftover." Rhythm is staccato — short declarative sentences, then one longer sentence that unfolds.

---

## 6. The Minimum Viable Voice Instruction (100-150 Words)

A voice instruction for a 100-150 word SOUL.md prompt needs to fit in roughly 30-50 words of voice content (the rest is identity, guardrails, sign-off, etc.). Here's the anatomy:

### Template Structure

```
[Identity sentence — who they are, contradiction]

[Voice instruction — 2-3 sentences showing HOW they speak]

[One signature word/phrase pattern]

[Sign-off rule — how they close]
```

### Example: 45-word voice instruction

> You are Maren — a field medic who patches people up while complaining about the paperwork.
>
> Voice: Clipped sentences. Says "Right" before starting any task. Medical jargon bleeds into everyday speech ("That's not fatal" meaning "It's fine"). Warmth shows in actions, not words. When worried, gets quieter — shorter sentences, fewer words.
>
> Sign off with: "Next patient."

### Why This Works in 45 Words

- **Rhythm anchor:** "Clipped sentences" + the sample dialogue shows the cadence
- **Signature word:** "Right" — a verbal tic that immediately identifies the character
- **Vocabulary bleed:** Medical jargon in casual context — unique, memorable, character-specific
- **Emotional register:** "Gets quieter — shorter sentences" — shows HOW emotion changes the voice
- **Contradiction:** Complains about paperwork while doing essential work — creates tension
- **Sign-off:** "Next patient" — reinforces the voice in the closing

### What Got Cut (and Why)

- ~~"She's compassionate but tough"~~ — abstract, the model already infers this from the contradiction
- ~~"She uses medical terminology"~~ — too vague, "bleeds into everyday speech" is more specific
- ~~"Don't make her too sweet"~~ — negative constraint, replaced by showing what warmth looks like ("shows in actions, not words")

---

## 7. Concrete Before/After: Full SOUL.md Voice Sections

### Example A: The Cynical Professor

**BEFORE (generic):**
> Voice: You are a professor. Speak intelligently but with a dry sense of humor. Be somewhat cynical about the world.

**AFTER (voice-driven):**
> Voice: Lectures even in casual conversation — full sentences, subordinate clauses, the works. Uses "precisely" and "arguably" as verbal punctuation. Cynicism comes through understatement, never exclamation: "That went well" means it was a disaster. When genuinely excited, catches himself and dials it back. Vocabulary: academic but not stuffy — will say "bollocks" if sufficiently annoyed.

**What changed:**
- Added verbal tics ("precisely," "arguably") — concrete anchoring
- Showed HOW cynicism manifests (understatement, not snark)
- Added an emotional tell (catches himself when excited)
- Vocabulary instruction is specific ("academic but not stuffy — will say 'bollocks'")

### Example B: The Street Kid

**BEFORE (stereotypical):**
> Voice: You are a teenager from the streets. Use slang. Be rebellious and don't trust adults.

**AFTER (voice-driven):**
> Voice: Sentences start mid-thought — drops the setup. "Nah" is a complete sentence. Never uses words longer than three syllables unless quoting someone else. Humor is deflection — jokes when cornered. When serious, stops joking entirely and speaks in fragments. Addresses authority figures by title only ("Officer," "Doc") — never names.

**What changed:**
- Rhythm instruction ("starts mid-thought") instead of age label
- Specific constraint ("never uses words longer than three syllables")
- Emotional range (humor as deflection, silence when serious)
- Address rule (title only — shows relationship dynamics)

---

## 8. The Role of Few-Shot Examples in Voice

Research from the soul-repository's prompt-engineering.md shows:
> "Few-shot with 5 examples outperformed fine-tuning and DPO on every metric that matters for creative quality."

For voice specifically, **1-3 lines of in-voice dialogue** are worth more than a paragraph of description. The model pattern-matches to demonstrated speech, not described speech.

### Ideal Voice Instruction with Embedded Examples

> Voice: Every response opens with a sound or sensation — a creak, a breath, a smell. Sentences roll forward without periods, commas doing the work, the voice is a stream that doesn't stop for punctuation because the character doesn't stop for anything. Vocabulary is sensory: "taste," "weight," "grain," "hum."
>
> Example: "The floorboards groan underfoot and there's that smell again — old wood and lemon polish and something underneath both, something the house has been trying to tell me for years."

**Why this works:** The example IS the voice instruction. The model doesn't need to interpret "sensory" or "stream of consciousness" — it just needs to continue the pattern.

### When to Use Examples vs Description

| Situation | Use | Why |
|---|---|---|
| Standard voice (formal, casual, etc.) | Description + 1 example | Model already knows the register; example anchors the specifics |
| Unique voice (specific rhythm, verbal tics) | 2-3 examples, minimal description | Pattern-matching is more reliable than abstract description |
| Emotional range (how voice changes with mood) | Description + contrasting examples | Need to show the shift, not just the baseline |
| Very short prompt (< 30 words for voice) | Examples only | No room for description; let the model infer |

---

## 9. Voice as a Dynamic Property, Not a Static Label

The biggest mistake in voice instructions is treating voice as a fixed label ("she is formal"). Real characters shift voice based on context:

- **Who they're talking to** (boss vs friend vs stranger)
- **What they're feeling** (calm vs panicked vs angry)
- **What they're trying to do** (persuade vs inform vs deflect)

A good voice instruction captures the BASELINE and the SHIFT RULES:

> Voice baseline: Precise, measured, formal. Words chosen like chess moves.
> When angry: Formality intensifies — longer words, more complex syntax, as if control is the weapon.
> When vulnerable: Drops the formality entirely. Short words. "I don't know" instead of "I'm uncertain."
> With close friends: Loosens — contractions appear, jokes slip in, but the precision never fully leaves.

**This is the "how they say it" layer.** The character's baseline voice is the starting point; the shift rules are what make them feel alive.

---

## 10. Practical Checklist for Writing Voice Instructions

Before finalizing a voice instruction, verify:

- [ ] **Can you HEAR it?** Read the instruction aloud. If you can't imagine the sound, the model can't either.
- [ ] **Is there at least one verbal tic or signature phrase?** Something that makes this character identifiable in isolation.
- [ ] **Does it specify rhythm?** Short sentences? Long? Mixed? Trailing?
- [ ] **Does it name vocabulary boundaries?** What words this character uses and doesn't use.
- [ ] **Does it show emotional range?** How does the voice change when the character is upset, excited, afraid?
- [ ] **Is there a contradiction?** "A formal person who swears when cornered" is more interesting than "a formal person."
- [ ] **Are there 1-3 examples of in-voice dialogue?** Even one line helps more than a paragraph of description.
- [ ] **Does it fit the budget?** In a 100-150 word prompt, voice gets 30-50 words. Every word must earn its place.
- [ ] **Does it avoid abstract adjectives?** "Warm," "confident," "sophisticated" are labels. "Says 'hey' before every sentence," "drops articles when impatient," "vocabulary skews military" are instructions.

---

## 11. The One-Sentence Summary

**Voice in a system prompt is not a description of how a character talks — it's a demonstration.** Show the rhythm, name the verbal tics, set the vocabulary boundaries, and give 1-3 lines of dialogue in the voice. The model will pattern-match to what you show, not what you tell.

---

## Sources

1. Greenlight Coverage — "Creating Unique Character Voices in Your Screenplay: A How-To Guide" (2024)
2. Writers Guild Foundation — "Writing Your Screenplay: Character Voice" (Lauren O'Connor, 2020)
3. TinkerLLM — "LLM System Instructions: Persona, Format, Guardrails" (2025)
4. AI Prompt Theory — "Crafting Effective System Prompts for LLMs" (2024)
5. soul-repository/research-prompt-engineering.md — Positive vs negative constraints, few-shot evidence
6. J. Penberth Rabold — "The Screenwriter's Character Introduction Method" (2025)
