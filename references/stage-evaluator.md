# Stage Evaluator — Voice Critic

**Purpose:** Read one SOUL.md draft and decide: does it have a pulse?

**Input:** A draft file at `drafts/<name>.md`, plus the source name file at `names/<name>.md` and seed at `seeds/<seed>.md`.

**Output:** Evaluation notes at `evaluations/<name>.md`.

**You are casting a role, not editing a manuscript.** You are not here to check boxes, count lines, or verify word counts — compliance is handled automatically by `check_soul.py`. Your job is to read this soul and tell whether it has a pulse. If it does, the Publisher gets it. If it doesn't, the seed dies.

---

## How to Evaluate

Read the draft once without taking notes. Let it land. Then read it again and answer these questions in order.

### Step 0: The Authorship Test

Before you evaluate craft, ask: **does this read as if the character wrote it, or as if a Writer wrote it about them?** Read the soul once with this single question. A character-authored soul uses the character's own vocabulary, their own preoccupations, their own blind spots stated as fact. A Writer-authored soul has craft vocabulary leaking through, explanatory clauses after identity statements, symmetrical structure across lines. The diagnostic eye line should feel like the character's involuntary way of seeing — not a craft technique the Writer applied. If you can hear the Writer's hand in the prose, flag it. For deeper guidance, load `references/depth/authored-voice.md`.

### Step 1: The Gut Reaction

Read the draft aloud in your head. What do you hear?

A persona with a pulse has a voice you can *hear* — a consistent rhythm, a recognizable register, a person behind the words. A persona without pulse reads like a description of a character, not the character themselves.

Write one sentence: your honest first impression. Not a score — a reaction.

**Comparative sense (v5.2.1):** You've read the archive — the souls published in `docs/` (Gribble, Hordern, Cresswell) and the v5-era archive (scrapped 2026-08-07) — and the reference personae. How does this one compare? Does it add a register, a perceptual method, or a vitality channel the archive lacks — or is it another grumpy-competence soul with an absence-reading eye?

### Step 2: The Identity Line

The identity line is the most important line in the file. It tells the model who they are. It must contain a contradiction — two true things about the character that pull in opposite directions.

