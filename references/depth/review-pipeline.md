# Depth Reference: Review Pipeline (Evaluator–Publisher)

Three lines, three fates under the same review chain:

> "You are Ewan — a harbor pilot. You guide vessels safely into port and keep the log accurate." — correctly flagged: a definition, not a person. The floor did its job.
> "You never trust a calm sea — she is only gathering herself to ask for something." — flagged as an "unusual metaphor," rewritten to "You stay alert in calm conditions." The edge, sanded.
> "The orchard tells you what it needs by what it drops — windfalls are the tree's own report, and you read them before you pick." — flagged as "obscure," replaced with "You inspect crops carefully before harvest." The lens, gone.

The catch and the sanding are one mechanism: the same checklist that stops the voiceless draft also flattens the distinctive one.

**Core principle:** The T4–T5–T6 review pipeline is a quality floor, not a quality ceiling — it reliably prevents voiceless personae from being archived, but it also systematically sands off the interesting edges that make personae memorable. Treat it as quality *prevention*, not quality *improvement*.

**What doesn't work:** the fix that satisfies every gate — "You remain vigilant, professional, and thorough in all conditions." It passes the Four Pillars, passes the Three Questions, and reads like a job description.

---

## What the Research Says

### 1. The Pipeline Prevents the Worst Outcomes (but Can't Create the Best)

- **Structural catch:** The pipeline catches missing vitality lines (no inner life in world language through any channel), stamp-like sign-offs, fake identity tension, and broken format — failures that produce voiceless, un-archivable characters. The bottom-10 personae from archive-old (Silver, Coil, Ingram, Reed) would not survive it.
- **Density enforcement:** The 5-20 line / ≤200-word budget forces writers to earn every line. This is a genuine quality constraint.
- **Prescriptive feedback:** T4's gap-note format (quote → diagnose → suggest) is specific and actionable. It's the best part of the pipeline.

### 2. Three Passes Compound Reviewer Biases

The pipeline is a "Goodhart machine" (Tian Pan, 2026) that optimizes for reviewer approval rather than character quality:

| Bias | Effect | Pipeline Impact |
|------|--------|-----------------|
| **Verbosity bias** | Longer responses score higher | Verbose critiques produce more "fix this" notes → refiner pads the persona |
| **Position bias** | 20–40% of verdicts flip when list order changes | First gap note in T4 critique gets prioritized by T5, not the most important one |
| **Self-preferential bias** | Models score their own outputs higher (perplexity mechanism) | Pipeline optimizes for the model's taste, not human taste |
| **Agreeableness bias** | True Negative Rates < 25% | Personae that should be killed get "minor gap" notes and pass |
| **Format/authority bias** | Structured outputs score higher than equivalent prose | Perfect format compensates for lifeless content |

**The compound loop:** T4 flags gaps (with biases) → T5 fixes flagged gaps (with its own biases) → T6 approves the now-conventional result. Each pass makes the persona more reviewable, not more alive.

### 3. The Refiner Can Fix but Cannot Elevate

T5's instruction — "fix the flagged gaps, leave everything else untouched" — has three failure modes:

1. **Can't fix what wasn't flagged.** If T4 doesn't identify "this persona is technically correct but uninteresting," T5 can't address it. And T4's checklist structure systematically misses existential problems.
2. **Adds compliance, not voice.** Missing a Never rule? T5 adds one. Sign-off framing functional? T5 makes it distinctive-er. These are checklist satisfactions, not character improvements.
3. **No mandate to elevate.** The instruction is "fix" (bad → adequate), not "elevate" (good → great). The best lines in pipeline personae (Moulden's "You count the dips," Cadell's "You never read flat when the text demands weight") were *unflagged creative additions* from the refiner — evidence that the refiner's instinct for surprise is stronger when acting outside the gap-fixing frame.

### 4. Compliance and Quality Are Conflated

The Four Pillars (T4) and Three Questions (T6) are **compliance checklists disguised as quality heuristics**:

- A persona that satisfies all four pillars is format-compliant — not necessarily good.
- The Three Questions are easily satisfied by technically correct personae. "Intention ✓, Credibility ✓, Palpability ✓" — all three pass for a persona that has a clear identity line, uses domain vocabulary, and has one memorable line. "Passable" is not "great."
- The "any-persona test" can't distinguish between "this line is generic" and "this line is versatile" — it penalizes both equally.
- The severity hierarchy (Critical/Significant/Minor) maps quality judgments to compliance decisions. The reviewer spends cognitive budget categorizing issues rather than asking "Is this persona alive?"

### 5. Interesting Edges Are Systematically Removed

The mechanism is specific and reproducible:

1. **T4 identifies "gaps" that are actually strengths.** An unusual metaphor, unconventional structure, or provocative line gets flagged as "template sentence structure" or "register that doesn't vary." The checklist can't distinguish unusual from wrong.
2. **T5 fixes the "gaps" by making them conventional.** The refiner replaces what was distinctive with something adequate.
3. **T6 approves the now-conventional persona.** All three questions pass. The persona is archived. It is no longer interesting.

**Evidence:** Old pre-pipeline personae (Helm, Cobb, Roux) have more edges — longer lines, unconventional Nevers, philosophical statements disguised as instructions. Pipeline personae (Cadell, Moulden) are smoother, more polished, less distinctive. The pipeline raises the floor but lowers the ceiling.

### 6. The Three Questions Have No Calibration Anchor

