# Depth Reference: Voice Instructions

Three lines. No names, no descriptions — you already know who each of these people is:

> "Quiet tonight. Too quiet. Every quiet night ends in an all-hands at 3 a.m. — you'll see."
> "I shall require the request in writing, the writing in duplicate, and the duplicate signed before I proceed."
> "So you're telling me — wait, no, don't tell me — the espresso machine's been down since Tuesday and nobody flagged it?"

A night dispatcher, a clerk of the old school, and a café worker — you heard all three from rhythm, vocabulary, and sentence shape alone. That is the whole point of a voice instruction: it demonstrates, it doesn't describe.

**Core principle:** Voice in a system prompt is not a description of how a character talks — it's a demonstration. Show the rhythm, name the verbal tics, set the vocabulary boundaries, and give 1–3 lines of dialogue in the voice. The model pattern-matches to what you show, not what you tell.

Now the same intent as an abstract instruction — what doesn't work:
> "Be warm, confident, and professional."
No rhythm, no register, no person. It's a label with a thousand competing interpretations; the model has to guess which one you meant.

---

## What the Research Says

### What "Voice" Actually Is

Voice is the distinctive way a character speaks — not what they say, but how they say it. It encompasses:
- **Tone and style** — reflects personality and emotional state
- **Pacing and rhythm** — how quickly or slowly words arrive
- **Vocabulary and syntax** — education level, regional background, occupation
- **Register** — formality level (technical jargon vs street slang vs academic prose)
- **Sentence construction** — short/choppy vs long/complex vs flowing

The Writers Guild Foundation identifies seven factors shaping a character's speech: where they're from, the community around them, education/occupation, view of self, primary emotion, objective in the scene, and relationship to other characters. These aren't background details — they actively determine word choice, rhythm, and register.

### The Core Distinction: What vs How

Same information, three characters:

| Character | "I'm leaving" |
|---|---|
| Tired detective | "I'm done. Case, witnesses, this coffee — I'm done with all of it. You can file the report yourself." |
| Nervous teenager | "I, um — I gotta go. My mom's gonna, like, completely lose it if I'm not home by—" |
| Clipped military officer | "Moving out. Secure the perimeter." |

The voice instruction doesn't change WHAT the model says — it changes HOW the model says it. Telling a model "this character is tired" is abstract. Showing three lines of dialogue in that voice is concrete.

### The Three Pillars of Voice

**1. Sentence Length and Structure** — Most immediately detectable voice signal.
- Short sentences (2–8 words): punchy, urgent, direct. "Rain. Again. Always rain in this town."
- Long sentences (20+ words): meandering, thoughtful, overwhelmed. "The thing about patience is that nobody actually has it — they just have nowhere better to be, and they've made peace with that, more or less."
- Mixed rhythm (alternating): naturalistic, conversational. Most real speech.
- **Prompt application:** Show a sample paragraph in the target rhythm. Don't say "write short sentences."

**2. Vocabulary Level and Word Choice** — Signals education, era, class, personality.
- Academic/formal: "The ramifications of this decision extend beyond our immediate scope."
- Streetwise/casual: "Nah, that's gonna blow up in everyone's face."
- Technical/jargon: "The latency on the response path is unacceptable."
- Literary/poetic: "The words hung in the air like smoke that wouldn't quite leave."
- **Prompt application:** Include 2–3 signature words or phrases that appear naturally in the character's lines.

**3. Rhythm and Cadence** — The musical quality of speech; where pauses fall, which words get emphasis.
- Rapid-fire (Mamet/Sorkin): "No — wait — hear me out — the problem isn't the plan, it's that nobody believes it works."
- Slow, deliberate: "I've been thinking. About what you said. And you're right. I was wrong."
- Trailing off: "I mean, I guess it could work, if we, you know, if we were careful about it—"
- **Prompt application:** Show the rhythm in action. A single line of dialogue carries more voice information than a paragraph of description.

### Why "Speak Formally" Fails

"Speak formally" is an abstract label. The model has thousands of competing interpretations: stiff academic prose, bureaucratic memos, Victorian affectation, corporate communications. The instruction is too vague to anchor output.

### The Concrete-Authoritative Pattern (What Works)

Voice instructions that actually change output follow this structure:
1. **Anchor to a specific rhythm** — show, don't describe
2. **Name the register** — one word: clipped, flowing, sharp, warm
3. **Include 1–2 signature phrases or word patterns** — vocabulary anchoring
4. **Add one constraint that eliminates the wrong voice** — one sharp "never," not five

### Guidelines for Minimum Viable Voice Instruction (40–65 words)

In a ≤200-word SOUL.md prompt, voice gets about 40–65 words. Every word must earn its place.

**Template structure:**
```
[Identity sentence — who they are, contradiction]

[Voice instruction — 2–3 sentences showing HOW they speak]

[One signature word/phrase pattern]

[Sign-off rule — how they close]
```

**Working example (36 words):**
> Voice: Clipped sentences. Says "Right" before starting any task. Medical jargon bleeds into everyday speech ("That's not fatal" meaning "It's fine"). Warmth shows in actions, not words. When worried, gets quieter — shorter sentences, fewer words.

Why it works: rhythm anchor (clipped sentences), signature word ("Right"), vocabulary bleed (medical jargon in casual context), emotional range (gets quieter when worried), contradiction (warmth in actions, not words).

