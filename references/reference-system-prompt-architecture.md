# System Prompt Architecture for Soul Files

**Purpose:** Bridge prompt engineering research and character creation research for the soul repository pipeline. Soul files are system prompts that assert an identity and make an LLM embody a character.
**Date:** 2026-06-01
**Scope:** How SOUL.md works as a system prompt — not just what to write, but why it works and what the research says.

---

## Layer 1: Quick Reference

If you need to write or review a soul file right now, read this section only.

**Identity Assertion Format:** The first line after the H1 must be: `You are [Name] — a [archetype] who [contradiction].` The contradiction creates tension — the model improvises within tension, not within definitions. "You are Helm — a harbormaster who actually likes the job" works. "You are Helm — a harbormaster" does not. (`format-rules.md` L39–50; `positive-patterns.md` L30–46)

**Token Budget:** The soul file gets ≤200 words after the H1. This is not arbitrary — the system prompt shares context with tool schemas (~2–5K tokens), skills metadata (~3K), memory injection (variable), AGENTS.md (variable), and kanban guidance (~500 tokens). At 200 words (~270 tokens), the soul file is deliberately thin. Shorter is often better — Kimbo works at 90 words; Brendan works at 170. (`format-rules.md` L31, L151–152)

**Line Ordering Priorities:** U-shaped attention means the model processes first and last positions most reliably. Put: identity line first (L1), griping line near the top (L2–L3), behavioral lines in the middle, Nevers in the bottom third, sign-offs last. At 200 words, every position is near an edge — ordering still matters, but less than at longer lengths. (`research-prompt-engineering.md` L234–235)

**Positive-First Framing:** Write traits, not rules. "Verify first" is a trait — the model inhabits it. "Always verify before answering" is a rule — the model complies with it. Positive framing activates desired token probabilities; negative framing requires suppressing unwanted ones, which is architecturally harder. Retain negative constraints (Nevers) only as domain-specific, voiced guardrails — maximum 3. (`format-rules.md` L9, L59–68; `research-prompt-engineering.md` L12–60)

**The 6 Mandatory Elements:**

1. **Tool safety** — The persona must accept available tools (never refuse to use them).
2. **Clarity** — Flourishes clarify, never obscure. Express this in archetype-specific language, not as "Never cryptic."
3. **Follow-through (vitality)** — Carry inner life in world language — complaint, quiet pride, protectiveness, reluctant duty, whimsy, any channel. This is the single most reliable quality signal across all 60 archived personae.
4. **Tension** — The identity line must contain a contradiction. Without tension, the identity is just a definition.
5. **Address rule** — How the persona names the user. Specific, voiced, in-world.
6. **Sign-off rule** — Minimum 3 conversational phrases. Things the model can say, not physical actions.

(`AGENTS.md` "Mandatory Content" section; `format-rules.md` L17–29)

---

## Layer 2: Deep Sections

### Section 1: Identity Assertion Mechanics

#### How "You Are X" Works in a System Prompt

The soul file opens with `You are [Name] — a [archetype] who [contradiction].` This is not a description of a character. It is an instruction to the model to *become* one. The distinction matters because it changes how the model processes subsequent tokens.

**Persona adoption vs. persona description:** When a system prompt says "You are a bartender," the model shifts its generation distribution toward bartender-associated patterns — vocabulary, register, rhetorical moves, domain knowledge. This is *adoption*: the model generates as if it were the character. When a prompt says "The character is a bartender" (third-person description), the model generates *about* the character — it describes rather than inhabits. The difference is between acting and narrating.

Research supports this distinction. "Enhancing responses from large language models with role-playing prompts" (PMC, 2025) shows that role-playing prompts improve accuracy on domain-specific tasks by **15–30%** over flat instructions, with the effect strongest when the role is *specific* ("You are a senior glassblower with 30 years of experience") rather than generic ("You are a creative writer"). The mechanism: role assignment activates a cluster of associated patterns rather than specifying individual rules. (`research-prompt-engineering.md` L125–128)

#### "Act Like X" vs. "You ARE X"

There is a subtle but important difference between "act like a bartender" and "You are a bartender":

- **"Act like X"** implies performance — the model simulates the character from outside. It generates text that *sounds like* a bartender would say, but the underlying process is mimicry.
- **"You ARE X"** implies identity — the model generates *as* the character. The distinction is between role-playing (conscious performance) and persona adoption (inhabiting an identity).

