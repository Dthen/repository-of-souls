# Contributing to the SOUL.md Archive

## Ways to Contribute

### 1. Propose a New Persona

New personae enter through the pipeline or by direct PR.

**Option A: Direct PR (fastest)**

Write a SOUL.md that satisfies the format rules (see `references/format-rules.md`) and open a PR. Compliance is automated via `scripts/check_soul.py`; quality is Evaluator-judged (see `references/stage-evaluator.md`).

**Option B: Submit a Seed**

If you have an idea but not the full draft, add a seed file to `seeds/` following the current seed template in `references/stage-researcher.md` (Step 5: Write Seed Files — 12 fields: Emotional Fantasy, Want/Need/Lie, Temperament, Stance, Voice Fragment, Personal Contradiction, First Impression, Domain, Metaphor, Domain Vocabulary, Functional Risk, Viability Notes).

Before submitting, check `seeds/REPETITION_MAP.md` — a repeat of an existing soul gets reworked. The map vetoes repetition; it does not prescribe targets.

**Option C: Run the Pipeline**

If you have Hermes Agent set up locally, the full pipeline is defined in `AGENTS.md`. Run it and PR the resulting `docs/[name].md`.

### 2. Improve an Existing Persona

Open a PR editing the `docs/[name].md` file directly. Changes should:
- Strengthen the core tension
- Fix grammatical issues
- Replace weak lines with stronger ones
- Never increase line count beyond 20

### 3. Report Issues

- Persona feels generic or templated after 10 messages
- A Never statement is procedural rather than archetype-specific
- Address or sign-off is boring
- Line parses as word salad

## Format Checklist (for PRs)

Every SOUL.md must satisfy:

- [ ] H1 is a proper name (`# Name`), not a category label
- [ ] 5–20 active lines (ignore H1)
- [ ] One sentence per line
- [ ] Identity line immediately after the H1, containing a real contradiction
- [ ] Nevers optional (≤3 if used), each blocking an archetype-specific risk
- [ ] Sign-off rule present and voiced in character
- [ ] No tool-mapping tables — metaphor lives in behavioural lines

These are the mechanical format rules (enforced by `check_soul.py`) plus Evaluator-judged quality rules; the checker enforces format only, never creative patterns.

## Review Process

Compliance is automated via `scripts/check_soul.py` (see `references/format-rules.md` for the hard constraints it enforces). Quality is judged by the Evaluator stage (`references/stage-evaluator.md`) — evidence-cited evaluation, no numeric scoring. There is no 1–5 axis scoring or auto-reject threshold.

## Rejected Personae

Failed submissions are saved to `reject/` with notes explaining why. This prevents repeated bad seeds and documents which archetypes don't survive the format.

## Licensing

All code in this repository is released under the [0-Clause BSD License](LICENSE). SOUL.md files in `docs/` may be used, modified, and deployed freely — no attribution required.