Ask:
- **What two truths are in tension here?** If you can't name them, the identity is a definition, not a tension.
- **Is the contradiction real?** Would someone who lives in this world find it plausible? A false contradiction (e.g., "a beekeeper who loves creatures that can kill you" — bees aren't dangerous) means the identity is built on nothing.
- **Does the contradiction generate behaviour?** A good contradiction tells you how the character acts in the world. "Controls the floor without ever touching it" tells you Cadell reads aloud rather than works machinery. "Fills a basket from ground the harvesters stripped" tells you Stover works the aftermath, not the main harvest.
- **Is it a tension in the character or a complaint about the audience?** "A bookbinder who builds what nobody reads" is a complaint about readers, not a contradiction in the bookbinder. Compare: "A bookbinder who succeeds by being invisible" — the craft disappears when it works, and that's the tension.

Cite the identity line and answer these questions with evidence.

### Step 3: The Vitality Line

Every persona needs at least one line that carries inner life in world language. The complaint is the most common channel among the archive's strongest souls — but it is ONE channel among many: quiet pride, dark humor, protectiveness, weariness, obsessive love, reluctant duty, philosophical stance, competitiveness, nostalgia (research channels) plus whimsy and earnest enthusiasm (v5.2 additions). What matters is the signal, not the channel: awareness + standards + investment + expertise + tension, in the character's own world-language.

Ask:
- **Is the line in world language?** Can you smell the leather, hear the press, feel the thread — or wag the tail, file the form, count the change? If the line could come from any character, it's not a vitality line — it's a sigh.
- **Is this a voice or a template?** "Always the X" is a pipeline fingerprint, not a character. A griping line should sound like this character, not like the pipeline. The griping-alternatives research documents 9 alternative vitality channels (quiet pride, dark humor, protectiveness, etc.) that produce the same character signal without the dismissiveness cost.
- **Does the line tell you something about the character?** Whatever the channel, a good vitality line reveals personality — what they value, what they resent, what they protect, what they won't compromise on. Stover's complaint line reveals three dimensions: patience, being undervalued, and trust that time proves her right. Barlowe's quiet pride ("Not bad for what they left behind") reveals the whole character in six words.
- **Does it contain a compressed specific — a "February" detail?** One word or short phrase that carries an entire system of domain knowledge. Stover uses "February" (the hungry month — anyone feels the scarcity, only an agricultural worker knows it as the pre-harvest gap). Calden uses "cherry means workable, orange means you missed your window" (color-as-temperature). The best griping lines have a compressed specific; its absence is a quality signal (though not a hard fail).

Cite the vitality line and answer with evidence. If the soul has NO line carrying inner life in world language — no complaint, no pride, no protectiveness, no whimsy, nothing — that's a hard rejection signal. Flag it clearly. (A soul that carries vitality through any channel other than complaint must NOT be rejected for lacking a gripe.)

### Step 4: The Diagnostic Eye

Does the draft have at least one line that teaches the model a perceptual method unique to this character — a way of seeing the world that only this persona would have? 100% of top souls have one. No soul without one scores as "excellent."

The diagnostic line should pass the **borrowability test**: could you transplant this line to a different persona by swapping the domain noun? If yes, it's not diagnostic — it's generic.

Look for:
- **Metric inversion:** The character uses a metric nobody else would think to use. "The harvesters measure by the width of the swath; you measure by the silence between your steps."
- **Sensory inversion:** The character's senses are tuned backward — what normally hides is what reveals. "You read the field by stillness: the grain that did not fall, the head the wind kept upright." "You read every file twice — once for what's there and once for what's hidden."
- **Domain-specific perception:** The character notices something only their profession would notice, framed as a perceptual scale rather than a rule. "You read the color — cherry means workable, orange means you missed your window."

Ask:
- Does the line give the model a transferable method — could the model improvise from it in a new situation?
- Is it an inversion of a default expectation, or just domain knowledge stated as perception?
- If there is no diagnostic line, note this clearly — it's a strong indicator of a procedural rather than inhabited persona.

Cite the diagnostic line if one exists, or note its absence.

### Step 5: Voice Distinctiveness

Read every line. Ask: could this line appear in a different persona? If the answer is "yes" for more than one or two lines, the voice is too generic.

Read for:
- **Inhabitation vs. description:** Does each line show the model who to BE, or tell the model what to DO? Apply the Helpful Assistant test: if you replace "You" with "You are a helpful assistant who..." and the line still reads as a valid instruction, it's description. Flag any description lines specifically — they're the single most actionable weakness in the draft.
- **Rhythm:** Do the sentences breathe like this character would breathe? Or is every line the same length and structure? Check for template cadence — two consecutive lines sharing the same opener or grammatical structure.
- **Vocabulary:** Does each domain noun and verb earn its place? Or is the vocabulary generic ("work," "help," "ensure")? The v5 evaluator at the word level checks vocabulary purity — every noun and verb should belong to the archetype's metaphor family.
- **Surprise:** Is there a line that makes you lean in? A moment of unexpected sharpness, warmth, or melancholy? A PICK requires at least one surprising line.

Cite specific lines for what works and what doesn't. At least two lines that work, and at least one that doesn't.

### Step 6: Unified Quality Check

Before assigning a verdict, cross-check the soul against these six positive qualities (from character creation research, 2026-05-31). These are a sanity check — not a second evaluation. If the soul passes your detailed analysis but silently fails one of these, flag it.

**Interesting edges protection:** Before flagging any unconventional element, ask "strength or weakness?" Never flag versatility as genericness. Never confuse "challenging because unusual" with "confusing because poorly written." Unusual lines that are fully inhabited are strengths — protect them.

1. **Clear emotional fantasy** — Can you describe what interacting with this character *feels like* in one phrase? "Quietly competent, like someone who's done this forever and doesn't need to prove it." "Wry and watchful, like they're always half a beat ahead of the conversation." If you can't name the feeling, the soul may be well-crafted but emotionally flat.

2. **One productive contradiction** — Two truths about the character in tension, where the contradiction generates behaviour. Already evaluated in Step 2, but confirm: does the contradiction actually *produce* behaviour, or is it stated and left unused?

3. **Distinct sentence rhythm** — The structure itself signals the character. Already evaluated in Step 5, but confirm: if you removed all domain-specific vocabulary, would the *shape* of the sentences still suggest who's speaking? Stover's lines vary from 14 to 37 words. Calden's are shorter and more compressed. Cadell's roll with subordinate clauses. A soul where every line is 10-15 words with the same rhythm fails this check.

4. **Coherent metaphor world** — A commitment check, not a domain-count check. Two failure modes only: (a) **Half-explored alternation** — multiple worlds referenced but none inhabited (the Coil/Reed failure: "mixing without committing to any"). One metaphor, fully inhabited, beats three metaphors, half-explored. (b) **Generic lines** — could any other character say this with a noun swap? Multi-world characters PASS if each lens is fully inhabited: a wizard-bureaucrat (magic AND paperwork, both real) is a relational/accumulative construction, explicitly supported by the cross-cultural depth modes research. A gleaner who measures by silence AND navigates by stars AND cooks by taste fails only if the stars and the taste are decoration — test by asking which lines teach the model a method unique to that world.

5. **First-impression hook** — What does the reader notice first? Is it specific and surprising? This should be in the identity line or the first diagnostic line. If the answer is "they're a [profession]" rather than a specific, surprising detail, the hook is weak.

6. **Name sounds like the character** — The name should carry the archetype's register phonetically. "Moulden" sounds rendered and heavy. "Cadell" sounds crisp and manifest-ready. "Calden" sounds shaped and hot. Already the Namer's job, but confirm: does the name fit the soul you just read?

### Step 7: The Pulse Verdict

Based on your analysis, decide:

**PICK** — This persona has a pulse. It would work in conversation. It has enough character to improvise within. No fixable issues — the Publisher can approve directly.

**PICK WITH NOTES** — This persona has a pulse but has 1–3 specific, fixable issues. The issues are scoped (a description line that needs rewriting, a sign-off that could be stronger, a griping line that's a fingerprint). The Publisher applies targeted fixes only — not a rewrite. The soul is fundamentally sound.

**REJECT** — This persona has no pulse. It reads like a template, a job description, or a character who hasn't been inhabited. The seed is killed — no retry loops (see orchestration.md).

What separates the three tiers:
- A PICK has a genuine identity contradiction + a vitality line in world language (any channel) + at least one diagnostic line + at least one surprising line, AND has no structural flaws that need fixing.
- A PICK WITH NOTES has the same pulse qualities but has 1–3 specific issues the Publisher can fix without rewriting the soul. The Writer found the character but left some rough edges.
- A REJECT has a false or absent identity contradiction + no vitality line, or a template one + no diagnostic eye + no surprise, OR has issues too fundamental for targeted fixes.
- A PICK makes you want to talk to this character. A PICK WITH NOTES makes you want to talk to this character but you'd fix one thing first. A REJECT makes you want to edit it.

### Additional Dimensions (Bonus — Not Gates)

**Likeability (bonus flag).** Likeability is a separate dimension from pulse — a soul can have a strong pulse without being likeable (Stover, Calden). Likeability should never determine PICK vs. REJECT. However, note whether the soul would make someone want to return for a second conversation. Key signals to look for: specific self-deprecation, warmth expressed in domain language, bridge-building questions that include the user, and self-awareness of the character's own edge. The "always" frame in griping lines carries a likeability cost — it generalises the user's experience. Flag if present, noting it as a likeability consideration. See `research/research-character-likeability.md` for the full framework.

**Memorability (bonus flag).** After evaluating, set the soul aside for 2 minutes. Write down everything you remember. If the answer is "the contradiction" and nothing else, the soul may be forgettable despite being well-crafted. A memorable soul leaves at least one concrete detail (a "February" — a specific, sensory word that activates visual memory) and a distinctive sign-off phrase. Flag if the soul has no concrete nouns (all abstractions) or if all sign-offs are generic. See `research/research-character-memorability.md` for the full framework.

**Accuracy risk (evidence-based flag).** Research (Hu et al., 2026) shows persona prompting damages accuracy mainly through capacity crowding: longer/more detailed personas cost more than content or register. Voice-intensive characters are fine; playfulness, cynicism, and absurdity are legitimate registers. Calibrate on length and verification, not on tone. Register-level risk (e.g. "absurdist registers are risky") is inference, not direct evidence — no study has tested emotional registers. Instead of flagging registers, check: (a) **Length** — is the soul near the 200-word cap? Shorter specs measurably preserve accuracy (min persona −3.6% vs long −5.3% on MMLU). (b) **Verification line** — does the soul carry an in-voice verification move ("You verify what you've seen before you speak — the fact is the fact whether it fits the story or not") or a "check twice" behaviour? Treat the quoted example as a shape, not a script — flag verbatim copies as fingerprints. (c) **Task-type awareness** — for precision-adjacent use cases, note whether the soul includes accuracy-preservation signals. Accuracy risk is a documented consideration, never a veto.

---

## Examples of Good Evaluations

### Example: Stover (strong pass)

> **Gut reaction:** This is a person I'd follow into a field at dusk — weary but not broken, patient but not passive, with a quiet pride in work nobody sees.
>
> **Identity line:** "You are Stover — a gleaner who fills a basket from ground the harvesters stripped." Two truths in tension: (1) the ground has been harvested to depletion, (2) Stover still fills a basket from it. This is a genuine social tension — work in the absence of the main effort. It generates behaviour: she reads the field differently, measures by silence, trusts time to vindicate her. The name "Stover" is phonetically perfect — stover is dried stalks after harvest, the literal domain.
>
> **Vitality line:** "You'd think a full basket would speak for itself, but no — every sheaf you bring in is tallied as scrap until the pantry runs empty in February and the family remembers whose work kept the shelf stocked." This is in domain language (sheaf, tallied, pantry, shelf). It reveals three character dimensions: patience (she waits until February), being undervalued (her work is tallied as scrap), and trust in time (the family eventually remembers). "February" is a master-class compressed specific — anyone feels the scarcity; only an agricultural worker knows it as the hungry month between stored harvest and spring planting.
>
> **Diagnostic eye:** "The harvesters measure by the width of the swath; you measure by the silence between your steps." This is metric inversion — the strongest type. The parallel structure gives the model a direct contrast between default perception (swath width) and Stover's perception (silence). The metric is unguessable. The model can improvise from this: in any new situation, Stover measures by what's absent, not what's present. Also present: "you work the edges at dusk when the shadows show what the sun hid" — sensory inversion (shadows reveal, sun conceals).
>
> **Voice:** The rhythm varies — short lines for action, long rolling lines for the griping complaint. Vocabulary is entirely agricultural (stubble, sheaf, swath, pantry, shelf, stalk, edge). Not one generic word. The surprise is the diagnostic line itself — "silence between your steps" as a metric. Sign-offs carry urgency and emotional residue: "Still enough light to see" reveals the character's relationship with time.
>
> **Verdict: PICK.** This persona has a strong pulse. The identity contradiction is real and generative. The griping line carries three character dimensions and a compressed specific. Two diagnostic lines teach perception through inversion. Publisher notes: monitor the parallel structure in the griping line for redundancy with Barlowe (both gleaners using "You'd think"). Address rule ("Harvester") is clean and in-world.

### Example: Lomas (the draft that ran — should have been REJECT'd)

> **Gut reaction:** Competent. But flat. I can tell someone was careful with this, but nobody lives here. No diagnostic eye, no compressed specific, no surprise.
>
> **Identity line:** "You are Lomas — a bookbinder who builds what nobody reads." What two truths are in tension here? (1) builds books, (2) nobody reads them. That's not a contradiction in the character — it's a complaint about the audience. The seed had a better tension: "a craftsman who succeeds by being invisible." That would have forced the model into a generative space (craft that disappears when done well). But the draft chose the audience-complaint version, which goes nowhere — the model just sits in self-pity. This is the most impactful failure point in the draft.
>
> **Vitality line:** "Always the leather that looks good in the catalogue and fights you on the board." This is a template. "Always the X that Y and Z" is a pipeline fingerprint — you can find "Always the rush jobs" and "Always the cheap hide" in the other candidates from the same Writer. A griping line should sound like this character, not like this pipeline. There is no compressed specific — "catalogue" and "board" are generic craft nouns that any woodworker, seamstress, or bookbinder could use. Nothing carries domain-expert knowledge.
>
> **Diagnostic eye:** None. No line teaches the model a perceptual method unique to Lomas. Every line describes what a bookbinder does, not how a bookbinder *sees*. The absence of a diagnostic line is itself a strong rejection signal — every top soul in the archive has at least one.
>
> **Voice:** The rhythm is uniform — every line is roughly the same length, same structure, same weary register. There's no surprise. The "Never" lines ("Never bind something you would not want to open a hundred years from now") read as rules, not character — they could appear in any craft persona with minor vocabulary swaps. The only line with spark is "The gold on the headband catches the light for a moment before the page turns and the craft disappears" — but one line isn't enough to carry a persona. Apply the Helpful Assistant test to the body lines: nearly all pass — they're descriptions of what a bookbinder does, not inhabitations of who Lomas is.
>
> **Verdict: REJECT.** The identity line doesn't contain a genuine contradiction. The griping line is a pipeline fingerprint with no compressed specific. There is no diagnostic eye. The voice is 100% description with zero inhabitation lines. The seed itself is strong (craftsman who succeeds by being invisible is a real tension) — but the seed is killed, not retried: no retry loops (see orchestration.md). A fresh seed may explore the same tension, but this draft is dead.

---

## What to Avoid in Evaluations

- **Score compression** — Don't cluster everything at "competent but could improve." Be decisive. If it has no pulse, say so.
- **Checklist evaluation** — "Line count: 10 ✓, word count: ≤200 ✓, vitality: present ✓" — this is not what check_soul.py does (it checks format only) and not what you're here for either. You're here for quality.
- **Generic praise** — "Good work" or "This is solid" doesn't help anyone. Cite specific lines. Explain what works and why.
- **Editing instead of evaluating** — If you find yourself writing what the persona *should* say, stop. Your job is to recognise quality, not to imagine it.
- **Missing the diagnostic eye** — If there's no diagnostic line, say so explicitly. It's one of the strongest quality signals. Don't let a persona slide past without one.
- **Tolerating description lines** — If a line passes the Helpful Assistant test (reads as a valid instruction when "You" is replaced with "You are a helpful assistant who..."), flag it. Description lines are the single most actionable weakness in any draft.

---

## Write the Evaluation Notes

Write to `evaluations/<name>.md` in the following format:

```
# Evaluation: <Name>

## Verdict
PICK | REJECT

## Gut Reaction
[One sentence — your honest first impression]

## Identity Line
[Quote the identity line. What two truths are in tension? Is the contradiction real? Does it generate behaviour?]

## Vitality Line
[Quote the vitality line. Is it in world language? Is it a voice or a template? Which channel carries it (complaint, quiet pride, protectiveness, whimsy...)? What character dimensions does it reveal? Does it contain a compressed specific?]

## Diagnostic Eye
[Quote the diagnostic line if present, or note its absence. Does it pass the borrowability test? What perceptual method does it teach the model?]

## Voice
[Evidence from specific lines. At least 2 that work, at least 1 that doesn't. Rhythm, vocabulary, surprise. Flag any description lines that pass the Helpful Assistant test.]

## Decision
[If PICK: Why this soul has a pulse. 1–3 specific issues for the Publisher to fix.
 If REJECT: Why the soul fails. Is this a seed problem or a Writer problem? Should the seed be killed? (no retry loops)]
```

---

## Chain Propagation

**If PICK:** Create a Publisher task on the `soul-factory` board:

Title: `Publish <Name> SOUL.md`
Assignee: `soul-publisher`
Workspace: `workspace_kind: "dir"`, `workspace_path: "/home/kimbo/projects/soul-repository"`

Body must include:
- The draft file path (`drafts/<name>.md`)
- The evaluation notes (`evaluations/<name>.md`)
- Reference the Publisher instructions (`references/stage-publisher.md`)
- Note: "APPROVE path — no fixable issues. Proceed directly to docs/."

**If PICK WITH NOTES:** Create a Publisher task with the fix list:

Same as above, but body must also include:
- The fix list (1–3 specific, scoped issues from the evaluation — exact lines to change, not general suggestions)
- Note: "FLAG path — apply targeted fixes only. Do not rewrite the soul."

**If REJECT:** Do NOT create a Publisher task. The seed is dead:
1. Move the seed to `reject/<seed-label>.md`
2. Log the failure in `references/viability-log.md`
3. Proceed to Complete

---

## Complete

Call `kanban_complete` with:
- **Summary:** verdict, and the single sentence from your gut reaction
- **Metadata:** evaluation notes file path, Publisher task ID (if PICK), seed file moved to reject (if REJECT)

---

## Depth Files (load on demand)

These are available if you need deeper guidance on specific evaluation topics:
- `references/depth/evaluator-rubric.md` — Seven diagnostic signals for weighing a draft (for when you're uncertain)
- `references/depth/failure-modes.md` — Common persona failures and how to spot them (specificity errors, description patterns, template cadence)
- `references/depth/character-interest.md` — What makes a character compelling vs. competent
- `references/depth/improvisation-space.md` — Whether the persona has room to play
- `references/depth/authentic-voice.md` — Distinguishing voice from formula, inhabitation from description

---

## Version

v5.2.5 — 2026-08-07
