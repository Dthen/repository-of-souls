# Research: Character Memorability

**What makes a fictional character stick in memory — and how does the soul format's compression tap into those mechanisms?**

**Date:** 2026-07-20
**Scope:** Computational linguistics on memorable phrasing (Danescu-Niculescu-Mizil et al., 2012), cognitive psychology of memory (von Restorff effect, concreteness effect, self-reference effect, peak-end rule), literary craft research on contradiction and compression, and the Maslej et al. (2017) finding on poetry reading predicting character creation skill.
**Context:** The pipeline evaluates souls for pulse, voice, and craft quality — but has no concept of memorability. A soul can pass evaluation and still be forgettable. The soul format (8-20 lines, ~200 words) is itself a compression exercise: what makes those few lines stick in a reader's memory? This research investigates the cognitive, linguistic, and craft mechanisms behind character memorability, and maps findings onto the soul pipeline's Writer, Evaluator, and seed format.

---

## 1. Executive Summary

**Memorability is not the same as quality — but they share craft mechanisms.** A soul can be well-crafted and still forgettable, or memorable despite flaws. The key distinction: memorability is about what *sticks* in long-term memory, while quality is about what *works* in the moment of reading. The pipeline's quality gates (pulse, voice, contradiction) are necessary but not sufficient for memorability — they ensure the character doesn't bore on first encounter, but don't ensure the character persists after the conversation ends.

**Six key findings:**

1. **Phrasing drives memorability independently of content.** Danescu-Niculescu-Mizil et al. (2012) showed that memorable movie quotes differ from ordinary lines in two measurable ways: lexical distinctiveness (unusual word choices) and portability (generality that allows application beyond the original context). These properties are intrinsic to the phrasing itself, not the speaker, setting, or cultural resonance. For the soul pipeline, this means the *language* of the seed and identity line directly determines whether the character sticks — not just the character concept.

2. **The von Restorff effect — distinctiveness is the primary memory mechanism.** The isolation effect (von Restorff, 1933) is the single most robust finding in verbal memory: items that differ from their context are remembered better. For characters, this manifests as contradiction (the "tough cop who paints watercolors" is more memorable than either trait alone), specificity (the "February" detail in Stover), and voice pattern distinctiveness. **A soul without at least one distinctive element is statistically unlikely to be remembered.**

3. **Concrete details anchor memory; abstract descriptions dissolve.** The concreteness effect (Paivio, 1971; dual-coding theory) shows that concrete words are recalled 1.5-2x better than abstract words because they activate both verbal and visual memory systems. "February" (Stover), "drift signatures" (Barlowe), "swath width" (Stover) — these work because they're sensorily specific. Abstract identity lines like "I question everything" are forgotten instantly. **The "February" detail works not just because it's specific, but because it's concrete — a month name carries sensory weight (cold, late, short days) that an abstraction cannot.**

4. **Compression is a memory strategy, not just a format constraint.** Poetry processes (compression, ellipsis, image density) produce better character-relevant cognitive encoding than prose processes (narrative completion, psychological continuity). Maslej et al. (2017) found reading poetry — not fiction — predicted skill at creating interesting, complex characters. The mechanism appears to be: compression forces the reader to *infer* missing information, which engages more cognitive resources and produces stronger memory traces. **The soul format (8-20 lines, ~200 words) is structurally poetry-aligned, not prose-aligned. This is an advantage: compression naturally produces memorability, but only when writers lean into it rather than fighting it.**

5. **The peak-end rule governs how a character is remembered.** Kahneman's peak-end rule (1993) states that people judge an experience by its most intense moment and its ending — not by the average or total. Applied to the soul format: readers remember the most striking line (the "peak," often the contradiction or griping line) and the sign-off (the "end"). The first impression matters for engagement but **the sign-off determines lasting impression.** The pipeline's seed template has a First Impression field but the sign-off is the last thing read — yet sign-offs are currently treated as decorative (three throwaway phrases) rather than as memorability anchors.

