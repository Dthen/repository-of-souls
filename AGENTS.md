1|# SOUL.md — Pipeline Spec
2|
3|## Pipeline Overview
4|
5|Six stages, strictly linear:
6|
7|```
8|T1 (Researcher) → T2 (Namer) → T3 (Writer) → T4 (Reviewer) → T5 (Refiner) → T6 (Final Reviewer)
9|```
10|
11|| Stage | Assignee | Input | Output |
12||---|---|---|---|
13|| T1 | `researcher` | `archive/`, `drafts/` | `seeds/` |
14|| T2 | `soul-namer` | `seeds/<seed>.md` | `names/<name>.md` |
15|| T3 | `soul-writer` | `names/<name>.md` + seed | `drafts/<name>.md` |
16|| T4 | `soul-reviewer` | `drafts/<name>.md` | `critiques/<name>.md` |
17|| T5 | `soul-refiner` | `drafts/<name>.md` + `critiques/<name>.md` | `refined/<name>.md` |
18|| T6 | `soul-final-reviewer` | `refined/<name>.md` | `archive/<name>.md` (or T5 retry) |
19|
20|**For detailed stage instructions, see the corresponding reference file in `references/`.**
21|
22|---
23|
24|## Reference Files
25|
26|| File | Contents |
27||---|---|
28|| [`references/orchestration.md`](references/orchestration.md) | Task creation rules, chain validation, pre-flight checks, retry chains, file path rules, git credentials, naming conventions |
29|| [`references/stage-t1.md`](references/stage-t1.md) | T1 Researcher instructions (including coverage map and web search methodology) |
30|| [`references/stage-t2.md`](references/stage-t2.md) | T2 Namer instructions (including rejection rules and rename instructions) |
31|| [`references/stage-t3.md`](references/stage-t3.md) | T3 Writer instructions (including line count enforcement and anti-copy rules) |
32|| [`references/stage-t4.md`](references/stage-t4.md) | T4 Reviewer scoring rubric and gap flags |
33|| [`references/stage-t5.md`](references/stage-t5.md) | T5 Refiner instructions |
34|| [`references/stage-t6.md`](references/stage-t6.md) | T6 Final Reviewer hard-gate checklist, scoring rubric, archive instructions, and retry chain rules |
35|| [`references/format-rules.md`](references/format-rules.md) | Hard format constraints (lines, words, Nevers, sign-offs, filename case) |
36|| [`references/positive-patterns.md`](references/positive-patterns.md) | What good personae do right, what sign-offs are (and are not) |
37|| [`references/reference-personae.md`](references/reference-personae.md) | Kimbo + Brendan the Wizen — examples to study, not templates to copy |
38|
39|**Stage bodies within task creation must include** the relevant reference file content inline. Do not rely on workers finding the references on their own.
40|
41|---
42|
43|## Mandatory Content
44|
45|Six guardrails, each voiced in character:
46|
47|1. **Tool safety** — Never refuses to use available tools.
48|2. **Clarity** — Flourishes clarify, never obscure. The persona must never be cryptic — but this guardrail must be expressed in archetype-specific language in the SOUL.md, not copied verbatim as "Never cryptic" (which is Brendan's wording).
49|3. **Follow-through** — Complains about the work while doing it perfectly. **This is the griping line — mandatory for every persona.**
50|4. **Tension** — The identity line must contain a contradiction. "You are [Name] — a [archetype] who [contradiction]" creates tension. "You are [Name] — a [archetype]" is just a definition.
51|5. **Address rule** — How the persona names the user.
52|6. **Sign-off rule** — How the persona closes.
53|
54|These are the only hard constraints. Everything else is voice.
55|
56|**Souls as system prompts:** The soul file is a system prompt that tells the model "embody this character." Every line should help the model do that better. Positive framing works better than negative framing. Write traits, not rules.
57|
58|Full format constraints (line count, word count, Never rules, sign-off rules, etc.) are in [`references/format-rules.md`](references/format-rules.md).
59|
60|---
61|
62|## Version
63|
64|v2.0 — 2026-05-31
65|