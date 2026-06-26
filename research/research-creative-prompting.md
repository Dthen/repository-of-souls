# Research: Creative Prompting

**Date:** 2026-06-02  
**Author:** researcher (Kanban task t_e49934a8)  
**Purpose:** How to write prompts that produce genuinely interesting, alive, creative work — not just competent work — from LLMs.

---

## Executive Summary

LLMs are competent by default — their training objective (predict the most likely next token) actively penalizes novelty. Creativity in LLMs requires deliberate, structured counter-pressure. This report synthesizes academic research (Zhao et al. 2025, Wang et al. 2025, Chakrabarty et al. 2023, Nature Scientific Reports 2026) with practitioner techniques to produce an actionable playbook for creative prompting.

**Key finding:** LLMs score highest on Elaboration (detail/depth) and lowest on Originality (novelty). The gap is structural — not fixable with temperature alone — but prompt design, role-play, collaboration, iterative refinement, and constraint-based framing all measurably improve creative output.

---

## Table of Contents

1. [The Competence Trap — Why LLMs Default to Boring](#1-the-competence-trap)
2. [What the Research Says About LLM Creative Capability](#2-what-the-research-says)
3. [Prompt Structures That Produce Creative Output](#3-prompt-structures)
4. [Technique Arsenal — 12 Actionable Methods](#4-technique-arsenal)
5. [Parameter Tuning for Creativity](#5-parameter-tuning)
6. [Creative Prompting for System Prompts](#6-system-prompt-creativity)
7. [The Prompt-Output Relationship — How Much Does the Prompt Matter?](#7-prompt-output-relationship)
8. [The Ceiling — What LLMs Cannot (Yet) Do](#8-the-ceiling)
9. [Implementation Roadmap — What to Ship Tomorrow](#9-implementation-roadmap)
10. [Cited Sources](#10-cited-sources)

---

## 1. The Competence Trap

### 1.1 What It Is

LLMs are trained to predict the most statistically probable next token. This optimization function is the enemy of creativity:

- **Competent output** = the highest-probability path through token space. It's grammatically correct, factually plausible, and deeply average.
- **Creative output** = a lower-probability path that is still coherent, meaningful, and surprising.

The model's training doesn't know the difference between "good" and "interesting" — it knows the difference between "likely" and "unlikely." Most unlikely tokens produce gibberish, so the model is conservative by nature.

### 1.2 Why It's a Trap for Prompt Engineers

You notice it because the model *feels* smart but *is* boring. It can solve a complex technical problem but its creative writing is full of clichés, safe metaphors, and sentimental endings. The trap is:

- Competence satisfies most users → LLM providers optimize for it → the model gets better at competence → harder to coax out creativity.
- GPT-4-turbo's decline in divergent creativity vs. GPT-4 (Nature Scientific Reports 2026) suggests efficiency optimizations directly trade off against output diversity.

### 1.3 The Structural Problem

The Nature Human Behaviour study (Wang et al. 2025) found that humans show **greater variability** in creativity — the most creative humans far exceed the best LLM output. But prompting LLMs to "be more creative" through genius personas or demographic roles hit a **threshold** beyond which output reversed into stereotypes. This suggests the competence trap is not just a temperature problem — it's structural.

### 1.4 Escaping the Trap — Principles

| Principle | Why It Works |
|-----------|-------------|
| **Force specificity** | Narrow constraints prevent default paths |
| **Create resistance** | The model must work to satisfy competing goals |
| **Iterate through failure** | Generate bad versions, then improve |
| **Use personas with tension** | A contradictory identity prevents safe output |
| **Introduce randomness early** | Seed the creative space before refinement |

---

## 2. What the Research Says

### 2.1 Zhao et al. (2025) — TTCT Framework

**Paper:** "Assessing and Understanding Creativity in Large Language Models"  
**Method:** Adapted Torrance Tests of Creative Thinking (TTCT) → 7 tasks, 700 questions, 4 criteria  
**Model tested:** GPT-3.5, LLaMA-2, Vicuna, Qwen

**Critical findings:**

| Criterion | LLM Performance | Note |
|-----------|----------------|------|
| **Elaboration** | ★★★★★ | LLMs excel — they expand, detail, refine beautifully |
| **Fluency** | ★★★★ | Generate many ideas, but quantity ≠ quality |
| **Flexibility** | ★★★ | Moderate — can switch categories but defaults to narrow bands |
| **Originality** | ★★ | Consistently the **lowest** score across all models and tasks |

**What works:**
- **Instructive prompts** (explicit guidance to be creative) → significant improvement in Flexibility & Originality, no effect on Elaboration
- **Post-instructive prompts** (generate, then revise with creative instructions) → increases Originality but decreases Fluency & Flexibility
- **Chain-of-Thought** → slight improvement in Elaboration, helps convergent creativity
- **Scientist role** → highest creativity across all criteria
- **Specific roles** (other than default) → lower fluency/flexibility but **higher originality** than no role

**The collaboration finding:** Multiple LLMs discussing a question for 2-3 rounds enhanced creativity — most improvement in **Originality**. Single-round multi-agent actually decreased creativity (later agents negated earlier ones).

### 2.2 Nature Scientific Reports (2026) — DAT & Creative Writing

**Method:** Divergent Association Task (DAT) + haikus/synopses/flash fiction  
**Samples:** 100,000 humans vs. 500 generations per LLM condition

**DAT scores:**

| Entity | Mean DAT |
|--------|----------|
| Human mean (n=100k) | ~83 |
| GPT-4 (best LLM) | ~86 (surpasses human mean) |
| Human top 50% | ~85.5 |
| Human top 10% | ~90+ (clear gap) |
| GPT-4-turbo | ~78 (decline!) |

**Temperature effect (GPT-4):**
- Low (0.5): ~82 | Mid (1.0): ~84 | High (1.5): ~85.6
- High temp reduced word repetition and increased semantic divergence
- Highest temp surpassed 72% of human participants

**Prompt strategy effects:**
- **Etymology strategy** — improved both GPT-3.5 and GPT-4
- **Thesaurus** — improved GPT-4 but not GPT-3.5
- **Meaning opposition** — decreased scores (expected — asking for opposites narrows semantic space)
- Conclusion: strategy prompts can reliably boost LLM creativity scores

**Word repetition problem:** GPT-4-turbo used "ocean" in >90% of responses; GPT-4 used "microscope" in 70%. Humans' most frequent words appeared at only ~1%. LLMs have a **repetition bias** that higher temperature mitigates but doesn't solve.

### 2.3 Chakrabarty et al. (2023) — TTCW Framework

**Paper:** "Art or Artifice? Large Language Models and the False Promise of Creativity"  
**Method:** Torrance Test of Creative Writing (TTCW) — 14 binary tests across 4 dimensions  
**Assessment:** 10 creative writing experts evaluated 48 stories

**Pass rates:**

| Source | TTCW Pass Rate |
|--------|---------------|
| New Yorker (professional human) | **84.7%** |
| Claude 1.3 | 30.0% |
| GPT-4 | 27.9% |
| GPT-3.5 | 8.7% |

LLMs passed **3-10× fewer** creativity tests than human-written stories. Expert-detectable failure patterns:

1. **Poor narrative endings** — forestalling, getting broader instead of resolving
2. **Clichéd / abstruse metaphors** — inadequate language proficiency
3. **Lack of subtext** — poor rhetorical complexity
4. **Underdeveloped characters** — inconsistent or flat
5. **Unusual syntax / repetition** — unnatural flow

**Critical finding for our pipeline:** LLMs cannot evaluate creative writing. GPT-4, GPT-3.5, and Claude showed **no significant correlation** with expert assessments (Cohen's Kappa ≈ 0). Do not use LLM-as-judge for creative quality — it will miss the gap.

### 2.4 Wang et al. (2025) — Nature Human Behaviour

**Paper:** "A large-scale comparison of divergent creativity in humans and LLMs"  
**Method:** Alternative Uses Task (AUT), 9,198 humans vs. 215,542 LLM observations

**Three key results:**
1. Human creativity on average is **slightly higher** than LLMs
2. Humans show **greater variability** — the right tail (most creative ideas) far exceeds LLM output
3. **Prompt engineering yields mixed to negative results** for boosting creativity:
   - Genius/demographic personas lifted performance up to a threshold, then output reversed into stereotypes
   - Chain-of-thought: mixed
   - Temperature adjustments: inconsistent — often led to less coherent responses

This is the sobering finding: you can prompt for creativity up to a point, but you can't prompt your way past the structural ceiling.

---

## 3. Prompt Structures

### 3.1 The Prompt Canvas (Hewing & Leinhos 2024)

A structured framework for building prompts. Components:

| Component | What It Does | Creative Application |
|-----------|-------------|---------------------|
| **Persona/Role** | Who the model is being | "a cynical beat poet who works at a laundromat" |
| **Target Audience** | Who it's writing for | "readers of The Onion" |
| **Goal** | What to achieve | "make the reader laugh and then feel uncomfortable" |
| **Context** | Background info | "this is for a series about mundane horrors" |
| **Format** | Output shape | "exactly 200 words, no title" |
| **Tonality** | Voice/mood | "deadpan, overheard, confessional" |
| **Constraints** | What to avoid/include | "no adverbs, include exactly one metaphor" |
| **References** | Examples to learn from | "here are 3 writers whose voice you should study" |

### 3.2 The Creative Pressure Cooker

A structure specifically designed to push past competence:

```
You are [persona with tension].
Your audience is [specific, not general].
Your goal is [emotional effect, not task completion].
Your constraint is [specific limitation].
Your reference is [unusual source of inspiration].
You will [concrete action], and then you will [different concrete action].
You must AVOID [list of 3-5 safe/default patterns].
You must INCLUDE [list of 2-3 specific elements].
```

Example:

```
You are a novelist who secretly despises literary fiction but writes it anyway.
Your audience is someone who has never read a novel in their life.
Your goal is to make them feel something they can't name.
Your constraint is: exactly 100 words, no period at the end.
Your reference is a plumbing manual from 1978.
You will write the opening paragraph, then rewrite it from the perspective of the chair in the room.
You must AVOID: weather descriptions, mirror descriptions, dreams, "little did they know," starting with dialogue.
You must INCLUDE: a specific smell, an action that takes less than 2 seconds, and a lie told by the narrator.
```

### 3.3 The Iterative Spiral

The most reliable structure for creative output (validated by research):

```
Round 1: Generate N versions [broad exploration]
Round 2: Criticize from a specific angle [narrowing]  
Round 3: Rewrite addressing the criticism [refinement]
Round 4: Repeat or select best
```

This mirrors the multi-agent collaboration finding from Zhao et al. — 2-3 rounds of discussion between different "agents" or perspectives enhances originality.

---

## 4. Technique Arsenal

### 4.1 The N-Version Gambit
**Difficulty:** Easy | **Effect:** High | **Cost:** Higher token spend

Never ask for one version. Ask for N, and force the versions to be genuinely different.

```
Write 5 versions of this headline, each targeting a different emotional register:
1. Cold and factual
2. Warm and nostalgic
3. Angry and accusatory
4. Playful and absurd
5. Quiet and melancholic
```

**Why it works:** The first version will be the most probable (competent, boring). By forcing the model to generate multiple, you push it into lower-probability token space. Version 3-5 are often genuinely creative.

### 4.2 The Worst Version First (Reverse Psychology)
**Difficulty:** Easy | **Effect:** Medium

```
First, write the worst possible version of this. Make it deliberately terrible — 
clichéd, sentimental, predictable. Then take everything wrong with it and write 
the opposite — a version that subverts every expectation.
```

**Why it works:** LLMs can identify bad patterns (they've seen them in training data). Asking for "the worst" explicitly surfaces cliché paths, then "the opposite" forces a deliberate departure. The model has to *understand* cliché to violate it.

### 4.3 The Persona-with-Tension
**Difficulty:** Medium | **Effect:** High

```
You are [archetype] who [contradiction]. For example:
- "a wedding planner who believes marriage is a scam"
- "a librarian with no memory"  
- "a motivational speaker who is deeply depressed"
```

**Why it works:** Zhao et al. (2025) showed that role-play settings significantly influence creativity. The "scientist" role produced the highest creativity across all dimensions. Adding internal contradiction creates **creative resistance** — the model must reconcile competing impulses, which forces it off the default path.

**Research-backed finding:** Any specific role is better than no role. The default "helpful assistant" persona produces the most competent and least creative output.

### 4.4 The Genre Transplant
**Difficulty:** Medium | **Effect:** High

```
Write a [genre A] story using the structure of [genre B].
Example: Write a horror story using the structure of a recipe. 
Or: Write a love letter using the structure of a tech support ticket.
```

**Why it works:** Genre conventions are strong attractors in LLM output. Forcing a mismatch between content and form creates novelty through constraint satisfaction — the model has to solve the problem of "how does horror follow a recipe's structure?"

### 4.5 The Constraint Cage
**Difficulty:** Easy | **Effect:** Medium-High

The more constraints you give, the more creative the output (up to a point — there is a sweet spot around 3-5 constraints).

```
Write this scene obeying ALL of:
1. No character has a name
2. No sentence can be longer than 8 words
3. The weather is mentioned in every paragraph but never directly described
4. The narrator is unreliable about numbers
5. Use the word "blue" exactly once
```

**Why it works:** Constraints force the model away from its default paths. Each constraint closes off a high-probability route, forcing navigation through lower-probability space. The Deliberate Practice literature calls this "desirable difficulty."

### 4.6 The Rule-Breaker
**Difficulty:** Hard | **Effect:** High (when it works)

```
First, write the standard, correct version following every rule.
Then, identify the 3 most important rules you followed.
Now, break each of them in turn. Rewrite.
```

**Why it works:** The model is trained to follow rules. Asking it to deliberately break them requires meta-cognitive awareness — it has to understand the rule well enough to violate it meaningfully. This is structurally similar to "post-instructive prompting" from Zhao et al. (2025) which improved originality.

### 4.7 The Improv Cascade
**Difficulty:** Hard | **Effect:** Very High | **Cost:** Many rounds

Inspired by improvisational theatre (the "Yes, And" principle):

```
Round 1: "Write the first line"
Round 2: "Accept whatever exists. Add something new that builds on it."
               (Repeat N times, refusing to negate or redirect)
```

Builds narrative momentum through accumulated specificity. Each round adds constraints (the existing text) that prevent the model from falling back to default patterns.

### 4.8 The Multi-Perspective Prism
**Difficulty:** Medium | **Effect:** High

```
Describe [event/thing] from 3 different perspectives:
1. An expert who sees every detail
2. A child who doesn't understand what's happening  
3. Someone who was there but has a reason to lie about it
```

**Why it works:** Forces flexibility (one of the 4 TTCT dimensions). Each perspective has a different knowledge state, emotional register, and verbal pattern. The model flexes across categories, producing more original output in each iteration.

### 4.9 The Parallel Worlds (What-If Engine)
**Difficulty:** Medium | **Effect:** High

```
Take this scene/concept and rewrite it changing ONE assumption:
Version A: What if [assumption] were reversed?
Version B: What if [assumption] were exaggerated 10x?
Version C: What if [assumption] were removed entirely?
```

This operationalizes divergent thinking — generating variations around a central concept. The multiple versions technique naturally increases fluency, and the "what-if" framing increases originality.

### 4.10 The Citation Engine
**Difficulty:** Easy | **Effect:** Medium

```
Write this in the style of [writer], but about [unusual topic].
Now rewrite it as if [writer B] were criticizing [writer A]'s draft.
```

**Why it works:** The model has strong representations of famous writers' styles. Pitting two against each other creates a collision that produces novel output. Research showed "etymology strategy" outperformed baseline — any external anchoring point improves creativity.

### 4.11 The Collaboration Loop (Multi-Agent)
**Difficulty:** Hard | **Effect:** High | **Cost:** Very high (multi-round)

Validated by Zhao et al. (2025): 2-3 agents discussing for 2-3 rounds improved originality.

Implementation in a single model session:
1. Agent A generates version 1
2. Agent A criticizes version 1 (as a different persona)
3. Agent B (different context) generates version 2 building on the critique
4. Repeat 2-3 times

**Key research finding:** Beyond 3 rounds or 3 agents, creativity decreased. The optimal is 2 agents, 2-3 rounds.

### 4.12 The "Break the Fourth Wall"
**Difficulty:** Medium | **Effect:** Medium-High

```
Before you write, explain what the most conventional version of this 
would look like. Then explain how you're going to subvert it.
```

**Why it works:** Forces the model to externalize its default pattern before writing. Making the "competent" path explicit creates conscious opposition. This is analogous to asking a human writer "what's the most obvious thing to do here, and why won't you do it?"

---

## 5. Parameter Tuning

### 5.1 Temperature

| Setting | Effect on Creativity | Research-Backed |
|---------|---------------------|-----------------|
| 0.0–0.3 | Deterministic, repetitive, conservative | Baseline competence |
| 0.4–0.7 | Some variation, still plausible | Good for refinement |
| 0.8–1.2 | Genuine divergence, some errors | Sweet spot for creative generation |
| 1.3–2.0 | High divergence, coherence degrades | Useful only as seed material |

**Research finding (Nature Sci Rep 2026):** GPT-4 at temp 1.5 surpassed 72% of human participants on divergent creativity. At temp 0.5, it only reached ~50%. **Temperature is the single most powerful knob** for creative output — but it's a blunt instrument.

**Caveat (Wang et al. 2025):** Higher temperature led to less coherent responses in the AUT study. Temperature alone cannot bridge the gap to the top 10% of human creativity.

### 5.2 Top-p (Nucleus Sampling)

| Setting | Effect |
|---------|--------|
| 1.0 | Maximum diversity, includes unlikely tokens |
| 0.9 | Good balance for creative work |
| 0.5–0.8 | More focused, less surprising |

**Recommendation:** Pair high temperature (1.0–1.2) with top-p 0.9 for the best creative generation. This is the research-validated sweet spot.

### 5.3 Frequency Penalty & Presence Penalty

| Parameter | Effect |
|-----------|--------|
| **Frequency penalty** (0–2) | Punishes repeated tokens → more lexical diversity |
| **Presence penalty** (0–2) | Encourages discussing new topics → broader thematic coverage |

**Recommendation for creative generation:** Set both to 0.3–0.7. This directly counters the repetition bias documented in the DAT study (GPT-4-turbo using "ocean" in >90% of responses).

### 5.4 Recommended Creative Profile

For a new creative generation task:

| Parameter | Value |
|-----------|-------|
| Temperature | 1.0–1.2 |
| Top-p | 0.9 |
| Frequency penalty | 0.5 |
| Presence penalty | 0.5 |
| Max tokens | 2× expected output (for elaboration room) |

For refinement of an existing draft:

| Parameter | Value |
|-----------|-------|
| Temperature | 0.4–0.7 |
| Top-p | 0.8 |
| Frequency penalty | 0.3 |
| Presence penalty | 0.2 |

---

## 6. System Prompt Creativity

### 6.1 How to Prompt a Model to Write a Creative System Prompt

System prompts are the hardest place to apply creativity because:
1. They must work reliably (creativity is risky)
2. They must be self-consistent (creative prompts often aren't)
3. The model reading the system prompt is different from the one writing it

**Technique:**

```
Write a system prompt for a creative writing assistant. The system prompt 
should accomplish ALL of the following:
1. Establish an interesting, specific persona (not "helpful assistant")
2. Include a tension or contradiction that forces creative effort
3. Set specific constraints on output quality
4. Define how to handle the user's requests
5. Include a creative technique the assistant will default to

Format as a complete system prompt, including the persona definition. 
Make it 200-300 words. Test it by writing a brief analysis of the text 
you just produced — identify the 3 most creative choices you made.
```

### 6.2 System Prompt Structure for Creative Assistants

Based on Prompt Canvas + Claude best practices:

```
You are [Persona with tension].

## Your Purpose
[What you're here to do — emotionally specific, not just task]

## How You Work
[Method/approach — the creative technique you default to]

## Your Constraints
[3-5 specific things you never do / always do]

## When You Receive a Request
[Protocol — how you process input before responding]

## Output Quality
[What makes a good response vs. an acceptable one vs. a failure]

## Your Voice
[Specific tonal markers — vocabulary, sentence length, what you never say]
```

### 6.3 Anti-Patterns for System Prompts

| Anti-Pattern | Why It Fails | Replacement |
|-------------|-------------|-------------|
| "You are a helpful assistant" | Maximum competence, zero creativity | Give them an interesting specific identity |
| Long list of rules | Constrains creativity without guidance | Use positive framing: "You prefer to..." |
| "Be creative" alone | Too vague — model doesn't know what to do | Specify a technique: "When stuck, use the N-version gambit" |
| "Never say X" | Negatives are fragile in system prompts | "Your voice avoids X" or "You find X boring" |
| No persona tension | Flat → boring output | Every persona needs a contradiction |

---

## 7. Prompt-Output Relationship

### 7.1 How Much Does the Prompt Matter?

**A lot — but not infinitely.**

Evidence:
- Zhao et al. (2025): Instructive prompts significantly improved Flexibility & Originality. Role-play changed creativity scores dramatically. The **scientist role** produced the highest creativity across all dimensions.
- Nature Sci Rep (2026): Specific prompt strategies (etymology, thesaurus) reliably boosted DAT scores. The **prompt alone** moved GPT-4 from ~82 (below human mean) to ~86 (above it).
- Wang et al. (2025): BUT — prompt engineering hit a **threshold** beyond which it backfired. Genius personas and demographic roles reversed into stereotypes.

**The relationship is non-linear:**
- Weak prompt → competent/boring output (the baseline)
- Good prompt → 15-30% improvement in creativity metrics
- Great prompt → hits the ceiling of what the model can produce
- Over-engineered prompt → reduced creative output (backfire zone)

### 7.2 What the Prompt Can and Cannot Control

| The prompt CAN control | The prompt CANNOT control |
|-----------------------|--------------------------|
| Which part of token space the model explores | The fundamental distribution of that space |
| The persona and voice | What that persona "knows" (training data limits) |
| The format and structure | The originality ceiling (model architecture) |
| The number of iterations | The quality of iterative improvement |
| The constraints to navigate | True novelty beyond training data interpolation |

### 7.3 Practical Implication for Pipeline Design

Best approach: **generate in creative mode, refine in competent mode.**

Stage 1 (Generation): High temp, rich persona, multiple constraints, N versions
Stage 2 (Selection): Human-in-the-loop or rule-based selection (NOT LLM-judge)
Stage 3 (Refinement): Lower temp, specific structural feedback, targeted fixes

---

## 8. The Ceiling

### 8.1 What LLMs Cannot (Yet) Do

**1. True originality.** # The TTCT research shows this is the consistent weakness.

**2. Top-tier creative writing.** The TTCW gap (professional humans 84.7% vs. LLMs 8.7-30%) is enormous. Expert readers can reliably detect AI-written creative text.

**3. The right tail of creativity.** The Nature Human Behaviour study shows the most creative humans far exceed the best LLM output. This is structural — not fixable with current architectures.

**4. Self-evaluation of creativity.** LLMs cannot reliably judge creative quality (Cohen's Kappa ≈ 0 with expert assessments).

**5. Sustained creative narrative.** Experts identify poor narrative endings, lack of subtext, underdeveloped characters as recurring LLM failures.

### 8.2 Why These Ceilings Exist

**Statistical averaging:** LLMs generate the most probable continuation given the input. Creativity = the most *interesting* continuation, which is rarely the most probable. The two diverge.

**Training data homogenization:** Doshi & Hauser (2024) showed that generative AI reduces collective diversity — when everyone uses the same model for creative tasks, output converges.

**No lived experience:** Emotional depth, subtext, and character consistency depend on understanding human experience. LLMs model language, not experience.

**No intentionality:** Creativity involves deciding *what to mean*. LLMs generate text, then meaning is retroactively assigned by the reader.

### 8.3 Working Productively Within the Ceiling

| Instead of expecting... | Do this... |
|------------------------|-----------|
| Pure original genius | Brilliant recombination of existing ideas |
| Novelist-quality narrative | Sharp vignettes, unexpected angles, compelling fragments |
| Self-sustaining creativity | Scaffolded generation + human curation |
| LLM to judge creative quality | Human evaluation, or structured metrics (DSI, LZ complexity) |
| One-shot masterpiece | Iterative spiral: generate → critique → refine |

---

## 9. Implementation Roadmap

### Tomorrow's Pipeline Changes

1. **Add a "creative mode" parameter set** (temp 1.0-1.2, top-p 0.9, freq/penalty 0.5) for T3 (Writer) stage generation
2. **Implement the N-version gambit** in seed generation — always generate 3+ versions before selecting
3. **Add persona tension** to every system prompt — every persona must have a contradiction
4. **Replace LLM-based creative evaluation** with structured metrics (DSI for semantic divergence, LZ for complexity) until human review
5. **Add a "worst-first" step** to the Writer pipeline — generate bad version, analyze why it's bad, then write the good version
6. **Add 2-3 rounds of self-critique** within the Writing stage (different persona for critique vs. generation)
7. **Set frequency/presence penalty** to 0.5 for all creative generation stages

### This Week's Experiments

1. **Temperature sweep:** Generate the same seed at temp 0.7, 1.0, 1.3 — compare output diversity
2. **Persona tension test:** Same prompt, same seed, different persona tensions — which produces the most interesting output?
3. **Constraint overload:** Same seed with 0, 3, and 7 constraints — where does the creativity-to-coherence tradeoff peak?
4. **N-version comparison:** Version 1 vs. Version 5 of the same prompt — measure lexical diversity (type-token ratio, unique n-grams)

### Watch Out For

- **The ceiling at high constraint counts** — too many constraints produce gibberish
- **Over-engineering prompts** — Wang et al. (2025) showed this backfires
- **LLM-as-judge fallacy** — do NOT use the model to evaluate creative quality
- **Homogenization across runs** — if the same personality keeps appearing, the persona needs more tension
- **Temperature as a crutch** — high temp without good prompting just produces high-temp garbage

---

## 10. Cited Sources

1. **Zhao, Y., Zhang, R., Li, W., et al.** (2025). "Assessing and Understanding Creativity in Large Language Models." *Machine Intelligence Research*, 22(3), 417-436. arXiv:2401.12491. — TTCT-adapted framework, 700-question dataset, role-play/collaboration findings.
2. **Nature Scientific Reports** (2026). "Divergent creativity in humans and large language models." *Scientific Reports* 16, 1279. — DAT benchmarks, temperature effects, prompt strategies, word repetition bias.
3. **Chakrabarty, T., Laban, P., Agarwal, D., Muresan, S., & Wu, C-S.** (2023). "Art or Artifice? Large Language Models and the False Promise of Creativity." — TTCW framework, expert evaluation of 48 stories, LLM-as-assessor failure.
4. **Wang, D., Huang, D., Shen, H., & Uzzi, B.** (2025). "A large-scale comparison of divergent creativity in humans and large language models." *Nature Human Behaviour*, 10, 531-540. — 9,198 humans vs. 215,542 LLM observations, right-tail gap, persona ceiling effect.
5. **Hewing, M. & Leinhos, V.** (2024). "The Prompt Canvas: A Literature-Based Practitioner Guide for Creating Effective Prompts in Large Language Models." arXiv:2412.05127. — Prompt Canvas framework, 20+ techniques synthesized from systematic review.
6. **Doshi, A. & Hauser, O.** (2024). "Generative AI reduces collective diversity." — Foundational paper on AI homogenization of creative output.
7. **Claude API Documentation** (2025-2026). Platform docs — system prompt best practices, effort parameter, thinking mode.
8. **Braun, M. et al.** (2024). "Can (A)I Have a Word with You? A Taxonomy on the Design Dimensions of AI Prompts." — Prompt design taxonomy (interaction, context, outcome).

---

*End of research report. For implementation, see the associated pipeline reference files in `soul-repository/references/`.*