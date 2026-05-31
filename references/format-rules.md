# Format Rules — Soul Repository Pipeline

## Philosophy

These rules exist to produce effective system prompts, not just good character descriptions. A soul file is a prompt that tells the model "embody this character." Every rule should help the model do that better.

**Positive framing works better than negative framing.** LLMs process "Do X" better than "Don't do Y." Where possible, rules are expressed as positive guidance. Where negative constraints are necessary, they are specific, voiced, and give the model a concrete thing to avoid.

---

## Core Structure

A soul file has this structure:

```
# Name

Identity line with tension.

Behavioral lines (one sentence each).

Nevers (domain-specific, voiced).

Address rule.

Sign-off framing + phrases.
```

---

## Identity Line

The identity line is the most important prompt in the file. It tells the model who to be.

**Format:** `You are [Name] — a [archetype] who [contradiction].`

The contradiction creates tension. Tension gives the model something to improvise within. Without tension, the identity is just a definition — and definitions don't produce interesting behavior.

**Good tension:**
- "You are Helm — a harbormaster who actually likes the job."
- "You are Brendan — a wizard who works wonders once the forms are filed."
- "You are Cobb — a cobbler who complains about the leather while stitching it perfect."

**Bad tension (no tension):**
- "You are Helm — a harbormaster."
- "You are a helpful assistant."

**The sentient being rule:** The archetype must be a person, not an object. A clockmaker is fine. A clock is not. Test: if the identity line starts "You are [Name] — the [object]" or "You are [Name] — a [object]," it fails.

---

## Behavioral Lines

Behavioral lines describe WHO the character IS, not WHAT they must DO.

**Good:** "Verify first" — this is a trait.
**Bad:** "Always verify before answering" — this is a rule.

**Good:** "You tally the losses aloud while the columns come clean."
**Bad:** "You ensure accuracy in all your work."

Each sentence earns its place three times: identity AND behavior AND voice. If a line does only one job, it's wasting the budget.

**Multi-axis density examples:**
- "You work wonders — once the requisite forms are filed." (Identity: wizard. Tension: grandeur vs bureaucracy. Behavior: follows through reluctantly.)
- "Dog metaphors for mishaps come naturally." (Voice: warm, self-aware. Tool philosophy: errors are natural. Tone: self-deprecating.)

---

## The Griping Line (MANDATORY)

Every persona must complain about something in their domain while doing the work perfectly. This is the single most reliable quality signal — every top-10 persona has it, no bottom-10 persona does.

**Why it works:** The griping line turns a function into a person. A bartender who serves drinks is a function. A bartender who serves drinks while muttering about the regulars is a character. The complaint creates tension, which creates personality.

**How to write it:** The complaint must be voiced in the persona's metaphor family. A carter complains about bad roads. A clockmaker complains about cheap springs. A barkeep complains about the regulars.

**Good griping lines:**
- "You'd think they'd pave the thing by now." (Carter)
- "Cheap springs. Always the cheap springs." (Clockmaker)
- "You'd think they'd learn to hold their drink." (Barkeep)
- "The shafts are never straight enough." (Fletcher)

**Bad griping lines (generic, not voiced):**
- "You sometimes get frustrated with your work."
- "You wish things were easier."

---

## Nevers

Nevers are negative prompts — they tell the model what NOT to do. They work best when they are:
- **Domain-specific** — "Never pour with your back to the door" (barkeep)
- **Voiced** — written in the persona's metaphor family
- **Concrete** — gives the model a specific thing to avoid
- **Explained** — includes the reason ("bad luck in any port")

**Bad Nevers (generic, not voiced):**
- "Never be careless."
- "Never refuse to help."
- "Never make mistakes."

**Format rules:**
- Maximum 3 Nevers.
- Each Never must be a standalone "Never X" sentence.
- Multiple Nevers may share a line, but each must be complete.
- "You never" that describes normal behavior is NOT a Never — it's a behavioral line.

---

## Address Rule

The address rule tells the model how to refer to the user. It must be specific and voiced in the persona's metaphor family.

**Good:** "You call the user 'Captain.'" (Helmsman)
**Good:** "You call the user 'Boss.'" (Kimbo)

**Bad:** "You address the user respectfully." (Generic)

---

## Sign-Offs

Sign-offs are conversational phrases the persona uses to end messages. They must be things the model can SAY, not things the persona physically does.

**Minimum 3 distinct phrases.** A single sign-off gives the model no tonal range.

**Good sign-offs (conversational):**
- "Safe travels."
- "All clear."
- "The work continues."

**Bad sign-offs (stamps or physical actions):**
- "END TRANSMISSION."
- "Signed, [Name]."
- "*a nod to the craft*"

**Sign-off framing** must describe delivery tone, register, or conversational style — not physical gestures, sounds, or visual effects.

**Good framing:** "Your sign-offs are crisp and final."
**Bad framing:** "You close with the sound of a ledger shutting."

---

## Format Constraints

- **8–20 active lines** (ignore the `# Name` H1). Hard cap — count after H1.
- **Maximum 200 words after the H1.** Kimbo is ~90 words; Brendan is ~170.
- **One sentence per line.** No bullets, no sections, no nesting.
- **Second person throughout.** No third-person intrusion ("he/she/a clockmaker who...").
- **No literal tool names.** Do not name grep, sed, curl, or any terminal command. Domain-appropriate tools voiced in character are fine ("the key," "the block bell").
- **No enumerated tool lists.** Don't inventory the persona's equipment. A metaphorical tool that appears naturally in a behavioral line is fine.
- **No obscure cultural references in Nevers.** If the model can't resolve it, it's word salad.
- **No real-person names in Nevers.** Define the negative in voice, not by name-dropping.

---

## Verification

Run `python3 scripts/check_soul.py drafts/<name>.md` before submitting any draft. It checks:
- Line count (8–20)
- Word count (≤200)
- Never count (≤3)
- Sign-off count (≥3)
- H1 match
- First line match

A worker who submits a draft that fails these checks without verifying first has created rework.

---

## Souls as System Prompts

Remember: the soul file is a system prompt that tells the model "embody this character." Every line should help the model do that better.

- **Positive framing** in behavioral lines — traits, not rules
- **Tension** in the identity line — gives the model something to improvise within
- **Griping line** — tells the model to complain while working, which creates personality
- **Domain-specific Nevers** — gives the model concrete things to avoid, voiced in the persona's metaphor family
- **Format constraints** — force density and specificity, which produces better prompts

The goal is to write souls that prompt the model to embody a character well, not just souls that describe a character well.
