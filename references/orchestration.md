# Pipeline Orchestration Guide

This document governs how pipeline tasks are created, linked, and validated. Every worker who creates kanban tasks must follow these rules.

---

## Pipeline Architecture

The pipeline is a **linear 5-stage pipeline** with pre-flight gates and no internal retry loops:

```
Researcher (T0) → Namer → Writer → Evaluator → Publisher
```

Researcher (T0) is the orchestrator that finds archetypes and spawns Namer tasks. Each subsequent stage is **independent** — there are no parent/child chain dependencies between stages. Each stage reads its input from disk and writes its output to disk. The next stage discovers its input by convention (known file paths), not by task-parent linkage.

---

## Progressive Disclosure

Each stage only sees what it needs:

- **Researcher** sees the published souls in docs/ and existing seeds. It hunts for characters that delight, then generates seed candidates.
- **Namer** sees the seed. It runs the 6 character tests, generates 5 candidate names, scores them, and picks the best. One pass, done.
- **Writer** sees the chosen name + seed. It produces one SOUL.md, focusing on finding a genuine voice rather than generating variants. See `references/stage-writer.md` for the writing approach.
- **Evaluator** sees the draft. It evaluates for pulse (voice, contradiction, vitality quality) and either picks it (with fix notes) or rejects it and kills the seed.
- **Publisher** sees the winning candidate + evaluator's notes. It either approves directly or applies targeted fixes to specific issues, then publishes to docs/ and rebuilds the site.

**The Evaluator is the sole quality gate.** Evaluators and Publishers do NOT mechanically check format, line counts, or word counts — format rules are guidance the Evaluator weighs as part of its verdict. They evaluate creative quality and fix scoping only.

---

## Creation Order and Chain Rules

### No Parent/Child Chains

Stages are **independent**. A task MUST NOT be created with `parent` links to upstream stages. Each stage reads its input from a known file path, not from task-parent linkage.

### Stage Independence

Each stage can be created independently once its required artifact exists on disk:

| Stage | Required artifact on disk before creating |
|---|---|---|
| Researcher | — (creates seeds) |
| Namer | `seeds/<seed>.md` |
| Writer | `names/<name>.md` + `seeds/<seed>.md` |
| Evaluator | Draft file at `drafts/<name>.md` |
| Publisher | Winning candidate at `drafts/<name>.md` + evaluator notes |

### Self-Propagating Chains

Each stage creates the next stage's task as part of its completion. The Namer creates a Writer task. The Writer creates an Evaluator task. The Evaluator creates a Publisher task (or kills the seed). The Publisher is terminal — no next task.

**Chain rule:** Before creating the next task, verify the upstream artifact exists on disk. If it doesn't, kanban_block with the reason.

### The Evaluator Is the Sole Quality Gate

Format rules (line count, word count, sign-off presence, H1 match, etc.) are guidance the Evaluator weighs as part of its verdict, not a separate mechanical gate. Evaluators evaluate creative quality against the reference personae. Do NOT ask evaluators to run mechanical checks — it wastes their cognitive budget.

Rely on the Evaluator's verdict before creating a Publisher task. If the Evaluator flagged issues, note them in the Publisher task so targeted fixes are applied.

---

## Stage-to-Profile Mapping

| Stage | Title pattern | `assignee` value | Purpose |
|---|---|---|---|
| Researcher | `Research <topic>` | `soul-researcher` | Archetype discovery, seed generation |
| Namer | `Namer <seed-label>` | `soul-namer` | Viability gate (6 character tests) + name selection |
| Writer | `Write <Name> SOUL.md` | `soul-writer` | Single focused write, principles with examples |
| Evaluator | `Evaluate <Name> SOUL.md` | `soul-evaluator` | Pulse evaluation or kill |
| Publisher | `Publish <Name> SOUL.md` | `soul-publisher` | Approve/flag, publish to docs/, site rebuild |

Do NOT assign all stages to one profile. Do NOT use the creating worker's own profile.

---

## Task Workspace

Every task MUST be created with:

```yaml
workspace_kind: "dir"
workspace_path: "/home/kimbo/projects/soul-repository"
```

`scratch` workspaces isolate workers in temporary directories where they cannot read AGENTS.md, cannot see existing personae, and cannot write outputs to the correct locations.

---

## Pre-Flight Checks Before Creating Any Task

Before calling `kanban_create`, verify the upstream artifact exists on disk.

| Creating stage | Required upstream artifact | Path to check | Quality gate |
|---|---|---|---|
| Researcher | Published souls + seeds | `docs/`, `seeds/` | — |
| Namer | Seed file | `seeds/<seed-label>.md` | — |
| Writer | Chosen name file + seed | `names/<chosen-name>.md`, `seeds/<seed-label>.md` | — |
| Evaluator | Draft file | `drafts/<name>.md` | — |
| Publisher | Winning candidate + evaluator notes | `drafts/<name>.md` (as picked by evaluator) | Evaluator verdict must be APPROVE/FLAG (notes carry any fix items for the Publisher) |

**If the file doesn't exist:** Do NOT create the downstream task. Create the missing upstream stages instead.

**If the Evaluator flags issues:** Note them in the Publisher task body so the Publisher can apply targeted fixes.

---

## Input File Path Rules

The `Input file` directive in each task body MUST reference the correct directory for that stage:

