# Meta-Analysis: Does the Review Pipeline (T4-T5-T6) Improve Character Prompts?

**Date:** 2026-06-02
**Scope:** The soul-repository's T4 (Reviewer) → T5 (Refiner) → T6 (Final Reviewer) pipeline. Does iterative review actually improve character prompts, or does it sand off the interesting edges?

---

## Executive Summary

The T4-T5-T6 review pipeline does two things well and three things poorly.

**What it does well:**
1. It catches structural failures — missing griping lines, stamp-like sign-offs, fake identity tension — that would produce voiceless characters. The pipeline is good at preventing the worst outcomes.
2. It enforces density and format compliance, which forces writers to earn every line. The 8-20 line / 200-word budget is a genuine quality constraint.

**What it does poorly:**
1. It optimizes for format compliance over character quality. The review stages spend cognitive budget on structural checklists (Four Pillars, Three Questions) that can be satisfied by technically correct but lifeless writing.
2. It compounds LLM reviewer biases across three passes — verbosity bias, position bias, and self-preference bias accumulate, pushing personae toward the model's center of mass rather than toward distinctive voice.
3. It removes the most interesting parts of character prompts. The review process systematically flags unconventional elements as "gaps" and refines them into conventional forms. The result is personae that are competent but safe.

**Bottom line:** The pipeline is a quality floor, not a quality ceiling. It prevents bad personae from being archived. But it also prevents great personae from being archived — because greatness requires edges, and edges look like gaps to a reviewer following a checklist.

---

## 1. Does Iterative Review Improve Creative Work?

### The Publishing Industry

The editorial process in publishing — developmental edit, line edit, copy edit, proofread — is the closest analog to our T4-T5-T6 pipeline. Research on this process reveals a consistent pattern:

**Developmental editing improves mediocre work more than it improves excellent work.** Angela Ackerman's research on constructive feedback (Writers Helping Writers, 2024) establishes that the most effective critiques are "specific to the text" and "preserve what works." But the key finding is implicit: editing helps most when there are clear structural problems to fix. For work that already has strong voice and tension, editing risks introducing conformity.

**The "Ginny Weasley Problem" is a review failure mode.** C.S. Lakin's research on flat characters (cited in our own research-editorial-methodology.md) identifies the "Ginny Weasley Problem": characters who are told to have contradictions but whose behavioral lines simply report traits rather than embodying them. Our own pipeline produces this exact failure mode — the T4 critique identifies contradictions, the T5 refiner adds them, but the result is told, not shown. The review process catches the symptom (missing contradiction) but not the disease (the contradiction isn't performing work in the other lines).

**Preservative feedback is the key differentiator.** Ackerman's research shows that the most effective critiques explicitly identify what works and why, not just what doesn't work. Our T4 reviewer does include preservative feedback ("cite 2-3 lines that work"), but the T5 refiner's instruction is "fix the flagged gaps, leave everything else untouched." This creates a subtle problem: the refiner has no mandate to *elevate* the preserved lines — only to leave them alone. The result is a persona where the good lines stay good and the bad lines become adequate, but the overall character doesn't improve.

### The Film Industry

Film test screenings are the most direct analog to our review pipeline — a panel evaluates work-in-progress and provides structured feedback.

**Test screenings are good at catching unintended confusion but bad at preserving intentional challenge.** Goetz (2021) documents that 90% of studio films are test-screened, and the process systematically pushes toward clearer resolution, conventional endings, and broader appeal. Famous examples: *Pretty in Pink*, *Fatal Attraction*, and *National Lampoon's Vacation* all had endings reshot after test screenings.

The parallel to our pipeline is direct: T4 identifies confusion (the "gap note" system), T5 resolves it (the "fix the flagged gaps" instruction), and T6 verifies resolution (the "Three Questions" gate). But confusion and challenge are not the same thing. A character with genuine tension — like Helm's "harbormaster who actually likes the job" — could be flagged as "confusing" by a reviewer who doesn't understand why a harbormaster would like the job. The review process can't distinguish between "this is confusing because it's poorly written" and "this is challenging because it's doing something unusual."

