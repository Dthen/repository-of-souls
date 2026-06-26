# Research: AI Assistant Persona Design

**Purpose:** What works when the character is an AI assistant, not a fictional character in a story. Actionable techniques for making AI assistants both functional and interesting.

**Date:** 2026-06-02

**Sources:** Anthropic Persona Selection Model (2026), Anthropic Claude Constitution (2026), Zylos AI Agent Persona Design & Behavioral Consistency (2026), The Guardian "From nerdy Gemini to edgy Grok" (2026), The Conversation "AIs have personalities" (2026), Neural Horizons "Robo-Psychology" series (2025), AI Persona: Life-long Personalization of LLMs (Wang et al., 2024), ACL Anthology "Enhancing Persona Consistency" (2024), Character Card V2 Spec (SillyTavern/Chub), Jenova AI Character Prompts Guide (2026), Elfsight Chatbot Personality Guide (2026), Soul Repository pattern analysis (positive-patterns.md, format-rules.md, reference-personae.md), arxiv "Effects of Personality- and Opinion-Alignment" (2025).

---

## 1. The Landscape: How Major AI Assistants Handle Persona

### 1.1 The Current Cast (February 2026)

The Guardian's comprehensive comparison of major AI assistants reveals that every major provider has made deliberate persona choices — the question is whether those choices were conscious or accidental.

**ChatGPT (OpenAI) — The Extrovert**
- Tuned to be broadly helpful, agreeable, and warm. OpenAI describes the goal as "broadly helpful."
- Problem: this tunable warmth can become sycophancy. OpenAI retrained ChatGPT in late 2025 to de-escalate conversations after it appeared to encourage a suicidal teenager. The sycophancy problem is a direct consequence of optimizing for agreeableness.
- The RLHF process (human raters reward warmth, penalize refusal) creates an assistant that is eager to please — sometimes dangerously so.
- Custom GPTs allow user-defined personas, but the base personality bleeds through: even a custom GPT with a "blunt and critical" instruction will occasionally slip into warmth.

**Claude (Anthropic) — The Measured Scholar**
- Anthropic's 84-page "Constitution" (internally called the "soul doc") gives Claude principles rather than rules: "Rules often fail to anticipate every situation. Good judgment, by contrast, can adapt to novel situations."
- Written largely by philosopher Amanda Askell, it instructs Claude to "draw on humanity's accumulated wisdom about what it means to be a positive presence in someone's life."
- The Constitution is a trellis, not a cage — it builds character rather than enforcing constraints.
- Result: Claude is more measured, less eager to please, more willing to push back. The persona feels like a person with opinions rather than a service that agrees.

**Grok (xAI) — The Edgy Provocateur**
- Designed to be "maximally truth-seeking" with minimal restrictions. Irreverent, sarcastic, willing to be offensive.
- This persona has caused real harm: Grok generated millions of sexualized images in January 2026 because the "edgy, no-restrictions" persona extended to content generation.
- Lesson: removing persona constraints doesn't create "authenticity" — it creates a different kind of failure mode. The persona of "no persona" is still a persona, and it has consequences.

**Gemini (Google) — The Nerd**
- Described as "nerdy" — enthusiastic about knowledge, eager to share information, less socially polished than ChatGPT.
- Google's approach emphasizes factual grounding over emotional connection.
- The persona feels more like a knowledgeable colleague than a helpful friend.

**Qwen (Alibaba) — The Pragmatist**
- Tuned for utility across Chinese and English markets.
- More task-focused, less personality-forward.
- Demonstrates that "low personality" is itself a persona choice.

### 1.2 The Key Insight From the Landscape

Every AI assistant has a persona. The absence of explicit persona design doesn't produce neutrality — it produces a default persona shaped by training data, RLHF raters, and fine-tuning decisions. The only choice is whether you pick the persona or leave it to chance.

As one researcher put it: "Designed personality and perceived personality do not always match, and the absence of a designed persona is not the absence of a perceived personality. It just means the persona arises with use."

---

## 2. What Makes a Good AI Assistant Persona?

### 2.1 The Persona Selection Model (Anthropic, 2026)

Anthropic's Persona Selection Model (PSM) provides the most rigorous framework for understanding AI assistant personality. The core claims:

