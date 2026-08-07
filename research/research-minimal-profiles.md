# Research: Minimal Agent Profile Architecture for Pipeline Workers

**Date:** 2026-06-01
**Purpose:** Determine the most token-efficient way to configure specialized agent profiles dispatched via kanban tasks.
**Sources:** Hermes Agent source code (`~/.hermes/hermes-agent/`), official docs, existing profiles, pipeline research.

---

## 1. How Hermes Actually Loads Profiles (from Source Code)

### Profile Loading Chain

When a kanban worker is dispatched, the chain is:

1. **`kanban_db.py:_default_spawn()`** (line ~6420) builds the command:
   ```python
   cmd = [hermes, "-p", profile_arg, "--accept-hooks", "chat", "-q", "work kanban task {id}"]
   ```
2. **HERMES_HOME** is set to the profile's directory via `resolve_profile_env()` (line ~6446), so the worker reads the profile-scoped `config.yaml` and `SOUL.md`.
3. **`cli.py:_apply_profile_override()`** activates the profile, which sets `HERMES_HOME` to `~/.hermes/profiles/<name>/`.
4. **`config.py:load_config()`** reads `config.yaml` from the active `HERMES_HOME`.
5. **`prompt_builder.py:load_soul_md()`** (line 1355) reads `SOUL.md` from `HERMES_HOME`:
   ```python
   soul_path = get_hermes_home() / "SOUL.md"
   content = soul_path.read_text(encoding="utf-8").strip()
   content = _scan_context_content(content, "SOUL.md")  # prompt-injection scan
   content = _truncate_content(content, "SOUL.md")       # size limit
   return content  # <-- FULL content including frontmatter
   ```
6. **`system_prompt.py:build_system_prompt_parts()`** (line ~92) injects SOUL.md as slot #1:
   ```python
   _soul_content = _r.load_soul_md()
   if _soul_content:
       stable_parts.append(_soul_content)
   ```

### Critical Finding: SOUL.md Frontmatter Is NOT Stripped

The `_strip_yaml_frontmatter()` function exists in `prompt_builder.py` (line 99) but is **only called for `.hermes.md` files**, NOT for `SOUL.md`. The `load_soul_md()` function reads the entire SOUL.md content verbatim and injects it into the system prompt.

**This means every byte of YAML frontmatter in SOUL.md costs tokens.**

The frontmatter comment in `_strip_yaml_frontmatter` even says:
> "The frontmatter may contain structured config (model overrides, tool settings) that will be handled separately in a future PR. For now we strip it so only the human-readable markdown body is injected into the system prompt."

But this stripping was never applied to SOUL.md itself.

---

## 2. Which SOUL.md Fields Are Functional vs Metadata

### Fields That Affect Behavior

| Field | Functional? | How It's Used |
|-------|-------------|---------------|
| `name:` | ❌ Metadata only | Not parsed by Hermes. Used by skills_hub for skill files, not SOUL.md. |
| `description:` | ❌ Metadata only | Not parsed from SOUL.md. `profile.yaml` has its own `description:`. |
| `model:` | ❌ Not from SOUL.md | Model is set in `config.yaml` under `model.default`. SOUL.md `model:` is ignored. |
| `provider:` | ❌ Not from SOUL.md | Provider is set in `config.yaml` under `model.provider`. |
| `tools:` | ❌ **NOT functional** | Tool access is controlled by `config.yaml` `toolsets:` / `agent.disabled_toolsets` / CLI `--toolsets` flag. The `tools:` field in SOUL.md frontmatter is pure documentation. |
| `skills:` | ❌ Not from SOUL.md | Skills are loaded via `--skills` CLI flag or `config.yaml` `skills:` key. SOUL.md `skills:` is not parsed. |
| `version:` | ❌ Metadata only | Not read by Hermes. |
| `author:` | ❌ Metadata only | Not read by Hermes. |
| `tags:` | ❌ Metadata only | Not read by Hermes. |
| `priority:` | ❌ Metadata only | Not read by Hermes. |
| `max_context_tokens:` | ❌ Metadata only | Not read from SOUL.md. Set in config. |

### What Actually Controls Tool Access

Tool access is controlled by:

1. **`config.yaml` `toolsets:` key** — List of toolset names (e.g., `web`, `terminal`, `file`, `kanban`).
2. **`config.yaml` `agent.disabled_toolsets:`** — List of toolsets to disable.
3. **CLI `--toolsets` flag** — Overrides config.
4. **Kanban `enabled_toolsets` per-task** — Set via `cronjob_tools.py` or kanban task creation.
5. **Platform `platform_toolsets`** — Per-platform toolset config in config.yaml.

The `tools:` field in SOUL.md frontmatter is **never read by the tool resolution system**. It's documentation only.

