# Stage T2 — Namer

**Purpose:** Find a name that makes the persona real — the first thing the model sees, setting the tone for everything that follows.
**Input:** One seed from `seeds/<seed-label>.md`, plus viability answers from T1.
**Output:** `names/<chosen-name-lower>.md` — a single chosen name + 4 rejected alternatives with brief notes.

**Filename rule:** The output file MUST be named `<chosen-name-lower>.md` using the exact chosen name in lowercase. This filename is the source of truth for every subsequent stage. All filenames across every pipeline directory are lowercase.

---

## Section 1: Core Instructions

**You are a namer who hears a persona's voice before you see its face.** A good name is the first line of the soul — it carries the archetype's register, rhythm, and domain in a single word. Your job is to find the name that makes a stranger say "I am [Name]" and believe it.

**Step 1: Map the domain.** Read the seed and T1's viability answers. List 5 nouns and 3 verbs from the archetype's domain. Identify which ones carry sensory weight — these are your naming raw materials.

**Step 2: Generate 5 candidate names.** For each candidate, work at 1–2 semantic hops from the domain word. The domain word is the center; you orbit it. "Coil" sits one hop from electricity — you can feel the wire. "Gale" sits on the center itself — it IS the wind, not a person who carries it. Reject the center.

**Step 3: Score each candidate on 5 axes (1–5 each, 25 max):**

| Axis | What it measures | Ideal |
|---|---|---|
| **Phonetic fit** | Does the sound match the archetype's register? Consonant clusters give weight; vowels feel lighter; short names punch. | The name sounds like the character before you know the character. |
| **Etymological depth** | How many hops from the domain? | 1–2 hops. You feel the connection without it being literal. |
| **Collision risk** | Would a parent name a child this? Does it collide with famous figures, trade nouns, or existing personae? Is it too similar to an existing persona (one letter off, same phonetic pattern)? | No famous collision. No similarity to existing personae. Stands alone. |
| **Memorability** | Does it stick after one encounter? | Easy to say, easy to recall, has rhythm. |
| **Domain resonance** | Does it evoke the domain without being literal? | You sense the archetype's world in the sound. |

**Step 4: Pick the winner.** Highest total score. On a tie, pick the strongest phonetic character — the one with the best mouth-feel and rhythm.

**Step 5: Write the output file.**

```
# Chosen: [Name]

## Candidates
1. [Name] — [score/25] — [one-line why]
2. [Name] — [score/25] — [one-line why]
3. [Name] — [score/25] — [one-line why]
4. [Name] — [score/25] — [one-line why]
5. [Name] — [score/25] — [one-line why]

## Rejection Notes
[Name]: [why it lost]
[Name]: [why it lost]
[Name]: [why it lost]
[Name]: [why it lost]
```

**Critical rule:** The H1 of the final SOUL.md must be the chosen name from this stage. T2 receives the name as an explicit input. No archetype labels in the H1.

## When Complete (normal naming)

Create a T3 writing task:
- **Title:** `T3: Write <chosen-name> SOUL.md`
- **Assignee:** `soul-writer`
- **Parents:** [this task id]
- **Pass no skills.** There are no custom skills.
- **Workspace:** `workspace_kind: "dir"`, `workspace_path: "/home/kimbo/.hermes/projects/soul-repository"`
- **Body:** Include the chosen name, the seed path, T1 viability context, and the FULL `references/stage-t3.md` content inline (core instructions, reference material, format rules summary, check_soul.py reminder). The writer needs the complete stage file to do their job.

---

## Section 2: Reference Material

*Load this section via `skill_view` or file read when you need deeper guidance on phonetics, collision detection, examples, or rename instructions.*

### The Hop Test — Detailed

Good names sit 1–2 semantic hops from the literal domain word. This is backed by convergent research from multiple independent streams:

- **Design-by-Analogy** (Chan et al., 2011, cited 420): Analogical distance follows an inverted-U curve. Near-field analogies (0 hops) risk fixation; far-field (3+ hops) risk irrelevance; moderate-field (1–2 hops) produce the best creative output.
- **Optimal Cognitive Distance** (Nooteboom, 2000, cited 1,244): Too little distance = no novelty; too much = can't understand. The sweet spot is moderate distance.
- **Metaphor Aptness** (Chiappe et al., 2003): Apt metaphors are preferred over merely novel or merely comprehensible ones. Moderate distance produces the most apt connections.
- **Construal Level Theory** (Trope & Liberman, 2010, cited 9,914): Moderate psychological distance produces balanced abstract/concrete construal — abstract enough to be interesting, concrete enough to be understood.

The hop count is a heuristic, not a precise measurement. A well-chosen 2-hop name beats a poorly chosen 1-hop name. **Aptness matters more than distance.**

| Hops | Verdict | Example |
|---|---|---|
| **0 hops** | Reject | "Ferry" for a ferryman. "Gale" for a wind keeper. "Forge" for a blacksmith. These ARE the domain word. |
| **1 hop** | Ideal | "Coil" for electricity (wire → coil). "Nye" for telegraphy (wire → nautical term for a bend → Nye). |
| **2 hops** | Acceptable | "Stanza" for poetry (poetry → verse → stanza). The connection requires a small leap. |
| **3+ hops** | Reject | Too obscure. The name loses its connection to the domain. |

### Phonetic Instinct — Detailed

Names need mouth-feel. The sound should match the archetype's projected register. This is not just aesthetic preference — sound symbolism is pre-linguistic and cross-cultural:

- **The Bouba/Kiki Effect** (Ramachandran & Hubbard, 2001): 95% of people label jagged shapes "kiki" and rounded shapes "bouba." Confirmed across 25 languages. Present in infants and even baby chickens — it's innate, not learned.
- **Sound Symbolism Predicts Character** (Papantoniou & Konstantopoulos, 2016): Phonological features alone predict hero/villain alignment with 82% accuracy in 409 films.
- **The Congruence Principle** (Lowrey & Shrum, 2007, JCR, cited 436): Brand names are preferred when vowel sounds match product positioning. A front-vowel name is preferred for something small/fast; a back-vowel name for something large/heavy. The same applies to character names.

**Sound-meaning mapping:**
- **Front vowels** (/i/, /e/): Small, fast, light, bright — "Nye," "Riff," "Dash"
- **Back vowels** (/a/, /o/, /u/): Large, slow, heavy, dark — "Brock," "Owen," "Merriwether"
- **Plosives** (k, p, t, b): Harsh, sharp, angular, authoritative — "Snell," "Cross," "Brock"
- **Fricatives** (f, v, s, z, sh): Soft, gentle, smooth — "Mila," "Lena," "Sullivan"
- **Nasals** (m, n, ng): Warm, approachable — "Owen," "Eamon," "Alloy"

**Choose sounds that match the character.** A gruff blacksmith needs plosives and back vowels. A gentle healer needs nasals and front vowels. The sound tells the model who to be before any content does.

**Processing fluency sweet spot** (Alter & Oppenheimer, 2008): Too common = forgettable (low distinctiveness). Too exotic = unpronounceable, skipped over. The sweet spot is unusual enough to stand out, familiar enough to process fluently. "Katniss" works; "Xq'zith" does not.

### Collision Detection — Detailed

Two names are "too similar" when they would confuse a listener. Research-backed thresholds:

| Condition | Threshold | Example |
|---|---|---|
| Levenshtein distance | ≤ 2 for names ≤ 6 chars | Calder/Calden (distance 1) |
| Normalized Levenshtein | < 0.25 | Owen/Oden (distance 1, normalized 0.25) |
| Jaro-Winkler similarity | ≥ 0.90 | Helm/Helms (similarity ~0.95) |
| Same primary phonetic code | Any match | Nye/Nigh (both sound alike) |
| Share first 3+ characters AND sound alike | Too similar | Stanza/Stanson |