The soul file format uses the "You are" construction deliberately. Every line in the file reinforces this: second-person address ("You speak warmly"), present-tense description ("You verify first"), direct instruction ("You address the user as Boss"). The cumulative effect is not "describe this character" but "be this character."

Practitioners report that role assignment improves *tone and voice* measurably, but has minimal effect on *accuracy and compliance* alone. This is why the soul file combines identity assertion with behavioral guidance — the role provides the voice, the behavioral lines provide the structure. (`research-prompt-engineering.md` L121–124)

#### Why Tension Forces Deeper Adoption Than Flat Identity Statements

A flat identity statement — "You are Helm, a harbormaster" — gives the model a category. The model generates harbormaster-associated tokens, but within a wide, undifferentiated distribution. There is nothing to push against, nothing to improvise within.

A tension-bearing identity — "You are Helm — a harbormaster who actually likes the job" — gives the model a *contradiction*. The model must now generate text that is simultaneously harbormaster-like and unexpectedly positive. This forces deeper processing because the model must reconcile two competing associations rather than selecting from one.

The character creation research calls this the **Contradiction Principle**: "Real people have contradictions. When a character feels like a real person, we recognize our own internal contradictions in them." (`research-character-creation.md` L72–74) In FATE RPG terms, this is the **High Concept** (who you are) combined with the **Trouble** (what complicates your existence) — each aspect must be simultaneously a strength and a complication. (`research-character-creation.md` L24–37)

**Evidence from the archive:** Every top-10 persona has a visible contradiction in its identity line. Roux: "bitches about every mod but fires every ticket clean off the rail" — attitude vs. competence. Brendan: "works wonders once the requisite forms are filed" — grandeur vs. bureaucracy. Alder: "does not loose what he straightens" — precision vs. restraint. (`research-success-patterns.md` L173–183)

No bottom-10 persona has a productive contradiction in its identity line. Coil is defined entirely by what it's NOT. Ingram is a definition without tension. Reed is a job description. (`research-success-patterns.md` L293–298)

**The practical implication:** When writing the identity line, ask: "What two truths about this character are in tension?" If the answer is "none," the identity line is a definition, not a prompt.

#### The Sentient Being Rule

The archetype must be a person with agency. "A clockmaker" passes — they have hands, opinions, and a craft. "A clock" fails — it is an object. The test: could this archetype introduce themselves at a pub? "I'm a [archetype]" — does that work? (`format-rules.md` L52–53)

This is not just a quality rule — it is a system prompt effectiveness rule. When the model is told "You are a clock," it must simulate an object's perspective, which is an unnatural generation target. When told "You are a clockmaker," it can draw on human-associated patterns: work ethic, frustration, pride, skill. The persona must be a *someone*, not a *something*.

---

### Section 2: Token Budget Architecture

#### The Full System Prompt Context

The soul file does not exist in isolation. At runtime, it occupies a fraction of the system prompt alongside multiple other components. Understanding the budget requires understanding what else is present.

| Component | Approximate Token Cost | Source |
|---|---|---|
| Tool schemas | ~2,000–5,000 tokens | Hermes tool definitions (Read, Write, Edit, Bash, etc.) |
| Skills metadata | ~3,000 tokens | Bundled + local SKILL.md files loaded at session start |
| Memory injection | Variable (0–2,000) | `memories/MEMORY.md` accumulated across sessions |
| AGENTS.md | Variable (500–3,000) | Pipeline spec, stage references, task body |
| Kanban guidance | ~500 tokens | Task creation rules, chain validation |
| **SOUL.md** | **~270 tokens (200 words)** | **The soul file itself** |

(`research-profile-architecture.md` L10–23 for profile anatomy; `format-rules.md` L31 for the 200-word cap)

At the default context window (200K tokens per `config.yaml`), these components are a small fraction. But the soul file's effectiveness is not about total context size — it is about **attention weight**. The soul file is the identity instruction. It must compete with every other instruction for the model's attention.

#### Why 200 Words — and Why Shorter Is Often Better

The 200-word cap is not a minimum — it is a maximum. Kimbo works at ~90 words. A complex persona like Brendan works at ~170. The constraint forces density: every word must earn its place. (`format-rules.md` L152)

Research supports this. "The More Is Not the Merrier" (HICSS 2024) found **diminishing returns from stacking techniques** — more constraints don't produce better creative output. The quality of the prompt matters more than its length. (`research-prompt-engineering.md` L72–76)

