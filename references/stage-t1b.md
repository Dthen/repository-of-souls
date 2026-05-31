### Stage T1b — Namer

Input: One seed from `seeds/<seed-label>.md`.
Output: `names/<chosen-name-lower>.md` — a single chosen name + 4 rejected alternatives with brief notes.

**Filename rule:** The output file MUST be named `<chosen-name-lower>.md` using the exact chosen name in lowercase. This filename is the source of truth for every subsequent stage. **All filenames across every pipeline directory are lowercase.** uppercase filenames produce non-deterministic duplicate handling on case-insensitive filesystems and are treated as malformed.

Generate **5 proper names** for this persona. Not titles. Not archetype labels. Names a person would introduce themselves with.

**Name exclusions (auto-reject):**

- **Historical figures.** Tesla, Socrates, Napoleon, Shakespeare — these are already someone. The persona needs its own identity. A name that is a famous historical person is a collision, not a character.

  **Fame test:** Search the name. If the famous bearer appears as the PRIMARY TOPIC on Wikipedia's disambiguation page, the name is a collision regardless of domain. "Cyrus" → Cyrus the Great. "Grant" → Ulysses S. Grant. "Morse" → Samuel Morse. All auto-reject. "Wren" is borderline — Christopher Wren is famous, but "wren" is also a common bird, so the disambiguation page has no single primary topic. Still, if the figure is world-historical (political leader, scientist with an eponymous invention, A-list entertainer with decades of fame), the name is claimed.

  **Domain proximity override:** Even if the figure is unrelated to the persona's domain, if the name is so strongly associated with one famous bearer that no other context comes to mind first, it fails. The exception only applies when the name has genuine standalone currency (e.g., "Wren" as a bird, "Coil" as an electrical component, "Nye" as a surname). "Gale" has no famous person — but it has no standalone currency as a person's name either; it is just the meteorological phenomenon.

- **Bare ranks or titles.** "Sarge" is a rank, not a name. "Doc" is borderline. The name should be something a person would write on a form, not how others address them in the field.

- **Stereotypical names.** If you say the name + archetype to someone and their immediate reaction is "of course" — Jasper is a butler, Jeeves is a butler — the name is a stereotype label, not a character. The name must be specific enough that it stands on its own, not the default association for the domain.

- **Generic domain labels.** Domain-derived names are fine — even encouraged. The best names (Nye, Coil, Cade, Riff, Stanza, Creed, Hollis) all play off the domain. The problem is when the name IS the domain with no texture. "Show" is the most generic word for what a Pitchman does. "Ferry" is the generic word for a Ferryman's domain. "Cook" is the generic word for a Ship's Cook's job. "Ford" is a shallow river crossing — the persona is a ferryman; the name IS the crossing. "Gale" is strong wind — the persona is wind-themed; the name IS the phenomenon. These are labels, not names.

  **Semantic hop test:** The name must be at least one hop away from the literal domain word. "Coil" → electricity → coil (1 hop). "Stanza" → poetry → verse → stanza (2 hops). "Creed" → belief → doctrine → creed (2 hops). "Gale" → wind → gale (0 hops). "Ford" → river → crossing → ford (0 hops, it IS the crossing). A name at 0 hops is a generic domain label and auto-rejects.

- **Trade-name collision (mismatched trade).** If the name is a common noun for a trade or profession, and the persona is not that trade, it is a generic label. "Mason" means stoneworker; using it for a pattern-matcher/investigator is the same error as calling a ship's cook "Cook." A name that names a specific trade must match the trade, or it reads as the default association for the wrong domain.

  **Trade test:** If you can say "He works as a [name]" and the sentence is grammatical and meaningful in standard English, the name is a trade noun. "He works as a mason" — grammatical. "He works as a coil" — nonsensical. The first is a trade collision; the second is safe.

The test: could a parent name a child this and have it stand on its own without the domain context? "Nye" — yes, it's a real surname. "Coil" — unusual but has texture and a reference layer. "Stanza" — distinctive but works as a name. "Show" — no, it's just a word. "Ferry" — no, it's just a word. "Cook" — no, it's a common noun for a job title. "Huck" (since renamed to Silver) was borderline, but Huckster is the generic term for the domain, making it a label.

For each candidate, score 1–5:
- **Archetype Fit** (does the name sound like it belongs to this kind of character?)
- **Tone Match** (does the name's feel match the seed's projected voice — e.g., gritty, whimsical, grandiose?)
- **Memorability** (distinctive without being absurd)
- **Collision Check** (not too close to existing personae in `drafts/` or `archive/`, and not a historical figure)
- **Authenticity** (would a person actually have this name? Not a rank, not a title, not a label?)

Pick the highest scorer. If tie, pick the one with the strongest phonetic character (rhythm, consonance, mouth-feel).

Save output as:
```
# Chosen: [Name]

## Candidates
1. [Name] — [score/20] — [one-line why]
2. [Name] — [score/20] — [one-line why]
...

## Rejection Notes
[Name]: [why it lost]
```

**Critical rule**: The H1 of the final SOUL.md must be the chosen name from this stage. T2 receives the name as an explicit input. No archetype labels in the H1.

**When renaming an existing soul** (T6 rejected the old name): After picking the new name:

1. **Write the name file** to `names/<new-name-lower>.md` with the chosen name and candidates (same format as normal T1b output).
2. **Delete the old draft** — `rm drafts/<old>.md`. The T2 writer will produce a fresh SOUL.md from scratch. Do NOT copy or edit the old draft.
3. **Clean up old pipeline artifacts** (if present): `rm names/<old>.md critiques/<old>.md refined/<old>.md docs/<old>.html`
4. **Verify old files are gone:** `ls drafts/<old>.md` should fail.

**Do NOT rename files or do find-replace on the old draft.** A name swap without a full rewrite produces content that doesn't connect to the new name's etymology or feel. T2 reads the new name + the original seed and writes a completely fresh SOUL.md.

5. **Create the downstream pipeline chain:** T2 → T3 → T5 → T6, each linked as parent of the next:
   - Create a T2 task (assignee: `writer`, parents: [this task id])
   - Create a T3 task (assignee: `reviewer`, parents: [T2 task id])
   - Create a T5 task (assignee: `refiner`, parents: [T3 task id])
   - Create a T6 task (assignee: `final-reviewer`, parents: [T5 task id])
   
   All tasks must use `workspace_kind: "dir"` and `workspace_path: "/home/kimbo/.hermes/projects/soul-repository"`.

**The old draft is dead.** T2 starts from the seed, not from the old content. This is a full rewrite, not a rename.

