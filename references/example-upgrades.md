# Example Layer — Upgrade Pass (provisional by design)

## The principle

The spec has not yet accumulated enough genuinely excellent example lines to fill every
teaching slot with canon. The example layer — the personae and lines quoted as craft
examples in the stage specs and depth files — is therefore **provisional by design**:
examples stand in for future excellence, and they are **upgraded in passes** as better
examples get written. A placeholder example that teaches the right lesson is better than
no example; a placeholder that has been superseded by a better canon line is a liability
and must be replaced in the next pass.

This file is the ledger and the procedure. It exists so the example layer is honest about
its provenance and so upgrading is mechanical, not archaeological.

## Provenance hierarchy (what examples SHOULD be quoted from)

1. **Published souls** (`docs/`) — Gribble, Hordern, Cresswell. The best source: they are
   canon, they are second-person, and they passed the checker.
2. **Reference personae** (`references/reference-personae.md`) — Kimbo, Brendan, Stover,
   Barlowe. Hand-made standards; quote them verbatim.
3. **Research-derived example personae** — characters invented inside the depth files
   (Helm, Nell, Sera, Mara, Lin, Idris, Orin, Maren, Tamsin, Cobb, Fletcher). They are
   teaching props, not canon; fine to use, cheapest to replace.
4. **Legacy salvage** — lines whose provenance is the scrapped v5-era material
   (Calden, Moulden). **Not canon.** These stand ONLY because no canon line yet exceeds
   them in their teaching slot, and they are tracked in the ledger below. They must never
   be quoted as if they were archive canon, and they are the first candidates for upgrade.

**Hard rule:** never canonicalize content from scrapped or legacy material. Salvage may
stand temporarily as a *marked example*; it never becomes canon. Provenance claims in the
spec must always trace to `docs/` or `reference-personae.md`.

## Current legacy-salvage slots (upgrade targets)

| Slot | Current example (salvage provenance) | Where it lives | Upgrade target when written |
|---|---|---|---|
| Calden identity | "You are Calden — a glassblower who loves the transformation and resents the clock that governs it." | appears in 7 live files; Calden is mentioned in ~17 | A published soul's identity line (Gribble/Hordern/Cresswell) |
| Calden behavior | "You shape what's still moving — what's cooled past workable gets set aside without mourning." | depth files (2) | A published soul's behavioral line |
| Calden address | "the caller" | AGENTS.md, stage specs, and depth files | A published soul's address term |
| Calden sign-offs | "Still warm." / "Cooled and sound." / "The piece holds." | depth files (3) | A published soul's sign-off set |
| Moulden identity | "renders fat into light while knowing no one thinks about the rendering yard" | depth files (4 live files carry the full line) | A published soul's identity line |
| Moulden sign-offs | "The light holds." / "The rendering is done." / "The vat is clean." | depth files | A published soul's sign-off set |
| Never Charon | "Never Charon — a query about the weather is just that, not a passage to the dark shore." | stage-writer.md:213 (a "generic ferryman" Never example); Helm's pre-pipeline line, documented in review-pipeline.md:140 | A published soul's Never line |
| Quoted-speech example | None yet — the archive has no published soul whose seed Voice Fragment is preserved and densified as quoted in-voice speech (e.g. Drysdale's fragment with its dropped sting restored) | stage-writer.md "The Seed's Words Are the Spine"; stage-evaluator.md Step 1.5 | A published soul's seed fragment preserved + densified as quoted speech |

**Note on "Never Charon":** the ferryman Never example in stage-writer.md:213 is not an
anonymous archetype prop — it is Helm's own pre-pipeline ferryman-era line (documented in
review-pipeline.md:140). It therefore carries legacy-salvage provenance and is tracked in
the ledger above; the stage-writer example that presents it as a generic ferryman Never
actually reproduces Helm's old line.

## When to run an Example Upgrade Pass

1. **After every successful publish** — a new soul in `docs/` is the most likely source of
   a better example. Before the next spec version bump, check its lines against the ledger.
2. **After every seed that delights** — a hand-written or Researcher seed that Dthen keeps
   is a candidate for the example layer even before it publishes.
3. **Before every spec version bump** — the audit is cheap and the version stamp forces the
   cadence.

## The pass procedure

1. Read the ledger above (and grep for Calden/Moulden to catch new slots).
2. For each slot, ask: does any line in `docs/` or `reference-personae.md` teach this
   lesson better — same craft point, more character, less template?
3. Replace the example **verbatim** (quotes must byte-match their source), update the
   ledger (remove the slot or mark it upgraded), and keep every citation intact.
4. If a new soul's line is promoted into the example layer, note it in the ledger as
   canon-provenance so future passes know it is no longer a candidate for replacement.
5. If no canon line exceeds the placeholder yet, leave it and note "still standing" —
   the pass is about the layer's drift toward canon, not about churn for its own sake.
6. Upgrade candidates should also include quoted in-voice lines — a seed fragment
   preserved and densified as quoted speech. The archive currently has none to quote,
   so this pass must produce them before the layer can canonize them; the upgrade pass
   after the next publish should check for the first one (see the quoted-speech slot
   in the ledger above).

## Relationship to QA sweeps

Full QA sweeps check that quoted lines are byte-verbatim and that provenance claims are
true. The Upgrade Pass is the mechanism that moves provenance up the hierarchy over time.
A sweep may flag a salvage-provenance example as a finding; the correct response is either
an upgrade (if a better canon line exists) or a ledger note (if the slot is still
placeholder-filled by necessity). It is never a rewrite of the example layer from scratch —
the layer is rebuilt one upgrade at a time as the archive grows.

## Version v5.2.5 — 2026-08-07
