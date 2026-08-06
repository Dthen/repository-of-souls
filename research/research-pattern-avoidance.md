# Research: Pattern Avoidance in Creative Writing with LLMs

**Date:** 2026-07-20
**Author:** researcher (Kanban task t_8c130047)
**Purpose:** Consolidate what's known about preventing homogenization when using LLMs for creative writing — at the prompt design level, generation strategy level, instruction format level, and training level.

---

## Executive Summary

LLMs are collectively homogeneous. Wenger & Kenett (2025) showed that 22 different LLMs produce outputs that are significantly more similar to each other than human outputs are to each other — even though individual LLM creativity scores match or exceed human averages. Doshi & Hauser (2024) found that while GenAI *enhances individual creative output*, AI-assisted stories are substantially more similar to each other than human-only stories. Yun et al. (2025) demonstrated that structured prompt templates (role markers, system/user tokens) actively *induce* diversity collapse — the very format conventions designed to improve alignment suppress creative variability, and this persists even at high temperature.

This research consolidates findings across six research questions: what prompt design techniques produce diversity, what generation strategies prevent homogenization, what causes LLM convergence, why counter-examples work, what practitioners do, and what role instruction format plays. The central finding: **pattern avoidance requires deliberate counter-pressure at every level of the pipeline** — no single technique suffices.

**Key takeaway for the Soul Repository v5 pipeline:** Structured templates (the SOUL.md format itself) are a source of diversity collapse. Every format constraint, every "Never" rule, every structured section heading pulls the model toward a shared output space. The solution is not to abandon structure but to build *deliberate diversity levers* into the pipeline — multi-agent disagreement, genre transplant prompts, constraint cages, and diversity-aware selection — that actively counteract the homogenizing pull of the format.

---

## Table of Contents

