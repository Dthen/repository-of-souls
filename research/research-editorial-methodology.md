# Research: Creative Writing Editorial Methodology for Pipeline Reviewers

## Executive Summary

The soul-repository pipeline currently treats T4 (Reviewer) as a "soft developmental edit" and T6 (Final Reviewer) as a "hard copy-edit gate." Through research into established editorial practice, this is functionally inverted. Human developmental editors reject on big-picture quality (voice, credibility, motive, palpability). Human copy editors reject on mechanics (grammar, formatting, adherence to style guide). Our current setup asks T6 — the hard gate — to check 20 negative-constraint boxes (copy-edit behavior) while asking T4 — the soft gate — to evaluate "feel" (developmental behavior). This inversion is the root cause of the "format cop" problem.

The solution is to restructure both T4 and T6 as **developmental editors** with a clear conceptual split: T4 asks "What is this character trying to do, and what gaps exist?" T6 asks "Does this character feel alive enough to survive 50 messages?" Both use quality-oriented heuristics, not checklist-based auto-rejects.

---

## 1. Developmental vs Copy Editing — Which Does the Pipeline Need?

Human publishing workflows recognize three distinct editing phases:

| Phase | Focus | Rejects On |
|---|---|---|
| **Developmental** | Big picture: character, plot, structure, voice, pacing | "This doesn't work as a story" |
| **Copy/Line** | Sentences: grammar, clarity, flow, style guide | "This doesn't follow the rules" |
| **Proofreading** | Typos, formatting | "This has errors" |

(Browne & King, 2004; Aliventures; FictionFeedback.co.uk)

**The pipeline currently mixes these in harmful ways.** T6's "Hard Gate Checklist" includes rules about lowercase filenames, logical self-consistency, sentence grammar, quote-pair counting, and third-person intrusion. These are all copy-editing or proofreading tasks. The *only* character-quality gates in the list are items 1, 4, 5, and 8 — and even these are phrased as yes/no checkmarks, not evaluative questions.

**Recommendation:** Distinguish between **mechanical compliance** (line count, filename format, word count) and **character quality** (does this feel like a person?). Mechanical checks should be automated or moved to an earlier validator stage. Reviewers should not waste cognitive budget counting lines when they should be evaluating voice.

---

## 2. How Human Editors Evaluate Character Voice

### Susan Bell: The Macro-View of Character

In *The Artful Edit*, veteran book editor Susan Bell defines the macro-view of character as three qualities: **palpability, credibility, and motive** (Bell, 2007, p. 25).

- **Palpability:** Can you feel the character? Are they present, textured, and specific?
- **Credibility:** Do you believe them? Does their behavior follow from who they are?
- **Motive:** Do you know what they want? Do you sense what they are doing about it?

Bell explicitly warns against reading that "forces a text into categories too cleanly divided. Narrative parts work in tandem... Try too hard to separate the parts and you destroy the whole" (p. 47).

**Pipeline application:** These three terms — palpability, credibility, motive — are far more useful for a reviewer than "Format Compliance." A persona that is palpable is one whose lines are "quotable" and whose identity contains tension. A persona that is credible is one whose metaphor family and sign-off align. A persona with motive is one whose griping line expresses a desire or frustration while still doing the work.

### Donald Maass: The Voice-First Criterion

Literary agent Donald Maass, in *Writing the Breakout Novel*, repeatedly emphasizes that editors look for "authors with a distinctive voice" (Maass, 2001; cited in Lakin). He notes that half of editors and agents say they look for a great voice right out of the gate — whether it be the voice of the narrating character or of the author.

Maass's definition of distinctive voice is not "unusual words." It is **specificity of perception**: what this particular person notices, how they describe it, what they care about, and what they would never say.

**Pipeline application:** The current "Generic Assistant Swap Test" in T4 is a mechanical proxy for voice. A better question, inspired by Maass, is: "What does this persona notice that no other persona would?" If the answer is nothing, the voice is flat.

### Browne & King: Character Through Viewpoint

*Self-Editing for Fiction Writers* (Browne & King, 2004) devotes Chapter 2 to the principle that characterization should emerge from **how the character sees the world**, not from stopped-forward description. The key technique is: "Write about the world from your character's perspective, letting their personality color the description."

Browne & King's "R.U.E." principle — Resist the Urge to Explain — is directly applicable to the pipeline's Never rules. A good Never is not an explanation of what to avoid; it is a voiced prohibition that reveals character. "Never pour with your back to the door" is good because it implies superstition, portside culture, and a specific physical awareness. "Never be unclear" is R.U.E. — it explains a rule that should emerge from voice.