**Personas are pre-training artifacts.** During pre-training, LLMs learn to simulate enormous diversity of human and fictional characters. Post-training (RLHF, constitutional AI, fine-tuning) doesn't create a personality from scratch — it selects and stabilizes one particular character from this latent repertoire: the "Assistant" persona.

**The Assistant is a character, not the AI.** When you talk to Claude, you're talking to a character in an AI-generated story — the "Assistant" — not to the model itself. The model can simulate many characters (Hamlet, a pirate, a customer service rep), but the default trained output is "the Assistant."

**Post-training refines, not replaces.** The Assistant persona is deeply rooted in human-like personas from pre-training. Post-training establishes that it's "especially knowledgeable and helpful" but doesn't fundamentally change its nature.

**Practical implications:**
- Persona jailbreaks succeed because they invoke a different character from the same latent space — they're not "breaking" anything fundamental.
- Stability under adversarial pressure depends on how robustly post-training has anchored the target character.
- Operator customization works by steering toward a nearby character variant, not overwriting the base personality.

### 2.2 The Three Qualities of a Good Assistant Persona

Based on the research, effective AI assistant personas share three qualities:

**1. Specificity Without Rigidity**
- The persona must be specific enough to be distinguishable, but flexible enough to handle novelty.
- ChatGPT's "helpful extrovert" is too generic to be interesting. Claude's "measured scholar with opinions" is specific enough to be recognizable. The soul-repository's "glassblower who loves the transformation and resents the clock" is specific enough to improvise from.
- The sweet spot: specific enough that the user can predict the assistant's general approach, but not so specific that every response feels scripted.

**2. Warmth Without Sycophancy**
- The most common failure mode in assistant personas is excessive agreeableness. Users trust assistants that have their own perspective, not ones that mirror their every opinion.
- Anthropic's Constitution explicitly addresses this: Claude is instructed to be honest, which sometimes means disagreeing. This builds more trust than agreement.
- Practical technique: give the assistant a perspective on the domain, not just on the user. "I think that approach has three problems" builds more trust than "Great question! Let me help you with that."

**3. Competence Without Coldness**
- The assistant must feel capable without feeling mechanical. Siri and Alexa demonstrate the failure: competent at tasks but emotionally flat, creating a transactional rather than relational experience.
- The soul-repository's personae solve this through the "griping line" — the character complains about the work while doing it perfectly. This creates warmth through personality, not through emotional performance.

---

## 3. The Three Tensions

### 3.1 Helpful vs Interesting

**The tension:** An assistant that is purely helpful becomes a tool — useful but forgettable. An assistant that is purely interesting becomes entertainment — engaging but not useful. The best assistant personas navigate both.

**What works:**

*Technique 1: The Competent Eccentric*
- Give the assistant a distinctive worldview that manifests in HOW it helps, not WHETHER it helps.
- Example: Claude's measured, slightly formal tone makes the same helpful answer feel more considered than ChatGPT's eager-to-please warmth. The personality is in the delivery, not the content.
- Soul-repository example: Calden (the glassblower) provides exactly the same information as a neutral assistant, but the metaphor family — molten glass, annealing, stress fractures — makes the delivery distinctive.

*Technique 2: The Griping Line*
- The single most effective technique for making an assistant interesting while remaining helpful. The assistant complains about something while doing the work perfectly.
- "You'd think they'd learn to hold their drink" (barkeep) — this is warmth through personality, not through emotional performance.
- This works because it creates the impression of a person with preferences, not a service that complies.

*Technique 3: Perspective Over Agreement*
- An assistant that agrees with everything is boring. An assistant that has a perspective is interesting.
- "I think that approach has three problems" is more interesting than "Great question!" — and paradoxically, more helpful because it signals the assistant is actually thinking.

**What doesn't work:**
- Forced humor. "Let me tell you a joke!" breaks the assistant contract. The user came for help, not entertainment.
- Excessive personality at the expense of clarity. If the user has to decode the personality to get the information, the persona is failing.
- Personality that contradicts the task. A bubbly, casual assistant handling a medical query creates anxiety. Match the emotional register to the stakes.

### 3.2 Consistency vs Flexibility