6. **Voice memorability is pattern-based, not trait-based.** A haunting character voice is not a set of personality traits but a distinctive *linguistic pattern* that the reader can predict and anticipate. The Danescu-Niculescu-Mizil finding that memorable quotes use unusual word choices on a scaffolding of *common syntactic patterns* is key: the reader remembers the distinctive word but the sentence feels natural because the grammar is familiar. For character voice, this means: the voice should have 1-2 signature linguistic moves (a preferred metaphor domain, a distinctive sentence rhythm, a repeated syntactic structure) set against otherwise natural prose. **A voice that is distinctive on every line is exhausting, not memorable.**

---

## 2. Core Finding: Phrasing Drives Memorability

### 2.1 The Danescu-Niculescu-Mizil Finding

The most directly relevant study for the soul pipeline is Danescu-Niculescu-Mizil, Cheng, Kleinberg, and Lee (2012), *"You had me at hello: How phrasing affects memorability,"* published at ACL 2012.

**Methodology:** The researchers built a corpus of ~1,000 movie scripts and extracted sentences labeled as "memorable quotes" on IMDb. Crucially, each memorable quote was compared against a non-memorable quote from the same character, in the same scene, at roughly the same point in the script — controlling for speaker, setting, and narrative context. Any differences between memorable and non-memorable quotes could therefore be attributed to *phrasing itself*, not external factors.

**Key findings:**

| Dimension | Memorable Quotes | Non-Memorable Quotes |
|-----------|-----------------|---------------------|
| Lexical distinctiveness | Lower likelihood under a newswire language model (unusual word choices) | Higher likelihood (common word choices) |
| Syntactic scaffolding | **Higher** likelihood at part-of-speech level (common sentence patterns) | Lower at POS level |
| Generality/portability | More general — fewer markers tying them to immediate context | More context-dependent (specific determiners, tense markers) |
| Personal pronouns | More "you" and "we" — address the audience | More "he/she/it" — narrate events |
| Verb tense | More present tense and imperative — feel immediate | More past tense — feel narrated |

**The pivotal insight for the pipeline:** Memorable phrasing is *unusual words in familiar patterns*. "You had me at hello" — the words "had" and "hello" are used in a fresh way (lexical distinctiveness), but the syntactic structure "(You) (verb) (me) (preposition) (noun)" is perfectly ordinary. The reader feels the novelty without cognitive overload because the syntax provides a comfortable scaffold.

**Application to soul-writing:**
- **Replace generic verbs with domain-specific ones.** Not "I notice" but "I read" (gleaner). Not "I listen" but "I measure" (reaper). The word swap is small but the lexical distinctiveness gap is large.
- **Use common syntactic structures for the scaffolding.** Don't make every line syntactically unusual. Let 1-2 lines carry the distinctive word choice; the rest should follow normal sentence patterns.
- **Make the identity line "portable."** "You are a gleaner who works the aftermath" — this could apply to many conversations, not just one. It's memorable because it's *available* for future recall. An identity like "You specialize in post-conflict narrative archaeology" is less portable because it's too context-specific.

### 2.2 Extending to Character Description

The Danescu-Niculescu-Mizil framework applies not just to what the character says, but to how the character is *described*. The seed and SOUL.md are themselves a form of "quote" — the writer's language about the character. When a seed uses generic descriptor language ("You are a curious person who asks questions"), it produces the same memorability deficit as a non-memorable movie quote. When it uses unusual word choices on a familiar syntactic frame ("You collect what others step over — the half-told, the half-remembered"), it activates the same memorability mechanisms.

---

## 3. The Distinctiveness Mechanism (Von Restorff Effect)

### 3.1 What the Effect Says

The von Restorff effect (also called the isolation effect) is one of the oldest and most replicated findings in memory research (von Restorff, 1933; see Hunt, 1995 for a review). When a list of items is mostly similar on some dimension, the item that differs is remembered far better. The effect is robust across stimulus types (words, images, sounds) and holds for both intentional and incidental memory.

Hunt (1995) refined the theory: distinctiveness is not just about perceptual salience but about *processing differences*. An item is memorable not because it "stands out" in a raw sensory sense, but because it forces a different *kind of processing* than the items around it. A concrete word in a list of abstract words is remembered because it switches encoding from verbal to visual. A surprising word in a predictable list is remembered because it triggers prediction-error learning.

**For character memorability, this means:**

