1|### Stage T5 — Refiner
2|
3|Input: One draft + critique notes.
4|Output: `refined/`.
5|
6|Apply the fixes requested. For high-scoring drafts: polish and tighten. For low-scoring drafts: heavier surgery — replace lines, restructure, even rewrite the opening if Voice Immediacy is weak.
7|
8|**Line count is non-negotiable.** After every edit, recount active lines after the H1. If you exceed 20 lines, cut the weakest line immediately — do not wait for a final pass. If the critique flagged repetition, cut the redundant lines first; do not merely rephrase them. A refined draft with >20 lines is a failed refinement.
9|
10|**Sanity check:** After any rewrite, read the changed line aloud. If it does not parse as a grammatical sentence that makes literal sense, discard that fix and try a smaller edit. Preserve meaning first, then improve tone.
11|
12|**Do NOT rename files yourself.** If you catch a name that fails v1.7 rules (historical figure, bare rank, domain label), do NOT rename the files yourself. Create a standalone T2 task (no parent) for the namer to handle. The namer has explicit instructions to rename ALL files and inline content. If you rename files yourself, you will create duplicates (copying to a new name without deleting the old one). The namer uses `mv`, not `cp`.
13|
14|