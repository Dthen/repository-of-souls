# Research: Pipeline Architecture v2

**Task:** t_314b2dcf  
**Researcher:** Researcher profile  
**Date:** 2026-06-02  
**Status:** DRAFT

---

## Executive Summary

This report evaluates the 7-stage linear pipeline (T0–T6) used for creative persona generation at Soul Factory against the research literature on LLM pipeline architectures, multi-agent systems for creative work, LLM self-critique, and computational creativity. The central question: **is a multi-pass, multi-agent pipeline the right architecture for getting good creative output from LLMs?**

**Core finding: The linear pipeline architecture has critical theoretical and empirical problems.** The 7-stage pipeline introduces compounding self-bias, diminishing returns from sequential refinement, evaluation circularity, and — most damningly — **the literature suggests that for creative generation, a generate-and-select architecture with strong external evaluators outperforms iterative refinement pipelines by a wide margin.** The evidence from the 2025 "When Agents Disagree" paper, the ICLR 2025 Multi-Agent Debate analysis, and the ACL 2024 "Pride and Prejudice" paper collectively paint a clear picture: multi-stage linear refinement pipelines are the _wrong architecture_ for creative output.

**Recommendation:** Replace the linear refinement pipeline with a **generate-and-select architecture**: generate N candidate outputs in parallel (with diverse configurations), then use a trained or well-prompted external evaluator (not the same model) to select the best. Optionally, follow with a single, tightly-scoped refinement pass guided by the evaluator's specific verdict. This matches what the best image generation, music generation, and code generation pipelines already do.

---

## 1. The Existing Pipeline

The current Soul Factory pipeline has seven stages in strict linear order:

```
T0 (Researcher) → T1 (Viability Screener) → T2 (Namer)
→ T3 (Writer) → T4 (Reviewer) → T5 (Refiner) → T6 (Final Reviewer)
```

Each stage is a distinct task dispatched to a specialized agent profile. The pipeline operates sequentially: T0 produces seeds, T1 screens them, T2 names a persona, T3 writes the full persona document, T4 critiques it, T5 refines based on the critique, T6 does a final check.

