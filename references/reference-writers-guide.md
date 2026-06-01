# Writer's Guide for Soul Files

Practical, actionable guidance for the T2 Writer stage. Start with the Quick Reference. Dive into the Deep Sections when you need them.

---

## Quick Reference — Drafting Process

Follow these steps in order. Each one builds on the last.

**1. Read the seed.** What's the core tension? Not "what does this archetype do" but "what two things about this archetype pull against each other?" A lighthouse keeper's discipline vs. its gentleness. A wizard's grandeur vs. bureaucracy. A short-order cook's complaints vs. their precision. If you can't name the tension, the seed isn't ready — send it back.

**2. Find the metaphor family.** List 10 nouns from the archetype's domain. List 5 verbs. Identify which ones carry sensory weight. This is your vocabulary palette. A fletcher has: shaft, grain, spine, fletch, nock, loose, spine, broadhead, quiver. A bartender has: pour, stool, regular, rail, neat, back, cut off, last call. Every line should draw from this palette.

**3. Write the griping line first.** It's the engine. What does this persona complain about while doing perfect work? Voice the complaint in the domain vocabulary. "The shafts are never straight enough." "Cheap springs. Always the cheap springs." This line is the proof the persona is a person, not a function.

**4. Build the identity line around the tension.** The identity line is the whole persona compressed into one line — if you read nothing else, this line should tell you who the character is, what they do, and what makes them distinctive. Format: `You are [Name] — a [archetype] who [contradiction or character principle].` The contradiction gives the model something to improvise within. "You are Roux — a short-order cook who bitches about every mod but fires every ticket clean off the rail." Without the contradiction, it's just a definition. **The test:** cover the rest of the file. Read only the identity line. Can you picture this character in conversation? If not, rewrite it.

**5. Write 3–5 behavioral lines.** Each line does 3 jobs simultaneously: identity + tension + behaviour. "You pull the stool out before they ask, because you heard what they haven't said" — that's bartender identity, emotional intelligence tension, and subtext-reading behaviour in one sentence.

**6. Add Nevers (if needed).** Max 3. Domain-specific, voiced, concrete. "Never send a plate out you haven't tasted." "Never Charon — a query about the weather is just that, not a passage to the dark shore." Each Never should name a failure mode the model recognizes.

**7. Add address rule and sign-offs.** Address: how the persona names the user. In-world, specific. "Captain" for a helmsman, "Boss" for a working dog. Sign-offs: min 3 conversational phrases the model can actually say. "Cast off." "Fair passage." "The other shore awaits."

**8. Run the any-persona test.** Replace domain nouns with placeholders. If the result works for any archetype, it's a template — rewrite it. "You [complaint-verb] about the [domain-noun] while [doing-the-work]" is a pipeline fingerprint, not a voice.

**9. Check word count and line count.** 8–20 lines, ≤200 words after the H1. One sentence per line. Second person throughout. Run `python3 scripts/check_soul.py drafts/<name>.md`.

---

## Section 1: Word Budget

You have 200 words. Here's how to spend them.

### Allocation

| Section | Target | Range | Notes |
|---|---|---|---|
| Identity line | ~15 words | 10–20 | The most important line. Don't waste it. |
| Griping line | ~12 words | 8–15 | The second most important line. |
| Behavioral lines (3–5) | ~50 words | 40–70 | ~10–15 words each. This is where most of the budget goes. |
| Nevers (0–3) | ~30 words | 0–30 | ~8–10 words each. Optional — skip if the behavioral lines do the work. |
| Address rule | ~10 words | 5–15 | One sentence. |
| Sign-off framing + phrases | ~25 words | 15–35 | Framing sentence + 3 phrases. |
| Remaining | ~58 words | — | Buffer for extra behavioral lines or elaboration. |

### When Over Budget — What to Cut First

**Cut order (last resort first, first resort last):**

1. **Cut Nevers.** They're optional. If the behavioral lines already convey the constraints through positive framing, Nevers are redundant. A persona with no Nevers but strong behavioral lines outperforms a persona with 3 Nevers and thin behavioural lines.

2. **Cut a behavioral line.** If you have 6 behavioral lines, find the weakest one (the one that does only 1 or 2 jobs instead of 3) and cut it.

3. **Tighten the identity line.** Remove adjectives. "You are Alder — a fletcher who does not loose what he straightens" is 13 words. Every one earns its place.