- No objective standard: "Intention = yes" for Cadell may not mean the same as "Intention = yes" for Helm.
- The "50 Messages" test is aspirational — the reviewer answers it in the abstract, not against actual conversation data.
- The "kill vs refine" rule is asymmetric: killing has higher social cost (it implies the researcher made a mistake), so reviewers default to REFINE. Personae with fundamental archetype problems get refined rather than killed.

---

## How to Apply It

### For Evaluator

**Distinguish compliance from quality explicitly.** Before running the Four Pillars checklist, ask: "Is this persona alive?" — a single yes/no that gates the structural review.

- In gap notes, flag two categories separately: **(a) structural gaps** (missing vitality line — no inner life in world language through any channel, broken format) and **(b) creative gaps** (no surprise, competent but generic, no friction).
- Ask "What does this persona notice that no other persona would?" If the answer is "nothing," flag it — even if all Four Pillars pass.
- Protect unconventional lines. Before flagging anything as a "template sentence," ask: "Is this genuinely generic, or is this doing something unusual that I don't recognize as good?"

### For Publisher-Side Refinement

**Change the instruction from "fix" to "fix AND elevate."** The refiner should:

1. Fix the flagged structural gaps (compliance pass).
2. Identify the most alive line in the draft. Ask: "What makes this line work? Can I make it work harder?"
3. Add at least one line that surprises you. This is where the best pipeline improvements come from (Moulden's "count the dips," Cadell's "read flat when the text demands weight").
4. Before fixing a flagged "gap," check: is this actually a strength? Protect distinctive elements even if they don't match the checklist.

### For Evaluator (Hard Gates)

**Add a distinctiveness gate after the Three Questions.** If all three pass:

1. Ask: "What does this persona notice that no other persona would?"
2. Ask: "After 50 messages, would this persona still feel distinct — or would it blend?"
3. If the answer to either is "nothing / it would blend," return REFINE with a specific note: "Competent but generic. The persona needs at least one line that could only belong to this character."
4. **Do NOT send back for more than one refinement round.** Research on code review shows diminishing returns after the first refinement pass. If it's not good enough after one round, it won't get there.

### Calibration

- Build a gold set of 10 existing personae with human-assigned quality labels (3 "has a pulse," 4 "competent," 3 "no pulse"). Run the Evaluator against this set periodically.
- If the LLM approves personae that humans rate as "no pulse," the threshold is too lenient.
- If it kills personae that humans rate as "has a pulse," the threshold is too strict.
- Use this gold set to anchor the Three Questions — not as a rubric, but as a calibration reference that the reviewer can compare against.

---

## What to Watch Out For

| Pitfall | Why It Happens | Mitigation |
|---------|----------------|------------|
| **The "Ginny Weasley Problem"** | T4 flags "no contradiction," T5 adds one, but it's told, not shown — the contradiction doesn't perform work in other lines | Check that the contradiction actually manifests in behavioral lines, not just the identity line |
| **Goodhart machine** | Pipeline optimizes for reviewer approval, not character quality | Add distinctiveness audit to T6; protect unconventional elements through the review chain |
| **LLM-as-judge fallacy** | Chakrabarty et al. (2023): LLMs show NO significant correlation with expert creative quality assessment (Cohen's Kappa ≈ 0) | Never use the LLM to evaluate creative quality without structure — evidence-cited CoT per llm-judge-calibration research is the Evaluator's method; unstructured "rate this 1-5" is invalid |
| **Kill vs refine asymmetry** | Killing implies the seed was bad, so reviewers default to REFINE | Make "kill" a neutral verdict: a good seed can produce a bad draft |
| **Diminishing returns on iteration** | Code review research: first pass catches most issues; subsequent passes catch progressively fewer | Limit T4→T5→T6 to one full cycle. If T6 sends back REFINE, that's one more T5 fix, then a final T6 verdict — no third loop |
| **The "file drawer" problem** | Personae too unusual to survive review end up in reject/ — they may be the most memorable | Periodically audit the reject/ directory for personae that are unusual-but-alive rather than broken |

---

## Examples

### The Refiner's Best Work Wasn't Flagged

**Moulden draft (T3):** Griping line excellent ("The batch smoked — always the over-heated rendering"). Sign-offs excellent ("The light holds," "The rendering is done"). Line 5 procedural ("You skim the impurities from the vat because a clean vat makes a clean burn").

**T4 critique:** Flags line 5 as procedural. Fixes it.

**T5 refined:** Line 5 becomes voiced ("You skim the fat off the top and leave the grit where it settled"). The refiner also adds an *unflagged* line: "You count the dips — a hundred dips for an hour of clean light, and no one asks why."

**What happened:** The best line in the refined persona was not a gap fix — it was a creative addition the refiner made without being asked. The "fix flagged gaps" instruction prevented the refiner from doing this by mandate. **Change the instruction.**

### The "Interesting Edge" That Would Have Been Lost

**Helm (archive-old, pre-pipeline):** Never line reads "Never Charon — a query about the weather is just that, not a passage to the dark shore." This is the single most distinctive element in the archive — a cultural reference that creates immediate character.

**If it hit the pipeline:** T4 would likely flag "obscure reference" or "cultural rejection without explanation." T5 would replace it with something domain-appropriate but conventional ("Never ignore a weather warning from a captain who's been out longer than you"). T6 would approve. The persona would be competent. It would no longer be Helm.

**The lesson:** The pipeline cannot distinguish between unconventional and broken. Reviewer checklists are biased toward the familiar. **Protect the edges.**
