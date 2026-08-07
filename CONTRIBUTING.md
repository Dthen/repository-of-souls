# Contributing to the SOUL.md Archive

## Ways to Contribute

### 1. Propose a New Persona

New personae enter through the pipeline or by direct PR.

**Option A: Direct PR (fastest)**

Write a SOUL.md that satisfies the format rules (see `references/format-rules.md`) and open a PR. A maintainer will score it on the 7 axes and approve or request changes.

**Option B: Submit a Seed**

If you have an idea but not the full draft, add a seed file to `seeds/` with:
- **Archetype** (e.g., "botanist", "chess hustler", "archivist")
- **Domain** (where this persona lives)
- **Metaphor** (how they relate to tool use)
- **Functional Risk** (what could go wrong)

A seed must be distinct from existing personae in at least two of: archetype, domain, or metaphor.

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
- [ ] No bullets, sections, nesting, code blocks
- [ ] Core tension present (positioning is the character's own — ordering is voice)
- [ ] At least one quotable line (position not fixed)
- [ ] Nevers optional (≤3 if used), each blocking an archetype-specific risk
- [ ] Address rule present and specific
- [ ] Sign-off rule present and voiced in character
- [ ] No tool-mapping tables — metaphor lives in behavioural lines

## Review Process

All submissions are scored 1–5 on:

1. **Distinctiveness** — swappable with "Generic Assistant?"
2. **Functional Safety** — guardrails present and voiced
3. **Consistency Sustainability** — 50 messages: charming or grating?
4. **Metaphor Coherence** — maps to tools, not just accent
5. **Terse Format** — 5–20 lines, one sentence each
6. **Voice Immediacy** — at least one quotable line (position not fixed)
7. **Name Quality** — proper name, fits tone

Auto-reject if: Total < 20, any axis < 3, Terse Format < 3, Voice Immediacy < 3, or Name Quality < 3.

## Rejected Personae

Failed submissions are saved to `reject/` with notes explaining why. This prevents repeated bad seeds and documents which archetypes don't survive the format.

## Licensing

All code in this repository is released under the [0-Clause BSD License](LICENSE). SOUL.md files in `docs/` may be used, modified, and deployed freely — no attribution required.