1. [The Homogenization Problem — Evidence and Scope](#1-the-homogenization-problem)
2. [Mechanistic Sources — Why LLMs Converge](#2-mechanistic-sources)
3. [Prompt Design Techniques for Diversity](#3-prompt-design-techniques)
4. [Generation Strategies That Prevent Homogenization](#4-generation-strategies)
5. [Counter-Examples as Pattern Prevention](#5-counter-examples)
6. [What the Practitioner Community Does](#6-practitioner-community)
7. [Instruction Format — Principles vs Formats](#7-instruction-format)
8. [Training-Level Interventions](#8-training-level-interventions)
9. [Synthesis and Actionable Insights](#9-synthesis)
10. [Sources](#10-sources)

---

## 1. The Homogenization Problem

### 1.1 The Core Finding

The headline result from Wenger & Kenett (2025) is deceptively simple: LLM outputs are individually creative (matching or exceeding humans on divergent association, alternative uses, and forward flow tests) but collectively homogeneous across models. **Population variability** — the semantic spread of outputs across a group — is dramatically lower for LLMs than for humans:

| Measure | Human | LLM |
|---------|-------|-----|
| **Population variability (AUT)** | 0.727 | 0.459 |
| **Pairwise similarity (open-ended)** | 0.45 | 0.75 |
| **Distinct-n (lexical diversity)** | higher | −15–20% |

(Wenger & Kenett 2025; Sourati et al. 2025)

This means: using *any* LLM as a creative partner pushes all users toward a shared output space, regardless of which model they use.

### 1.2 The Doshi & Hauser Social Dilemma

Doshi & Hauser (2024, *Science Advances*) ran a pre-registered experiment where 293 writers wrote short stories, with some having access to GPT-4 ideas and others writing without AI. Key findings:

- **Individual creativity increased:** GenAI-enabled stories were rated as better written and more enjoyable, especially for less creative writers
- **Collective diversity decreased:** GenAI-enabled stories were significantly more similar to each other than human-only stories
- **This is a social dilemma:** Each individual writer benefits from AI assistance, but collectively the scope of novel content narrows

The effect persisted regardless of whether writers received 1 or 5 GenAI ideas — just having access was enough to anchor outputs toward a shared distribution.

### 1.3 Format-Induced Diversity Collapse

Yun et al. (2025, "The Price of Format: Diversity Collapse in LLMs") made a critical discovery: **structured prompt templates themselves cause diversity collapse**. Specifically:

- **Format consistency between fine-tuning and inference is crucial for structure-sensitive tasks** (GSM8K, IFEval) but has marginal influence on knowledge-heavy tasks (MMLU, WebQuestions)
- **Output diversity is primarily governed by the presence or absence of structural tokens** — role markers, system/user boundaries, special delimiters
- **Diversity collapse persists even under high-temperature sampling** — temperature alone cannot overcome format-induced convergence
- **Removing chat-format tokens increases output diversity by 2–3×** in free-form generation

This is the most consequential finding for pipeline design: every structural constraint in a prompt template is a potential diversity-collapse vector.

### 1.4 Cross-Domain Homogenization

The homogenization effect is robust across domains and measurement approaches:

- **Narrative function:** LLM fiction has sharply peaked narrative-function histograms with low entropy — repetitive plot paradigms. Even DeepSeek and Qwen default to "hero-struggle-victory" templates (Ma et al., 2026)
- **Open-ended ideation:** 79% of open-ended prompts on the Infinity-Chat corpus yield intra-model similarity > 0.8 (Jiang et al., 2025)
- **Creative evaluation:** LLM judges agree with each other at Spearman ρ > 0.7, reinforcing homogeneity in both creation and assessment (Rabeyah et al., 2024)
- **Cross-lingual:** The narrative homogenization pattern replicates in both English and Chinese story generation (Ma et al., 2026)

### 1.5 The Reinforcement Loop

Sourati et al. (2025/2026, *Trends in Cognitive Sciences*) documented a dangerous feedback loop: as LLM-generated content is recursively used in communications, education, and knowledge bases, statistically dominant patterns become cultural norms, which then appear more frequently in training data, which further reinforces the LLM's bias toward those patterns. This creates a self-reinforcing cycle of homogenization.

---

## 2. Mechanistic Sources — Why LLMs Converge

### 2.1 Statistical Centrality (Next-Token Prediction)

The fundamental cause: next-token prediction rewards high-probability continuations. This pulls outputs toward the statistical center of the training distribution — grammatically correct, factually plausible, and deeply average. Uhlmann (2025) calls this the **"kitsch" dynamic** — the model produces what feels right rather than what is novel.

**For creative writing, this manifests as:**
- **Grumpy competence** — the default emotional register. Most LLMs default to weary, mildly frustrated competence because this is the statistical center of professional writing in the training data
- **"You'd think" / "Always the X that Y" structures** — these are high-probability rhetorical patterns that appear repeatedly in instructional and narrative text. The model prefers them because they sit at a local probability maximum
- **Symmetrical "X but Y" sentences** — balanced structures are high-probability continuations in formal writing

### 2.2 Format-Induced Collapse

Yun et al. (2025) showed that instruction fine-tuning on chat-style templates instills **fixed generation priors**. The structural tokens (```<|im_start|>```, ```<|user|>```, ```<|assistant|>```) act as **behavioral anchors** that the model's generation rapidly converges toward. After just a few decoding steps, the output space is dramatically constrained.

**Why this happens:**
- During SFT, the model learns that after certain structural tokens, particular output distributions are rewarded
- During inference, these priors dominate — the model defaults to the highest-probability path from the structural anchor
- Removing the structural tokens removes the anchor, allowing wider exploration

### 2.3 Alignment and Uncertainty Minimization

RLHF and SFT steer outputs toward low-uncertainty, "safe" continuations. Sui (2026) shows that this suppresses **constructive ambiguity** — the productive uncertainty that makes creative writing interesting. The aligned model avoids:

- Unresolved tensions
- Ambiguous endings
- Unreliable narrators
- Subversion of expectations

All of which are hallmarks of genuinely creative writing.

### 2.4 Cognitive Process Compression

Nguyen et al. (2025) identify a structural problem: without explicit **divergent-convergent phase separation**, LLMs conflate idea generation with immediate constraint satisfaction. In human creative practice, divergence (generating many possibilities) and convergence (selecting and refining) are separate phases. LLMs try to do both simultaneously, which prunes uncommon ideas before they fully form.

### 2.5 Training Data and Social Bias

Lee et al. (2024) documented that differential coverage in training corpora causes subordinate social groups to be depicted with markedly higher narrative homogeneity — mirroring the human out-group homogeneity effect. The model's training data has less diversity for certain groups, and this compounds in generation.

### 2.6 Repetition Bias

The Nature Scientific Reports (2026) study documented a specific repetition pattern: GPT-4-turbo used "ocean" in >90% of responses; GPT-4 used "microscope" in 70%. Humans' most frequent words appeared at only ~1% frequency. This confirms a **lexical repetition bias** that higher temperature mitigates but does not solve.

### 2.7 The Selection Bottleneck in Multi-Agent Systems

Maryanskyy (2026) identified a critical finding about multi-agent pipelines: **generator diversity matters less than selector quality**. The paper derives a crossover threshold s* (Proposition 1) below which diverse teams underperform single models and above which they excel. The mechanism: if the selection/aggregation mechanism is poor, diversity in the candidate pool is wasted — the selector picks the most average candidate.

For creative pipelines: generating many diverse candidates is only useful if there's a good selection mechanism. A poor selector (or a selector with the same homogenization biases as the generator) will collapse diversity back to the mean.

---

## 3. Prompt Design Techniques for Diversity

### 3.1 Structure-Free / Natural Instruction Prompts

Yun et al. (2025) found that **minimal formatting produces the most diverse outputs**. Removing role markers, system/user boundaries, and structural tokens increases output diversity by 2–3×.

**For creative writing:** Frame the task as a natural instruction rather than a structured template. Compare:

> ❌ `[SYSTEM: You are a creative writer. Write a story.]\n[USER: Write about a forest.]`

> ✅ `"Write a story about a forest — the kind of story that wouldn't work if you set it anywhere else."`

The second version is minimally formatted and produces wider output variation because it doesn't anchor the model's generation prior.

### 3.2 The Constraint Cage

Paradoxically, *content* constraints increase diversity while *structural* constraints decrease it. The key difference:

- **Content constraints** (avoid a specific word, include a specific object, limit sentence length) force the model away from default paths by closing off high-probability routes
- **Structural constraints** (section headers, role markers, format requirements) anchor the model to a fixed generation prior

The sweet spot is 3–5 content constraints. More than 7 and output quality degrades as the model struggles to satisfy competing requirements.

### 3.3 Specific Roles with Internal Tension

Research from Zhao et al. (2025), confirmed across multiple studies:

- **Any specific role** is better than no role for creative output
- **A role with internal contradiction** (a wedding planner who believes marriage is a scam) outperforms a flat role (just "writer")
- **The "scientist" role** produced the highest creativity scores across all dimensions — possibly because "scientist" implies systematic inquiry rather than artistic expression, which reduces the model's stylistic priors

The mechanism: a contradictory persona creates **creative resistance** — the model must reconcile competing impulses, which forces it off the default path.

### 3.4 Positive Framing Over Negative Constraints

Research on negation in prompts (arXiv:2209.12711, 2305.17311, 2306.08189) consistently shows that negative instructions ("don't do X") are unreliable:

- Larger models get *worse* at following negative instructions relative to positive ones
- Negative prompts require the model to first represent X, then suppress it — a harder task than generating toward a positive target
- Practitioner evidence (Gadlet, 2025): "Don't uppercase names" frequently fails; "Always lowercase names" consistently works

**For pattern avoidance:** Convert top-level negative constraints to positive instructions. Retain negatives only for specific, recurring failure modes that positive framing can't catch.

### 3.5 Example Diversity

Research on few-shot prompting for creativity shows:
- **3 diverse examples** beat 10 similar ones (Medium AI Architecture, 2025)
- **Counter-examples** (showing what NOT to do) prevent pattern adoption more effectively than exclusive positive examples
- **Structural diversity in examples** — showing examples with different structures — directly prevents pattern formation
- Examples should show *range* across genres, registers, and structures, not just the ideal output

### 3.6 Decoding Parameters

| Parameter | Effect on Diversity | Research Finding |
|-----------|-------------------|------------------|
| Temperature (0.8–1.2) | ✓ Moderate increase | Necessary but insufficient. Cannot overcome format-induced collapse alone |
| Top-p (0.9) | ✓ Some increase | Pairs well with high temp |
| Frequency penalty (0.3–0.7) | ✓ Moderate increase | Directly counters lexical repetition bias |
| Presence penalty (0.3–0.7) | ✓ Thematic spread | Encourages broader topic coverage |

**Critical finding from Yun et al. (2025):** Higher temperature and nucleus sampling have *limited impact* unless format priors are also weakened. If the prompt uses structured templates, raising temperature won't fix diversity collapse.

### 3.7 Divergent-Convergent Decoupling

Nguyen et al. (2025) propose **CreativeDC**: explicitly separating the divergent phase (generate many alternatives freely) from the convergent phase (select and refine). This mirrors the human creative process and yields higher Vendi scores, lexical diversity, and semantic diversity than combined generation.

**In practice:**
1. **Divergent phase:** "Generate 5 completely different openings for this story. Make them as structurally different from each other as possible."
2. **Convergent phase:** "Select the most promising opening. Now develop it, but preserve whatever made it unique."

---

## 4. Generation Strategies That Prevent Homogenization

### 4.1 N-Version Gambit

Ask for N versions with explicit differentiation instructions. The first version will always be the most probable (competent, boring). Version 3–5 are often genuinely creative because the model has exhausted the high-probability paths.

**Research grounding:** This operationalizes the "multiple versions" technique validated in Zhao et al. (2025) — generating multiple outputs before selection increases flexibility and originality.

**Critical refinement:** Explicitly instruct differentiation, not just count. "Write 5 versions" without guidance produces subtle surface variations on the same core structure. "Write 5 versions, each using a different narrative strategy" produces genuine diversity.

### 4.2 Multi-Agent Generation with Disagreement (The Maryanskyy Finding)

Maryanskyy (2026) showed that in generate-then-select pipelines, **selector quality matters more than generator diversity**:

- A diverse team with judge-based selection achieved a win rate of 0.810 against single-model baseline
- A homogeneous team scored 0.512 (near chance)
- Judge-based selection outperformed MoA-style synthesis by Δ_WR = +0.631
- **Including a weaker model** improved performance while reducing cost

**Practical pipeline implication:** Having multiple writer agents with different personas/approaches is only valuable if the evaluator agent can meaningfully distinguish quality. If the evaluator uses the same criteria as the writers (or the same underlying model with the same biases), diversity collapses at the selection stage.

### 4.3 "Worst Version First" (Reverse Psychology)

Ask the model to generate the worst possible version first, then write the opposite. This forces the model to:

1. Externalize its default pattern (the "worst" version surfaces clichés and expected tropes)
2. Understand the pattern well enough to subvert it
3. Navigate toward lower-probability token space

**Research support:** This is structurally similar to "post-instructive prompting" in Zhao et al. (2025), which improved originality by having the model revise after initial generation. The mechanism: the first pass exhausts high-probability paths; the second pass must explore lower-probability space.

### 4.4 Genre Transplant

Forcing content-form mismatch creates novelty through constraint satisfaction:

| Content | Form | Creative Tension |
|---------|------|-----------------|
| Horror story | Recipe structure | How does dread follow procedural steps? |
| Love letter | Tech support ticket | How does emotion survive a format designed for detachment? |
| Obituary | Grocery list | How does memorialization fit between "milk" and "eggs"? |

**Why it works:** Genre conventions are strong attractors in LLM output. Forcing a mismatch between content and form forces the model to solve a novel constraint-satisfaction problem, breaking the default path.

### 4.5 The Collaboration Loop (Optimized Multi-Agent)

Zhao et al. (2025) found that 2–3 agents discussing for 2–3 rounds enhanced creativity, with the strongest improvement in **Originality**. Key constraints:

- **Single-round multi-agent** actually decreased creativity (later agents negated earlier ones)
- **Beyond 3 rounds or 3 agents**, creativity decreased
- **2 agents, 2–3 rounds** is the optimal configuration

### 4.6 Break the Fourth Wall Meta-Cognition

Ask the model to explicitly identify the conventional approach before writing:

> "Before you begin, explain what the most conventional version of this writing would look like. Then explain how you're going to subvert it. Then write."

**Why it works:** Forces the model to externalize its default pattern. Making the "competent" path explicit creates conscious opposition. This is analogous to asking a human writer "what's the most obvious thing to do here, and why won't you do it?"

### 4.7 Diverse Generation Pool Construction

When building a multi-agent pipeline for creative generation:

| Strategy | Effect | Research Support |
|----------|--------|-----------------|
| Same model, different roles | Produces surface variation | Zhao et al. 2025 |
| Different models, same task | Produces structural variation | Maryanskyy 2026 |
| Different models + different roles | Maximum variation | Maryanskyy 2026 |
| Same model, different temperatures | Limited — structure dominates | Yun et al. 2025 |

**Key insight for pipelines:** If all agents use the same underlying model, they will converge on similar outputs even with different instructions. True diversity requires model heterogeneity or deliberate counter-pressure mechanisms.

---

## 5. Counter-Examples as Pattern Prevention

### 5.1 What Makes Counter-Examples Effective

The finding that showing a "bad" example prevents pattern adoption more effectively than showing a "good" example is supported by both research and practitioner evidence:

- **Reddit practitioner study (2025):** "I tested 4 methods to make LLMs write literary subtext" — few-shot with 5 examples outperformed fine-tuning and DPO
- **Contrastive prompting** (showing good + bad examples with explanations) helps the model understand the *boundaries* of acceptable output rather than just the target
- **Counter-examples teach what NOT to do** — and since the model's default path is high-probability competence, knowing what to avoid is more valuable than knowing what to aim for

### 5.2 The Mechanism

The contrastive mechanism works because:
1. The model already knows what "good" looks like (its training data is full of competent writing)
2. What it lacks is a theory of *failure* — what distinguishes creative from merely competent
3. Showing failure modes (clichés, predictability, formulaic structure) gives the model explicit criteria for avoidance
4. The "bad" example provides a negative anchor that shifts probability mass away from default paths

### 5.3 Optimal Counter-Example Structure

Research on few-shot prompting for creative tasks suggests:

- **3 examples + 1 counter-example per rule** is the sweet spot
- **Diverse examples** (different registers, archetypes) prevent the examples from becoming new templates
- **Counter-examples should be annotated** — explain *why* each is a failure, not just that it is
- **Don't use reference personae as the only examples** — they become templates, not inspiration

### 5.4 The Pipeline Application

For the Soul Repository v5 pipeline, counter-examples should be:
- **Stage-specific:** What does a bad seed look like? What does a bad name look like? What does a bad soul draft look like?
- **Annotated for specific failure modes:** "This line fails because it describes behavior instead of revealing character"
- **Diverse across registers:** Don't show the same failure type repeatedly
- **Updated periodically:** As the pipeline evolves, new failure modes emerge

---

## 6. What the Practitioner Community Does

### 6.1 Character Card Systems (SillyTavern / Character.AI)

The roleplay community has developed the most sophisticated practical systems for maintaining voice diversity across LLM interactions. Key techniques:

**Character Cards** (SillyTavern):
- A character card bundles persona definition, scenario context, example dialogues, and behavioral instructions
- **Example dialogues are the most critical component** — not abstract rules about how the character should behave, but concrete demonstrations of the character in conversation
- Cards include both positive demonstrations (what the character says) and negative demonstrations (what the character would never say)
- **Post-history instructions** (system prompts that appear after the last user message) are used to reinforce voice when the model starts drifting

**Emergent patterns:**
- **Scenario anchoring:** A well-crafted scenario narrows the output space in productive ways — specific context prevents default responses
- **Voice markers:** Distinctive vocabulary, sentence rhythm markers, and register patterns embedded in the card
- **Avoidance lists:** Short (3–5 items) lists of specific phrases or response types the character should never use
- **Iterative refinement:** Users frequently regenerate responses until the character's voice emerges, treating the first 3–5 outputs as noise

### 6.2 Creative Fiction Writers Using AI

The "From Pen to Prompt" study (Singh et al., 2024) interviewed 18 creative writers who regularly use AI. Key findings about voice maintenance:

- **Intentionality was the primary theme:** Writers make deliberate decisions about when to use AI and when not to, based on strongly held values about authenticity
- **AI for scaffolding, not substance:** Most writers use AI for structure, research, and brainstorming — not for the actual creative text
- **Post-editing is universal:** Every interviewed writer described significant editing of AI output to "make it sound like me"
- **Genre-specific prompting:** Writers develop prompting styles specific to their genre (poetry vs fiction vs memoir) rather than using generic approaches
- **Preserving authentic voice:** Writers report that AI tends to flatten their voice toward a generic register, requiring conscious restoration of their own patterns

### 6.3 Prompt Engineering Community Techniques

The r/PromptEngineering community has documented several diversity-preserving techniques:

- **Multiple drafts with explicit differentiation:** Generate 3–5 variations with instructions to make them structurally different, then cherry-pick
- **Persona-switching within a session:** Cycle through 2–3 distinct persona instructions to force the model out of any single register
- **Temperature cycling:** Start high (1.0–1.2) for initial generation, drop low (0.3–0.5) for refinement — prevents the model from falling back to the same high-probability pattern during refinement
- **"Avoid these words" lists:** Short lists of overused words or phrases specific to the current genre
- **Citation prompting:** "Write this in the style of [X], but about [unusual topic]" — external anchoring provides a specific voice target

### 6.4 What Practitioners Get Right

- **They show, don't tell:** Character cards use demonstration over instruction
- **They use negative constraints sparingly:** 3–5 specific avoidance items, not exhaustive lists
- **They iterate through failure:** Treat the first outputs as aspirational noise, not final product
- **They accept the structural limit:** Practitioners understand that LLMs default to competence and plan for it, rather than trying to eliminate it through perfect prompting

### 6.5 What Practitioners Get Wrong

- **Over-indexing on temperature:** Many practitioners assume high temperature = creativity, not realizing that structural format priors dominate
- **Under-investing in selection:** Generating many versions is common, but selection criteria are often vague ("pick the best one")
- **Assuming roleplay is real diversity:** Different characters on the same model still share underlying distributional patterns
- **Neglecting the evaluator:** Most practitioners don't realize that their own evaluation (which version to keep) has the same biases as the generator

---

## 7. Instruction Format — Principles vs Formats

### 7.1 The Central Question

Does instructing WHAT to achieve produce more diverse outputs than instructing HOW to achieve it? The evidence suggests a nuanced answer:

- **"Teach principles, not formats"** works when the principles are operationalized — the model needs to translate the principle into generation behavior
- **Format instructions** (line count, word count, section structure) are reliably followed but actively reduce diversity
- **Principle instructions** (voice quality, character depth) produce more varied but less reliable outputs

### 7.2 The Operationalization Gap

The problem with principles is the **operationalization gap**: "Write with authentic voice" is interpretable to a human but ambiguous to an LLM. The model needs to know what "authentic voice" *sounds like* — which requires demonstration, not definition.

**Effective pattern: principle + demonstration:**

> "Every line should do at least two jobs — reveal character, advance voice, create tension, or teach perception. Here are 3 lines that do this well, and 1 line that doesn't."

This combines the flexibility of principle-based instruction with the specificity of format-based instruction.

### 7.3 Evidence on Format vs Principle

| Approach | Reliability | Diversity | Best For |
|----------|------------|-----------|----------|
| Pure format constraints | High | Low | Compliance-critical tasks |
| Pure principles | Low | High | Open-ended creative tasks |
| Principle + 1–3 format guardrails | Medium | Medium-High | Most creative writing tasks |
| Principle + demonstration | Medium | High | Teaching quality judgment |

### 7.4 The Format-as-Anchor Problem

Yun et al. (2025) is the definitive paper on this: **structured format instructions act as behavioral anchors**. The more structured the prompt, the narrower the output distribution — regardless of content instructions.

**Practical implications:**
- SOUL.md format (H1, lines, sections) is itself a diversity-reducing structure
- Every format constraint should be justified: "Does this constraint improve quality enough to justify the diversity loss?"
- Consider **optional formatting** — allow deviation from format in low-stakes sections, enforce it only where structural consistency is essential

### 7.5 Example Structural Diversity

Showing examples with *structural* diversity prevents pattern formation more effectively than showing examples with the same structure. If all few-shot examples use the same format, the model learns the format as a template. If examples vary in structure, the model learns the range of acceptable variation.

**For SOUL.md:** If every reference persona follows the same sentence pattern ("You are X who Y"), the model will reproduce that pattern. If reference personae show structural variety (some starting with "You are", some starting with domain metaphor, some starting with complaint), the model learns that structure is flexible.

### 7.6 The Yun et al. Counter-Intuitive Finding

The most counter-intuitive result: **format consistency between fine-tuning and inference matters more for diversity than the format content itself**. If the model was fine-tuned with structured templates, using unstructured prompts at inference time doesn't fully recover diversity — the generation prior is baked in. This suggests that:

- Post-training (SFT, RLHF) on structured data creates a lasting diversity penalty
- This penalty cannot be fully recovered through prompt engineering alone
- Diversity-aware fine-tuning (Chung et al., 2025 — DivPO, ORPO) may be necessary

---

## 8. Training-Level Interventions

### 8.1 Diversity-Promoting Post-Training

Chung et al. (2025, "Modifying LLM Post-Training for Diverse Creative Writing") demonstrated that training objectives can be modified to promote diversity:

- **Core idea:** Include *deviation* — the degree of difference between a training sample and all other samples with the same prompt — in the training objective
- Applied to DPO and ORPO, this approach promoted output diversity while minimally decreasing quality
- The best 8B parameter model achieved on-par diversity with a human-created dataset while maintaining quality similar to GPT-4o and DeepSeek-R1
- Validated with human evaluation and ablation studies

### 8.2 Anti-Causal and Contrastive Losses

Ma et al. (2026) proposed fine-tuning with:
- **Anti-causal losses** that penalize the model for reproducing narrative-function templates
- **Structural-contrastive losses** that reward deviation from high-probability plot structures
- Explicit narrative-function supervision for fiction domains

### 8.3 Uncertainty-Aware Alignment

Sui (2026) proposed **ambiguity-permissive reward models** and **credal-set planning** to re-inject productive unpredictability into aligned models. The key insight: current RLHF penalizes ambiguity, but ambiguity is essential for creative writing. Reward models should be trained to recognize *productive* uncertainty versus *unproductive* incoherence.

### 8.4 Implications for Pipeline Design (Not Training)

Since the Soul Repository pipeline works with existing models rather than training new ones, these training-level findings translate to:

- **Model selection matters:** Some models have inherently more diverse output distributions (Chung et al. found significant variation across similarly-sized models)
- **Fine-tuning lineage matters:** A model fine-tuned on diverse creative writing will produce more diverse outputs than one fine-tuned on chat/instruction data
- **API vs open-weight:** API models may have more alignment-induced homogenization than open-weight models that can be fine-tuned for diversity

---

## 9. Synthesis and Actionable Insights

### 9.1 The Counter-Pressure Framework

Pattern avoidance requires **deliberate counter-pressure at every level** because homogenization operates at every level:

| Level | How Homogenization Occurs | Counter-Pressure |
|-------|--------------------------|-----------------|
| **Training** | Next-token prediction favors central tendencies | Diversity-promoting objectives (DivPO, ORPO) |
| **Alignment** | RLHF penalizes ambiguity, rewards safety | Ambiguity-permissive reward models |
| **Format** | Structural tokens anchor generation priors | Minimal formatting, structure-free prompts |
| **Instruction** | "Never" rules require suppression of defaults | Positive framing, teach what TO generate |
| **Examples** | Few-shot examples become templates | Diverse structural examples + counter-examples |
| **Generation** | Single-pass conflates divergence/convergence | Divergent-convergent decoupling |
| **Selection** | Poor selector collapses diverse candidate pool | Judge-based selection, diversity-aware evaluation |
| **Pipeline** | Same model + same format across stages | Model heterogeneity, structural variety |

### 9.2 Specific Recommendations for the Soul Repository v5 Pipeline

**1. Minimize structural formatting in writer prompts:**
The SOUL.md format constraints (H1, line count, section structure) should be stated once as a post-generation requirement, not embedded in the generation prompt. The writer should generate freely, then run a compliance check.

**2. Introduce writer-pool diversity:**
If the pipeline uses a single writer agent, consider using 2–3 writer agents with different model backends (or different fine-tune lineages). The Maryanskyy finding shows that even a weaker model in the pool improves output diversity.

**3. Upgrade the evaluator:**
The evaluator is the most critical quality lever. A poor evaluator collapses whatever diversity the writer pool produces. Use:
- **Judge-based selection** over synthesis-based aggregation
- **Chain-of-thought evaluation** before scoring
- **Explicit diversity criteria** — does this candidate bring something new to the table?

**4. Replace "Never" rules with positive counter-examples:**
Each format constraint should be paired with a counter-example showing the failure mode. The model learns more from "this is what bad looks like" than from "never do this."

**5. Use the genre-transplant technique for seed generation:**
When the Researcher (T0) generates archetypes, force content-form mismatch: "Describe a [warrior archetype] using the structure of a [recipe]" or "Describe a [healer archetype] using the language of [engineering specs]."

**6. Add a diversity gate before the evaluator:**
After N candidates are generated, enforce minimum pairwise diversity before evaluation. If all candidates cluster around the same pattern, require regeneration before passing to evaluation. This prevents the evaluator from being forced to choose between near-identical candidates.

**7. Apply the format-as-anchor finding:**
Yun et al. (2025) showed that minimal formatting produces the most diverse outputs. The SOUL.md format should be treated as a **compliance constraint** (verified post-generation) rather than a **generation template** (embedded in the prompt). The pipeline currently does the latter.

### 9.3 Quick Wins

1. **Remove structural tokens** from the writer generation prompt — state format requirements as post-generation instructions
2. **Add counter-examples** to each format rule — show what failure looks like
3. **Implement the Maryanskyy selection approach** — judge-based selection over synthesis-based combination
4. **Add a diversity check** at the Namer-to-Writer handoff — ensure the Namer isn't producing structurally identical candidates
5. **Diversify reference personae** — ensure they show structural variety, not just character variety

### 9.4 Open Questions

1. **Does the format-as-anchor finding scale to persona-length prompts?** Yun et al. studied shorter generation tasks — the effect may be stronger or weaker for longer persona definitions.
2. **What is the optimal diversity/quality trade-off in generate-then-select pipelines?** Chung et al. found that diversity can be increased with minimal quality loss, but the shape of the trade-off curve is task-dependent.
3. **Can counter-examples become templates too?** There's a risk that repeated counter-examples become a new set of patterns to avoid — or, worse, become patterns to inadvertently follow.
4. **Does the reinforcement loop (Sourati et al.) affect pipeline-generated personas?** If pipeline outputs are fed back into training data or used as reference for future generations, homogenization may compound across pipeline iterations.

---

## 10. Sources

### Academic Papers

1. Wenger, E. & Kenett, Y. (2025). "We're Different, We're the Same: Creative Homogeneity Across LLMs." arXiv:2501.19361.
   - *Core finding: LLM outputs are individually creative but collectively homogeneous — population variability is significantly lower for LLMs than humans.*

2. Doshi, A.R. & Hauser, O.P. (2024). "Generative AI enhances individual creativity but reduces the collective diversity of novel content." *Science Advances*, 10(28). DOI: 10.1126/sciadv.adn5290. Earlier version: arXiv:2312.00506.
   - *Core finding: GenAI improves individual story quality and enjoyment but makes stories more similar to each other — a social dilemma.*

3. Yun, L., An, C., Wang, Z., Peng, L., & Shang, J. (2025). "The Price of Format: Diversity Collapse in LLMs." arXiv:2505.18949. EMNLP 2025.
   - *Core finding: Structured prompt templates (structural tokens) actively induce diversity collapse — persists even at high temperature. Minimal formatting produces the most diverse outputs.*

4. Maryanskyy, A. (2026). "When Agents Disagree: The Selection Bottleneck in Multi-Agent LLM Pipelines." arXiv:2603.20324.
   - *Core finding: Selector quality matters more than generator diversity in multi-agent pipelines. Diverse teams with good selectors achieve 0.810 win rate vs baseline.*

5. Sourati, Z., Ziabari, A.S., & Dehghani, M. (2025/2026). "The Homogenizing Effect of Large Language Models on Human Expression and Thought." *Trends in Cognitive Sciences*. arXiv:2508.01491.
   - *Core finding: LLMs risk standardizing language and reasoning through a self-reinforcing feedback loop. Synthesizes evidence across linguistics, psychology, and computer science.*

6. Chung, J.J.Y., Padmakumar, V., Roemmele, M., Sun, Y., & Kreminski, M. (2025). "Modifying Large Language Model Post-Training for Diverse Creative Writing." arXiv:2503.17126.
   - *Core finding: Including deviation in training objectives (DivPO/ORPO) promotes output diversity while minimally decreasing quality. 8B model achieves human-level diversity.*

7. Zhao et al. (2025). "Assessing and Understanding Creativity in Large Language Models." TTCT Framework.
   - *Core finding: LLMs score highest on Elaboration, lowest on Originality. Scientist role produces highest creativity. Multi-agent (2 agents, 2-3 rounds) improves originality.*

8. Chakrabarty et al. (2023). "Art or Artifice? Large Language Models and the False Promise of Creativity." TTCW Framework.
   - *Core finding: LLMs pass 3–10× fewer creativity tests than humans. LLMs cannot evaluate creative writing (Cohen's Kappa ≈ 0 with expert judges).*

9. Wang et al. (2025). "A large-scale comparison of divergent creativity in humans and LLMs." *Nature Human Behaviour*.
   - *Core finding: Humans show greater variability — the most creative humans far exceed the best LLM. Genius/demographic prompting hits a threshold then reverses into stereotypes.*

10. Nature Scientific Reports (2026). DAT & Creative Writing study.
    - *Core finding: GPT-4 at temp 1.5 surpasses 72% of humans on divergent creativity. But lexical repetition bias persists — GPT-4-turbo used "ocean" in >90% of responses.*

11. Singh et al. (2024). "From Pen to Prompt: How Creative Writers Integrate AI into their Writing Practice." ACM CHI.
    - *Core finding: Creative writers are highly intentional about AI use, using it for scaffolding but preserving authentic voice through post-editing.*

12. Lee et al. (2024). "Homogenizing effect of LLMs on creative diversity — subordinate group bias." arXiv/Journal.
    - *Core finding: Subordinate social groups depicted with markedly higher narrative homogeneity in LLM generation.*

13. Ma et al. (2026). "Narrative Homogenization in LLM Fiction." arXiv:2603.14430.
    - *Core finding: LLMs exhibit fixed, repetitive plot paradigms with low narrative-function entropy — "hero-struggle-victory" templates across languages.*

14. Sui (2026). "Uncertainty-Aware Alignment for Productive Ambiguity." arXiv:2602.16162.
    - *Core finding: Current RLHF suppresses constructive ambiguity. Ambiguity-permissive reward models can re-inject productive unpredictability.*

15. Jiang et al. (2025). "Intra- and Inter-Model Creative Homogeneity." arXiv:2510.22954.
    - *Core finding: 79% of open-ended prompts yield intra-model similarity > 0.8. Human population variability dwarfs LLM variability.*

16. Uhlmann (2025). "The Kitsch Dynamic in LLM Creative Output." arXiv:2509.16794.
    - *Core finding: LLMs produce "kitsch" — what feels right rather than what is novel. Statistical centrality pulls outputs toward average rhetorical modes.*

17. Nguyen et al. (2025). "CreativeDC: Divergent-Convergent Decoupling for LLM Creativity." arXiv:2512.23601.
    - *Core finding: Without explicit divergent-convergent phase separation, LLMs conflate idea generation with immediate constraint satisfaction, pruning uncommon ideas.*

18. Rabeyah et al. (2024). "LLM Judges Agree With Each Other." arXiv:2411.15560.
    - *Core finding: LLM judges agree at Spearman ρ > 0.7, reinforcing homogenization in both creation and assessment.*

### Existing Research (Soul Repository)

19. Research: Creative Prompting (2026-06-02). `/research/research-creative-promping.md`
    - N-version gambit, persona-with-tension, genre transplant, constraint cage, break the fourth wall, collaboration loop

20. Research: Prompt Engineering for Creative AI Tasks (2026-05-31). `/research/research-prompt-engineering.md`
    - Positive vs negative constraints, few-shot examples, role assignment, CoT for evaluation

### Practitioner and Community Sources

21. "I tested 4 methods to make LLMs write literary subtext." Reddit r/PromptEngineering, 2025.
22. "Contrastive Prompting — Good vs Bad Examples." Quipoin Prompt Engineering Tutorial.
23. SillyTavern Character Card documentation and community practices.
24. "The Way of the Voice in AI Prompts — A Field Guide." Alen Peric, 2025.
25. "The Art of the Persona: A Masterclass in Tone-Adjusted Prompts for LLMs." Medium, 2026.

### EmergentMind Synthesis

26. "Creative Homogeneity in LLMs." EmergentMind, updated 1 May 2026.
    - Comprehensive synthesis of formal definitions, metrics, empirical manifestations, mechanistic sources, and mitigation strategies.