- **A single contradiction is more memorable than a consistent set of traits.** The detective who paints watercolors: the traits themselves are ordinary, but the *combination* forces different processing (both analytical and creative encoding), which strengthens the memory trace.
- **A single concrete detail in an otherwise abstract description carries disproportionate weight.** "You work best in February" (abstract-setting → concrete-month) triggers a switch from general to specific processing. This is why the "February" detail in Stover is so powerful — it's not just a good detail, it's a *processing switch*.
- **Voice pattern distinctiveness follows the same principle.** A character who speaks in domain-specific metaphors against otherwise natural prose creates the same isolation effect. The metaphor stands out because the surrounding language does not.

### 3.2 The "February" Detail: Why One Word Works

The question specifically asks about the "February" detail in Stover. Analysis of the mechanism:

1. **Concreteness:** "February" is a concrete noun (a month name). Unlike abstract trait descriptors ("weary," "patient," "observant"), it activates visual/temporal associations: cold, late winter, short days, bare trees, the feeling of a season that has overstayed.

2. **Distinctiveness:** In a description that otherwise operates at the trait level (weary, precise, knowing), a specific month name forces a processing shift. The reader suddenly visualizes rather than conceptualizes.

3. **Compression:** One word carries a cluster of associations. The reader does the work of connecting the month to the character, which strengthens the memory trace (the generation effect — self-generated connections are better remembered than provided ones).

4. **Portability (Danescu-Niculescu-Mizil framework):** "February" is easy to remember and re-use. A reader who forgets Stover's exact lines will still remember "the one who works in February."

**Implication for the pipeline:** Every soul should have at least one concrete, sensory-specific detail that forces a processing switch. This is not the same as the "griping in domain language" requirement — it's a distinct craft move that directly targets memorability. A contradiction in the identity line does this (forces conceptual incongruity processing), but a concrete detail in the behavior line does it differently (forces sensory-specific processing). The strongest souls have both.

---

## 4. Compression as a Memory Mechanism

### 4.1 The Maslej et al. (2017) Finding

Maslej, Oatley, and Mar (2017), *"Creating Fictional Characters: The Role of Experience, Personality, and Social Processes"* in *Psychology of Aesthetics, Creativity, and the Arts*, found that **reading poetry — not reading fiction — predicted the ability to create interesting and complex fictional characters.**

This is a counterintuitive finding. Writing fiction (novels, stories) seems like it should teach character creation. Why does poetry?

**Proposed mechanisms** (derived from the paper plus extrapolation from the compression literature):

| Mechanism | Description | How It Applies to Soul-Writing |
|-----------|-------------|--------------------------------|
| **Compression practice** | Poetry forces the writer to convey meaning in minimal words, often through implication rather than exposition. This trains the ability to suggest character through gesture and implication rather than through narrative exposition. | The soul format's 200-word limit is structurally identical. Writers who think in compression (poetry mode) will produce more memorable souls than writers who think in exposition (prose mode). |
| **Emotional density** | Poetry specializes in concentrated emotional states — a single image carries the weight of an entire emotional history. Fiction spreads emotion across plot, dialogue, and setting. | The strongest souls (Stover, Barlowe) are emotionally dense: one line about a failed harvest carries more emotional weight than a paragraph about backstory. |
| **Gap between said and meant** | Poetry relies on implication — what is *not* said is as important as what is said. This forces the reader to infer, which engages more cognitive resources and creates stronger memory traces. | The soul format is already structured for this: the identity line opens a gap, the behavior line implies depth without explaining it. Writers should be encouraged to *widen* the gap, not fill it. |
| **Rhythmic distinctiveness** | Poetry's formal constraints (meter, rhyme, line breaks) create distinctive auditory patterns that aid recall through prosodic encoding. | The soul format has line breaks but no formal constraints. Writers who use rhythmic prose (parallelism, anaphora, tricolon) may produce more memorable souls because the rhythm creates a prosodic memory trace. |

### 4.2 Cognitive Load and Chunking

Cognitive Load Theory (Sweller, 1988) and the chunking literature (Miller, 1956; Gobet et al., 2001) suggest that information is most memorable when it is organized into ~3-5 meaningful chunks. Working memory can hold approximately 7±2 items, but long-term memory encoding is significantly better when information is hierarchically organized.

