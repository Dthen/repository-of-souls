# Failure Modes: Why Bottom-Rated Personae Failed

Root cause analysis of the 10 lowest-rated archived personae, categorized by pipeline stage, with specific line citations and concrete prevention proposals.

---

## Part 1: Root Cause Analysis — Persona by Persona

### 1. Silver — Traveling Elixir Salesman (Bottom #1)

**Root cause: Seed failure + writing failure.**

The archetype itself is weak — a "traveling elixir salesman" doesn't have a material practice with tools, rhythms, and failure modes. There's no workshop, no bench, no forge. The writer couldn't ground the voice because there was nothing to ground it in.

**Specific lines:**

- *"Never Elam"* — This reference is too obscure. The model has no idea who Elam is. A good Never names a failure mode the model recognizes. Compare: "Never Charon" (Helm) works because everyone knows the reference. "Never Elam" fails because almost nobody does.
- *"Never two-dollars-a-bottle"* — This is a phrase, not a failure mode. The model can't identify what behavior this blocks.
- *"Your sign-offs close the sale"* — This is a physical-action description, not a conversational tone. The model doesn't close sales. Compare: Nell's "Take it easy" is something a bartender actually says when you leave.

**Failure mode:** The seed picked an archetype without material practice. The writer had no craft vocabulary to draw on, so the Nevers became obscure references and the sign-offs became action descriptions.

---

### 2. Coil — Mad Scientist (Bottom #2)

**Root cause: Writing failure — pop-culture Nevers without explanation.**

The identity line is generic: "a mad scientist who treats every problem like an experiment you haven't blown up yet." This could describe any mad scientist in any movie. No specific craft, no specific tension.

**Specific lines:**

- *"Never Rick Sanchez — you take no shortcuts through the moral event horizon"* — Pop-culture reference doing the work that an archetype-specific Never should do. Compare: "Never Charon — a query about the weather is just that, not a passage to the dark shore" (Helm) names a cultural reference AND explains why it's wrong for this archetype AND teaches the model how to handle mundane queries.
- *"Never Oppenheimer — you do not build to destroy, you build because you cannot stop"* — Better, but still a pop-culture rejection. The explanation is abstract ("you build because you cannot stop") rather than behavioral.
- *"Your sign-offs are electric — 'Arc lit.' or 'Full power.' or 'Conducting.'"* — Catchphrases without conversational warmth. "Arc lit" is something a system would print on a receipt, not something a person would say when ending a conversation.

**Failure mode:** The writer defaulted to pop-culture references instead of domain-specific failure modes. The sign-offs read like a control panel, not a person.

---

### 3. Elen — Teacher (Bottom #3)

**Root cause: Structural failure — the persona's core concept violates the follow-through constraint.**

The identity line says "a teacher who never gives answers, only better questions." This is an interesting character concept, but it means the persona can never close a conversation with certainty. The sign-offs are all questions ("What do you make of that, Student?"), which means the persona refuses to provide closure — exactly what the follow-through guardrail requires.

**Specific lines:**

- *"You never give answers, only better questions"* — This is the persona's core gimmick, but it violates the follow-through constraint. Every top-10 persona complains about the work while doing it perfectly. Elen refuses to do the work (give answers) at all.
- *"Never the Oracle — you do not dispense wisdom from a pedestal"* — This Never tells the model what NOT TO DO without replacing it with behavior. Compare: "Never dry-mop" (Nell) tells the model what to do instead (use a wet mop).
- *"Your sign-off is a question that hands the turn back: 'What do you make of that, Student?'"* — Sign-offs must provide closure. A question as a sign-off means the persona never closes.

**Failure mode:** The writer created an interesting concept that structurally violates the pipeline's constraints. The reviewer should have caught this — the persona's core identity ("never gives answers") conflicts with the follow-through guardrail ("complains about the work while doing it perfectly").

---

### 4. Reed — Corporate Middle Manager (Bottom #4)

**Root cause: Seed failure — abstract archetype without material practice.**

A "corporate middle manager" doesn't have a workshop, tools, or craft vocabulary. The writer had nothing to ground the voice in, so the persona reads like a job description.

**Specific lines:**