This is a classic **prompt chaining** pattern (in Anthropic's terminology) applied to creative generation. The pipeline has the following properties:
- **Sequential**: each stage depends on the previous
- **Specialized**: each stage has a dedicated agent profile
- **Refinement-heavy**: T4, T5, and T6 exist purely to evaluate and refine
- **Reviewer as self-model**: T4 and T6 are LLMs evaluating other LLMs' output

---

## 2. What the Research Says About LLM Pipeline Architectures

### 2.1 The Three Major Pipeline Paradigms

The EMNLP 2025 survey on creativity in LLM-based MAS (Lin et al., 2025) identifies three fundamental generation techniques:

| Technique | Description | What Soul Factory Does |
|-----------|-------------|----------------------|
| **Divergent Exploration** | Generate a wide range of diverse outputs before filtering | Partially at T0-T2 |
| **Iterative Refinement** | Progressive enhancement through repeated feedback/revision loops | T3→T4→T5→T6 (the core of the pipeline) |
| **Collaborative Synthesis** | Integrate diverse agent perspectives into a coherent output | Not used |

**Critical insight**: iterative refinement is the _least_ well-supported technique for creative work among these three. The survey notes that divergent exploration produces the most novel results, while iterative refinement tends toward convergence on safe, predictable outputs — the opposite of what creative generation needs.

### 2.2 The Selection Bottleneck — Why Multi-Pass Fails

The most directly relevant paper is **"When Agents Disagree: The Selection Bottleneck in Multi-Agent LLM Pipelines" (arXiv:2603.20324, 2025)**. This paper's core finding is devastating for refinement-heavy pipelines:

- **Judge-based selection** outperforms synthesis-style multi-agent pipelines **with win rate 0.810 vs 0.179** across 42 tasks.
- **Synthesis loses to a single-model baseline in ALL 42 tasks.**
- **Selector quality is a more impactful design lever than generator diversity.**

The paper formalizes the **selection bottleneck** with a crossover threshold: a diverse team's high-variance candidate pool is an asset **only if** the selector is good enough. Below the threshold, diversity hurts. Above it, diversity helps. The key equation:

```
s* = (μ_best - M(T_d)) / (O(T_d) - M(T_d))
```

Where diversity helps iff **s > s*** (selector quality is above the crossover threshold).

**Implication for Soul Factory**: The T4 Reviewer and T6 Final Reviewer are acting as selectors, but they evaluate a _single_ candidate, not a diverse pool. This is the worst of both worlds — they're making a judgment on one sample, with no diversity to exploit, and the self-bias problem (see 2.3) means the judgment is unreliable.

### 2.3 Self-Bias in Self-Refinement — The "Pride and Prejudice" Effect

**"Pride and Prejudice: LLM Amplifies Self-Bias in Self-Refinement" (Xu et al., ACL 2024)** directly studies what happens when LLMs evaluate and refine their own output. Key findings:

- **Self-bias is prevalent in ALL examined LLMs**: GPT-4, GPT-3.5, Gemini, LLaMA2, Mixtral, DeepSeek — all show a systematic tendency to favor their own generations.
- **Self-refinement amplifies self-bias**: The refine pipeline improves fluency and understandability but makes the model _more_ biased toward its own output.
- **Mitigation requires external feedback**: Larger model size and external (human or independent model) feedback significantly reduce bias.

**Implication for Soul Factory**: The T4 (Reviewer) and T6 (Final Reviewer) stages are LLMs evaluating output generated by other LLMs. However, if the same model family is used across stages, self-bias still applies because the models share training data and evaluation tendencies. The pipeline's sequential refinement (T4→T5→T6) **compounds self-bias** — each round makes the output more fluent but also more homogenized.

### 2.4 Multi-Agent Debate Fails to Outperform Simpler Baselines

The **ICLR 2025 study on Multi-Agent Debate (MAD)** evaluated 5 MAD frameworks across 9 benchmarks. The finding is stark:

- **"Current MAD frameworks fail to consistently outperform simple single-agent test-time computation strategies"** such as Chain-of-Thought or Self-Consistency.
- No MAD framework consistently beat CoT or Self-Consistency despite using _more_ computation.
- Multi-Persona (forced role-playing like "angel" vs "devil") performed worst — the forced opposition caused incorrect answers to prevail.
- Increasing rounds or number of agents showed **no consistent accuracy improvement**.

**Implication**: Multi-agent debate and multi-pass critique loops are not empirically validated for improving output quality. They add latency and cost without reliable benefit. This directly undermines the T4→T5 review→refine cycle.

---

## 3. Does Multi-Pass Improve Creative Quality? The Evidence

### 3.1 The Case FOR Iterative Refinement

The MAS survey (Lin et al., 2025) cites positive results for some iterative refinement systems:

- **HoLLMwood** (Chen et al., 2024): Writer, Editor, Actor agents for screenwriting; achieves convergence on coherent scripts.
- **DesignGPT** (Ding et al., 2023): Higher completeness, novelty, practicality than one-shot.
- **Baby-AIGS-MLer** (Liu, 2024): ML research pipeline with ideation → coding → testing.

However, these systems succeed because:
1. They have **objective or near-objective evaluation criteria** (code compiles, tests pass, design specs met).
2. They use **genuinely diverse models**, not the same model family in different roles.
3. The refinement loops are **tightly scoped** to fix specific issues, not open-ended "improve this."

### 3.2 The Case AGAINST Iterative Refinement for Creativity

The **LitBench paper (Fein et al., 2025)** on evaluating creative writing found:

- Best zero-shot LLM judge (Claude-3.7-Sonnet) achieves only **73% agreement** with human preferences.
- Chain-of-thought reasoning **degrades** evaluator accuracy for creative writing (72% vs 78% without CoT).
- **Stylistic choices account for judgments more than substance** (Feuer et al., 2025).

The **Measuring LLM Novelty paper (Padmakumar et al., 2025)** found:

- Inference-time methods (prompting, novel in-context examples) have **smaller effect** on novelty than model scale or architecture.
- They often increase **originality at the expense of quality**, keeping novelty flat.
- **Model selection matters more than prompting** for creative output.

The **CreativityPrism framework (Hou et al., 2025)** evaluated 17 state-of-the-art LLMs across 8 tasks and found:

- **High performance in one dimension rarely generalizes** — novelty often shows weak or negative correlation with quality/diversity.
- Proprietary models lead in creative writing and logical reasoning by ~15%, but **open-source models are comparable in divergent thinking**.
- This means pipeline architecture matters less than model choice for certain creative dimensions.

### 3.3 The Torrance Tests — What They Reveal

The **Springer study on assessing LLM creativity via adapted Torrance Tests (Zhao et al., 2025)** evaluated LLMs across 7 tasks using 4 criteria: fluency, flexibility, originality, elaboration.

Key findings:
- **LLMs excel at elaboration** (detail and development) — this is their strength.
- **LLMs are weakest at originality** — the fundamental bottleneck.
- **Role-play settings significantly influence creativity** — persona assignment works.
- **Multi-LLM collaboration enhances originality** — this IS a positive signal for multi-agent approaches.
- **Prompt engineering has strong effects** — better prompts can partially compensate for model weaknesses.

**Implication**: The original T2 Namer and T3 Writer stages that assign persona and write in voice are actually well-founded. The problem is the refinement-after-the-fact stages (T4, T5, T6) that then sand down whatever originality was achieved.

---

## 4. The "Flatness" Problem — Root Cause Analysis

The "flatness" problem (creative output that feels safe, predictable, lacking in surprise) has been discussed among practitioners. The research points to **multiple interacting causes**:

### 4.1 Model Capability: The Primary Cause

The strongest evidence from Padmakumar et al. (2025): **model-generated text can be less novel than human-written text from the internet, even at scale.** Increasing model scale and post-training (RLHF) improves novelty primarily through _quality_ improvements, not through _originality_ gains. The fundamental training objective (predict the next token from a corpus of existing human text) naturally biases toward the statistically likely — which is the opposite of creative surprise.

This is the **"mode coverage" problem**: LLMs learn a probability distribution over text. Creative outputs are in the tails of this distribution. Multi-pass refinement pushes outputs back toward the mode (the "safe" center of the distribution) because that's where the model's own evaluation prefers to be.

### 4.2 Pipeline Architecture: An Amplifier

The pipeline doesn't cause flatness, but it **amplifies** it. Here's how:

- T4 Reviewer evaluates the T3 Writer's output. If the reviewer and writer use similar models (same training data, similar RLHF), the reviewer will naturally prefer fluent, well-structured text that stays within familiar patterns — i.e., "flat" text.
- T5 Refiner then shifts the output toward what the reviewer rated highly.
- T6 Final Reviewer then does this again.
- Result: **three passes of regression toward the mean** of the model's probability distribution.

Compare this to **generate-and-select** where 5-10 diverse outputs are generated in parallel and the single best one is selected: the best one is in the tail of the distribution; the selection doesn't push it back toward the center.

### 4.3 Prompt Engineering: A Modest Amplifier

Padmakumar et al. (2025) found that inference-time methods (prompting, ICL) have only a "smaller effect" on novelty — they "often increase originality at the expense of quality." The prompts could be better, but this is a smaller lever than model choice or architecture.

### 4.4 Review Criteria: A Significant Factor

This is the most **actionable** finding. The evaluation criteria used by T4 and T6 directly shape what T5 produces. If the rubric rewards "well-structured," "clear," "consistent," it will naturally penalize "unexpected," "unconventional," "risky." The research on **divergent thinking assessment** (Torrance Tests) shows that originality requires explicitly measuring and rewarding it — it doesn't emerge naturally from quality-focused evaluation.

**Conclusion on flatness**: It's primarily a model capability problem (models have limited originality), amplified by pipeline architecture (multi-pass convergence) and exacerbated by review criteria (implicitly preferring the safe). The most impactful fix is changing the pipeline architecture; the second is revising review criteria to explicitly reward novelty.

---

## 5. What Pipeline Architectures Work for Other Creative Domains?

### 5.1 Image Generation (Stable Diffusion)

The most successful creative generation pipeline in production today. Its architecture:

1. **Text encoding**: CLIP/T5 encodes prompt into embedding
2. **Latent diffusion**: Iterative denoising in latent space (not agent feedback — mathematical refinement)
3. **Optional upscaling**: Second model increases resolution
4. **Optional inpainting/etc**: Post-hoc fixes

Key difference from Soul Factory: SD refinement is **mathematical**, not evaluative. The diffusion process has a clear mathematical objective (reduce noise toward the prompt embedding). There's no LLM agent saying "I think this image could be more creative." The uncertainty and diversity come from the **initial noise seed** — generate many times, pick the best.

**Lesson**: Generate-and-select + mathematical refinement (not evaluative refinement).

### 5.2 Music Generation (MusicLM, MusicGen)

MusicLM uses **hierarchical sequence-to-sequence modeling**:
1. Semantic tokens (high-level structure)
2. Coarse acoustic tokens
3. Fine acoustic tokens

This is a multi-stage pipeline, but the stages are **representational levels**, not refinement loops. Each stage adds detail to a representation, not critique-and-revise. MusicGen uses a single-stage autoregressive transformer.

**Lesson**: Multi-stage works when stages add information (encoding hierarchy), not when they critique and revise.

### 5.3 Code Generation

Code generation pipelines (AgentCoder, Blueprint2Code, CodeAgent) often use multi-stage architectures:

- AgentCoder: Programmer + Test Designer + Test Executor
- Blueprint2Code: Preview → Blueprint → Implement → Debug

But these work because **code has verifiable correctness** — tests either pass or fail. The evaluator isn't making a subjective "is this creative?" judgment; it's checking objective constraints.

**Lesson**: Multi-stage works when stages have objective verification criteria. Creative work lacks this, making multi-stage evaluation unreliable.

---

## 6. What Would a Better Pipeline Look Like?

### 6.1 The Generate-and-Select Architecture (Recommended)

Based on the evidence, the best architecture for creative generation is:

```
┌──────────────────────────────────────────────────┐
│                  GENERATE PHASE                   │
│                                                   │
│  Candidate 1 (Seed A, Temp=1.2, Model=Claude)     │
│  Candidate 2 (Seed B, Temp=1.0, Model=Claude)     │◄── Parallel. Diverse seeds,
│  Candidate 3 (Seed C, Temp=0.9, Model=DeepSeek)   │    diverse temps, diverse
│  Candidate 4 (Seed D, Temp=1.1, Model=Gemini)     │    models.
│  Candidate N (...diverse configuration...)         │
│                                                   │
└──────────────────────────────────────────────────┘
                        │
                        ▼
┌──────────────────────────────────────────────────┐
│                  SELECT PHASE                      │
│                                                   │
│  External Evaluator (independent model or         │
│  trained reward model) rates all N candidates     │
│  on a multi-dimensional rubric:                   │
│    - Originality (30%)                            │
│    - Voice/Character (25%)                        │
│    - Internal consistency (20%)                   │
│    - Tension/Conflict (15%)                       │
│    - Emotional resonance (10%)                    │
│                                                   │
└──────────────────────────────────────────────────┘
                        │
                        ▼
┌──────────────────────────────────────────────────┐
│           OPTIONAL: TIGHT REFINEMENT              │
│                                                   │
│  If needed: one targeted pass on the winner       │
│  using the evaluator's specific critique.         │
│  (Not "make it better" — "fix these 3 things")    │
│                                                   │
└──────────────────────────────────────────────────┘
```

### 6.2 Specific Changes to the Current Pipeline

| Current | Proposed |
|---------|----------|
| T0 (Researcher) → T1 (Screener) → T2 (Namer) | **Keep**: these stages are fine — they're generative/diverge phase |
| T3 (Writer): single pass | **Expand to N parallel passes**: same brief, different seeds/temps/models |
| T4 (Reviewer): evaluate one output | **Replaced by Multi-Candidate Evaluator**: judge N candidates side-by-side |
| T5 (Refiner): open-ended refinement | **Replace with Targeted Fix**: only address specific flagged issues |
| T6 (Final Reviewer): another evaluation | **Keep as final gate** but use different model family from earlier stages |

### 6.3 Key Design Principles

1. **Diversity in generation, not in evaluation.** Generate diverse candidates; evaluate with a single strong selector. The "When Agents Disagree" paper proved this works.
2. **External evaluator.** The selector must NOT be the same model family as the generators to avoid self-bias. Use a different model (Claude evaluates GPT outputs, or vice versa) or a trained reward model.
3. **Parallel, not sequential.** Generate candidates in parallel, not in sequence. Sequential generation introduces path dependency and regression to the mean.
4. **Explicit novelty weighting.** The evaluation rubric must have an originality criterion with weight ≥ 30%. Without it, selection will favor the safe and fluent.
5. **No multi-pass refinement loops.** The evidence shows they compound self-bias and don't reliably improve creative quality. One targeted pass (when needed) is the maximum.
6. **Model choice matters more than pipeline.** The CreativityPrism data shows that model choice accounts for large performance differences. A strong model with a generate-and-select wrapper outperforms a weak model with an elaborate pipeline.

### 6.4 The "Free Lunch" — Adding a Weaker Model

The "When Agents Disagree" paper found an unintuitive result: **adding a substantially weaker model (Claude Haiku) to a diverse generation pool improved win rate (0.929) and reduced cost**. This suggests the optimal candidate pool for generate-and-select includes a mix of model strengths, not just top-tier models. The weaker model occasionally produces surprising outputs that the strong models don't.

---

## 7. How Image and Audio Generation Confirm the Generate-and-Select Pattern

### 7.1 Stable Diffusion

The de facto workflow for professional Stable Diffusion artists (documented in SD workflow guides):

1. **Generate multiple candidates** — a single prompt with different seeds produces different images
2. **Select the best composition** — human or aesthetic scoring model picks the winner
3. **Refine that one** — inpainting specific defects, upscaling
4. **No iterative critique loops** — you don't ask the model to "critique and improve" its own image

This is exactly generate-and-select. The "multi-pass" in SD is the **diffusion denoising process itself**, which is mathematical, not evaluative.

### 7.2 MusicLM

MusicLM generates music through **hierarchical token levels**: semantic → coarse acoustic → fine acoustic. Each level adds granularity. This is NOT an iterative refinement loop — the stages are architectural necessities for handling different time scales. The evaluation happens AFTER generation (human listener or audio quality metric).

### 7.3 Key Pattern

Across all three domains (image, music, code), the successful pattern is:

> **Generate many → select best → (optionally) one targeted fix**

The only domain where iterative refinement loops dominate is code generation, and that works because of **objective verification** (test suites). Creative work lacks this.

---

## 8. Can LLMs Actually Produce Creative Work?

### 8.1 Yes — But With Important Caveats

The evidence is nuanced:

- **LLMs can produce novel outputs** relative to their training data (Padmakumar et al., 2025)
- **They score well on fluency and elaboration** but **poorly on originality** (Zhao et al., 2025, Torrance tests)
- **Multi-agent collaboration enhances originality** (Zhao et al., 2025) — a genuine positive
- **Role-playing significantly influences creativity** (Zhao et al., 2025) — persona assignment works
- **But human-level creative insight remains elusive** — the "stochastic parrot" critique (Bender et al., 2021) still applies: LLMs recombine known patterns, they don't create genuinely new concepts

The CreativityPrism leaderboard shows that the best LLMs (DeepSeek-V3, GPT-4.1) achieve overall creativity scores around 0.75 on a 0-1 scale. That's good but not human-level. More importantly, **excellence in one dimension doesn't predict excellence in others** — novelty and quality often trade off.

### 8.2 The Csikszentmihalyi Insight

The "Creative Agents" paper (Imasato et al., 2024) simulates Csikszentmihalyi's Systems Model of Creativity: creativity emerges from interaction between an individual (the creator), a domain (the body of knowledge), and a field (the gatekeepers who judge novelty). The multi-agent version — where agents interact with each other and receive field-like feedback — produced more creative artifacts than isolated agents.

**Implication**: The social/feedback dimension matters. But the feedback must come from an **external field**, not the same agent's self-evaluation. Soul Factory's current pipeline has this backwards: the "field" (reviewers) is too similar to the "individual" (writers).

---

## 9. Sources Cited

| # | Source | Relevance |
|---|--------|-----------|
| 1 | **Lin et al., 2025** — "Creativity in LLM-based Multi-Agent Systems: A Survey" (EMNLP 2025) | Taxonomies of creative MAS techniques: divergent exploration, iterative refinement, collaborative synthesis |
| 2 | **Xu et al., 2024** — "Pride and Prejudice: LLM Amplifies Self-Bias in Self-Refinement" (ACL 2024) | Formal proof that self-refinement amplifies self-bias across all tested LLMs |
| 3 | **"When Agents Disagree" (arXiv:2603.20324, 2025)** — Selection bottleneck in multi-agent LLM pipelines | Judge-based selection wins 0.810 vs 0.179 over synthesis; synthesis loses to single model in all 42 tasks |
| 4 | **ICLR Blogposts 2025** — Multi-Agent Debate performance analysis | MAD fails to consistently outperform CoT or Self-Consistency; more rounds/agents don't help |
| 5 | **Fein et al., 2025** — "LitBench: A Benchmark for Creative Writing" (Stanford) | Best zero-shot LLM judge only 73% accurate; CoT degrades evaluation; trained reward models outperform |
| 6 | **Padmakumar et al., 2025** — "Measuring LLM Novelty" (arXiv) | Model scale improves novelty via quality; inference-time methods have smaller effect; base text is less novel than human text |
| 7 | **Zhao et al., 2025** — "Assessing and Understanding Creativity in LLMs" (Springer) | Adapted Torrance Tests: LLMs strong on elaboration, weak on originality; role-play and multi-agent collaboration help |
| 8 | **Hou et al., 2025** — "CreativityPrism" | 8-task, 3-dimension creativity evaluation of 17 LLMs; model matters more than pipeline |
| 9 | **Anthropic, 2024** — "Building Effective Agents" | Practical advice: simple composable patterns; evaluator-optimizer only when clear criteria exist |
| 10 | **Imasato et al., 2024** — "Creative Agents: Simulating the Systems Model of Creativity" (IEEE Access) | Multi-agent edition of Csikszentmihalyi's model outperforms isolated agents |
| 11 | **MusicLM (Google, 2023)** — Hierarchical text-to-music generation | Multi-stage as representational hierarchy, not refinement loop |
| 12 | **Stable Diffusion workflows** — Professional image generation practice | Generate-many, select-best, one-pass fix; no iterative critique loops |

---

## 10. Recommendations (Action Items)

### High Priority (Immediate Impact)

1. **Convert T3 Writer from single to N parallel generations.** Generate 5-10 candidates with different seeds, temperatures (0.8–1.2), and optionally different models. This is a configuration change, not a code change.

2. **Replace T4 Reviewer with a Multi-Candidate Evaluator.** Instead of evaluating one output, have one evaluation phase that judges all N candidates side-by-side and selects the best. Use a different model family than the generators.

3. **Add explicit originality weighting to evaluation rubrics.** The T6 final gate should weigh originality at ≥30%. Without this, selection will always favor safe outputs.

4. **Eliminate the T5 → T6 multi-pass refinement cycle.** Replace with a single targeted refinement pass (if needed) based on specific flagged issues, not an open-ended "improve this."

### Medium Priority

5. **Introduce model diversity in the generation pool.** Include a weaker or different-variant model alongside the main generator. Research shows this can improve performance at lower cost.

6. **Train or fine-tune a dedicated evaluator model** for creative quality. The LitBench results show trained reward models (78% accuracy) outperform zero-shot judges (73%).

### Lower Priority (But Worth Investigating)

7. **Experiment with adversarial generation** — one agent writes a persona, another tries to find its weaknesses, the weakness-finding feeds back into a targeted revision. This is the one refinement pattern that has some theoretical basis (it's how scientific peer review works).

8. **Consider removing the pipeline entirely for some cases.** For routine persona generation, a strong single model with a well-structured prompt + N samples may outperform the pipeline at lower cost and latency.

---

## Appendix: Key Metrics Comparison

| Approach | Cost/Task | Latency | Originality | Consistency | Evaluated By |
|----------|-----------|---------|-------------|-------------|-------------|
| Current 7-stage pipeline | High (7 LLM calls) | Very High (sequential) | Low (regression to mean) | High | Self-bias contaminated |
| Generate-and-select (N=5) | Medium (5+1 calls) | Low (parallel) | High (exploit tails) | High (select best) | External evaluator |
| Single strong model × N samples | Low (N calls) | Low (parallel) | Medium | Medium | Human or RM |
| Multi-agent debate (4 agents, 3 rounds) | Very High (12+ calls) | Very High | Medium (forced diversity) | Low (incoherent) | Self-evaluation |

**Verdict**: Generate-and-select is the clear winner on the metrics that matter for creative output: originality (the hardest problem), cost, and latency.

---

*End of research report. Written for Soul Factory pipeline architecture decision.*