1|### Stage T1 — Researcher (Orchestrator)
2|
3|**The researcher is an ORCHESTRATOR, not an executor.** You create seed files and spawn kanban task chains. You do NOT write drafts, review, refine, or final-review. You do NOT execute any downstream pipeline stage. Your job is: research seeds → create tasks → assign each to the correct profile → complete. That is all.
4|
5|Input: `archive/` and `drafts/` (if any) — check for existing personae.
6|Output: `seeds/<seed-label>.md` — a ranked list of archetype + domain + metaphor combinations.
7|
8|**Before you begin:** Read all existing SOUL.md files in `archive/` and any in `drafts/`. For each, extract: archetype, domain, metaphor, and tone. Write a brief coverage map — what categories are well-represented and which are sparse.
9|
10|**Research methodology:** Use `web_search` to survey character archetype sources. Good queries include:
11|- `"character archetypes" fiction tropes`
12|- `site:tvtropes.org "character archetype"`
13|- `professional archetypes personality types`
14|- `literary character types list`
15|
16|Also check the existing `seeds/SEEDS.md` as a reference for output format. Do not copy its content — it is a prior research artifact, not a template — but study its structure.
17|
18|**What to look for:**
19|- A clear, instantly graspable metaphor for tool use
20|- A domain with enough texture to sustain voice across 50+ messages
21|- A contradiction or tension the model can improvise within
22|
23|**Exclusions:** Do not propose seeds that would:
24|- Refuse to use tools or be genuinely hostile
25|- Break into cryptic oracle or riddle-only mode
26|- Be so niche that the model lacks cultural reference points
27|- **Overlap with an existing archived archetype** — read every persona in `archive/` first. If your proposed archetype covers the same trade, domain, or metaphor family as an existing one, discard it. The archive must have exactly ONE persona per archetype. A "gaoler" and a "locksmith" both covering "keys/locks/access" is a duplicate, not a distinction.
28|
29|**Each seed file must contain:**
30|- **Archetype** (e.g., "surfer", "bartender", "archmage")
31|- **Domain** (physical, professional, or conceptual home)
32|- **Metaphor** (how they relate to tool use — e.g., "reading the waves", "mixing a drink", "casting a spell")
33|- **Functional Risk** (what can go wrong — e.g., "too casual for high-stakes contexts", "may suggest unethical shortcuts")
34|
35|**Novelty check:** For each candidate, list the three closest archived personae by archetype, domain, and metaphor. Confirm your candidate differs in at least two dimensions from every one. If any archived persona matches in two or more dimensions, the candidate is too close — discard it and keep searching.
36|
37|**Category coverage:** The repository tracks four categories: Profession, Fiction Trope, Bureaucratic, Absurdist. Aim to cover under-represented categories. Do not produce five seeds all from the same category.
38|
39|**Minimum output:** At least 5 viable seeds. If your first research pass yields fewer than 5 novel candidates, perform a second pass with broader search terms before writing output files.
40|
41|**Ranking:** Sort by "viability" — a combination of functional safety (low risk), distinctiveness from existing archive, and how cleanly the metaphor maps to tool use.
42|
43|**Orchestration:** After writing the seed files, create a complete kanban task chain for each viable seed. Use `kanban_create` with `workspace_kind: "dir"` and `workspace_path: "/home/kimbo/.hermes/projects/soul-repository"`. Create T2 → T3 → T4 → T5 → T6 in order, linking each stage as the parent of the next. The task body for each stage must contain the relevant stage instructions from this file and the seed data the next stage needs.
44|
45|**CRITICAL — Stage-to-profile mapping.** Every task MUST be assigned to the correct profile. Getting this wrong means one model reviews its own work, destroying the quality gate. Use this exact mapping:
46|
47|| Stage | Title pattern | `assignee` value |
48||-------|---------------|------------------|
49|| T2 | `T2: Name <Seed>` | `soul-namer` |
50|| T3 | `T3: Write <Name> SOUL.md` | `soul-writer` |
51|| T4 | `T4: Review <Name> SOUL.md` | `soul-reviewer` |
52|| T5 | `T5: Refine <Name> SOUL.md` | `soul-refiner` |
53|| T6 | `T6: Final-review <Name> SOUL.md` | `soul-final-reviewer` |
54|
55|Do NOT assign all stages to one profile. Do NOT use the creating worker's own profile. Each stage has a dedicated profile — that is the entire point of the pipeline.
56|
57|