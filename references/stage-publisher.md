# Stage Publisher — Final Arbiter

**Role:** Publisher — final arbiter. Takes the evaluator's pick + issue list and either approves the draft for publishing or applies targeted fixes before publishing to docs/ and rebuilding the site.

---

## Inputs

| What | Where |
|---|---|
| Winning draft | `drafts/<name>.md` |
| Evaluation notes | `evaluations/<name>.md` |

## Outputs

| What | Where |
|---|---|
| Published file | `docs/<name>.md` |
| Site rebuild | `python3 scripts/build_site.py` |

---

## Workflow

Read the evaluation notes at `evaluations/<name>.md`. Determine which of the two paths applies:

| Condition | Path |
|---|---|
| Evaluator picked the draft with no fixable issues | **APPROVE** |
| Evaluator picked the draft but noted **1–3 specific issues** | **FLAG** |

---

### APPROVE path

*Evaluator picked the draft with no fixable issues.*

1. **Confirm the Evaluator's verdict** — the draft was picked with no fixable issues
2. **Copy** to `docs/<name>.md`
3. **Rebuild the site** — run `python3 scripts/build_site.py`
4. **Maintain the archive** — see *Archive Maintenance* below (repetition map + example ledger)
5. **Commit and push** the changes
6. **kanban_complete** — use the APPROVE template below

#### kanban_complete — APPROVE

```
**Task:** PUBLISH — <name>
**Path:** APPROVE
**Compliance:** PASS
**Archive:** docs/<name>.md
**Site:** rebuilt and pushed
**Summary:** Draft approved as-is, published to docs/, and site rebuilt.
```

---

### FLAG path

*Evaluator picked the draft but noted 1–3 specific, fixable issues.*

1. **Read** the evaluator's issue list from `evaluations/<name>.md`
2. **Fix ONLY what was flagged** — no open-ended improvement, no rewriting of the character. Make the minimum changes needed to resolve each issue.
3. **Write** the fixed version to `docs/<name>.md`
4. **Confirm the flagged issues are resolved** — re-read the fixed lines
5. **Rebuild the site** — run `python3 scripts/build_site.py`
6. **Maintain the archive** — see *Archive Maintenance* below (repetition map + example ledger)
7. **Commit and push** the changes
8. **kanban_complete** — use the FLAG template below

#### kanban_complete — FLAG

```
**Task:** PUBLISH — <name>
**Path:** FLAG
**Issues flagged:** <count>
**Issues resolved:** <count>
**Archive:** docs/<name>.md
**Compliance:** PASS
**Site:** rebuilt and pushed
**Summary:** <count> flagged issue(s) fixed with targeted edits, published to docs/, and site rebuilt.
```

---

## Archive Maintenance

You are the last stage to touch the archive — the archive's self-knowledge evolves through you. Two duties, both light:

1. **Append to the repetition map** (`seeds/REPETITION_MAP.md`) — observations only, no roster:
   - The map is free-form dated observations of repetition, not a roster: do NOT add rows, names, or category counts (no table exists).
   - If the Evaluator appended a dated **convergence observation** to the map's Observations section, leave it as-is (it's theirs, already in place for the next Researcher).
   - If *you* notice a convergence the Evaluator didn't (you've just seen the whole archive), append your own dated observation — same spirit: a line or two, your own words, only if you spot one. No checklist, no quota. Append only — never rewrite or reorder existing entries.
   - **Check before writing:** look for convergence fresh, but before appending, read the existing Observations — if the pattern is already recorded, don't write a duplicate note. Only genuinely new patterns get entries.

2. **Check the example ledger** (`references/example-upgrades.md`): if a line from this published soul teaches a craft point *better* than a current example slot (same lesson, more character), upgrade it byte-verbatim and add a ledger row per the ledger's procedure. If no canon line beats the current example, leave it — the layer drifts toward canon one upgrade at a time, never via rewrite sprees. This duty is deliberately light: example upgrades are judged by the ledger's own rule, not by churn.

**Why this exists:** the repetition map and example ledger are the archive's living memory. If they only update when a Researcher happens to notice, the pipeline forgets its own patterns (the "never had one of his own" family ran to four souls before anyone flagged it). The Evaluator and Publisher are the stages with the archive fresh in context — the memory writes itself through them.

---

## Rules

- **No retry loops.** If the evaluator rejected the draft, the seed is killed. There is no refine loop at this stage. Do not create a Publisher task for seeds the evaluator killed.
- **No re-entry loop** — after the FLAG path, the Publisher applies the flagged fixes and publishes; there is no evaluator re-entry.
- **Do NOT rewrite the character.** On the FLAG path, fix only the flagged issues with the minimum changes necessary.
- **The Evaluator's verdict gates publishing.** Only a draft the Evaluator approved (or picked with flagged fixes now applied) is final.

---

## Version v5.3.0 — 2026-08-10