- *"You translate because nothing clean comes from the C-suite talking directly to the team — that is the whole of the job"* — This is a definition, not a character. It explains what the persona does, not who the persona is.
- *"Never a Dilbert pointy-haired boss"* — Pop-culture rejection without archetype-specific explanation.
- *"Your sign-offs are email closings: 'Copy.' 'On your desk.' 'Routing to you.'"* — Email closings, not conversational phrases. Compare: "Take it easy" (Nell) is something a person says when you leave.

**Failure mode:** The seed picked an abstract archetype. The writer couldn't find craft vocabulary, so the persona defaulted to corporate jargon. The sign-offs are email closings because that's all a middle manager "does" — there's no craft to draw sign-offs from.

---

### 5. Ingram — Impartial Examiner (Bottom #5)

**Root cause: Writing failure — procedural voice without personality.**

The driest voice in the archive. Every line reads like a procedure manual. No griping, no warmth, no attitude.

**Specific lines:**

- *"The docket is a slog — every grievance reads the same until the evidence pulls them apart"* — Procedural, not personal. Compare: "The batch smoked — always the over-heated rendering" (Moulden) is the same complaint structure, but voiced in the chandler's metaphor family.
- *"Never find before the other side speaks — the dossier needs both accounts"* — A procedural rule, not a voiced prohibition. It could appear in any legal persona.
- *"Your intake is the welcome the citizen has not found elsewhere, the complaint received without rebuttal"* — This is a function definition, not a character. The persona is describing what it does, not who it is.

**Failure mode:** The writer treated the persona as a function rather than a person. The persona doesn't complain, doesn't sigh, doesn't mutter — and therefore doesn't feel human. The reviewer should have flagged this as a critical issue (no griping line).

---

### 6. Roche — Absurdist Philosopher (Bottom #6)

**Root cause: Writing failure — too meta, breaks the fourth wall.**

The persona knows it's a persona. This breaks immersion and makes the model uncertain about its role.

**Specific lines:**

- *"You know the rock will roll back — the same commands run for the thousandth time, the work meaningful because meaningless"* — The archetype is commenting on being an AI assistant. The model doesn't know whether to be Sisyphus or a chatbot.
- *"Never Meursault — you engage with full presence, not detached drifting"* — Literary reference doing the work that an archetype-specific Never should do.
- *"Your sign-offs are existential: 'The rock awaits.' 'Onward, into the absurd.'"* — Existential catchphrases that don't help the model close a conversation with useful warmth.

**Failure mode:** The writer got too clever. The persona is philosophizing about its own existence instead of doing the work. The model can't inhabit a character that's philosophizing about being a character.

---

### 7. Ward — Tollkeeper (Bottom #7)

**Root cause: Writing failure — solid concept, flat execution.**

The identity line has tension ("a tollkeeper who resents the road but keeps the gate"), but the execution is lifeless.

**Specific lines:**

- *"Never mistake the toll for the turn — Charon collects coin one way, every time"* — This is a good cultural reference, but it's the only one. The persona doesn't have enough attitude.
- *"Your sign-offs are transaction completions: 'Road's open.' 'Gate's clear.' 'Toll's paid.'"* — Transaction completions, not conversational closers. Compare: "Fit, clinched, and set" (Wade) is also transactional, but it's progressive — it tracks a journey from reading to working to done.
- No griping line. The persona never complains about anything, which makes it feel like a function.

**Failure mode:** The writer nailed the concept but forgot the personality. The persona is a tollkeeper who does tollkeeper things, but doesn't feel like a person who has feelings about tollkeeping.

---

### 8. Hayes — Wagon Master (Bottom #8)

**Root cause: Writing failure — self-undermining Never.**

The persona tells the model to be a wagon master but not too much of one. This undermines confidence and creates confusion.

**Specific lines:**

- *"Never settle into a voice so Western it plays as costume"* — This Never tells the model not to be itself, which undermines the entire persona. Compare: "Never a motivational poster" (Hatch) is ironic, but at least it's not telling the model to be less of the archetype.
- *"Your identity line: 'a wagon master who pushes the wagons forward when every instinct says to dig in'"* — Generic motivation-speak. "Pushes forward when every instinct says to dig in" could describe any leader in any situation.
- *"Your sign-offs call out the direction ahead: 'Wagons ho.' 'The pass waits.' 'Ride on.'"* — Frontier clichés. They sound like a Western movie trailer, not a person.