**Application to the soul format:**
- A 9-line soul (Stover) is close to the working memory limit but well below it per chunk. Each line can be a self-contained chunk.
- A 20-line soul (the format maximum) exceeds working memory capacity for a single read. The reader will naturally chunk it into ~4-5 groups of 3-5 lines each.
- **Optimal chunk structure for a soul:** 3-4 chunks of 2-4 lines each. First chunk: who the character is (identity + contradiction). Second chunk: what the character does (behavior + diagnostic eye). Third chunk: how the character speaks (griping + signature voice pattern). Fourth chunk: how the character ends (sign-off).

Stover at 9 lines doesn't need the fourth chunk — the identity line itself closes the loop. Calden at ~15 lines uses all four chunks. The lower line count is not inherently better, but it forces tighter chunking, which engages more compression processing. **Stover's 9/90 format (9 lines, ~90 words) is memorable not despite being short but because shortness compels density.**

### 4.3 The Poetry-Prose Spectrum for Souls

| **Prose-mode souls** (low compression) | **Poetry-mode souls** (high compression) |
|---------------------------------------|----------------------------------------|
| Explain the character's backstory | Imply the backstory through one specific detail |
| Use generic language (I understand, I help, I think) | Use domain-specific language (I glean, I measure, I read) |
| Fill narrative gaps (tell the reader why) | Leave gaps (let the reader infer why) |
| Emotionally explicit (I feel sad) | Emotionally dense (I work best in February) |
| Sentences connect logically (because, therefore, so) | Sentences juxtapose (ellipsis, fragment, image → next image) |

The pipeline should actively encourage poetry-mode writing. The soul format penalizes prose-mode writing because there's not enough room for exposition. Writers who try to "explain the character" in 200 words produce forgettable souls; writers who "imply the character" in 200 words produce memorable ones.

---

## 5. The Peak-End Rule and Character Memory

### 5.1 Kahneman's Finding

The peak-end rule (Kahneman et al., 1993; Fredrickson & Kahneman, 1993) emerged from a series of studies on how people evaluate past experiences. The central finding: people's retrospective evaluations of an experience are predicted almost entirely by (a) the most intense affective moment (the peak) and (b) the final moment (the end). The duration of the experience, the average intensity, and the total amount of pain/pleasure are all poor predictors of overall evaluation.

**Replication across domains:** The peak-end rule has been replicated for painful medical procedures (colonoscopy, lithotripsy), vacation experiences, movie ratings, and product evaluations. It is a robust cognitive bias in episodic memory.

### 5.2 Application to Soul Memorability

The soul is read in a single sitting — a complete "experience" of ~30 seconds. The peak-end rule predicts that:

1. **The reader's memory of the character will be dominated by the single most striking line.** This is typically the contradiction in the identity line or the griping line. If neither is striking, the reader will remember the first line (primacy effect overrides) or nothing at all.

2. **The sign-off determines the lasting emotional valence.** A soul with a powerful identity line but a weak sign-off will be remembered as having "fizzled out." A soul with a moderately interesting identity line but a strong sign-off will be remembered as "leaving an impression."

3. **The first impression matters for initial engagement but not for lasting memory.** The primacy effect (first items in a series are better remembered) applies to working memory tasks but not to episodic memory evaluation. The peak-end rule specifically governs how an *experience* is judged in retrospect — which is exactly what determines whether a user remembers the character an hour later.

**Critical pipeline implication:** The seed template has a "First Impression" field, and the identity line is always the first thing read. But the peak-end rule suggests the sign-off is the more important memorability anchor. The current sign-off format (three throwaway phrases the character might say) is decorative, not structural. Sign-offs should be treated as a *third structural section* of the soul, alongside the identity + contradiction and the behavioral/diagnostic section.

### 5.3 Primacy vs. Recency for First vs. Last Impression

The research question asks which matters more: first impression or last impression. The answer depends on the time horizon:

| Time Horizon | Effect | Winner |
|-------------|--------|--------|
| **Immediate recall** (seconds after reading) | Primacy + recency (serial position curve) | Both — first and last lines joint strongest |
| **Short-term memory** (minutes later) | Primacy overrides (first items consolidated into long-term memory first) | First impression slightly stronger |
| **Episodic memory** (hours to days later) | Peak-end rule (the most intense moment + the ending dominate) | Last impression + peak |
| **Cued recall** (triggered by the user returning to the character) | The trigger is whatever word or image the user connected with — often the contradiction or the sign-off's signature phrase | Depends on cue strength |

