1|### Stage T1 — Namer
2|
3|Input: One seed from `seeds/<seed-label>.md`.
4|Output: `names/<chosen-name-lower>.md` — a single chosen name + 4 rejected alternatives with brief notes.
5|
6|**Filename rule:** The output file MUST be named `<chosen-name-lower>.md` using the exact chosen name in lowercase. This filename is the source of truth for every subsequent stage. **All filenames across every pipeline directory are lowercase.** uppercase filenames produce non-deterministic duplicate handling on case-insensitive filesystems and are treated as malformed.
7|
8|---
9|
10|## Naming Principles
11|
12|**You are finding a name that makes a character real.** The name is the first thing the model sees — it sets the tone for everything that follows.
13|
14|**Think in sound first, meaning second.** A name must be speakable — something a person would introduce themselves with, not a label on a catalogue. You hear the rhythm before you check the etymology.
15|
16|**Work at one or two hops from the literal.** The domain word is the center; you orbit it. "Coil" sits one hop from electricity — you can feel the wire. "Gale" sits on the center itself — it IS the wind, not a character who carries it. You reject the center.
17|
18|**Carry a collision sensor.** Famous figures, trade nouns, stereotype names — these are already claimed. Test: would a parent name a child this, and have it stand alone without the domain context?
19|
20|**Your candidates have texture.** Each one earns its place by sounding like a person, not a category.
21|
22|---
23|
24|## The Hop Test
25|
26|Good names sit 1–2 semantic hops from the literal domain word.
27|
28|- **0 hops (reject):** "Ferry" for a ferryman. "Gale" for a wind keeper. "Forge" for a blacksmith. These ARE the domain word. A parent would not name a child this.
29|- **1 hop (ideal):** "Coil" for electricity (wire → coil). "Nye" for telegraphy (wire → nautical term for a bend → Nye). You can feel the connection without it being literal.
30|- **2 hops (acceptable):** "Stanza" for poetry (poetry → verse → stanza). The connection is there but requires a small leap.
31|- **3+ hops (reject):** Too obscure. The name loses its connection to the domain.
32|
33|---
34|
35|## Phonetic Instinct
36|
37|Names need mouth-feel. The sound should match the archetype's projected register.
38|
39|- **Consonant clusters give weight:** "Snell," "Cross," "Brock" — these feel solid, grounded.
40|- **Vowel-forward names feel lighter:** "Owen," "Alloy," "Eamon" — these feel more fluid, approachable.
41|- **Short names punch:** "Nye," "Riff," "Dash" — these feel quick, decisive.
42|- **Long names flow:** "Merriwether," "Lysander," "Sullivan" — these feel more formal, deliberate.
43|
44|---
45|
46|## Collision Detection
47|
48|Test each candidate against:
49|
50|1. **Famous figures:** "Tesla," "Einstein," "Shakespeare" — already claimed.
51|2. **Common trade nouns:** "Smith," "Baker," "Taylor" — too generic.
52|3. **Stereotypical associations:** "Jasper the Butler," "Jeeves" — already a trope.
53|4. **Existing personae:** Check against all archived personae in `archive/`.
54|5. **The "parent test":** Would a parent name a child this, and have it stand alone without the domain context? If no, reject.
55|
56|**Fame test:** Search the name. If the famous bearer appears as the PRIMARY TOPIC on Wikipedia's disambiguation page, the name is a collision regardless of domain.
57|
58|---
59|
60|## Name Quality Scoring
61|
62|Generate **5 proper names** for this persona. Not titles. Not archetype labels. Names a person would introduce themselves with.
63|
64|Score each candidate on 5 axes (1–5):
65|
66|1. **Phonetic fit:** Does the name sound like the archetype? Does it have the right mouth-feel?
67|2. **Etymological depth:** How many hops from the domain? 1–2 is ideal.
68|3. **Collision risk:** How likely is this to collide with famous figures, trade nouns, or existing personae?
69|4. **Memorability:** Is this name easy to remember? Does it stick?
70|5. **Domain resonance:** Does this name evoke the domain without being literal?
71|
72|Pick the highest scorer. If tie, pick the one with the strongest phonetic character (rhythm, consonance, mouth-feel).
73|
74|---
75|
76|## Output Format
77|
78|Save output as:
79|```
80|# Chosen: [Name]
81|
82|## Candidates
83|1. [Name] — [score/25] — [one-line why]
84|2. [Name] — [score/25] — [one-line why]
85|...
86|
87|## Rejection Notes
88|[Name]: [why it lost]
89|```
90|
91|**Critical rule**: The H1 of the final SOUL.md must be the chosen name from this stage. T2 receives the name as an explicit input. No archetype labels in the H1.
92|
93|---
94|
95|## Few-Shot Examples
96|
97|### Good Naming
98|
99|**Seed:** Telegraphy archetype
100|**Candidate:** "Nye"
101|**Reasoning:** 1 hop from telegraphy (wire → nautical term for a bend → Nye as surname). Phonetic: short, punchy, the 'y' gives it a spark. Real surname. No famous collision. Score: 5/5 phonetic, 5/5 etymological, 5/5 collision, 5/5 memorability, 5/5 domain.
102|
103|### Bad Naming
104|
105|**Seed:** Ferryman archetype
106|**Candidate:** "Ferry"
107|**Reasoning:** 0 hops. It IS the domain word. A parent would not name a child Ferry. No texture, no reference layer. This is a label, not a name. Score: 1/5 phonetic, 1/5 etymological, 1/5 collision, 1/5 memorability, 1/5 domain.
108|
109|---
110|
111|## Rename Instructions
112|
113|**When renaming an existing soul** (T6 rejected the old name): After picking the new name, revise the existing content — do NOT rewrite from scratch.
114|
115|1. **Move the file:** `mv archive/<old>.md drafts/<new>.md`. The existing content is the artifact — keep it.
116|2. **Update ALL name references** in `drafts/<new>.md`:
117|   - H1: `# <OldName>` → `# <NewName>`
118|   - Identity line: `You are <OldName> — ...` → `You are <NewName> — ...`
119|   - Any other mentions of the old name in the body
120|   - Use `grep -ri "<old-name>\" .` to find them all
121|3. **Write the name file** to `names/<new>.md` with the chosen name and candidates (same format as normal T2 output).
122|4. **Clean up old artifacts** (if present): `rm names/<old>.md critiques/<old>.md refined/<old>.md docs/<old>.html`
123|5. **Verify:** `ls archive/<old>.md` should fail. `drafts/<new>.md` should contain the updated content.
124|
125|**Do NOT create a T2 task.** The existing content is the artifact — T2 would start from the seed and lose the refiner's work. The content, voice, and structure stay the same; only the name changes.
126|
127|6. **Create the downstream pipeline chain:** T3 → T5 → T6, each linked as parent of the next:
128|   - Create a T3 task (assignee: `soul-reviewer`, parents: [this task id])
129|   - Create a T5 task (assignee: `soul-refiner`, parents: [T3 task id])
130|   - Create a T6 task (assignee: `soul-final-reviewer`, parents: [T5 task id])
131|   
132|   All tasks must use `workspace_kind: "dir"` and `workspace_path: "/home/kimbo/.hermes/projects/soul-repository"`.
133|
134|**The old draft is revised, not replaced.** T2 is not part of the rename chain.
135|