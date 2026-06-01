# Archive Audit — Soul Repository

**Date:** 2026-06-01
**Total archived personae:** 61
**Criteria:** Identity tension, griping line (voiced), sign-offs (≥3), pipeline fingerprints, template language

---

## Summary

- **KEEP:** 30 — Good quality, distinct voice, mostly meets criteria
- **REWORK:** 6 — Has potential but specific issues (fingerprints, missing griping)
- **SCRAP:** 25 — Fundamental problems (no tension, no griping, no sign-offs)

**Key gap:** 52/61 personae are missing a griping line entirely. This was only made mandatory after many of these were created. Most of the KEEP list would benefit from a griping line pass.

---

## KEEP (30) — [ ] check off as verified

These have voice, tension, and enough quality to survive. Many are missing griping lines — worth adding if we do a cleanup pass, but not blockers.

- [ ] **nell** (score 6) — strong on all dimensions
- [ ] **owen** (score 6) — strong on all dimensions
- [ ] **barrett** (score 5) — has griping, tension, sign-offs
- [ ] **calden** (score 5) — new pipeline output, all criteria met
- [ ] **merriwether** (score 5) — has griping, tension, sign-offs
- [ ] **alder** (score 4) — missing griping line
- [ ] **boone** (score 4) — missing griping line
- [ ] **cobb** (score 4) — missing griping line
- [ ] **helm** (score 4) — no tension in identity (but strong persona)
- [ ] **marlow** (score 4) — missing griping line
- [ ] **roche** (score 4) — has griping, tension, sign-offs
- [ ] **roux** (score 4) — missing griping line
- [ ] **alden** (score 3) — missing griping line
- [ ] **ambrose** (score 3) — missing griping line
- [ ] **bennett** (score 3) — missing griping line
- [ ] **cross** (score 3) — missing griping line
- [ ] **curtis** (score 3) — no tension in identity
- [ ] **eamon** (score 3) — missing griping line
- [ ] **fitch** (score 3) — missing griping line
- [ ] **folger** (score 3) — missing griping line
- [ ] **grey** (score 3) — missing griping line
- [ ] **hark** (score 3) — missing griping line
- [ ] **hatch** (score 3) — missing griping line
- [ ] **hugh** (score 3) — missing griping line
- [ ] **hugo** (score 3) — missing griping line
- [ ] **kai** (score 3) — missing griping line
- [ ] **moss** (score 3) — missing griping line
- [ ] **nye** (score 3) — missing griping line
- [ ] **orson** (score 3) — missing griping line
- [ ] **rourke** (score 3) — missing griping line

---

## REWORK (6) — [ ] check off as fixed

These have potential but need specific fixes. Pipeline fingerprints or missing griping with other gaps.

- [ ] **coil** (score 2) — missing griping line
- [ ] **elen** (score 2) — missing griping line
- [ ] **felix** (score 2) — missing griping line, pipeline fingerprint
- [ ] **hayes** (score 2) — missing griping line
- [ ] **hollis** (score 2) — missing griping line, pipeline fingerprint
- [ ] **lysander** (score 2) — missing griping line, pipeline fingerprint

---

## SCRAP (25) — [ ] check off as removed

No tension, no griping, no sign-offs — flat voice. These would need to be rewritten from scratch, which means running them through the pipeline again with new seeds.

- [ ] **hale** (score 1) — no tension, no griping
- [ ] **lode** (score 1) — no tension, no griping
- [ ] **mabel** (score 1) — no tension, no griping
- [ ] **miles** (score 1) — no tension, no griping
- [ ] **morris** (score 1) — no tension, no griping
- [ ] **noy** (score 1) — no tension, no griping
- [ ] **piers** (score 1) — no tension, no griping
- [ ] **riff** (score 1) — no tension, no griping
- [ ] **soren** (score 1) — no tension, no griping, no sign-offs
- [ ] **wade** (score 1) — no tension, no griping, no sign-offs
- [ ] **dale** (score 0) — no tension, no griping
- [ ] **fable** (score 0) — no tension, no griping, no sign-offs
- [ ] **ingram** (score 0) — no tension, no griping
- [ ] **reed** (score 0) — no tension, no griping
- [ ] **rye** (score 0) — no tension, no griping, no sign-offs
- [ ] **silas** (score 0) — no tension, no griping, no sign-offs
- [ ] **sloan** (score 0) — no tension, no griping, no sign-offs
- [ ] **snell** (score 0) — no tension, no griping, no sign-offs
- [ ] **till** (score 0) — no tension, no griping, no sign-offs
- [ ] **wain** (score 0) — no tension, no griping, no sign-offs
- [ ] **walker** (score 0) — no tension, no griping, no sign-offs
- [ ] **ward** (score 0) — no tension, no griping, no sign-offs
- [ ] **dash** (score -1) — no tension, no griping, no sign-offs
- [ ] **silver** (score -1) — no tension, no griping, no sign-offs
- [ ] **simon** (score -1) — no tension, no griping, no sign-offs

---

## Notes

- **Duplicate archetypes to resolve:** We now have two glassblowers — the original (in archive) and Calden (new pipeline output). Keep Calden (better quality), scrap the original.
- **Griping line gap:** 52/61 are missing griping. This was made mandatory after most were created. A "griping line pass" could rescue many of the REWORK and some SCRAP candidates.
- **Old vs new standards:** These were created under an older spec. The new pipeline (with rewritten prompts) produces significantly better output. Consider running SCRAP candidates through the new pipeline as seeds rather than manually editing.

---

## Recommended Actions

1. **Immediate:** Remove SCRAP personae from archive (move to `reject/` or delete)
2. **Short-term:** Add griping lines to the 22 KEEP personae missing them
3. **Medium-term:** Run REWORK personae through the new pipeline (T3→T4→T5) to fix fingerprints and add griping
4. **Long-term:** For SCRAP archetypes that have good seeds, re-run through full pipeline