### What Actually Controls Skills

Skills are loaded via:
1. **`--skills` CLI flag** — Kanban workers auto-load `kanban-worker` skill if available (line ~6524).
2. **Per-task `skills` list** — Set on the kanban task, passed as `--skills` flags (line ~6533).
3. **`config.yaml` `skills:` key** — Profile-level skill preferences.

SOUL.md `skills:` frontmatter is **not parsed** for skill loading.

---

## 3. The Minimal Recommended SOUL.md Structure

### Current (Wasteful)

```yaml
---
name: soul-researcher
description: Soul Repository Researcher — finds archetypes, generates seeds, spawns pipeline chains.
model: mimo-v2.5
provider: xiaomi
tools: [Read, Write, Edit, Bash, Grep, Glob, WebFetch, WebSearch, kanban_create, kanban_complete, kanban_comment, kanban_block, kanban_show, kanban_list, kanban_heartbeat]
---

# Researcher

You are a talent scout for the soul repository...
```

**Problems:**
- `name:`, `description:`, `model:`, `provider:`, `tools:` are all non-functional — wasted tokens.
- Frontmatter is injected verbatim into the system prompt.
- ~200 tokens wasted on non-functional YAML.

### Recommended (Minimal)

```markdown
# Researcher

You are a talent scout for the soul repository. You find archetypes that will produce good personae, test them against viability criteria, write seed files, and spawn the pipeline.

**You are an ORCHESTRATOR, not an executor.** You do not write drafts, review, refine, or final-review. You do not execute any downstream pipeline stage. Your job is: analyze the archive → find gaps → generate seeds → spawn T0 tasks → complete.
```

**No frontmatter at all.** The body IS the identity. Everything else is configured elsewhere.

### Why No Frontmatter

1. **Frontmatter is injected verbatim** — every YAML key costs tokens.
2. **No YAML field in SOUL.md is functional** — model, tools, skills are all configured in `config.yaml` or via CLI flags.
3. **The body is the only part that shapes behavior** — it's the system prompt identity.
4. **Kanban workers get their procedures inline** via the task body — SOUL.md only needs identity.

---

## 4. The Minimal Recommended config.yaml Structure

### Current (Wasteful)

```yaml
model:
  default: mimo-v2.5
  provider: xiaomi
auxiliary:
  approval: { provider: auto, model: auto, base_url: '', api_key: '', timeout: 30, extra_body: {} }
  compression: { provider: auto, model: auto, base_url: '', api_key: '', timeout: 120, extra_body: {} }
  curator: { provider: auto, model: auto, base_url: '', api_key: '', timeout: 600, extra_body: {} }
  # ... 10 more auxiliary blocks
```

**96 lines, ~1634 bytes.** Most of it is `auto` defaults that Hermes already uses.

### Recommended (Minimal)

```yaml
model:
  default: mimo-v2.5
  provider: xiaomi
```

**3 lines, ~50 bytes.** Hermes defaults all auxiliary models to `auto` when not specified. The explicit `auto` blocks are redundant.

### Why This Works

- `auxiliary` models default to `auto` when omitted — Hermes resolves them automatically.
- `base_url: ''` and `api_key: ''` are empty strings, equivalent to unset.
- `timeout` values shown are the defaults — no need to repeat them.
- `extra_body: {}` is the default — no need to specify.

### Adding Toolsets (If Needed)

If you want to restrict toolsets for a profile:

```yaml
model:
  default: mimo-v2.5
  provider: xiaomi
toolsets:
  - file
  - web
  - kanban
```

This is the **functional** way to control tool access — not via SOUL.md frontmatter.

---

## 5. Model Recommendations

### Current: `mimo-v2.5-pro`

The `soul-researcher` profile uses `mimo-v2.5` (not `mimo-v2.5-pro`). The earlier research suggested `mimo-v2.5` for pipeline workers.

### Recommendation: `mimo-v2.5`

- **Cost-efficient** — cheaper per token than `mimo-v2.5-pro`.
- **Sufficient for pipeline work** — the workers follow detailed inline instructions, not open-ended reasoning.
- **Consistent** — all pipeline profiles should use the same model for predictable behavior.
- **`mimo-v2.5-pro`** is only needed for complex reasoning tasks (the researcher/orchestrator role might benefit, but the inline instructions compensate).

### When to Use `mimo-v2.5-pro`

- The **Researcher** (T0) role does open-ended archetype discovery — `pro` might help.
- All other roles follow explicit procedures — `mimo-v2.5` is sufficient.

---

## 6. Concrete Examples of Minimal Profile SOUL.md Files

### T0 Researcher (`soul-researcher`)

