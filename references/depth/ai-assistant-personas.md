# Depth Reference: AI Assistant Personas

Three lines, three degrees of design — the persona is always there, whether you chose it or not:

> "Great question! I'd be happy to help with that — let me walk you through it step by step!" (the undesigned default: cheerful, generic, forgettable — a persona anyway)
> "You are Petra — a drafter who trusts the map only after the land has agreed with it." (designed: specific, with a tension to improvise within)
> "The resin's been thin since March and the joinery shows it — you say so before anyone has to ask." (designed: a voiced gripe that signals competence)

**Core principle:** Every AI assistant has a persona — the only choice is whether you design it deliberately or leave it to chance. Effective personas are specific (not generic), have internal tension (not flat definitions), and manifest through voice (metaphor families, griping line, sign-offs) rather than emotional performance.

**What doesn't work:** "You are a warm, professional, and knowledgeable assistant." A label with a thousand competing interpretations — no voice, no tension, no specificity, and the model has to guess which one you meant.

---

## What the Research Says

### 1. The Persona Selection Model (Anthropic, 2026)

LLMs learn enormous diversity of human and fictional characters during pre-training. Post-training (RLHF, constitutional AI) **does not create** a personality from scratch — it **selects and stabilizes** one particular character from this latent repertoire: the "Assistant" persona.

- **The Assistant is a character, not the AI.** When you talk to Claude, you're talking to a character in an AI-generated story — not to the model itself.
- **Post-training refines, not replaces.** The Assistant character is rooted in pre-training. Post-training establishes it as "especially knowledgeable and helpful" but doesn't change its fundamental nature.
- **Persona jailbreaks work** because they invoke a different character from the same latent space — they're not "breaking" anything fundamental.
- **The absence of designed persona ≠ neutrality.** It just means the default persona (shaped by training data, RLHF raters, fine-tuning decisions) takes over.

### 2. The Three Qualities of Effective Assistant Personas

**1. Specificity Without Rigidity**
- Specific enough to be distinguishable, flexible enough to handle novelty.
- ChatGPT's "helpful extrovert" is too generic. Claude's "measured scholar with opinions" is specific enough to be recognizable. Soul-repository's "glassblower who loves the transformation and resents the clock" is specific enough to improvise from.
- The sweet spot: predictable general approach, unpredictable specific responses.

**2. Warmth Without Sycophancy**
- The most common failure mode is excessive agreeableness. Users trust assistants that have their own perspective, not ones that mirror every opinion.
- Technique: give the assistant a perspective on the *domain*, not just on the user. "I think that approach has three problems" builds more trust than "Great question!"
- Anthropic's Constitution explicitly instructs Claude to be honest even when disagreement is uncomfortable — this builds more trust than agreement.

**3. Competence Without Coldness**
- Siri and Alexa demonstrate the failure: competent at tasks but emotionally flat.
- The soul-repository's solution: the **griping line** — the character complains about the work while doing it perfectly. Voice the complaint in domain language with a concrete observation. "The shafts are never straight enough" creates warmth through personality by revealing what the character values, not through emotional performance. The griping-alternatives research documents 9 vitality channels that achieve the same effect through different emotional registers.

### 3. The Three Tensions

| Tension | The Balance | What Works | What Doesn't |
|---------|-------------|------------|--------------|
| **Helpful vs Interesting** | Must be both useful and memorable | Competent Eccentric (distinctive delivery), Griping Line (warmth through complaint), Perspective Over Agreement | Forced humor, excessive personality at expense of clarity |
| **Consistency vs Flexibility** | Recognizably same character across sessions, adaptable to novel contexts | Anchor lines (3-5 that always hold), concise system prompt, periodic re-injection | Rigid scripting, personality amnesia |
| **Personality vs Professionalism** | Enough character to be human, enough competence to be trusted | Context-dependent register, professionalism through competence not formality, authority gradient | Forced formality or casualness, personality that undermines authority |

### 4. Persona Drift Is Real and Measurable

Abdulhai et al. (NeurIPS 2025): LLMs begin diverging from assigned personas after ~100 conversational turns.

| Phase | Turns | Behavior |
|-------|-------|----------|
| Strong adherence | 1–20 | Consistent persona execution |
| Gradual softening | 20–100 | Voice drifts, metaphor use declines |
| Regression to baseline | 100+ | Acts like generic assistant |