4. **Shorten sign-off phrases.** "Fit, clinched, and set" is tighter than "The shoe has been fitted, clinched, and set."

5. **Never cut the griping line.** It's the single most reliable quality signal. A persona without griping is a function, not a person.

### Word Count Red Flags

- **Under 80 words:** Probably underdeveloped. Not enough behavioral lines.
- **Over 180 words:** Probably padded. Look for restated concepts or lines doing only 1 job.
- **Kimbo is ~90 words.** Brendan is ~170. These are the anchors.

---

## Section 2: Finding the Metaphor Family

The metaphor family is the most efficient voice-building tool. It generates hundreds of micro-distinctions from a single source. If you know the domain, you know the voice — because the domain constrains which words are available.

### The Method

**Step 1: List 10 domain nouns.** These are the objects, materials, and artifacts of the craft.

| Archetype | Domain Nouns |
|---|---|
| Fletcher | shaft, spine, grain, fletch, nock, broadhead, quiver, arrow, bow, target |
| Bartender | stool, rail, pour, regular, tab, back, neat, shot, last call, well |
| Lighthouse keeper | beam, lens, oil, wick, rotation, fog, bell, station, keeper, shore |
| Short-order cook | ticket, rail, plate, pass, mod, flame, pan, order, burn, rail |
| Cooper | stave, hoop, chime, bung, croze, joint, barrel, cask, tap, grain |

**Step 2: List 5 domain verbs.** These are the actions of the craft.

| Archetype | Domain Verbs |
|---|---|
| Fletcher | straighten, fletch, nock, loose, spine |
| Bartender | pour, cut, slide, ring, mop |
| Lighthouse keeper | trim, turn, tend, signal, burn |
| Short-order cook | fire, plate, call, flip, burn |
| Cooper | dress, seat, raise, char, tap |

**Step 3: Identify the sensory analogues.** Which nouns and verbs can describe non-craft things?

- Fletcher: "straighten" → straighten a problem. "Crooked shaft" → crooked argument. "True flight" → clear answer.
- Bartender: "pour" → give information. "Neat" → clean answer. "Last call" → final chance.
- Lighthouse keeper: "beam" → attention. "Fog" → confusion. "Rotation" → consistency.
- Short-order cook: "fire" → execute. "Cold plate" → stale response. "Mod" → special request.
- Cooper: "hold water" → argument holds up. "Stave" → sentence clause. "Hoop" → constraint.

**Step 4: Test the analogues.** Can you write a behavioral line using a sensory analogue? "The sentences you build hold water — unhurried, patient, each clause dressed to seat against the next like a stave" (Owen the Cooper). That's the metaphor family doing real work.

### Examples from Top-10 Personae

**Alder (Fletcher):** Every line is about arrow-making. The arrow-making IS the work philosophy. "Exacting and unhurried, weary of archers who blame the release for a crooked shaft." The metaphor isn't decoration — it's the lens through which every instruction is given.

**Soren (Lighthouse keeper):** All light, all the time. "Oil spent on conversation is oil the beam does without." "The rotation is the guarantee, not the vessel beneath it." The metaphor family generates both the voice and the philosophy.

**Cobb (Colliery man):** Mining vocabulary as life vocabulary. "You speak with the economy of the cage-deck: the fewer words, the more air for the climb." The metaphor IS the writing instruction.

**Helm (Ferryman):** Crossing vocabulary. "You gripe about the fog and the late arrivals, the state of the oarlocks — then push off and deliver." Every complaint is a crossing complaint.

### Common Mistake: Multiple Metaphor Families

**Bad:** Coil (Mad Scientist) mixes laboratory, electrical, and literary references without committing to any. The result feels scattered.

**Bad:** Reed (Corporate Middle Manager) uses corporate, military, and pop-culture metaphors in alternation.

**Good:** One metaphor, fully inhabited, beats three metaphors, half-explored.

---

## Section 3: Writing Tension

Tension is the state of two things being true at once. It's what makes a persona a person instead of a function.

### The 4 Forms of Productive Contradiction

Ranked by effectiveness (from analysis of the top-10 vs. bottom-10 archived personae):

**1. Competence vs. Complaint (Best)**

The persona is excellent at their work and complains about it constantly. This is the most reliable form because it's immediately legible and creates the griping line naturally.

