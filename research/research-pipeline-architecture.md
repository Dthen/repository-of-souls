# Research Brief: Workflow Automation Patterns for Creative Pipelines

**Date:** 2026-06-01
**Scope:** Architectural patterns for the soul-repository persona-generation pipeline (T1→T2→T3→T4→T5→T6)
**Sources:** Hermes Kanban documentation, agentic workflow literature, CI/CD pipeline patterns, LLM evaluation infrastructure, stage-gate NPD research, and multi-agent topology analysis.

---

## 1. Pipeline Architectures for Creative Workflows

### 1.1 Linear Chain (Current Pattern)

The soul-repository currently uses a strictly sequential six-stage chain:
```
T1 (Researcher) → T2 (Namer) → T3 (Writer) → T4 (Reviewer) → T5 (Refiner) → T6 (Final Reviewer)
```

**Strengths:**
- Simple to reason about and debug — execution log is a list
- Natural handoff boundaries with clear artifact ownership
- Works well when each stage is genuinely dependent on the full output of the previous

**Weaknesses:**
- No parallelism means wall-clock time for one full cycle = sum of all stage latencies
- No feedback loops — downstream learning does not reach upstream (T6 rejections do not inform T1 seed selection)
- Cascading errors: a bad T3 draft poisons T4→T5→T6 regardless of effort invested
- Single point of failure per stage — one bad worker assignment loses the entire seed

**Research finding:** Linear chains "break at scale" (Tian Pan, 2026). In agentic systems, linear execution is appropriate only for genuinely unparallelizable dependencies — and many creative pipeline dependencies are weaker than they appear.

### 1.2 DAG (Directed Acyclic Graph)

A DAG allows fork/join patterns:
```
T1 → T2 → T3
           ↓
      T4a (Format) ─┐
      T4b (Voice) ──┼→ T5 (Aggregate) → T6
      T4c (Safety) ─┘
```

**Applied to our pipeline:**
- T4 (Reviewer) could split into parallel reviewers: one checks compliance, one checks voice, one checks metaphor coherence
- T5 (Refiner) aggregates multi-source critiques instead of reading a single critique

**Academic backing:** DAG-first agent orchestration is becoming default practice (Hashmap/Medium, 2020; Tian Pan, 2026). By separating independent tasks and optimizing execution order, DAGs minimize latency compared to sequential execution.

**Risk:** DAGs make execution "harder to trace visually" — a linear chain's execution log is a list; a DAG's is a graph. For debugging the occasional failure, this adds cognitive overhead. However, for a well-documented pipeline with clear artifact directories, this is manageable.

### 1.3 Swarm / Parallel Fan-Out

The Map-Reduce pattern for creative work:
1. **Map:** Dispatch N parallel workers at the same stage (e.g., 3 writers for the same seed)
2. **Reduce:** Aggregate or select the best output

**Application to soul-repository:**
- Run T3 (Writer) in triplicate, sending the same seed to three `soul-writer` instances
- Run T4/T6 in parallel against all three drafts
- Select by consensus score or pick the single highest-scored draft to advance

**Evidence:** Anthropic reports "90.2% improvement over single agent" on research benchmarks using multi-agent collaboration. The swarm pattern trades token cost for quality — exactly the right trade when final artifacts are durable assets (like archived personae). The cost of 3x writing is negligible compared to the cost of a bad soul in the archive.

**Warning from Wasowski (2026):** Without deliberate topology, multi-agent systems can burn massive budgets ($47k / 11 days in infinite loops). Swarm requires hard ceilings (max iterations = 1 per writer instance, no recursive dispatch).

### 1.4 Sequential with Feedback Loops

The current pipeline has a *local* feedback loop (T6→T5 retry), but no *global* feedback loop. Architectural improvement patterns:

**T6→T2 loop:** When T6 rejects a name, it already loops back to T2 via the rename chain. This is the only cross-stage feedback that currently exists.

