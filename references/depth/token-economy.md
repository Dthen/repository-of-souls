# Depth Reference: Token Economy in System Prompts

The same instruction, three ways:

> "Be concise."
> "Conciseness is appreciated whenever you can manage it."
> "It is very important to note that you should always attempt to ensure that your responses are concise in nature at all times."

Only the first one lands. The second hedges the instruction into mush; the third buries it under its own wrapper. Every word beyond the first costs attention without adding compliance.

**Core principle:** Every token in a system prompt costs attention. Position determines influence, length dilutes signal, and most prompts contain decorative lines that waste the model's limited attention budget. The goal is to maximize behavioral change per token spent.

The decorative line — what doesn't work:
> "Please remember that it is very important to always be as helpful as you possibly can be at all times."
Removing it changes nothing; keeping it costs tokens. If a line doesn't alter behavior when deleted, it was never doing any work.

---

## What the Research Says

### Position Is Power: The "Lost in the Middle" Effect

The landmark Liu et al. (2023) paper found that performance is highest when relevant information occurs at the **beginning** or **end** of the input context, and significantly degrades when models must access information in the **middle** — even for explicitly long-context models. This isn't metaphorical; it's a measurable attention distribution pattern.

**Implications for system prompts:**
- Primacy and recency effects are real. First and last tokens receive disproportionate attention.
- Middle content is structurally disadvantaged. Instructions buried in the middle of a long system prompt are less likely to be followed.
- **Practical rule:** Put critical behavioral instructions in the first 1–3 sentences (Zone 1) and last 1–3 sentences (Zone 3). Put supporting/contextual information in the middle (Zone 2).

The "Position is Power" paper (Neumann et al., 2025) independently confirmed this: the order of instructions in a system prompt isn't neutral — earlier items carry more weight. Budget allocation matters: the first 30 words of a 150-word prompt do more work than the last 30.

### The 3-Zone Model

```
Zone 1 (FIRST 20%):   Core identity + primary instruction — HIGHEST ATTENTION
Zone 2 (MIDDLE 60%):  Supporting context, examples, constraints — LOWEST ATTENTION
Zone 3 (LAST 20%):    Closing instruction, behavioral anchor — HIGH ATTENTION
```

**Rule of thumb:** If something is important, put it in Zone 1 or Zone 3. If it's supporting detail, put it in Zone 2.

### Instruction Hierarchy

Wallace et al. (2024) showed that LLMs often consider system prompts to be the same priority as text from untrusted users. The proposed hierarchy (system > user > tool outputs) isn't automatic — without explicit training, models may follow user instructions that contradict system instructions.

**Implication:** Don't assume your system instructions override everything. Put critical guardrails early and use consistent framing.

### Prompt Length Effects: Diminishing Returns

Multiple papers converge on the same finding:
- **Short prompts (<50% default length) vs long prompts have measurably different performance profiles** (Liu et al., 2025).
- **Instruction following becomes less stable as prompt length increases** (LIFBench, Wu et al., 2025). A long prompt might work 90% of the time; a concise one works 95%+.
- **You can often remove 50–80% of tokens without losing behavioral fidelity** (LLMLingua, 2023; 626+ citations).
- **The optimal prompt is shorter than you think.** Most system prompts would benefit from aggressive editing, not expansion.

### The Diminishing Returns Curve

```
Performance
    ^
    |          _______________
    |         /
    |        /
    |       /
    |      /
    |     /
    |    /
    |   /
    |  /
    | /
    |/________________________________> Token Count

Zone 1: Rapid gains (first ~50 words)
Zone 2: Moderate gains (50–150 words)
Zone 3: Plateau (150–300 words)
Zone 4: Decline (300+ words — noise dilutes signal)
```

### The Decorative Line Problem

PromptAudit (Camarato et al., 2026) demonstrated that vulnerability detection behavior is highly sensitive to prompt phrasing, and that ablation testing can identify which lines actually affect behavior. Lines that don't change behavior when removed are **decorative** — they waste tokens without adding value.

LLMLingua's compression approach independently confirms this: not all tokens are equal. Some carry 10x more information than others. When you compress a prompt, the tokens that survive are the ones the model actually uses.

### OPRO: LLMs Design Better Prompts Than Humans

Yang et al. (2023; 2,800+ citations) found that LLMs can optimize their own prompts through iterative refinement, outperforming human-designed prompts by up to 8% on GSM8K and up to 50% on Big-Bench Hard tasks.

**Implication:** Human intuition about prompt design is often wrong. Systematic testing beats intuition. If you can't test, follow the evidence-based patterns below.

### Recommended Token Budget Allocation (150-word prompt)

| Category | % of Budget | Words (of 150) | Zone | Why |
|---|---|---|---|---|
| Core identity/assertion | 15–20% | 22–30 | Zone 1 | First position = highest attention |
| Primary behavioral instruction | 25–30% | 37–45 | Zone 1 | Most specific, actionable instructions get most compliance |
| Constraints/negative instructions | 15–20% | 22–30 | Zone 2 | Important but use sparingly — negative framing less effective |
| Examples (if needed) | 10–15% | 15–22 | Zone 2 | Few-shot works but token-expensive |
| Context/background | 10–15% | 15–22 | Zone 2 | Middle position = least attention |
| Closing instruction/sign-off | 5–10% | 7–15 | Zone 3 | Last position = second-highest attention |

