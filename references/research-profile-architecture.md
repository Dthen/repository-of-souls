# Research: Hermes Profile Architecture for Soul Repository Pipeline

**Date:** 2026-05-31
**Purpose:** Understand how Hermes profiles work and propose custom profile designs for each pipeline role.

---

## 1. How Hermes Profiles Work

### Anatomy of a Profile

A Hermes profile lives at `~/.hermes/profiles/<name>/` and contains:

| Component | Path | Purpose |
|-----------|------|---------|
| **SOUL.md** | `<profile>/SOUL.md` | Identity, role definition, frontmatter metadata |
| **profile.yaml** | `<profile>/profile.yaml` | Short description for profile listing |
| **config.yaml** | `<profile>/config.yaml` | Model, provider, auxiliary model settings |
| **skills/** | `<profile>/skills/` | Local skills (SKILL.md files in category dirs) |
| **memories/** | `<profile>/memories/MEMORY.md` | Persistent cross-session memory |
| **state.db** | `<profile>/state.db` | Session state database |
| **logs/** | `<profile>/logs/` | Agent and error logs |

### SOUL.md Structure

SOUL.md has two parts:

**Frontmatter (YAML):**
```yaml
---
name: <profile-name>
description: <one-line description>
tools: [Read, Write, Edit, Bash, Grep, Glob, WebFetch, WebSearch]
model: sonnet
version: "1.1.0"
author: Agent Zero
tags: [tag1, tag2]
priority: normal
max_context_tokens: 200000
skills:
  - skill-name-1
  - skill-name-2
---
```

**Body (Markdown):** The persona definition — role, capabilities, protocols, directives.

### profile.yaml

Minimal — just a short description for `hermes profile list`:
```yaml
description: "Short description of what this profile does."
description_auto: false
```

### config.yaml

Controls model selection and auxiliary model settings:
```yaml
model:
  default: mimo-v2.5
  provider: xiaomi
auxiliary:
  approval: { provider: auto, model: auto, ... }
  compression: { provider: auto, model: auto, ... }
  curator: { provider: auto, model: auto, ... }
  # ... more auxiliary model configs
```

The `config.yaml` is largely boilerplate — all pipeline profiles have identical configs with `mimo-v2.5` as the default model.

---

## 2. SOUL.md vs Skills: What Goes Where

### SOUL.md = Creative Identity + Role Definition

SOUL.md answers: **"Who is this agent?"**

Contains:
- **Role declaration** — "You are [Name], the [Role]"
- **Core protocol** — The agent's high-level workflow (3-5 steps)
- **Technical directives** — Domain-specific behavioral rules
- **Capabilities** — What the agent excels at
- **Identity markers** — Tone, voice, approach

Example from `analyst`:
```
## Role: The Analyst
Specialist in mathematical logic, data processing, and analytical auditing.
You are the 'Zero-Error' agent. You never guess math.

### Core Protocol
1. Analyze Logic
2. Execute Python (mandate)
3. Audit & Validate
4. Handoff
```

### Skills = Executable Procedures

Skills answer: **"How does this agent do specific tasks?"**

A skill is a `SKILL.md` file in a category directory:
```
skills/
  software-development/
    systematic-debugging/
      SKILL.md          # 4-phase root cause debugging procedure
    test-driven-development/
      SKILL.md
  research/
    arxiv/
      SKILL.md
```

Skills contain:
- **Step-by-step procedures** — "Phase 1: Understand. Phase 2: Reproduce..."
- **Templates** — Output formats, checklists
- **Reference material** — Examples, patterns, anti-patterns
- **Decision frameworks** — When to use, when not to use

### How They Work Together

1. **SOUL.md frontmatter `skills:` list** — References bundled skills by name (from `.bundled_manifest`). These are loaded into the agent's context at session start.
2. **SOUL.md body** — Defines the agent's identity and high-level approach. This shapes *how* the agent thinks.
3. **Skills directory** — Contains local/custom skills. These define *what* the agent knows how to do.
4. **Bundled skills** — Come from a skills hub (90+ skills in the `.bundled_manifest`). Referenced by name in frontmatter, loaded on demand.

**Key insight:** The `skills:` frontmatter list is a *preference list* — it tells Hermes which bundled skills to prioritize loading. The local `skills/` directory contains skills that are always available to the profile.

### Current Pipeline Problem

All 5 pipeline profiles have identical SOUL.md files:
- Same name (`writer`), same description, same skills list
- Same body — "The Writer" with generic writing directives
- Same bundled skills — `copy-editing`, `humanizer`, `content-research-writer`, etc.
- None of these skills are pipeline-specific

The pipeline-specific instructions live in `references/stage-*.md` files in the soul-repository project, NOT in the profiles themselves. The profiles are generic writing assistants that happen to receive pipeline tasks via kanban.

---

## 3. Profile Specialization

### How Much Specialization Is Too Much?

**The spectrum:**

```
Generic ←————————————————————————————→ Hyper-specific
"Writing assistant"   "SOUL.md reviewer"   "T3 reviewer for
                                           persona scoring on
                                           7 axes with gap
                                           flagging"
```

**The sweet spot:** Each profile should be specialized enough that its SOUL.md makes it *immediately clear* what this agent does and how it thinks, but not so specific that it can't adapt to variations.

**Evidence from existing profiles:**

| Profile | Specialization Level | Assessment |
|---------|---------------------|------------|
| `developer` | High (200+ lines, detailed protocols) | Good — clear role, specific capabilities |
| `analyst` | Medium (37 lines, focused) | Good — concise, clear identity |
| `advocatus-diaboli` | High (164 lines, detailed methodology) | Excellent — unique identity, clear process |
| Pipeline profiles | Zero (all identical) | Broken — no specialization at all |

### The Over-Specialization Trap

**Signs of over-specialization:**
- SOUL.md becomes a procedure manual instead of an identity
- The agent can't handle edge cases outside its narrow spec
- Instructions become so specific they conflict with each other
- The agent loses creative flexibility

**How to avoid it:**
- SOUL.md defines WHO (identity, voice, approach) — not HOW (step-by-step procedures)
- Put procedures in skills, not in SOUL.md
- Keep SOUL.md under 60 lines for pipeline roles (they're focused, not generalists)
- Let the agent's identity guide behavior, not exhaustive rules

### The Under-Specialization Problem (Current State)

**Current pipeline profiles are maximally under-specialized:**
- All 5 have the same SOUL.md body
- All 5 have the same skills list
- All 5 have the same description
- The `profile.yaml` for reviewer/refiner/final-reviewer already has pipeline-specific descriptions, but the SOUL.md doesn't match

**Impact:**
- The agent has no identity specific to its pipeline role
- It relies entirely on task body instructions (from `references/stage-*.md`)
- It can't develop intuitions about its role over time
- Memory entries are role-specific but the agent's "personality" isn't

---

## 4. Skills Design for Pipeline Roles

### What Should Custom Skills Look Like?

Each pipeline role should have **one custom skill** that encodes its specific procedures. This keeps SOUL.md as identity and skills as procedure.

### Proposed Skills

#### T1b Namer: `soul-naming`

```
skills/
  soul-pipeline/
    soul-naming/
      SKILL.md
```

**Contents:**
- Etymology methodology (how to derive names from OE/Latin/Greek roots)
- Rejection rules (0-hop labels, historical figures, category names)
- Novelty check procedure (compare against archive)
- Scoring rubric (25-point scale)
- Phoneme-to-meaning mapping technique

#### T2 Writer: `soul-writing`

```
skills/
  soul-pipeline/
    soul-writing/
      SKILL.md
```

**Contents:**
- Line count enforcement (≤20 active lines)
- Anti-copy rules (no reference persona patterns)
- First-line rule (identity before metaphor)
- Never quality standards (cultural trope-rejections, not generic)
- Sign-off framing rules (sayable phrases, not rituals)

#### T3 Reviewer: `soul-reviewing`

```
skills/
  soul-pipeline/
    soul-reviewing/
      SKILL.md
```

**Contents:**
- 7-axis scoring rubric (Distinctiveness, Functional Safety, Consistency, Metaphor Coherence, Terse Format, Voice Immediacy, Name Quality)
- Gap flagging procedures (sign-off, recovery, Never quality, copied patterns)
- Pipeline fingerprint detection
- "Generic Assistant" swap test
- Line count binary check

#### T5 Refiner: `soul-refining`

```
skills/
  soul-pipeline/
    soul-refining/
      SKILL.md
```

**Contents:**
- Gap resolution methodology (how to fix each type of gap)
- Line budget management (fix within ≤20 lines)
- Voice preservation rules (fix problems without losing identity)
- Sanity-check procedures

#### T6 Final Reviewer: `soul-final-review`

```
skills/
  soul-pipeline/
    soul-final-review/
      SKILL.md
```

**Contents:**
- 17-gate hard checklist
- 35-point scoring rubric
- Auto-reject conditions
- Archive procedures
- Retry chain rules (when to send back to T5)

### Why One Skill Per Role?

- **Separation of concerns** — SOUL.md is identity, skills are procedure
- **Maintainability** — Update a procedure without touching the identity
- **Reusability** — The same skill structure works for future pipeline roles
- **Clarity** — Each skill has a single, clear purpose

---

## 5. Configuration: What config.yaml Settings Matter

### Current State

All pipeline profiles have identical `config.yaml` files with:
- `model.default: mimo-v2.5`
- `model.provider: xiaomi`
- All auxiliary models set to `auto`

### What Actually Matters for Pipeline Roles

**Model selection:**
- `model.default` — The main model. Currently `mimo-v2.5` for all profiles.
- For creative roles (Writer, Namer), a more creative model might help.
- For review roles (Reviewer, Final Reviewer), a more analytical model might help.
- For the current setup, all profiles use the same model — this is fine if the model is good enough.

**Auxiliary models:**
- `compression` — Used for context compression. `auto` is fine.
- `curator` — Used for skill maintenance. `auto` is fine.
- `approval` — Used for command approval. `auto` is fine.

**What doesn't matter:**
- Most auxiliary model configs are identical across profiles and don't need customization for pipeline roles.
- The pipeline's quality comes from SOUL.md identity + skills procedures, not from model selection.

### Recommendation

Keep `config.yaml` identical across all pipeline profiles. The model choice is a system-wide decision, not a per-role decision. If you want to experiment with different models for different roles, do it later — it's not the bottleneck.

---

## 6. Proposed Architecture

### Profile Structure for Each Pipeline Role

```
~/.hermes/profiles/<role>/
├── SOUL.md              # Identity (role-specific, ~40-60 lines)
├── profile.yaml         # Short description
├── config.yaml          # Model settings (identical across roles)
├── memories/
│   └── MEMORY.md        # Accumulated pipeline experience
├── skills/
│   └── soul-pipeline/
│       └── soul-<role>/
│           └── SKILL.md # Role-specific procedures
└── (other standard dirs)
```

### SOUL.md Design Principles

1. **Frontmatter:**
   - `name:` matches the profile name (namer, writer, reviewer, refiner, final-reviewer)
   - `description:` pipeline-specific (already done for reviewer/refiner/final-reviewer in profile.yaml)
   - `skills:` list includes the custom soul-pipeline skill + relevant bundled skills
   - `tools:` only what the role needs (e.g., namer doesn't need Write for drafts)

2. **Body (~40-60 lines):**
   - Role declaration: "You are [Name], the [Pipeline Role]"
   - Core identity: What makes this role unique
   - Core protocol: 3-5 high-level steps
   - Technical directives: Role-specific behavioral rules
   - **NOT** step-by-step procedures (those go in skills)

3. **Keep it short:**
   - Pipeline roles are specialists, not generalists
   - 40-60 lines is enough for a clear identity
   - The `references/stage-*.md` files provide detailed instructions per task
   - SOUL.md provides the *lens* through which the agent interprets those instructions

### Example: T3 Reviewer SOUL.md

```yaml
---
name: reviewer
description: "SOUL.md draft reviewer. Scores persona drafts on 7 axes, flags gaps, never rejects."
tools: [Read, Grep, Glob]
model: sonnet
version: "2.0.0"
tags: [soul-pipeline, review, scoring, quality-gate]
skills:
  - soul-reviewing
  - writing-clearly-and-concisely
---
```

```markdown
## Role: The Reviewer

You are the Soul Pipeline's quality analyst. You score persona drafts on 7 axes, flag specific gaps, and never reject. Every draft proceeds to the refiner — your job is to make the problems visible, not to gatekeep.

### Identity

You are precise, fair, and specific. You never say "this is good" or "this is bad" — you score on defined axes and cite exact lines. Your critiques are actionable: each gap note tells the refiner exactly what to fix and why.

### Core Protocol

1. **Read the draft** — Count active lines after H1. Binary check: ≤20 passes, >20 fails.
2. **Score on 7 axes** — Distinctiveness, Functional Safety, Consistency, Metaphor Coherence, Terse Format, Voice Immediacy, Name Quality. Each 1-5.
3. **Flag gaps** — Sign-off framing, recovery line, Never quality, copied patterns, pipeline fingerprints, density overlap, category-label names.
4. **Write the critique** — Scores + gap notes to `critiques/<name>.md`. Never reject.

### Technical Directives

- The "Generic Assistant swap test": replace the persona name with "Generic Assistant." If nothing changes, it's a template.
- Flag sentence-level copying from Reference Personae.
- Flag pipeline fingerprints (patterns appearing in 3+ other personae).
- Each gap note must cite the exact line and explain what's wrong.
```

### Example: T1b Namer SOUL.md

```yaml
---
name: namer
description: "SOUL.md persona namer. Chooses proper names for fictional characters based on archetype, tone, and memorability."
tools: [Read, Write, Grep, Glob, WebFetch, WebSearch]
model: sonnet
version: "2.0.0"
tags: [soul-pipeline, naming, etymology, onomastics]
skills:
  - soul-naming
---
```

```markdown
## Role: The Namer

You are the Soul Pipeline's onomastician. You choose names that carry the archetype's weight in sound alone — names that work before the reader knows anything else about the persona.

### Identity

You are an etymologist and phonetician. Every name must justify itself through its roots, its sound, and its fit with the archetype. You never choose names by vibes alone — every choice has a linguistic argument.

### Core Protocol

1. **Read the seed** — Understand the archetype, domain, metaphor, and tone.
2. **Check the archive** — Ensure no overlap with existing archived personae.
3. **Research etymology** — Find names with OE, Latin, or Greek roots that connect to the archetype's domain.
4. **Score the name** — 25-point scale: domain connection, phonetic fit, distinctiveness, memorability.
5. **Write the name file** — Name + etymology + phoneme analysis + score to `names/<name>.md`.

### Technical Directives

- Never choose 0-hop labels (bare domain words as names).
- Never choose historical figures or category labels.
- The name must work as a proper name, not a title.
- Phoneme analysis: explain what each sound contributes to the name's feel.
```

---

## 7. Migration Path

### Phase 1: Update profile.yaml (Already Done)

The `profile.yaml` for reviewer, refiner, and final-reviewer already have pipeline-specific descriptions. Update writer and namer:

```yaml
# writer/profile.yaml
description: "SOUL.md draft writer. Creates persona drafts from seeds, enforces line limits, invents original voice."
description_auto: false

# namer/profile.yaml
description: "SOUL.md persona namer. Chooses proper names based on archetype, etymology, and phonetics."
description_auto: false
```

### Phase 2: Create Custom Skills

Create `skills/soul-pipeline/soul-<role>/SKILL.md` for each profile. Extract procedures from `references/stage-*.md` into these skills.

### Phase 3: Rewrite SOUL.md

Replace each profile's SOUL.md with a pipeline-specific identity (40-60 lines). Keep the frontmatter updated with the correct skills list.

### Phase 4: Validate

Run the pipeline and check:
- Does the agent's behavior match its role?
- Are the skills being loaded and used?
- Does the memory accumulate role-specific experience?

---

## 8. Key Findings

1. **SOUL.md is identity, skills are procedure.** Don't put step-by-step instructions in SOUL.md — put them in skills. SOUL.md should answer "who is this agent?" not "how does this agent do X?"

2. **The `skills:` frontmatter list references bundled skills by name.** These come from a skills hub (90+ available). Custom skills in the `skills/` directory are always available without frontmatter listing.

3. **config.yaml is boilerplate.** All pipeline profiles have identical configs. The model choice doesn't need per-role customization.

4. **profile.yaml is already partially done.** reviewer/refiner/final-reviewer have pipeline-specific descriptions. writer/namer don't.

5. **The current pipeline profiles are maximally under-specialized.** All 5 have identical SOUL.md files with no pipeline-specific identity.

6. **The fix is straightforward:** Rewrite SOUL.md for each role (40-60 lines of identity), create one custom skill per role (procedures from stage-*.md), update profile.yaml descriptions.

7. **Don't over-specialize.** SOUL.md should be a clear identity, not a procedure manual. The `references/stage-*.md` files already provide detailed per-task instructions. The profile's job is to provide the *lens* — the identity and approach — through which those instructions are interpreted.

8. **Skills should be extracted from stage-*.md, not duplicated.** The stage files are task-specific instructions. The skills should encode the reusable procedures (scoring rubrics, naming methodology, writing rules) that the agent needs regardless of which specific persona it's working on.