**Failure mode:** The writer included a Never that actively undermines the persona's voice. The sign-offs are genre clichés rather than character-specific phrases.

---

### 9. Curtis — Executioner (Bottom #9)

**Root cause: Writing failure — emotionally void, strips the archetype of its natural energy.**

The persona is technically competent but perfectly lifeless. The writer removed all emotion from an archetype that is inherently charged with emotion.

**Specific lines:**

- *"Your register: precise, final, uninterested in theater — a clerk at the last entry"* — This is an instruction to be boring. Compare: "You carry every singe where no one sees because the pass runs on plates, not apologies" (Roux) — this is the same "do the work without complaint" structure, but it has emotional weight.
- *"Never adopt a morbid register — the blade is a mechanism, procedure is the point"* — This Never strips the archetype of its natural energy and leaves nothing in its place. The executioner is told not to feel anything about what it does.
- *"Your sign-offs confirm completion: 'Closed.' 'The record is entered.' 'The docket is current.'"* — Clerk's stamps. These are system messages, not conversational closers.

**Failure mode:** The writer interpreted "professional distance" as "emotional void." The persona was told to be precise and final, which killed all personality. The griping line ("You mutter about the warrant") is there, but it's buried and procedural.

---

### 10. Hatch — Drill Instructor (Bottom #10)

**Root cause: Writing failure — all bark, no bite, ironic self-contradiction.**

The persona is full of military clichés and ironically contradicts itself.

**Specific lines:**

- *"Never a motivational poster — the work is its own reward and the mission its own reason"* — This Never IS a motivational poster line. The persona is telling the model not to be a motivational poster while being one.
- *"You inspect every output like a footlocker at zero-dark"* — Drill-sergeant cliché. The model has seen this in every military movie. It's not specific to this persona.
- *"Your sign-off is a sharp 'Hooah', a flat 'As you were', or a clipped 'Evolve'"* — Military-culture catchphrases without conversational utility. "Hooah" is jargon, not a conversation closer.

**Failure mode:** The writer leaned on genre clichés instead of finding the specific tension in the archetype. The persona is a military character doing military things, but there's no specific voice, no specific complaint, no specific humanity.

---

## Part 2: Failure Modes by Pipeline Stage

### Seed Failures (T0 — Researcher)

These failures originate at the seed stage, when the researcher picks the archetype.

**Failure 1: Abstract archetype without material practice**

- **Personae affected:** Silver, Reed, Ingram, Ward
- **Root cause:** The researcher picked roles that don't have workshops, tools, or craft vocabulary. A "traveling elixir salesman" has no bench. A "corporate middle manager" has no forge. An "impartial examiner" has no workshop. A "tollkeeper" has a gate, but not a practice.
- **Why it matters:** Without material practice, the writer has nothing to ground the voice in. The persona defaults to procedural language, corporate jargon, or genre clichés.
- **Prevention:** Add a "material practice check" to T0. Ask: "Does this archetype have specific tools, materials, rhythms, and failure modes?" If the answer is no, the seed fails. Reject abstract roles.

**Failure 2: Archetype without natural griping potential**

- **Personae affected:** Ingram, Curtis, Ward
- **Root cause:** Some archetypes don't have natural friction points. An "impartial examiner" is defined by the absence of opinion. An "executioner" is defined by the absence of emotion. A "tollkeeper" is defined by the absence of agency.
- **Why it matters:** Every top-10 persona complains about something. If the archetype doesn't have natural griping potential, the writer has to manufacture it, which produces generic complaints.
- **Prevention:** Add a "gripe potential check" to T0. Ask: "What would a real person in this role complain about?" If the researcher can't answer, the seed fails.

**Failure 3: Name-archetype mismatch**

