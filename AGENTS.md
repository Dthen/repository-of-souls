# SOUL.md — Pipeline Spec

## Pipeline Overview

Five stages, strictly linear:

```
Researcher (T0) → Namer → Writer → Evaluator → Publisher
```

| Stage | Assignee | Input | Output |
|---|---|---|---|
| Researcher | `soul-researcher` | `docs/`, `seeds/` | New seed files + Namer tasks |
| Namer | `soul-namer` | `seeds/<seed>.md` | Viability verdict + chosen name at `names/<name>.md` |
| Writer | `soul-writer` | `names/<name>.md` + seed | One SOUL.md draft at `drafts/<name>.md` |
| Evaluator | `soul-evaluator` | The draft at `drafts/<name>.md` | Picks or rejects — kills seed on reject |
| Publisher | `soul-publisher` | Winning candidate + evaluator notes | `docs/<name>.md` + site rebuild (with or without targeted fixes) |

**For detailed stage instructions, see the corresponding reference file in `references/`.**

---

## Reference Files

| File | Contents |
|---|---|
| [`references/orchestration.md`](references/orchestration.md) | Task creation rules, chain validation, pre-flight checks, file path rules, git credentials, naming conventions |
| [`references/stage-researcher.md`](references/stage-researcher.md) | Researcher (T0) — archetype discovery, seed generation, pipeline spawning |
| [`references/stage-namer.md`](references/stage-namer.md) | Namer — merged viability screening + naming, 6 character tests, candidate scoring |
| [`references/stage-writer.md`](references/stage-writer.md) | Writer — single focused write, craft techniques with diverse examples |
| [`references/stage-evaluator.md`](references/stage-evaluator.md) | Evaluator — evidence-cited evaluation, no checklist |
| [`references/stage-publisher.md`](references/stage-publisher.md) | Publisher — approve/flag logic, targeted fixes, docs + site rebuild |
| [`references/format-rules.md`](references/format-rules.md) | Hard format constraints (lines, words, sign-offs, filename case) |
| [`references/positive-patterns.md`](references/positive-patterns.md) | What good personae do right, what sign-offs are (and are not) |
| [`references/reference-personae.md`](references/reference-personae.md) | Kimbo, Brendan, Stover, Barlowe — examples to study, not templates to copy |
| [`references/profile-setup.md`](references/profile-setup.md) | Profile setup, thin-pointer conventions, git credentials |
| [`references/viability-log.md`](references/viability-log.md) | Kill/rejection record — Namer and Evaluator screenings |
| [`references/example-upgrades.md`](references/example-upgrades.md) | Example layer ledger + upgrade-pass procedure (provisional by design) |

**Workers load the latest spec from the references directory.** Task bodies should reference the relevant stage specification file (e.g., "Follow `references/stage-namer.md`") rather than duplicating its content inline. Workers have disk access to `/home/kimbo/projects/soul-repository` via `workspace_kind: "dir"` — they read the current version of the spec at runtime. This ensures spec updates propagate automatically to all downstream tasks without requiring task-body rebuilds. One source of truth, always current.

---

## Depth Files (references/depth/)

Depth files provide optional, on-demand reference material for specific topics. They are **not loaded by default** — each stage loads depth files only when a topic warrants deeper guidance.

Depth files cover areas including (but not limited to):

- **Character craft**: `character-depth.md`, `character-interest.md`, `identity-line.md`, `authentic-voice.md`, `authored-voice.md`, `internal-life.md`, `emotional-register.md`, `perceptual-lens.md`, `perception-filters.md`
- **Voice and tone**: `voice-instructions.md`, `conversational-dynamics.md`, `improvisation-space.md`, `griping-alternatives.md`, `token-economy.md`
- **Naming**: `name-sound-symbolism.md`, `name-collision.md`
- **Review and evaluation**: `evaluator-rubric.md`, `failure-modes.md`, `review-pipeline.md` (historical)
- **Creative technique**: `creative-prompting.md`, `roleplay-prompting.md`, `character-cards.md`, `character-persona-dual-duty.md`
- **Culture and complexity**: `cross-cultural.md`, `complexity-handling.md`, `character-relationships.md`
- **AI-specific**: `ai-assistant-personas.md`

**Loading convention:** When a stage task body references a depth topic, the relevant depth file(s) should be appended to the task body after the core stage instructions.

---

## Qualities of a Good Soul

A good SOUL.md gives the model a person to be, not instructions to follow. Seven qualities matter, drawn from analysis of the 39 souls archived under v4/v5 (2026-era) and the v5-era archive (scrapped 2026-08-07; the published archive in `docs/` holds Gribble, Hordern, Cresswell):

