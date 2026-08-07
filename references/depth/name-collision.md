# Depth Reference: Name Collision

## Examples First

Three name pairs, three different outcomes — the difference is never just one metric:

> ❌ **Collides:** "Riven" and "Ravin" — one letter apart, and the ear can't tell them apart in a hallway: two personae that sound like one.

> ❌ **Collides:** "Delia" and "Dalia" — the eye sees two names and the mouth makes one; a single vowel is all that separates them, and vowels are exactly what users mishear.

> **Safe:** "Hollow" and "Grim" share a mood, not a sound — different first letters, different rhythms, no shared syllables; a user could meet both in the same week and never mix them up.

**What these show:** collision is multidimensional. The first pair fails every check at once — spelling, sound, rhythm. The second passes the eye (the spellings are plainly different) but fails the ear, which is where users actually live. The third passes on every dimension even though both names evoke the same register. No single similarity metric is enough; the thresholds below are the hard guardrails.

---

## Core Principle

Two persona names are "too similar" when a reasonable user could confuse them — in reading, in memory, in conversation, or in search. Name collision erodes the distinct identity of both personae and creates friction across every interaction: users summon the wrong persona, confuse personalities, and the repository's catalog blur together. Preventing collision requires checking multiple dimensions of similarity simultaneously — orthographic (how names look), phonetic (how they sound), and structural (their morphological patterns) — because a name that passes one check may fail another.

## What the Research Says

### Name similarity is multidimensional

The research on name matching (from census record linkage, trademark law, and string metrics) converges on a critical finding: no single similarity measure is sufficient. A name pair may look different (different spelling) but sound the same (phonetic collision), or look similar but sound different. The best approach combines multiple metrics.

### Metric thresholds for "too similar"

From naming-similarity.md research, synthesized across computer science and legal sources:

| Metric | Collision Threshold | Notes |
|---|---|---|
| **Levenshtein distance** | ≤ 2 for names ≤ 6 chars; ≤ 3 for names ≤ 10 chars | Raw character edit distance; normalize by length for variable-length names |
| **Normalized Levenshtein** | < 0.25 | Edit distance / max string length; accounts for name length differences |
| **Jaro-Winkler similarity** | ≥ 0.90 | Designed specifically for name matching; weights prefix matches more heavily |
| **Shared Double Metaphone primary code** | Match = high collision risk | Names that sound alike share the same phonetic encoding |
| **Same Soundex code** | Any match (high false positive rate) | Useful as a coarse filter only; many dissimilar names share Soundex codes |
| **Shared first 3+ characters + phonetic match** | Too similar | The combination of visual AND phonetic overlap is a strong collision signal |
| **Suffix-only difference** (-ify, -ly, -er, -ing) | Often too similar | Different affixes on the same root are easily confused |
| **Vowel-only difference** | Often too similar phonetically | "Cortana" vs "Cortina" — single vowel change is easily misheard |

### The "moron in a hurry" standard

UK trademark law uses this standard: would "a moron in a hurry" be confused? The principle applies directly to persona names because:
- Users don't compare names side-by-side
- Memory is imperfect, especially across days or weeks of interaction
- Attention varies — a user scrolling a list of personae may glance for milliseconds

A name that survives careful analysis but causes confusion in rapid scanning has failed the collision test.

### Real-world confusion research shows the stakes

- Visual similarity alone causes confusion in ~15–25% of cases when names share >60% of characters
- Phonetic similarity is the strongest predictor of confusion in spoken/verbal contexts
- Conceptual similarity (same meaning space: "Quick"/"Swift"/"Rapid") can cause confusion even when visual and phonetic similarity are low

### Brand naming science confirms the "distance" principle

Professional naming agencies implicitly maximize distance on four dimensions:

1. **Orthographic distance** — different spelling patterns from competitors
2. **Phonetic distance** — different sound patterns from competitors
3. **Semantic distance** — different meaning space from competitors
4. **Structural distance** — different word patterns (different roots, affixes, morphological structures)

The goal is **phonetic and orthographic isolation** — being the only name in your category that sounds or looks the way you do.

### Common anti-patterns that produce collisions

Research on naming failures (brand naming and fiction) identifies patterns that repeatedly cause trouble:
- **"X-ify" suffix pattern:** Shopify, Spotify, Notify — overused suffix creates confusion
- **"X-ly" suffix pattern:** Bitly, Grammarly — same structure, blur together
- **Prefix-swapped variants:** "FaceTime" vs "FaceChat" — share too much structure
- **Same-initial characters in the same set:** Readers confuse Sam, Sarah, and Steve (Anne R. Allen)
- **Same syllable count and stress pattern:** A cast of three-syllable names with stress on the first syllable will blur together
- **Synonym substitution:** "Quick" vs "Swift" vs "Rapid" — same meaning space, easily confused

## How to Apply It

### For Namer — Pre-submission collision check

Before settling on a name, run this multi-step check against all existing persona names in the repository:

1. **Normalize** — lowercase, strip whitespace and punctuation
2. **Check Levenshtein distance** against every existing name
   - Reject if ≤ 2 for names ≤ 6 characters
   - Reject if ≤ 3 for names ≤ 10 characters
   - Flag if normalized distance < 0.25