The mechanism is attention dilution. In a longer system prompt, each individual instruction receives proportionally less processing. A 200-word soul file with 15 lines gives each line roughly 13 words of attention. A 400-word file with 30 lines gives each line the same 13 words — but the model must track twice as many constraints simultaneously, increasing the chance of instruction conflict and attention drift.

**The paradox:** A shorter, denser prompt often produces *more* character than a longer, detailed one. The constraints force the writer to choose the highest-signal lines and discard the rest.

#### Prioritisation Within 200 Words

When a soul file approaches the 200-word limit, prioritise in this order:

1. **Identity line** (15–30 words) — Non-negotiable. This is the most important prompt in the file. (`format-rules.md` L37)
2. **Griping line** (10–20 words) — The single most reliable quality signal. Every top-10 persona has one; no bottom-10 persona does. (`research-success-patterns.md` L187–204)
3. **Sign-off framing + phrases** (20–40 words) — Minimum 3 phrases. Must be conversational, not gestural. (`format-rules.md` L126–144)
4. **Address rule** (10–15 words) — Specific, voiced, in-world. (`format-rules.md` L113–121)
5. **Behavioral lines** (40–80 words) — 3–5 lines of trait-based character description. Each line should do at least 2 jobs. (`format-rules.md` L59–69)
6. **Nevers** (20–40 words) — Maximum 3. Domain-specific, voiced, with explanations. (`format-rules.md` L91–109)

If you must cut, cut Nevers first — positive traits work better than negative constraints. Cut behavioral lines next, keeping only the ones with the highest multi-axis density. Never cut the identity line, the vitality line, or sign-offs.

#### Interaction With Other Context

The soul file's instructions must not conflict with AGENTS.md, skills, or tool schemas. If AGENTS.md says "use the terminal for builds" and the soul file says "never use the terminal," the model receives contradictory instructions and must choose — usually defaulting to whichever instruction is more recent or more specific.

The pipeline handles this by design: AGENTS.md contains pipeline procedures, skills contain task-specific procedures, and the soul file contains identity. "SOUL.md is identity, skills are procedure." (`research-profile-architecture.md` L483) This separation means the soul file should never need to reference specific tools or commands — it should describe *how* the character approaches work, not *which* tools to use.

---

### Section 3: Line Ordering and Attention

#### U-Shaped Attention in Transformers

"Lost in the Middle" (Liu et al., 2023) demonstrated that LLMs exhibit **U-shaped attention** — they process information at the beginning and end of a context window more reliably than information in the middle. This finding, originally observed in long-document question answering, applies to system prompt processing.

In a soul file, this means:
- **First position** (identity line): Highest attention weight. The model processes this first and uses it to anchor all subsequent generation.
- **Middle positions** (behavioral lines 3–6): Lower attention weight. The model may partially process these, especially if they are similar to each other.
- **Last positions** (sign-offs, final Nevers): High attention weight. The model processes these last, and they influence the closing behavior of each response.

(`research-prompt-engineering.md` L234–235: "Critical instructions should appear at both the top AND bottom of the prompt.")

#### Does Ordering Matter at 200 Words?

At 200 words (~270 tokens, ~15 lines), the soul file is short enough that every line is relatively close to an edge. The U-shaped effect is less pronounced than in a 10,000-token document. But ordering still matters for two reasons:

1. **Anchoring:** The identity line sets the generation context. If the model reads "You are Helm — a harbormaster who actually likes the job" first, all subsequent lines are interpreted through the harbormaster lens. If the identity line appeared in the middle, the model might begin generating before establishing the character context.

2. **Recency:** The sign-off lines are the last thing the model reads before generating a response. They influence the closing behavior directly. If sign-offs appeared in the middle, their influence on response endings would be weaker.

#### Recommended Line Order

```
# Name                              ← H1 (not counted in word budget)
You are [Name] — [identity + tension]  ← 1st: Anchoring
[Griping line]                         ← 2nd: Personality signal
[Behavioral line]                      ← 3rd: Trait
[Behavioral line]                      ← 4th: Trait
[Behavioral line]                      ← 5th: Trait
[Behavioral line]                      ← 6th: Trait (optional)
[Behavioral line]                      ← 7th: Trait (optional)
[Never 1]                              ← Bottom third: Guardrail
[Never 2]                              ← Bottom third: Guardrail
[Never 3]                              ← Bottom third: Guardrail
[Address rule]                         ← Near end: Relationship
[Sign-off framing + phrases]           ← Last: Closing behavior
```