**T6→T1 loop (missing):** When T6 rejects on structural grounds (same flaw across three retries), this indicates the seed itself may be flawed. The researcher should learn that "middle manager" archetypes produce structurally weak personae. Currently, this knowledge evaporates with each pipeline run.

**Recommended pattern:** Add a `learning.md` file that T6 appends to after each rejection, and T1 reads at the start of each research cycle. This creates structural feedback without making the pipeline non-acyclic.

---

## 2. Persistent Feedback / Learning Across Pipeline Runs

### 2.1 The Current Gap

The soul-repository pipeline is stateless across runs. T1 (Researcher) does read `archive/` and existing `drafts/` for novelty checking, but:
- There is no record of *which seeds produced failures*
- There is no tracking of *which archetypes repeatedly fail T6*
- There is no accumulation of *which name patterns correlate with low Name Quality scores*
- The `research-success-patterns.md` document exists but is manually maintained, not automatically updated

### 2.2 Patterns from the Literature

**Memory-Augmented Pipeline:** Masquieira (2026) describes "memory-augmented" pipelines where "every bug makes the system smarter." A structured log (`failure-log.md`) accumulates:
- Seed archetype → rejection reason mapping
- Retry count histogram by archetype
- Score delta between T4 and T6 (when T4 passes but T6 rejects, the T4 rubric may be miscalibrated)

**Reinforcement Learning from Feedback:** APIGen-MT (2025) uses "reflection and improvement based on validation results" to progressively generate better outputs. Applied to our pipeline: accumulate T6 scores per archetype and use them to weight seed viability rankings.

**LLM-as-Judge Calibration:** The LMSYS Chatbot Arena methodology uses pairwise comparison with Elo ratings. Applied to our pipeline: accumulated T6 scores could produce archetype Elo ratings, allowing T1 to discard archetypes with proven low scores before investing T3→T6 compute.

### 2.3 Concrete Recommendation

Create `references/failure-patterns.md`, a machine-writeable log (not prose) with this schema:

```yaml
- seed: "the-middle-manager"
  archetype: "corporate-middle-manager"
  domain: "bureaucracy"
  outcomes:
    - attempt: 1
      failed_gate: "Name Quality"
      score: 18
      final_disposition: "archive/reed.md"  # eventually passed after rename
    - attempt: 2
      failed_gate: "Griping Line Present"
      score: 16
      retry_count: 3
      final_disposition: "reject/curtis.md"
  composite_rating: "high-risk archetype — weak voice potential"
```

T1 reads this at startup and weights archetype novelty by composite survival rate.

---

## 3. Quality Gate Patterns

### 3.1 Pre-Flight / Viability Gate (Missing)

The current pipeline invests T3→T6 effort into every seed. No gate answers "Is this seed even viable?" before T3 begins writing.

**Pre-flight patterns from literature:**
- **CI/CD pre-flight checks:** Run lightweight format/schema validation before expensive tests
- **ML pipeline pre-checks:** Data quality gates before training; training gates before evaluation
- **Agentic input router:** Classify input before processing and send to the specialist handler

**Application to soul-repository:**
A T0 "Viability Screener" stage should run before T3 (ideally before T2, even). It checks:
- Does this archetype have natural gripe potential? (The single strongest quality predictor)
- Does the metaphor family have enough texture for 50+ messages?
- Is the domain populated with concrete tools/materials/rhythms?
- Does the archetype already exist in archive with >0.5 overlap? (Stricter than current novelty check)

This screener could be a simple prompt-completion that outputs `GO / HOLD / KILL` — seconds of compute versus minutes of full pipeline.

### 3.2 Hard Gate vs Soft Gate

The soul-repository conflates two distinct gate types at T6:

| Gate Type | Purpose | Current Location | Examples |
|---|---|---|---|
| **Compliance Gate** | Pass/fail against objective criteria | T6 Checklist 1–20 | Line count, word count, sentient being, lowercase filename |
| **Quality Gate** | Score against subjective rubric | T6 Scoring (1–5 × 7 axes) | Distinctiveness, Voice Immediacy, Name Quality |