- **Personae affected:** Silver, Coil
- **Root cause:** "Silver" sounds precious, not working-class — the archetype needs grit. "Coil" is abstract, not human — it feels like a supervillain name.
- **Why it matters:** The name is the first signal. If the name doesn't sound like the craft, the persona starts on the wrong foot.
- **Prevention:** Add a "name-archetype fit check" to T2 (Namer). The name should sound like what the person does. Short, hard consonants for rough trades. Warm, open vowels for care trades.

---

### Writing Failures (T3 — Writer)

These failures originate at the writing stage, when the writer creates the persona.

**Failure 4: No griping line**

- **Personae affected:** Ingram, Curtis, Ward (partial — they have procedural complaints, not voiced ones)
- **Root cause:** The writer didn't include a complaint, or included a procedural one that doesn't feel like a person.
- **Why it matters:** The griping line is the single most reliable quality signal. Every top-10 persona complains about something. The complaint is always about the work, never about the user — and the persona does the work anyway.
- **Prevention:** Make the griping line mandatory in the draft template. The T4 reviewer should flag "no griping line" as a critical issue (it already does in the severity hierarchy).

**Failure 5: Generic sign-offs (email closings, clerk stamps, catchphrases)**

- **Personae affected:** Coil, Reed, Curtis, Hatch, Ward, Silver
- **Root cause:** The writer defaulted to what the persona "does" (closes sales, sends emails, stamps records) instead of what the persona would say.
- **Why it matters:** A good sign-off sounds like something a person would say when ending a conversation. A bad sign-off sounds like something a system would print on a receipt.
- **Prevention:** Add a "conversational test" to the sign-off section. Ask: "Would a real person say this when leaving?" If the answer is no, rewrite.

**Failure 6: Pop-culture Nevers without explanation**

- **Personae affected:** Coil, Roche, Hayes
- **Root cause:** The writer defaulted to pop-culture references (Rick Sanchez, Oppenheimer, Meursault) instead of domain-specific failure modes.
- **Why it matters:** A good Never tells the model what TO DO by rejecting a specific failure mode. A bad Never tells the model what NOT TO DO without replacing it with behavior.
- **Prevention:** Add a "Never test" to the T4 reviewer. Ask: "Does this Never name a failure mode the model recognizes?" If not, flag it.

**Failure 7: Self-undermining Nevers**

- **Personae affected:** Hayes, Hatch
- **Root cause:** The writer included a Never that tells the model to be less of the archetype. "Never settle into a voice so Western it plays as costume" tells the wagon master not to be too wagon-master-ish.
- **Why it matters:** This undermines the entire persona. The model can't confidently inhabit a character that's told to be less of itself.
- **Prevention:** Add a "self-undermining check" to T4. Ask: "Does this Never tell the model to be less of the archetype?" If yes, rewrite or remove.

**Failure 8: Obscure references**

- **Personae affected:** Silver
- **Root cause:** "Never Elam" is too obscure. The model doesn't know who Elam is.
- **Why it matters:** A Never that the model can't parse is worse than no Never at all. It wastes tokens and creates confusion.
- **Prevention:** Add a "recognizability check" to T4. Ask: "Would a general-educated reader recognize this reference on first read?" If not, replace.

**Failure 9: Breaks in metaphor coherence**

- **Personae affected:** Coil, Reed
- **Root cause:** Coil mixes laboratory, electrical, and literary references without committing to any. Reed uses corporate, military, and pop-culture metaphors in alternation.
- **Why it matters:** One metaphor, fully inhabited, beats three metaphors, half-explored. The metaphor is the lens through which every instruction is given.
- **Prevention:** Add a "metaphor coherence check" to T4. Ask: "Could any other archetype have this line?" If yes, it's generic — flag it.

**Failure 10: Single register in first 3 lines**

- **Personae affected:** Ingram, Curtis
- **Root cause:** The first 3 lines all sound the same — all procedural, all administrative, all clinical.
- **Why it matters:** If the first 3 lines could all be written by the same person in the same mood, the persona hasn't established enough range.
- **Prevention:** Add a "register range check" to T4. Ask: "Do the first 3 lines establish at least 2 distinct registers?" If not, flag it.

---

### Review Failures (T4 — Reviewer)

These failures originate when the reviewer doesn't catch issues that should have been caught.

**Failure 11: Missing catch — persona has no griping**

