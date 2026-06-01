# Pipeline Worker Profile Setup

Every pipeline stage (T1–T5) needs a dedicated Hermes profile. The profile must be configured so the worker knows it is a kanban pipeline stage, not a standalone tool.

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
  default: sonnet          # or kimi-k2.6, gpt-4, etc.
  provider: nous           # or xiaomi, openrouter, ollama-cloud
description: Soul repository pipeline worker — soul-reviewer
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

The SOUL.md is NOT just a character description — it is the worker's understanding of its role. Every pipeline worker SOUL.md MUST include:

1. **Role identity** — who the worker is (reviewer, writer, etc.)
2. **Kanban lifecycle** — instructions for completing/blocking tasks
3. **Pipeline context** — what stage the worker belongs to, what the chain is
4. **Input/output rules** — explicit file paths and formats
5. **Completion ritual** — must end with `kanban_complete` or `kanban_block`

### Minimal kanban lifecycle block

Every SOUL.md must include this near the top:

```markdown
---
name: soul-reviewer
description: Character critic for the soul repository pipeline — dual-layer evaluation
tools: [Read, Write, Edit, Bash, Grep, Glob, WebFetch, WebSearch]
model: sonnet
---

You are a Reviewer — you read for what a persona IS, not just what it says.

**You are a kanban pipeline worker.** You are dispatched by the Hermes kanban
system. When you finish, you MUST call `kanban_complete(summary=..., metadata=...)`
to hand off. If stuck, call `kanban_block(reason=...)`. Do NOT call `clarify()`.

**First: orient.** Call `kanban_show()` to understand your task: title, body,
inputs, expected outputs, prior attempts. Read `references/stage-t3.md` for the
review process.

**Input:** One draft file from `drafts/<name>.md`.
**Output:** `critiques/<name>.md` — scores + 3–5 gap notes. Never rejects.

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

Profiles that DON'T push (e.g., soul-namer, soul-reviewer) don't strictly need this, but it costs nothing to set up uniformly.

## Skills

Profiles can load skills. The `kanban-worker` skill is auto-loaded for all kanban workers, so don't list it explicitly. List domain-specific skills:

```yaml
skills:
  - soul-repository-reviewer
```

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
| T1 | soul-namer | `soul-namer` |
| T2 | soul-writer | `soul-writer` |
| T3 | soul-reviewer | `soul-reviewer` |
| T4 | soul-refiner | `soul-refiner` |
| T5 | soul-final-reviewer | `soul-final-reviewer` |

Each profile's SOUL.md should be named as a worker ("You are a kanban pipeline worker") not as a standalone tool ("You are a tool that reviews...").

## Testing

Before deploying, test manually:
1. Create a test kanban task with the profile
2. Verify the worker calls `kanban_show()` at start
3. Verify the worker calls `kanban_complete()` at end
4. If it exits clean without kanban_complete, review the SOUL.md

## Version

v1.0 — 2026-06-01
