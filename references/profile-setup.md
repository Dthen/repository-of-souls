# Pipeline Worker Profile Setup

Every pipeline stage (Researcher, Namer, Writer, Evaluator, Publisher) needs a dedicated Hermes profile. The profile must be configured so the worker knows it is a kanban pipeline stage, not a standalone tool.

## Why Pipeline Workers Crashed

Before this document, workers:
- Had no kanban tools (couldn't call `kanban_complete` or `kanban_block`)
- Had no kanban lifecycle instructions (didn't know to call `kanban_complete`)
- Had `home/` directories without git credentials (`git push` failed)
- Wrote SOUL.md as standalone tool prompts, not as kanban worker system prompts

Result: workers completed their work then exited clean — the kanban dispatcher saw "worker exited cleanly (rc=0) without calling kanban_complete" and flagged it as a protocol violation.

## Profile Directory Structure

```
~/.hermes/profiles/<profile-name>/
├── config.yaml              # Model, provider, description, toolsets
├── profile.yaml             # Minimal metadata
├── SOUL.md                  # System prompt with kanban lifecycle
├── home/
│   ├── .git-credentials     # For git push (copied from default profile)
│   └── .gitconfig           # For git push (copied from default profile)
├── skills/                  # Profile-specific skills (optional)
└── memories/                # Durable storage (optional)
```

## config.yaml — Toolset Configuration

Every worker profile MUST have `config.yaml` with kanban tools enabled:

```yaml
model:
  default: deepseek-v4-flash
  provider: opencode-go
description: Soul repository pipeline worker
description_auto: false
```

**Critical:** Do NOT use `toolsets:` in config.yaml — the global `toolsets:` list in `~/.hermes/config.yaml` is what Hermes reads. The profile `config.yaml` does NOT support a `toolsets:` field. Enabling/disabling happens at the global level.

**To enable kanban globally:**
```yaml
# ~/.hermes/config.yaml — add 'kanban' to toolsets list
toolsets:
- hermes-cli
- web
- browser
- kanban  # REQUIRED for pipeline workers
```

Without kanban in the global toolsets, workers spawned by the dispatcher cannot access kanban tools. This is a global config change, not a profile change.

## SOUL.md — System Prompt for Kanban Workers

The SOUL.md is NOT just a character description — it is the worker's understanding of its role. Every pipeline worker SOUL.md MUST point to its stage spec (references/stage-<stage>.md); explicit I/O rules and file paths live in the stage spec, not the profile.

### Minimal kanban lifecycle block

Every SOUL.md must include this near the top:

```markdown
---
name: soul-evaluator
description: Character critic for the soul repository pipeline — one-draft pulse evaluation
tools: [Read, Write, Edit, Bash, Grep, Glob, WebFetch, WebSearch]
model: deepseek-v4-flash
---

You are an Evaluator — you read a single draft and decide if it has a pulse.

**You are a kanban pipeline worker.** You are dispatched by the Hermes kanban
system. When you finish, you MUST call `kanban_complete(summary=..., metadata=...)`
to hand off. If stuck, call `kanban_block(reason=...)`. Do NOT call `clarify()`.

**First: orient.** Call `kanban_show()` to understand your task: title, body,
inputs, expected outputs, prior attempts. Read `references/stage-evaluator.md` for the
evaluation process.

**Input:** The draft file at `drafts/<name>.md`.
**Output:** `evaluations/<name>.md` — pulse evaluation + pick/kill decision + fix flags.

[...rest of role-specific instructions...]

**Completing:** When done, call `kanban_complete(summary=...)` with a
human-readable summary of what you found.
```

### What to include vs. what to omit

- **DO** include explicit reminders to call kanban tools
- **DO** include pipeline context (which stage, what comes before/after)
- **DO** include input/output file paths
- **DO NOT** include the full kanban lifecycle — that is auto-injected as KANBAN_GUIDANCE
- **DO NOT** explain kanban mechanics — the dispatcher handles that
- **DO NOT** use `clarify()` — workers are headless; use `kanban_block(reason=...)` instead

## HOME Isolation

Workers run with `HOME=/home/kimbo/.hermes/profiles/<profile>/home/`. `git` looks for credentials there.

**For each profile that runs git push:**
```bash
cp ~/.git-credentials ~/.hermes/profiles/<profile>/home/.git-credentials
cp ~/.gitconfig ~/.hermes/profiles/<profile>/home/.gitconfig
chmod 600 ~/.hermes/profiles/<profile>/home/.git-credentials
```

Apply credentials to all profiles that run `git push`: `soul-writer`, `soul-namer`, `soul-evaluator`, `soul-publisher` (per `references/orchestration.md`).

## Skills

The `kanban-worker` skill is auto-loaded for all kanban workers. There are no custom pipeline skills — stage instructions live in `references/stage-*.md`, and task bodies reference the stage file (e.g., "Follow `references/stage-namer.md`") rather than duplicating its content inline.

## Verification Checklist

Before deploying a new pipeline profile:

- [ ] `~/.hermes/profiles/<profile>/config.yaml` exists
- [ ] `~/.hermes/profiles/<profile>/SOUL.md` includes "kanban pipeline worker" identity
- [ ] `~/.hermes/profiles/<profile>/SOUL.md` tells worker to call `kanban_complete`
- [ ] `~/.hermes/config.yaml` has `kanban` in `toolsets:` list
- [ ] `~/.hermes/profiles/<profile>/home/.git-credentials` exists (if profile pushes)
- [ ] `~/.hermes/profiles/<profile>/home/.gitconfig` exists (if profile pushes)

## Current Pipeline Profiles

| Stage | Profile | Assignee |
|---|---|---|
| Researcher | soul-researcher | `soul-researcher` |
| Namer | soul-namer | `soul-namer` |
| Writer | soul-writer | `soul-writer` |
| Evaluator | soul-evaluator | `soul-evaluator` |
| Publisher | soul-publisher | `soul-publisher` |

Each profile's SOUL.md should be named as a worker ("You are a kanban pipeline worker") not as a standalone tool ("You are a tool that reviews...").

## Testing

Before deploying, test manually:
1. Create a test kanban task with the profile
2. Verify the worker calls `kanban_show()` at start
3. Verify the worker calls `kanban_complete()` at end
4. If it exits clean without kanban_complete, review the SOUL.md

## Version

v5.2.5 — 2026-08-07