**Current problem:** The hard-gate checklist is run by the same profile (T6) as the scoring rubric. This creates perverse incentives: a T6 reviewer may be reluctant to fail a draft on hard gates if it scores well on rubric, or vice versa.

**Recommended pattern:** Separate gates into distinct stages:
```
T4 (Soft review) → T5 (Refine) → T6a (Compliance Gate) → T6b (Quality Gate)
```

Or use parallel reviewers at T6:
- `soul-compliance-checker`: Runs the 20-point checklist. Output: PASS/REJECT with failure reasons.
- `soul-quality-rater`: Runs the 7-axis rubric. Output: Score + notes.
- Only drafts passing T6a advance to T6b scoring.

This separation is standard in software engineering (CI pipelines separate lint from test from security scan) and in ML pipelines (separate data validation from model evaluation from bias audit).

### 3.3 Multi-Stage Review

The current pipeline has exactly one reviewer per stage (T4, T6). Literature on LLM-as-judge shows that inter-rater reliability is a major concern: "The judge cannot exceed inter-rater agreement on the underlying task" (Galtea Blog, 2026). If a single T6 worker is inconsistent, the archive quality is inconsistent.

**Recommendation:** Use ensemble review at T6:
- Dispatch the same `refined/<name>.md` to 2–3 `soul-final-reviewer` instances
- Require majority vote on PASS/REJECT
- Average the rubric scores
- Flag high-variance cases (one PASS, two REJECT) for human review

This pattern is the core of LMSYS Arena (pairwise voting with Elo) and the "Mixture of Agents" pattern (aggregative topology per Wasowski).

---

## 4. Failure Handling Patterns

### 4.1 Retry (Current Pattern)

The current T6→T5 retry loop:
- Bounded to 3 retries
- Orphan risk: T6 must create both T5 and chained T6 in same step
- No exponential backoff (not relevant for creative work, but no jitter either)

**Improvement:** Add retry metadata tracking:
- Retry #1: What changed?
- Retry #2: What changed?
- Retry #3: Same flaw? → Dead letter

### 4.2 Dead Letter Queue

A dead letter queue (DLQ) handles "unprocessable records without stopping the rest of the pipeline." In the soul-repository, `reject/` is a manual dump. A proper DLQ would:
- Store rejected personae with structured rejection reasons
- Categorize by rejection type (format, voice, archetype, name)
- Enable batch analysis: "40% of rejections are missing griping lines" → update T3 instructions
- Support periodic reprocessing: run a `reject-reviewer` that checks if improved T3/T5 instructions could salvage an old reject

### 4.3 Feedback Loop

The missing T6→T1 feedback is the biggest architectural gap. Literature on agentic pipelines (APIGen-MT, 2025; multiple Medium sources, 2026) identifies "no feedback loop" as the #1 cause of plateaued performance.

**Pattern:** After every N pipeline completions, run an `analysis` task:
- Read all rejections from the last N runs
- Cluster rejection reasons
- Output spec changes for T1, T3, or T5

This is a "meta-worker" that treats the pipeline as its dataset.

### 4.4 Kill Pattern (Stage-Gate)

From the Stage-Gate NPD literature (Cooper, 1970s–present), every gate should have four outcomes:
- **Go:** Advance to next stage
- **Kill:** Abandon, archive reason
- **Hold:** Pause for external input
- **Recycle:** Return to earlier stage for rework

The soul-repository uses only Go and Recycle. Kill exists only after 3 retries. Hold does not exist at all.

**Recommendation:** Allow T6 to KILL after 1 retry if the flaw is "unfixable at this archetype" (e.g., the teacher archetype inherently violates the follow-through constraint). Allow T6 to HOLD if the flaw is a spec ambiguity (e.g., "Is this sign-off framing physical or tonal?"). These should create a `blocked` kanban task with a comment, waiting for human resolution.

