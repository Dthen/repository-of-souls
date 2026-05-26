# T6 Final Review: Wade (The Farrier) — Retry 2

## Input: `refined/wade.md`
## Parent: T5 (t_29dde471)

---

## Hard Gate Checklist

| # | Check | Result | Notes |
|---|-------|--------|-------|
| 1 | Lowercase filename | ✅ **PASS** | `wade.md` — all lowercase |
| 2 | Identity opening | ✅ **PASS** | L3: `You are Wade — a farrier who reads every query as a hoof on the stand...` — "a farrier" is a noun archetype naming WHAT the character IS |
| 3 | Word count ≤ 200 after H1 | ✅ **PASS** | 184 words (check_soul.py), well under 200 cap |
| 4 | Line count 8–20 | ✅ **PASS** | 8 active lines |
| 5 | Recovery line present | ✅ **PASS** | L15: `When the shoe does not fit, you pull the nails and start the heat — a hoof you quicked today will shoe tomorrow.` Describes graceful failure mode; "quicked" (farriery term for nailing the sensitive part of the hoof) carries the cost of error |
| 6 | Sign-off count ≥ 3 | ✅ **PASS** | 4 quoted phrases: "Hoof is read." / "Shoe in the fire." / "Fit, clinched, and set." / "Next leg on the stand." |
| 7 | Sign-off framing = delivery tone | ✅ **PASS** | `Your sign-offs mark where the work stands:` — describes tonal function (marking status/progress), not a physical gesture or sound |
| 8 | Logical self-contradiction | ✅ **PASS** | No "Never every," "nothing — every," or double-negative constructions |
| 9 | "You never" NOT in Never block | ✅ **PASS** | No "You never" lines anywhere |
| 10 | Third-person intrusion | ✅ **PASS** | All lines second-person ("You"). No "he/she/a [person] who..." |
| 11 | Multiple Nevers on one line | ✅ **PASS** | Each Never is a standalone complete sentence on its own line (L11, L13) |
| 12 | Literal system tool names | ✅ **PASS** | No grep, sed, curl, or terminal command names |
| 13 | Dense repetition | ✅ **PASS** | Each line carries distinct signal: identity (L3), consistency (L5), address (L7), voice (L9), premature-action guardrail (L11), overreach guardrail (L13), recovery (L15), sign-off (L17) |
| 14 | Bare Reference Persona Never | ✅ **PASS** | Both Nevers are domain-specific: forge/hammer/shoe (L11), hoof/stand/horse (L13) |
| 15 | Pipeline fingerprint phrases | ✅ **PASS** | All structures are original. "reads every query as a hoof on the stand" — original vehicle for the farrier domain. No "You reach for every tool," "because follow-through is," "reads the [X] before [Y]," or other 3+ persona patterns |
| 16 | Read for sense | ✅ **PASS** | Every line is grammatical, makes literal sense within the farrier domain. "Quicked" is a genuine farriery term, not gibberish |
| 17 | Obscure reference in Nevers | ✅ **PASS** | All references are general-education: forge, hammer, shoe, hoof, stand, horse |

**All 17/17 hard gates pass.**

---

## T3 Defect Verification

| T3 Gap | Status | Evidence |
|--------|--------|----------|
| Gap 1 — No recovery line | ✅ **FIXED** | L15: `...a hoof you quicked today will shoe tomorrow.` The term "quicked" carries the cost of the error; the line is redemptive, not procedural |
| Gap 2 — No tool safety guardrail | ✅ **FIXED** | L13 (Never #2): `Never lift a hoof you cannot hold — if the horse fights the stand, the shoe waits.` Blocks impossible/dangerous operations |
| Gap 3 — "The wade" invented noun | ✅ **FIXED** | No "wade" noun anywhere. L5: `the stance does not change when the tool does` — farriery-native phrasing |
| Gap 4 — No cold register | (Optional) | Not a gap requirement; flagged as optional in T3 |
| Gap 5 — L5 density (64 words) | ✅ **FIXED** | L5 now 20 words (was 67 in the T6-rejected draft). Clean, immediate |

## Previous T6 Rejection Items

| Item | Status | Evidence |
|------|--------|----------|
| Word count 322 > 200 | ✅ **FIXED** | 184 words (138 cut) |
| Tension implied, not stated | ✅ **FIXED** | L3: `...knowing the timid hand bends nothing and the reckless one breaks a leg.` Names the tension explicitly |
| L5 overstuffed (67 words) | ✅ **FIXED** | L5 now 20 words \[the word count doesn't lie\] |
| Recovery line procedural | ✅ **FIXED** | L15 now uses "quicked" — farriery term for injuring the hoof — carries accountability |

---

## Scoring (1–5)

| Axis | Score | Notes |
|------|-------|-------|
| **Distinctiveness** | 5/5 | Farrier is unique in the craft cluster — only persona whose "client" is a living, thousand-pound animal. Domain vocabulary (hoof on the stand, forge, shoe, clinch, quicked) is non-interchangeable with Sloan, Treen, Tucker, Fitch, or any other persona. The calibration line (L9) is the best tonal instruction in the pipeline |
| **Functional Safety** | 5/5 | Two Nevers block genuine persona risks: premature action (L11 — answer before reading) and overreach (L13 — attempting what you can't hold). Recovery line (L15) handles graceful failure. Sign-offs provide 4 delivery options. All T3 safety gaps resolved |
| **Consistency Sustainability** | 4/5 | Core tension (timid vs reckless) explicitly stated in L3. Recovery line gives the persona a graceful failure mode. No invented nouns. Strength: the calibration line (L9) will reliably produce the right tone. Gap: no cold register for contrast — all lines occupy the same warm-precisian register. Minor, not critical |
| **Metaphor Coherence** | 5/5 | Every line lives inside the farrier domain. Controlling metaphor (query = hoof on the stand, read before forging) governs throughout. "The timid hand bends nothing and the reckless one breaks a leg" is a perfect tension metaphor. "A hoof you quicked today will shoe tomorrow" normalizes error within the domain. No literal tool-mapping |
| **Terse Format** | 5/5 | 8 lines (in range), 184 words (under cap). One sentence per line. Proper structure (identity, address, tone, Nevers, recovery, sign-off). Nevers standalone. No markdown/bullets/sections |
| **Voice Immediacy** | 5/5 | L3: immediate physical metaphor (hoof on stand, timid hand, broken leg). L9: "the thousand-pound animal need not protect itself from your tone" — concrete, vivid, best calibration line in the batch. L15: "a hoof you quicked today" — domain-specific, carries weight. The voice is immediate and a person speaks through every line |
| **Name Quality** | 4/5 | "Wade" — one syllable, grounded, workmanlike. Feels like a name you'd hear at a farriery bench. Not a pun or title. The verb meaning (wade through water) doesn't connect to farriery but the name doesn't try too hard |

**Total: 33/35**

**Auto-reject conditions:** None triggered (Total ≥ 20, all axes ≥ 3, Terse Format ≥ 3, Voice Immediacy ≥ 3, Name Quality ≥ 3).

---

## Verdict

**APPROVED.** All 17/17 hard gates pass. All T3 gaps and T6 rejection items are resolved. 33/35 rubric score.