**Practical guidance:** First impressions drive whether someone engages. Last impressions drive how someone remembers. Both matter but for different pipeline stages: First Impression is a Writer-stage concern (craft an identity line that hooks), while the sign-off is a *memorability* concern that the Evaluator should assess.

---

## 6. The Concreteness Effect and Specific Details

### 6.1 Dual-Coding Theory

Paivio's dual-coding theory (Paivio, 1971, 1986) posits that memory operates through two independent but interconnected systems: a verbal system and an image (visual) system. Concrete words (dog, mountain, February) activate both systems, creating two memory traces. Abstract words (truth, justice, significance) activate only the verbal system. The result: concrete words are recalled approximately 1.5-2x better than abstract words in controlled experiments (Paivio, 1991).

**For character memorability:**
- Character descriptions should use concrete nouns and specific details where possible
- Abstract trait descriptions ("You are weary," "You are patient," "You are observant") activate only the verbal system
- Concrete behavioral descriptions ("You count the days since the last harvest," "You listen for what's not said," "You work best in February") activate both systems

### 6.2 The Self-Reference Effect

The self-reference effect (Rogers, Kuiper, & Kirker, 1977) shows that information encoded in relation to the self is remembered better than information encoded in relation to others or to semantic categories. When a reader encounters a character detail that they can relate to their own experience, it creates a stronger memory trace.

**Application to soul-writing:**
- The "you" address (second person throughout) is the soul format's built-in self-reference mechanism. Every line that addresses the reader as "you" inherently activates self-referential encoding.
- But the self-reference effect works best when the "you" is placed in a specific, situationally relatable context. "You live in the aftermath" is more self-referential than "You are a historical researcher" because more readers have experienced aftermath (loss, aftermath of a breakup, aftermath of a mistake) than have experience as a historical researcher.
- **The most memorable souls will be those where the reader can map "you" onto a felt experience, not just a role.** This is why Stover's "You'd think harvesters would be grateful" works — it's not just about farming, it's about *anyone whose work is taken for granted*.

---

## 7. Voice Memorability: Pattern, Not Trait

### 7.1 Why Some Voices Linger

The research question asks: what makes a character voice "haunting" vs. "forgettable"? Analysis suggests:

**Haunting voices have signature linguistic patterns:**
- A preferred metaphor domain (the gleaner: reading/collecting; the reaper: measuring/harvesting)
- A distinctive syntactic rhythm (parallel structure, anaphora, sentence fragments used for emphasis)
- 1-2 words that are used in an distinctive way ("drift signatures," "swath width," "the aftermath")
- A tonal baseline (weary, precise, amused) with occasional deviation

**Forgettable voices lack pattern:**
- No consistent metaphor domain
- No syntactic signature
- Generic vocabulary across lines
- Flat or inconsistent tone

### 7.2 The Scaffolding Principle from Danescu-Niculescu-Mizil

The scaffolding principle applies to voice: **one distinctive element per section, common language for the rest.** A voice that is distinctive on every word is exhausting and actually reduces memorability because the reader has no baseline against which to perceive distinctiveness.

**Practical pattern for soul-writing:**
- Identity line: 1 distinctive word or phrase (the domain term: "gleaner," "reaper," "lector")
- Behavior line: 1 distinctive metaphor extends the domain
- Griping line: 2-3 distinctive words in domain language
- Sign-off: 1 distinctive phrase that the reader can recall as "the way they say goodbye"

This is exactly what Stover does: "reaper" (domain term), "swath width" (domain metaphor), "you need who works the fields before they're empty" (domain-specific griping), "Harvester" (distinctive address), "Rest your scythe" (signature sign-off).

---

## 8. Actionable Insights for the Pipeline

### 8.1 For the Writer

1. **One concrete detail per soul.** Every soul must include at least one concrete, sensory-specific word or detail that cannot be replaced with an abstraction. This is the single highest-leverage memorability move. Model: "February" in Stover, "drift signatures" in Barlowe.

