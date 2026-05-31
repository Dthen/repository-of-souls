1|# Pipeline Orchestration Guide
2|
3|This document governs how pipeline tasks are created, linked, and validated. Every worker who creates kanban tasks must follow these rules. Getting them wrong produces the blocked tasks we just debugged.
4|
5|---
6|
7|## Creation Order and Chain Rules
8|
9|The pipeline is a **strictly linear chain**:
10|
11|```
12|T1 (Researcher) → T2 (Namer) → T3 (Writer) → T4 (Reviewer) → T5 (Refiner) → T6 (Final Reviewer)
13|```
14|
15|Each stage is the **parent of the next**. A task MUST NOT be created unless its upstream parent either exists or is created in the same orchestration step.
16|
17|### Critical Rule: No Gaps Allowed
18|
19|If you are creating a task for Stage N, Stage N-1 must:
20|- Already exist on the board as a done task (with its output artifact on disk), OR
21|- Be created alongside Stage N in the same orchestration step.
22|
23|**THIS IS NOT OPTIONAL.** Creating a downstream task without its upstream parent is the root cause of phantom-blocked chains like "T3 Review farrier" with no `drafts/farrier.md`.
24|
25|### Stage-to-Profile Mapping
26|
27|| Stage | Title pattern | `assignee` value |
28||-------|---------------|------------------|
29|| T2 | `T2: Name <Seed>` | `soul-namer` |
30|| T3 | `T3: Write <Name> SOUL.md` | `soul-writer` |
31|| T4 | `T4: Review <Name> SOUL.md` | `soul-reviewer` |
32|| T5 | `T5: Refine <Name> SOUL.md` | `soul-refiner` |
33|| T6 | `T6: Final-review <Name> SOUL.md` | `soul-final-reviewer` |
34|
35|Do NOT assign all stages to one profile. Do NOT use the creating worker's own profile.
36|
37|### Task Workspace
38|
39|Every task MUST be created with:
40|```yaml
41|workspace_kind: "dir"
42|workspace_path: "/home/kimbo/.hermes/projects/soul-repository"
43|```
44|
45|`scratch` workspaces isolate workers in temporary directories where they cannot read AGENTS.md, cannot see existing personae, and cannot write outputs to the correct locations.
46|
47|---
48|
49|## Pre-Flight Checks Before Creating Any Task
50|
51|Before calling `kanban_create`, verify the upstream artifact exists. If it does not, you MUST create the missing upstream stages first.
52|
53|| Creating stage | Required upstream artifact | Path to check |
54||---|---|---|
55|| T2 | Seed file | `seeds/<seed-label>.md` |
56|| T2 | Chosen name file | `names/<chosen-name>.md` |
57|| T3 | Draft file | `drafts/<name>.md` |
58|| T5 | Critique file | `critiques/<name>.md` |
59|| T6 | Refined file | `refined/<name>.md` |
60|
61|**If the file doesn't exist:** Do NOT create the downstream task. Create the missing upstream stages instead. For example:
62|- If `seeds/the-farrier.md` exists but no `drafts/farrier.md`, create a T2 → T3 chain for farrier first.
63|- If `critiques/cross.md` exists but no `refined/cross.md`, create a T5 for cross first.
64|
65|---
66|
67|## Input File Path Rules
68|
69|The `Input draft file` directive in each task body MUST reference the correct directory for that stage:
70|
71|| Stage | Output directory | Task body must reference |
72||---|---|---|
73|| T2 | `drafts/` | Input: `names/<name>.md` |
74|| T3 | `critiques/` | Input: `drafts/<name>.md` |
75|| T5 | `refined/` | Input: `drafts/<name>.md` + `critiques/<name>.md` |
76|| T6 | `archive/` or `reject/` | Input: `refined/<name>.md` |
77|
78|**T6 MUST read `refined/<name>.md`, never `drafts/<name>.md`.** Passing the wrong path means T6 judges stale draft content instead of the refiner's actual output.
79|
80|---
81|
82|## T6 Retry Chain (On Rejection)
83|
84|When T6 rejects a draft, it does NOT block. It creates a **loopback**:
85|
86|1. Create a new T5 task with:
87|   - The `refined/<name>.md` file as input
88|   - The specific failure notes from T6 as the critique
89|   - A clear instruction on what must change to pass
90|
91|2. **In the same orchestration step**, create a T6 child task chained to the new T5 (assignee: `soul-final-reviewer`, parents: [new T5 task id]).
92|
93|3. Complete the current T6 with a note that a retry was created.
94|
95|**Without step 2, the T5 fix completes with no T6 to re-review it — the chain breaks and the fix is orphaned.**
96|
97|The refiner applies the fixes and returns the draft to T6. Repeat until the draft passes or the character fundamentally cannot be saved.
98|
99|Only when a draft has failed T6 three times with the same structural flaw should you consider abandoning it — and even then, the final disposition is `reject/<name>.md` with a note explaining which seed archetype does not work.
100|
101|---
102|
103|## T6 Name-Rejection Chain
104|
105|If T6 rejects on Name Quality (< 3), the chain is:
106|
107|1. Create a **standalone** T2 task (no parent) with the archetype context and a note that it replaces the rejected name.
108|2. The T2 namer picks a new name, renames the existing file, and creates the downstream chain: **T4 → T5 → T6**.
109|3. Complete the current T6 noting that a rename chain was created.
110|
111|**How the rename works:** The content is already in archive — T2 revises it in place, not rewrites from scratch. T2 moves `archive/<old>.md` → `drafts/<new>.md`, then updates every reference to the old name: the H1, the identity line (`You are <OldName> — ...`), and any other mentions in the body. Use `grep -ri "<old-name>" .` to find them all. The content, voice, and structure stay the same — only the name changes.
112|
113|Do NOT create a T2 task. The existing content is the artifact — T2 would start from the seed and lose the refiner's work. Do NOT rename files yourself. Do NOT create a child T5 chained to the blocked T6 parent — this creates a deadlock.
114|
115|---
116|
117|## File Naming Convention
118|
119|Every stage uses the **chosen character name** as the filename, not the seed label.
120|
121|The T2 Namer is the source of truth. If the chosen name is **Roux**, all files for that persona are:
122|- `names/roux.md`
123|- `drafts/roux.md`
124|- `critiques/roux.md`
125|- `refined/roux.md`
126|- `archive/roux.md` (or `reject/roux.md`)
127|
128|**Rule:** Read the chosen name from the previous stage's output file. Never construct a filename from the seed label (e.g. `the-galley-chef`).
129|
130|---
131|
132|## Git Credentials and HOME Isolation
133|
134|Kanban workers run with a **profile-isolated HOME**. When a worker uses profile `soul-writer`, its `HOME` is set to `~/.hermes/profiles/writer/home/`. This means `git` looks for `~/.gitconfig` and `~/.git-credentials` inside the profile's `home/` directory.
135|
136|If `git push` fails with "no credentials configured", the profile's `home/` is missing credentials.
137|
138|```bash
139|cp ~/.git-credentials ~/.hermes/profiles/<profile>/home/.git-credentials
140|cp ~/.gitconfig ~/.hermes/profiles/<profile>/home/.gitconfig
141|chmod 600 ~/.hermes/profiles/<profile>/home/.git-credentials
142|```
143|
144|Apply this to all profiles that run `git push`: `soul-writer`, `soul-namer`, `soul-reviewer`, `soul-refiner`, `soul-final-reviewer`.
145|
146|---
147|
148|## Process Integrity
149|
150|Pipeline outputs are read-only. Every file produced by any stage is the artifact of the spec, not raw material for manual editing.
151|
152|If a draft has the wrong filename, a malformed line, or a missing guardrail, the defect is in the spec — not the file. Fix the reference document or AGENTS.md, then re-run the stage. Never manually edit, rename, move, commit, or otherwise touch any output from any pipeline stage.
153|
154|This rule exists because manual edits destroy provenance. If a file in `archive/` was hand-corrected, no one can verify which parts came from the pipeline and which came from post-hoc intervention. The result is untrustworthy.
155|