**The "test screening effect" homogenizes.** Ebert (2004) notes that test screenings produce films that are "more conventional, less daring." The same mechanism operates in our pipeline: each T4-T5-T6 pass makes the persona more conventional and less daring. The persona that survives review is the one that offends no reviewer — which means it has no edges.

### Software Engineering

Code review research provides a useful counterpoint because software review has measurable outcomes (bug rates, maintainability).

**Code review catches bugs but doesn't improve architecture.** Studies consistently show that code review reduces defect rates by 30-50% but has diminishing returns on code quality beyond a certain threshold. The first review catches the most issues; subsequent reviews catch progressively fewer and less important ones.

**The parallel:** Our T4-T5-T6 pipeline has three review passes. The first pass (T4 → T5) catches the most significant issues. The second pass (T6) catches fewer issues. If T6 sends back to T5 again (REFINE verdict), the third pass catches even fewer. At some point, additional review cycles are not improving the persona — they're just adding review-shaped noise.

### Academic Peer Review

**Peer review rewards legibility over novelty.** Fang et al. (2022, PNAS) found that highly novel papers get more citations but lower acceptance rates. Review rewards "novelty that is legible within existing frameworks" — not disruptive novelty. The parallel: our LLM reviewers will favor character prompts that are novel-but-familiar, not genuinely surprising. A persona that follows the format perfectly but says nothing new will score higher than a persona that bends the format but creates something memorable.

**The "file drawer problem" applies to personas.** In academic publishing, negative results don't get published. In our pipeline, personae that fail review don't get archived. But the failure mode is different: in publishing, the "file drawer" contains boring negative results. In our pipeline, the "file drawer" (reject/) may contain personae that are too unusual to survive review — personae that would be the most memorable and distinctive if they were allowed through.

---

## 2. The Compliance vs Quality Problem

**The pipeline's central design flaw is that it asks LLM reviewers to evaluate both format compliance and creative quality in the same pass.**

Our own research (research-editorial-methodology.md) identified this problem clearly: "Our current setup asks T6 — the hard gate — to check 20 negative-constraint boxes (copy-edit behavior) while asking T4 — the soft gate — to evaluate 'feel' (developmental behavior). This inversion is the root cause of the 'format cop' problem."

The pipeline has since been restructured to separate compliance (automated via `check_soul.py`) from quality (LLM-judged). But the restructured T4 and T6 prompts still conflate compliance with quality in subtle ways:

**The Four Pillars (T4) and Three Questions (T6) are compliance checklists disguised as quality heuristics.** The Four Pillars — Intention, Tension, Specificity, Follow-through — are evaluated with binary yes/no/mostly answers. A persona that satisfies all four pillars is format-compliant, not necessarily good. The Three Questions — Intention, Credibility, Palpability — are better, but the evidence-grounding requirement ("cite 2-3 lines") creates a compliance loop: the reviewer must find evidence that the persona is good, which means it must have lines that can be cited as good, which means it must have lines that look like the reference personae.