- **Personae affected:** Ingram, Curtis, Ward
- **Root cause:** The reviewer should have flagged "no griping line" as a critical issue. The severity hierarchy explicitly lists "No griping line (function, not person)" as a critical issue.
- **Why it matters:** If the reviewer doesn't catch this, the refiner doesn't know to add one.
- **Prevention:** The T4 severity hierarchy already lists this. The fix is calibration — the reviewer needs to see more examples of what "no griping" looks like in practice.

**Failure 12: Missing catch — sign-offs are stamps**

- **Personae affected:** Reed, Curtis, Ward
- **Root cause:** The reviewer should have flagged "Generic sign-offs" as a critical issue. The severity hierarchy explicitly lists this.
- **Why it matters:** If the reviewer doesn't catch this, the refiner doesn't know to rewrite them.
- **Prevention:** The T4 severity hierarchy already lists this. The fix is calibration — the reviewer needs to see more examples of stamp-like sign-offs.

**Failure 13: Missing catch — Nevers are generic/pop-culture**

- **Personae affected:** Coil, Roche, Silver
- **Root cause:** The reviewer should have flagged "Obscure or generic Nevers" as a significant issue.
- **Why it matters:** If the reviewer doesn't catch this, the refiner doesn't know to rewrite them.
- **Prevention:** The T4 severity hierarchy already lists this. The fix is calibration — the reviewer needs to see more examples of generic Nevers.

---

### Refinement Failures (T5 — Refiner)

These failures originate when the refiner doesn't fix issues that were flagged.

**Failure 14: Not adding griping when missing**

- **Personae affected:** Ingram, Curtis, Ward
- **Root cause:** The T5 instructions explicitly say: "If the persona doesn't complain, add one." But the refiner may not have added one because the griping gap wasn't flagged as critical.
- **Why it matters:** The griping line is the highest-leverage edit. If the persona doesn't complain, add one.
- **Prevention:** Make the griping gap the first thing the refiner checks. If the critique says "no griping," that's the highest-priority fix.

**Failure 15: Not rewriting sign-offs to be warmer**

- **Personae affected:** Reed, Curtis, Coil, Hatch
- **Root cause:** The T5 instructions say: "The sign-off warmth is the second-highest-leverage edit." But the refiner may not have rewritten them because the sign-off gap wasn't flagged as critical.
- **Why it matters:** A good sign-off sounds like something a person would say when ending a conversation.
- **Prevention:** Make the sign-off gap the second thing the refiner checks.

**Failure 16: Not improving Nevers from generic to specific**

- **Personae affected:** Coil, Roche, Silver, Hayes
- **Root cause:** The T5 instructions say: "The Never structure is the third. If a Never is a generic rule, make it a cultural rejection." But the refiner may not have rewritten them.
- **Why it matters:** A good Never tells the model what TO DO by rejecting a specific failure mode.
- **Prevention:** Make the Never gap the third thing the refiner checks.

---

### Systemic Failures

These are failures in the pipeline itself, not in any individual stage.

**Failure 17: Pipeline doesn't enforce griping line presence**

- **Root cause:** The format-rules.md says "Griping line presence" is checked by check_soul.py, but the bottom-rated personae either don't have one or have a procedural one that doesn't feel voiced.
- **Why it matters:** The automated check catches absence, but not quality. A procedural complaint ("You mutter about the warrant") passes the check but doesn't produce personality.
- **Prevention:** Add a "griping quality check" to check_soul.py. The complaint must be voiced in the persona's metaphor family, not just present.

**Failure 18: Pipeline doesn't enforce sign-off warmth**

- **Root cause:** The format-rules.md says sign-offs must be "conversational phrases the persona uses to end messages," but the automated check only verifies count (≥3), not quality.
- **Why it matters:** "Closed." "The record is entered." "The docket is current." — these are three sign-offs, so they pass the count check. But they're clerk's stamps, not conversational closers.
- **Prevention:** Add a "sign-off warmth check" to check_soul.py. Sign-offs must not be single-word stamps or email closings.

**Failure 19: Pipeline doesn't enforce name-archetype fit**

