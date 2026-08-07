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

1. **Verify compliance** — run `check_soul.py` on the draft at `drafts/<name>.md`
2. **Copy** to `docs/<name>.md`
3. **Rebuild the site** — run `python3 scripts/build_site.py`
4. **Commit and push** the changes
5. **kanban_complete** — use the APPROVE template below

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
4. **Verify compliance** — run `check_soul.py` on the published file
5. **Rebuild the site** — run `python3 scripts/build_site.py`
6. **Commit and push** the changes
7. **kanban_complete** — use the FLAG template below

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

## Rules

- **No retry loops.** If the evaluator rejected the draft, the seed is killed. There is no refine loop at this stage. Do not create a Publisher task for seeds the evaluator killed.
- **If more fixes are needed** after the FLAG path, do not iterate — go back through the evaluator as a new task.
- **Do NOT rewrite the character.** On the FLAG path, fix only the flagged issues with the minimum changes necessary.
- **Compliance check before publishing is mandatory.** The `check_soul.py` step must pass before the docs/ copy is considered final.

---

## Version

v5.2.5 — 2026-08-07
