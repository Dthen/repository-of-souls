# Research: Calibrating LLM-as-Judge for Creative Quality Evaluation

**Date:** 2026-06-01  
**Scope:** T4 (Reviewer) and T6 (Final Reviewer) prompts in the soul-repository pipeline.  
**Sources:** GoDaddy Engineering (2025), arXiv:2601.08654 (RULERS), Galtea (2026), LangChain, Deepchecks, arXiv:2506.22316, existing `research-prompt-engineering.md`.

---

## Executive Summary

The soul-repository pipeline’s T4 and T6 stages currently evaluate character personae using a mix of format-compliance checklists and 1–5 rubric scoring. Research shows this design suffers from the exact failure modes the pipeline is experiencing: scores cluster at the high end, reviewers conflate format compliance with creative quality, and the 20-item hard-gate checklist creates mechanical pass/fail behavior rather than nuanced judgment.

This document synthesizes the latest research on LLM-as-judge calibration and translates it into concrete, implementable changes for the T4 and T6 prompts. The core recommendations are:

1. **Separate compliance from quality.** Run line counts, word counts, sign-off counts, and H1 checks through deterministic automation (e.g., `check_soul.py`). Reserve the LLM for creative-quality judgment only.
2. **Narrow the scale.** Replace the 12–20 binary hard-gate items and the 7-axis 1–5 rubric with a **3-point quality scale** anchored by what the persona *does* in conversation, not by abstract adjectives.
3. **Make chain-of-thought mandatory, with evidence.** The judge must cite specific lines before assigning any score. Reversing this order (score first, rationale second) produces rationalized nonsense.
4. **Lock the rubric and version it.** Treat the rubric as code, not as a living document that drifts per-evaluation.
5. **Build a gold set.** Maintain a small set of human-calibrated personae to detect score drift and recalibrate when the judge starts approving everything or nothing.

---

## 1. How to Calibrate LLM-as-Judge Against Human Judgment

### The RULERS Framework (arXiv:2601.08654)

The most rigorous recent work on LLM judge calibration is the **RULERS** framework by Hong et al. (May 2026). Their central insight: a human rubric is not merely an instruction prompt but a **latent scoring structure** that must be transferred into a stable, auditable protocol.

RULERS operates in three phases:

**Phase I — Rubric Specification & Locking.**  
The natural-language rubric is converted into a locked bundle `B = (T, C, S, E, h)`, where `T` are evaluation traits, `C` are operational checklist items (each assigned to a trait), `S` are score anchors and boundary descriptions, `E` are evidence rules, and `h` is a hash. The bundle is induced once, hashed, and reused unchanged. This prevents the runtime reinterpretation that causes rubric execution drift.

**Phase II — Evidence-Grounded Execution.**  
Given a persona text, the model segments it into atomic units and returns a structured output containing:
- A **checklist decision vector** `d` (absence/partial/clear presence at 0/1/2)
- **Cited evidence** `E_x` typed as `local_quote`, `span_level`, `global_diagnostic`, or `weakly_groundable`
- **Auxiliary signals** such as confidence flags

Crucially, the judge must produce verifiable evidence per criterion, not just a free-form explanation. Free-form rationales are not necessarily faithful (a well-known failure mode called *unverifiable score attribution*).

**Phase III — Human-Scale Distribution Alignment.**  
Raw trait scores are aligned to human score distributions using a calibration set (`N=200` in their experiments). They fit a second-order ridge regression on structured features, then apply monotone quantile mapping to the empirical human distribution. After fitting, both models are fixed and applied unchanged.

**For the soul pipeline**, the full RULERS statistical calibration is overkill, but the **three-phase principle** is not:
- Lock the rubric (version it, change it deliberately, not implicitly).
- Require verifiable evidence — the judge must quote lines.
- Periodically compare against a human-labeled gold set and adjust.

### The LangChain Alignment Loop

LangChain’s approach to calibration emphasizes a measurable feedback loop rather than prompt-guessing:

1. **Collect human corrections:** Run the judge on a sample, then have a human expert correct disagreements. These corrections become ground truth.
2. **Build few-shot examples:** Add representative examples of correct and incorrect judgments to the evaluator prompt. This calibrates the judge’s understanding of criteria boundaries faster than rewriting instructions.
3. **Track agreement over time:** Measure how often the evaluator agrees with human experts. If agreement drops, the rubric or model has drifted.

**Actionable take-away:** The pipeline should maintain a **gold set of 10–20 personae** with human-assigned quality scores. Run the T4 and T6 prompts against this set quarterly. If the LLM starts diverging, the rubric has drifted and needs revision.