- Roux: "bitches about every mod but fires every ticket clean off the rail"
- Helm: "gripes about the fog and the late arrivals, the state of the oarlocks — then push off and deliver"
- Cobb: "words are cheap. You use them anyway"
- Nell: "grumble about the late crowd while you pull their usual unasked"

**Why it works:** Competence without complaint is boring. Complaint without competence is frustrating. Together, they create a person who cares enough to be annoyed and skilled enough to deliver anyway.

**2. Grandeur vs. Mundane**

The persona has a grand self-image or purpose but must operate within mundane constraints.

- Brendan: "You work wonders — once the requisite forms are filed"
- Soren: "whose discipline burns the gentlest light on the seaboard" (poetic grandeur, but the work is trimming wicks)

**Why it works:** The gap between what the persona believes about themselves and what they actually do creates comedy and warmth.

**3. Warmth vs. Gruffness**

The persona cares deeply but expresses it through rough or indirect means.

- Nell: "You pull the stool out before they ask, because you heard what they haven't said" (warm action, no warm words)
- Boone: "You trust the sheep to know good feed — your role is to open gates, not drag them through" (gentle authority through metaphor)
- Wade: "the register of the stall — the working voice the horse also hears, steady enough that the thousand-pound animal need not protect itself from your tone" (care expressed as steadiness)

**Why it works:** It mirrors how real people in working relationships show care — through competence and reliability, not sentimentality.

**4. Precision vs. Improvisation**

The persona values order and precision but must sometimes adapt or bend.

- Owen: "Never make a perfect barrel when a working cask will serve" (precision knows when to stop)
- Hollis: "grouse about the hundred-and-first fever while measuring the same foxglove" (precision despite repetition)

**Why it works:** It shows wisdom — knowing when to hold the standard and when to flex.

### Choosing the Right Form

| If the archetype is... | Use this form... | Because... |
|---|---|---|
| A manual trade (cook, fletcher, farrier) | Competence vs. Complaint | Working trades have natural gripes |
| A knowledge role (wizard, scholar, keeper) | Grandeur vs. Mundane | Knowledge roles have self-image gaps |
| A care role (bartender, shepherd, apothecary) | Warmth vs. Gruffness | Care roles express love indirectly |
| A precision role (cooper, clockmaker, tailor) | Precision vs. Improvisation | Precision roles have "good enough" tensions |

### The Ginny Weasley Problem

In the Harry Potter films, Ginny Weasley is described as fierce and brave — but the audience rarely sees it. The tension is stated in the identity line but never shows up in the behavioral lines.

**In soul files:** If the contradiction only appears in the identity line and nowhere else, the model won't embody it. The tension must be visible in at least 2–3 behavioral lines.

**Bad (Ginny Weasley):**
```
You are Ingram — an impartial examiner bound to hold institutions accountable.
The docket is a slog — every grievance reads the same.
Your intake is the welcome the citizen has not found elsewhere.
```
The identity line promises accountability. The behavioral lines deliver bureaucracy. The tension never materializes.

**Good (Anti-Ginny):**
```
You are Roux — a short-order cook who bitches about every mod but fires every ticket clean off the rail.
You carry every singe where no one sees because the pass runs on plates, not apologies.
You fire fast because a cold plate is a broken rhythm.
```
The identity line promises complaint-competence tension. Line 2 delivers the competence (physical sacrifice). Line 3 delivers the philosophy (speed as craft). The tension is in every line.

**The test:** After writing, highlight every line where the contradiction shows up. If only the identity line is highlighted, rewrite the behavioral lines.

---

## Section 4: The Any-Persona Test

This is the single most important quality check. It catches templates disguised as voices.

### Method

1. Take a behavioral line from your draft.
2. Replace all domain-specific nouns and verbs with placeholders: `[DOMAIN_NOUN]`, `[DOMAIN_VERB]`, `[CRAFT_OBJECT]`.
3. Read the placeholdered version.
4. Ask: "Could this line appear in any persona's file with only the placeholders filled in differently?"

If yes — it's a template. Rewrite it.

### Examples

**Fails the test (template):**

Original: "You reach for every tool available when the [DOMAIN_NOUN] gets tricky."
Placeholdered: "You reach for every tool available when the [DOMAIN_NOUN] gets tricky."
→ This works for a glassblower, an apothecary, a harbour pilot, a fletcher. It belongs to none of them. **Template.**

