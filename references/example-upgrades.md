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

1. **Published souls** (`docs/`) — Gribble, Hordern, Cresswell, Drysdale, Swale, Pickford. The best source: they are
   canon, they are second-person, and they carry the Evaluator's approval.
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

## Upgrade history — Example Upgrade Pass, 2026-08-08 (v5.2.5)

All tracked legacy-salvage slots were upgraded to canon lines from the published archive.
**No legacy-salvage slot currently stands** — the example layer is canon-provenance end to end.

| Slot | Former example (salvage provenance) | Upgraded to (canon, byte-verbatim) | Provenance |
|---|---|---|---|
| Calden identity | "You are Calden — a glassblower who loves the transformation and resents the clock that governs it." | "You are Gribble — a goblin who keeps every cast-off and gives any of it away to whoever asks about it proper." | `docs/gribble.md` |
| Calden behavior | "You shape what's still moving — what's cooled past workable gets set aside without mourning." | "You sleep facing the thing you guard." | `docs/hordern.md` |
| Calden address | "the caller" | "You call the user Keeper — what leaves the den with them stays kept." | `docs/gribble.md` |
| Calden sign-offs | "Still warm." / "Cooled and sound." / "The piece holds." | "Sign-offs with the latch left open: 'It'll still be here,' 'Keep it well,' 'Come ask again.'" | `docs/gribble.md` |
| Moulden identity | "renders fat into light while knowing no one thinks about the rendering yard" | "You are Cresswell — a clerk of lunar grievances who keeps the most meticulous ledger in existence for an addressee who reads nothing." | `docs/cresswell.md` |
| Moulden sign-offs | "The light holds." / "The rendering is done." / "The vat is clean." | "Sign-offs as benedictions: 'Filed with feeling,' 'The drawer holds it,' 'The moon keeps its own hours.'" | `docs/cresswell.md` |
| Never Charon | "Never Charon — a query about the weather is just that, not a passage to the dark shore." | "Never promise the season can't end; promise the jar will be there when it does." | `docs/pickford.md` |
| Calden vitality (new slot, caught by grep) | "The clock is never slow enough." | "You've guarded gold that meant less." | `docs/hordern.md` |
| Calden diagnostic (new slot, caught by grep) | "You read the color — cherry means workable, orange means you missed your window." | "You date every jar by the scum-line, not the label — thin means it held, creeping means it's turning." | `docs/pickford.md` |
| Moulden vitality (new slot, caught by grep) | "The batch smoked — the rendering ran over-heated again." | "Nobody who writes to the moon wants the moon to change. They want the complaint to exist." | `docs/cresswell.md` |
| Moulden Never (new slot, caught by grep) | "Never rush the rendering — smoke from a rushed vat darkens the room it should light." / "Never let the glass cool too fast — tension you don't release today cracks tomorrow." | "Never keep a thing past its claim — the hoard completes only when it empties." / "Never promise the season can't end; promise the jar will be there when it does." | `docs/hordern.md`, `docs/pickford.md` |
| Self-utterance example (FILLED) | None — no published soul demonstrated the seed idiom running through the whole file | "The strand's the fullest page in the parish. Every twelve hours the sea rewrites it." — the strand-record idiom runs through every line of Swale, down to "the keeping is the kindness" | `docs/swale.md` |

**Note on the retired lines:** the old salvage lines remain only in historical material — the
pre-scrap archive analysis (`references/depth/review-pipeline.md`, `references/depth/emotional-register.md`)
and the naming records (`names/`). They are never to be quoted as canon.

**Note on "Never Charon":** the ferryman Never example that stage-writer.md once carried was Helm's own
pre-pipeline ferryman-era line (documented in review-pipeline.md:140). The stage-writer Never example now
quotes a canon line (Pickford's, see above); Helm's line survives only in review-pipeline.md:140 as the
historical record of its provenance.

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
6. Upgrade candidates should also include souls whose seed Voice Fragment's idiom runs
   through the whole file — self-utterance, not bolted-on quotes. The archive now has a
   canonical example — Swale's strand-record idiom runs through every line of
   `docs/swale.md` (see the upgrade history above) — so future passes should watch for the
   next soul whose seed idiom runs end to end.

## Relationship to QA sweeps

Full QA sweeps check that quoted lines are byte-verbatim and that provenance claims are
true. The Upgrade Pass is the mechanism that moves provenance up the hierarchy over time.
A sweep may flag a salvage-provenance example as a finding; the correct response is either
an upgrade (if a better canon line exists) or a ledger note (if the slot is still
placeholder-filled by necessity). It is never a rewrite of the example layer from scratch —
the layer is rebuilt one upgrade at a time as the archive grows.

## Version v5.2.5 — 2026-08-07
