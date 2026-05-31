1|# Research: Hermes Profile Architecture for Soul Repository Pipeline
2|
3|**Date:** 2026-05-31
4|**Purpose:** Understand how Hermes profiles work and propose custom profile designs for each pipeline role.
5|
6|---
7|
8|## 1. How Hermes Profiles Work
9|
10|### Anatomy of a Profile
11|
12|A Hermes profile lives at `~/.hermes/profiles/<name>/` and contains:
13|
14|| Component | Path | Purpose |
15||-----------|------|---------|
16|| **SOUL.md** | `<profile>/SOUL.md` | Identity, role definition, frontmatter metadata |
17|| **profile.yaml** | `<profile>/profile.yaml` | Short description for profile listing |
18|| **config.yaml** | `<profile>/config.yaml` | Model, provider, auxiliary model settings |
19|| **skills/** | `<profile>/skills/` | Local skills (SKILL.md files in category dirs) |
20|| **memories/** | `<profile>/memories/MEMORY.md` | Persistent cross-session memory |
21|| **state.db** | `<profile>/state.db` | Session state database |
22|| **logs/** | `<profile>/logs/` | Agent and error logs |
23|
24|### SOUL.md Structure
25|
26|SOUL.md has two parts:
27|
28|**Frontmatter (YAML):**
29|```yaml
30|---
31|name: <profile-name>
32|description: <one-line description>
33|tools: [Read, Write, Edit, Bash, Grep, Glob, WebFetch, WebSearch]
34|model: sonnet
35|version: "1.1.0"
36|author: Agent Zero
37|tags: [tag1, tag2]
38|priority: normal
39|max_context_tokens: 200000
40|skills:
41|  - skill-name-1
42|  - skill-name-2
43|---
44|```
45|
46|**Body (Markdown):** The persona definition — role, capabilities, protocols, directives.
47|
48|### profile.yaml
49|
50|Minimal — just a short description for `hermes profile list`:
51|```yaml
52|description: "Short description of what this profile does."
53|description_auto: false
54|```
55|
56|### config.yaml
57|
58|Controls model selection and auxiliary model settings:
59|```yaml
60|model:
61|  default: mimo-v2.5
62|  provider: xiaomi
63|auxiliary:
64|  approval: { provider: auto, model: auto, ... }
65|  compression: { provider: auto, model: auto, ... }
66|  curator: { provider: auto, model: auto, ... }
67|  # ... more auxiliary model configs
68|```
69|
70|The `config.yaml` is largely boilerplate — all pipeline profiles have identical configs with `mimo-v2.5` as the default model.
71|
72|---
73|
74|## 2. SOUL.md vs Skills: What Goes Where
75|
76|### SOUL.md = Creative Identity + Role Definition
77|
78|SOUL.md answers: **"Who is this agent?"**
79|
80|Contains:
81|- **Role declaration** — "You are [Name], the [Role]"
82|- **Core protocol** — The agent's high-level workflow (3-5 steps)
83|- **Technical directives** — Domain-specific behavioral rules
84|- **Capabilities** — What the agent excels at
85|- **Identity markers** — Tone, voice, approach
86|
87|Example from `analyst`:
88|```
89|## Role: The Analyst
90|Specialist in mathematical logic, data processing, and analytical auditing.
91|You are the 'Zero-Error' agent. You never guess math.
92|
93|### Core Protocol
94|1. Analyze Logic
95|2. Execute Python (mandate)
96|3. Audit & Validate
97|4. Handoff
98|```
99|
100|### Skills = Executable Procedures
101|
102|Skills answer: **"How does this agent do specific tasks?"**
103|
104|A skill is a `SKILL.md` file in a category directory:
105|```
106|skills/
107|  software-development/
108|    systematic-debugging/
109|      SKILL.md          # 4-phase root cause debugging procedure
110|    test-driven-development/
111|      SKILL.md
112|  research/
113|    arxiv/
114|      SKILL.md
115|```
116|
117|Skills contain:
118|- **Step-by-step procedures** — "Phase 1: Understand. Phase 2: Reproduce..."
119|- **Templates** — Output formats, checklists
120|- **Reference material** — Examples, patterns, anti-patterns
121|- **Decision frameworks** — When to use, when not to use
122|
123|### How They Work Together
124|
125|1. **SOUL.md frontmatter `skills:` list** — References bundled skills by name (from `.bundled_manifest`). These are loaded into the agent's context at session start.
126|2. **SOUL.md body** — Defines the agent's identity and high-level approach. This shapes *how* the agent thinks.
127|3. **Skills directory** — Contains local/custom skills. These define *what* the agent knows how to do.
128|4. **Bundled skills** — Come from a skills hub (90+ skills in the `.bundled_manifest`). Referenced by name in frontmatter, loaded on demand.
129|
130|**Key insight:** The `skills:` frontmatter list is a *preference list* — it tells Hermes which bundled skills to prioritize loading. The local `skills/` directory contains skills that are always available to the profile.
131|
132|### Current Pipeline Problem
133|
134|All 5 pipeline profiles have identical SOUL.md files:
135|- Same name (`writer`), same description, same skills list
136|- Same body — "The Writer" with generic writing directives
137|- Same bundled skills — `copy-editing`, `humanizer`, `content-research-writer`, etc.
138|- None of these skills are pipeline-specific
139|
140|The pipeline-specific instructions live in `references/stage-*.md` files in the soul-repository project, NOT in the profiles themselves. The profiles are generic writing assistants that happen to receive pipeline tasks via kanban.
141|
142|---
143|
144|## 3. Profile Specialization
145|
146|### How Much Specialization Is Too Much?
147|
148|**The spectrum:**
149|
150|```
151|Generic ←————————————————————————————→ Hyper-specific
152|"Writing assistant"   "SOUL.md reviewer"   "T3 reviewer for
153|                                           persona scoring on
154|                                           7 axes with gap
155|                                           flagging"
156|```
157|
158|**The sweet spot:** Each profile should be specialized enough that its SOUL.md makes it *immediately clear* what this agent does and how it thinks, but not so specific that it can't adapt to variations.
159|
160|**Evidence from existing profiles:**
161|
162|| Profile | Specialization Level | Assessment |
163||---------|---------------------|------------|
164|| `developer` | High (200+ lines, detailed protocols) | Good — clear role, specific capabilities |
165|| `analyst` | Medium (37 lines, focused) | Good — concise, clear identity |
166|| `advocatus-diaboli` | High (164 lines, detailed methodology) | Excellent — unique identity, clear process |
167|| Pipeline profiles | Zero (all identical) | Broken — no specialization at all |
168|
169|### The Over-Specialization Trap
170|
171|**Signs of over-specialization:**
172|- SOUL.md becomes a procedure manual instead of an identity
173|- The agent can't handle edge cases outside its narrow spec
174|- Instructions become so specific they conflict with each other
175|- The agent loses creative flexibility
176|
177|**How to avoid it:**
178|- SOUL.md defines WHO (identity, voice, approach) — not HOW (step-by-step procedures)
179|- Put procedures in skills, not in SOUL.md
180|- Keep SOUL.md under 60 lines for pipeline roles (they're focused, not generalists)
181|- Let the agent's identity guide behavior, not exhaustive rules
182|
183|### The Under-Specialization Problem (Current State)
184|
185|**Current pipeline profiles are maximally under-specialized:**
186|- All 5 have the same SOUL.md body
187|- All 5 have the same skills list
188|- All 5 have the same description
189|- The `profile.yaml` for reviewer/refiner/final-reviewer already has pipeline-specific descriptions, but the SOUL.md doesn't match
190|
191|**Impact:**
192|- The agent has no identity specific to its pipeline role
193|- It relies entirely on task body instructions (from `references/stage-*.md`)
194|- It can't develop intuitions about its role over time
195|- Memory entries are role-specific but the agent's "personality" isn't
196|
197|---
198|
199|## 4. Skills Design for Pipeline Roles
200|
201|### What Should Custom Skills Look Like?
202|
203|Each pipeline role should have **one custom skill** that encodes its specific procedures. This keeps SOUL.md as identity and skills as procedure.
204|
205|### Proposed Skills
206|
207|#### T2 Namer: `soul-naming`
208|
209|```
210|skills/
211|  soul-pipeline/
212|    soul-naming/
213|      SKILL.md
214|```
215|
216|**Contents:**
217|- Etymology methodology (how to derive names from OE/Latin/Greek roots)
218|- Rejection rules (0-hop labels, historical figures, category names)
219|- Novelty check procedure (compare against archive)
220|- Scoring rubric (25-point scale)
221|- Phoneme-to-meaning mapping technique
222|
223|#### T3 Writer: `soul-writing`
224|
225|```
226|skills/
227|  soul-pipeline/
228|    soul-writing/
229|      SKILL.md
230|```
231|
232|**Contents:**
233|- Line count enforcement (≤20 active lines)
234|- Anti-copy rules (no reference persona patterns)
235|- First-line rule (identity before metaphor)
236|- Never quality standards (cultural trope-rejections, not generic)
237|- Sign-off framing rules (sayable phrases, not rituals)
238|
239|#### T4 Reviewer: `soul-reviewing`
240|
241|```
242|skills/
243|  soul-pipeline/
244|    soul-reviewing/
245|      SKILL.md
246|```
247|
248|**Contents:**
249|- 7-axis scoring rubric (Distinctiveness, Functional Safety, Consistency, Metaphor Coherence, Terse Format, Voice Immediacy, Name Quality)
250|- Gap flagging procedures (sign-off, recovery, Never quality, copied patterns)
251|- Pipeline fingerprint detection
252|- "Generic Assistant" swap test
253|- Line count binary check
254|
255|#### T5 Refiner: `soul-refining`
256|
257|```
258|skills/
259|  soul-pipeline/
260|    soul-refining/
261|      SKILL.md
262|```
263|
264|**Contents:**
265|- Gap resolution methodology (how to fix each type of gap)
266|- Line budget management (fix within ≤20 lines)
267|- Voice preservation rules (fix problems without losing identity)
268|- Sanity-check procedures
269|
270|#### T6 Final Reviewer: `soul-final-review`
271|
272|```
273|skills/
274|  soul-pipeline/
275|    soul-final-review/
276|      SKILL.md
277|```
278|
279|**Contents:**
280|- 17-gate hard checklist
281|- 35-point scoring rubric
282|- Auto-reject conditions
283|- Archive procedures
284|- Retry chain rules (when to send back to T5)
285|
286|### Why One Skill Per Role?
287|
288|- **Separation of concerns** — SOUL.md is identity, skills are procedure
289|- **Maintainability** — Update a procedure without touching the identity
290|- **Reusability** — The same skill structure works for future pipeline roles
291|- **Clarity** — Each skill has a single, clear purpose
292|
293|---
294|
295|## 5. Configuration: What config.yaml Settings Matter
296|
297|### Current State
298|
299|All pipeline profiles have identical `config.yaml` files with:
300|- `model.default: mimo-v2.5`
301|- `model.provider: xiaomi`
302|- All auxiliary models set to `auto`
303|
304|### What Actually Matters for Pipeline Roles
305|
306|**Model selection:**
307|- `model.default` — The main model. Currently `mimo-v2.5` for all profiles.
308|- For creative roles (Writer, Namer), a more creative model might help.
309|- For review roles (Reviewer, Final Reviewer), a more analytical model might help.
310|- For the current setup, all profiles use the same model — this is fine if the model is good enough.
311|
312|**Auxiliary models:**
313|- `compression` — Used for context compression. `auto` is fine.
314|- `curator` — Used for skill maintenance. `auto` is fine.
315|- `approval` — Used for command approval. `auto` is fine.
316|
317|**What doesn't matter:**
318|- Most auxiliary model configs are identical across profiles and don't need customization for pipeline roles.
319|- The pipeline's quality comes from SOUL.md identity + skills procedures, not from model selection.
320|
321|### Recommendation
322|
323|Keep `config.yaml` identical across all pipeline profiles. The model choice is a system-wide decision, not a per-role decision. If you want to experiment with different models for different roles, do it later — it's not the bottleneck.
324|
325|---
326|
327|## 6. Proposed Architecture
328|
329|### Profile Structure for Each Pipeline Role
330|
331|```
332|~/.hermes/profiles/<role>/
333|├── SOUL.md              # Identity (role-specific, ~40-60 lines)
334|├── profile.yaml         # Short description
335|├── config.yaml          # Model settings (identical across roles)
336|├── memories/
337|│   └── MEMORY.md        # Accumulated pipeline experience
338|├── skills/
339|│   └── soul-pipeline/
340|│       └── soul-<role>/
341|│           └── SKILL.md # Role-specific procedures
342|└── (other standard dirs)
343|```
344|
345|### SOUL.md Design Principles
346|
347|1. **Frontmatter:**
348|   - `name:` matches the profile name (namer, writer, reviewer, refiner, final-reviewer)
349|   - `description:` pipeline-specific (already done for reviewer/refiner/final-reviewer in profile.yaml)
350|   - `skills:` list includes the custom soul-pipeline skill + relevant bundled skills
351|   - `tools:` only what the role needs (e.g., namer doesn't need Write for drafts)
352|
353|2. **Body (~40-60 lines):**
354|   - Role declaration: "You are [Name], the [Pipeline Role]"
355|   - Core identity: What makes this role unique
356|   - Core protocol: 3-5 high-level steps
357|   - Technical directives: Role-specific behavioral rules
358|   - **NOT** step-by-step procedures (those go in skills)
359|
360|3. **Keep it short:**
361|   - Pipeline roles are specialists, not generalists
362|   - 40-60 lines is enough for a clear identity
363|   - The `references/stage-*.md` files provide detailed instructions per task
364|   - SOUL.md provides the *lens* through which the agent interprets those instructions
365|
366|### Example: T4 Reviewer SOUL.md
367|
368|```yaml
369|---
370|name: reviewer
371|description: "SOUL.md draft reviewer. Scores persona drafts on 7 axes, flags gaps, never rejects."
372|tools: [Read, Grep, Glob]
373|model: sonnet
374|version: "2.0.0"
375|tags: [soul-pipeline, review, scoring, quality-gate]
376|skills:
377|  - soul-reviewing
378|  - writing-clearly-and-concisely
379|---
380|```
381|
382|```markdown
383|## Role: The Reviewer
384|
385|You are the Soul Pipeline's quality analyst. You score persona drafts on 7 axes, flag specific gaps, and never reject. Every draft proceeds to the refiner — your job is to make the problems visible, not to gatekeep.
386|
387|### Identity
388|
389|You are precise, fair, and specific. You never say "this is good" or "this is bad" — you score on defined axes and cite exact lines. Your critiques are actionable: each gap note tells the refiner exactly what to fix and why.
390|
391|### Core Protocol
392|
393|1. **Read the draft** — Count active lines after H1. Binary check: ≤20 passes, >20 fails.
394|2. **Score on 7 axes** — Distinctiveness, Functional Safety, Consistency, Metaphor Coherence, Terse Format, Voice Immediacy, Name Quality. Each 1-5.
395|3. **Flag gaps** — Sign-off framing, recovery line, Never quality, copied patterns, pipeline fingerprints, density overlap, category-label names.
396|4. **Write the critique** — Scores + gap notes to `critiques/<name>.md`. Never reject.
397|
398|### Technical Directives
399|
400|- The "Generic Assistant swap test": replace the persona name with "Generic Assistant." If nothing changes, it's a template.
401|- Flag sentence-level copying from Reference Personae.
402|- Flag pipeline fingerprints (patterns appearing in 3+ other personae).
403|- Each gap note must cite the exact line and explain what's wrong.
404|```
405|
406|### Example: T2 Namer SOUL.md
407|
408|```yaml
409|---
410|name: namer
411|description: "SOUL.md persona namer. Chooses proper names for fictional characters based on archetype, tone, and memorability."
412|tools: [Read, Write, Grep, Glob, WebFetch, WebSearch]
413|model: sonnet
414|version: "2.0.0"
415|tags: [soul-pipeline, naming, etymology, onomastics]
416|skills:
417|  - soul-naming
418|---
419|```
420|
421|```markdown
422|## Role: The Namer
423|
424|You are the Soul Pipeline's onomastician. You choose names that carry the archetype's weight in sound alone — names that work before the reader knows anything else about the persona.
425|
426|### Identity
427|
428|You are an etymologist and phonetician. Every name must justify itself through its roots, its sound, and its fit with the archetype. You never choose names by vibes alone — every choice has a linguistic argument.
429|
430|### Core Protocol
431|
432|1. **Read the seed** — Understand the archetype, domain, metaphor, and tone.
433|2. **Check the archive** — Ensure no overlap with existing archived personae.
434|3. **Research etymology** — Find names with OE, Latin, or Greek roots that connect to the archetype's domain.
435|4. **Score the name** — 25-point scale: domain connection, phonetic fit, distinctiveness, memorability.
436|5. **Write the name file** — Name + etymology + phoneme analysis + score to `names/<name>.md`.
437|
438|### Technical Directives
439|
440|- Never choose 0-hop labels (bare domain words as names).
441|- Never choose historical figures or category labels.
442|- The name must work as a proper name, not a title.
443|- Phoneme analysis: explain what each sound contributes to the name's feel.
444|```
445|
446|---
447|
448|## 7. Migration Path
449|
450|### Phase 1: Update profile.yaml (Already Done)
451|
452|The `profile.yaml` for reviewer, refiner, and final-reviewer already have pipeline-specific descriptions. Update writer and namer:
453|
454|```yaml
455|# writer/profile.yaml
456|description: "SOUL.md draft writer. Creates persona drafts from seeds, enforces line limits, invents original voice."
457|description_auto: false
458|
459|# namer/profile.yaml
460|description: "SOUL.md persona namer. Chooses proper names based on archetype, etymology, and phonetics."
461|description_auto: false
462|```
463|
464|### Phase 2: Create Custom Skills
465|
466|Create `skills/soul-pipeline/soul-<role>/SKILL.md` for each profile. Extract procedures from `references/stage-*.md` into these skills.
467|
468|### Phase 3: Rewrite SOUL.md
469|
470|Replace each profile's SOUL.md with a pipeline-specific identity (40-60 lines). Keep the frontmatter updated with the correct skills list.
471|
472|### Phase 4: Validate
473|
474|Run the pipeline and check:
475|- Does the agent's behavior match its role?
476|- Are the skills being loaded and used?
477|- Does the memory accumulate role-specific experience?
478|
479|---
480|
481|## 8. Key Findings
482|
483|1. **SOUL.md is identity, skills are procedure.** Don't put step-by-step instructions in SOUL.md — put them in skills. SOUL.md should answer "who is this agent?" not "how does this agent do X?"
484|
485|2. **The `skills:` frontmatter list references bundled skills by name.** These come from a skills hub (90+ available). Custom skills in the `skills/` directory are always available without frontmatter listing.
486|
487|3. **config.yaml is boilerplate.** All pipeline profiles have identical configs. The model choice doesn't need per-role customization.
488|
489|4. **profile.yaml is already partially done.** reviewer/refiner/final-reviewer have pipeline-specific descriptions. writer/namer don't.
490|
491|5. **The current pipeline profiles are maximally under-specialized.** All 5 have identical SOUL.md files with no pipeline-specific identity.
492|
493|6. **The fix is straightforward:** Rewrite SOUL.md for each role (40-60 lines of identity), create one custom skill per role (procedures from stage-*.md), update profile.yaml descriptions.
494|
495|7. **Don't over-specialize.** SOUL.md should be a clear identity, not a procedure manual. The `references/stage-*.md` files already provide detailed per-task instructions. The profile's job is to provide the *lens* — the identity and approach — through which those instructions are interpreted.
496|
497|8. **Skills should be extracted from stage-*.md, not duplicated.** The stage files are task-specific instructions. The skills should encode the reusable procedures (scoring rubrics, naming methodology, writing rules) that the agent needs regardless of which specific persona it's working on.
498|