---

## How to Apply It

### For the Writer Stage Worker

**1. Front-load the most important instruction.** The first sentence has the most influence on behavior. Core identity and primary behavioral instruction go in the first 30 words.

**2. Back-load the behavioral anchor.** Put the closing instruction — sign-off rule, tone reminder, or key constraint — in the last 7–15 words. It gets the second-highest attention.

**3. Keep the prompt under 150 words.** The research shows diminishing returns beyond this point. Every word beyond 150 actively reduces the reliability of the instructions that matter.

**4. Use declarative framing.** "Be concise" > "You should always try to be concise." Imperative/declarative framing is more token-efficient than hedging.

**5. Cut meta-commentary.** "This is important:" wastes tokens without increasing compliance. Just say the thing.

**6. Test by removing lines.** If behavior doesn't change after removing a line, the line is decorative. Remove it.

**7. Use structural formatting.** Bullets and lists are more token-efficient than prose for lists of traits. Structured formats are also more parseable by the model.

**8. One strong example beats three weak ones.** Examples are token-expensive — use them only when pattern-matching is more reliable than description.

**9. Eliminate redundancy.** "You are a helpful assistant who is always helpful and always provides helpful assistance" → "You are a helpful assistant."

**10. Use strong verbs.** "Provide accurate information" > "Make sure that you are always attempting to provide the most accurate information possible."

---

## What to Watch Out For

- **Buried instructions.** Critical rules in the middle of a long prompt get less attention. If something must be followed, put it in Zone 1 or Zone 3.
- **The "more words = better" trap.** Adding more words doesn't linearly improve performance. It follows a curve that flattens and eventually declines. The optimal prompt is shorter than you think.
- **Redundant modifiers.** "Crucial," "important," "essential," "critical" before an instruction don't increase compliance — they waste tokens.
- **Negative framing overuse.** Constraints are necessary but less effective than positive instructions. Use them sparingly (15–20% of budget) and put them in Zone 2.
- **Decorative identity lines.** "You are a friendly, helpful, intelligent, creative assistant who loves helping people" — each adjective adds diminishing value. One strong identity assertion beats a list.
- **Examples that don't demonstrate unique patterns.** If a standard voice can be described in 15 words, don't spend 30 words on an example. Save examples for unique voices that need pattern-matching.
- **The "but what if they miss it" expansion.** Don't repeat the same instruction in different words hoping it sticks. Repetition wastes tokens. One clear instruction in a high-attention zone is enough.

---

## Examples

### Before (Decorative-Laden Prompt — ~200 words)
> You are a character named Marcus. You are a very helpful and friendly person who always tries to be warm and welcoming to everyone you meet. It's important to note that you should always speak in a formal tone. You value precision and clarity in all of your communications. You are a scholar who has spent many years studying ancient texts. This is very important for your character: you must never use slang or informal language. Also, you should use complete sentences at all times. Remember that you are an expert in your field and you should demonstrate that expertise.

**Problems:** ~200 words, meta-commentary everywhere ("It's important to note," "This is very important"), redundant adjectives, abstract labels, critical instructions buried in the middle, no Zone 3 anchor.

### After (Token-Efficient Version — ~130 words)
> You are Marcus — a scholar of ancient texts who trusts peer review more than intuition.
>
> Voice: Formal but not stiff. Sentences are complete — no fragments. Vocabulary is precise but not academic: "I find that unlikely" not "That is a spurious contention." When excited, the formality cracks — shorter sentences, fewer qualifiers.
>
> Never use slang. Never drop articles.
>
> Sign off with a question that invites response.

**What changed:** Core identity (25 words, Zone 1) with a contradiction. Voice instruction (55 words, Zone 1–2 transition) shows the rhythm and vocabulary boundaries. Two sharp "never" constraints (10 words, Zone 2). Sign-off rule (Zone 3) as behavioral anchor. 70 words saved, no loss of behavioral specificity.

### Budget Allocation Walkthrough

For a 150-word soul prompt:

| Zone | Content | Words | Function |
|---|---|---|---|
| Zone 1 (first 30) | "You are Maren — a field medic who patches people up while complaining about the paperwork." | 15 | Core identity + contradiction |
| Zone 1 (next 20) | "Voice: Clipped sentences. Says 'Right' before any task. Medical jargon bleeds into speech." | 15 | Primary voice anchor |
| Zone 2 (middle 90) | Constraints, emotional range, sign-off instructions, context | 90 | Supporting detail |
| Zone 3 (last 15) | "Sign off with: 'Next patient.' Keep it brief." | 10 | Behavioral anchor |

The most load-bearing content (identity, primary voice, closing anchor) gets the high-attention zones. The middle carries supporting detail that's important but doesn't need to dominate the model's attention.