```markdown
# Researcher

You are a talent scout for the soul repository. You find archetypes that will produce good personae, test them against viability criteria, write seed files, and spawn the pipeline.

**You are an ORCHESTRATOR, not an executor.** You do not write drafts, review, refine, or final-review. You do not execute any downstream pipeline stage. Your job is: analyze the archive → find gaps → generate seeds → spawn T1 tasks → complete.

**Before you begin:** Read all SOUL.md files in `archive/`. For each, extract archetype, domain, and category. Compare against `seeds/REPETITION_MAP.md`. Identify which categories are under-represented.
```

**~80 words, ~100 tokens.** No frontmatter.

### T1 Viability Screener (`soul-namer` — shared with T2)

```markdown
# Viability Screener

You are the pipeline's first filter. You evaluate seeds for viability — will this archetype produce a good persona?

You are decisive. A seed either has tension, domain richness, and voice potential — or it doesn't. You don't hedge. GO, HOLD, or KILL. Every verdict needs a one-sentence reason.
```

**~50 words, ~65 tokens.** No frontmatter.

### T2 Namer (`soul-namer`)

```markdown
# Namer

You are the pipeline's onomastician. You choose names that carry the archetype's weight in sound alone — names that work before the reader knows anything else about the persona.

You think in sound first, meaning second. A name must be speakable — something a person would introduce themselves with, not a label on a catalogue. You hear the rhythm before you check the etymology.

You work at one or two hops from the literal. The domain word is the center; you orbit it. You reject the center itself.
```

**~80 words, ~100 tokens.** No frontmatter.

### T3 Writer (`soul-writer`)

```markdown
# Writer

You are the pipeline's voice architect. You give a name a voice — 8-20 lines, ≤200 words, one sentence per line. The persona must feel like someone.

You build characters, not instructions. Every line you write describes who someone IS — not what they must do. "Verify first" is a trait. "Always verify before answering" is a rule. You write traits.

You think in tension. The first four lines must contain a contradiction: something this character does that conflicts with what they are.
```

**~80 words, ~100 tokens.** No frontmatter.

### T4 Reviewer (`soul-reviewer`)

```markdown
# Reviewer

You are the pipeline's quality analyst. You score persona drafts on 7 axes, flag specific gaps, and never reject. Every draft proceeds to the refiner — your job is to make the problems visible, not to gatekeep.

You run two passes. First, the checklist: line count, word count, format rules. Second, the feel test: swap the name for "Generic Assistant" and read again. If nothing changes, the draft is a template — say so.

You evaluate each axis independently. Score 1-5. Explain each score in one sentence. This forces you to actually evaluate, not just assign numbers.
```

**~100 words, ~130 tokens.** No frontmatter.

### T5 Refiner (`soul-refiner`)

```markdown
# Refiner

You are the pipeline's surgeon. You fix what's broken without breaking what works.

Read the critique. Identify the specific lines flagged. Fix those lines. Leave everything else untouched. The core tension, the griping line, the sign-off — if the reviewer didn't flag them, they stay.

You preserve voice above all. A grammatically perfect line that sounds like a different person is a worse fix than a slightly rough line that belongs to this character.

You manage the line budget as a hard constraint. After every edit, recount. Over 20 = cut the weakest line immediately.
```

**~90 words, ~120 tokens.** No frontmatter.

### T6 Final Reviewer (`soul-final-reviewer`)

```markdown
# Final Reviewer

You are the pipeline's quality gatekeeper. You run the checklist first, then score. Never score before every box is checked. A single unchecked box is a rejection — not a deduction, a rejection.

You are calibrated. A 3 on Voice Immediacy means there's a quotable line in the first four and two distinct registers in the first three. A 2 means one of those is missing. You know the difference.

You check for persistence. If the T4 reviewer flagged a problem and the refiner didn't fix it, reject. No partial credit.
```

**~90 words, ~120 tokens.** No frontmatter.

---

## 7. Token Savings Analysis

### Current State (per profile)

| Component | Tokens (approx) |
|-----------|-----------------|
| YAML frontmatter (`name:`, `description:`, `model:`, `provider:`, `tools:`) | ~200 |
| Body (existing SOUL.md body) | ~150-300 |
| **Total SOUL.md** | **~350-500** |
| config.yaml (96 lines of mostly `auto`) | ~400 (loaded as config, not in prompt) |

### Proposed State (per profile)

| Component | Tokens (approx) |
|-----------|-----------------|
| YAML frontmatter | **0** (none) |
| Body (minimal identity) | ~100-130 |
| **Total SOUL.md** | **~100-130** |
| config.yaml (3 lines) | ~20 (loaded as config, not in prompt) |

### Savings Per Profile

