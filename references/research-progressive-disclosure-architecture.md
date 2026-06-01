# Progressive Disclosure Architecture for Multi-Stage Character Pipelines

## Executive Summary

This research examines how to architect rich, multi-layered guidance across the Soul Repository's 6-stage pipeline (T0→T5) using progressive disclosure principles. The core challenge: packing absurd amounts of detail into the pipeline without overwhelming any single worker.

**Key Finding:** The pipeline already implements progressive disclosure at the task level (each stage sees only its inputs), but the stage files themselves have become dense monoliths. The solution is a three-tier disclosure architecture: core instructions (always visible), contextual guidance (loaded per-task), and reference material (available on demand).

---

## 1. The Problem: Information Density in Stage Files

### Current State

Each stage file contains:
- Stage-specific instructions (purpose, process, rules)
- Quality frameworks (Four Pillars, Three Questions)
- Examples (good/bad patterns)
- Output format specifications
- Edge case handling
- Compliance rules

**Current file sizes (approximate words):**
- stage-t0.md: ~1,100 words
- stage-t1.md: ~1,400 words
- stage-t2.md: ~1,200 words
- stage-t3.md: ~1,600 words
- stage-t4.md: ~1,300 words
- stage-t5.md: ~2,000 words
- orchestration.md: ~2,000 words
- format-rules.md: ~1,400 words
- positive-patterns.md: ~1,400 words

**Total context per worker:** When a task is created, the orchestrator includes the full stage file inline in the task body. This means every worker receives 1,000-2,000 words of instructions plus the task context.

### The Cognitive Load Problem

Research on LLM attention patterns (Liu et al., 2023 - "Lost in the Middle") shows:
- **U-shaped attention:** Models attend best to information at the beginning and end of context
- **Middle degradation:** Information in the middle of long contexts is accessed less reliably
- **Position matters:** The same information placed at different positions yields different performance

This means our current approach of dumping 2,000 words of instructions into a task body may cause workers to miss critical details in the middle of the instruction set.

---

## 2. Progressive Disclosure Patterns in Creative Pipelines

### How TV Writers Rooms Distribute Expertise

TV writers rooms operate on a hierarchy of knowledge distribution:

1. **Showrunner** (T5 equivalent): Final creative authority. Knows everything about every character.
2. **Story Editor** (T3/T4 equivalent): Deep knowledge of character arcs, continuity.
3. **Staff Writer** (T2 equivalent): Focused on individual episodes/scenes.
4. **Research Assistant** (T1 equivalent): Fact-checking, background material.

**Key insight:** Each role "owns" specific knowledge domains. A staff writer doesn't need to know every continuity detail - they need to know what's relevant to their episode.

### How Game Writing Rooms Distribute Expertise

Game writing rooms (e.g., BioWare, Naughty Dog) use:

1. **Character Bible:** The canonical reference for a character's voice, backstory, constraints.
2. **Mission Brief:** Specific scene requirements, dialogue goals.
3. **Dialogue Trees:** Branching paths with constraints.

**Key insight:** The character bible exists as a separate document that writers reference, not as inline instructions in every task.

### Pattern: Layered Disclosure Hierarchy

The successful pattern across creative industries is:

```
Layer 1: Role Definition (always visible)
  "You are a [role]. Your job is [specific responsibility]."

Layer 2: Process Guidelines (loaded per task)

<!-- NOTE: This file was recovered from a truncated kanban log. 443 of 521 lines were omitted from the log; only the first 78 lines are preserved here. The full document was 521 lines. -->
