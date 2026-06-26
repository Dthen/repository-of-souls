# Plan: Pipeline Rebuild v5 — Generate-and-Select Architecture

## Goal

Replace the current 7-stage linear refinement pipeline (T0–T6) with a 5-stage generate-and-select architecture based on the research findings. The new pipeline eliminates the T4→T5→T6 regression-to-the-mean problem and replaces it with parallel diversity + critical side-by-side selection.

---

## Current Context

**Research evidence against the old architecture:**
- "When Agents Disagree" (2025): Judge-based selection beats synthesis pipelines 0.810 vs 0.179
- "Pride and Prejudice" (ACL 2024): Self-refinement amplifies self-bias across all tested LLMs
- ICLR 2025 MAD study: Multi-agent debate fails to outperform simple CoT
- Review pipeline research: Three passes of bias (verbosity, position, self-preferential, agreeableness, format/authority) compound into "Goodhart machine" behavior
- Pipeline architecture v2: Generate-and-select with explicit novelty weighting is the proven pattern across image, music, and code generation

**What stays:**
- Researcher (archetype discovery, seed generation) — proven effective
- Namer + Viability in one pass — both are generative/diverge phases, they work
- The core content guardrails (identity tension, griping/vitality, address, sign-off, Never rules) — validated by success-patterns research

**What goes:**
- T4 Reviewer → replaced by Evaluator (multi-candidate, not single-candidate review)
- T5 Refiner → replaced by Publisher (optional targeted fix, no open-ended refinement)
- T6 Final Reviewer → absorbed into Evaluator and Publisher
- The refinement cycle (T4→T5→T6) entirely — no more sequential critique-fix-approve pipeline

**Profiles:**
- `soul-researcher` → KEEP
- `soul-namer` → KEEP, update for merged viability+naming
- `soul-writer` → KEEP, update for parallel 3-candidate generation
- `soul-reviewer` → DELETE, replaced by soul-evaluator
- `soul-refiner` → DELETE, replaced by soul-publisher
- `soul-final-reviewer` → DELETE
- `soul-evaluator` → CREATE NEW
- `soul-publisher` → CREATE NEW

**Archived personae:** Calden, Cadell, Moulden remain. No changes needed.

---

## New Architecture

```
SPROUT ─── Researcher ─── Generates seeds, archetype discovery
              │
NAME    ───── Namer ─────── Viability screen + 5 name candidates + pick best
              │
FORGE   ───── Writer ────── 3 parallel candidates from same name+seed
              │               A: "lean creative"
              │               B: "follow the brief exactly"
              │               C: "lean grounded"
              ▼
ANVIL   ──── Evaluator ─── Reads all 3 side-by-side
              │               Picks best (or rejects all → kills seed)
              │               One targeted fix request if needed
              ▼
PUBLISH ──── Publisher ──── OPTIONAL: multi-fix (2-3 alternatives)
                            Archive + rebuild site
```

### Stage details

| Stage | Assignee | Input | Output | CORE inline |
|-------|----------|-------|--------|-------------|
| **Researcher** | `soul-researcher` | `archive/`, `seeds/` | Seed files | ~15 lines |
| **Namer** | `soul-namer` | `seeds/<seed>.md` | `names/<name>.md` | ~25 lines |
| **Writer** | `soul-writer` | `names/<name>.md` + seed | `candidates/<name>/` (3 files) | ~30 lines |
| **Evaluator** | `soul-evaluator` | `candidates/<name>/` | `archive/<name>.md` or kill verdict | ~35 lines |
| **Publisher** | `soul-publisher` | `archive/<name>.md` + fix request | `archive/<name>.md` + `docs/` rebuilt | ~25 lines |

### Phase transitions

