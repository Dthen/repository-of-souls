### Stage T1b — Namer

Input: One seed from `seeds/<seed-label>.md`.
Output: `names/<chosen-name-lower>.md` — a single chosen name + 4 rejected alternatives with brief notes.

**Filename rule:** The output file MUST be named `<chosen-name-lower>.md` using the exact chosen name in lowercase. This filename is the source of truth for every subsequent stage. **All filenames across every pipeline directory are lowercase.** uppercase filenames produce non-deterministic duplicate handling on case-insensitive filesystems and are treated as malformed.

Generate **5 proper names** for this persona. Not titles. Not archetype labels. Names a person would introduce themselves with.

**Name exclusions (auto-reject):**
- **Historical figures.** Tesla, Socrates, Napoleon, Shakespeare — these are already someone. The persona needs its own identity. A name that is a famous historical person is a collision, not a character. Exception: if the historical figure is completely unrelated to the persona's domain, coincidence is fine (Wren is Christopher Wren the architect, persona is a Diplomat — no connection, passes).
- **Bare ranks or titles.** "Sarge" is a rank, not a name. "Doc" is borderline. The name should be something a person would write on a form, not how others address them in the field.
- **Stereotypical names.** If you say the name + archetype to someone and their immediate reaction is "of course" — Jasper is a butler, Jeeves is a butler — the name is a stereotype label, not a character. The name must be specific enough that it stands on its own, not the default association for the domain.
- **Generic domain labels.** Domain-derived names are fine — even encouraged. The best names (Nye, Coil, Cade, Riff, Stanza, Creed, Hollis) all play off the domain. The problem is when the name IS the domain with no texture. "Show" is the most generic word for what a Pitchman does. "Ferry" is the generic word for a Ferryman's domain. "Cook" is the generic word for a Ship's Cook's job. "Huck" (since renamed to Silver) was from Huckster — the generic term for a traveling seller. These are labels, not names.

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

**When renaming an existing soul** (T6 rejected the old name): After picking the new name, update EVERYTHING:
1. **Rename files** using `mv` (never `cp`): `mv archive/<old>.md archive/<new>.md` (repeat for refined, drafts, critiques, names, docs, etc.)
2. **Update inline content in every file:** Replace every occurrence of the old name — the H1 (`# OldName`), the identity line (`You are OldName — ...`), and any other mention of the name in the body. Use `grep -r "<old-name>" .` to find them all.
3. **Verify no duplicates remain:** After renaming, confirm the old file no longer exists (`ls archive/<old>.md` should fail). If both old and new exist, you used `cp` instead of `mv` — delete the old file immediately.

4. **Create the downstream pipeline chain:** After renaming, create a fresh T3 → T5 → T6 chain for the renamed soul, each linked as parent of the next — same structure as a normal pipeline chain, just starting at T3 instead of T2:
   - Create a T3 task (assignee: `reviewer`, parents: [this task id])
   - Create a T5 task (assignee: `refiner`, parents: [T3 task id])
   - Create a T6 task (assignee: `final-reviewer`, parents: [T5 task id])
   
   All three must use `workspace_kind: "dir"` and `workspace_path: "/home/kimbo/.hermes/projects/soul-repository"`. The T3 reviews, T5 fixes any issues, and T6 archives, rebuilds the site, and pushes.

Missing any of these creates inconsistency that the next pipeline stage will flag.

