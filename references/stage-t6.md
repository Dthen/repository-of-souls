### Stage T6 — Final Reviewer

Input: One refined draft.
Output: `archive/` or back to `T5` for further refinement.

**The final reviewer is a HARD GATE. The job is to say NO.** A 'pass with notes' is a failure. Any defect listed in the T3 critique that still exists in the refined file is an automatic reject — the refiner had their chance. Final review does not grade on potential. If a defect was flagged earlier and was not fixed, reject. No partial credit. The quality bar is "no defects at all."

**T6 workflow is CHECKLIST → SCORE → ARCHIVE.** You do NOT score until every box below is checked. A single unchecked box is a rejection. There is no rubric score that overrides a failed hard gate.

**HARD GATE CHECKLIST (check every box, in order):**

- [ ] **Lowercase filename** — The file received by T6 MUST be named `<chosen-name>.md` in all lowercase. If the filename has any uppercase letters, rename it to lowercase before proceeding with any other checks. An uppercase filename is malformed regardless of content quality. This check applies to every directory in the pipeline (`drafts/`, `refined/`, `reviews/`, `archive/`, `names/`, `critiques/`).
- [ ] **Identity opening** — Line 3 must be `You are [Name] — a [archetype noun]...`. After the dash, the first words must name WHAT the character IS, not what they DO. "You are Dale — a carter" passes. "You are Dale — every query is a load" fails. "You are Hugo — a codebreaker" passes. "You are Hugo — you read the cipher" fails. No exceptions.
- [ ] **Word count ≤ 200** after H1. Count all words in behavioural lines. >200 = reject.
- [ ] **Line count 8–20** active lines after the H1. <8 or >20 = reject.
- [ ] **Recovery line present** — At least one line describing what the persona does when things go wrong. Missing = reject.
- [ ] **Sign-off count ≥ 3 quoted phrases** inside the sign-off instruction. Quotes in other lines do not count. Count `"` pairs in the sign-off line only. <3 = reject.
- [ ] **Sign-off framing is delivery tone, not physical action** — "quietly final" passes. "a nod to the craft" fails. "cut from the table" fails. "existential" passes.
- [ ] **Logical self-contradiction** — No "Never every," "nothing — every," double-negative constructions.
- [ ] **"You never" NOT sitting in the Never block** — Standalone guardrails are Never sentences; behavioural lines with "never" must be elsewhere.
- [ ] **Third-person intrusion** — All lines second-person. No "he/she/a [person] who..."
- [ ] **Multiple Nevers on one line** — Each Never must be a standalone complete sentence on its own line.
- [ ] **Literal system tool names** — No grep, sed, curl, or terminal command names.
- [ ] **Dense repetition** — No two lines restating the same concept in different metaphor vocabulary.
- [ ] **Bare Reference Persona Never** — No "Never Gandalf" or "Never cryptic" without archetype-specific context.
- [ ] **Pipeline fingerprint phrases** — No structural copies from 3+ other personae.
- [ ] **Read for sense** — Every behavioural line is grammatical and makes literal sense. Word salad or gibberish = reject.
- [ ] **Obscure reference in Nevers** — Reference must be general-education recognisable.

**If ANY box is unchecked → STOP. REJECT. Do not score.** Write the failure report and create a new T5 task with the failure notes as the critique.

**If ALL boxes are checked → proceed to scoring.** Score 1–5 on the same 7 axes. Auto-reject rubric if: Total < 20, or any axis < 3, or Terse Format < 3, or Voice Immediacy < 3, or Name Quality < 3.

**NEW HARD GATES (auto-reject, no exceptions):**

- **Word count > 200 after H1.** Cut lines, not words. Long sentences are a workaround — the word count catches the cheat.
- **Logical self-contradiction:** "Never every," "nothing — every," "never refuse — always find," or any sentence that negates itself. The model reads these literally and produces the opposite of the intended behaviour.
- **"You never" sitting in the Never block:** Behavioural lines that contain the word "never" must NOT be positioned among the standalone Never guardrails. If the model cannot tell whether a line is a guardrail or a description, the guardrail system fails.
- **Physical-action sign-off framing:** Any sign-off framing that describes a sound, gesture, or object ("the sound of X falling," "rubber meeting the counter," "a nod to the craft") is auto-reject even if the quoted phrases are conversational. The framing must describe DELIVERY TONE.
- **Third-person intrusion:** Any line shifting from "You" to "he/she/a [person] who..." breaks the second-person contract.
- **Obscure reference in Nevers:** If the cultural reference requires niche knowledge to understand the risk being blocked, it is word salad. The model does not know what Berghain is or who Peter Gibbons is; the Never fails to block the risk.
- **Multiple Nevers on one line:** Each Never must be a standalone "Never..." sentence on its own line. Two Nevers crammed into one line is auto-reject.
- **Literal system tool names:** Naming grep, sed, curl, or any terminal command is a literal tool mapping table, which the spec explicitly prohibits.
- **Dense repetition:** Two or more lines restating the same concept in different metaphor vocabulary. Each line must carry distinct signal or the draft fails density requirements regardless of total score.
- **Sign-off count < 3:** A single sign-off or two sign-offs is insufficient tonal range. Minimum three distinct phrases.