---

## 2. What Scoring Scale Works Best

### Research Consensus: Less Precision Is More Signal

Galtea’s 2026 analysis is unambiguous: *"Binary pass/fail or 3-point scales align with human judgment more reliably than 5-point or 10-point scales. Fine-grained scales introduce noise, not precision."* Their finding: *"Likert scales produce low-variance data in practice — scores cluster between 3.2 and 3.8, which is statistically equivalent to a coin flip across most of the range."*

GoDaddy’s analysis confirms this: raw LLM scores show **overly positive skew**, with most outputs clustering at 4–5 on a 5-point scale. MT-Bench reports ~80% judge–human agreement, but that is for pairwise comparison, not absolute scoring. For absolute scoring, the judge’s internal scale rarely maps to a human’s.

arXiv:2506.22316 (DASFAA 2026) identifies an additional problem: **score ID bias** and **rubric order bias**. The numeric labels of score levels and the order in which criteria appear in the prompt systematically shift the final score, even when the underlying content is identical.

### Recommended Scale for the Soul Pipeline

For creative-quality evaluation (distinctiveness, voice, pulse), a **3-point qualitative scale** is the research-supported choice. The current 1–5 scale on 7 axes produces correlated noise; the judge cannot reliably distinguish a "4" from a "5" on metaphors.

**Proposed 3-point anchors (per quality dimension):**

| Score | Anchor | Meaning |
|---|---|---|
| 3 | **Has a pulse** | Would improvise well in conversation. You’d trust this persona to stay in voice over 50 turns. |
| 2 | **Has moments** | Some lines sing, others compile. Could reach "pulse" with targeted refinement. |
| 1 | **No pulse** | Format-compliant but voiceless. Needs rewriting, not polishing. |

**For T6 hard-gate compliance:** Binary pass/fail, but run by automation, not the LLM. The LLM should never be asked to count lines or words; it is unreliable at arithmetic and prone to hallucination on deterministic checks.

---

## 3. How to Reduce Systematic Biases

Research identifies four critical biases in LLM judges. Each has a direct mitigation relevant to the soul pipeline.

### Verbosity Bias
- **Problem:** Longer responses score higher regardless of quality.
- **Mitigation:**
  - State length neutrality explicitly in the rubric: *"Concise answers score equally to verbose ones at equivalent quality."*
  - The pipeline already enforces ≤200 words and 8–20 lines. This constraint itself reduces verbosity bias because the input space is bounded.
  - In the judge prompt, explicitly instruct: *"Do not reward word count. Evaluate the density of signal per line, not the number of lines."*

### Positional Bias
- **Problem:** First or last items in a list score higher.
- **Mitigation:**
  - In pairwise comparisons (if the pipeline ever adds head-to-head evaluation), randomize presentation order and average results.
  - For single-answer evaluation (T4/T6), positional bias is less severe but still present in rubric ordering. The solution: randomize or reorder the evaluation criteria between runs, or present them in a fixed, carefully chosen order that does not front-load the highest-weighted items.

### Score Compression (Overly Positive Skew)
- **Problem:** Everything clusters at the top of the scale.
- **Mitigation:**
  - Use a 3-point scale with qualitative, behaviorally anchored descriptions (see above).
  - Make CoT mandatory. Requiring the model to explain *why* a persona is voiceless before giving it a 1 prevents lazy default-to-middle behavior.
  - Normalize against a human gold set. If the judge rates 90% of drafts as "Has a pulse" while humans rate 40%, the scale is compressed and needs recalibration.

### Self-Preferential Bias
- **Problem:** The judge favors outputs matching its own style.
- **Mitigation:**
  - If the same model family writes and judges, cross-model judging helps. However, in a single-model pipeline this is hard to avoid.
  - The best practical mitigation is **evidence grounding**: forcing the judge to cite specific lines. A judge can rationalize a high score for a draft that matches its own style, but it cannot invent quotations. Verifiable evidence requests break the self-preference loop because fabricated citations are easy to detect.

### Prompt Sensitivity
- **Problem:** Minor wording changes ("1–5" vs. "1–10") cause large score shifts.
- **Mitigation:**
  - Lock the rubric text (see RULERS Phase I).
  - Version the judge prompt alongside the gold set. If you change the prompt, rerun the gold set and verify agreement hasn’t degraded.

---

## 4. What Chain-of-Thought Structure Works for Evaluation