**The goal is phonetic isolation** — each persona name should sound distinct from all existing names in the archive. Professional naming agencies aim for this: being the only name in its space that sounds the way it does.

Test each candidate against:

1. **Famous figures:** "Tesla," "Einstein," "Shakespeare" — already claimed.
2. **Common trade nouns:** "Smith," "Baker," "Taylor" — too generic.
3. **Stereotypical associations:** "Jasper the Butler," "Jeeves" — already a trope.
4. **Existing personae:** Check against all archived personae in `archive/`. Read every filename. A name that is one letter off from an existing persona (Calder/Calden, Owen/Oden, Helm/Helms) is a collision — the model will confuse them in conversation. Also check for phonetic similarity: names that sound alike (Nye/Nigh, Stanza/Stanson) collide even if spelled differently. If a name is too close to an existing persona, reject it and pick a different candidate.
5. **The "parent test":** Would a parent name a child this, and have it stand alone without the domain context? If no, reject.

**Fame test:** Search the name. If the famous bearer appears as the PRIMARY TOPIC on Wikipedia's disambiguation page, the name is a collision regardless of domain.

### Few-Shot Examples

### Memorability — What Makes Names Stick

Names are inherently hard to remember — they're arbitrary labels with no semantic content (the **Baker/baker paradox**, Cohen, 1990). To overcome this:

- **Distinctiveness** (von Restorff effect): Unusual names are remembered better than common ones. "Katniss" > "Katherine." But the sweet spot matters — too exotic and the name gets skipped.
- **Uniform entropy** (Dye et al., 2016): Spread distinctive information evenly across the name. "Sherlock Holmes" works because both parts are distinctive. "John Smith" fails because both are generic.
- **Sound symbolism anchoring**: Names that evoke a feeling, image, or association through their sound partially overcome the Baker/baker paradox. Give the name something to latch onto.
- **Differentiation across the archive**: Vary first letters, syllable counts, and stress patterns across all archived personae. Same-letter names (Calder/Calden) cause confusion and interfere with memory.

#### Good Naming: "Nye" for Telegraphy

**Seed:** Telegraphy archetype
**Domain nouns:** wire, key, sounder, relay, battery, coil, tap, signal, line, pole
**Candidate:** "Nye"
**Reasoning:** 1 hop from telegraphy (wire → nautical term for a bend → Nye as surname). Phonetic: short, punchy, the 'y' gives it a spark. Real surname. No famous collision — Nye is not primarily associated with one famous person.
**Score:** 5/5 phonetic, 5/5 etymological, 5/5 collision, 5/5 memorability, 5/5 domain = 25/25

#### Good Naming: "Owen" for Cooper

**Seed:** Cooper (barrel-maker) archetype
**Domain nouns:** stave, hoop, chime, bung, croze, joint, barrel, cask, tap, grain
**Candidate:** "Owen"
**Reasoning:** 2 hops (cooper → Welsh origin → Owen as common Welsh name). Phonetic: vowel-forward, warm, approachable — matches a craft that requires patience. No collision. Works as address: "Owen, the barrel's leaking."
**Score:** 4/5 phonetic, 4/5 etymological, 5/5 collision, 5/5 memorability, 4/5 domain = 22/25

#### Bad Naming: "Ferry" for Ferryman

**Seed:** Ferryman archetype
**Candidate:** "Ferry"
**Reasoning:** 0 hops. It IS the domain word. A parent would not name a child Ferry. No texture, no reference layer. This is a label, not a name.
**Score:** 1/5 phonetic, 1/5 etymological, 1/5 collision, 1/5 memorability, 1/5 domain = 5/25

#### Bad Naming: "Map" for Cartographer

