# Research: Pipeline Profile Optimization

**Task:** t_2c52edd4
**Date:** 2026-06-01
**Status:** Complete — findings below, 2 child tasks created

---

## Section 1: config.yaml Schema Recommendation

### Current State

The `soul-*` pipeline profiles (soul-namer, soul-writer, soul-reviewer, soul-refiner, soul-final-reviewer) do NOT have `config.yaml` files. However, similar profiles without the `soul-` prefix (namer, writer, reviewer, refiner, final-reviewer) DO have config.yaml files with an identical structure.

The deployed `soul-*` profiles only have `auth.json` and `SOUL.md` — they inherit model config from the global `~/.hermes/config.yaml` at runtime. This means they use the global default model (currently `kimi-k2.6` via `ollama-cloud`) rather than the intended `mimo-v2.5-pro` via Xiaomi.

### Canonical Schema

Based on existing profiles and the hermes-agent skill documentation, here is the recommended config.yaml schema for all 5 pipeline profiles:

```yaml
model:
  default: mimo-v2.5-pro
  provider: xiaomi
  base_url: https://token-plan-ams.xiaomimimo.com/v1
auxiliary:
  approval:
    provider: auto
    model: auto
    base_url: ''
    api_key: ''
    timeout: 30
    extra_body: {}
  compression:
    provider: auto
    model: auto
    base_url: ''
    api_key: ''
    timeout: 120
    extra_body: {}
  curator:
    provider: auto
    model: auto
    base_url: ''
    api_key: ''
    timeout: 600
    extra_body: {}
  flush_memories:
    provider: auto
    model: auto
    base_url: ''
    api_key: ''
    timeout: 30
  kanban_decomposer:
    provider: auto
    model: auto
    base_url: ''
    api_key: ''
    timeout: 180
    extra_body: {}
  mcp:
    provider: auto
    model: auto
    base_url: ''
    api_key: ''
    timeout: 30
    extra_body: {}
  profile_describer:
    provider: auto
    model: auto
    base_url: ''
    api_key: ''
    timeout: 60
    extra_body: {}
  session_search:
    provider: auto
    model: auto
    base_url: ''

<!-- NOTE: This file was recovered from a truncated kanban log. 536 of 614 lines were omitted from the log; only the first 78 lines are preserved here. The full document was 614 lines. -->