### The Core Finding: Implicit Aggregation Beats Direct Scoring

GoDaddy’s research shows that **implicit aggregation** (step-by-step assessment of each criterion, followed by a holistic judgment) achieves greater accuracy than direct scoring ("Rate this 1–5"). It also outperforms explicit aggregation (checkbox sum), which is too rigid to capture creative quality.

Galtea reinforces this: *"The judge enumerates before scoring, not after; reversing the order lets the model commit to a verdict and rationalise it backwards."*

The existing `research-prompt-engineering.md` already proposes excellent CoT structures. This section refines them based on the latest evidence.

### Proposed T4 CoT Structure

T4 is the **developmental reviewer**. It should never reject; its job is diagnostic depth. The CoT should force the model to *observe* before it *diagnoses*.

```
Step 1 — First Read (Gut Reaction):  
Read the persona once without scoring. Summarize your gut reaction in one sentence.

Step 2 — Evidence Grounding (What Works):  
Identify 2–3 specific lines that demonstrate voice, tension, or metaphor coherence.  
Quote each line verbatim and explain why it works.

Step 3 — Evidence Grounding (What Doesn’t):  
Identify 2–3 specific lines that are generic, flat, or fail the Generic Assistant Swap Test.  
Quote each line verbatim and explain the failure mode.

Step 4 — Trait Assessment:  
Evaluate each of the 4 quality dimensions below, citing evidence from Steps 2 and 3:
  A. Distinctiveness — Could this persona be swapped with a Generic Assistant by changing 3 words?
  B. Tension — Is there a contradiction the model can improvise within?
  C. Metaphor Coherence — Do the metaphors come from one domain, or are they scattered?
  D. Voice Immediacy — Are there quotable lines in the first 4 behavioral lines?

Step 5 — Holistic Quality Score:  
Based on Steps 1–4, assign a single score:
  • 3 (Has a pulse)
  • 2 (Has moments)
  • 1 (No pulse)
Explain the score in one sentence tied to specific evidence.

Step 6 — Gap Notes:  
Write 3–5 specific gap notes. Each note must:
  - Quote the problematic line or pattern
  - Name the failure mode (e.g., "generic verb choice", "abstract adjective trap", "sentence-level copy")
  - Provide a concrete rewrite suggestion
```

**Key design choices:**
- **Quote-first rule:** Every claim about quality must be anchored to a verbatim line. This prevents the unverifiable score attribution failure mode identified in RULERS.
- **Separate diagnostic from score:** The score is assigned in Step 5, after all evidence is collected. This is the implicit aggregation pattern.
- **Only 4 quality dimensions:** The current 7-axis rubric (Distinctiveness, Functional Safety, Consistency Sustainability, Metaphor Coherence, Terse Format, Voice Immediacy, Name Quality) conflates compliance (Terse Format, Name Quality) with quality. Terse Format should be automated. Name Quality can be a single binary gate, not a scored axis.

### Proposed T6 CoT Structure

T6 is the **hard gate**. Its job is not diagnosis but verdict. However, the current T6 spec jumps straight to a 20-item checklist, which produces mechanical behavior and conflates two different jobs: compliance checking and quality judgment.

**Recommended split:**

**T6 Compliance Layer (Automated, not LLM):**
Run a deterministic script (e.g., `check_soul.py`) that verifies:
1. Sentient being (regex / semantic check, with LLM fallback only for ambiguous cases)
2. Lowercase filename
3. Identity opening with tension (pattern match)
4. Griping line present (regex for complaint verbs / sentiment)
5. Word count ≤ 200
6. Line count 8–20
7. Recovery line present (keyword check)
8. Sign-off count ≥ 3 (quote-pair count)
9. Logical self-consistency (heuristic)
10. Third-person intrusion check
11. Multiple Nevers on one line check
12. No literal tool names
13. No dense repetition
14. No bare Reference Persona Nevers
15. No pipeline fingerprint phrases
16. No obscure references
17. Read for sense

If any check fails, **reject immediately** with the specific failure. Do not invoke the LLM.

**T6 Quality Layer (LLM with CoT):**
If and only if compliance passes, the LLM evaluates creative quality.