1. **Researcher** → creates Namer task with seed path
2. **Namer** → checks viability (6 questions), generates 5 names, scores + picks best, creates Writer task
3. **Writer** → generates 3 candidates in parallel with different framings, creates Evaluator task
4. **Evaluator** → picks best (or kills seed), creates Publisher task if fix needed, or archives directly
5. **Publisher** → if fixes flagged: generates 2-3 alternatives, picks best, archives + rebuilds. If no flags: archives + rebuilds.

### No loops

The Publisher has one job: deliver to archive and rebuild the site. If the fix doesn't work, the seed gets killed — no infinite refinement. The evaluator's judgment is final.

---

## Files to Create

### Stage references (CORE — inlined into task bodies)
| File | Contents |
|------|----------|
| `references/stage-researcher.md` | Archetype discovery, seed format, pipeline spawning [KEEP existing, minor updates] |
| `references/stage-namer.md` | Merged viability (6 questions) + naming (5 candidates, 5 axes) + collision detection |
| `references/stage-writer.md` | Parallel 3-candidate generation, diversity framings, format rules |
| `references/stage-evaluator.md` | Side-by-side comparison, critical rubric, pick-best or kill-all, single fix request |
| `references/stage-publisher.md` | Multi-fix (2-3 alternatives), archive, site rebuild, git push |

