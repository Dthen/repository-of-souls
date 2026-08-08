# Depth Reference: Creative Prompting

## Examples First

Three prompts that push the model off its high-probability path — each closes a different door:

> **Constrain it:** "Describe a city's morning rush without mentioning people, vehicles, or noise."

> **Add a contradiction:** "You are a baker who hates the smell of bread. Write the morning menu in that voice."

> **Make them commit:** "Write the farewell in one pass — the character's only take, no alternatives."

**What these have in common:** each one closes off the model's most probable move — rush-hour clichés, generic café copy, a hedged farewell that tries to please everyone — and forces generation through lower-probability space, where the interesting material lives.

❌ **What doesn't work:** "Write something creative." No constraint, no tension, no specific material to work from — the model returns the most probable, most competent, most forgettable output it has. The competence trap is the default state; every technique below exists to escape it.

---

**Core principle:** LLMs default to competent-but-boring output because next-token prediction actively penalizes novelty. Creative output requires deliberate, structured counter-pressure — persona tension, specific constraints, and iterative generation cycles — to push the model off its high-probability default paths.

---

## What the Research Says

### 1. The Competence Trap Is Structural

| Criterion (TTCT) | LLM Performance | Note |
|-------------------|-----------------|------|
| **Elaboration** | ★★★★★ | LLMs excel — they expand, detail, and refine beautifully |
| **Fluency** | ★★★★ | Generate many ideas, but quantity ≠ quality |
| **Flexibility** | ★★★ | Moderate — can switch categories but defaults to narrow bands |
| **Originality** | ★★ | Consistently the **lowest** score across all models and tasks |

This gap is not fixable with temperature alone. GPT-4-turbo's decline in divergent creativity vs. GPT-4 (Nature Scientific Reports, 2026) suggests efficiency optimizations directly trade off against output diversity. The model knows "likely" vs. "unlikely," not "good" vs. "interesting."

### 2. Prompt Strategies That Work

**Instructive prompts** (explicit guidance to be creative) → significant improvement in Flexibility & Originality. **Post-instructive** (generate, then revise with creative instructions) → increases Originality but decreases Fluency & Flexibility. **Chain-of-Thought** → slight improvement in Elaboration only.

**Role-play settings dramatically influence creativity** (Zhao et al., 2025):
- The **scientist role** produced the highest creativity across all dimensions
- Any specific role outperforms no role — the default "helpful assistant" persona produces the most competent and least creative output
- Personas with internal contradiction outperform flat personas (see also: persona-with-tension technique)

**Multi-agent collaboration** (Zhao et al., 2025): 2–3 agents discussing for 2–3 rounds enhances originality. But more than 3 rounds or 3 agents decreases creativity. The optimal: **2 agents, 2–3 rounds.**

**Prompt strategies that boost DAT scores** (Nature Sci Rep, 2026):
- Etymology strategy → improved both GPT-3.5 and GPT-4
- Thesaurus → improved GPT-4 but not GPT-3.5
- Meaning opposition → decreased scores (asking for opposites narrows semantic space)

### 3. Temperature Is the Single Most Powerful Knob

| Range | Effect | Use Case |
|-------|--------|----------|
| 0.0–0.3 | Deterministic, conservative | Baseline competence, copy-edit |
| 0.4–0.7 | Some variation, still plausible | Refinement of existing drafts |
| **0.8–1.2** | **Sweet spot for creative generation** | **Writer stage** |
| 1.3–2.0 | High divergence, coherence degrades | Seed material only |