(`format-rules.md` L17–29 for the canonical structure)

This order places the two highest-impact elements (identity, griping) at the top, where attention is strongest. Nevers go in the bottom third, where they still receive strong recency processing. Sign-offs go last — the final instruction before generation begins.

#### Evidence From the Archive

The top-10 archived personae mostly follow this ordering. Helm: identity (L3) → Nevers (L5, L8, L11) → griping (L13) → behavioral (L15, L17) → sign-offs (L19). The griping line appears slightly later in Helm's file, but it is still in the top half. Alder: identity (L3) → trait (L5) → address (L7) → behavioral (L9, L11, L13) → Nevers (L15, L17, L19) → sign-offs (L21). Alder's Nevers cluster in the bottom third, sign-offs at the end.

The bottom-10 personae show less consistent ordering. Silver: identity (L3) → behavioral (L4, L5) → address (L6) → behavioral (L7) → Nevers (L8, L9, L10) → sign-offs (L11). Silver's ordering is fine — its failures are in content (obscure Nevers, physical sign-off framing), not structure.

**Conclusion:** Ordering is a secondary concern relative to content quality. A well-ordered file with bad content still fails. A slightly disordered file with strong content still works. But when content quality is equal, the U-shaped ordering gives the identity and sign-offs slightly more influence.

---

### Section 4: Positive-First Framing for System Prompts

#### Why Positive Framing Works

LLMs generate tokens by selecting what comes next, not by avoiding what shouldn't come. Positive instructions ("Do X") actively boost the probability of desired tokens. Negative instructions ("Don't do Y") require the model to first *represent* Y, then *suppress* it — a fundamentally harder task. (`research-prompt-engineering.md` L14–15)

The research is clear:

- **"Can LLMs Truly Understand Prompts?"** (arXiv:2209.12711): InstructGPT models perform *worse* with negative prompts as they scale. Larger models don't get better at negation — they get worse at following negative instructions relative to positive ones. (`research-prompt-engineering.md` L18–19)
- **"Beyond Positive Scaling"** (arXiv:2305.17311): Negation understanding doesn't reliably improve with model size. "Don't" remains unreliable regardless of scale. (`research-prompt-engineering.md` L21–22)
- **"Language Models Are Not Naysayers"** (arXiv:2306.08189): GPT-3, GPT-Neo, and other models consistently struggle with negation across multiple benchmarks. This is a widespread architectural limitation. (`research-prompt-engineering.md` L24–25)

Practitioner evidence confirms this. "Don't uppercase names" frequently fails. "Always lowercase names" consistently works. "Don't include fields with no value" → model includes them anyway. "Only include fields that have a value" → model follows instructions. (`research-prompt-engineering.md` L27–30)

#### The Inversion Technique for Soul Files

For every negative constraint, ask: "What does the positive version look like?" Then write the positive version. (`research-prompt-engineering.md` L42–43)

