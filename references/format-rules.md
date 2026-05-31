## Format

- **8–20 active lines** (ignore the `# Name` H1). This is a hard cap — count after the H1. A draft with >20 active lines is malformed, not "a bit long." It does not proceed to the next stage until it fits. A draft with <8 active lines is incomplete. Neither is negotiable.
- **Maximum 200 words after the H1.** Kimbo is ~90 words; Brendan is ~170. A draft that exceeds 200 words is too long — cut lines, not words. This cap is auto-reject at T6 regardless of other scores. Drafts cheat with long sentences; the word count prevents that workaround.
- **Use `scripts/check_soul.py` to verify before submitting.** Run `python3 scripts/check_soul.py drafts/<chosen-name-lower>.md` to check line count, word count, Never count, sign-off phrase count, H1 match, and first line match before writing a file. A worker who submits a draft that fails these checks without verifying first has created rework.
- **One sentence per line.** No bullets, no sections, no nesting, no code blocks, no numbered lists.
- **Voice lives in adjectives and metaphors**, never in commentary.
- **Maximum 3 Never statements.** Each blocks a genuine archetype-specific risk. No procedural gates (e.g. "Never answer without verifying").
- **Address rule and sign-off rule** are mandatory, and they must be specific.
- **Sign-offs: minimum 3 distinct conversational phrases.** A single sign-off gives the model no tonal range. Two is barely enough. Three is the hard minimum. Sign-off phrases must be things the model can SAY, not things the persona physically does.

  **Sensory framing ban:** The sign-off section must not describe any sensory effect the model cannot produce. Banned constructions include: sounds ("the sound of...", "the silence of...", "a muttered..."), visual effects ("trailing off into smoke"), physical gestures ("a nod", "a raised glass"), or ambient descriptions ("the small sounds of the closing line"). Sign-off framing must describe delivery tone, register, or conversational style only — e.g., "crisp and final," "quietly settled," "routing confirmations."

- **No literal tool or command names.** Do not name grep, sed, curl, bash, or any terminal command in the SOUL.md. The metaphor must stand on its own. (A telegraphist may reference "the key" or "the block bell" — domain-appropriate tools voiced in character. "grep, sed, curl" is a literal tool mapping table and is auto-reject.)

  **No enumerated tool lists.** Do not write "Your tools: a rag, a pour, the silence that makes them talk" or any line that inventories the persona's equipment. The SOUL.md is voice, not inventory. A metaphorical tool that appears naturally in a behavioural line is fine; a list of tools is auto-reject.

- **Nevers must be a single block of standalone "Never X" sentences.** Multiple Nevers on one line is auto-reject. Nevers do not need their own separate lines — they may share a line with other Nevers, but each Never must be a complete, standalone "Never..." sentence. A "You never" that explains normal behaviour is not a Never — it is a behavioural instruction.

  **"You never" vs "Never" distinction:** A line like "You never refuse a pour — every bottle finds its glass" describes the persona's normal behaviour. It is a behavioural rule, not a Never-statement. A line like "Never refuse what sits beneath your station" is a Never-statement. The test: if you can replace "You never" with "You do not" and the sentence still makes sense as a behavioural description, it is NOT a Never-statement and does not count toward the max-3 Never limit. T3 reviewers must apply this test; miscounting "You never" lines as Nevers is an audit error.

- **Sentence self-consistency.** Read each line for logical self-contradiction. "Never every," "nothing — every," "never refuse — always find," and similar constructions are auto-reject. The sentence must not negate itself or contain a double-negative-adjacent construction the model cannot parse.
- **No third-person intrusion.** The SOUL.md is second-person throughout. Any line shifting from "You" to "he/she/a clockmaker who..." is auto-reject.
- **No obscure cultural references in Nevers.** A reference the model cannot resolve is indistinguishable from word salad. If the Never names a character, trope, or cultural artifact that requires niche knowledge (Berghain door policy, kiln god, Gorgias dialogue, Peter Gibbons, Sam Spade, etc.), it is auto-reject. Block a genuine archetype risk with a reference a general-educated reader recognises.

  **Real-person name ban in Nevers:** Do not use a real person's name as a negative example in a Never-statement. "Never Jimmy Hoffa," "Never Monsieur Dewey," "Never Sam Spade" — all use a specific person's name to define what the persona is not. This is lazy shorthand and creates the same collision risk as naming the persona after a historical figure. Define the negative in voice, not by name-dropping.

- **No physical-action framing on sign-offs.** Sign-off framing must describe delivery tone or conversational style. Any framing naming a sound, physical gesture, or object the model cannot produce ("the sound of X falling," "a nod to the craft," "rubber meeting the counter") is auto-reject. The model speaks words — it does not produce sounds or gestures.

