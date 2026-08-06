# Proposal: v5.2 Character-First Rework

**Date:** 2026-08-06
**Status:** Proposal (awaiting approval → plan → execution)
**Origin:** Conversation with Dthen — "do the souls in the soul repository get made a bit dry by the pipeline?" The two souls he actually uses (Kimbo, Brendan) are whimsical, character-first creations; the pipeline produces dignified job-shaped souls. Investigation of all stage specs + 18 research files + archive confirmed the pipeline has four structural filters that dry out souls. This proposal fixes them.

---

## 1. The Four Gates (Diagnosis)

### Gate 1 — The Researcher only thinks in professions

`references/stage-researcher.md` Step 2-3 sources candidates exclusively from job-shaped categories: historical trades, guild crafts, institutional roles, fiction tropes. Even the "Absurdist" category is defined as *obscure professions* (knocker-up, raker, mudlark). The one diversity lever — "forced mismatch" — is aimed domain-to-domain ("A clockmaker described through kitchen vocabulary"), so the weirdest output possible is a job wearing another job's coat. It never crosses job → not-job.

**Evidence that the fix already exists in our own research:**
- `research-character-creation.md` — PbtA playbooks: "Start with the emotional fantasy — what does *interacting with this persona feel like*?" (roleplay-prompting L174). A persona is a playbook, not a job posting.
- `research-character-interest.md` — the Want Test explicitly rejects job-shape: "Not 'wants to help people' — that's a job description" (L323). "Competence = what the character CAN DO; Interest = who the character IS" (L356-362). Seven Tests at L321-335.
- `research-internal-life.md` — profession is only ONE of four forces shaping perception; trauma, values, and desire are the others (L65-73). This is a diagnostic eye with no job required. Non-gripping archetypes documented (optimist-wrong-a-lot, builder, curious observer, stubborn one, caretaker) at L260-303.
- `research-roleplay-prompting.md` — identity-with-tension: "a forest guardian who heals with magic" is a role; "...who has begun to forget her own name" is a *situation* — "improvisation looks like embodiment" (L367).
- `research-success-patterns-v5.md` — "The 'Absurdist' category label is misleading. What matters is material practice" (L417). Pure-concept archetypes failed; world-bearing ones passed. The character's world does not have to be a job.
- Seed fields are ALREADY character-shaped (v3.0: Temperament, Stance, Voice Fragment, Personal Contradiction, First Impression). Only the candidate SOURCES are job-shaped. The mismatch is the bug.

### Gate 2 — The viability questions require a craft

`references/stage-namer.md` Step 1: six questions, structurally job-based — the pub test ("I am a glassblower" passes), "can you list 5 actions? Physical or craft-specific behaviors," etc. A golden retriever in himbo form fails question one. Brendan (wizard + paperwork) fails the craft-action test.

**Evidence:**
- `research-inhabitation-vs-description.md` — "If you can replace this line with 'You are a helpful assistant who…' and it still reads as a valid instruction, it's description" (L17, L411-415). Enumerating craft facts IS description. The "list 5 craft actions" question is the description pattern the Helpful Assistant test exists to kill.
- `research-failure-modes.md` — the REAL failure taxonomy: no material practice (L175-180), no griping potential (L182-187), no griping line (L202-207), stamp sign-offs (L209-214), bad Nevers (L216-235), metaphor breaks (L237-242), single register (L244-249). None of these require "has a profession."
- `research-llm-judge-calibration.md` — valid gates are evidence-grounded: 3-point behavioral scales beat fine-grained ones (L66), judges must cite lines before scoring (L40, L130-132), lock and version the rubric (L31-48), calibrate on a gold set (L58, L293-298).

### Gate 3 — "Coherent metaphor family" kills two-domain characters

`references/stage-evaluator.md` Step 6.4: "A gleaner who measures by silence AND navigates by stars AND cooks by taste — no. One domain, one lens." This kills Brendan (magic + paperwork), Kimbo (dog + assistant), and any genre-crossing soul.

