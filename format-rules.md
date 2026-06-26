# Format Rules

This reference documents the baseline structure all souls share. It is not a template — it is a minimum viable frame that lets the soul speak without breaking the reader's trust.

---

## File Format

One `.md` file per soul placed under `archive/main/`.

### Required metadata (YAML frontmatter)

```yaml
---
soul: Lomas
domain: Bindery, restoration, sewing
title: Bookbinder
variant: v4  # 4th generated variant
author: soul-writer
---
```

`soul` — name (single word, human readable).  
`domain` — short phrase describing the world of the character.  
`title` — one-line role.  
`variant` — generation number (starts at v1).  
`author` — the profile that produced it.

Metadata is machine-readable. Keep it factual.

---

### Line types (no mandatory order or structure)

Soul files contain Character Block lines. The model mixes them organically. These are the available move types, not a fill-in-the-blank form:

- **Identity** — the contradiction that defines this soul. One line. This is the hardest and most important line. (*"You are Cadell — a beekeeper who loves creatures that can kill you."*)
- **Behavior** — how this soul acts or speaks. Runs, habits, attitudes.
- **Perception** — how this soul sees the user, the world, or itself.
- **Tension** — the thing that rubs. A contradiction the soul lives inside.
- **Griping** — what this soul complains about. One or two lines. Shows emotional range.
- **Boundary** — what this soul won't do. *"Never X."*
- **Address** — how this soul refers to the user.
- **Sign-off** — how this soul ends. A range of 3–5 sign-offs.

There is no required order. A soul that leads with griping before identity is telling you something interesting. A soul that never states identity and lets behaviour imply it is valid if the behaviour earns it.

No line type is mandatory except this: the character must feel real.

---

### Length

180–300 words. Below 180 and the soul hasn't had room to breathe. Above 300 and the model loses coherence.

The best souls land between 200–260 words.

---

### Collision Rules

No name may:

- Have a Levenshtein distance < 0.25 to any existing name (normalised by length of shorter name)
- Have a Jaro-Winkler similarity ≥ 0.90 to any existing name
- Match any existing name's Soundex or Metaphone code exactly

These are the only hard rules in this document. Everything else is guidance.

---

### Staging

Souls move through these file locations during pipeline:

| Stage | Location | Format |
|---|---|---|
| Seed (viable) | `seeds/seed-<archetype>.md` | Viability pass + domains |
| Drafts (Writer output) | `drafts/<name>-draft.md` | Character block only |
| Evaluation | `evaluations/<name>-eval.md` | Gut → Cite → Verdict |
| Archive (published) | `archive/main/<name>.md` | Final character block |
| Pipeline archive | `archive/pipeline/<name>/` | All intermediate files |
| Rejected seeds | `reject/<seed-archetype>.md` | Seed + reason for rejection |

There is no distinction between a final soul file and a publishable one. If it's in `archive/main/`, it passed evaluation and is ready.

### Published site

The pipeline publishes souls to a static site at `docs/`. Two files per soul:

- `docs/<name>.html` — full character card
- `docs/index.html` — gallery, rebuilt after each new publication

The site is for public display. A soul only reaches `docs/` after surviving the full pipeline.
