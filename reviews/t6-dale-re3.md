# T6 Final Review — Dale (Carter) — REJECTED (3rd attempt)

**Date:** 2026-05-26
**Reviewer:** final-reviewer

## Result: HARD GATE FAILURE — Word Count > 200

The draft was checked against the 16-point hard gate checklist from stage-t6.md. One gate failed.

### Failed Gate

**Word count ≤ 200** — `wc -w` reports **209 words** after the H1, confirmed by Python `split()`. Per stage-t6.md: *"Word count > 200 after H1. Cut lines, not words. Long sentences are a workaround — the word count catches the cheat. This cap is auto-reject at T6 regardless of other scores."*

### How the count changed — and why it's still high

The T5 retry 2 claimed to trim from 203 to 199 by removing 4 words:
1. `"between the yard and the receiving dock"` → `"between yard and receiving dock"` (saves 2)
2. `"the sender's trust rides"` → `"trust rides"` (saves 2)

These changes ARE visible in the file. However, the actual count of the current file is 209 — not 199. The word count discrepancy suggests earlier counts may have been off. What matters: the current file has 209 words, which is 9 over the cap.

### Passing Gates (16/16)

| Gate | Status |
|---|---|
| Lowercase filename — `dale.md` | ✅ |
| Line count 8–20 — 10 active lines | ✅ |
| Identity opening — "You are Dale — a carter:..." | ✅ |
| Recovery line — L9, L13 | ✅ |
| Sign-off count ≥ 3 — 3 quoted phrases | ✅ |
| Sign-off framing is delivery tone — "mark the leg between yard and receiving dock" | ✅ |
| Logical self-contradiction — None | ✅ |
| "You never" not in Never block — All Nevers start with bare "Never" | ✅ |
| Third-person intrusion — All lines second-person | ✅ |
| Multiple Nevers on one line — Three Nevers on separate lines | ✅ |
| Literal system tool names — None | ✅ |
| Dense repetition — Good structural variety across 10 lines | ✅ |
| Bare Reference Persona Never — All Nevers domain-specific to carter | ✅ |
| Pipeline fingerprint phrases — No structural copies | ✅ |
| Read for sense — Coherent and grammatical | ✅ |
| Obscure reference in Nevers — Domain-consistent, not obscure | ✅ |

**Word count** is the only failing gate — but it fails by 9 words.

### Word Distribution (current lines and word counts)

| Line | Words | Content |
|---|---|---|
| L3 | 23 | Identity opening — DO NOT CHANGE |
| L5 | 19 | "You carry gold or gravel with the same pace..." |
| L7 | 24 | Address line — "You address the user by the load they carry..." |
| L9 | 18 | Recovery: "When the waybill is illegible..." |
| L11 | 20 | Follow-through: "Before every draw, you walk the traces..." |
| L13 | 21 | Recovery: "When the axle breaks on the grade..." |
| L15 | 21 | Never — domain-specific |
| L17 | 18 | Never — domain-specific |
| L19 | 20 | Never — domain-specific |
| L21 | 25 | Sign-off — longest line |
| **Total** | **209** | |

### Fix Required

Cut **10+ words** from the draft. The spec says "Cut lines, not words" — the cleanest approach is to remove an entire line. You have 10 active lines, minimum is 8, so you can lose up to 2.

**Recommended trim: remove L5** (19 words — "You carry gold or gravel..."). This line describes Dale's impartiality, which is also conveyed in L3 ("bound by the ropes you check, not the sender"). Cutting it saves 19 words, bringing the count to 190 — well within the cap.

**Alternative if L5 is precious:** cut 10–11 words from any combination of:
- L7 (24w): Remove "against the grade" from the quoted phrase → saves 3
- L9 (18w): "a cart on a guess delivers nothing" → "a cart on guess delivers nothing" saves 1
- L21 (25w): Tighten to: `"Your sign-offs mark the leg: \"Load secured.\" / \"Team on the road.\" / \"Delivery made — receipt signed.\"`" → saves 5 (removes "between yard and receiving dock" + 3 instances of "is")

**DO NOT** change the identity opening (L3) — it now passes. DO NOT change L11 again — the T5 already trimmed it.

### Previous History

- **T6 rejection #1:** Identity opening — line 3 jumped into metaphor instead of naming archetype noun. → **FIXED**
- **T6 rejection #2:** Word count 203 > 200. T5 trimmed 4 words but the real count was higher. → Needs further trimming
- **T6 rejection #3 (this one):** Word count 209 > 200. Needs 10+ word reduction.