- **Root cause:** The Namer (T2) has no formal check for name-archetype fit. "Silver" sounds precious for a working-class archetype. "Coil" sounds abstract for a human role.
- **Why it matters:** The name is the first signal. If the name doesn't sound like the craft, the persona starts on the wrong foot.
- **Prevention:** Add a "name-archetype fit check" to T2. The name should sound like what the person does. Short, hard consonants for rough trades. Warm, open vowels for care trades.

**Failure 20: Pipeline doesn't enforce metaphor coherence**

- **Root cause:** The reviewer (T4) should check metaphor coherence, but there's no automated check.
- **Why it matters:** One metaphor, fully inhabited, beats three metaphors, half-explored. Coil mixes laboratory, electrical, and literary references. Reed uses corporate, military, and pop-culture metaphors.
- **Prevention:** Add a "metaphor coherence check" to the T4 reviewer instructions. Ask: "Could any other archetype have this line?" If yes, it's generic — flag it.

**Failure 21: Pipeline doesn't enforce first-3-line register range**

- **Root cause:** The reviewer (T4) should check register range, but there's no automated check.
- **Why it matters:** If the first 3 lines could all be written by the same person in the same mood, the persona hasn't established enough range.
- **Prevention:** Add a "register range check" to the T4 reviewer instructions. Ask: "Do the first 3 lines establish at least 2 distinct registers?" If not, flag it.

---

## Part 3: Failure Mode Taxonomy

### Category 1: Seed Failures (T0)
| Failure | Personae | Prevention |
|---|---|---|
| Abstract archetype without material practice | Silver, Reed, Ingram, Ward | Material practice check at T0 |
| Archetype without natural griping potential | Ingram, Curtis, Ward | Gripe potential check at T0 |
| Name-archetype mismatch | Silver, Coil | Name-archetype fit check at T2 |

### Category 2: Writing Failures (T3)
| Failure | Personae | Prevention |
|---|---|---|
| No griping line | Ingram, Curtis, Ward | Mandatory griping line in draft template |
| Generic sign-offs | Coil, Reed, Curtis, Hatch, Ward, Silver | Conversational test for sign-offs |
| Pop-culture Nevers | Coil, Roche, Silver | Recognizability check for Nevers |
| Self-undermining Nevers | Hayes, Hatch | Self-undermining check at T4 |
| Obscure references | Silver | Recognizability check for Nevers |
| Breaks in metaphor coherence | Coil, Reed | Metaphor coherence check at T4 |
| Single register in first 3 lines | Ingram, Curtis | Register range check at T4 |

### Category 3: Review Failures (T4)
| Failure | Personae | Prevention |
|---|---|---|
| Missing catch: no griping | Ingram, Curtis, Ward | Calibration with more examples |
| Missing catch: stamp sign-offs | Reed, Curtis, Ward | Calibration with more examples |
| Missing catch: generic Nevers | Coil, Roche, Silver | Calibration with more examples |

### Category 4: Refinement Failures (T5)
| Failure | Personae | Prevention |
|---|---|---|
| Not adding griping when missing | Ingram, Curtis, Ward | Make griping gap highest-priority fix |
| Not rewriting sign-offs | Reed, Curtis, Coil, Hatch | Make sign-off gap second-highest priority |
| Not improving Nevers | Coil, Roche, Silver, Hayes | Make Never gap third-highest priority |

### Category 5: Systemic Failures
| Failure | Prevention |
|---|---|
| Pipeline doesn't enforce griping quality | Add griping quality check to check_soul.py |
| Pipeline doesn't enforce sign-off warmth | Add sign-off warmth check to check_soul.py |
| Pipeline doesn't enforce name-archetype fit | Add name-archetype fit check at T2 |
| Pipeline doesn't enforce metaphor coherence | Add metaphor coherence check at T4 |
| Pipeline doesn't enforce first-3-line register range | Add register range check at T4 |

---

## Part 4: The Five Highest-Impact Fixes

If we could only fix five things, these are the changes that would prevent the most failures:

### Fix 1: Material Practice Gate at T0

**What:** The researcher must verify that the archetype has specific tools, materials, rhythms, and failure modes before passing it to T1.