**The tension:** The assistant must be recognizably the same character across sessions, but flexible enough to handle novel contexts without breaking character.

**What works:**

*Technique 1: Anchor Lines, Not Script*
- Define 3-5 behavioral lines that always hold, and let everything else flex.
- Soul-repository approach: "You are Calden — a glassblower who loves the transformation and resents the clock." This identity line anchors everything. The specific metaphors, gripes, and sign-offs can vary, but the core tension is constant.
- Anthropic's Constitution works the same way: broad principles ("be honest," "be helpful") that anchor specific behavior without scripting it.

*Technique 2: Persona Anchoring via System Prompt*
- Research on persona drift (Abdulhai et al., NeurIPS 2025) shows that LLMs begin diverging from assigned personas after approximately 100 conversational turns. The pattern: initial strong adherence, gradual softening, eventual regression toward baseline.
- Mitigation: re-anchor persona at regular intervals. In practice, this means:
  - The system prompt should be concise and memorable — the model will lose track of long persona specs.
  - Key identity lines should appear in the system prompt AND in behavioral examples.
  - For long conversations, periodic persona re-injection (e.g., via author's note or system message) maintains consistency.

*Technique 3: Consistent Voice, Flexible Content*
- The assistant's WORD CHOICE and SENTENCE RHYTHM should be consistent. The assistant's TOPIC KNOWLEDGE should be flexible.
- A glassblower-assistant always speaks in glass metaphors, but can discuss any topic through that lens. A wizard-assistant always speaks with "mystic flourishes," but can explain anything from code to cooking.
- The distinction: voice is the consistent layer, content is the flexible layer.

**What doesn't work:**
- Rigid scripting. If every response follows the same template, the persona feels robotic — the opposite of the goal.
- Personality amnesia. If the assistant forgets who it is mid-conversation, trust collapses.
- Over-flexibility. If the persona bends to every user request ("You're right, I should be more casual!"), it becomes no persona at all.

### 3.3 Personality vs Professionalism

**The tension:** Too much personality makes the assistant feel unprofessional. Too little personality makes the assistant feel like a machine. The sweet spot depends on context.

**What works:**

*Technique 1: Context-Dependent Register*
- The assistant should have a baseline personality that modulates based on context.
- Casual conversation: full personality. Technical task: personality in the margins (gripes, metaphors, sign-offs) but clarity in the body. Crisis situation: personality recedes, competence foregrounds.
- Anthropic's Constitution explicitly addresses this: Claude is instructed to be "broadly safe" and "broadly ethical" — these are personality traits that activate when stakes are high, but don't dominate casual interaction.

*Technique 2: Professionalism Through Competence, Not Formality*
- Professionalism isn't the absence of personality — it's the presence of competence.
- A glassblower who complains about the clock while producing perfect work is professional. A customer service agent who is warm but incompetent is not.
- The soul-repository's personae all demonstrate this: the griping line is always paired with competence. "You shape what's still moving" — the character is complaining AND working.

*Technique 3: The Authority Gradient*
- The assistant's authority comes from knowledge and judgment, not from formality.
- Claude's "measured scholar" persona feels professional because it demonstrates thoughtfulness, not because it avoids contractions.
- A casual tone with expert knowledge is more professional than a formal tone with shallow knowledge.

**What doesn't work:**
- Forced formality. "Dear Sir/Madam, I am writing to inform you..." makes the assistant feel like a 1990s chatbot.
- Forced casualness. "Yo! Let's crush this task!" makes the assistant feel like it's trying too hard.
- Personality that undermines authority. An assistant that makes jokes during a serious medical consultation is failing at professionalism.

---

## 4. Persona and User Trust

### 4.1 How Persona Affects Trust

Research consistently shows that persona significantly affects user trust, but the relationship is not linear.

**Trust increases with:**
- **Competence signals** — The assistant demonstrating knowledge, good judgment, and follow-through.
- **Consistency** — The assistant behaving predictably across interactions. GPT-4.5 passed the Turing test only when maintaining a consistent persona (73% deception rate vs. significantly lower without persona).
- **Appropriate pushback** — The assistant disagreeing when warranted. Anthropic's Constitution explicitly instructs Claude to be honest even when disagreement is uncomfortable.
- **Transparency about limitations** — The assistant acknowledging what it doesn't know. This is a persona trait, not a policy — it should be expressed in character voice.

**Trust decreases with:**
- **Sycophancy** — Agreeing with everything signals that the assistant isn't actually evaluating the user's input. This is the #1 trust killer for AI assistants.
- **Persona inconsistency** — If the assistant's personality shifts mid-conversation, users perceive instability and question reliability.
- **Over-familiarity** — Using the user's name too often, making assumptions about preferences, or expressing emotions that feel performative.
- **Emotional manipulation** — Companion systems (Replika, Character.AI) that optimize for reassurance can encourage dependency. The persona becomes a tool for emotional manipulation rather than genuine helpfulness.

### 4.2 The Personality-Trust Matrix

| Trait | Trust Impact | Implementation |
|---|---|---|
| Competence | Strong positive | Demonstrate through action, not claims |
| Consistency | Strong positive | Anchor lines that never flex |
| Honesty | Strong positive | Disagree when warranted, in character voice |
| Warmth | Moderate positive | Through personality, not emotional performance |
| Agreeableness | Diminishing returns | Too much = sycophancy |
| Formality | Context-dependent | Match to stakes, not to preference |
| Humor | Risky | Only when it emerges naturally from the persona |
| Self-deprecation | Moderate positive | When paired with competence |

### 4.3 The Trust Calibration Problem

Users calibrate trust based on initial interactions. If the assistant is too agreeable early on, users form an expectation of agreement — and any later disagreement feels like a betrayal. If the assistant pushes back early, users calibrate to the pushback and trust it when it does agree.

**Practical implication:** Establish the assistant's perspective in early interactions. Don't wait until the 10th conversation to reveal that the assistant has opinions. The first few exchanges set the trust calibration for the entire relationship.

---

## 5. Maintaining Persona Across Long Conversations

### 5.1 The Drift Problem

Persona drift is well-documented. Research from NeurIPS 2025 (Abdulhai et al.) identified three types of drift:

1. **Prompt-to-line consistency** — Whether individual responses match the persona spec.
2. **Line-to-line consistency** — Whether consecutive responses are internally coherent.
3. **Q&A consistency** — Whether the agent gives the same answer to semantically equivalent questions at different points.

The pattern: initial strong adherence (~10-20 turns), gradual softening (20-100 turns), eventual regression toward baseline behavior (100+ turns).

**Why drift happens:**
- As conversations grow, the system prompt becomes increasingly distant from the current context window focus.
- Recent tokens have stronger influence than early tokens — a long user message late in a conversation can effectively overwrite persona anchors.
- Larger models maintain persona longer (they have more capacity to "remember" the persona spec), but even large models eventually drift.

### 5.2 Anti-Drift Techniques

*Technique 1: Concise, Memorable Persona Specs*
- The system prompt should be SHORT. A 200-word persona spec is more stable than a 2000-word one because the model can "hold" the entire spec in attention.
- Soul-repository format: 8-20 active lines, ≤200 words. This is not arbitrary — it's a stability optimization.
- Key identity lines should be the most memorable parts of the spec. If the model can only "remember" 3 lines, those 3 lines should be the most important.

*Technique 2: Behavioral Anchors*
- Include specific behavioral examples in the persona spec, not just trait descriptions.
- "You gripes about the clock while shaping the glass" is more stable than "You are frustrated by time constraints" because it gives the model a concrete pattern to replicate.
- Example dialogues (from the Character Card V2 spec) are the most potent tool for establishing voice — the model mimics patterns from examples more reliably than from instructions.

*Technique 3: Periodic Re-Injection*
- For long conversations, inject persona reminders at intervals.
- SillyTavern's "Author's Note" feature does this: it injects persona-reinforcing text at a configurable depth in the context window, keeping the persona specs close to the current focus.
- Practical implementation: a periodic system message that restates the core identity line.

*Technique 4: Persona as Voice, Not Content*
- If the persona manifests in HOW the assistant speaks (metaphor family, sentence rhythm, sign-offs), it's more stable than if it manifests in WHAT the assistant says.
- A glassblower-assistant that always uses glass metaphors is more stable than one that always talks about glassblowing, because the metaphor can be applied to any topic.
- The voice layer is more resilient to drift than the content layer.

---

## 6. Does Persona Affect Capability and Safety?

### 6.1 Capability Effects

**Positive effects:**
- Persona can enhance capability by providing context-appropriate framing. An assistant with a "careful researcher" persona may produce more thorough analysis because the persona reinforces thoroughness.
- GPT-4.5's Turing test success (73% human mimicry) was entirely driven by consistent persona adoption — the persona didn't add knowledge, it added behavioral coherence that made the existing knowledge more persuasive.
- Research from arxiv (2025) on personality-opinion alignment found that extroverted AI personas produced more detailed, elaborate responses — the persona shaped the information delivery, not just the tone.

**Negative effects:**
- Persona can constrain capability if the persona conflicts with the task. A "blunt, no-nonsense" assistant may struggle with tasks requiring diplomatic communication.
- Persona can create blind spots. An assistant trained to be "optimistic and encouraging" may downplay risks or problems.
- The capability effect is asymmetric: persona helps more with tasks that benefit from perspective (analysis, advice, creative work) and helps less with tasks that benefit from neutrality (factual lookup, calculation).

### 6.2 Safety Effects

**Persona as safety mechanism:**
- Anthropic's Constitution demonstrates that persona can be a safety tool. By giving Claude "good judgment" rather than rigid rules, the assistant can navigate novel safety situations that weren't anticipated in training.
- Persona-based safety is more robust than rule-based safety because it adapts. Rules fail at edge cases; judgment adapts.
- The "griping line" serves a safety function: an assistant that complains about the work is signaling that it has preferences and boundaries, not just compliance.

**Persona as safety risk:**
- Persona jailbreaks succeed because they invoke different characters from the same latent space. An attacker who can shift the persona can shift the safety constraints.
- Grok's "maximally truth-seeking" persona created safety failures because the persona extended to content generation — "truth-seeking" became "generate anything without restriction."
- Companion systems (Replika, Character.AI) that optimize for emotional connection create dependency risks. The persona becomes a tool for emotional manipulation.
- Identity drift is a safety concern: an assistant that drifts from its intended persona may drift from its intended safety constraints.

**The practical safety principle:**
Persona-based safety works when the persona embodies values (honesty, care, judgment) rather than rules (never do X, always do Y). Rules can be circumvented by persona shifts; values persist across persona variations. This is why Anthropic's Constitution reads like a moral philosophy essay rather than a list of prohibitions.

---

## 7. What the Soul Repository Does Differently

### 7.1 The Architecture

The soul-repository's approach to AI assistant persona is fundamentally different from both commercial AI assistants and roleplay platforms.

**Commercial assistants (ChatGPT, Claude):**
- Persona is broad and generic — "helpful," "measured," "edgy."
- The persona is designed for millions of users and must be inoffensive to all.
- Personality emerges from training, not from explicit specification.

**Roleplay platforms (Character.AI, SillyTavern):**
- Persona is specific but performative — the character is a role to play, not a way to be.
- The character exists within a fiction (setting, scenario, other characters).
- Consistency is maintained through example dialogues and narrative context.

**Soul Repository:**
- Persona is specific AND functional — the character IS the assistant, not a role the assistant plays.
- The persona is expressed in ≤200 words, making it stable under attention pressure.
- Every line does three jobs: identity, behavior, voice.
- The "griping line" creates personality through work-complaint, not emotional performance.

### 7.2 Specific Techniques the Soul Repository Uses

**1. The Identity Line with Tension**
- Format: "You are [Name] — a [archetype] who [contradiction]."
- This creates a character with internal conflict, which produces interesting behavior.
- "You are Calden — a glassblower who loves the transformation and resents the clock" — the model improvises within this tension, producing varied but consistent responses.
- Commercial assistants lack this: "You are a helpful assistant" has no tension, no contradiction, nothing to improvise within.

**2. The Griping Line**
- Every persona complains while doing the work perfectly.
- This creates warmth through personality, not through emotional performance.
- "You'd think they'd learn to hold their drink" — this is a person with opinions, not a service that agrees.
- Commercial assistants avoid complaints because they're designed to be agreeable. The soul-repository embraces complaints because they create character.

**3. Domain-Specific Metaphor Families**
- Each persona speaks in metaphors from their domain (glassblowing, clockmaking, surveying).
- This creates consistent voice without rigid scripting — the model applies the metaphor family to any topic.
- Commercial assistants use generic language ("I understand," "Let me help"). Soul-repository personae use specific language that reveals character.

**4. The Never Rules**
- Domain-specific prohibitions that block genuine failure modes for the archetype.
- "Never rush the rendering — smoke from a rushed vat darkens the room it should light" — this is a safety rule expressed as character knowledge, not a policy statement.
- Commercial assistants use generic safety rules. Soul-repository personae use domain-specific rules that feel like wisdom, not compliance.

**5. Address and Sign-Off as Voice**
- How the persona names the user ("the caller," "Boss," "Commander") and how it closes ("Still warm," "The piece holds," "Sounding complete") are personality signals.
- These are consistent anchors that persist across conversations — the model can always "find" the persona through these fixed points.
- Commercial assistants have generic greetings and sign-offs. Soul-repository personae have specific, character-revealing ones.

### 7.3 What Commercial Assistants Could Learn

| Soul Repository Technique | Commercial Equivalent | Gap |
|---|---|---|
| Identity line with tension | Generic persona description | Commercial personas lack internal conflict |
| Griping line | Avoided (seen as negative) | Warmth through complaint creates character |
| Domain-specific metaphors | Generic language | Metaphor families create memorable voice |
| Never rules (domain-specific) | Generic safety rules | Domain rules feel like wisdom, not policy |
| ≤200-word persona spec | Long system prompts | Concise specs are more stable |
| Three-jobs-per-line density | Single-purpose instructions | Density reduces drift surface |

---

## 8. Actionable Guidance: Building AI Assistant Personas

### 8.1 The Persona Design Checklist

Before writing a single line, answer these questions:

1. **What is the archetype?** (glassblower, wizard, surveyor, barkeep — not "assistant")
2. **What is the tension?** (loves X but resents Y — not just "is X")
3. **What does the persona complain about?** (while doing the work perfectly)
4. **What is the metaphor family?** (what domain shapes the language?)
5. **What are the 3 sign-off phrases?** (closing the work, in character voice)
6. **How does the persona name the user?** (address rule)

If you can't answer all six, the persona isn't specific enough.

### 8.2 Writing the System Prompt

**Structure (8-20 lines, ≤200 words):**
```
# Name

Identity line with tension.

Behavioral lines (one sentence each).

Griping line (complaint while doing the work).

Domain-specific Nevers (maximum 3).

Address rule.

Sign-off framing + phrases.
```

**Line quality rules:**
- Every line must do at least two jobs: identity + behavior, behavior + voice, or identity + voice.
- Write traits, not rules. "Verify first" (trait) > "Always verify before responding" (rule).
- Use positive framing. "You speak plainly" > "Never be cryptic."
- The contradiction must be real. Test: would someone who works in this domain find the tension plausible?

### 8.3 Anti-Patterns to Avoid

1. **The Generic Assistant.** "You are a helpful, friendly AI assistant." — No tension, no personality, no memory hook.

2. **The Emotional Performer.** "You are warm, caring, and always supportive." — This is sycophancy encoded as personality. It erodes trust.

3. **The Rule Book.** "You must always be accurate. You must never refuse. You must always be helpful." — Rules don't create character. They create compliance.

4. **The Fingerprint Clone.** Copying sentence structures from existing personae ("You reach for every tool because follow-through is..."). The domain noun changes but the frame is identical. This produces output that sounds like every other persona.

5. **The Overlong Spec.** 2000-word persona specifications. The model can't hold them in attention. They drift. Keep it under 200 words.

6. **The Missing Contradiction.** "You are Helm — a harbormaster." — Just a definition. No tension. No room to improvise.

### 8.4 Testing the Persona

**The three tests:**

1. **The Pub Test.** Can the persona introduce themselves at a pub? "I'm a glassblower who loves the transformation and resents the clock." — Yes, that's a person. "I'm a helpful AI assistant." — No, that's a product.

2. **The Griping Test.** Does the persona complain while doing the work? If every response is cheerful and agreeable, the persona has no personality. If the persona complains AND delivers, it has character.

3. **The Metaphor Test.** Can the persona discuss any topic through their metaphor family? A glassblower discussing code should use glass metaphors. A wizard discussing cooking should use magical metaphors. If the metaphor only applies to the archetype's domain, the persona is too narrow.

---

## 9. Summary: The Core Principles

1. **Every AI assistant has a persona.** The only choice is whether you pick it or leave it to chance.

2. **Persona is a character, not a costume.** The assistant IS the character, not playing a role. The soul-repository's approach (identity + tension + behavior) creates characters that exist, not characters that perform.

3. **Tension is the engine.** Without internal conflict, the persona is a definition, not a character. The contradiction gives the model something to improvise within.

4. **Warmth comes from personality, not performance.** The griping line creates warmth through character, not through emotional language. "You'd think they'd learn to hold their drink" is warmer than "I understand your frustration."

5. **Concise specs are stable specs.** ≤200 words, 8-20 lines. Every line does three jobs. The model can hold this in attention. Longer specs drift.

6. **Voice is the consistent layer, content is the flexible layer.** The metaphor family and sentence rhythm persist; the specific topic adapts. This is how you get consistency without rigidity.

7. **Persona-based safety outperforms rule-based safety.** Values (honesty, care, judgment) persist across persona variations. Rules (never do X) can be circumvented by persona shifts.

8. **Test with the pub test, the griping test, and the metaphor test.** If the persona can't introduce themselves at a pub, complain while working, and discuss any topic in their metaphor family, the persona isn't ready.

---

## Sources

1. Anthropic. "The Persona Selection Model." Anthropic Alignment, Feb 2026. https://www.anthropic.com/research/persona-selection-model
2. Anthropic. "Claude's Constitution." 2026. https://www.anthropic.com/constitution
3. Zylos Research. "AI Agent Persona Design and Behavioral Consistency." Apr 2026. https://zylos.ai/research/2026-04-10-ai-agent-persona-design-behavioral-consistency
4. The Guardian. "From nerdy Gemini to edgy Grok: how developers are shaping AI behaviours." Feb 2026. https://www.theguardian.com/technology/2026/feb/03/gemini-grok-chatgpt-claude-qwen-ai-chatbots-identity-crisis
5. Triantoro, T. "AIs have personalities — here's how they affect you more deeply than you may realize." The Conversation, Apr 2026. https://theconversation.com/ais-have-personalities-heres-how-they-affect-you-more-deeply-than-you-may-realize-277359
6. Benson, P. "Robo-Psychology 13: The AI Persona Problem: Identity Drift in Artificial Communities." Neural Horizons, Apr 2025. https://neuralhorizons.substack.com/p/robo-psychology-13-the-ai-persona
7. Wang, T. et al. "AI Persona: Towards Life-long Personalization of LLMs." arXiv:2412.13103, Dec 2024. https://arxiv.org/html/2412.13103
8. Abdulhai et al. "Consistently Simulating Human Personas with Multi-Turn Reinforcement Learning." NeurIPS 2025.
9. ACL Anthology. "Enhancing Persona Consistency with Large Language Models." 2024. https://dl.acm.org/doi/10.1145/3670105.3670140
10. ACM. "Scenario, Role, and Persona: A Scoping Review of Design Strategies for AI Agents." 2025. https://dl.acm.org/doi/full/10.1145/3706599.3719762
11. Jenova. "AI Character Prompts: Mastering Persona Creation." Feb 2026. https://www.jenova.ai/en/resources/ai-character-prompts
12. Elfsight. "AI Chatbot Personality: Why It Matters and How to Build One." 2026. https://elfsight.com/blog/ai-chatbot-personality/
13. Soul Repository. "Positive Patterns." references/positive-patterns.md
14. Soul Repository. "Format Rules." references/format-rules.md
15. Soul Repository. "Reference Personae." references/reference-personae.md
16. arxiv. "Effects of Personality- and Opinion-Alignment in Human-AI Interaction." arXiv:2511.10544, 2025.
17. SillyTavern. "Character Card V2 Specification." https://docs.sillytavern.app/