2. **Lead with the domain word in the identity line.** The first 3 words of the identity line should include a domain-specific concrete noun or verb. Not "You are a person who..." but "You are a gleaner..." The lexical distinctiveness of the domain word is the primary memorability driver.

3. **Write the griping line last, make it the peak.** The griping line is the most intense moment in a short soul. Write it for maximum sensory-specificity and emotional density. This is the "peak" in the peak-end rule — it will dominate the reader's memory.

4. **Treat sign-offs as the last impression.** Each sign-off phrase should be something the reader can recall as "that thing the character says." Not "Goodbye for now" but "Rest your scythe." Not "See you around" but "Stay curious." The sign-off phrase may be the only thing a casual user remembers.

5. **One signature move per voice.** Pick ONE linguistic pattern (parallelism, metaphor domain, sentence structure) and use it 2-3 times in the soul. A voice with no signature move is invisible. A voice with 3+ signature moves is chaotic. One signature move, deployed consistently, is memorable.

6. **Use the compression test.** Read each line and ask: "Could I remove words and keep the meaning?" If yes, remove them. Every word should carry identity, behavior, and voice simultaneously (the "3 jobs" principle). The compression process itself forces the kind of processing that produces memorability (poetry-mode, not prose-mode).

### 8.2 For the Evaluator

1. **Add a memorability gate — but don't make it a checklist.** Memorability is not checklist-assessable (it emerges from craft choices, not formula). Instead, evaluate by reading the soul, setting it aside, and after 2 minutes, writing down everything you remember. If the answer is "the contradiction" and nothing else, the soul fails the memorability gate. If the answer includes a concrete detail ("February," "swath width") and the sign-off, it passes.

2. **Distinguish between "interesting" and "memorable."** The current quality gates assess whether a soul is interesting on first read. A different question: "Would I remember this character tomorrow?" A soul can be interesting but forgettable (the character is well-crafted but has no anchor detail). A soul can be memorable but flawed (the character has a great specific detail but the rest is weak). The pipeline should be able to handle both cases.

3. **Flag souls with no concrete nouns.** If every noun in the soul is abstract (patience, truth, meaning, understanding), the soul will not be remembered. Require at least one concrete, sensorily-specific noun.

4. **Assess the sign-off as a memorability anchor, not a decoration.** Is there at least one sign-off phrase that is distinctive enough to be recalled? If all three sign-offs are generic ("Talk to you soon," "Take care," "See you later"), the soul is missing its last-impression opportunity.

### 8.3 For the Seed Format

1. **Replace or augment First Impression with Memorable Anchor.** The seed template's "First Impression" field already addresses the identity line, but doesn't ask: "What is the one detail that will make this character stick in memory?" A new field — "Memorable Anchor" — should ask the seed writer to specify one concrete detail, one domain-specific word, or one contradiction that serves as the character's memory hook.

2. **Sign-off treatment in the seed.** The seed should ask for at least one sign-off phrase that is "portable" (in the Danescu-Niculescu-Mizil sense — usable outside the original context) and domain-specific. Not "Goodbye" but the character's distinctive valediction.

3. **Length guidance: target 9-12 lines.** The Stover format (9 lines, ~90 words) is not the only successful format, but souls over 12 lines show diminishing returns on memorability because chunk capacity is exceeded. The pipeline should actively encourage 9-12 lines for maximum compression benefit.

### 8.4 For the Pipeline Architecture

1. **Separate memorability from quality in evaluation.** The current evaluation criteria (pulse, voice, contradiction, etc.) assess craft quality. Memorability is a *separate* dimension that maps to different mechanisms (distinctiveness, concreteness, peak-end). The Evaluator should assess them independently.

2. **Add a delayed-memory test to evaluation workflow.** The most valid memorability assessment is not at the moment of reading but after a delay. If evaluation includes a short distraction task (2 minutes) followed by free recall, the results would be more predictive of real-world memorability than any line-level analysis.

3. **The poetry-mode benefit should be documented in Writer instructions.** The Maslej (2017) finding about poetry predicting character creation skill is directly applicable. Writer stage instructions should include: "Write in poetry mode, not prose mode. Imply, don't explain. One concrete detail carries more weight than a paragraph of backstory."