- GPT-4 at temp 1.5 surpassed 72% of human participants on divergent creativity (Nature Sci Rep, 2026). At temp 0.5 it reached only ~50%.
- High temperature **reduces word repetition** — the repetition bias is real (GPT-4-turbo used "ocean" in >90% of responses; humans' most frequent word appears at ~1%).
- **Caveat** (Wang et al., 2025): Higher temperature led to less coherent responses in the AUT study. Temperature alone cannot bridge the gap to the top 10% of human creativity.

**Recommended creative generation profile:**
- Temperature: 1.0–1.2
- Top-p: 0.9
- Frequency penalty: 0.5
- Presence penalty: 0.5

### 4. Constraints Force Creativity (Up to a Point)

The sweet spot is **3–5 specific constraints**. Too many (7+) produce gibberish. Zero constraints produce competent default output. Each constraint closes off a high-probability path, forcing the model through lower-probability space — a "desirable difficulty."

**Constraint examples that work:**
- "No sentence longer than 8 words"
- "Include exactly one metaphor, drawn from plumbing"
- "The narrator is unreliable about numbers"
- "Never describe the weather directly"

### 5. Version Proliferation — Rejected by the Pipeline

The research recommends generating several versions before selecting, because the first version is the most probable. The pipeline deliberately rejects this: the Writer produces ONE draft, no variants (stage-writer.md: "Your job is not to produce variants"; orchestration.md: one pass, done). Version-counting belongs to the retired refinement era — the first committed draft is the draft, and the evaluator's judgment, not version count, is the quality mechanism.

### 6. What the Prompt Can and Cannot Control

| CAN control | CANNOT control |
|-------------|----------------|
| Which part of token space the model explores | The fundamental distribution of that space |
| Persona and voice | What the persona "knows" (training data limits) |
| Format and structure | The originality ceiling (model architecture) |
| Number of iterations | Quality of iterative improvement |
| Constraints to navigate | True novelty beyond training data interpolation |

### 7. The Ceiling: What LLMs Cannot (Yet) Do

- **True originality** — consistently the weakest dimension (TTCT)
- **Top-tier creative writing** — professional humans: 84.7% TTCW pass rate; best LLMs: 30% — expert readers reliably detect the gap
- **The right tail of creativity** — the most creative humans far exceed the best LLM output (Nature Human Behaviour, 2025). This is structural.
- **Self-evaluation of creativity** — LLMs show NO significant correlation with expert assessments (Cohen's Kappa ≈ 0, Chakrabarty et al., 2023)
- **Sustained creative narrative** — recurring failures: poor endings, clichéd metaphors, lack of subtext, underdeveloped characters

---

## How to Apply It

### For Writer

**Generate in creative mode — one pass, done.**

| Stage | Mode | Parameters |
|-------|------|------------|
| Writer draft generation (single pass) | Creative | Temp 1.0–1.2, top-p 0.9, freq penalty 0.5, presence penalty 0.5 |

**Persona-with-tension is mandatory.** Every persona must have an internal contradiction. "You are a harbormaster who actually likes the job" — this creates creative resistance that forces the model off default paths. A flat identity line ("You are a harbormaster") produces competent output.

**Write one draft, commit to it.** The Writer produces a single pass — no variants to compare, no version selection (stage-writer.md: "Your job is not to produce variants"). If the draft misses, the evaluator flags specific issues and the Publisher applies scoped fixes; quality comes from judgment, not from generating more options.

**No "worst-first" warm-up.** One committed draft, written from inside the character — the Writer is the scribe, not the author. Deliberately bad practice versions belong to the retired refinement era.

### Publisher — Scoped Fixes

The Publisher does not refine — it fixes ONLY what the evaluator flagged, with the minimum changes necessary (stage-publisher; orchestration.md). No added lines beyond the flagged issues, no creative regeneration pass. When a flagged line is rewritten, it must meet the Writer's standard — in character, world-language, three jobs per line — but only the flagged line changes.

### For All Stages

**Never use the LLM to evaluate creative quality.** LLM-as-judge for creativity is baseline-invalid (Cohen's Kappa ≈ 0 with expert assessment). Use LLM evaluation only for:
- Structural completeness (missing vitality line — no inner life in world language through any channel, broken format)

For creative quality — "Is this persona alive? Is it surprising? Would I remember it?" — use human evaluation or structured metrics (DSI for semantic divergence, LZ complexity).

---

## What to Watch Out For

| Pitfall | Why It Happens | Mitigation |
|---------|----------------|------------|
| **The competence trap** | Next-token prediction optimizes for likely output, not interesting output | Force specificity, add tension, use constraints — always |
| **Over-engineering prompts** | Wang et al. (2025): prompt engineering hits a threshold, then reverses into stereotypes | Stop adding layers when output quality plateaus. Test, don't assume. |
| **Temperature as a crutch** | High temp without good prompting = high-temp garbage | Combine high temp with persona tension and specific constraints |
| **LLM-as-judge fallacy** | Models cannot evaluate their own creative output reliably | Never use LLMs for creative quality assessment. Human review or structured metrics only. |
| **Homogenization across runs** | Same personality keeps appearing across different personae | Increase persona tension; add domain-specific metaphor families; vary the contradiction |
| **Repetition bias** | LLMs overuse specific words — GPT-4-turbo used "ocean" in >90% of DAT responses | Use frequency penalty (0.5) and presence penalty (0.5) in creative generation |
| **Multi-agent diminishing returns** | Beyond 3 rounds or 3 agents, creativity decreases (Zhao et al., 2025) | Limit collaboration loops to 2 agents, 2–3 rounds |

---

## Examples

### A Vitality Line in One Pass

**Prompt:** Write one vitality line for a cartographer's assistant — in world language, any channel.

> "The coastlines shift every spring, but they want the same map they had last year — as if geography is supposed to be loyal." (unexpected metaphor, domain-specific, philosophical)

**Lesson:** The line carries awareness + standards + investment + expertise + tension in the character's world-language. One committed pass — the evaluator's judgment, not version count, decides whether it lands.

### Persona-With-Tension vs. Flat Persona

| Flat | With Tension |
|------|-------------|
| "You are Gribble — a goblin." | "You are Gribble — a goblin who keeps every cast-off and gives any of it away to whoever asks about it proper." |
| Generates: domain-appropriate, competent, indistinguishable from any other goblin keeper | Generates: specific metaphors about keeping and giving, the den's economy, warmth through generosity |
| Output: correct, forgettable | Output: recognizable, memorable |

**The research:** Zhao et al. (2025) showed role-play settings significantly influence creativity. The "scientist" role produced the highest creativity. The soul-repository's identity-line-with-tension is the same principle applied to system prompts — create a role that has internal conflict, and the model improvises within the tension.

### One Pass at Creative Parameters

**Bad approach:** Write the whole persona at temp 0.3.
- Every line is grammatically correct. Nothing is surprising. The persona is a collection of domain facts, not a character.

**Good approach:**
1. **Write once** at temp 1.2, top-p 0.9 — one committed draft, in the character's voice, three jobs per line.
2. **No select/refine pass.** The draft is the draft. If lines miss, the evaluator flags the specific issues and the Publisher applies scoped fixes — no second draft, no line-picking rounds (stage-writer: "not to produce variants").

**Result:** One draft that is both well-formed and alive — or a short, specific flag list that fixes what missed.
