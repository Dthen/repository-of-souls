# T6 Reject: Vance — Sign-off count < 3

**Date:** 2026-05-25
**Reviewer:** final-reviewer
**File:** refined/vance.md

## Result: FAIL — Rejected at HARD GATE

One HARD GATE violation found. Re-score below passes all axis thresholds, but the sign-off count gate is auto-reject with no exceptions.

## HARD GATE Checklist

| Gate | Result | Detail |
|------|--------|--------|
| Word count ≤ 200 | ✓ PASS | 192 words after H1 |
| Logical self-contradiction | ✓ PASS | No self-negating lines found |
| "You never" in Never block | ✓ PASS | All Never lines start with "Never" |
| Physical-action sign-off framing | ✓ PASS | "land flatly final" = delivery tone |
| Third-person intrusion | ✓ PASS | All lines use "You" / "Your" |
| Obscure reference in Nevers | ✓ PASS | Port admiral, stamp/inspection — clear |
| Multiple Nevers on one line | ✓ PASS | 3 standalone Never lines |
| Literal system tool names | ✓ PASS | None |
| Dense repetition | ✓ PASS | All 10 lines carry distinct signal |
| **Sign-off count < 3** | **❌ FAIL** | 2 phrases: "Cleared.", "Next manifest." — minimum 3 required |
| Line count (8–20) | ✓ PASS | 10 active lines |
| Recovery check | ✓ PASS | Line 6: "When cargo is spilled across the dock, you call for the tally clerk and work through the wreckage line by line." |
| Identity opening | ✓ PASS | "You are Vance — a customs officer at the port gate..." |
| Bare Reference Persona Never | ✓ PASS | All archetype-specific |
| Sentence-level copying | ✓ PASS | Original structures |
| Generic Nevers | ✓ PASS | All domain-specific |
| Pipeline fingerprint phrases | ✓ PASS | None detected |
| Read for sense | ✓ PASS | All lines parse as grammatical sentences |
| T3 defect carries forward | ✓ PASS | All 6 gaps resolved |

## 7-Axis Scores

| Axis | Score | Notes |
|------|-------|-------|
| Distinctiveness | 4/5 | Customs officer at the port gate — clear, domain-specific. Not swappable with Generic Assistant. |
| Functional Safety | 4/5 | Three archetype-specific Nevers, clarity guardrail present, recovery line present. Strong. |
| Consistency Sustainability | 4/5 | Domain vocabulary provides lexical variety. Cold/warm contrast in first 3 lines. |
| Metaphor Coherence | 5/5 | Every line within customs domain. No literal tool mapping. |
| Terse Format | 4/5 | 10 lines, one sentence each, clean formatting. |
| Voice Immediacy | 4/5 | Strong quotable identity in line 1. Cold ("gatekeeper's answer is no") + warm ("merchants their meal") registers in first 3 lines. |
| Name Quality | 5/5 | Vance — proper name, not a category label, not historical, not bare rank. |
| **Total** | **30/35** | All axes ≥ 3. Exceeds minimum total of 20. |

## Failure Detail

**Gate: Sign-off count < 3 (AGENTS.md line 409)**

> "A single sign-off or two sign-offs is insufficient tonal range. Minimum three distinct phrases."

The refined draft has exactly 2 sign-off phrases:

```
Your sign-offs land flatly final: 'Cleared.' 'Next manifest.'
```

**Root cause:** The T3 critique (critiques/vance.md, Gap 3) incorrectly stated "The T6 gate treats ≥3 as excessive" and advised reducing from 3 to 2. This is a misread of the gate direction. AGENTS.md clearly requires a **minimum** of 3 distinct phrases. The T5 refiner followed the T3 advice and introduced a T6 violation.

## T3 Defect Carried Forward Check

| T3 Gap | Status | Evidence |
|--------|--------|----------|
| Gap 1: Word count > 200 | ✓ Fixed | 192 words after H1 |
| Gap 2: Physical-action sign-off framing | ✓ Fixed | "land flatly final" = delivery tone |
| Gap 3: Sign-off count (was: ≥3) | ✗ New violation | Reduced to 2, but min 3 required per AGENTS.md |
| Gap 4: Clarity guardrail missing | ✓ Fixed | "You read every manifest in the open — both the merchant and you can see what's in the hold." |
| Gap 5: Recovery line missing | ✓ Fixed | "When cargo is spilled across the dock, you call for the tally clerk and work through the wreckage line by line." |
| Gap 6: Uniform register | ✓ Fixed | Cold register: "the gatekeeper's answer is no until the hold is read" (line 2). Warm pivot: "stalled goods cost the merchants their meal" (line 3). |

## Required Fix

Restore the third sign-off phrase. Options:
- Re-add "Flagged." from the original — it was removed per T3 advice but it's valid
- Create a new third phrase that adds tonal range, e.g. "'Hard to read.'" or "'On hold.'" or "'Gate's closed.'"
- Verify the revised line maintains the 3+ count: e.g. "Your sign-offs land flatly final: 'Cleared.' 'Flagged.' 'Next manifest.'"

The rest of the draft is strong and passes all other gates at scoring thresholds above minimum.