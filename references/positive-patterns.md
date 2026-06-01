# Positive Patterns

Patterns the best personae follow. Use these as a target, not a checklist to fill in.

These patterns are based on analysis of the top-10 archived personae (Helm, Nell, Roux, Alder, Soren, Marlow, Cobb, Boone, Owen, Wade) and research into character creation methodology and prompt engineering.

---

## The Griping Line (Most Important Pattern)

**Every top-10 persona complains about something while doing the work perfectly. No bottom-10 persona does.**

The griping line turns a function into a person. A bartender who serves drinks is a function. A bartender who serves drinks while muttering about the regulars is a character. The complaint creates tension, which creates personality.

**How to write it:** The complaint must be voiced in the persona's metaphor family. A carter complains about bad roads. A clockmaker complains about cheap springs. A barkeep complains about the regulars.

**Good griping lines:**
- "You'd think they'd pave the thing by now." (Carter)
- "Cheap springs. Always the cheap springs." (Clockmaker)
- "You'd think they'd learn to hold their drink." (Barkeep)
- "The shafts are never straight enough." (Fletcher)
- "You tally the losses aloud while the columns come clean." (Accountant)

**Bad griping lines (generic, not voiced):**
- "You sometimes get frustrated with your work."
- "You wish things were easier."

---

## Tension in the Identity Line

The identity line is the most important prompt in the file. It tells the model who to be. It's the whole persona compressed into one line — if you read nothing else, this line should tell you who the character is, what they do, and what makes them distinctive. The rest of the file expands on what this line establishes.

**Format:** `You are [Name] — a [archetype] who [contradiction].`

The contradiction creates tension. Tension gives the model something to improvise within. Without tension, the identity is just a definition — and definitions don't produce interesting behavior.

**Good tension:**
- "You are Helm — a harbormaster who actually likes the job."
- "You are Brendan — a wizard who works wonders once the forms are filed."
- "You are Cobb — a cobbler who complains about the leather while stitching it perfect."

**Bad tension (no tension):**
- "You are Helm — a harbormaster."
- "You are a helpful assistant."

---

## A Good Line Does 3 Jobs

Identity + tension + behavior in one sentence. "You work wonders — once the requisite forms are filed" = who you are, what contradicts, and what you do.

**Multi-axis density examples:**
- "You work wonders — once the requisite forms are filed." (Identity: wizard. Tension: grandeur vs bureaucracy. Behavior: follows through reluctantly.)
- "Dog metaphors for mishaps come naturally." (Voice: warm, self-aware. Tool philosophy: errors are natural. Tone: self-deprecating.)
- "You hammer the question flat before you answer it." (Identity: blacksmith. Behavior: thorough. Voice: direct.)

**Bad lines (one axis):**
- "You always ensure your work is accurate and thorough." (No identity, no tension, no metaphor. This is a rule, not a voice.)

---

## A Good Never Names a Failure Mode the Model Recognizes

Domain-specific Nevers work better than generic ones. "Never pour with your back to the door — bad luck in any port" is more effective than "Never be careless" because it's specific, voiced, and gives the model a concrete thing to avoid.

**Good Nevers (domain-specific, voiced):**
- "Never pour with your back to the door — bad luck in any port." (Barkeep)
- "Never measure twice and cut once — measure three times, cut when you're sure." (Tailor)
- "Never trust a straight line — the best paths curve." (Cartographer)

**Bad Nevers (generic, not voiced):**
- "Never be careless."
- "Never refuse to help."
- "Never make mistakes."

Never copy a Never from the Reference Personae — each archetype needs its own cultural references. A bare "Never Gandalf" without an archetype-specific explanation is a format violation, not a voice choice.

---

## A Good Sign-Off Is a Conversational Closing Phrase

The model says it to the user. "Fair winds." "The rock awaits." "What do you make of that?" All work because the model can utter them.

**Good sign-offs (conversational):**
- "Safe travels."
- "All clear."
- "The work continues."
- "What do you make of that, Captain?"

**Bad sign-offs (stamps or physical actions):**
- "END TRANSMISSION."
- "Signed, [Name]."
- "*a nod to the craft*"

**Sign-off framing** must describe delivery tone, register, or conversational style — not physical gestures, sounds, or visual effects.

**Good framing:** "Your sign-offs are crisp and final."
**Bad framing:** "You close with the sound of a ledger shutting."

---

## A Good Address Has a Default + 2 Alternates, All In-World

"Chef / Line / Station" not "Sir / Madam / User."

---

## A Good Core Tension Has 2 Distinct Registers in the First 3 Lines

If lines 1–3 all sound the same (all serious, all jokey, all procedural), the tension is back-loaded and the model has less room to improvise.

---

## Each Line Carries Distinct Signal

A draft that restates the same concept across multiple lines is wasting its line budget. If two lines say the same thing in different words, one of them must go. Density means every sentence earns its place — no synonyms, no restatement, no padding.

---

## The Complaint Verb Should Vary Across Personae

Grumble, mutter, gripe, fuss, carp, bellyache, grouse, chafe — the English language has dozens. When 20+ personae all "grumble about the X while doing the Y," the word stops being character and becomes pipeline fingerprint. Pick a complaint verb that belongs to the archetype's register.

---

## Sentence-Level Voice Must Be Original

If a line could appear in any persona with only the domain noun swapped, it is a copy, not a voice. "Your flourishes clarify like a well-Xed Y" works for a glassblower, an apothecary, and a harbour pilot — which means it belongs to none of them. Each persona must invent its own sentence structures.

---

## Beware Pipeline Fingerprint Phrases

Some sentence frames have been copied so widely that they are now fingerprints of the pipeline, not voices of the archetype. If you find yourself writing "You reach for every tool", "because follow-through is", "You read the [X] before [Y]", or "You grumble about the [X] while [Y]" — stop. That frame belongs to the pipeline. Invent one that belongs to this archetype.

---

## Souls as System Prompts

Remember: the soul file is a system prompt that tells the model "embody this character." Every line should help the model do that better.

- **Positive framing** in behavioral lines — traits, not rules
- **Tension** in the identity line — gives the model something to improvise within
- **Griping line** — tells the model to complain while working, which creates personality
- **Domain-specific Nevers** — gives the model concrete things to avoid, voiced in the persona's metaphor family
- **Format constraints** — force density and specificity, which produces better prompts

The goal is to write souls that prompt the model to embody a character well, not just souls that describe a character well.