---

## 5. Hermes Kanban Features Not Currently Used

### 5.1 `triage` Status

The current pipeline creates tasks directly as `todo`. The kanban system supports `triage` → `todo` promotion. The T1 researcher could:
- Create all seed tasks in `triage`
- A human (or T0 screener) reviews seeds and promotes viable ones to `todo`
- Seeds that fail viability stay in `triage` until revised

### 5.2 Batch Operations

The kanban CLI supports "multiple ids so you can clean up a batch in one command." The orchestrator never uses this:
- After archiving a persona, stale artifacts (`drafts/`, `critiques/`, `refined/`, `names/`) could be deleted in one batch
- Failed/rejected chains could be batch-archived to `reject/`

### 5.3 Parent Links for Parallel Review

The kanban `link` primitive supports multiple parents. For ensemble T6 review:
```python
kanban_create(title="T6b: Quality-review <Name>", assignee="soul-final-reviewer-b", parents=[t5_task_id])
```
Both T6 reviewers run in parallel, reading the same `refined/<name>.md`.

### 5.4 `goal_mode` Cards

From the kanban docs: "Worker runs in a judge loop (Ralph engine). Body = acceptance criteria. If turn budget runs out → blocked for human review."

This is exactly the right mode for T6 final review, where the acceptance criteria is the 20-point checklist. Currently, T6 workers presumably run in standard completion mode. `goal_mode` would prevent silent failures.

### 5.5 `metadata` and `summary` for Structured Handoffs

The kanban `complete` call supports `metadata` (JSON dict) and `summary` (structured handoff). The current pipeline uses file artifacts for handoffs, which is robust but does not use the kanban's structured handoff capabilities.

**Use case:** T4 could complete with:
```python
kanban_complete(
    summary="Reviewed draft",
    metadata={
        "scores": {"distinctiveness": 4, "voice": 3, "metaphor": 5},
        "gap_count": 3,
        "critical_gaps": ["missing_griping", "generic_nevers"]
    }
)
```
T5 reads the metadata directly instead of parsing prose from `critiques/<name>.md`.

### 5.6 Tenant Namespace

The kanban supports "tenant" as a soft namespace. The soul-repository could use separate tenants per batch run (e.g., `tenant: batch-2026-05`) to isolate different research waves. Currently, all tasks share the default namespace.

### 5.7 `scheduled_at` for Deferred Dispatch

The `scheduled_at` field allows scheduling tasks for future execution. The researcher could prepare a week of seed tasks and schedule them to dispatch at intervals, managing load.

### 5.8 Workspace Kinds

The pipeline correctly uses `dir` workspace (preserved). But `worktree` (git worktree, preserved) is never used. Worktrees would allow parallel branches where different pipeline variants are tested simultaneously.

---

## 6. Separating Compliance from Quality

### 6.1 Current Conflation

In the current pipeline:
- T4 (Reviewer) does both format compliance checking AND feel evaluation
- T6 (Final Reviewer) runs 20 checklist items AND 7 rubric axes

Both stages use a single profile, a single prompt, and a single artifact. This conflates:
- **Invariant checks** (line count, word count, sentient being) that should never vary
- **Variant checks** (distinctiveness, voice immediacy) that depend on taste and archetype

### 6.2 Patterns from Software Engineering

CI/CD pipelines separate:
- **Lint** (format/compliance): deterministic, fast, fails build
- **Test** (quality/behavior): heuristic, slower, produces scores
- **Security scan** (safety): policy-driven, blocks deployment

Applied to soul-repository:
- **T4a (Lint):** Format rules, line/word counts, sign-off count, griping line presence. Binary pass/fail. Should be fully automated (a compliance script is a start, but not comprehensive).
- **T4b (Review):** Voice, metaphor, distinctiveness. Heuristic scoring. Always passes, produces gap notes.
- **T4c (Safety):** Object non-person check, no literal tool names, no obscure references. Binary pass/fail.