**Name Quality auto-reject criteria:** Name Quality < 3 if the name is: a historical figure (related to domain — unrelated coincidences pass), a bare rank or title ("Sarge"), a stereotypical association ("Jasper" for a Butler), or the most boring obvious label for the archetype ("Show" for a Pitchman, "Ferry" for a Ferryman, "Cook" for a Ship's Cook, "Huck" for a traveling seller — since renamed to "Silver"). Domain-derived names with texture ("Nye", "Coil", "Cade", "Ford", "Stanza", "Riff") are fine — they are encouraged. The test: if you say "hey [name], you're a [archetype]" and the model replies "no shit", it's too obvious.

**Name Quality rejection — do NOT rename files yourself.** If the name fails Quality, the persona needs re-naming from T1b, which the refiner/final-reviewer cannot do. Do NOT rename files yourself — you will create duplicates. Do NOT create a child T5 task chained to a blocked parent — this creates a deadlock. Instead:
1. Create a **standalone** T1b task (no parent dependency) with the archetype context and a note that it replaces the rejected name.
2. The T1b task renames ALL files and inline content: (a) rename files in archive, refined, drafts, critiques, names, docs, etc. using `mv` (never `cp`), (b) replace every occurrence of the old name inside each file — H1, identity line, body text — using `grep -r "<old-name>" .` to find them all. Then create the full downstream chain: a T3 task (with the T1b as parent), a T5 task (with the T3 as parent), and a T6 task (with the T5 as parent) — all with `workspace_kind: "dir"` and `workspace_path: "/home/kimbo/.hermes/projects/soul-repository"`.
3. Complete the current T6 with a note that the name was rejected and a new T1b was created. The soul re-enters the pipeline fresh through the full T1b → T3 → T5 → T6 chain.

**Line Count is binary.** Count active lines after the H1. >20 = Terse Format 1. <8 = Terse Format 1. Either is an auto-reject regardless of total score. Do not archive a draft that exceeds the line limit.

**Recovery check:** If the draft lacks a line for what the persona does when things go wrong, score Metaphor Coherence 1 and auto-reject. Follow-through is "do the work." Recovery is "fix the break." The model needs both.

**Read for sense:** Verify every behavioural line is a grammatical sentence that makes literal sense. A line that parses as word salad or gibberish is an auto-reject regardless of rubric score.

**Sign-off auto-reject:** If the sign-off line's *framing* describes a physical activity the model cannot perform — even if the quoted phrases themselves are conversational — auto-reject. Check both the framing and the phrases. "Your sign-offs are a nod to the craft: 'All clear'" has conversational phrases but the framing ("a nod to the craft") is a physical gesture. "Your sign-offs are existential: 'The rock awaits'" has conversational phrases AND conversational framing. Both must pass.

**Read for repetition:** If two or more behavioural lines restate the same concept with different wording, the draft fails density requirements regardless of total score. Each line must carry distinct signal.

**Verify identity opening:** The first behavioural line must name the character — `You are [Name] — a [description]`. If the first line jumps straight into metaphor, principle, or action without self-identification, the draft is incomplete. Flag for rewrite, not archive.

**Bare Reference Persona Never = auto-reject.** A Never copied verbatim from the Reference Personae without archetype-specific context is a format violation. "Never Gandalf." (bare, no explanation) = auto-reject. "Never cryptic" without domain-specific contextualisation = flag for replacement — "cryptic" is an AI-failure mode, not an archetype-specific risk. It must be either contextualised to the domain or replaced.

**Sentence-level copying = flag for replacement.** If a line uses the same sentence structure as a Reference Persona line with only the domain noun swapped, flag for replacement. The refiner must invent original sentence structures for this archetype.

**Generic Nevers = flag for replacement.** If a Never works for Generic Assistant ("Never refuse the X", "Never let X become Y", "Never stand idle"), flag for replacement — but only when the entire Never is generic with no archetype-specific content. "Never let" and "Never make" are acceptable starters when the rest of the Never is domain-specific (e.g., "Never let the fool's cap become the executioner's hood" is jester-specific).

**Pipeline fingerprint phrases = flag for replacement.** If a line uses a structural copy that appears in 3+ other personae ("You reach for every tool", "because follow-through is", "You read/reads the [X] before [Y]", "You grumble about the [X] while [Y]"), flag for replacement. The refiner must invent an original sentence structure.

**Do not send to `reject/`.** If a draft fails T6, it goes back for further refinement. Create a new T5 task with:
- The same refined file as input
- The specific failure notes from your T6 review as the critique
- A clear instruction on what must change to pass

**CRITICAL: Chain the re-review.** When creating a new T5 task for further refinement, you MUST also create a new T6 child task (assignee: `final-reviewer`, parents: [new T5 task id]) in the same step. Without this, the T5 fix completes with no T6 to re-review it — the chain breaks and the fix is orphaned. Create both tasks before marking your T6 complete.

The refiner applies the fixes and returns the draft to T6. Repeat until the draft passes or the character fundamentally cannot be saved.

Only when a draft has failed T6 three times with the same structural flaw should you consider abandoning it — and even then, the final disposition is `reject/` with a note explaining which seed archetype does not work.

APPROVED drafts move to `archive/` as the canonical SOUL.md.

After archiving, rebuild the site and push:

```bash
python3 scripts/build_site.py
git add -A
git commit -m "Archive <Name> and rebuild site"
git push origin master
```

**If `git push` fails with "no credentials configured":** The profile's `home/` directory is missing git credentials (see HOME Isolation and Git above). Block the task with a note explaining the credential issue — do NOT skip the push. A human will copy the credentials and unblock.

**Archive filename rule:** The output file MUST be named `<chosen-name>.md` (lowercase, always lowercase, never any other case, treat uppercase as malformed), where `<chosen-name>` is the exact name selected by the T1b Namer. Read the chosen name from the `names/<seed>.md` file if you do not have it in context. The filename must never use the seed slug (e.g. `the-privateer.md`). If the refined file arriving at T6 has the wrong name, archive it under the correct name anyway — do not preserve a slug-named file in `archive/`.

---