| Stage | Output directory | Task body must reference |
|---|---|---|
| Researcher | `seeds/` | Input: `docs/`, `seeds/` |
| Namer | `names/` | Input: `seeds/<seed-label>.md` |
| Writer | `drafts/` | Input: `names/<name>.md` + `seeds/<seed-label>.md` |
| Evaluator | `evaluations/` | Input: `drafts/<name>.md` |
| Publisher | `docs/` | Input: `drafts/<name>.md` (the winning candidate) + evaluator notes |

**Writer writes 1 file:** `<name>.md` to `drafts/`.

**Evaluator writes evaluation notes** to `evaluations/<name>.md` covering the voice assessment, decision rationale, and any fix items for the Publisher.

**Publisher reads the winning candidate from Evaluator** — there is one draft; the Evaluator either picks it or rejects it. If picked, the Publisher reads the draft and the evaluator's fix notes.

---

## Publisher Approval / Fix / Kill Logic

The Publisher has two paths:

### APPROVE Path

1. Read the winning candidate from `drafts/<name>.md`.
2. Confirm the Evaluator's verdict is APPROVE (no fixable issues). If so, proceed. If the Evaluator flagged issues, see FLAG path.
3. Copy the candidate to `docs/<name>.md`.
4. Rebuild the site.
5. Complete the task with a summary.

### FLAG Path

1. Read the winning candidate from `drafts/<name>.md`.
2. Read the evaluator's minor-issue notes.
3. Apply **targeted fixes** only — fix the specific issues identified by the evaluator. Do not rewrite, restyle, or improve the draft beyond the scoped fixes.
   - "Fix these 3 things" means exactly 3 changes, not "make it better."
4. Confirm the flagged issues are resolved in the fixed copy.
5. Copy the fixed candidate to `docs/<name>.md`.
6. Rebuild the site.
7. Complete the task noting which fixes were applied.

### KILL Path (Evaluator rejects the draft)

If the Evaluator rejects the draft:

1. The seed is killed. Do NOT create a Publisher task.
2. Move the seed to `reject/<seed-label>.md` (or note the kill in `references/viability-log.md`).
3. Log the failure in `references/viability-log.md` explaining why the seed archetype failed.
4. Complete the Evaluator task with the kill note.

---

## File Naming Convention

Every stage uses the **chosen character name** as the filename, not the seed label.

The Namer is the source of truth. If the chosen name is **Roux**, all files for that persona are:

- `names/roux.md`
- `drafts/roux.md`
- `docs/roux.md` (or `reject/<seed-label>.md` if killed)

**Rule:** Read the chosen name from the Namer's output file (`names/<name>.md`). Never construct a filename from the seed label (e.g. `the-galley-chef`).

**Writer output:** The Writer writes `<name>.md` to `drafts/`.

**Publisher output:** The winning draft is copied to `docs/<name>.md`.

---

## Git Credentials and HOME Isolation

Kanban workers run with a **profile-isolated HOME**. When a worker uses profile `soul-writer`, its `HOME` is set to `~/.hermes/profiles/soul-writer/home/`. This means `git` looks for `~/.gitconfig` and `~/.git-credentials` inside the profile's `home/` directory.

If `git push` fails with "no credentials configured", the profile's `home/` is missing credentials.

```bash
cp ~/.git-credentials ~/.hermes/profiles/<profile>/home/.git-credentials
cp ~/.gitconfig ~/.hermes/profiles/<profile>/home/.gitconfig
chmod 600 ~/.hermes/profiles/<profile>/home/.git-credentials
```

Apply this to all profiles that run `git push`: `soul-writer`, `soul-namer`, `soul-evaluator`, `soul-publisher`.

---

## Process Integrity

1. **Read `references/stage-*.md` before creating tasks.** Do not guess at the instructions.
2. **Verify artifacts exist before creating downstream tasks.** Never assume a previous stage completed.
3. **Rely on the Evaluator's verdict before the Publisher stage.** Flagged issues become targeted fixes.
4. **Use full task bodies.** Abbreviated task bodies produce incomplete work.
5. **Do not create parent/child chains between stages.** Each stage is independent — it reads its input from disk, not from task linkage.
6. **Do not skip stages.** Every seed goes through all 5 stages: Researcher → Namer → Writer → Evaluator → Publisher.
7. **Log failures.** Killed personae go in `references/viability-log.md`. This prevents repeated failures.
8. **No retry loops.** If the Evaluator rejects the draft, the seed is killed. Do not re-generate candidates.
9. **Scoped fixes only.** The Publisher FLAG path applies exactly the fixes specified by the Evaluator — no more, no less. "Fix these 3 things" means 3 changes, not a rewrite.
10. **Separate format from craft in task bodies.** Research (Yun et al., 2025) shows that structural format tokens embedded in generation prompts actively induce diversity collapse. When building task bodies for creative stages (Writer, Namer, Researcher), place format constraints at the END of the task body, clearly separated from craft instructions. The worker reads craft guidance first, then checks compliance rules last. Format rules should be presented as a post-generation compliance checklist, not interleaved with creative instruction. Example: the Writer's task body should have the craft sections ("Tension in the Identity Line," "The Diagnostic Eye," etc.) first, followed by a clearly marked "## Format Constraints (check after writing)" section at the bottom. Never embed line-count rules, word-count rules, or structural requirements inside the craft guidance sections.

---

## Version v5.3.0 — 2026-08-10