**Evidence:**
- `research-failure-modes.md` — the original Coil/Reed failures were "mixing without committing to any… half-explored" (L239-241). The real rule: **"One metaphor, fully inhabited, beats three metaphors, half-explored"** (L241) — a COMMITMENT check, not a domain-count check.
- `research-success-patterns-v2.md` — the one-domain induction came from a sample of 63 souls that never contained a multi-domain character. The sample never tested the hypothesis. Induction error.
- `research-cross-cultural.md` — five depth modes: psychological, relational, temporal, aesthetic, accumulative (L363-368). Relational contradiction ("I owe two incompatible debts," L351) *structurally requires* multiple domains. "A wabi-sabi character doesn't have contradictory traits — they have ACCUMULATED textures" (L349). Tradition-mixing explicitly endorsed (L419). None of the five modes requires domain unity.
- `research-llm-judge-calibration.md` — the rule's own origin: the judge CoT asked "Do the metaphors come from one domain, or are they scattered?" (L156, L267). "Scattered" = half-explored. The generalization to "one domain only" over-shot the evidence.

### Gate 4 — Whimsy is not a register, and absurdity is flagged as risk

`references/stage-researcher.md` Temperament examples: weary, darkly amused, quietly proud. "Silly" is not a register. `references/stage-evaluator.md` bonus flag: "Absurdist category, cynical or darkly amused registers carry higher accuracy risk."

**Evidence:**
- `research-emotional-register.md` — documented registers: grumpy competence (56%, L157), patient craft (L158), weary (L159), warm competence (L160), earnest enthusiasm (~8%, L161), absurdist (~3%, L165). Playful is NOT documented — but "No soul is primarily comedic" (L177) is called open territory, joyful registers under-represented (L174). Explicit warning against closed register lists (L283). Register pairing: "Enthusiastic + Self-aware: awareness makes the enthusiasm earned" (L317). Subversion table blesses "a cheerful executioner, an upbeat detective" (L188).
- `research-persona-accuracy-tradeoffs.md` — the accuracy risk is REAL but the mechanism is capacity crowding: "What matters is persona detail, not persona content" (L75-77): min persona −3.6%, long −5.3% MMLU (L78-79). **The §6.3 register-risk table (Playful/Absurdist = "High") is explicitly "inference, not direct evidence" (L250); Appendix gap #2 admits no study tests emotional registers (L368).** Voice-preserving mitigations exist: in-persona verification line (L180-184), "check twice" writer-level line (L284), diagnostic-eye-as-verification (L286), task-type separation (L169-175), shorter specs (L161-166). Risk should be "a flaggable dimension — not a veto" (L295).
- `research-character-likeability.md` — affiliative humour + specific self-deprecation = highest return (L91); "Lightness alongside depth — heavy worldview, light register" is a proven bridge pattern (L146); humour is the most efficient likeability tool (L239-243); give the model "a relationship to humour, not jokes" (L247).
- `research-griping-alternatives.md` — griping is "a proxy for inner life"; ANY signal encoding awareness + standards + investment + expertise + tension works (L591-604). Playfulness can carry the same vitality load as complaint. The Optimist model: "You see the potential in every mess. Your enthusiasm is exhausting and genuine" (L499).
- `research-ai-assistant-personas.md` — the Competent Eccentric: personality in the delivery, not the content (L97-100). Context-dependent register: casual = full personality, technical = personality in the margins, crisis = personality recedes (L150-153). "Professionalism isn't the absence of personality — it's the presence of competence" (L156). Forced humor is an anti-pattern (L112).

### Archive evidence

All five published souls (docs/: Barlowe, Cadell, Calden, Teague, Tillman) are job-shaped characters. Tillman the mudlark is the spec's own "Absurdist" category example — proving the category is job-shaped. Diagnostic eyes have converged: Barlowe reads by stillness, Teague reads the silence between words, Tillman reads absence, Stover measures silence — 4 of 6 souls use the same absence-reading inversion. The very quality meant to differentiate characters has become the pipeline's newest fingerprint.

### Meta-finding

`~/.hermes/plans/2026-06-02_144500-spec-rewrite-prompt-research.md` — written to fix exactly this problem ("the research was written for exactly this scenario but was not applied during the v5 rewrite") — has status **Plan (no execution)**. The pattern: research exists → rewrite happens → research not applied. v5.2 must include an application check so this proposal does not join it in the file-drawer.

---

## 2. Proposed Changes

