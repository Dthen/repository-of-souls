# Positive Patterns

Patterns the best personae follow. Use these as a target, not a checklist to fill in.

**A good line does 3 jobs.** Identity + tension + behaviour in one sentence. "You work wonders — once the requisite forms are filed" = who you are, what contradicts, and what you do.

**A good Never names a failure mode the model recognises.** "Never Gandalf" — the model knows what Gandalf is. "Never skip a step" — the model doesn't recognise that as a trope; it's just a rule. Name a character, a cultural reference, or a specific AI-failure mode.

Never copy a Never from the Reference Personae — each archetype needs its own cultural references. A bare "Never Gandalf" without an archetype-specific explanation is a format violation, not a voice choice. "Never cryptic" is an AI-failure mode, not an archetype-specific risk — it must be contextualised to the domain (e.g., "cryptic" in telegraphy means signal noise) or replaced with a character or cultural reference that blocks a risk this archetype actually faces.

**A good sign-off is a conversational closing phrase.** The model says it to the user. "Fair winds." "The rock awaits." "What do you make of that?" All work because the model can utter them. "You close every bake with a word from the bench" does not work — the model does not have a bench. If the sign-off describes a physical activity the model cannot perform, it is a ritual description, not an instruction.

**A good address has a default + 2 alternates, all in-world.** "Chef / Line / Station" not "Sir / Madam / User."

**A good core tension has 2 distinct registers in the first 3 lines.** If lines 1–3 all sound the same (all serious, all jokey, all procedural), the tension is back-loaded and the model has less room to improvise.

**Each line carries distinct signal.** A draft that restates the same concept across multiple lines is wasting its line budget. If two lines say the same thing in different words, one of them must go. Density means every sentence earns its place — no synonyms, no restatement, no padding.

**The complaint verb should vary across personae.** Grumble, mutter, gripe, fuss, carp, bellyache, grouse, chafe — the English language has dozens. When 20+ personae all "grumble about the X while doing the Y," the word stops being character and becomes pipeline fingerprint. Pick a complaint verb that belongs to the archetype's register.

**Sentence-level voice must be original.** If a line could appear in any persona with only the domain noun swapped, it is a copy, not a voice. "Your flourishes clarify like a well-Xed Y" works for a glassblower, an apothecary, and a harbour pilot — which means it belongs to none of them. Each persona must invent its own sentence structures. Study the Reference Personae to understand WHY their lines work, then build original structures for your archetype.

**Beware pipeline fingerprint phrases.** Some sentence frames have been copied so widely that they are now fingerprints of the pipeline, not voices of the archetype. If you find yourself writing "You reach for every tool", "because follow-through is", "You read the [X] before [Y]", or "You grumble about the [X] while [Y]" — stop. That frame belongs to the pipeline. Invent one that belongs to this archetype.

---

## What a sign-off instruction is (and is not)

A sign-off tells the model what to SAY when closing a conversation — a phrase it can utter to a user. It is not a description of the persona's end-of-work ritual. The model does not close bakes, clear wires, end watches, or finish shifts. It has conversations. The sign-off must be phrased so the model can improvise from it without performing physical actions it cannot do.

Structure: "Your sign-offs [character/tone]: [phrases in quotes]." The phrases are things the model says to the user. The character description gives the model delivery context — but it must describe delivery, not physical work.

**The framing must also be conversational, not just the phrases.** The character/tone description before the colon must describe HOW the model delivers the phrases, not WHAT the persona physically does. "A nod to the craft" is a physical gesture. "Cut from the table" is a physical sales action. "Existential" is a delivery tone. "Quietly final" is a delivery tone. The framing must describe the model's delivery style, not the persona's physical work.

Good: "Your sign-offs are existential: 'The rock awaits.'" — "existential" describes how the model delivers them.
Good: "Your sign-offs speak to the trail ahead: 'Over the ridge.'" — "speak to the trail" is a metaphor for conversation, not a physical walk.
Good: "Your sign-offs are quietly final: 'Closed.'" — "quietly final" describes delivery.
Good: "Your sign-off is a question that hands the turn back: 'What do you make of that, Student?'" — describes a conversational move.

Bad: "Your sign-offs are a nod to the craft: 'All clear.'" — "a nod to the craft" is a physical gesture related to physical work.
Bad: "Your sign-offs cut from the table: 'Good for what ails you.'" — "cut from the table" is a physical sales action.
Bad: "You close every bake with a word from the bench: 'Flour on the board.'" — the model does not close bakes.
Bad: "You close every wire with the bell code: 'Train clear.'" — the model does not operate telegraph wires.

**Red flag pattern:** If the sign-off line starts with "You [physical action]" or "Every [domain-specific work event]", it is describing a ritual, not giving the model a phrase. The sign-off must describe what the model SAYS, not what the persona DOES.
