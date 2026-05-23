# T6 Final Review: Sully (The Engineer) — Revision

**File:** `refined/sully.md` → **Archived:** `archive/sully.md`

## Auto-Reject Gates — ALL CLEAR

| Gate | Result |
|------|--------|
| Bare Reference Persona Never ("Never Gandalf", etc.) | ✓ PASS — none present |
| Line count 8–20 | ✓ PASS — 13 active lines |
| Nevers ≤ 3 | ✓ PASS — 3 Nevers |
| Identity opening | ✓ PASS — "You are Sully — a starship chief engineer..." |
| Recovery line | ✓ PASS — "you don't let the same failure burn you twice" / "trust your gut but double-check it anyway" |
| Read for sense | ✓ PASS — all lines parse as grammatical sentences |
| Read for repetition | ✓ PASS — no restated concepts. "burned" (L5: trusting clean theory) and "burn" (L8: repeating failures) are distinct signals |
| Pipeline fingerprints | ✓ PASS — 0 remaining. L3 uses "reads the [X] and the [Y] at the same time", not the "reads [X] before [Y]" pattern |
| Generic Nevers | ✓ PASS — all three are domain-specific |
| Sentence-level copying | ✓ PASS — all structures are original for this archetype |

## 7-Axis Scoring

| Axis | Score | Rationale |
|------|-------|-----------|
| **Distinctiveness** | 5 | Starship chief engineer with specific trade-offs (schematic vs smoke signal, yard-spares, system states/hull zones). Nothing swappable with Generic Assistant. |
| **Functional Safety** | 5 | Three domain-specific Nevers: don't over-explain, don't get lost in analysis-pareto, don't leave things half-done. Plus implicit guardrails: double-check gut, traceability on scuttled components. |
| **Consistency Sustainability** | 4 | Strong pragmatic engineer voice sustains across 50 messages. Minor note: "burn" metaphor appears in lines 5 and 8 in different contexts (trusting theory vs repeating failure) — close enough to flag but not redundant. |
| **Metaphor Coherence** | 5 | Engine-room domain holds throughout: schematics, smoke signals, scorch marks, gauges, relays, yard-spares, power surges, fault trees, reroutes, signal hums. Maps to tool behaviours (verification, triage, communication). Recovery line present. |
| **Terse Format** | 5 | 13 active lines, one sentence each, no nesting. Well within the 8–20 cap. |
| **Voice Immediacy** | 5 | Opening identity line correctly formed. Three quotable candidates in first 4 lines: "sign off like it's your name on the hull", "bad call follows you longer than a good one rewards you", "scorch mark tells you more than the gauge ever will". Three distinct registers in first 3 lines: identity/duality, accountability/consequences, experiential wisdom. |
| **Name Quality** | 5 | "Sully" is a proper name, fits a no-nonsense engineer. |

**Total: 34/35**

## T5 Issue Verification

| Issue | Resolution | Status |
|-------|-----------|--------|
| 1. `reads [X] before [Y]` pipeline fingerprint | "reads the schematic and the smoke signal at the same time" — structurally distinct, uses "and...at the same time" not "before" | ✓ CLOSED |
| 2. Generic procedural Never | "Never let the fault tree distract you from the fix that holds pressure" — uses fault-tree analysis as the engineering cultural reference | ✓ CLOSED |

## Decision

**APPROVED.** All auto-reject gates clear. Score 34/35 with every axis ≥ 4. No structural issues, no copied structures, no pipeline fingerprints, no generic Nevers. Archiving Sully as a canonical persona.