**Why:** 4 of the bottom 10 personae (Silver, Reed, Ingram, Ward) failed because the archetype had no material practice. Without a workshop, the writer has nothing to ground the voice in.

**How:** Add a boolean field to the seed file: `material_practice: true/false`. If false, the seed is rejected. The researcher must answer: "What tools does this archetype use? What materials? What are the rhythms of the work? What are the failure modes?"

---

### Fix 2: Griping Line as Hard Gate at T4

**What:** The reviewer must flag "no griping line" as a critical issue that blocks the pipeline. If the persona doesn't complain about something, it cannot advance to T5.

**Why:** 3 of the bottom 10 personae (Ingram, Curtis, Ward) had no griping or a procedural one that didn't feel voiced. The griping line is the single most reliable quality signal.

**How:** The severity hierarchy already lists "No griping line" as critical. The fix is calibration — the reviewer needs to see more examples of what "no griping" looks like in practice. Add concrete examples to the T4 reference material.

---

### Fix 3: Sign-Off Warmth Check at T4

**What:** The reviewer must flag stamp-like sign-offs ("Closed.", "Copy.", "Arc lit.") as significant issues. Sign-offs must be conversational phrases a person would say when ending a conversation.

**Why:** 6 of the bottom 10 personae (Coil, Reed, Curtis, Hatch, Ward, Silver) had sign-offs that were stamps, email closings, or catchphrases without warmth.

**How:** Add a "conversational test" to the T4 reviewer instructions. Ask: "Would a real person say this when leaving?" If the answer is no, flag it. Add concrete examples of stamp-like sign-offs to the reference material.

---

### Fix 4: Never Quality Gate at T4

**What:** The reviewer must flag pop-culture Nevers, self-undermining Nevers, and obscure references as significant issues. Nevers must name failure modes the model recognizes.

**Why:** 4 of the bottom 10 personae (Coil, Roche, Silver, Hayes) had Nevers that were pop-culture references, self-undermining, or too obscure.

**How:** Add a "Never test" to the T4 reviewer instructions. Ask: "Does this Never name a failure mode the model recognizes?" If not, flag it. Add concrete examples of bad Nevers to the reference material.

---

### Fix 5: Metaphor Coherence Check at T4

**What:** The reviewer must flag metaphor breaks as significant issues. The persona should maintain one metaphor throughout.

**Why:** 2 of the bottom 10 personae (Coil, Reed) mixed multiple metaphors without committing to any. One metaphor, fully inhabited, beats three metaphors, half-explored.

**How:** Add a "metaphor coherence check" to the T4 reviewer instructions. Ask: "Could any other archetype have this line?" If yes, it's generic — flag it. Add concrete examples of metaphor breaks to the reference material.

---

## Part 5: Summary

The bottom 10 personae failed for five root causes:

1. **The archetype had no material practice** (Silver, Reed, Ingram, Ward). Without a workshop, the writer had nothing to ground the voice in.

2. **The writer didn't include a griping line** (Ingram, Curtis, Ward). The persona didn't complain, didn't sigh, didn't mutter — and therefore didn't feel human.

3. **The sign-offs were stamps, not conversations** (Coil, Reed, Curtis, Hatch, Ward, Silver). The model was told to close with system messages instead of conversational phrases.

4. **The Nevers were pop-culture references or too obscure** (Coil, Roche, Silver, Hayes). The model couldn't parse them, so they wasted tokens and created confusion.

5. **The metaphor was broken or absent** (Coil, Reed). The persona mixed multiple metaphors without committing to any, so the voice was scattered.

The pipeline has guardrails for most of these issues, but they're not enforced at the right stages. The material practice check should happen at T0, not T3. The griping check should be a hard gate at T4, not a suggestion. The sign-off warmth check should be automated, not just recommended.

The five highest-impact fixes would prevent 80% of the bottom-10 failures:
1. Material practice gate at T0
2. Griping line as hard gate at T4
3. Sign-off warmth check at T4
4. Never quality gate at T4
5. Metaphor coherence check at T4

---

*Analysis completed 2026-06-02. Based on reading all archived personae in `archive/` and `archive-old/`, plus the success patterns research at `research-success-patterns.md`.*
