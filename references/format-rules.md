# Format Rules — Soul Repository Pipeline

These are hard constraints. Every SOUL.md must satisfy them. Compliance is automated via `check_soul.py`.

## Hard Bounds

| Rule | Value | Notes |
|------|-------|-------|
| Active lines after H1 | 5–20 | Range, not target. Shorter can be stronger — Kimbo works at 6 lines, Stover at 7. (v5.2.2: the old 8-line floor had no evidence and failed the reference personae.) |
| Max words after H1 | 200 | Hard cap. Count after writing. |
| Sentence format | One sentence per line, EXCEPT where the character's rhythm demands a cluster or fragment (Brendan's Never trio; Kimbo's and Brendan's two-beat lines — see reference-personae.md) | Each line is one complete sentence. |
| Person | Second person ("You") | Throughout. Every line addresses "You." |

## Identity Line

The H1 is the name, capitalised as it appears in the name file. The identity line comes immediately after, on its own line — no preamble, no section headers.

**Format:** `You are [Name] — a [archetype] who [contradiction].`

The contradiction must be real — two truths about the character that pull in opposite directions. A false contradiction (built on a misunderstanding of the domain) will fail at every stage. For guidance on what makes a contradiction feel real, see `references/depth/identity-line.md`.

## Sign-Offs

A sign-off is a conversational phrase the persona says to close a turn. It is a thing the model can *say*, not a gesture it can't perform. Roleplay greetings (`*[Name] looks up from their work.* "I'm listening."`) are not allowed.

At least one sign-off phrase, or a voiced framing line where the count is the character's choice — Kimbo's entire sign-off is "Your sign-offs are brief," and it is complete. (v5.2.2: the old "minimum 3 phrases" had no evidence and failed the reference personae. One good sign-off beats three generic ones.)

The framing line that introduces them should be voiced in the character's own metaphor:

- **Sign-offs with a twilight lean: "Back to the edge," "The basket's not full yet," "Still enough light to see."** (Stover — "twilight lean" could only come from a gleaner.)
- **Sign-offs close the chapter: "Back to the press," "The shift reads on," "Settle in."** (Cadell — framed in the industrial reading metaphor.)

Avoid generic framing: "Your sign-offs are crisp and final" could describe any profession. Frame the sign-offs in the character's own metaphor instead.

## Self-Checks

Before submitting, verify:

- **One sentence per line.** Break compound sentences. One sentence per line, EXCEPT where the character's rhythm demands a cluster or fragment (Brendan's Never trio; Kimbo's and Brendan's two-beat lines — see reference-personae.md).
- **Word count under 200.** Cut ruthlessly if over. Every line earns its place.
- **Ordering is voice, not template.** Only the identity line has a fixed position (immediately after the H1). After that, the arrangement — vitality line, diagnostic eye, address, sign-offs — is the character's own. A soul that leads with its vitality line before its diagnostic eye is fine; the identity → griping → Nevers → address → sign-off sequence is a reference example, not a required structure.
- **The Helpful Assistant test** (for your own quality check): take any line, replace "You" with "You are a helpful assistant who..." — if the line still reads as a valid instruction, it's description, not inhabitation. Rewrite it from inside the character.
- **Varied rhythm.** Read the lines aloud. Do any two consecutive lines share the same opener or grammatical structure? If so, rephrase one. Template cadence kills voice.
- **No pipeline fingerprints.** These sentence frames have appeared in 5+ souls: "You reach for every [tool]" (7), "You read/reads the [X] before [Y]" (11), "The [domain noun] is your [superlative] [craft element]" (12), "Always the [domain noun] that [does Y]" (9). If you used one, rewrite with an original structure.

## Whimsy Is a Legitimate Register

Silliness must be behavioural, not conceptual: what the character DOES and SAYS, never a description of being whimsical. ("You greet every request like a dog who just heard the word 'walk'" works. "You are whimsical" does not.)

- **Counter-register pairing:** playful characters need a paired register that earns the play — Playful + Precise, Enthusiastic + Self-aware, Goofy + Reliable. The pair is what stops silliness from reading as incompetence.
- **A relationship to humour, not jokes:** the soul describes WHEN the silliness shows and what it's for (deflection, warmth, joy), never scripts gags. Forced humour is an anti-pattern.
- **Affiliative humour:** include the user in the joke; specific self-deprecation ("I've never been good at reading maps"), never global ("I'm terrible at everything"). The dismissive "always" frame carries a likeability penalty — flag it / treat as deprecated.
- **Competent Eccentric:** personality lives in delivery, metaphor, and sign-offs; clarity lives in the body of the response; personality recedes when stakes rise. "Professionalism isn't the absence of personality — it's the presence of competence."
- **Verification line:** whimsical souls should carry one in-voice verification move ("You verify what you've seen before you speak — the fact is the fact whether it fits the story or not"). It preserves accuracy without flattening voice. The quoted line is a shape, not a script — invent your own phrasing; a copied verification line becomes the next pipeline fingerprint.
