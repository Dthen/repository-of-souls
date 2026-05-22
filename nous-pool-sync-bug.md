## Bug: `_sync_nous_entry_from_auth_store` never checks the shared Nous token store, causing pool entries to stay EXHAUSTED after runtime refresh

### Summary

When a Nous OAuth token expires and the credential pool marks the entry `STATUS_EXHAUSTED`, the auto-recovery path `_sync_nous_entry_from_auth_store` only checks `~/.hermes/auth.json` for fresher tokens. However, the runtime refresh path (`resolve_nous_runtime_credentials`) writes the new token to `~/.hermes/shared/nous_auth.json`. Since `auth.json` is not updated by the refresh, the pool never sees the fresh token and the entry stays EXHAUSTED until a full gateway restart.

### Steps to Reproduce

1. Authenticate with Nous Portal: `hermes auth add nous --type oauth`
2. Wait for the access token to expire (~15 minutes)
3. Observe that the gateway or kanban worker fails with "no available entries (all exhausted or empty)"
4. Run `hermes auth reset nous` — output: `Reset status on 0 nous credentials`
5. The pool entry remains EXHAUSTED. Only a gateway restart fixes it.

### Root Cause

In `agent/credential_pool.py`, `_sync_nous_entry_from_auth_store` (line 606) calls `_load_auth_store()` which reads `~/.hermes/auth.json`. The shared store at `~/.hermes/shared/nous_auth.json` is never consulted.

Meanwhile, `hermes_cli/auth.py` `_try_import_shared_nous_state` and the runtime refresh paths write to and read from the shared store exclusively after the initial login.

### Expected Behavior

When `_sync_nous_entry_from_auth_store` finds `auth.json` stale, it should fall back to `_read_shared_nous_state()` and adopt the fresher tokens from there.

### Proposed Fix

In `_sync_nous_entry_from_auth_store`, after loading state from `auth.json`, if the tokens are unchanged (or `auth.json` is stale), also load from the shared store and use whichever is fresher.

### Related Code

- `agent/credential_pool.py:606` — `_sync_nous_entry_from_auth_store`
- `hermes_cli/auth.py:4199` — `_read_shared_nous_state`
- `hermes_cli/auth.py:4001` — shared Nous store documentation

### Environment

- Hermes Agent: current main (post `hermes update`, commit `1264fab15`)
- Provider: Nous Portal (OAuth device code)
- Impact: Gateway-embedded kanban dispatch, any long-running daemon using Nous