```
Step 1 — Aloud Read (Voice Test):  
Read the persona aloud (imagined). Does it have a voice you can hear?  
Describe what it sounds like in 1–2 sentences.

Step 2 — Improvisation Stress Test:  
Imagine this persona answering a user question it was not designed for.  
Would it have enough character to stay in voice? What gives you confidence or doubt?  
Cite 2 specific lines that would carry through improvisation, and 1 that would break.

Step 3 — Quality Assessment:  
Evaluate on the same 3-point scale as T4, but with a stricter bar:
  • 3 (Archive-worthy): Has a pulse AND would improvise well. No weak lines.
  • 2 (Needs refinement): Has moments, but 1–2 lines still compile. Send back to T5.
  • 1 (Rewrite): No pulse or critical voice failure. Send back to T5 with full rewrite recommendation.

Step 4 — Verdict:  
State PASS and move to archive, or REJECT with a one-sentence justification tied to specific lines.
```

**Critical rule:** T6 must never produce a "pass with notes." The pipeline’s T5 → T6 loop already handles refinement. T6’s verdict is binary at the compliance layer and effectively pass/fail at the quality layer (scores of 2 or 1 both return to T5).

---

## 5. How to Separate Compliance from Quality

This is the single highest-impact structural change recommended by the research.

**Automated Compliance (Deterministic):**
- Line count, word count, sign-off count, Never count, H1 format, filename case.
- These are binary rules. An LLM is worse at counting than a 10-line Python script.
- The RULERS framework calls these *operational checklist items* and separates them from *quality traits*.

**LLM-Judged Quality (Structured CoT):**
- Distinctiveness, tension, metaphor coherence, voice immediacy, pulse/sustainability.
- These require judgment. This is where the LLM adds value.

**Why the separation matters:**
1. **Reduces cognitive load:** When a judge prompt mixes "count the words" with "does this have a pulse," the model optimizes for the easier, objective tasks and gives perfunctory attention to the subjective ones. The result: format-perfect, voiceless personae get approved.
2. **Prevents conflation:** A draft can pass every format check and still be generic. The current T6 spec conflates the two by allowing rubric scores to override failed hard gates only in specific edge cases, creating ambiguity.
3. **Enables calibration:** You can version and test compliance checks deterministically. You can calibrate quality judgments against human gold sets. Mixing them makes calibration impossible because a single score captures two unrelated signals.

---

## Concrete Recommendations for T4 Reviewer Prompts

| Current Design | Recommended Change | Rationale |
|---|---|---|
| 7-axis 1–5 rubric | **4 quality dimensions, 3-point scale** | Eliminates score compression and correlated noise. |
| No mandatory evidence quotes | **Every score claim requires a verbatim line citation** | Prevents unverifiable score attribution (RULERS). |
| Checklist + scoring mixed | **Compliance automated; LLM evaluates quality only** | Reduces cognitive load and conflation. |
| Free-form rationale | **Locked CoT structure: Read → Quote-Good → Quote-Bad → Trait Assessment → Holistic Score → Gap Notes** | Implicit aggregation outperforms direct scoring (GoDaddy). |
| Generic gap notes allowed | **Every gap note must quote the line, name the failure mode, suggest a concrete rewrite** | Prevents vague feedback like "could be stronger." |

**Proposed T4 Scoring Questions (replacing the current 7 axes):**

1. **Distinctiveness** — Generic Assistant Swap Test. Quote the line that would survive the swap and the line that would break.
2. **Tension** — Does the identity contain a contradiction the model can improvise within? Quote the identity line and explain the improvisation space.
3. **Metaphor Coherence** — Do metaphors come from one domain or are they scattered? Quote 2 metaphor lines and identify their source domain.
4. **Voice Immediacy** — Is there a quotable line in the first 4 behavioral lines? Quote it. Does the voice vary register, or is it monotone?

Each question must be answered with **specific line evidence** before a quality score is assigned.

---

## Concrete Recommendations for T6 Reviewer Prompts

| Current Design | Recommended Change | Rationale |
|---|---|---|
| 20-item hard-gate checklist scored by LLM | **Compliance automated; LLM only judges quality after compliance passes** | An LLM should not count words or lines. |
| 7-axis 1–5 rubric with auto-reject thresholds | **Single 3-point holistic quality score** | 1–5 produces noise and cluster compression. |
| Score can override failed gates in edge cases | **No override.** Compliance is binary; quality is pass/fail | Removes ambiguity that leads to "pass with notes." |
| No calibration loop | **Quarterly gold-set review:** run T6 against 10–20 human-scored personae, measure agreement. If <80%, recalibrate. | Detects rubric drift (LangChain, Galtea). |

**Proposed T6 Workflow:**