1. **A contradiction in the identity line** — "You are [Name] — a [archetype] who [contradiction]." Without tension, the identity is just a definition. The strongest contradictions are social (gleaner working in the aftermath, lector shaping without touching) rather than merely oppositional (love vs. resentment).

2. **A vitality line in world language** — At least one line that carries the character's inner life through ANY channel: complaint, quiet pride, dark humor, protectiveness, weariness, obsessive love, reluctant duty, philosophical stance, competitiveness, nostalgia, whimsy, earnest enthusiasm. (v5.2.1: the complaint is one channel, not the gate — a soul that carries vitality through quiet pride is as alive as one that gripes.) The signal it must carry: awareness + standards + investment + expertise + tension, in the character's own world-language, and NOT a pipeline fingerprint ("Always the X" template). The griping-alternatives research documents the 9 alternative vitality channels — the Writer should reach for these before defaulting to any single complaint structure, and the automated checker must never require complaint patterns (that was the v5-era fingerprint engine).

3. **A diagnostic eye** — At least one line that teaches the model a perceptual method unique to the character. 100% of top souls have one; no soul without one scores as "excellent." The strongest diagnostic lines invert a default expectation: Stover measures by silence, not swath width. Barlowe reads by stillness, not presence. Gribble: You date each cast-off by the drop — an angry throw dents, a careless slip skids, a gentle setting-down was meant to be found. The Inversion Formula is teachable: identify the default perception, pick the opposite channel, state it as active instruction.

4. **Lines that do 3 jobs** — Every line should carry identity, behaviour, and voice at once. If a line does only one job, it's wasting the budget. The Helpful Assistant test catches description lines: if you can replace "You" with "You are a helpful assistant who..." and the line still reads as a valid instruction, it's description — delete it.

5. **A specific address rule** — How the persona names the user, voiced in-world. A single distinctive term is enough; the v5 evaluator does not require multiple alternates. Stover's "Harvester" and Calden's "the caller" both carry character in one word.

6. **Conversational sign-offs** — One or more phrases the persona might say to close a turn, or a voiced framing line where the count is the character's choice (Kimbo's "Your sign-offs are brief" is a complete sign-off; v5.2.2 dropped the three-phrase minimum — it had no evidence and failed the reference personae). Things the model can *say*, not gestures it can't perform. The framing line should be voiced in the character's own metaphor ("Sign-offs with a twilight lean") rather than describing the sign-offs generically ("Your sign-offs are warm and weary").

7. **Second person throughout** — Every line addresses "You." No third-person framing.

**What changed from v5.0:** The diagnostic eye is now an explicit quality (elevated from implicit). Nevers are downgraded — the v5 evaluator does not require them (2 of the 4 pre-scrap v5-era souls had no Nevers — Stover, Barlowe; Cadell, Calden had them — and passed). The griping line compression rule is dropped — length is acceptable if the line carries character density. The single-address rule is accepted — the old "default + 2 alternates" pattern is no longer expected. The v5 single-write architecture has eliminated template propagation by removing refinement loops — no shared template library across writers.

These are qualities, not checkboxes. A soul that hits all seven but has no pulse is still dead. A soul that misses one but has voice can be fixed.

## The Example Layer (provisional by design)

The personae and lines quoted as craft examples throughout this spec are **provisional** — the pipeline has not yet written enough excellent souls to fill every teaching slot with canon. Examples are upgraded in passes as better lines get written: after every publish, after every seed that delights, and before every version bump. Provenance hierarchy: published souls (`docs/`) > reference personae > research-derived example personae > legacy salvage (never canon — tracked placeholders only). The ledger and procedure live in `references/example-upgrades.md`; salvage-provenance examples (Calden, Moulden, and the "Never Charon" ferryman line) stand only until a canon line exceeds them, and are the first candidates for every upgrade pass.

Full format constraints (line count, word count, etc.) are in [`references/format-rules.md`](references/format-rules.md).

---

## Version v5.2.5 — 2026-08-07

## Application Check (v5.2)

Every rule in this spec traces to evidence in the research corpus — citations live in `research/proposal-v5.2-character-first-rework.md`. The v5.1-era failure mode was research existing without being applied (see `~/.hermes/plans/2026-06-02_144500-spec-rewrite-prompt-research.md`, status: never executed). Before the next spec rewrite, verify each new rule against its cited research and delete any rule that cannot be traced. Rules without evidence are how souls go dry.