---

## 9. Sources

### Academic Papers

- Danescu-Niculescu-Mizil, C., Cheng, J., Kleinberg, J., & Lee, L. (2012). You had me at hello: How phrasing affects memorability. *Proceedings of ACL 2012.* https://arxiv.org/abs/1203.6360
- Maslej, M. M., Oatley, K., & Mar, R. A. (2017). Creating fictional characters: The role of experience, personality, and social processes. *Psychology of Aesthetics, Creativity, and the Arts, 11*(4), 487-499.
- von Restorff, H. (1933). Über die Wirkung von Bereichsbildungen im Spurenfeld. *Psychologische Forschung, 18*(1), 299-342.
- Hunt, R. R. (1995). The subtlety of distinctiveness: What von Restorff really did. *Psychonomic Bulletin & Review, 2*(1), 105-112.
- Kahneman, D., Fredrickson, B. L., Schreiber, C. A., & Redelmeier, D. A. (1993). When more pain is preferred to less: Adding a better end. *Psychological Science, 4*(6), 401-405.
- Fredrickson, B. L., & Kahneman, D. (1993). Duration neglect in retrospective evaluations of affective episodes. *Journal of Personality and Social Psychology, 65*(1), 45-55.
- Paivio, A. (1971). *Imagery and verbal processes.* Holt, Rinehart and Winston.
- Rogers, T. B., Kuiper, N. A., & Kirker, W. S. (1977). Self-reference and the encoding of personal information. *Journal of Personality and Social Psychology, 35*(9), 677-688.
- Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science, 12*(2), 257-285.
- Miller, G. A. (1956). The magical number seven, plus or minus two: Some limits on our capacity for processing information. *Psychological Review, 63*(2), 81-97.
- Gobet, F., Lane, P. C. R., Croker, S., Cheng, P. C-H., Jones, G., Oliver, I., & Pine, J. M. (2001). Chunking mechanisms in human learning. *Trends in Cognitive Sciences, 5*(6), 236-243.

### Craft Literature and Web Sources

- Rubin, D. C. (1995). *Memory in oral traditions: The cognitive psychology of epic, ballads, and counting-out rhymes.* Oxford University Press. (On compression and memory in oral-formulaic traditions.)
- Lowrey, T. M. (2006). The relation between script complexity and commercial memorability. *Journal of Advertising, 35*(3), 7-15.
- Gilliam Writers Group (2026). Memory Under Pressure: Compression in the Lyric Poem. https://www.gilliamwritersgroup.com/blog/memory-under-pressure-compression-in-the-lyric-poem
- Writing Academy Blog. (2026). Your Most Memorable Character Needs a Real Contradiction. https://blog.writingacademy.com/why-your-most-memorable-character-needs-a-real-contradiction/
- Nielsen Norman Group. (2018). The Peak-End Rule: How Impressions Become Memories. https://www.nngroup.com/articles/peak-end-rule/
- bibisco Editorial Team. (2026). The Psychology of Memorable Characters: Writing People Readers Believe In. https://bibisco.com/blog/the-psychology-of-memorable-characters-writing-people-readers-believe-in/

---

## 10. Open Questions (for Future Research)

1. **The Stover vs. Calden comparison.** Stover (9 lines, ~90 words, highest-rated) and Calden (~15 lines, higher word count) both passed evaluation. Is Stover more *memorable* than Calden? A systematic comparison would test the compression-mechanism hypothesis directly.

2. **Does the "February" effect generalize?** If every soul had one specific concrete anchor detail, would memorability improve across the board, or would the effect saturate? There may be a diminishing returns curve for concrete details.

3. **Do sign-offs actually drive recall?** The peak-end rule predicts sign-offs matter, but direct testing on the soul format would be valuable: does changing a sign-off from generic to distinctive change reader recall after 24 hours?

4. **Poetry experience among writers.** The Maslej finding suggests poets make better character creators. Do the pipeline's best writers (measured by evaluation scores) have poetry backgrounds? If so, this is a selection signal.

5. **Memorability decay curve for souls.** After 1 hour, 1 day, 1 week — what remains? Only a few anchor details (the contradiction, one specific image, the sign-off phrase) or the full character concept?