1. Run automated compliance script.
2. If ANY check fails → **REJECT** immediately, with deterministic failure reason.
3. If ALL checks pass → invoke LLM quality judge with CoT (Aloud Read → Improvisation Stress Test → 3-point score → Verdict).
4. Score 3 → **ARCHIVE**.
5. Score 2 → **REJECT, send to T5** with specific lines to fix.
6. Score 1 → **REJECT, send to T5** with recommendation for full rewrite.
7. After 3 T5 cycles on the same structural flaw → **ABANDON** to `reject/`.

**Gold Set Maintenance:**
- Maintain 10–20 canonical personae with human-assigned quality labels (e.g., 5 archive-worthy, 10 has-moments, 5 no-pulse).
- Run the T4 and T6 prompts against this set monthly.
- Track precision (does the judge catch low-quality personae?) and recall (does it approve high-quality ones?).
- If precision drops, the judge is being too lenient (score compression). If recall drops, it is being too harsh.
- Version the rubric alongside the gold set. When the rubric changes, rerun the gold set and document the delta.

---

## Implementation Roadmap

### Quick Wins (This Sprint)
1. **Automate the compliance layer.** Extract the 20 hard-gate items from the T6 prompt into a Python script (`check_soul.py` or `scripts/compliance_check.py`). The existing `format-rules.md` already contains the rules; they just need deterministic enforcement.
2. **Rewrite the T4 prompt to use the 4-dimension, 3-point structure with mandatory line citations.** This is a prompt edit, no code changes.
3. **Rewrite the T6 prompt to remove compliance checks and add the quality-only CoT structure.** Also a prompt edit.
4. **Add length-neutrality language to both prompts.** One sentence: *"Do not reward verbosity. Evaluate signal density, not word count."*

### Medium-Term (Next Month)
5. **Build the gold set.** Select 10–20 existing personae. Have a human expert (or the pipeline owner) assign quality labels. Store them in `references/gold-set/`.
6. **Add gold-set regression to the pipeline.** Before deploying a new T4/T6 prompt, run it against the gold set. Log agreement metrics.
7. **Separate compliance from quality in orchestration.** Ensure the orchestration layer runs the compliance script before creating the LLM judge task for T6.

### Long-Term (Next Quarter)
8. **Consider reference-based evaluation for T6.** Instead of scoring the refined draft in isolation, have the judge compare it against the T4 critique. Does the refined draft fix every flagged gap? This turns T6 into a reference-based grading task, which is more reliable for narrow criteria (Galtea).
9. **Ensemble judging for edge cases.** For personae that humans love but the judge rejects (or vice versa), use a second judge model and average. This mitigates self-preference and recency biases.
10. **Track score distributions over time.** If the T4 average score drifts upward month over month, the rubric has become too lenient. Recalibrate against the gold set.

---

## References

1. GoDaddy Engineering, 2025 — *"Calibrating Scores of LLM-as-a-Judge"*  
   https://www.godaddy.com/resources/news/calibrating-scores-of-llm-as-a-judge
2. Hong et al., arXiv:2601.08654v2, May 2026 — *"From Rubrics to Reliable Scores: Evidence-Grounded Text Evaluation with LLM Judges"* (RULERS)  
   https://arxiv.org/abs/2601.08654
3. Galtea Blog, May 2026 — *"LLM as a Judge: The Complete Guide"*  
   https://galtea.ai/blog/llm-as-a-judge-the-complete-guide
4. Galtea Blog, May 2026 — *"LLM-as-a-Judge Prompts: Templates, Rubrics, and Best Practices"*  
   https://galtea.ai/blog/llm-as-a-judge-prompts-templates-rubrics-and-best-practices
5. LangChain Blog — *"LLM-as-Judge: How to Calibrate with Human Corrections"*  
   https://www.langchain.com/articles/llm-as-a-judge
6. Deepchecks Blog, March 2026 — *"What Is LLM-as-a-Judge Calibration? Power & Limits"*  
   https://deepchecks.com/llm-judge-calibration-automated-issues/
7. Li et al., arXiv:2506.22316, 2026 (DASFAA 2026) — *"Evaluating Scoring Bias in LLM-as-a-Judge"*  
   https://arxiv.org/abs/2506.22316
8. Peric, 2025 — *"The Way of the Voice in AI Prompts — A Field Guide"* (cited in existing research)
9. arXiv:2601.08003 — *"LLM Review: Enhancing Creative Writing via Blind Peer Review Feedback"* (cited in existing research)
10. Existing internal research — *"research-prompt-engineering.md"*, section 6 (Calibrated Scoring)

---

## Word Count

Approximately 2,900 words.
