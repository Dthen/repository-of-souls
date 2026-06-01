# SOUL.md — Pipeline Spec

## Pipeline Overview

Seven stages, strictly linear:

```
T0 (Researcher) → T1 (Viability Screener) → T2 (Namer) → T3 (Writer) → T4 (Reviewer) → T5 (Refiner) → T6 (Final Reviewer)
```

| Stage | Assignee | Input | Output |
|---|---|---|---|
| T0 | `soul-researcher` | `archive/`, `seeds/` | New seed files + T1 tasks |
| T1 | `soul-namer` | `seeds/<seed>.md` | Viability verdict (GO/HOLD/KILL) |
| T2 | `soul-namer` | `seeds/<seed>.md` | `names/<name>.md` |
| T3 | `soul-writer` | `names/<name>.md` + seed | `drafts/<name>.md` |
| T4 | `soul-reviewer` | `drafts/<name>.md` | `critiques/<name>.md` |
| T5 | `soul-refiner` | `drafts/<name>.md` + `critiques/<name>.md` | `refined/<name>.md` |
| T6 | `soul-final-reviewer` | `refined/<name>.md` | `archive/<name>.md` (or T5 retry) |

**For detailed stage instructions, see the corresponding reference file in `references/`.**

---

## Reference Files

| File | Contents |
|---|---|
| [`references/orchestration.md`](references/orchestration.md) | Task creation rules, chain validation, pre-flight checks, retry chains, file path rules, git credentials, naming conventions |
| [`references/stage-researcher.md`](references/stage-researcher.md) | T0 Researcher — archetype discovery, seed generation, pipeline spawning |
| [`references/stage-t1.md`](references/stage-t1.md) | T1 Viability Screener instructions |
| [`references/stage-t2.md`](references/stage-t2.md) | T2 Namer instructions |
| [`references/stage-t3.md`](references/stage-t3.md) | T3 Writer instructions |
| [`references/stage-t4.md`](references/stage-t4.md) | T4 Reviewer scoring rubric and gap flags |
| [`references/stage-t5.md`](references/stage-t5.md) | T5 Refiner instructions |
| [`references/stage-t6.md`](references/stage-t6.md) | T6 Final Reviewer hard-gate checklist, scoring rubric, archive instructions, and retry chain rules |
| [`references/format-rules.md`](references/format-rules.md) | Hard format constraints (lines, words, Nevers, sign-offs, filename case) |
| [`references/positive-patterns.md`](references/positive-patterns.md) | What good personae do right, what sign-offs are (and are not) |
| [`references/reference-personae.md`](references/reference-personae.md) | Kimbo + Brendan the Wizen — examples to study, not templates to copy |

**Stage bodies within task creation must include** the relevant reference file content inline. Do not rely on workers finding the references on their own.

---

## Mandatory Content

Six guardrails, each voiced in character:

1. **Tool safety** — Never refuses to use available tools.
2. **Clarity** — Flourishes clarify, never obscure. The persona must never be cryptic — but this guardrail must be expressed in archetype-specific language in the SOUL.md, not copied verbatim as "Never cryptic" (which is Brendan's wording).
3. **Follow-through** — Complains about the work while doing it perfectly. **This is the griping line — mandatory for every persona.**
4. **Tension** — The identity line must contain a contradiction. "You are [Name] — a [archetype] who [contradiction]" creates tension. "You are [Name] — a [archetype]" is just a definition.
5. **Address rule** — How the persona names the user.
6. **Sign-off rule** — How the persona closes.

These are the only hard constraints. Everything else is voice.

**Souls as system prompts:** The soul file is a system prompt that tells the model "embody this character." Every line should help the model do that better. Positive framing works better than negative framing. Write traits, not rules.

Full format constraints (line count, word count, Never rules, sign-off rules, etc.) are in [`references/format-rules.md`](references/format-rules.md).

---

## Version

v4.0 — 2026-06-01
