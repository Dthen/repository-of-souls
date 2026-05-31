# SOUL.md — Pipeline Spec

## Pipeline Overview

Six stages, strictly linear:

```
T1 (Researcher) → T1b (Namer) → T2 (Writer) → T3 (Reviewer) → T5 (Refiner) → T6 (Final Reviewer)
```

| Stage | Assignee | Input | Output |
|---|---|---|---|
| T1 | `researcher` | `archive/`, `drafts/` | `seeds/` |
| T1b | `soul-namer` | `seeds/<seed>.md` | `names/<name>.md` |
| T2 | `soul-writer` | `names/<name>.md` + seed | `drafts/<name>.md` |
| T3 | `soul-reviewer` | `drafts/<name>.md` | `critiques/<name>.md` |
| T5 | `soul-refiner` | `drafts/<name>.md` + `critiques/<name>.md` | `refined/<name>.md` |
| T6 | `soul-final-reviewer` | `refined/<name>.md` | `archive/<name>.md` (or T5 retry) |

**For detailed stage instructions, see the corresponding reference file in `references/`.**

---

## Reference Files

| File | Contents |
|---|---|
| [`references/orchestration.md`](references/orchestration.md) | Task creation rules, chain validation, pre-flight checks, retry chains, file path rules, git credentials, naming conventions |
| [`references/stage-t1.md`](references/stage-t1.md) | T1 Researcher instructions (including coverage map and web search methodology) |
| [`references/stage-t1b.md`](references/stage-t1b.md) | T1b Namer instructions (including rejection rules and rename instructions) |
| [`references/stage-t2.md`](references/stage-t2.md) | T2 Writer instructions (including line count enforcement and anti-copy rules) |
| [`references/stage-t3.md`](references/stage-t3.md) | T3 Reviewer scoring rubric and gap flags |
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

v2.0 — 2026-05-31