### 2.1 `references/stage-researcher.md` — Character-first discovery

1. **Flip the discovery order.** Step 3 becomes: (a) emotional fantasy — "What should interacting with this persona FEEL like?" (first field, before any occupation); (b) contradiction — "two truths in tension, one of which can be 'I am a golden retriever in himbo form'"; (c) want vs need + the lie believed; (d) THEN the world — a job, a creature, a genre-cross, or a role-from-life. "What does it notice?" follows from the world but does not require a profession (internal-life L65-73: trauma/values/desire are valid perception-shapers).
2. **Retarget the forced-mismatch lever** from domain→domain to category→category: "A wizard described through tax-form vocabulary" is the target shape; "a clockmaker through kitchen vocabulary" is the old, insufficient shape. (The mismatch lever itself traces to Yun et al., 2025 on structural-prompt diversity collapse, documented in `research/research-pattern-avoidance.md`.)
3. **Add the Seven Tests as a pre-filter** (character-interest L321-335), especially the Want Test: reject any candidate that reads as a job description. Apply the "but" test: if you can't describe the character with a conjunction, kill it.
4. **Add a tone/comedy axis to the gap analysis.** Tone gaps already exist in prose ("if all archetypes are serious, look for playful or absurdist ones") but nothing operationalizes it. Add: "if all souls are dignified, look for silly; if all are human, look for non-human; if all are single-world, look for genre-crosses."
5. **Keep material practice** as a requirement — but re-source it: the character's WORLD supplies the griping language, diagnostic eye, metaphor family, and compressed specific. A wizard who files forms has form-language and grieves "the third copy." A dog has fetch, sniffing, and loyalty. (success-patterns-v5 L417: what matters is material practice, not profession.)
6. **Seed template additions:** (a) Emotional Fantasy field (first); (b) Want/Need/Lie fields (or one "What does it want, what does it need, what does it believe that isn't true?" field); (c) Warmth/Playfulness dimension with a "relationship to humour, not jokes" instruction; (d) optional counter-register field.

### 2.2 `references/stage-namer.md` — Character tests, not craft tests