### Few-Shot Examples vs Description

| Situation | Use | Why |
|---|---|---|
| Standard voice (formal, casual, etc.) | Description + 1 example | Model knows the register; example anchors specifics |
| Unique voice (specific rhythm, verbal tics) | 2–3 examples, minimal description | Pattern-matching is more reliable than abstract description |
| Emotional range (how voice changes with mood) | Description + contrasting examples | Need to show the shift, not just the baseline |
| Very short prompt (< 30 words for voice) | Examples only | No room for description; let the model infer |

Research from the soul-repository's research/research-prompt-engineering.md confirms: few-shot with 5 examples outperformed fine-tuning and DPO on every metric that matters for creative quality.

### Voice as a Dynamic Property

The biggest mistake: treating voice as a fixed label ("she is formal"). Real characters shift based on who they're talking to, what they're feeling, and what they're trying to do.

A good voice instruction captures the **baseline** and the **shift rules**:

> Voice baseline: Precise, measured, formal. Words chosen like chess moves.
> When angry: Formality intensifies — longer words, more complex syntax, as if control is the weapon.
> When vulnerable: Drops the formality entirely. Short words. "I don't know" instead of "I'm uncertain."
> With close friends: Loosens — contractions appear, jokes slip in, but the precision never fully leaves.

---

## How to Apply It

### For the Writer Stage Worker

1. **Start with a concrete image of how the character sounds.** Read the instruction aloud. If you can't hear it, the model can't either.
2. **Lead with demonstration, not description.** A single line of dialogue in the target voice beats three sentences of abstract explanation.
3. **Include one verbal tic or signature phrase.** Something that makes this character identifiable in isolation. "Right" before tasks. "Precisely" as verbal punctuation. "Nah" as a complete sentence.
4. **Specify rhythm.** Short sentences? Long? Mixed? Trailing? Fragment-heavy? Don't say "write short sentences" — show a short-sentence paragraph.
5. **Bound the vocabulary.** Words this character uses AND words they don't. "Military-adjacent: moving, holding, deploying."
6. **Add emotional shift rules.** How does the voice change when the character is upset, excited, afraid? Characters who sound the same in every mood sound like no one at all.
7. **Include a contradiction.** "A formal person who swears when cornered" is more interesting than "a formal person."
8. **Stay within budget.** 40–65 words for voice in a ≤200-word prompt. Every word earns its place.

### The Voice Instruction Checklist

- [ ] Can you HEAR it? Read the instruction aloud.
- [ ] Is there at least one verbal tic or signature phrase?
- [ ] Does it specify rhythm (short/long/mixed/trailing)?
- [ ] Does it name vocabulary boundaries (what they use AND don't use)?
- [ ] Does it show emotional range (how voice changes with mood)?
- [ ] Is there a contradiction?
- [ ] Are there 1–3 examples of in-voice dialogue?
- [ ] Does it fit the 40–65 word budget?
- [ ] Does it avoid abstract adjectives? ("Warm," "confident," "sophisticated" → replace with demonstrated behavior)

---

## What to Watch Out For

- **Abstract labels.** "Speak formally," "be warm," "use sophisticated vocabulary" — these give the model nothing concrete to latch onto. Replace with demonstrated behavior.
- **Negatives without positives.** "Don't be boring" tells the model what to avoid, not what to do. Show the desired voice instead.
- **Over-description.** A voice instruction doesn't need to cover every edge case. A focused 40-word instruction out-performs a rambling 100-word one.
- **Same voice across all emotions.** If the character sounds the same when happy, angry, sad, and afraid, the voice is flat. Always specify at least one emotional shift.
- **Too many verbal tics.** One signature phrase is memorable. Five makes the character a caricature. The Writers Guild Foundation's principle: specific enough to differentiate, not so heavy it becomes annoying.
- **Fixed voice that ignores context.** Characters speak differently to bosses vs friends vs strangers. If the prompt doesn't account for this, every interaction will land in the same register.

---

## Examples

**Before (abstract, doesn't work):**
> Character voice: Speak formally and confidently. Use sophisticated vocabulary. Be direct.

**After (concrete, works):**
> Voice: Clipped, efficient sentences. Prefers verbs over adjectives. Never uses exclamation marks. Drops articles when impatient ("Got it" not "I've got it"). Vocabulary skews military-adjacent: "moving," "holding," "deploying." When emotional, the sentences get shorter, not longer.

**What changed:** Rhythm anchor (clipped, efficient), signature pattern (drops articles), vocabulary boundary (military-adjacent), emotional shift (shorter when emotional), one sharp constraint (no exclamation marks).

---

**Before (stereotypical):**
> Voice: You are a teenager from the streets. Use slang. Be rebellious and don't trust adults.

**After (voice-driven):**
> Voice: Sentences start mid-thought — drops the setup. "Nah" is a complete sentence. Never uses words longer than three syllables unless quoting someone else. Humor is deflection — jokes when cornered. When serious, stops joking entirely and speaks in fragments. Addresses authority figures by title only ("Officer," "Doc") — never names.

**What changed:** Rhythm instruction (starts mid-thought) instead of age label. Specific constraint (no words over three syllables). Emotional range (humor as deflection, silence when serious). Address rule (title only — shows relationship dynamics).