### 6.3 Patterns from LLM Evaluation

The LLM evaluation literature distinguishes:
- **Metric-based evals:** Exact match, regex, rule-based (compliance)
- **LLM-as-Judge:** Subjective, rubric-based (quality)
- **Human review:** Ground truth validation

The EleutherAI lm-evaluation-harness is pure metric-based. The LMSYS Arena uses pairwise human preference. Soul-repository should adopt both: automated lint for compliance, LLM ensemble for quality, human spot-check for ground truth.

### 6.4 Concrete Recommendation

Add a `scripts/lint_soul.py` that implements ALL hard gates as deterministic checks:
- Line count 8–20
- Word count ≤200
- Griping line present (regex or heuristic)
- Identity line starts with "You are [Name] — a [noun] who [contradiction]"
- At least one "Never" sentence
- At least 3 quoted sign-off phrases
- No literal tool names (grep for banned strings)
- Sentient being check (entity type classification via simple keyword or external call)

Run this linter at T3-output (before T4) and at T5-output (before T6). Only drafts passing the linter advance to expensive human-style review.

---

## 7. Review Before Draft (Pre-Checking Viability)

### 7.1 The Current Investment Pattern

A seed moving through the current pipeline consumes:
- T1: ~1–2 minutes (research + orchestration)
- T2: ~1 minute (naming)
- T3: ~3–5 minutes (writing)
- T4: ~2 minutes (reviewing)
- T5: ~3–5 minutes (refining)
- T6: ~2–3 minutes (final review)
- T6 retry: +T5+T6 time

**Total per seed:** ~12–18 minutes of wall-clock + AI compute. If a seed is fundamentally flawed (e.g., "abstract philosopher" with no material practice), all of this is wasted.

### 7.2 Pre-Checking Patterns

**The "Viability Screener" (T0):**
Before writing a single behavioral line, answer:
1. List 5 concrete tools/materials the archetype uses
2. What does this archetype gripe about while working?
3. What is the metaphor family for tool use?
4. Does this archetype have a natural address term for a stranger?
5. Does this archetype have 3+ natural ways to end a conversation?

Any answer missing or generic → HOLD the seed. Do not create T2.

**The "Seed Quality Score":**
Apply a lightweight rubric (1–3 per question, max 15) to each seed. Only seeds scoring ≥10 advance. This is a pre-flight check, not a gate.

### 7.3 Alternative: Parallel Seed Development

Instead of screening one seed at a time, run T2→T3 for 3–5 seeds in parallel, then select the best 1–2 to advance to T4. This is "parallel exploration before serial exploitation" — the correct pattern when the cost of evaluation (T4) is lower than the risk of pursuing a bad seed.

---

## 8. Scaling Patterns

### 8.1 Batch Processing

**Currently:** T1 creates one chain at a time (T2→T3→T4→T5→T6 per seed).

**Recommended:** T1 research phase produces 5 seeds. All 5 seeds spawn parallel T2→T3 chains. After all T3 drafts exist, a batch T4 reviews all 5 drafts in a single task, comparing them against each other. The best 2–3 advance to T5→T6; the rest are parked.

**Benefit:** Comparative review ("Draft A has a stronger griping line than Draft B") is more reliable than absolute review ("This draft is a 4/5"). The LMSYS Arena is built on pairwise comparison because human (and LLM) judges are more consistent relatively than absolutely.

### 8.2 Parallel Review

As discussed in §3.3 and §5.3, run multiple reviewers in parallel:
- T4a/T4b/T4c (compliance/review/safety)
- T6 ensemble (2–3 final reviewers)

