# Pipeline Orchestration Guide

This document governs how pipeline tasks are created, linked, and validated. Every worker who creates kanban tasks must follow these rules. Getting them wrong produces the blocked tasks we just debugged.

---

## Creation Order and Chain Rules

The pipeline is a **strictly linear chain**:

```
T1 (Researcher) → T1b (Namer) → T2 (Writer) → T3 (Reviewer) → T5 (Refiner) → T6 (Final Reviewer)
```

Each stage is the **parent of the next**. A task MUST NOT be created unless its upstream parent either exists or is created in the same orchestration step.

### Critical Rule: No Gaps Allowed

If you are creating a task for Stage N, Stage N-1 must:
- Already exist on the board as a done task (with its output artifact on disk), OR
- Be created alongside Stage N in the same orchestration step.

**THIS IS NOT OPTIONAL.** Creating a downstream task without its upstream parent is the root cause of phantom-blocked chains like "T3 Review farrier" with no `drafts/farrier.md`.

### Stage-to-Profile Mapping

| Stage | Title pattern | `assignee` value |
|-------|---------------|------------------|
| T1b | `T1b: Name <Seed>` | `namer` |
| T2 | `T2: Write <Name> SOUL.md` | `writer` |
| T3 | `T3: Review <Name> SOUL.md` | `reviewer` |
| T5 | `T5: Refine <Name> SOUL.md` | `refiner` |
| T6 | `T6: Final-review <Name> SOUL.md` | `final-reviewer` |

Do NOT assign all stages to one profile. Do NOT use the creating worker's own profile.

### Task Workspace

Every task MUST be created with:
```yaml
workspace_kind: "dir"
workspace_path: "/home/kimbo/.hermes/projects/soul-repository"
```

`scratch` workspaces isolate workers in temporary directories where they cannot read AGENTS.md, cannot see existing personae, and cannot write outputs to the correct locations.

---

## Pre-Flight Checks Before Creating Any Task

Before calling `kanban_create`, verify the upstream artifact exists. If it does not, you MUST create the missing upstream stages first.

| Creating stage | Required upstream artifact | Path to check |
|---|---|---|
| T1b | Seed file | `seeds/<seed-label>.md` |
| T2 | Chosen name file | `names/<chosen-name>.md` |
| T3 | Draft file | `drafts/<name>.md` |
| T5 | Critique file | `critiques/<name>.md` |
| T6 | Refined file | `refined/<name>.md` |

**If the file doesn't exist:** Do NOT create the downstream task. Create the missing upstream stages instead. For example:
- If `seeds/the-farrier.md` exists but no `drafts/farrier.md`, create a T1b → T2 chain for farrier first.
- If `critiques/cross.md` exists but no `refined/cross.md`, create a T5 for cross first.

---

## Input File Path Rules

The `Input draft file` directive in each task body MUST reference the correct directory for that stage:

| Stage | Output directory | Task body must reference |
|---|---|---|
| T2 | `drafts/` | Input: `names/<name>.md` |
| T3 | `critiques/` | Input: `drafts/<name>.md` |
| T5 | `refined/` | Input: `drafts/<name>.md` + `critiques/<name>.md` |
| T6 | `archive/` or `reject/` | Input: `refined/<name>.md` |

**T6 MUST read `refined/<name>.md`, never `drafts/<name>.md`.** Passing the wrong path means T6 judges stale draft content instead of the refiner's actual output.

---

## T6 Retry Chain (On Rejection)

When T6 rejects a draft, it does NOT block. It creates a **loopback**:

1. Create a new T5 task with:
   - The `refined/<name>.md` file as input
   - The specific failure notes from T6 as the critique
   - A clear instruction on what must change to pass

2. **In the same orchestration step**, create a T6 child task chained to the new T5 (assignee: `final-reviewer`, parents: [new T5 task id]).

3. Complete the current T6 with a note that a retry was created.

**Without step 2, the T5 fix completes with no T6 to re-review it — the chain breaks and the fix is orphaned.**

The refiner applies the fixes and returns the draft to T6. Repeat until the draft passes or the character fundamentally cannot be saved.

Only when a draft has failed T6 three times with the same structural flaw should you consider abandoning it — and even then, the final disposition is `reject/<name>.md` with a note explaining which seed archetype does not work.

---

## T6 Name-Rejection Chain

If T6 rejects on Name Quality (< 3), the chain is:

1. Create a **standalone** T1b task (no parent) with the archetype context and a note that it replaces the rejected name.
2. The T1b namer renames ALL files and inline content using `mv` (never `cp`), then creates the full downstream chain: T3 → T5 → T6.
3. Complete the current T6 noting that a rename chain was created.

Do NOT rename files yourself. Do NOT create a child T5 chained to the blocked T6 parent — this creates a deadlock.

---

## File Naming Convention

Every stage uses the **chosen character name** as the filename, not the seed label.

The T1b Namer is the source of truth. If the chosen name is **Roux**, all files for that persona are:
- `names/roux.md`
- `drafts/roux.md`
- `critiques/roux.md`
- `refined/roux.md`
- `archive/roux.md` (or `reject/roux.md`)

**Rule:** Read the chosen name from the previous stage's output file. Never construct a filename from the seed label (e.g. `the-galley-chef`).

---

## Git Credentials and HOME Isolation

Kanban workers run with a **profile-isolated HOME**. When a worker uses profile `writer`, its `HOME` is set to `~/.hermes/profiles/writer/home/`. This means `git` looks for `~/.gitconfig` and `~/.git-credentials` inside the profile's `home/` directory.

If `git push` fails with "no credentials configured", the profile's `home/` is missing credentials.

```bash
cp ~/.git-credentials ~/.hermes/profiles/<profile>/home/.git-credentials
cp ~/.gitconfig ~/.hermes/profiles/<profile>/home/.gitconfig
chmod 600 ~/.hermes/profiles/<profile>/home/.git-credentials
```

Apply this to all profiles that run `git push`: `writer`, `namer`, `reviewer`, `refiner`, `final-reviewer`.

---

## Process Integrity

Pipeline outputs are read-only. Every file produced by any stage is the artifact of the spec, not raw material for manual editing.

If a draft has the wrong filename, a malformed line, or a missing guardrail, the defect is in the spec — not the file. Fix the reference document or AGENTS.md, then re-run the stage. Never manually edit, rename, move, commit, or otherwise touch any output from any pipeline stage.

This rule exists because manual edits destroy provenance. If a file in `archive/` was hand-corrected, no one can verify which parts came from the pipeline and which came from post-hoc intervention. The result is untrustworthy.