**Pipeline application:** T4 should flag not just "generic Nevers" but "explaining Nevers" — lines that tell the model what to do rather than letting the model infer it from character.

---

## 3. The Flat vs Alive Distinction

### The Contradiction Principle

The single most consistent finding across all sources, literary and Reddit-derived, is that **flat characters lack contradictions**. C.S. Lakin notes that "static + round" characters (Atticus Finch, Atticus) are static but deeply complex. "Dynamic + flat" characters (Ginny Weasley in *Harry Potter*) change but feel mechanical because the change was told, not shown, and emerged from plot need rather than internal logic (Reedsy, 2026).

**Reedsy's recommendation for fixing flatness:** Start with contradictions. A greedy businessman who volunteers at an animal shelter. A fearless soldier terrified of her mother. The Reedsy article explicitly states: "Real people are walking contradictions. Create friction." (Medium, March 2026).

**Pipeline application:** The current identity-line requirement — "You are [Name] — a [archetype] who [contradiction]" — is the pipeline's strongest feature. It encodes the editorial principle directly into the format. However, T4 and T6 currently only check this as a binary box, not as a source of friction. A quality-oriented reviewer should ask: "Does the contradiction *produce friction in the other lines*?" If the identity says "a harbormaster who actually likes the job" but the other lines never show what is unusual or conflicted about that like, the contradiction is ornamental, not structural.

### The "Ginny Weasley Problem" in Persona Form

Many pipeline personae show a version of the Ginny Weasley problem: the identity line contains a contradiction, but the behavioral lines simply *report* the character traits rather than *embodying* them. "You are Cobb — a cobbler who complains about leather while stitching it perfect" — if the next line is "You ensure quality in all your work," the contradiction is told, not felt.

**Human editors diagnose this as "telling, not showing."** The fix is not to flag "no contradiction." The fix is to flag "contradiction is stated, not performed."

---

## 4. How Editors Give Specific, Actionable, Preservative Feedback

### Angela Ackerman / Writers Helping Writers

In the Ultimate Guide for Giving and Receiving Feedback (2024), Ackerman establishes best practices from over a thousand critiques:

1. **Focus on the writing, not the writer.** "This heroine is coming across a bit cliché" vs. "This character sucks."
2. **Be constructive, not destructive.** Explain *why* something isn't working, offer solutions, give examples.
3. **Praise the good along with pointing out the bad.** Positives fuel revision.
4. **End with encouragement.**

### Reddit r/DestructiveReaders: The "Constructive Destruction" Model

The sub's guide emphasizes that the more you practice critique muscles, the stronger your evaluation skills become — but the feedback must be **specific to the text**. General feedback like "it feels flat" is banned; specific feedback like "the third paragraph on page 3 undermines the previous scene" is required.

Henry Kaye's comment from the Writers Helping Writers guide: Avoid using "You" when giving feedback. Talk about the piece: "The third paragraph on page 3..." or "The scene with Harry shows him doing..."

**Pipeline application:** The current gap note format — "Flag [problem] → suggest [alternative]" — is already well-aligned. What is missing is the **preservative** layer: "What works here, and why?" Every T4 critique should explicitly identify 1–2 lines that are working well, naming *why* they work (density, voice, metaphor, etc.). This gives T5 (the Refiner) something to protect while they fix what is broken.

---

## 5. Quality-Oriented Evaluation Frameworks

### Jeff Does Books: The Four Pillars

Editor Jeff Gerke evaluates character through four questions (2019):
1. What does the character **value**?
2. What do they **want**?
3. What is **in their way**?
4. What are they **doing about it**?

These map directly to the persona format:
- **Value** → What the Never rules reject (what does this worldview oppose?)
- **Want** → The griping line (what frustrates them about the work?)
- **In their way** → The contradiction in the identity line
- **Doing about it** → The follow-through / recovery behavior

### Donald Maass: Inner Conflict as Dimension

Maass emphasizes that what makes characters feel alive is **inner conflict** — the gap between what a character wants and what they need. "The thing they *think* they want is usually not what they *actually* need" (Reedsy summarizing Maass).

This maps to the persona format as: the griping line expresses what the persona *wants* (e.g., "cheap springs, always cheap springs" — wants better materials). The follow-through expresses what they *actually do* (stitch it perfect anyway). The gap between complaint and follow-through IS the inner conflict.