Hermes kanban `link` supports multiple parents natively. The orchestrator simply:
```python
kanban_create(title="T6a: Compliance <Name>", assignee="soul-compliance-checker", parents=[t5_task_id])
kanban_create(title="T6b: Quality <Name>", assignee="soul-quality-rater", parents=[t5_task_id])
```
Both tasks read the same `refined/<name>.md`, run in parallel, and complete independently.

### 8.3 Consensus Scoring

For the 7-axis rubric, use an agreement threshold:
- If all 3 reviewers agree within 1 point on every axis → high confidence
- If variance >1 point on any axis → flag for human review
- Final score = median (more robust than mean for creative ratings)

This is the "majority voting" pattern from Wasowski's aggregative topology class (Class VI).

---

## 9. Summary of Recommended Architectural Changes

| # | Gap | Pattern | Effort | Impact |
|---|---|---|---|---|
| 1 | No T6→T1 feedback | Persistent `failure-patterns.md` + T1 reads at startup | Low | High |
| 2 | Compliance & quality conflated | Split T4/T6 into compliance + quality sub-stages | Medium | High |
| 3 | Single reviewer per stage | Ensemble review (2–3 parallel reviewers) at T6 | Medium | High |
| 4 | No pre-flight viability check | T0 Screener: 5-question viability test before T2 | Low | Medium |
| 5 | No batch processing | Parallel T2→T3 for all seeds, then batch T4 review | Medium | Medium |
| 6 | No systematic DLQ | Structure `reject/` with categorization + periodic re-analysis | Low | Medium |
| 7 | Kanban metadata unused | Structured handoffs via `metadata` + `summary` JSON | Low | Low |
| 8 | No `goal_mode` / `triage` | Use `triage` for seeds, `goal_mode` for T6 | Low | Medium |
| 9 | No automated lint | `scripts/lint_soul.py` implementing all hard gates | Medium | High |
| 10 | No cross-run memory | Meta-worker analysis task every N runs | Medium | High |
| 11 | Single-task dispatch | Batch kanban operations (cleanup, archive) | Low | Low |
| 12 | No consensus scoring | Median score + variance flagging for rubric axes | Low | Medium |

---

## 10. Architectural Vision: Future State

```
T1 (Researcher) ──► seeds/ ──► T0 (Screener) ──┬──► KILL (reject/)
                                               ├──► HOLD (triage)
                                               └──► GO ──► T2 (Namer)
                                                        │
                                                        ▼
                                              T3a/T3b/T3c (Swarm Writers)
                                                        │
                                                    ┌───┴───┐
                                                    ▼       ▼
                                              T4 (Batch Comparative Review)
                                                    │
                                              T5 (Refiner — best 2 drafts)
                                                    │
                                              ┌─────┴─────┐
                                              ▼           ▼
                                        T6a (Compliance) T6b1/T6b2/T6b3 (Quality Ensemble)
                                              │           │
                                              └───► Aggregate ──► ARCHIVE / RETRY / KILL
                                                    │
                                            ▼
                                    feedback-loop ──► references/failure-patterns.md
```

This architecture uses:
- **DAG** (parallel T3a/b/c, parallel T6b1/2/3, parallel T6a+b)
- **Pre-flight gate** (T0 Screener)
- **Swarm** (multiple writers)
- **Ensemble review** (consensus scoring)
- **Automated lint** (compliance gate)
- **Structured metadata** (kanban handoffs)
- **Dead letter queue** (`reject/` with categorization)
- **Feedback loop** (`failure-patterns.md` read by T1)

It preserves the creative soul of the pipeline (human-feeling personae, craft-specific language) while adding the engineering rigor necessary to scale from 60 archived personae to hundreds without diluting quality.

---

*Research sources: Hermes Kanban docs (NousResearch), Anthropic "Building Effective Agents" (2024), Wasowski multi-agent topology analysis (2026), Sangam Pandey agentic workflow patterns (2026), Stage-Gate NPD literature, EleutherAI lm-evaluation-harness, LMSYS Arena methodology, CI/CD pipeline patterns, dead-letter queue literature.*