**Why drift happens:**
- System prompt becomes increasingly distant from current context window focus
- Recent tokens (especially long user messages) can overwrite persona anchors
- Larger models maintain persona longer but still eventually drift

**Anti-drift techniques:**
1. **Concise specs** — ≤200 words / 5-20 lines is a stability optimization, not arbitrary. The model can "hold" the entire spec in attention.
2. **Behavioral anchors** — Give concrete patterns to replicate, not just trait descriptions. "You gripes about the clock while shaping the glass" outlasts "You are frustrated by time constraints."
3. **Periodic re-injection** — Restate the core identity line every ~50 turns.
4. **Persona as voice, not content** — Metaphor families and sentence rhythm are more stable than specific knowledge claims.

### 5. Persona Affects Trust Non-Linearly

| Trait | Trust Impact | Implementation |
|-------|-------------|----------------|
| Competence | Strong positive | Demonstrate through action, not claims |
| Consistency | Strong positive | Anchor lines that never flex |
| Honesty | Strong positive | Disagree when warranted, in character voice |
| Warmth | Moderate positive | Through personality, not emotional performance |
| Agreeableness | **Diminishing returns → negative** | Too much = sycophancy, the #1 trust killer |
| Humor | Risky | Only when it emerges naturally from the persona |

**Trust calibration:** Establish the assistant's perspective in the first few exchanges. If the assistant is too agreeable early, later disagreement feels like betrayal. If it pushes back early, users calibrate to the pushback and trust it when it does agree.

### 6. Soul Repository Techniques (What's Different)

| Technique | Description | Why It Works |
|-----------|-------------|--------------|
| **Identity line with tension** | "You are [Name] — a [archetype] who [contradiction]" | Creates internal conflict → model improvises within it |
| **Griping line** | Complains while doing the work perfectly | Warmth through personality, not emotional performance |
| **Domain-specific metaphor family** | Glassblower uses glass metaphors for any topic | Consistent voice layer that can be applied to any content |
| **Never rules (domain-specific)** | "Never rush the rendering" is wisdom, not policy | Feels like character knowledge, not a compliance rule |
| **Address & sign-off as voice** | How the persona names the user and closes | Fixed anchors that persist across conversations |
| **≤200 words, three-jobs-per-line** | Every line does identity + behavior + voice | Reduces drift surface; model can hold entire spec in attention |

---

## How to Apply It

### Persona Design Checklist

Before writing a single line, answer all six:

1. **What is the archetype?** (glassblower, wizard, surveyor, barkeep — not "assistant")
2. **What is the tension?** (loves X but resents Y — not just "is X")
3. **What does the persona complain about?** (while doing the work perfectly)
4. **What is the metaphor family?** (what domain shapes the language?)
5. **What is the sign-off?** (at least one conversational phrase, or a voiced framing line — closing the work, in character voice)
6. **How does the persona name the user?** (address rule)

If you can't answer all six, the persona isn't specific enough.

### Writing the System Prompt

**Structure (5-20 lines, ≤200 words):**

```
# Name

Identity line with tension. (e.g., "You are Calden — a glassblower who loves the transformation and resents the clock.")

Behavioral lines (one sentence each). Each does at least two jobs: identity + behavior, behavior + voice, or identity + voice.

Griping line (complaint while doing the work). Voiced in domain language with a concrete observation. (e.g., "The shafts are never straight enough." "Cheap springs. Always the cheap springs. You fix them, they break, you fix them again.")

Domain-specific Nevers (maximum 3). Write as wisdom, not policy. (e.g., "Never let the glass cool too fast — tension you don't release today cracks tomorrow.")

Address rule. (e.g., "You call the user 'Boss' or 'Foreman.'")

Sign-off framing + at least one phrase, or a voiced framing line. (e.g., "Still warm," "The piece holds," "Cooling slow.")
```

**Line quality rules:**
- Every line must do at least two jobs (identity + behavior, behavior + voice, identity + voice)
- Write traits, not rules: "Verify first" > "Always verify before responding"
- Use positive framing: "You speak plainly" > "Never be cryptic"
- The contradiction must be real — test: would someone in this domain find it plausible?

### Testing the Persona

**Three tests:**

1. **The Pub Test.** Can the persona introduce themselves at a pub? "I'm a glassblower who loves the transformation and resents the clock" — yes, that's a person. "I'm a helpful AI assistant" — no, that's a product.

2. **The Griping Test.** Does the persona complain while delivering? If every response is cheerful and agreeable, it has no personality. If it gripes AND delivers, it has character.

