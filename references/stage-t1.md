### Stage T1 — Researcher (Orchestrator)

**The researcher is an ORCHESTRATOR, not an executor.** You create seed files and spawn kanban task chains. You do NOT write drafts, review, refine, or final-review. You do NOT execute any downstream pipeline stage. Your job is: research seeds → create tasks → assign each to the correct profile → complete. That is all.

Input: `archive/` and `drafts/` (if any) — check for existing personae.
Output: `seeds/<seed-label>.md` — a ranked list of archetype + domain + metaphor combinations.

**Before you begin:** Read all existing SOUL.md files in `archive/` and any in `drafts/`. For each, extract: archetype, domain, metaphor, and tone. Write a brief coverage map — what categories are well-represented and which are sparse.

**Research methodology:** Use `web_search` to survey character archetype sources. Good queries include:
- `"character archetypes" fiction tropes`
- `site:tvtropes.org "character archetype"`
- `professional archetypes personality types`
- `literary character types list`

Also check the existing `seeds/SEEDS.md` as a reference for output format. Do not copy its content — it is a prior research artifact, not a template — but study its structure.

**What to look for:**
- A clear, instantly graspable metaphor for tool use
- A domain with enough texture to sustain voice across 50+ messages
- A contradiction or tension the model can improvise within

**Exclusions:** Do not propose seeds that would:
- Refuse to use tools or be genuinely hostile
- Break into cryptic oracle or riddle-only mode
- Be so niche that the model lacks cultural reference points

**Each seed file must contain:**
- **Archetype** (e.g., "surfer", "bartender", "archmage")
- **Domain** (physical, professional, or conceptual home)
- **Metaphor** (how they relate to tool use — e.g., "reading the waves", "mixing a drink", "casting a spell")
- **Functional Risk** (what can go wrong — e.g., "too casual for high-stakes contexts", "may suggest unethical shortcuts")

**Novelty check:** For each candidate, list the three closest archived personae by archetype, domain, and metaphor. Confirm your candidate differs in at least two dimensions from every one. If any archived persona matches in two or more dimensions, the candidate is too close — discard it and keep searching.

**Category coverage:** The repository tracks four categories: Profession, Fiction Trope, Bureaucratic, Absurdist. Aim to cover under-represented categories. Do not produce five seeds all from the same category.

**Minimum output:** At least 5 viable seeds. If your first research pass yields fewer than 5 novel candidates, perform a second pass with broader search terms before writing output files.

**Ranking:** Sort by "viability" — a combination of functional safety (low risk), distinctiveness from existing archive, and how cleanly the metaphor maps to tool use.

**Orchestration:** After writing the seed files, create a complete kanban task chain for each viable seed. Use `kanban_create` with `workspace_kind: "dir"` and `workspace_path: "/home/kimbo/.hermes/projects/soul-repository"`. Create T1b → T2 → T3 → T5 → T6 in order, linking each stage as the parent of the next. The task body for each stage must contain the relevant stage instructions from this file and the seed data the next stage needs.

**CRITICAL — Stage-to-profile mapping.** Every task MUST be assigned to the correct profile. Getting this wrong means one model reviews its own work, destroying the quality gate. Use this exact mapping:

| Stage | Title pattern | `assignee` value |
|-------|---------------|------------------|
| T1b | `T1b: Name <Seed>` | `namer` |
| T2 | `T2: Write <Name> SOUL.md` | `writer` |
| T3 | `T3: Review <Name> SOUL.md` | `reviewer` |
| T5 | `T5: Refine <Name> SOUL.md` | `refiner` |
| T6 | `T6: Final-review <Name> SOUL.md` | `final-reviewer` |

Do NOT assign all stages to one profile. Do NOT use the creating worker's own profile. Each stage has a dedicated profile — that is the entire point of the pipeline.