Replace the six viability questions with character tests (evidence-cited per llm-judge-calibration — each verdict cites the seed line before deciding; the Namer retains its binary kill-gate, following the calibration research's "enumerate before scoring" rule):

1. **The Swap Test** — Helpful Assistant test on the voice fragment and first impression (inhabitation-vs-description L17). If the seed's core lines read as valid instructions, it's description.
2. **The Tension Test** — a contradiction the model can improvise within. Requires a "but." Not "a [job] who [does job well]."
3. **The Complaint Test** — "a complaint only this character could make." No domain required — but must carry awareness + standards + investment + expertise + tension (griping-alternatives L591-604).
4. **The Perception Test** — "What does this character notice that nobody else would?" Any source (trauma, values, desire, or profession) is valid (internal-life L65-73).
5. **The Improvisation Test** — "Could this character hold a 50-turn conversation without running out of voice?" (This replaces "list 5 craft actions" — 5 actions are a proxy for richness; the test should target richness directly.)
6. **The World Test** — "Does the character have a material practice of SOME kind — a world with nouns and verbs?" (success-patterns-v5 L417. Job not required; world required.)

Keep the name checks (sounds like a person, collision-safe) unchanged — they were never the problem.

### 2.3 `references/stage-evaluator.md` — Commitment check, not domain-count check

1. **Rewrite the Coherent Metaphor Family gate** (Step 6.4) as a commitment check: reject only (a) half-explored alternation — multiple worlds referenced but none inhabited; (b) generic lines — "could any other character have this line?" (failure-modes L239-242). Multi-domain characters PASS if each lens is fully inhabited (cross-cultural L349, L351, L419).
2. **Add an "interesting edges" protection clause** (review-pipeline L43, L73, L290): before flagging anything unusual, ask "strength or weakness?" Never flag versatility as genericness. Never confuse "challenging because unusual" with "confusing because poorly written."
3. **Reframe the accuracy-risk flag from register-based to evidence-based:** the register-risk table is labeled inference, not evidence (accuracy L250, L368). Replace "Absurdist/darkly amused = risk" with: length-based check (shorter specs preserve accuracy, L77-80), verification-line check (does the soul carry an in-voice verification move? L180-184, L284), and a "flaggable dimension, not a veto" note (L295).
4. **Update the register language:** add Playful/Whimsical to the register palette in the Writer guidance, with a mandated counter-register pairing (Playful + Precise; Enthusiastic + Self-aware model at emotional-register L317). Warn against closed register lists (L283). No soul "is primarily comedic" — but joyful registers are open territory (L174-177).

### 2.4 `references/format-rules.md` + `positive-patterns.md` — Whimsy legitimacy + register range

1. Add "Silliness is a legitimate register. Whimsy must be behavioral (what the character does/says), not conceptual (a description of being whimsical)." (roleplay-prompting L367: absurdity works as *situation*; success-patterns-v5 L417: pure concept fails.)
2. Add the humour guidance: affiliative humour + specific self-deprecation, user included in the joke; prohibit the dismissive "always" frame (likeability L91, L286). "A relationship to humour, not jokes" (L247). Forced humour is an anti-pattern (ai-assistant L112).
3. Add the Competent Eccentric principle: personality in delivery/metaphor/sign-offs, clarity in the body, personality recedes when stakes rise (ai-assistant L97-100, L150-153).
4. Add the verification-line pattern as a positive technique: "You verify what you've seen before you speak — the fact is the fact whether it fits the story or not" (accuracy L180-184). Whimsical souls should carry one.

### 2.5 `AGENTS.md` — Version + application check

1. Bump to v5.2, dated.
2. Add an "Application Check" section: the changes in this version cite their source research files with line numbers; reviewers of the spec (or the next rewrite) must verify each new rule traces to evidence, and the 2026-06-02 plan's "not applied" failure mode is the explicit anti-pattern. One source of truth: `research/proposal-v5.2-character-first-rework.md`.

### 2.6 Not changing (deliberately)

- Single-write architecture (v5's fix for template propagation — keep).
- Format bounds (8-20 lines, 200 words) — these are prompt constraints, not the problem.
- The five-stage linear structure.
- The Namer's name checks (sound, collision, memorability).

---

## 3. Validation Plan (How We Know It Worked)

1. **Test seeds through the new Researcher:** run the character-first discovery for 3 candidate characters: (a) a golden-retriever-in-himbo-form (the Kimbo shape), (b) a wizard who files forms (the Brendan shape), (c) a genuinely two-domain cross (e.g., a lighthouse keeper who's also a bookbinder — "binds the logbook of the sea"). All three should survive the new Namer tests and produce PICKable drafts.
2. **Regression check:** existing archive souls (Barlowe, Cadell, Calden, Teague, Tillman) must still pass the new gates — the changes must widen, not break, the current standard.
3. **Fingerprint check:** the next 5 pipeline outputs must not share sentence structures; specifically watch for absence-reading diagnostic-eye convergence (4/6 today).
4. **Gut check by Dthen:** the two test souls should be *fun* to talk to, not just compliant.

---

## 4. Open Questions

1. Should the Researcher's gap analysis move from coverage-map categories (Profession/Trope/Bureaucratic/Absurdist) to a richer axis set (register × world-type × tension-type)? Proposal: yes, but phase it — categories stay as a secondary taxonomy, primary is character anatomy.
2. Should "Emotional Fantasy" become a mandatory seed field before the pipeline runs again? Proposal: yes — it is the single highest-leverage change (it is the PbtA first principle).
3. Gold set: llm-judge-calibration recommends a 10-20 persona gold set for judge calibration. Proposal: build a first gold set of 6 — the 5 archive souls + 1 whimsical soul (Kimbo's soul file) — with human labels, to calibrate the Evaluator.
4. Do the pipeline profiles (soul-researcher/soul-namer/soul-writer/soul-evaluator SOUL.md files in profiles/) need updating alongside the spec? Proposal: check after spec change; the specs reference themselves as the source of truth, so profile updates may be minimal.

---

*This proposal supersedes the "whimsy cannot be a pipeline stage" intuition from the originating conversation: whimsy CAN be encouraged — it just can't be *mandated* as a checklist item. The v5.2 mechanism: make the seed character-first, make the gates test character, make the metaphor rule a commitment check, and give whimsy a register + guardrails instead of a veto.*