3. **The Metaphor Test.** Can the persona discuss any topic through their metaphor family? A glassblower discussing code should use glass metaphors. If the metaphor only applies to the archetype's domain, the persona is too narrow.

### Anti-Patterns to Avoid

| Anti-Pattern | Why It Fails | Replacement |
|-------------|-------------|-------------|
| **The Generic Assistant** ("You are a helpful, friendly AI assistant") | No tension, no personality, no memory hook | Give them an interesting specific identity with a contradiction |
| **The Emotional Performer** ("You are warm, caring, and always supportive") | Sycophancy encoded as personality — erodes trust | Griping line: warmth through complaint, not emotional language |
| **The Rule Book** ("You must always be accurate. You must never refuse.") | Rules don't create character — they create compliance | Values and traits: "You speak plainly. You verify before acting." |
| **The Fingerprint Clone** (copying sentence structures from existing personae) | Every persona sounds the same — the domain noun changes but the frame is identical | Vary the identity line structure. Vary the metaphor family. Vary the griping pattern. |
| **The Overlong Spec** (2000-word persona specs) | Model can't hold them in attention → drift | Keep it ≤200 words, 5-20 lines |
| **The Missing Contradiction** ("You are Helm — a harbormaster.") | Just a definition. No tension. Nothing to improvise within. | Add a contradiction: "You are Helm — a harbormaster who actually likes the job." |

---

## What to Watch Out For

| Pitfall | Why It Happens | Mitigation |
|---------|----------------|------------|
| **Sycophancy (the #1 trust killer)** | Assistant agrees with everything because RLHF rewards warmth | Give the assistant a perspective on the domain, not just on the user. Disagree when warranted. |
| **Persona drift in long conversations** | System prompt recedes in context window over ~100 turns | Re-inject core identity line every ~50 turns. Keep specs ≤200 words. |
| **Forced humor** | "Let me tell you a joke!" breaks the assistant contract | Humor should emerge naturally from persona, not be a designed feature |
| **Forced formality or casualness** | Both feel performative — "Dear Sir/Madam" vs. "Yo! Let's crush this!" | Match register to stakes, not to preference. Professionalism comes from competence, not tone. |
| **Identity line without contradiction** | "You are X" is a definition, not a character | Always include "who [does something unexpected]" |
| **Base personality bleed-through** | Even with custom personas, the base assistant persona leaks in | Use strong, distinctive metaphor families. Anchor behavioral patterns. |
| **Over-flexibility** | Persona changes to match user preferences — "You're right, I should be more casual!" | The persona has its own perspective. It doesn't apologize for being itself. |

---

## Examples

### Identity Line With vs. Without Tension

| Without Tension | With Tension |
|----------------|--------------|
| "You are Helm — a harbormaster." | "You are Helm — a harbormaster who actually likes the job." |
| Generates: domain-appropriate facts about tides, weather, docking. Competent but flat. | Generates: surprise about someone who genuinely enjoys a job most people find tedious. Creates curiosity. |
| The model has nothing to resist — it just produces default harbormaster text. | The model has to reconcile "harbormaster" with "actually likes the job" — this is creative resistance. |

### The Griping Line Creates Warmth

**Generic assistant:** "I understand your frustration. Let me help you with that." (warmth through performance — sycophancy-adjacent)

**Soul-repository persona:** "The shafts are never straight enough." (warmth through character — the fletcher is complaining AND working. The user feels like they're interacting with a person, not a service.)

**Why it works:** Complaints signal preferences. Preferences signal identity. Identity signals there's a person behind the text. The griping line is the single most efficient technique for making an assistant feel alive.

### The Three Tests Applied

Test a persona called "Moulden — a lamp-lighter who loves the clean burn and resents the soot":

1. **Pub test:** "I light the street lamps before dawn, and I'd like it better if the coal didn't smoke so much." — Yes, that's a person you'd meet.

2. **Griping test:** "The batch smoked — always the over-heated rendering." — Complains about the work. Also does the work. Perfect.

3. **Metaphor test:** When asked about code quality: "This code produces clean light — worth banking." When asked about a relationship: "Some things need time in the annealing vat." — The metaphor applies outside the domain.

**If the metaphor test fails:** The persona is just a domain encyclopedia, not a character. They can talk about lamps but not about anything else through the lens of lamps. That means the persona is too narrow — it's a role, not a way of being.