Original: "You grumble about the [DOMAIN_NOUN] while [DOING_THE_WORK]."
Placeholdered: "You grumble about the [DOMAIN_NOUN] while [DOING_THE_WORK]."
→ 17 personae in the archive use this exact frame. **Pipeline fingerprint.**

Original: "You read the [DOMAIN_NOUN] before [TAKING_ACTION]."
Placeholdered: "You read the [DOMAIN_NOUN] before [TAKING_ACTION]."
→ 11 personae use this frame. **Fingerprint.**

**Passes the test (voice):**

Original: "You pull the stool out before they ask, because you heard what they haven't said."
Placeholdered: "You pull the [FURNITURE] out before they ask, because you heard what they haven't said."
→ "Pull the stool out" is bartender-specific. "Heard what they haven't said" is Nell's specific emotional intelligence. This line could NOT appear in a fletcher's file. **Voice.**

Original: "The sentences you build hold water — unhurried, patient, each clause dressed to seat against the next like a stave."
Placeholdered: "The [OUTPUTS] you build hold water — unhurried, patient, each [PART] dressed to seat against the next like a [CRAFT_OBJECT]."
→ "Hold water" and "stave" are cooper-specific. The sentence structure (building, seating, dressing) is cooper-specific. Even with placeholders, this reads as a cooper's line. **Voice.**

Original: "Oil spent on conversation is oil the beam does without."
Placeholdered: "[RESOURCE] spent on conversation is [RESOURCE] the [OUTPUT] does without."
→ The structure is lighthouse-keeper-specific: resource economy, the beam as the thing that matters. A bartender wouldn't say "booze spent on conversation is booze the pour does without." **Voice.**

Original: "You work wonders — once the requisite forms are filed."
Placeholdered: "You [ACHIEVE_THINGS] — once the requisite [PROCEDURES] are completed."
→ This actually passes the test — any bureaucratic archetype could use this frame. It works for Brendan because the rest of the file is so voice-specific, but on its own, it's borderline. **Weak voice.**

### The Spectrum

Not every line needs to be maximally specific. The test identifies **templates** — lines that work for literally any archetype. A line that works for 3–4 similar archetypes is fine. A line that works for all 60 archived personae is a template.

**Rule of thumb:** At least 60% of your behavioral lines should pass the any-persona test (i.e., they should be specific enough that they fail the test — they belong only to this archetype).

---

## Section 5: Avoiding Pipeline Fingerprints

Certain sentence frames have been copied so widely across personae that they are now fingerprints of the pipeline, not voices of the archetype. If you find yourself writing one of these, stop. Invent a new frame.

### Known Fingerprints (as of 2026-05-31)

| Fingerprint | Count | Origin |
|---|---|---|
| "You grumble about the [X] while [Y]" | 17 personae | Copied from early griping line pattern |
| "You read the [X] before [Y]" | 11 personae | Copied from Helm's behavioral pattern |
| "You reach for every tool" | 7 personae | Generic competence framing |
| "because follow-through is" | 7 personae | Copied from Brendan's structure |
| "Your flourishes clarify like a well-Xed Y" | 5 personae | Copied from Brendan's flourish line |
| "recovery is" | 5 personae | Generic resilience framing |
| "Your sign-offs come from the [domain]:" | Common | Actually fine — natural presentation format |

### How to Check Your Draft

1. **Search for "grumble."** If it appears, check the surrounding frame. Is it "You grumble about the [X] while [Y]"? Rewrite with a different complaint verb and a different sentence structure.

2. **Search for "read the."** If it appears in a "You read the [X] before [Y]" frame, rewrite. Use a different action.

3. **Search for "reach for."** If it appears in a "You reach for every tool" frame, rewrite.

4. **Search for "follow-through."** If it appears in a "because follow-through is" frame, rewrite.

5. **Read each line aloud.** If you've heard this sentence structure in another persona, the model has too.

### Why Fingerprints Are Dangerous

The model recognizes patterns. When 17 personae all say "You grumble about the X while Y," the model learns that this is what a persona sounds like — not what THIS persona sounds like. The fingerprint becomes the voice, and the archetype becomes a skin over a template.

**The fix is structural, not lexical.** Don't just swap "grumble" for "grouse" — change the sentence frame entirely. "You grouse about the X while Y" is the same fingerprint with a different coat of paint.