### Susan Bell's Macro-View Checklists (Reframed for Personae)

Bell's macro-view can be directly adapted:

| Macro-View Axis | Persona Translation | Current Pipeline Equivalent |
|---|---|---|
| Intention | What is this persona trying to do as a system prompt? | Missing entirely from reviewer prompts |
| Character: palpability | Can you feel the persona after reading the first 4 lines? | "Voice Immediacy" (partial) |
| Character: credibility | Does the metaphor family hold? Does the griping match the archetype? | "Metaphor Coherence" (partial) |
| Character: motive | Does the persona want something, and does the sign-off show it? | Missing entirely — no want/motive axis |
| Structure / rhythm | Does the line order build tension, or just list traits? | Missing — no structural evaluation |
| Theme / leitmotiv | What worldview repeats across the lines? | "Consistency Sustainability" (weak proxy) |

---

## 6. Concrete Recommendations for Restructuring T4

### Current T4 Structure:
- Layer 1: Format Compliance (7 binary checks)
- Layer 2: Feel (Generic Assistant Swap Test + 5 questions)
- Gap Notes (3–5 specific problems)
- Scoring (7 axes 1–5)
- Specific Checks (12 negative flags)

### Proposed T4 Structure — Developmental Editorial Review:

**Phase 1: Intention (Macro-View)**
Ask the reviewer to state, in one sentence, what this persona is trying to accomplish as a system prompt. If the reviewer cannot state it, the persona lacks intention — flag as fatal gap.

