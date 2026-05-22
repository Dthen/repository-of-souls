# Contributing to the SOUL.md Archive

## Ways to Contribute

### 1. Propose a New Persona

New personae enter through the pipeline or by direct PR.

**Option A: Direct PR (fastest)**

Write a SOUL.md that satisfies the format rules (see `METHODOLOGY.md` §Format and §Mandatory Content) and open a PR. A maintainer will score it on the 7 axes and approve or request changes.

**Option B: Submit a Seed**

If you have an idea but not the full draft, add a row to `seeds/SEEDS.md` with:
- **Archetype** (e.g., "botanist", "chess hustler", "archivist")
- **Domain** (where this persona lives)
- **Metaphor** (how they relate to tool use)
- **Functional Risk** (what could go wrong)

A seed must be distinct from existing personae in at least two of: archetype, domain, or metaphor.

**Option C: Run the Pipeline**

If you have Hermes Agent set up locally, the full 5-stage pipeline is defined in `METHODOLOGY.md`. Run it and PR the resulting `archive/[name].md`.

### 2. Improve an Existing Persona

Open a PR editing the `archive/[name].md` file directly. Changes should:
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
- [ ] 8–20 active lines (ignore H1)
- [ ] One sentence per line
- [ ] No bullets, sections, nesting, code blocks
- [ ] Core tension visible in first 4 behavioural lines
- [ ] Quotable line in first 4 behavioural lines
- [ ] ≤ 3 Never statements, each blocking an archetype-specific risk
- [ ] Address rule present and specific
- [ ] Sign-off rule present and voiced in character
- [ ] No tool-mapping tables — metaphor lives in behavioural lines

## Review Process

All submissions are scored 1–5 on:

1. **Distinctiveness** — swappable with "Generic Assistant?"
2. **Functional Safety** — guardrails present and voiced
3. **Consistency Sustainability** — 50 messages: charming or grating?
4. **Metaphor Coherence** — maps to tools, not just accent
5. **Terse Format** — 8–20 lines, one sentence each
6. **Voice Immediacy** — quotable line in first 4 lines
7. **Name Quality** — proper name, fits tone

Auto-reject if: Total < 20, any axis < 3, Terse Format < 3, Voice Immediacy < 3, or Name Quality < 3.

## Rejected Personae

Failed submissions are saved to `reject/` with notes explaining why. This prevents repeated bad seeds and documents which archetypes don't survive the format.

## Licensing

All SOUL.md files in `archive/` are released under CC0 (public domain). Use them, modify them, deploy them — no attribution required.
