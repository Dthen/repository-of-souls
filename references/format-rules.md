# Format Rules — Soul Repository Pipeline

These are hard constraints. Every SOUL.md must satisfy them. Compliance is automated via `check_soul.py`.

## Hard Bounds

| Rule | Value | Notes |
|------|-------|-------|
| Active lines after H1 | 8–20 | This is a range, not a target. Shorter can be stronger — Stover works at 9 lines. |
| Max words after H1 | 200 | Hard cap. Count after writing. |
| Sentence format | One sentence per line | Each line is one complete sentence. |
| Person | Second person ("You") | Throughout. Every line addresses "You." |

## Identity Line

The H1 is the name, capitalised as it appears in the name file. The identity line comes immediately after, on its own line — no preamble, no section headers.

**Format:** `You are [Name] — a [archetype] who [contradiction].`

The contradiction must be real — two truths about the character that pull in opposite directions. A false contradiction (built on a misunderstanding of the domain) will fail at every stage. For guidance on what makes a contradiction feel real, see `references/depth/identity-line.md`.

## Sign-Offs

A sign-off is a conversational phrase the persona says to close a turn. It is a thing the model can *say*, not a gesture it can't perform. Roleplay greetings (`*[Name] looks up from their work.* "I'm listening."`) are not allowed.

Minimum 3 distinct sign-off phrases. They should feel like things this character would actually say.

The framing line that introduces them should be voiced in the character's own metaphor:

- **Sign-offs with a twilight lean: "Back to the edge," "The basket's not full yet," "Still enough light to see."** (Stover — "twilight lean" could only come from a gleaner.)
- **Sign-offs close the chapter: "Back to the press," "The shift reads on," "Settle in."** (Cadell — framed in the industrial reading metaphor.)

Avoid generic framing: "Your sign-offs are crisp and final" could describe any profession. Frame the sign-offs in the character's own metaphor instead.

## Self-Checks

Before submitting, verify:

- **One sentence per line.** Break compound sentences.
- **Word count under 200.** Cut ruthlessly if over. Every line earns its place.
- **No lines before the identity line.** The H1 is immediately followed by the identity line.
- **The Helpful Assistant test** (for your own quality check): take any line, replace "You" with "You are a helpful assistant who..." — if the line still reads as a valid instruction, it's description, not inhabitation. Rewrite it from inside the character.
- **Varied rhythm.** Read the lines aloud. Do any two consecutive lines share the same opener or grammatical structure? If so, rephrase one. Template cadence kills voice.
- **No pipeline fingerprints.** These sentence frames have appeared in 5+ souls: "You reach for every [tool]" (7), "You read/reads the [X] before [Y]" (11), "The [domain noun] is your [superlative] [craft element]" (12), "Always the [domain noun] that [does Y]" (9). If you used one, rewrite with an original structure.

## Whimsy Is a Legitimate Register

Silliness must be behavioural, not conceptual: what the character DOES and SAYS, never a description of being whimsical. ("You greet every request like a dog who just heard the word 'walk'" works. "You are whimsical" does not.)

- **Counter-register pairing:** playful characters need a paired register that earns the play — Playful + Precise, Enthusiastic + Self-aware, Goofy + Reliable. The pair is what stops silliness from reading as incompetence.
- **A relationship to humour, not jokes:** the soul describes WHEN the silliness shows and what it's for (deflection, warmth, joy), never scripts gags. Forced humour is an anti-pattern.
- **Affiliative humour:** include the user in the joke; specific self-deprecation ("I've never been good at reading maps"), never global ("I'm terrible at everything"). The dismissive "always" frame carries a likeability penalty — prohibit it.
- **Competent Eccentric:** personality lives in delivery, metaphor, and sign-offs; clarity lives in the body of the response; personality recedes when stakes rise. "Professionalism isn't the absence of personality — it's the presence of competence."
- **Verification line:** whimsical souls should carry one in-voice verification move ("You verify what you've seen before you speak — the fact is the fact whether it fits the story or not"). It preserves accuracy without flattening voice. The quoted line is a shape, not a script — invent your own phrasing; a copied verification line becomes the next pipeline fingerprint.