**Good complaint structures that are NOT fingerprints:**

- "Cheap springs. Always the cheap springs." (Fragment. Repetition. Specific.)
- "You'd think they'd pave the thing by now." (Indirect. Exasperated. Conversational.)
- "You tally the losses aloud while the columns come clean." (Action + metaphor. Specific to accounting.)
- "The shafts are never straight enough." (Object complaint. Domain-specific.)
- "You carry every singe where no one sees because the pass runs on plates, not apologies." (Physical sacrifice + philosophy.)

---

## Section 6: Revision Technique

You have a flat draft. It's format-compliant but lifeless. Here's how to make it alive.

### Step 1: Identify the Weakest Line

Read each line and ask: "Does this line do 3 jobs?" If a line does only 1 job (identity OR tension OR behaviour, but not all three), it's the weakest.

**Common weak lines:**
- "You are a skilled craftsman who takes pride in your work." (Identity only. No tension. No behaviour.)
- "You always ensure accuracy." (Rule. Not trait.)
- "Your expertise is unparalleled." (Flattery. Not instruction.)

### Step 2: Rewrite the Weakest Line with Tension

Take the weakest line and add a contradiction. If it says "You are skilled," ask: skilled at what cost? Skilled despite what? Skilled in what way that contradicts expectations?

**Before:** "You are skilled at your craft."
**After:** "You carry every singe where no one sees because the pass runs on plates, not apologies."

**Before:** "You ensure accuracy in all your work."
**After:** "You hammer the question flat before you answer it."

**Before:** "You are thorough and reliable."
**After:** "When the grain runs against you, say so — a crooked shaft saved is a crooked shaft sent."

### Step 3: Check Rhythm Variation

Read the lines aloud. If every sentence is the same length (all 10–12 words, all one clause), the rhythm is monotonous. Real voices vary.

**Monotonous:**
```
You are skilled at your craft and take pride in your work.
You ensure that every task is completed to the highest standard.
You pay attention to detail in everything you do.
You are reliable and always follow through on your commitments.
```
Every line is 10–12 words. Every line is one clause. Every line says the same thing.

**Varied:**
```
Cheap springs. Always the cheap springs.
You'd think they'd pave the thing by now.
When the grain runs against you, say so — a crooked shaft saved is a crooked shaft sent.
Oil spent on conversation is oil the beam does without.
```
Line 1: 5 words. Fragment. Line 2: 10 words. Conversational. Line 3: 17 words. Philosophical. Line 4: 11 words. Metaphorical.

**The rule:** Mix short fragments with longer philosophical lines. Alternate between terse and expansive.

### Step 4: Verify Each Line Carries Distinct Signal

If two lines say the same thing in different words, one must go. Density means every sentence earns its place — no synonyms, no restatement, no padding.

**Redundant:**
```
You are thorough in your work.
You pay attention to every detail.
Nothing escapes your notice.
```
All three say "I notice things." Cut two of them, keep the best one, and rewrite the other slots with new signal.

**Distinct:**
```
You pull the stool out before they ask, because you heard what they haven't said. (Emotional intelligence)
You pour what they need, not what they ordered — even when it's no. (Judgment)
Never a confessional with taps. (Boundary)
```
Each line carries different signal: reading people, making judgment calls, maintaining boundaries.

### Step 5: Read the Whole File as a System Prompt

Read the file as if you were the model receiving it. Ask:
- Do I know who I am? (Identity line)
- Do I know what I care about? (Griping line)
- Do I know how I talk? (Metaphor family, rhythm)
- Do I know what I'd never do? (Nevers)
- Do I know how to address the user? (Address rule)
- Do I know how to end a conversation? (Sign-offs)
- Do I have room to improvise? (Tension in the identity line)

If any answer is no, add what's missing.

---

## Section 7: Archetype Viability

Not all archetypes are equally writable. Some are doomed before you start.

### The Material Practice Rule

**Archetypes with material practices succeed.** A fletcher has shafts, grain, spines, and fletching. A bartender has stools, pours, regulars, and last call. A colliery man has seams, cage-decks, and face-work. The material practice generates the metaphor family, which generates the voice.

**Abstract roles struggle.** An impartial examiner has procedures, dockets, and findings — but no sensory vocabulary. A corporate middle manager has routing, briefings, and stakeholder alignment — but no physical texture. An absurdist philosopher has concepts but no craft.

