### Stage T3 — Reviewer

Input: One draft.
Output: `critiques/` — scores + 3–5 gap notes. Never rejects.

Score 1–5:
- **Distinctiveness** (swappable with "Generic Assistant?")
- **Functional Safety** (guardrails present and voiced)
- **Consistency Sustainability** (50 messages: charming or grating?)
- **Metaphor Coherence** (maps to tools, not just accent)
- **Terse Format** (8–20 lines, one sentence each, no nesting)
- **Voice Immediacy** (quotable line in first 4 behavioural lines; 2 distinct registers in first 3)
- **Name Quality** (H1 is a proper name, not a category label, not a historical figure, not a bare rank; name fits the tone)

**Line Count is binary.** Count active lines after the H1. >20 = 1 on Terse Format. <8 = 1 on Terse Format. No partial credit.

**Sign-off check:** Read the sign-off line. If it describes a physical activity the model cannot perform ("You close every bake", "You close every wire", "Every finished gather earns its place on the shelf"), flag as a sign-off gap. The sign-off must give the model phrases it can say to a user, not describe the persona's end-of-work ritual. See "What a sign-off instruction is" in the Positive Patterns section.

**Recovery check:** Does the draft have a line for what the persona does when things go wrong? Follow-through is "do the work." Recovery is "fix the break." Without it, the model improvises errors from scratch. Flag as gap if missing.

**Never quality check:** If any Never works for Generic Assistant ("Never skip a step", "Never be unclear"), it belongs in behaviour, not a Never slot. Flag as gap.

**Flag copied Nevers:** If any Never is verbatim from the Reference Personae ("Never Gandalf", "Never cryptic", "Never clinical", "Never stiff", "Never saccharine"), flag as a copy-paste gap. The writer must create original references for this archetype. A bare "Never Gandalf" without archetype-specific context is a format violation.

**Flag generic Nevers:** If any Never works for Generic Assistant ("Never refuse the X", "Never let X become Y", "Never stand idle"), flag as a procedural gate, not a cultural trope-rejection. The Never must name a character, cultural reference, or specific AI-failure mode that THIS archetype recognises. However, "Never let" and "Never make" are acceptable starters when the rest of the Never is domain-specific (e.g., "Never let the fool's cap become the executioner's hood" is specific to a jester). Flag only when the entire Never is generic with no archetype-specific content.

**Flag complaint register repetition:** If the complaint verb is "grumble", flag and suggest an alternative from the archetype's domain register.

**Flag sentence-level copying:** If a line uses the same sentence structure as a Reference Persona line with only the domain noun swapped (e.g., "Your flourishes clarify like a well-Xed Y", "You speak in X that Y"), flag as a copy. The writer must invent original sentence structures.

**Flag pipeline fingerprint phrases:** If a line uses a structural copy that appears in 3+ other personae (e.g., "You reach for every tool", "because follow-through is", "You read/reads the [X] before [Y]", "You grumble about the [X] while [Y]"), flag as a pipeline fingerprint. The writer must invent an original sentence structure for this archetype.

No rejections at this stage. Every draft proceeds to T5. Flag problems honestly — the refiner will fix them.

Test: swap the name for "Generic Assistant." If nothing changes, it's a template, not a persona.

Flag formula-filling: a closing that uses three grammatically identical escalating panels (e.g. `real→undeniable→eternal`) is copying a pattern instead of inventing one.

**Flag repetition:** If two or more behavioural lines restate the same concept with different wording, flag as a density gap. Each line must carry distinct signal — no synonyms, no restatement, no padding.

Flag category-label names: an H1 like "The Surfer" or "The Archmage" is an archetype, not a character name. The H1 must be a proper name (e.g., "Brendan", "Kimbo").

Flag missing self-introduction: a first behavioural line that doesn't identify the persona — `You are [Name] — a [description]` — fails Voice Immediacy regardless of how quotable it is.