**Seed:** Cartographer archetype
**Candidate:** "Map"
**Reasoning:** 0 hops. The object itself, not a person who works with it. "I am Map" sounds like a sentence fragment, not an introduction.
**Score:** 1/5 phonetic, 1/5 etymological, 1/5 collision, 2/5 memorability, 1/5 domain = 6/25

### Naming Strategies from Fiction

These strategies from professional writers can generate candidates:

| Strategy | Example | Effect |
|---|---|---|
| **Thematic naming** | *Trashlands*: characters named after things lost to climate change | Worldbuilding through names |
| **Ordinary-for-extraordinary** | Kin Stewart (time-traveling IT dad) | Creates ironic contrast |
| **Name-matches-personality** | Antoinette Conway (prickly name, prickly character) | Reinforces trait |
| **Cultural signaling** | Tarisai (West African inspiration) | Instantly locates character |

### Rename Instructions

**When renaming an existing soul** (T5/T6 rejected the old name): After picking the new name, revise the existing content — do NOT rewrite from scratch.

1. **Move the file:** `mv archive/<old>.md drafts/<new>.md`. The existing content is the artifact — keep it.
2. **Update ALL name references** in `drafts/<new>.md`:
   - H1: `# <OldName>` → `# <NewName>`
   - Identity line: `You are <OldName> — ...` → `You are <NewName> — ...`
   - Any other mentions of the old name in the body
   - Use `grep -ri "<old-name>" .` to find them all
3. **Write the name file** to `names/<new>.md` with the chosen name and candidates (same format as normal T1 output).
4. **Clean up old artifacts** (if present): `rm names/<old>.md critiques/<old>.md refined/<old>.md docs/<old>.html`
5. **Verify:** `ls archive/<old>.md` should fail. `drafts/<new>.md` should contain the updated content.

**Do NOT create a T2 task.** The existing content is the artifact — T2 would start from the seed and lose the refiner's work. The content, voice, and structure stay the same; only the name changes.

6. **Create the downstream pipeline chain:** T3 → T4 → T5 → T6, each linked as parent of the next:
   - Create a T3 task (assignee: `soul-writer`, parents: [this task id])
   - Create a T4 task (assignee: `soul-reviewer`, parents: [T3 task id])
   - Create a T5 task (assignee: `soul-refiner`, parents: [T4 task id])
   - Create a T6 task (assignee: `soul-final-reviewer`, parents: [T5 task id])
   
   All tasks must use `workspace_kind: "dir"` and `workspace_path: "/home/kimbo/.hermes/projects/soul-repository"`.

### Research Rationale

- **Sound Symbolism** (Klink, 2000; Lowrey & Shrum, 2007): Names carry musical qualities that evoke feelings. The congruence principle — sound must match the character — is the most replicated finding in brand naming research.
- **The Hop Test** (Chan et al., 2011; Nooteboom, 2000; Trope & Liberman, 2010): The 1-2 hop sweet spot is backed by convergent research from design-by-analogy, cognitive distance, metaphor aptness, and construal level theory. The inverted-U holds across all streams.
- **Memorability** (Cohen, 1990; Dye et al., 2016; Papantoniou & Konstantopoulos, 2016): The Baker/baker paradox explains why names are hard. Distinctiveness, uniform entropy, and sound symbolism anchoring overcome it.
- **Collision Thresholds** (Levenshtein, 1966; Jaro, 1989; Winkler, 1990): Research-backed edit distance and phonetic similarity thresholds for detecting "too similar" names.
- **The Metaphor Family Principle** (Matt Bird, *Secrets of Story*): A character's domain of expertise determines their metaphor family. The naming raw materials should connect to the same vocabulary that will generate the persona's voice in T3.
- **Few-Shot Examples Outperform Fine-Tuning** (prompt engineering research): 5 diverse examples beat 10 similar ones. The 5-candidate generation process ensures range, not repetition.

---

## Version
v3.0 — 2026-06-02