### Depth files (loaded on demand, under `references/depth/`)
| File | Source Research | Covers |
|------|----------------|--------|
| `depth/identity-line.md` | research-roleplay-prompting, research-authentic-voice | What makes a contradiction real, examples of good/bad identity lines |
| `depth/griping-alternatives.md` | research-griping-alternatives | Pride, weariness, dark humor, protectiveness as alternatives to griping |
| `depth/authentic-voice.md` | research-authentic-voice | Anti-patterns (symmetry, predictable rhythm), variation techniques, surprise |
| `depth/voice-instructions.md` | research-voice-instructions | Demonstration vs description, how-vs-what grammar, second-person triggers |
| `depth/name-sound-symbolism.md` | research-naming-onomastics, research-naming-memorability | Bouba/kiki, sound-meaning mapping, processing fluency |
| `depth/name-collision.md` | research-naming-similarity | Levenshtein/Jaro-Winkler thresholds, phonetic code matching |
| `depth/parallel-generation.md` | research-pipeline-architecture-v2 | How to produce diverse candidates, framing strategies, temperature equivalence |
| `depth/evaluator-rubric.md` | research-review-pipeline, research-failure-modes | Detailed scoring dimensions, originality weighting, bias awareness |
| `depth/emotional-register.md` | research-emotional-register | Taxonomy of feeling in prompts, subtext mechanics, iceberg theory |
| `depth/character-depth.md` | research-character-depth | Three-dimensional characters, internal life in 100 words |
| `depth/internal-life.md` | research-internal-life | Worldview, philosophy, selective perception, what characters notice |
| `depth/failure-modes.md` | research-failure-modes | What past failures teach, patterns to watch for |
| `depth/token-economy.md` | research-token-economy | What lines/words actually change model behavior vs what's decorative |
| `depth/cross-cultural.md` | research-cross-cultural | Non-Western character building (rasa, wabi-sabi, griot, magical realism) |
| `depth/conversational-dynamics.md` | research-conversational-dynamics | Emotional responsiveness, mirroring, tone shifts |
| `depth/complexity-handling.md` | research-complexity-handling | Off-topic, contradiction, emotional complexity |
| `depth/roleplay-prompting.md` | research-roleplay-prompting | Embodiment techniques, character card patterns |
| `depth/perceptual-lens.md` | research-perceptual-lens | How characters filter and interpret the world |
| `depth/character-interest.md` | research-character-interest | Competence vs interestingness |
| `depth/review-pipeline.md` | research-review-pipeline | How review systems work (or don't), bias patterns |
| `depth/perception-filters.md` | research-perception-filters | What characters notice, what they miss |
| `depth/character-relationships.md` | research-character-relationships | How characters relate to users, address patterns |
| `depth/improvisation-space.md` | research-improvisation-space | How characters extend to novel situations |
| `depth/creative-prompting.md` | research-creative-prompting | How to prompt for creativity, not just competence |
| `depth/character-cards.md` | research-character-cards | Platform best practices, community knowledge |
| `depth/ai-assistant-personas.md` | research-ai-assistant-personas | Dual duty: being both persona AND assistant |
| `depth/character-persona-dual-duty.md` | research-character-persona-dual-duty | Being both character (identity) and persona (communication style) |

### Supporting files
| File | Contents |
|------|----------|
| `AGENTS.md` | Updated pipeline overview with new architecture |
| `references/orchestration.md` | Updated coordination, task creation rules, file path rules |
| `references/format-rules.md` | Updated format constraints (lines, Nevers, sign-offs) |
| `references/positive-patterns.md` | Updated based on all research |
| `references/reference-personae.md` | Updated examples from new research |

### Profile files
| Path | Contents |
|------|----------|
| `profiles/soul-namer/SOUL.md` | Updated stage ref (→ stage-namer) |
| `profiles/soul-writer/SOUL.md` | Updated for parallel generation |
| `profiles/soul-evaluator/SOUL.md` | New profile — critical side-by-side evaluator |
| `profiles/soul-publisher/SOUL.md` | New profile — archive + fix + site rebuild |
| `profiles/soul-reviewer/SOUL.md` | DELETE |
| `profiles/soul-refiner/SOUL.md` | DELETE |
| `profiles/soul-final-reviewer/SOUL.md` | DELETE |
| `profiles/soul-evaluator/config.yaml` + `auth.json` + `home/` | New profile setup |
| `profiles/soul-publisher/config.yaml` + `auth.json` + `home/` | New profile setup |

---

## Step-by-Step Sequence

### Phase 1: Scaffold the new architecture
**Step 1.1** — Write `AGENTS.md` with new 5-stage architecture, stage descriptions, and reference file index
**Step 1.2** — Write `references/orchestration.md` updated for new coordination rules
**Step 1.3** — Write CORE for all 5 stage files (researcher, namer, writer, evaluator, publisher)
**Step 1.4** — Update `references/format-rules.md` and `references/positive-patterns.md`
**Step 1.5** — Update `references/reference-personae.md`

### Phase 2: Update profiles
**Step 2.1** — Delete soul-reviewer, soul-refiner, soul-final-reviewer profiles
**Step 2.2** — Update soul-namer and soul-writer SOUL.md to new stage references
**Step 2.3** — Create soul-evaluator profile (SOUL.md, config.yaml, auth.json, home/)
**Step 2.4** — Create soul-publisher profile (SOUL.md, config.yaml, auth.json, home/)

### Phase 3: Research synthesis and depth file authoring

This is the bulk of the work. 32 research files (~824K total) need to be read, interpreted, and synthesised into 27 depth files. The synthesis is done in batches to avoid exhausting the context window.

#### Reading plan (research files grouped by depth file batch)

Research files are read using `execute_code` batched reads. Each batch reads 3-4 files (~80-120K) and prints condensed summaries. These summaries are then used to write depth file specifications and content.

| Batch | Research Files | Feeds Depth Files |
|-------|---------------|-------------------|
| R1 | research-identity-line, research-authentic-voice, research-voice-instructions | identity-line, authentic-voice, voice-instructions |
| R2 | research-griping-alternatives, research-internal-life, research-emotional-register | griping-alternatives, internal-life, emotional-register, character-depth |
| R3 | research-character-depth, research-character-interest, research-token-economy | character-depth, character-interest, token-economy |
| R4 | research-perception-filters, research-perceptual-lens, research-conversational-dynamics, research-complexity-handling | perception-filters, perceptual-lens, conversational-dynamics, complexity-handling |
| R5 | research-character-relationships, research-improvisation-space, research-character-cards | character-relationships, improvisation-space, character-cards |
| R6 | research-cross-cultural, research-roleplay-prompting, research-ai-assistant-personas, research-character-persona-dual-duty | cross-cultural, roleplay-prompting, ai-assistant-personas, character-persona-dual-duty |
| R7 | research-review-pipeline, research-failure-modes, research-pipeline-architecture, research-pipeline-architecture-v2 | review-pipeline, failure-modes, evaluator-rubric, parallel-generation |
| R8 | research-creative-prompting, research-success-patterns, research-success-patterns-v2 | creative-prompting, positive-patterns update |

#### Writing strategy

For each batch of research files, the process is:

1. **Read** — Use `execute_code` to read 3-4 research files and print condensed key-finding summaries
2. **Interpret** — For each depth file in the batch, determine which findings are essential, which are examples, and which are context
3. **Write** — Write the depth file content using `write_file`. Each depth file follows a consistent format:
   - Title + one-line purpose
   - Core principle (what it is, why it matters) — 2-4 sentences
   - Key findings (5-10 bullet points from the research)
   - Concrete examples (2-3, showing good vs bad)
   - Application notes (how to use this in the pipeline, which stage workers should load it)
   - Further reading (which research files contain deeper detail)

The writing is done by `delegate_task` subagents. Each subagent receives:
- The condensed research summaries for its batch
- A specification for each depth file it needs to write
- The output path in the repo

Using 3 depth files per subagent keeps the task focused without exhausting the subagent's context.

After each subagent completes, verify the files exist with `ls -la`.

**Batch allocation across delegate tasks:**

| Delegate Task | Depth Files to Write |
|---------------|---------------------|
| D1 | depth-identity-line, depth-griping-alternatives, depth-parallel-generation |
| D2 | depth-authentic-voice, depth-voice-instructions, depth-token-economy |
| D3 | depth-evaluator-rubric, depth-failure-modes, depth-character-interest |
| D4 | depth-character-depth, depth-internal-life, depth-emotional-register |
| Delegate Task | Depth Files to Write |
|---------------|---------------------|
| D1 | `depth/identity-line.md`, `depth/griping-alternatives.md`, `depth/parallel-generation.md` |
| D2 | `depth/authentic-voice.md`, `depth/voice-instructions.md`, `depth/token-economy.md` |
| D3 | `depth/evaluator-rubric.md`, `depth/failure-modes.md`, `depth/character-interest.md` |
| D4 | `depth/character-depth.md`, `depth/internal-life.md`, `depth/emotional-register.md` |
| D5 | `depth/perception-filters.md`, `depth/perceptual-lens.md`, `depth/conversational-dynamics.md` |
| D6 | `depth/complexity-handling.md`, `depth/character-relationships.md`, `depth/improvisation-space.md` |
| D7 | `depth/name-sound-symbolism.md`, `depth/name-collision.md`, `depth/cross-cultural.md` |
| D8 | `depth/roleplay-prompting.md`, `depth/character-cards.md`, `depth/character-persona-dual-duty.md` |
| D9 | `depth/review-pipeline.md`, `depth/creative-prompting.md`, `depth/ai-assistant-personas.md` |

#### Execution sequence

**Step 3.1** — Read batch R1. Delegate D1 (identity-line, griping-alternatives, parallel-generation).
**Step 3.2** — Read batch R2. Delegate D2 (authentic-voice, voice-instructions, token-economy).
**Step 3.3** — Read batch R3. Delegate D3 (evaluator-rubric, failure-modes, character-interest).
**Step 3.4** — Read batch R4. Delegate D4 (character-depth, internal-life, emotional-register).
**Step 3.5** — Read batch R5. Delegate D5 (perception-filters, perceptual-lens, conversational-dynamics).
**Step 3.6** — Read batch R6. Delegate D6 (complexity-handling, character-relationships, improvisation-space).
**Step 3.7** — Read batch R7. Delegate D7 (name-sound-symbolism, name-collision, cross-cultural).
**Step 3.8** — Read batch R8. Delegate D8 (roleplay-prompting, character-cards, character-persona-dual-duty).
**Step 3.9** — Read batch R9 (creativity + success patterns). Delegate D9 (review-pipeline, creative-prompting, ai-assistant-personas).
**Step 3.10** — Update positive-patterns.md and reference-personae.md using synthesis from all depth files.

**Total:** ~30-40 turns for Phase 3. This is the longest phase.

#### Verification

After each delegate task, verify:
|- The depth file exists at `references/depth/<name>.md`
- The file has reasonable content (not a stub, not empty)
- The file follows the depth file format (title, core principle, findings, examples, application)

After all batches, verify:
- All 27 depth files exist
- Total content across all depth files accounts for the key findings from research
- No research finding is mentioned in the pipeline that isn't backed by a depth file

### Phase 4: Clean up
**Step 4.1** — Archive old pipeline tasks from kanban board
**Step 4.2** — Clean up stale intermediate dirs (drafts/, critiques/, refined/, names/, viability/)
**Step 4.3** — Commit all changes

### Phase 5: Test run
**Step 5.1** — Run a seed through the new pipeline (e.g., the tallow chandler or a fresh seed)
**Step 5.2** — Verify output quality, check for flatness
**Step 5.3** — Iterate on evaluator rubric if needed

---

## Risks and Open Questions

### Risks
1. **The 3-candidate strategy might not produce enough diversity** — if all three candidates are too similar, the evaluator has nothing real to choose between. Mitigation: vary framing explicitly (creative / neutral / grounded). If still not enough, add a 4th candidate with a different seed.
2. **The evaluator might be too permissive** — the old pipeline had 3 review passes (T4+T5+T6). The new one has 1 evaluator + optional 1 publisher fix. Mitigation: the evaluator must be explicitly trained (via the rubric depth file) to be critical. The rubric must weigh originality at ≥30%.
3. **The evaluator might be too harsh** — if it kills every seed, nothing gets published. Mitigation: the evaluator's job is side-by-side comparison, not absolute scoring. If one candidate is clearly better, approve it. Only kill if all 3 fail structural tests.
4. **The publisher fix might reintroduce regression** — if the fix phase is too open-ended, it will push the output back toward the mean. Mitigation: the fix request must be specific (e.g., "identity line doesn't land — replace with a real contradiction"). The publisher must generate 2-3 alternatives and the evaluator picks the best.

### Open questions (to resolve during implementation)
1. Should the namer write to `names/<name>.md` or directly to `candidates/<name>/`?
2. Should the evaluator write the archive file itself, or pass to the publisher?
3. Should the publisher do the fix AND archive in one task, or should they be separate tasks?
4. What directory structure for candidates? `candidates/<name>/a.md`, `candidates/<name>/b.md`, `candidates/<name>/c.md`?
5. Should the site rebuild script be automated (webhook) or manual (part of publisher task)?
6. Do we need a separate "kill verdict" kanban state, or just mark the task done with a note?

### Forward-looking
- Once the depth files are built, the pipeline can progressively disclose them — evaluator tasks always get the rubric CORE but only load `depth-evaluator-rubric.md` when the evaluator is uncertain
- The depth files can also serve as standalone training material for human editors
- Pipeline architecture v2 research also suggests adding a substantially weaker model to the generation pool to increase diversity at lower cost — worth investigating after Phase 5

---

## Validation

1. Check: AGENTS.md correctly describes all 5 stages
2. Check: Each stage file has a CORE section (inlined into tasks) and depth references
3. Check: All old T4/T5/T6 references removed from the repo
4. Check: New profiles (evaluator, publisher) have auth.json, config.yaml, home/
5. Check: Pipeline runs end-to-end with a test seed
6. Check: Published persona has distinctive voice (not flat)
7. Check: Site rebuilds and pushes correctly