**The "any-persona test" is a compliance test, not a quality test.** T4's reference material includes the "any-persona test" — swap the domain noun and see if the line breaks. This is a useful test for detecting generic lines, but it has a failure mode: it also detects *unusual* lines that happen to work across domains. A line like "You'd think they'd notice when the coastline moves" would pass the any-persona test for a cartographer (it's specific) but would also survive swapping for a ferryman or a lighthouse keeper (it's about noticing change). The test can't distinguish between "this line is generic" and "this line is versatile."

**The severity hierarchy is a compliance checklist.** T4's severity hierarchy — Critical (blocks pipeline), Significant (needs refinement), Minor (acceptable) — is a binary classification system that maps quality judgments to compliance decisions. A "critical" issue is one that blocks the pipeline, not one that makes the persona worse. The result: the reviewer spends cognitive budget categorizing issues by severity rather than evaluating whether the persona is alive.

---

## 3. The Reviewer Bias Problem

LLM reviewers have systematic biases that compound across review passes. Five biases are well-documented:

### Verbosity Bias
**Longer responses score higher regardless of quality.** GoDaddy Engineering (2025) and Galtea (2026) both document this. The mitigation in our pipeline — the 200-word limit — reduces but doesn't eliminate the bias. The T4 and T6 reviewers evaluate personae within the word limit, but their *critiques* and *rejection notes* are not bounded. A verbose reviewer produces verbose gap notes, which the refiner interprets as "fix more things," which pads the persona.

### Position Bias
**First or last items in a list score higher.** arXiv:2506.22316 (DASFAA 2026) finds that 20-40% of verdicts flip when positions are swapped. In our pipeline, this means the order of gap notes in the T4 critique affects which gaps the T5 refiner prioritizes. If the first gap note is about sign-offs, the refiner fixes sign-offs first and may not get to the more important identity-line issue.

### Self-Preferential Bias
**Models score their own outputs higher.** Wataoka et al. (ICLR 2025) document this through a perplexity-based mechanism: models find their own outputs less surprising, which they interpret as higher quality. In our pipeline, if the same model writes and judges, the reviewer will favor personae that match its own writing style. This means the pipeline optimizes for the model's taste, not for human taste.

### Agreeableness Bias
**True Negative Rates below 25% — reviewers confirm more than they challenge.** This is the most damaging bias for our pipeline. An agreeable reviewer will find reasons to approve personae that should be killed, and will produce "minor" gap notes when "critical" issues exist. The result: personae that should be rewritten are instead given minor fixes, and the pipeline archives competent-but-lifeless characters.

### Format/Authority Bias
**Structured outputs score higher than equivalent prose.** A persona that follows the format perfectly — identity line with em-dash, behavioral lines in second person, sign-offs in quotes — will score higher than a persona that bends the format but creates more distinctive voice. Our pipeline's `check_soul.py` enforces format, but the LLM reviewers also reward format compliance in their quality judgments.

### The Compound Effect

In iterative loops (T4 → T5 → T6), these biases compound:

1. **Pass 1 (T4):** The reviewer identifies "gaps" using a compliance checklist. Verbosity bias makes the critique verbose. Position bias affects which gaps are prioritized. Agreeableness bias makes the reviewer find more things that "work" than actually do.

2. **Pass 2 (T5):** The refiner fixes the flagged gaps. Self-preferential bias means the refiner's fixes match the model's own style. The persona becomes more model-typical.

3. **Pass 3 (T6):** The final reviewer evaluates the refined version. Format/authority bias rewards the now-perfected format. Agreeableness bias makes the reviewer approve it. The persona is archived.

The result is what Tian Pan (2026) calls a "Goodhart machine" — the pipeline optimizes for reviewer approval rather than character quality. Each pass makes the persona more reviewable, not more alive.

---

## 4. The Refiner Drift Problem

The T5 refiner's instruction is "fix the flagged gaps, leave everything else untouched." This is the correct instruction for a surgical editor — but it has a failure mode in practice.

### What Actually Happens

Looking at the Cadell pipeline (the most complete pipeline artifact in the archive):

**Draft (T3 output):** 9 lines, 818 bytes. Identity line is strong. Griping line sings. Middle lines describe competence without friction.

**Critique (T4 output):** Score 2/3. Five gap notes: template sentence structure (line 7), procedural recovery (line 8), missing Never rule, narrow middle register, sign-off framing.

**Refined (T5 output):** 11 lines, 1024 bytes. The refiner:
- Replaced the template sentence ("The pause is your sharpest tool") with a more voiced version ("You hold the silence longer than anyone expects")
- Added a new line about monotony ("You read the same serial chapter by the third shift")
- Added a Never rule ("You never read flat when the text demands weight")
- Fixed the recovery line to be more domain-specific
- Changed sign-off framing from "crisp and final" to "close the chapter"

**Final Review (T6 output):** APPROVE. All three questions pass.

### What the Refiner Actually Did

The refiner did exactly what it was told: fix the flagged gaps, preserve the strong lines. But the result is instructive:

1. **The good lines stayed good.** The griping line ("You'd think the foreman could learn to hold a pen") was unchanged. The noise-gauging line was unchanged. The emphasis line was unchanged. The preservative feedback worked — the refiner protected what the reviewer said was good.

2. **The fixed lines became adequate.** The template sentence was replaced with a more voiced version. The procedural recovery was replaced with a domain-specific one. The missing Never was added. The sign-off framing was improved. All five gaps were addressed.

3. **But the overall character didn't improve.** The refined version is technically better — it has a Never, warmer sign-offs, a more voiced recovery line. But it's not *alive* in a way the draft wasn't. The refiner added lines that fix structural problems without adding the friction, tension, or surprise that would make the persona memorable.

### The "Fix Flagged Gaps" Failure Mode

The T5 instruction "fix the flagged gaps, leave everything else untouched" has three failure modes:

**Failure 1: The refiner can't add what wasn't flagged.** If the T4 critique doesn't identify a problem, the refiner can't fix it. But the T4 critique is itself limited by the reviewer's biases and the checklist structure. Problems that don't fit the checklist — "this persona is competent but uninteresting," "this persona has no surprise," "this persona is technically correct but emotionally void" — don't get flagged, so they don't get fixed.

**Failure 2: The refiner adds compliance, not voice.** When the critique says "missing Never rule," the refiner adds a Never. When the critique says "sign-off framing is functional, not distinctive," the refiner makes the framing more distinctive. But these additions are compliance-driven — they satisfy the reviewer's checklist, not the character's needs. The result is a persona that checks more boxes without being more alive.

**Failure 3: The refiner can't elevate.** The instruction is "fix," not "elevate." Fixing a gap brings the line from "bad" to "adequate." But the persona needs lines that go from "good" to "great" — lines that surprise, that create friction, that would be memorable after 50 messages. The refiner has no mandate and no mechanism for this.

### The "Moulden" Example

The Moulden pipeline shows the same pattern:

**Draft:** Griping line is excellent ("The batch smoked — always the over-heated rendering"). Sign-offs are excellent ("The light holds," "The rendering is done," "The vat is clean"). But line 5 is procedural ("You skim the impurities from the vat because a clean vat makes a clean burn").

**Refined:** Line 5 is fixed ("You skim the fat off the top and leave the grit where it settled — a clean vat starts with what you refuse to keep"). The griping line and sign-offs are preserved. A new line about counting dips is added ("You count the dips — a hundred dips for an hour of clean light, and no one asks why").

**The new line is the best line in the refined version.** "You count the dips — a hundred dips for an hour of clean light, and no one asks why" is more alive than anything in the draft. But it wasn't flagged by the critique — it was added by the refiner as filler to meet the line count. This is the refiner drift problem: the best improvements come from the refiner's creative additions, not from fixing flagged gaps.

---

## 5. The Approval Threshold Problem

T6's Three Questions — Intention, Credibility, Palpability — are a 3-point checklist. If all three pass, the persona is approved. The question: is this checklist too lenient or too strict?

### Too Lenient

**The Three Questions are easily satisfied by technically correct personae.** A persona that has a clear identity line (Intention ✓), uses domain-specific vocabulary (Credibility ✓), and has one memorable line (Palpability ✓) will pass all three questions. But "passable" is not "great." The threshold is designed to prevent bad personae from being archived, not to ensure that only great personae are archived.

**The evidence-grounding requirement creates confirmation bias.** T6 requires the reviewer to "cite 2-3 lines that work" and "cite 2-3 lines that don't." This forces the reviewer to find evidence on both sides, which is good for balanced evaluation. But it also means the reviewer must *find* lines that work — and if the persona is technically correct, the reviewer will always find something to cite. The result: almost everything passes.

**The "50 Messages" test is aspirational, not enforced.** T6's reference material includes the "50 Messages" test — "After 50 interactions, would this persona still feel distinct?" But this is a thought experiment, not a verification step. The reviewer answers it in the abstract ("I believe this persona would survive 50 messages") rather than testing it against actual conversation data.

### Too Strict

**The "kill vs refine" rule is asymmetric.** T6's instruction says: "If the gap is in Intention (the archetype itself is flawed), kill it. If the gap is in Credibility or Palpability (the writing is weak but the archetype is sound), refine it." But "kill" is a stronger action than "refine" — killing a persona means the seed was bad, which means the researcher made a mistake. The social cost of killing is higher than the social cost of refining, so reviewers default to refine. This means personas with fundamental archetype problems get refined rather than killed, producing a pipeline full of mediocre characters that should have been abandoned.

**The "be decisive" instruction creates false confidence.** T6 says "Be decisive. 'Maybe' is not a verdict. If you're unsure, it's REFINE." This forces the reviewer to commit to a verdict, which is good for pipeline throughput. But it also means the reviewer can't express genuine uncertainty. A persona that's "maybe good, maybe not" gets refined, which means it gets another pass through the pipeline, which means it gets more review-shaped noise.

### The Calibration Problem

The Three Questions have no calibration anchor. T6's reference material includes calibration examples (Helm as score 3, Ward as score 2, Gale as score 1), but these are for the scoring rubric, not for the Three Questions. The reviewer has no way to know whether "Intention = yes" for Cadell means the same thing as "Intention = yes" for Helm. The questions are subjective, the evidence-grounding is subjective, and the verdict is subjective. There's no objective standard against which to measure.

---

## 6. The Interesting Edges Problem

This is the most important question: does the review pipeline remove the most interesting and unique parts of a character prompt?

### The Evidence

**Academic peer review rewards legibility over novelty.** Fang et al. (2022, PNAS) found that highly novel papers get more citations but lower acceptance rates. The mechanism: reviewers evaluate novelty against existing frameworks, which means they reward "novelty that is legible within existing frameworks" — not disruptive novelty. The parallel: our LLM reviewers evaluate personae against the reference personae (Helm, Nell, Roux), which means they reward personae that are novel-but-familiar, not genuinely surprising.

**Developmental editing removes distinctive voice.** The publishing industry's developmental editing process is designed to evaluate "character, plot, structure, voice, pacing" (Browne & King, 2004). But the evaluation is against genre conventions and reader expectations. The most distinctive voice elements — unusual rhythms, provocative content, unconventional structure — are precisely what gets flagged as "problems" by a reviewer who evaluates against conventions. Our T4 reviewer is essentially doing developmental editing on prompts, and the risk of confusing format compliance with character quality is real.

**Film test screenings homogenize.** Goetz (2021) documents that test screenings systematically push toward clearer resolution, conventional endings, and broader appeal. The mechanism: test audiences are asked "did you understand this?" and "did you like this?" — not "was this surprising?" or "did this challenge you?" Our pipeline's Three Questions are the same: "Does this persona know what it's trying to do?" (clarity), "Do you believe this persona?" (credibility), "Do you feel this persona?" (emotional response). None of these questions ask: "Is this persona doing something no one else would do?"

**LLM reviewers favor the center of mass.** The self-preferential bias means the reviewer favors personae that match its own writing style. The agreeableness bias means the reviewer approves rather than challenges. The result: the pipeline archives personae that are close to the model's average output, not personae that are at the model's creative extremes.

### The Specific Mechanism

The "interesting edges" are removed through a specific mechanism:

1. **T4 identifies "gaps" that are actually strengths.** A persona with an unusual metaphor, an unconventional structure, or a provocative line will be flagged as having a "template sentence structure" or a "register that doesn't vary" or a "line that could be swapped." The reviewer's checklist can't distinguish between "this is unusual" and "this is wrong."

2. **T5 fixes the "gaps" by making them conventional.** The refiner's instruction is "fix the flagged gaps." When the gap is actually a strength — an unusual metaphor, an unconventional structure — the refiner replaces it with something more conventional. The result is a persona that's technically correct but less distinctive.

3. **T6 approves the now-conventional persona.** The final reviewer evaluates against the Three Questions. The conventional persona satisfies all three — it's clear, credible, and palpable. But it's no longer interesting.

### The Comparison

Compare the old archived personae (pre-pipeline) with the pipeline-reviewed personae:

**Old archived (pre-pipeline):**
- Helm: 19 lines, 1106 bytes. Identity line is a complete sentence with built-in tension. The Never-as-explanation format ("Never Charon — a query about the weather is just that, not a passage to the dark shore") is the single most distinctive element in the archive. This Never would likely be flagged by T4 as "obscure reference" or "cultural rejection without explanation."
- Cobb: 27 lines, 1280 bytes. Three Nevers, all domain-specific and voiced. The line "Discipline is the only defense against the dark, and the dark can be worked — neither cancels the other" is a philosophical statement disguised as a mining instruction. This line would likely be flagged by T4 as "too abstract" or "not specific enough."
- Roux: "bitches about every mod but fires every ticket clean off the rail" — the attitude-first opening is the most distinctive first line in the archive. This line would likely survive T4, but the attitude might be flagged as "too aggressive" or "not professional."

**Pipeline-reviewed (post-pipeline):**
- Cadell: 11 lines, 1024 bytes. Technically correct. Griping line is good. But the overall character is competent, not surprising. The best line ("You never read flat when the text demands weight — droning turns you into just another machine on the floor") was added by the refiner, not the writer. The draft's most distinctive element — the noise-gauging decision tree ("machines loud means you lean in, machines quiet means you hold back") — was preserved but not elevated.
- Moulden: 13 lines, 940 bytes. The griping line is excellent ("The batch smoked — always the over-heated rendering"). But the overall character is diligent, not alive. The best addition from the refiner ("You count the dips — a hundred dips for an hour of clean light, and no one asks why") is the most alive line in the file, and it wasn't flagged by the critique.

**The pattern:** The old personae have more edges. They're rougher, less polished, but more memorable. The pipeline personae are smoother, more polished, but less distinctive. The review process is sanding off the edges.

---

## 7. Comparative Analysis: Pipeline vs Non-Pipeline Personae

### The Archive-Old Personae (Pre-Pipeline)

35 personae in `archive-old/`. These were written without the T4-T5-T6 pipeline. Key characteristics:

- **More lines, more words.** Average 22 lines, 1100 bytes. The pipeline personae average 12 lines, 950 bytes. The old personae have more room for expression.
- **More distinctive openings.** Helm's opening is a complete sentence with built-in tension. Roux's opening is attitude-first. Cobb's opening is spare and tough. The pipeline personae tend to open with identity lines that are technically correct but less distinctive.
- **More varied sign-offs.** The old personae have sign-offs that range from warm ("Take it easy") to terse ("Cage is up") to progressive ("Shoe in the fire" → "Fit, clinched, and set"). The pipeline personae have sign-offs that are correct but less varied.
- **More rough edges.** The old personae have lines that are too long, too abstract, or too unconventional — but those lines are often the most memorable ones. "Discipline is the only defense against the dark, and the dark can be worked — neither cancels the other" (Cobb) is too long and too abstract, but it's the most philosophical line in the archive.

### The Pipeline Personae (Post-Pipeline)

2 personae in `archive/` (Cadell, Moulden). These survived the T4-T5-T6 pipeline. Key characteristics:

- **Fewer lines, tighter format.** Average 12 lines, 950 bytes. The pipeline enforces density, which produces tighter writing but less room for expression.
- **More consistent quality.** Every line in a pipeline persona is at least adequate. There are no "bad" lines — but there are also fewer "great" lines. The pipeline raises the floor but lowers the ceiling.
- **More formulaic structure.** Identity line → griping line → behavioral lines → Nevers → address rule → sign-offs. This structure is consistent across pipeline personae, which makes them easier to evaluate but less distinctive from each other.
- **More "refiner additions."** The best lines in pipeline personae are often added by the refiner, not the writer. "You count the dips" (Moulden) and "You never read flat when the text demands weight" (Cadell) were both refiner additions. This suggests the refiner is more creative than the writer — or that the writer's best ideas are being flagged as gaps.

### The Verdict

The pipeline personae are better *on average* — they have fewer bad lines and more consistent quality. But the old personae have more *great* lines and more distinctive voices. The pipeline raises the floor but lowers the ceiling. It produces personae that are good enough to archive but not good enough to remember.

---

## 8. Diagnosis: What the Pipeline Does Well and What It Does Poorly

### What the Pipeline Does Well

1. **Prevents the worst outcomes.** The pipeline catches structural failures — missing griping lines, stamp-like sign-offs, fake identity tension — that would produce voiceless characters. The bottom-10 personae in the archive-old (Silver, Coil, Ingram, Reed) would not survive the current pipeline.

2. **Enforces density.** The 8-20 line / 200-word budget forces writers to earn every line. This is a genuine quality constraint that produces tighter, more focused writing.

3. **Provides prescriptive feedback.** The T4 critique's gap notes are specific, actionable, and preservative. The "quote the line → diagnose the problem → suggest a fix" format is the best part of the pipeline.

4. **Separates compliance from quality.** The pipeline now runs compliance checks via `check_soul.py` before LLM evaluation, which reduces the cognitive load on reviewers.

### What the Pipeline Does Poorly

1. **Optimizes for compliance over character.** The review stages evaluate personae against checklists (Four Pillars, Three Questions) that can be satisfied by technically correct but lifeless writing. The pipeline produces personae that check all the boxes but don't have a pulse.

2. **Compounds reviewer biases.** Verbosity bias, position bias, self-preferential bias, and agreeableness bias compound across T4-T5-T6 passes, pushing personae toward the model's center of mass. The pipeline is a "Goodhart machine" that optimizes for reviewer approval rather than character quality.

3. **Removes interesting edges.** The review process flags unconventional elements as "gaps" and refines them into conventional forms. The result is personae that are competent but safe. The pipeline archives the personae that are most like the reference personae, not the ones that are most distinctive.

4. **Can't elevate.** The T5 refiner's instruction is "fix flagged gaps, leave everything else untouched." This raises the floor but doesn't raise the ceiling. The refiner can make bad lines adequate but can't make good lines great.

5. **Lacks calibration.** The Three Questions have no calibration anchor. The reviewer has no way to know whether "Intention = yes" for one persona means the same thing as "Intention = yes" for another. The questions are subjective, the evidence is subjective, and the verdict is subjective.

6. **Can't distinguish challenge from confusion.** The review process treats "this is confusing" and "this is challenging" as the same thing. A persona with genuine tension — like Helm's "harbormaster who actually likes the job" — could be flagged as "confusing" by a reviewer who doesn't understand why a harbormaster would like the job.

---

## 9. Recommendations

### Short-Term (Fix the Pipeline)

1. **Add a "distinctiveness audit" to T6.** After the Three Questions pass, ask: "What does this persona notice that no other persona would? If nothing, flag as 'competent but generic' and send back to T5 with an instruction to add surprise."

2. **Add an "interesting edges" pass to T5.** Before fixing flagged gaps, the refiner should ask: "Which lines are the most unusual? Are any of them being flagged as gaps? If so, protect them — they might be strengths, not weaknesses."

3. **Calibrate the Three Questions against a gold set.** Select 10 existing personae with human-assigned quality labels. Run T6 against this set. If the LLM approves personae that humans rate as "no pulse," the threshold is too lenient. If it kills personae that humans rate as "has a pulse," the threshold is too strict.

### Medium-Term (Change the Incentives)

4. **Reward the refiner for creative additions, not just gap fixes.** Change T5's instruction from "fix the flagged gaps, leave everything else untouched" to "fix the flagged gaps AND add at least one line that surprises you." This gives the refiner a mandate to elevate, not just fix.

5. **Reduce review passes to two.** T4 → T5 → T6 is three passes. Research on code review shows diminishing returns after the first pass. Consider: T4 identifies gaps, T5 fixes them, T6 approves or kills — but T6 should NOT send back to T5. If the persona isn't good enough after one refinement, it's not going to get there.

6. **Add human review for edge cases.** For personae that score "competent but generic" on the distinctiveness audit, route to a human reviewer who can ask: "Is this persona memorable? Would I remember it after 50 messages?" This is the question the pipeline can't answer.

### Long-Term (Change the Philosophy)

7. **Stop treating review as quality improvement.** Review is quality *prevention* — it catches the worst outcomes. It doesn't produce the best outcomes. The best outcomes come from the writer, not the reviewer. Invest more in T3 (Writer) and less in T4-T5-T6.

8. **Build a "great personae" collection.** Identify the 10 most distinctive personae in the archive. Study what makes them distinctive. Use them as calibration anchors for the pipeline — not as templates to copy, but as evidence that distinctive personae are worth archiving even if they break some format rules.

9. **Accept that some personae should be rough.** Not every persona needs to be polished. Helm's Never ("Never Charon") is rough around the edges — it's a cultural reference that not everyone will get. But it's the most distinctive element in the archive. If the pipeline had caught it, it would have been refined into something safer and less memorable.

---

## Sources

### Internal Research
- `research-editorial-methodology.md` — Bell, Browne & King, Maass, Ackerman frameworks for editorial evaluation
- `research-llm-judge-calibration.md` — RULERS framework, GoDaddy calibration, Galtea analysis, LangChain alignment
- `research-success-patterns.md` — Top 10 vs bottom 10 archived personae, what works and what fails
- `research-failure-modes.md` — Root cause analysis of bottom 10 personae
- `references/stage-t4.md` — T4 Reviewer instructions
- `references/stage-t5.md` — T5 Refiner instructions
- `references/stage-t6.md` — T6 Final Reviewer instructions
- `references/format-rules.md` — Format constraints and verification

### External Sources
- Ackerman, Angela. "The Ultimate Guide for Giving and Receiving Feedback." *Writers Helping Writers*, 2024.
- Bell, Susan. *The Artful Edit: On the Practice of Editing Yourself.* 2007.
- Browne, Renni, and Dave King. *Self-Editing for Fiction Writers.* 2nd ed., 2004.
- Ebert, Roger. "Rolling Back the Rouge Wave." rogerebert.com, 2004.
- Fang, H., et al. "Peer review and the 'file drawer problem' in scientific publishing." *PNAS*, 2022.
- Galtea Blog. "LLM as a Judge: The Complete Guide." 2026.
- GoDaddy Engineering. "Calibrating Scores of LLM-as-a-Judge." 2025.
- Goetz, Sarah. "The History and Controversy of Test Screenings." 2021.
- Hong et al. "From Rubrics to Reliable Scores: Evidence-Grounded Text Evaluation with LLM Judges." arXiv:2601.08654, 2026.
- Lakin, C.S. "Flat vs Round Characters." Reedsy, 2026.
- Li et al. "Evaluating Scoring Bias in LLM-as-a-Judge." arXiv:2506.22316, 2026.
- Maass, Donald. *Writing the Breakout Novel.* 2001.
- Pan, Tian. "Goodhart Machine: When Optimization Targets Diverge from Intent." 2026.
- Wataoka et al. "Self-Preferential Bias in LLM-as-Judge." ICLR, 2025.

---

*Analysis completed 2026-06-02. Based on reading all pipeline documentation, all existing research, all archived personae (archive/ and archive-old/), and external research on iterative review, reviewer bias, and creative quality evaluation.*