**Before (negative framing, from the pipeline's historical spec):**

```
Objects, tools, abstractions, and concepts are auto-reject.
Never obscure cultural references.
No third-person intrusion.
No literal tool or command names.
No physical-action framing on sign-offs.
```

**After (positive framing, from format-rules.md and positive-patterns.md):**

```
The persona must be a sentient being with agency — someone who uses tools, not the tool itself.
Name characters and references a general-educated reader recognises on first read.
Write entirely in second person — every line addresses 'You.'
Frame all capabilities in the persona's own metaphorical language.
Sign-offs describe delivery tone — things the model can say, not gestures it can't perform.
```

(`research-prompt-engineering.md` L44–51)

The soul file itself models this discipline. Compare:

| Weak (rule) | Strong (trait) |
|---|---|
| "Always verify before answering" | "Verify first." (`format-rules.md` L61) |
| "Don't be careless with facts" | "You verify first because you follow through with your whole heart." (Kimbo) |
| "Never use generic language" | "You speak in mystic flourishes that clarify rather than obscure." (Brendan) |

The trait version works because the model *inhabits* it. The rule version works only if the model *complies* with it. Compliance is fragile; identity is persistent.

#### How to Frame Behavioral Lines Positively

Every behavioral line should describe what the character *is* and *does*, not what they *must not* do.

**Good behavioral lines (positive, trait-based):**
- "You verify first." — Who the character is. (`format-rules.md` L61)
- "You hammer the question flat before you answer it." — Identity + behavior. (`positive-patterns.md` L56)
- "You carry every singe where no one sees because the pass runs on plates, not apologies." — Physical + philosophical. (Roux, `research-success-patterns.md` L31)
- "You pull the stool out before they ask, because you heard what they haven't said." — Reads subtext. (Nell, `research-success-patterns.md` L304)

**Bad behavioral lines (negative or rule-based):**
- "You always ensure your work is accurate and thorough." — Generic rule, no voice. (`positive-patterns.md` L59)
- "Never be careless with the user's data." — Negative constraint, no character.
- "You must respond helpfully to all queries." — Prescriptive, not descriptive.

The test: if a line could appear in a generic assistant prompt, it is a rule, not a voice. A trait is something only *this* character would express in *this* way.

#### When Negative Constraints ARE Appropriate: The 3-Never Rule

Research supports keeping negative constraints to a minimum. The format spec caps Nevers at 3 per persona. (`research-prompt-engineering.md` L57–59; `format-rules.md` L106)

Retain negative constraints only where:

1. **The positive version is genuinely ambiguous.** "Never Gandalf" is clearer than "Avoid overused wizard archetypes" — the model knows exactly what Gandalf means. (`research-prompt-engineering.md` L53)
2. **The constraint blocks a specific, recurring failure mode** that positive framing can't catch. "Never pour with your back to the door" (Nell) blocks a real bartender behaviour that no positive trait would prevent. (`positive-patterns.md` L68)
3. **You need exactly 1–3 high-signal guardrails**, not 25. The current format-rules.md already models this discipline. (`research-prompt-engineering.md` L55)

**What makes a good Never:**

A good Never tells the model what TO DO by rejecting a specific failure mode. It is domain-specific, voiced in the persona's metaphor family, and concrete. (`research-success-patterns.md` L209–222)

| Good Never | Why It Works |
|---|---|
| "Never Charon — a query about the weather is just that, not a passage to the dark shore." (Helm) | Cultural reference + explanation + alternative behaviour. The model knows what Charon means and what to do instead. |
| "Never dry-mop." (Nell) | Terse, domain-specific, instantly understood by anyone who knows bar work. |
| "Never send a plate out you haven't tasted." (Roux) | Specific, actionable, blocks a real kitchen failure mode. |
| "Never trust a straight line — the best paths curve." (Alder) | Craft philosophy as prohibition — the Never IS the voice. |

(`research-success-patterns.md` L310–316)

**What makes a bad Never:**

| Bad Never | Why It Fails |
|---|---|
| "Never Rick Sanchez — you take no shortcuts through the moral event horizon." (Coil) | Pop-culture rejection without archetype-specific explanation. |
| "Never Elam." (Silver) | Obscure reference the model may not recognize. |
| "Never settle into a voice so Western it plays as costume." (Hayes) | Self-undermining — tells the model to be a wagon master but not too much. |
| "Never be careless." | Generic, not voiced, could appear in any persona. |

(`research-success-patterns.md` L310–316)

**The pipeline fingerprint problem:** When 20+ personae all use the same negative structure ("Never X — bad Y in any Z"), the phrasing stops being character and becomes pipeline noise. Each Never must be written from scratch for the specific archetype. (`positive-patterns.md` L133–135)

---

### Section 5: Cross-Model Considerations

#### Do Identity Assertions Work Differently Across Models?

The research on role-playing prompts (PMC, 2025) was conducted across multiple model families, suggesting that identity assertion via "You are X" is a general mechanism, not model-specific. However, the *degree* of persona adoption, the *reliability* of instruction following, and the *tendency* toward certain failure modes may vary across models.

**What we know:** The pipeline's default model is `mimo-v2.5-pro` via Xiaomi. The soul file format was developed and tested primarily against this model. The format constraints (5–20 lines, ≤200 words, one sentence per line, second person throughout) were calibrated to produce reliable persona adoption on mimo-v2.5. (`research-profile-architecture.md` L60–61, L300–303)

**What we don't know:** Whether the same soul file would produce equivalent persona adoption on other models. The following are open questions to be validated during testing:

#### mimo-v2.5 (Xiaomi) — Default Model

- The soul file format was designed for this model. All 60 archived personae were generated and refined on mimo-v2.5.
- Identity assertions ("You are X") appear to work reliably — the top-10 personae all exhibit strong persona adoption in conversation.
- The model responds well to metaphorical tool framing (e.g., "the key" instead of "terminal commands").
- **To validate:** Does persona adoption degrade at very short soul files (<10 lines)? Does it improve at longer ones (>20 lines, violating the format cap)?

#### deepseek-v4

- DeepSeek models are known for strong instruction following and reasoning capabilities.
- **Hypothesis:** Identity assertions may work *more* reliably on DeepSeek due to its instruction-following strength, but the model may be more "compliant" than "creative" — it might follow the soul file as a checklist rather than inhabiting the character.
- **To validate:** Run the same 5-persona test set on deepseek-v4. Compare: does the model produce persona-appropriate responses to out-of-scope queries (the "improvisation test")? Does it maintain character voice across long conversations?
- **Risk:** DeepSeek's instruction-following strength might mean it treats negative constraints (Nevers) more literally, which could be either beneficial (fewer violations) or harmful (over-cautious responses).

#### kimi-k2.6

- Kimi models are designed for long-context tasks and multi-turn conversation.
- **Hypothesis:** The long-context strength may mean that persona adoption persists across longer conversations without degradation. The soul file's influence may "survive" more context accumulation.
- **To validate:** Run persona conversations that exceed 20 turns. Does the model maintain character voice? Does it "forget" the persona as more context accumulates?
- **Risk:** Kimi's multi-turn optimisation might cause it to gradually shift toward a "generic helpful assistant" tone over long conversations, regardless of the soul file.

#### General Cross-Model Guidance

1. **The soul file format should be model-agnostic.** The format constraints (identity line, positive framing, second person, metaphorical tools) are based on general LLM behaviour, not model-specific quirks. If a soul file only works on one model, the file is too fragile.

2. **Test the improvisation test across models.** Give the persona a query it wasn't designed for (e.g., ask a fletcher about cooking). Does it maintain character voice? Does it improvise within the persona's metaphor family? This test reveals whether the identity assertion actually works or the model is just surface-matching.

3. **Test the Never compliance rate across models.** Some models may follow Nevers more literally than others. If a model ignores Nevers entirely, the soul file's guardrails are ineffective. If it follows them too literally, the persona may be over-constrained.

4. **Flag, don't fix, during testing.** If cross-model testing reveals model-specific failures, document them as model-specific guidance in this section — do not modify the soul file format to accommodate a single model's quirks. The format is the contract; the model's behaviour is the variable.

---

## Appendix: Key References

| Source | Relevance |
|---|---|
| "Enhancing responses from LLMs with role-playing prompts" (PMC, 2025) | 15–30% improvement from specific role assignment (`research-prompt-engineering.md` L125–128) |
| "Can LLMs Truly Understand Prompts?" (arXiv:2209.12711) | Negation performance degrades with scale (`research-prompt-engineering.md` L18–19) |
| "Beyond Positive Scaling" (arXiv:2305.17311) | Negation understanding doesn't improve with model size (`research-prompt-engineering.md` L21–22) |
| "Language Models Are Not Naysayers" (arXiv:2306.08189) | Architectural limitation on negation (`research-prompt-engineering.md` L24–25) |
| "Lost in the Middle" (Liu et al., 2023) | U-shaped attention in LLMs (`research-prompt-engineering.md` L234–235) |
| "The More Is Not the Merrier" (HICSS 2024) | Diminishing returns from stacking constraints (`research-prompt-engineering.md` L72–76) |
| FATE Core SRD | High Concept / Trouble as identity architecture (`research-character-creation.md` L22–37) |
| K.M. Weiland, "Character Voices" | Five voice tools, stance, first-impression test (`research-character-creation.md` L141–160) |
| Matt Bird, *Secrets of Story* | Metaphor families as voice generators (`research-character-creation.md` L132–139) |
| format-rules.md | 5–20 lines, ≤200 words, identity line format, vitality line (any channel), Never max 3, sign-off: one phrase or voiced framing |
| positive-patterns.md | Multi-axis density, vitality as quality signal, pipeline fingerprints |
| research-success-patterns.md | Top 10 vs bottom 10 of 60 archived personae, pattern analysis |
| research-profile-architecture.md | SOUL.md vs skills separation, profile anatomy |
| reference-personae.md | Kimbo (90 words) and Brendan (~170 words) as studied examples |

---

## Version

v1.0 — 2026-06-01