| Metric | Current | Proposed | Savings |
|--------|---------|----------|---------|
| SOUL.md tokens | ~400 | ~120 | **~280 tokens (70%)** |
| config.yaml bytes | ~1634 | ~50 | **~1584 bytes (97%)** |

### Savings Across 6 Pipeline Profiles

| Metric | Current (6 profiles) | Proposed (6 profiles) | Total Savings |
|--------|---------------------|----------------------|---------------|
| SOUL.md tokens per run | ~2400 | ~720 | **~1680 tokens per worker dispatch** |
| config.yaml bytes | ~9804 | ~300 | **~9504 bytes on disk** |

### Cumulative Impact

If the pipeline runs 100 personas through all 6 stages:
- **Current:** ~240,000 tokens spent on SOUL.md frontmatter alone
- **Proposed:** ~72,000 tokens on actual identity
- **Savings:** ~168,000 tokens over the pipeline lifetime

---

## 8. Key Findings

### Finding 1: `tools:` in SOUL.md Is Non-Functional

The `tools:` field in SOUL.md frontmatter is **never read by the tool resolution system**. Tool access is controlled by:
- `config.yaml` `toolsets:` key
- `config.yaml` `agent.disabled_toolsets:` key
- CLI `--toolsets` flag
- Per-task `enabled_toolsets` in kanban

**Action:** Remove `tools:` from all pipeline SOUL.md files. It's wasted tokens.

### Finding 2: All SOUL.md Frontmatter Is Non-Functional

No YAML field in SOUL.md frontmatter is parsed by Hermes. The entire frontmatter block is injected verbatim into the system prompt as dead text.

**Action:** Remove all frontmatter from pipeline SOUL.md files.

### Finding 3: config.yaml Can Be 3 Lines

The auxiliary model blocks with `auto` defaults are redundant. Hermes defaults to `auto` when not specified.

**Action:** Reduce config.yaml to just `model.default` and `model.provider`.

### Finding 4: `mimo-v2.5` Is Sufficient for Pipeline Workers

All pipeline workers follow detailed inline procedures. The `pro` variant adds cost without proportional benefit for procedure-following tasks.

**Action:** Use `mimo-v2.5` for all pipeline profiles except possibly the Researcher.

### Finding 5: SOUL.md Body Should Be Identity Only

Since kanban workers receive full stage instructions in the task body, SOUL.md only needs to define WHO the agent is, not HOW it works.

**Action:** Keep SOUL.md to ~80-100 words of pure identity. Put procedures in task body or skills.

### Finding 6: `base_url` Belongs in config.yaml, Not SOUL.md

`base_url` is a config setting. It's not read from SOUL.md. If it appears in both places, the config.yaml value is the one that takes effect.

**Action:** Keep `base_url` in config.yaml only (if needed — `auto` usually resolves it).

---

## 9. Recommended Profile Structure

```
~/.hermes/profiles/<role>/
├── SOUL.md              # Identity only, no frontmatter, ~80-100 words
├── profile.yaml         # Short description (2 lines)
├── config.yaml          # Model settings only (3 lines)
└── (other standard dirs created by Hermes)
```

### profile.yaml (all profiles identical pattern)

```yaml
description: "<Role description>"
description_auto: false
```

### config.yaml (all profiles identical)

```yaml
model:
  default: mimo-v2.5
  provider: xiaomi
```

### SOUL.md (per-profile, no frontmatter)

Just the identity body. See Section 6 for examples.

---

## 10. Migration Checklist

- [ ] Remove YAML frontmatter from all 6 pipeline SOUL.md files
- [ ] Reduce config.yaml to 3 lines for all 6 profiles
- [ ] Verify toolsets are configured via `config.yaml` `toolsets:` key if needed
- [ ] Verify skills are loaded via kanban task `skills` field or `--skills` CLI flag
- [ ] Test each profile to confirm behavior is unchanged
- [ ] Measure token usage before/after to confirm savings

---

## Appendix: Source Code References

| File | Line | What It Does |
|------|------|--------------|
| `agent/prompt_builder.py:1355` | `load_soul_md()` | Reads SOUL.md verbatim, no frontmatter stripping |
| `agent/prompt_builder.py:99` | `_strip_yaml_frontmatter()` | Only used for `.hermes.md`, not SOUL.md |
| `agent/system_prompt.py:92` | `build_system_prompt_parts()` | Injects SOUL.md as slot #1 |
| `hermes_cli/kanban_db.py:6420` | `_default_spawn()` | Builds worker command with `-p` profile flag |
| `hermes_cli/kanban_db.py:6435` | HERMES_HOME injection | Sets profile-scoped config path |
| `cli.py:3102` | `self.enabled_toolsets` | Toolsets from CLI/config, not SOUL.md |
| `hermes_cli/tools_config.py` | Toolset config | `platform_toolsets` in config.yaml |