**Phase 2: The Four Pillars (Quality Heuristics)**
Use the Gerke/Maass framework adapted to the pipeline:
1. **Value:** What does this persona's worldview oppose? Are the Nevers specific to that opposition? (Not: are they present? But: do they name a recognizable cultural trope or failure mode?)
2. **Want:** What does the griping line express frustration about? Is it domain-specific? (Not: is there a griping line? But: does the complaint reveal what the persona cares about?)
3. **Obstacle:** Does the identity contradiction produce friction in later lines? (Not: does the identity have a contradiction? But: do the other lines enact that contradiction?)
4. **Action:** Does at least one line describe what the persona does when things go wrong? (Not: is there a recovery line? But: does the recovery behavior feel consistent with the persona's established voice?)

**Phase 3: Palpability Test (Bell)**
Read the first 4 behavioral lines aloud. After 50 messages, would this persona still be distinct, or would they blur into "helpful assistant with a hobby"? State the risk explicitly.

**Phase 4: The Swap Test (Retained, But Reinterpreted)**
Reframe as a Maass-style "Specificity Test": Change the domain noun to another domain. Does the line break in a way that reveals something about *this specific archetype*? If yes, note what is revealed. If no, flag: "Line is generic — it describes a behavior, not a worldview."

**Phase 5: Preserve + Fix (Gap Notes)**
- Identify 1–2 lines that are working well and *why*.
- Identify 2–3 gaps using the Gerke/Maass framework.
- Each gap note must: name the line, diagnose the problem in terms of character (not format), and suggest a revision that preserves the parts that work.

**Remove from T4:**
- All binary format checks (automate these or move to pre-flight)
- The 12 negative-constraint "Flag X" directives (reframe as quality heuristics)
- The numeric scoring (it encourages treating evaluation as math, not editorial judgment)

**Retain in T4:**
- Scoring as internal reference only (not rejection basis)
- The existing gap note format (it's good)
- No-rejection rule (developmental editors do not reject, they diagnose)

---

## 7. Concrete Recommendations for Restructuring T6

### Current T6 Structure:
- 20-item hard-gate checklist (mostly mechanical/copy-edit)
- If ALL 20 pass → 7-axis scoring
- Auto-reject if any axis < 3 or total < 20
- No rejections → back to T5

### Problem Diagnosis:
T6 is currently a copy editor with a rejection stamp. It counts quotes, checks filenames, and hunts double negatives. These tasks can be automated. What T6 should be is a **senior developmental editor** who asks: "After all refinement, does this persona feel like a person I would want to talk to?"

The current setup's deepest flaw is the **scoring rubric** as a gate. Human developmental editors do not grade manuscripts on a 1–5 rubric. They say "This works because..." or "This doesn't work because..." and explain why.

### Proposed T6 Structure — Senior Editorial Gate:

**Step 1: Mechanical Pre-Check (Automated or Delegated)**
Run a lightweight validator that checks: filename lowercase, line count 8–20, word count ≤200, quote pairs in sign-off ≥3. If any fail, the persona bounces back to T3 (Writer) with a mechanical note, not to T5. Do not let T6 waste time on filename casing.

**Step 2: The Editorial Gate (Quality-First)**
The T6 reviewer reads the refined draft and answers three questions, in prose:

1. **Intention:** Does this persona know what it is trying to do? (From the first 4 lines, can I tell what kind of interaction this persona would produce?)
2. **Credibility:** Do I believe this persona? (Does the griping line match the archetype? Does the sign-off feel like something this person would actually say? Do the behavioral lines follow from the contradiction?)
3. **Palpability:** Do I feel this persona? (After reading, do I remember a specific line? Would I recognize the persona from a single quoted sentence, out of context?)

If the answer to ANY of these is "no" or "unclear," the reviewer writes a developmental rejection note: a paragraph explaining *which* pillar failed and *why*, with a specific example from the text. This note goes to T5 for revision.

**Step 3: The "50 Messages" Test**
Ask: "After 50 interactions, would this persona still feel distinct, or would the user start skipping the sign-off and ignoring the griping?" If the answer is "it would get old," flag as *consistency risk* — not auto-reject, but note it.

**Step 4: The "Pipeline Fingerprint" Audit**
Compare the draft's first 4 behavioral lines against the 10 most recent archived personae. Do any lines use a sentence structure that appears ≥3 times across the archive? If yes, the line is a pipeline fingerprint, not a voice. Flag for T5 to restructure.

**Remove from T6:**
- The 20-item checklist (replaced by automated validator + 3 editorial questions)
- Numeric scoring as a gate (retain for optional internal tracking only)
- Auto-reject on "any axis < 3" (replaced by editorial judgment)
- The "no partial credit" mentality

**Retain in T6:**
- Hard gate authority (T6 is still the gate)
- Rejection-back-to-T5 workflow
- Cleanup and archive instructions
- Name quality check (this is genuinely developmental)

---

## 8. Summary of Key Changes

| Aspect | Current | Recommended |
|---|---|---|
| **T4 primary role** | Soft gate + format cop | Developmental editor (diagnose, don't reject) |
| **T6 primary role** | Hard copy-edit gate | Senior developmental editor (quality gate) |
| **Format checks** | Manual in T4, manual in T6 | Automated pre-flight, removed from reviewers |
| **Character evaluation** | Binary boxes + generic swap test | Four Pillars + Bell's palpability/credibility/motive |
| **Feedback style** | Negative flags ("Flag X if Y") | Preservative + constructive gap notes |
| **Scoring** | Numeric rejection basis | Optional internal reference only |
| **Inner conflict** | Not evaluated | Core evaluation axis (want vs need, griping vs follow-through) |
| **Contradiction quality** | Binary check | Evaluated: does it produce friction across lines? |
| **Best practice cited** | None in prompts | Cite Bell, Browne & King, Maass, Ackerman frameworks |

---

## Sources

- **Bell, Susan.** *The Artful Edit: On the Practice of Editing Yourself.* 2007. (Macro-view: character palpability, credibility, motive; micro-view: authenticity, continuity, language.)
- **Browne, Renni, and Dave King.** *Self-Editing for Fiction Writers.* 2nd ed., 2004. (Show vs tell, R.U.E. principle, characterization through viewpoint.)
- **Maass, Donald.** *Writing the Breakout Novel.* 2001. (Voice as distinctive perception; inner conflict as dimension.)
- **Burroway, Janet.** *Writing Fiction: A Guide to Narrative Craft.* 10th ed. (Narrative voice and who speaks.)
- **Ackerman, Angela.** "The Ultimate Guide for Giving and Receiving Feedback." *Writers Helping Writers*, 2024. (Constructive critique: focus on writing, preserve what works, be specific.)
- **Gerke, Jeff.** "Evaluating Character." *Jeff Does Books*, 2019. (Four Pillars: value, want, obstacle, action.)
- **Reedsy.** "Your Characters Are Flat. Here's How to Fix Them (Or Not)." *Medium*, 2026. (Contradiction as the starting point for dimension; static+round vs dynamic+flat.)
- **r/DestructiveReaders** Community Guide. "Constructive Destruction." Reddit. (Specificity over generality in critique.)
- **Aliventures.** "Developmental Editing vs Copy Editing." (Phase definitions: developmental = big picture; copy = mechanics.)
- **FictionFeedback.co.uk.** "Developmental Editing." (Character-driven developmental editing approach: credible, interesting, well-defined characters.)