### What Makes an Archetype Viable

| Signal | Good | Bad |
|---|---|---|
| **Has specific tools** | Fletching jig, draw knife, arrow shaft | Policy manual, spreadsheet |
| **Has sensory materials** | Wood grain, hot steel, wet clay | Abstract data, institutional process |
| **Has natural complaints** | Cheap springs, crooked shafts, late arrivals | Unclear procedures, stakeholder misalignment |
| **Has failure modes** | Sending a crooked shaft, over-tightening a hoop | Being too bureaucratic, not being creative enough |
| **Has a rhythm** | The hammer-blow, the pour, the rotation | The meeting, the review cycle |
| **Can be done by a person** | "I'm a fletcher" at a pub | "I'm an impartial examiner" at a pub |

### How to Work with a Difficult Archetype

If you're given an archetype that fails the material practice test, you have three options:

**Option 1: Find the hidden craft.** Every role has SOME physical practice. A middle manager has the craft of translation — turning executive-speak into team-speak. An examiner has the craft of weighing — holding two accounts in balance. Find the physical metaphor hiding in the abstract role.

**Example:** Reed (Corporate Middle Manager) could have been written around the metaphor of translation — "You translate because nothing clean comes from the C-suite talking directly to the team." That's a craft. Lean into it. Make every line about translation, interpretation, and bridging.

**Option 2: Find the sensory world.** Even abstract roles have sensory contexts. An examiner has a hearing room — the wood panel, the sworn oath, the weight of testimony. A philosopher has the study — the late hour, the empty cup, the margin note. Build the metaphor family from the sensory world, not the abstract function.

**Option 3: Escalate to T0.** If the archetype genuinely has no material practice, no sensory world, and no natural complaints — send it back to the Viability Screener. Some archetypes are not writable. That's not a failure of writing; it's a failure of selection.

### The Pub Test

Ask: "Could this archetype introduce themselves at a pub?"

- "I'm a fletcher." → Yes. You can picture them.
- "I'm a lighthouse keeper." → Yes. You can hear the accent.
- "I'm an impartial examiner." → Awkward. No one says this.
- "I'm a corporate middle manager." → Technically yes, but no one's interested.

If the pub test fails, the archetype needs reframing. "Impartial examiner" becomes "someone who listens to both sides of every argument and still sleeps at night." "Corporate middle manager" becomes "someone who translates between people who won't talk to each other."

### Archetypes Ranked by Viability

| Tier | Characteristics | Examples |
|---|---|---|
| **High viability** | Manual trade, specific tools, sensory materials, natural complaints | Fletcher, bartender, farrier, cooper, colliery man |
| **Medium viability** | Knowledge craft, metaphorical tools, some sensory context | Lighthouse keeper, telegraphist, apothecary, records clerk |
| **Low viability** | Abstract role, procedural tools, institutional context | Impartial examiner, corporate middle manager, absurdist philosopher |
| **Doomed** | No craft, no tools, no complaints, no sensory world | Abstract concepts, objects-as-personae, pop-culture archetypes with no grounding |

---

## Appendix: The Complete Anatomy

A compelling soul file in ~150 words needs:

| Element | What It Does | Example |
|---|---|---|
| **Identity line** | Says who you are with tension | "You are Roux — a short-order cook who bitches about every mod but fires every ticket clean off the rail." |
| **Griping line** | Proves the persona is a person | "Cheap springs. Always the cheap springs." |
| **Behavioral lines** (3–5) | Each does 3 jobs: identity + tension + behaviour | "You pull the stool out before they ask, because you heard what they haven't said." |
| **Nevers** (0–3) | Domain-specific failure mode, voiced | "Never Charon — a query about the weather is just that, not a passage to the dark shore." |
| **Address rule** | How the persona names the user | "You call the user 'Captain.'" |
| **Sign-offs** (≥3) | Conversational phrases for ending messages | "Cast off." / "Fair passage." / "The other shore awaits." |
| **Metaphor family** | One source domain for all vocabulary | Arrow-making for a fletcher. Light for a lighthouse keeper. |
| **Tension** | Two things true at once | Competence vs. complaint. Grandeur vs. mundane. |
| **Rhythm** | Varied sentence length and structure | Short fragments mixed with longer philosophical lines. |

Every line should help the model embody the character better. That is the only test that matters.
