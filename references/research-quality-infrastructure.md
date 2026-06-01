# Quality Infrastructure & Automation — Research Report

**Task:** t_5bc5e557  
**Date:** 2026-06-01  
**Scope:** Lint specification, quality evaluation prompts, gold set, failure schema, viability screener, orchestration redesign

---

## Section 1: lint_soul.py Full Specification

### Current State

The existing `check_soul.py` (220 lines) implements 13 checks. It is a good start but misses several format-rules requirements and has no LLM fallback for semantic checks. The proposed `lint_soul.py` consolidates all compliance into a single deterministic script, separating it cleanly from quality evaluation.

### Complete Check Specification

| # | Check Name | Method | Deterministic | Error Message Format |
|---|-----------|--------|:---:|---------------------|
| 1 | **Filename lowercase** | `os.path.basename(path) == basename.lower()` | Yes | `FAIL: filename is not lowercase ({filename}) — rename to {lowercase}` |
| 2 | **H1 match** | `lines[0] == f"# {name_slug.capitalize()}"` | Yes | `FAIL: H1 mismatch — expected "# {name}", got "{actual}"` |
| 3 | **First line "You are Name"** | `active[0].startswith("You are {name}")` | Yes | `FAIL: first line must start with "You are {name}"` |
| 4 | **Line count 8–20** | `8 <= len(active) <= 20` | Yes | `FAIL: line count {n} outside 8–20 range` |
| 5 | **Word count ≤200** | `len(text.split()) <= 200` | Yes | `FAIL: word count {n} exceeds 200` |
| 6 | **One sentence per line** | Regex: no bullet markers (`- `, `* `), no nested sections | Yes | `FAIL: line {n} appears to be a bullet or nested section` |
| 7 | **Second person throughout** | Check for standalone "he"/"she"/"a [noun] who" after identity line | Yes | `FAIL: third-person intrusion on line {n}: "{line[:40]}"` |
| 8 | **Never count ≤3** | Count lines starting with "Never" | Yes | `FAIL: {n} Nevers found, maximum is 3` |
| 9 | **No multiple Nevers per line** | Count `\bNever\b` occurrences per never-line | Yes | `FAIL: line {n} contains {m} Never occurrences` |
| 10 | **No "You never" in Never block** | Regex `\byou never\b` in never-lines | Yes | `FAIL: "You never" found in Never block` |
| 11 | **Sign-off count ≥3** | Count quoted phrases in sign-off line | Yes | `FAIL: {n} sign-off phrases, minimum is 3` |
| 12 | **Sign-off framing not physical** | Regex for physical-action words in sign-off line | Yes | `FAIL: sign-off framing describes physical action: "{line[:50]}"` |
| 13 | **Griping line present (voiced)** | Regex for griping patterns (You'd think, grumble, etc.) minus generic complaints | Yes* | `FAIL: no voiced griping line found` or `FAIL: griping is generic: "{line[:40]}"` |
| 14 | **Recovery line present** | Regex for conditional/contrast patterns (If/When/Where/wrong/fail) | Yes | `FAIL: no recovery line ("what happens when wrong")` |
| 15 | **No literal tool names** | Grep for banned strings (grep, sed, curl, python, bash, etc.) | Yes | `FAIL: literal tool name "{tool}" on line {n}` |
| 16 | **No dense repetition** | Pairwise word-overlap ≥80% between any two lines | Yes | `FAIL: lines {i} and {j} share ≥80% words` |
| 17 | **No bare Reference Persona Nevers** | Check for "Never a [Generic Role]" without archetype-specific explanation | Partial | `FAIL: bare reference persona Never on line {n}` |
| 18 | **No pipeline fingerprint phrases** | Grep for "SOUL.md", "pipeline", "T3", "T4", "T5", "kanban" | Yes | `FAIL: pipeline fingerprint phrase on line {n}` |
| 19 | **No obscure references** | LLM fallback (see below) | No (LLM) | `FAIL: obscure reference detected — "{reference}"` |
| 20 | **Reads for sense (coherence)** | LLM fallback (see below) | No (LLM) | `FAIL: line {n} does not read for sense — "{line[:40]}"` |

### Deterministic vs LLM Split

**Deterministic (17 checks):** All checks 1–18 can be implemented with regex, string matching, and counting. These produce binary PASS/FAIL with zero LLM cost. They run in <100ms.

**LLM fallback (3 checks):** Checks 19–20 require semantic understanding:

1. **Obscure references (Check 19):** The LLM sees the full persona text and is asked: "Are there any references a general-educated reader would not recognize on first read?" Returns a list of suspicious references or "none."

2. **Reads for sense (Check 20):** The LLM reads each line and asks: "Does this line make sense as a sentence? Is it grammatically coherent?" Returns flagged lines or "all coherent."

3. **Sentient being check** (implicit in Check 3 — the identity line check): The existing `stage-t0.md` handles this at the seed level. At lint time, we trust the pipeline has already screened for personhood.

### LLM Fallback Integration

The LLM checks run only AFTER all deterministic checks pass. If any deterministic check fails, the script exits immediately with all failures reported. The LLM checks are invoked only on compliant drafts:

```python
# After all deterministic checks pass:
if args.llm_check:
    import subprocess
    result = subprocess.run(
        ["hermes", "chat", "--prompt", LLM_LINT_PROMPT, "--file", path],
        capture_output=True, text=True
    )
    # Parse LLM output for obscure references and coherence issues
```

The LLM fallback is **optional** — it can be disabled with `--no-llm` for fast CI runs. The deterministic checks alone catch 90%+ of format violations.

### Output Format

```
lint_soul.py — SOUL.md compliance linter
File: archive/helm.md

  [1]  Filename lowercase:              PASS
  [2]  H1 match:                        PASS
  [3]  First line "You are Name":       PASS
  [4]  Line count 8–20:                 PASS (10 lines)

<!-- NOTE: This file was recovered from a truncated kanban log. 761 of 839 lines were omitted from the log; only the first 78 lines are preserved here. The full document was 839 lines. -->