3. **Check Jaro-Winkler similarity** against every existing name
   - Reject if ≥ 0.90
4. **Check Double Metaphone** primary codes against every existing name
   - Reject if primary codes match AND Jaro-Winkler > 0.80
5. **Check for shared morphological patterns**
   - Same prefix or suffix family
   - Same syllable structure (count + stress)
   - Same first letter (especially problematic if the other name is close in other dimensions)
6. **Check for conceptual overlap**
   - Same meaning space, same domain associations, same implied cultural origin

If any automated check flags a concern, do not submit without human review.

### For Evaluator — Collision detection in critique

The reviewer should:

1. **Fetch the full list of existing persona names.** Collision checking requires the full set, not just memory.
2. **Run the similarity check pipeline** (or verify that the Namer did). If no automated check is possible, manually compare:
   - Does this name share its first 3+ characters with another name?
   - Does it differ by only one letter or vowel sound?
   - Does it use the same suffix family (-ify, -ly, -er) as another name?
   - Does it have the same syllable count and stress pattern as another prominent name?
3. **Test for "moron in a hurry" confusion.** Glance at the name for one second, look away, and describe it from memory. Then do the same for any potentially similar name. If your memory confuses them, a user will too.

### For Evaluator — hard floor

Name collision is a hard floor: a persona whose name collides with an existing one should not be archived. The Evaluator has the authority to reject at this stage. The pipeline has no retry loops — a rejected persona is not sent back for a new name; the Namer's pre-submission collision check is where a collision must be caught.

### Repository-wide naming hygiene

- Maintain a collision check script or manual checklist that runs before any new name is accepted
- Periodically audit the existing name set for latent collisions (names that were accepted individually but crowd each other in aggregate)
- Enforce first-letter diversity across the top 10–20 personae — if three names start with 'M', the catalog feels crowded even if no pair technically collides

## What to Watch Out For

1. **False positives from Soundex alone.** Soundex is too coarse — "Robert" and "Rupert" both encode to R163 but are legitimately similar enough in sound to warrant concern in the same repository. But many dissimilar names also share Soundex codes. Never rely on Soundex as a sole metric.

2. **False negatives from Levenshtein alone.** Two names may have high Levenshtein distance (different spelling) but sound nearly identical ("Katherine" vs "Catherine"). Phonetic checks catch what visual checks miss.

3. **Length effects skew raw distances.** A Levenshtein distance of 2 is very significant for "Jo" vs "Mo" (2/2 = 1.0 normalized) but trivial for "Alexandra" vs "Alexandria" (2/10 = 0.2 normalized). Always normalize edit distance by name length.

4. **Phonetic collision is worse than visual collision.** Users encounter persona names in speech (voice interfaces, word-of-mouth, verbal descriptions) more often than in text-only contexts. Phonetically similar names ("Cortana" / "Cortina") cause confusion in conversation even if the spelling is distinct.

5. **Conceptual collision is the hardest to catch.** Two names that are orthographically and phonetically distinct but belong to the same conceptual space ("Forge" / "Anvil" / "Smithy") may not technically collide but will blur in the user's mind because they evoke the same domain and register. This is a design concern, not a hard rule, but it matters for repository coherence.

6. **Collision with famous names or common words creates confusion of a different kind.** A persona named "Siri" or "Alexa" will be constantly confused with the commercial assistants. A persona named "Baker" may evoke the baker/baker paradox — the word "baker" carries occupational meaning that fights the arbitrary label. Avoid names that are already strongly associated with something else in the user's mind.

7. **Collision risk compounds.** A repository with 5 personae can tolerate names that are somewhat similar because the set is small. A repository with 50 personae needs much stricter thresholds. The collision standard should tighten as the catalog grows.

## Examples

- **Collision pair (bad):** "Korinne" and "Corinne" — Levenshtein distance 1 (K vs C), Jaro-Winkler very high (~0.96), same Double Metaphone code, same syllable count and stress. A user will confuse them every time. One must be renamed.

- **Safe pair (good):** "Maren" and "Corv" — Levenshtein distance 4 (normalized ~0.57), different first letters, different Double Metaphone codes, different syllable count (2 vs 1), different stress patterns, different vowel families (front vs back). No collision risk despite both being short.

- **Borderline pair (needs review):** "Trig" and "Trick" — Levenshtein distance 2 (normalized ~0.4), same first letter, both 1 syllable, Double Metaphone codes: Trig → TRK, Trick → TRK (same primary code). Phonetically they are different (hard g vs k sound) but structurally close. Would need human review: if they occupy different domains (one is a surveyor, one is a trickster), the conceptual distance may compensate. If both are in similar roles, they collide.

- **Anti-pattern (suffix collision):** Repository has "Verify" (a quality-checker persona). A new persona "Clarify" is proposed. Different first letter, different meaning — but the -ify suffix creates structural similarity and the rhythm (stressed first syllable, weak second) is identical. Users will group them mentally and may confuse them in rapid recall. Better to choose a name with a different morphological structure.

---

**Sources:** naming-similarity.md, research-character-creation.md (§4), naming-memorability.md (§5)
