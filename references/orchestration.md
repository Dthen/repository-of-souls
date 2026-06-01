# Pipeline Orchestration Guide

This document governs how pipeline tasks are created, linked, and validated. Every worker who creates kanban tasks must follow these rules.

---

## Pipeline Architecture

The pipeline is a **strictly linear chain** with pre-flight gates:

```
T0 (Viability) → T2 (Namer) → T3 (Writer) → T4 (Reviewer) → T5 (Refiner) → T6 (Final Reviewer)
```

T1 is the researcher (not on the kanban board). T0 is a kanban gate that runs after T1 produces seeds.

### Progressive Disclosure

The pipeline uses **progressive disclosure** — each stage only sees what it needs:

- **T0** sees the seed archetype and name candidates. It checks viability before investing pipeline cycles.
- **T2** sees the viable seed. It picks a name.
- **T3** sees the seed + chosen name. It writes a draft.
- **T4** sees the draft. It evaluates creative quality (not format compliance — that's automated).
- **T5** sees the draft + critique. It refines.
- **T6** sees the refined draft. It evaluates whether the character has a pulse.

**Compliance is automated.** `check_soul.py` runs before T4 and T6. Reviewers do NOT check format, line counts, or word counts. They evaluate creative quality only.

---

## Creation Order and Chain Rules

Each stage is the **parent of the next**. A task MUST NOT be created unless its upstream parent either exists or is created in the same orchestration step.

### Critical Rule: No Gaps Allowed

If you are creating a task for Stage N, Stage N-1 must:
- Already exist on the board as a done task (with its output artifact on disk), OR
- Be created alongside Stage N in the same orchestration step.

**THIS IS NOT OPTIONAL.** Creating a downstream task without its upstream parent is the root cause of phantom-blocked chains.

### Critical Rule: Full Task Body Only

Every task body MUST include the **complete stage instructions** from the relevant `references/stage-*.md` file. Do NOT write abbreviated task bodies. Do NOT omit the Archive Process section, the `build_site.py` step, git commit/push instructions, rejection-chain creation rules, or any other part of the spec. **This is especially true for test runs.** A worker receives its instructions from the task body; if the body is incomplete, the worker produces incomplete work. Read the full stage file and include every section.

### Critical Rule: Automate Compliance, Evaluate Quality

Format compliance (line count, word count, sign-off count, H1 match, etc.) is handled by `scripts/check_soul.py`. Reviewers (T4, T6) evaluate creative quality only. Do NOT ask reviewers to check compliance — it wastes their cognitive budget and turns them into format cops.

Run `check_soul.py` before creating T4 or T6 tasks. If the draft fails compliance, fix it or send it back to the writer. Do not send non-compliant drafts to reviewers.

---

## Stage-to-Profile Mapping

| Stage | Title pattern | `assignee` value | Purpose |
|-------|---------------|------------------|---------|
| T0 | `T0: Viability <Seed>` | `soul-namer` or `soul-writer` | 5-question viability gate |
| T2 | `T2: Name <Seed>` | `soul-namer` | Pick a name |
| T3 | `T3: Write <Name> SOUL.md` | `soul-writer` | Write draft |
| T4 | `T4: Review <Name> SOUL.md` | `soul-reviewer` | Developmental editing — Four Pillars |
| T5 | `T5: Refine <Name> SOUL.md` | `soul-refiner` | Craft editing — fix gaps |
| T6 | `T6: Final-review <Name> SOUL.md` | `soul-final-reviewer` | Senior gate — Three Questions |

Do NOT assign all stages to one profile. Do NOT use the creating worker's own profile.

---

## Task Workspace

Every task MUST be created with:
```yaml
workspace_kind: "dir"
workspace_path: "/home/kimbo/.hermes/projects/soul-repository"
```

`scratch` workspaces isolate workers in temporary directories where they cannot read AGENTS.md, cannot see existing personae, and cannot write outputs to the correct locations.

---

## Pre-Flight Checks Before Creating Any Task

Before calling `kanban_create`, verify the upstream artifact exists and (for review stages) that compliance checks pass.

| Creating stage | Required upstream artifact | Path to check | Compliance check |
|---|---|---|---|
| T0 | Seed file | `seeds/<seed-label>.md` | — |
| T2 | Viability passed | T0 task done | — |
| T3 | Chosen name file | `names/<chosen-name>.md` | — |
| T4 | Draft file + compliance | `drafts/<name>.md` | `check_soul.py` must pass |
| T5 | Critique file | `critiques/<name>.md` | — |
| T6 | Refined file + compliance | `refined/<name>.md` | `check_soul.py` must pass |

**If the file doesn't exist:** Do NOT create the downstream task. Create the missing upstream stages instead.

**If `check_soul.py` fails:** Do NOT create the review task. Send the draft back to the writer with the compliance report as feedback.

---

## Input File Path Rules

The `Input file` directive in each task body MUST reference the correct directory for that stage:

| Stage | Output directory | Task body must reference |
|---|---|---|
| T0 | (no output file) | Input: `seeds/<seed-label>.md` |
| T2 | `names/` | Input: `seeds/<seed-label>.md` |
| T3 | `drafts/` | Input: `names/<name>.md` |
| T4 | `critiques/` | Input: `drafts/<name>.md` |
| T5 | `refined/` | Input: `drafts/<name>.md` + `critiques/<name>.md` |
| T6 | `archive/` or `reject/` | Input: `refined/<name>.md` |

**T6 MUST read `refined/<name>.md`, never `drafts/<name>.md`.** Passing the wrong path means T6 judges stale draft content instead of the refiner's actual output.

**T4 MUST NOT read `critiques/<name>.md` as its input.** T4 writes the critique; it does not read one.

---

## T6 Retry Chain (On REFINE verdict)

When T6 returns REFINE (not APPROVE or KILL), it creates a **loopback**:

1. Write a specific rejection note (2–3 paragraphs) explaining which of the Three Questions failed and why. Quote problematic lines. Suggest fixes.
2. Create a new T5 task with:
   - The `refined/<name>.md` file as input
   - Your rejection note as the critique
   - A clear instruction on what must change to pass
3. **In the same orchestration step**, create a T6 child task chained to the new T5 (assignee: `soul-final-reviewer`, parents: [new T5 task id]).
4. Complete the current T6 with a note that refinement was requested.

**Without step 3, the T5 fix completes with no T6 to re-review it — the chain breaks and the fix is orphaned.**

The refiner applies the fixes and returns the draft to T6. Repeat until the draft passes or the character fundamentally cannot be saved.

Only when a draft has failed T6 **three times with the same structural flaw** should you consider KILL.

---

## T6 Kill Process (On KILL verdict)

When T6 returns KILL (unfixable):

1. Move the draft to `reject/<name>.md`.
2. Write a note explaining which seed archetype does not work and why.
3. Log the failure in `references/viability-log.md`.
4. Complete the T6 task with the kill note.

**T1 researchers read `references/viability-log.md` before proposing new seeds.** If the killed archetype appears in the log, the researcher should avoid it.

---

## T6 Name-Rejection Chain

If T6 rejects on name quality (not a person, common word, stereotype), the chain is:

1. Create a **standalone** T2 task (no parent) with the archetype context and a note that it replaces the rejected name.
2. The T2 namer picks a new name, renames the existing file, and creates the downstream chain: **T4 → T5 → T6**.
3. Complete the current T6 noting that a rename chain was created.

**How the rename works:** The content is already in archive — T2 revises it in place, not rewrites from scratch. T2 moves `archive/<old>.md` → `drafts/<new>.md`, then updates every reference to the old name: the H1, the identity line, and any other mentions in the body. Use `grep -ri "<old-name>" .` to find them all. The content, voice, and structure stay the same — only the name changes.

**Important:** Do NOT rename files yourself. Do NOT create a child T5 chained to the blocked T6 parent — this creates a deadlock. The T2 namer handles the rename; the downstream chain reviews the renamed content.

---

## File Naming Convention

Every stage uses the **chosen character name** as the filename, not the seed label.

The T2 Namer is the source of truth. If the chosen name is **Roux**, all files for that persona are:
- `names/roux.md`
- `drafts/roux.md`
- `critiques/roux.md`
- `refined/roux.md`
- `archive/roux.md` (or `reject/roux.md`)

**Rule:** Read the chosen name from the previous stage's output file. Never construct a filename from the seed label (e.g. `the-galley-chef`).

---

## Git Credentials and HOME Isolation

Kanban workers run with a **profile-isolated HOME**. When a worker uses profile `soul-writer`, its `HOME` is set to `~/.hermes/profiles/writer/home/`. This means `git` looks for `~/.gitconfig` and `~/.git-credentials` inside the profile's `home/` directory.

If `git push` fails with "no credentials configured", the profile's `home/` is missing credentials.

```bash
cp ~/.git-credentials ~/.hermes/profiles/<profile>/home/.git-credentials
cp ~/.gitconfig ~/.hermes/profiles/<profile>/home/.gitconfig
chmod 600 ~/.hermes/profiles/<profile>/home/.git-credentials
```

Apply this to all profiles that run `git push`: `soul-writer`, `soul-namer`, `soul-reviewer`, `soul-refiner`, `soul-final-reviewer`.

---

## Process Integrity

Pipeline outputs are read-only. Every file produced by any stage is the artifact of the spec, not raw material for manual editing.

If a draft has the wrong filename, a malformed line, or a missing guardrail, the defect is in the spec — not the file. Fix the reference document or AGENTS.md, then re-run the stage. Never manually edit, rename, move, commit, or otherwise touch any output from any pipeline stage.

This rule exists because manual edits destroy provenance. If a file in `archive/` was hand-corrected, no one can verify which parts came from the pipeline and which came from post-hoc intervention. The result is untrustworthy.
