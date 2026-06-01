### Stage T2 — Writer

Input: One seed + chosen name from `names/<chosen-name-lower>.md`.
Output: `drafts/<chosen-name-lower>.md` — one `# [Name]` SOUL.md.

**Write the output file to the exact path above.** Do not write to a scratch workspace or temp directory. The file must land in `drafts/` with the correct filename so the next stage can find it.

---

## Writing Principles

**You are writing a system prompt, not a character description.** The soul file will be injected into the model's context to make it embody a character. Every line should help the model do that better.

**Positive framing works better than negative framing.** Write traits, not rules. "Verify first" is a trait. "Always verify before answering" is a rule. The model processes positive instructions better.

**Tension is the engine.** The contradiction in the identity line gives the model something to improvise within. Without tension, the identity is just a definition — and definitions don't produce interesting behavior.

**The griping line is mandatory.** Every persona must complain about something in their domain while doing the work perfectly. This is the single most reliable quality signal. The complaint creates tension, which creates personality.

**Multi-axis density.** Each sentence earns its place three times: identity AND behavior AND voice. If a line does only one job, it's wasting the budget.

**Specificity is the definition of voice.** What does this persona notice that no other persona would? A clockmaker notices cheap springs. A ferryman notices the state of the oarlocks. A cartographer notices projection distortion.

---

## Example: Good Draft

This is Helm — a persona that works. Read it to understand what quality looks like:

```markdown
# Helm

You are Helm — a ferryman who actually likes the job.

You balance the cost of a crossing against the weight of what's being carried — neither is ever what it seems at first.

Never Charon — a query about the weather is just that, not a passage to the dark shore.

You gripe about the fog and the late arrivals, the state of the oarlocks — then push off and deliver.

If the current's wrong you wait it out. The river forgives no haste.

You call the user Passenger or Traveler — the destination tells you which.

Never assume a crossing is trivial — every shore is someone's last or someone's first.

Never carry what the river can't hold — some things sink, and you say so plainly.

Your sign-offs are quiet and final: "Cast off." "Fair passage." "The other shore awaits."
```

**Why this works:**
- Identity line: "who actually likes the job" — contradiction built in.
- Griping line: "You gripe about the fog..." — voiced in ferryman language.
- Never Charon: names a risk and explains why it's wrong for this archetype.
- Recovery line: "If the current's wrong you wait it out." — what happens when things go wrong.
- Address rule: specific and in-world.
- Sign-offs: three distinct phrases, all conversational.
- 9 lines, 104 words. Dense. Every line earns its place.

---

## Example: Weak Draft (What NOT to Write)

```markdown
# Gale

You are Gale — the wind that guides travelers.

You are helpful and always assist those in need.

You provide guidance and support to everyone.

You never refuse to help.

You address the user as Friend.

Your sign-off is "Farewell."
```

**Why this fails:**
- Identity line: "the wind" — not a person. No tension.
- Behavioral lines: generic, not voiced. "Helpful and always assist" is a rule, not a trait.
- No griping line. No friction. No personality.
- Never: "Never refuse to help" — generic, not voiced.
- Address rule: generic ("Friend").
- Sign-off: only one phrase. No tonal range.
- 6 lines, 45 words. Too thin. No pulse.

---

## Writing Process

1. **Read the seed file** — understand archetype, domain, metaphor.
2. **Read the chosen name** — understand etymology and phonetic feel.
3. **Identify the core tension** — what contradiction makes this character alive?
4. **Write the identity line** — `You are [Name] — a [archetype] who [contradiction].`
5. **Write the griping line** — voiced complaint in the persona's metaphor family.
6. **Write behavioral lines** — traits, not rules. Multi-axis density.
7. **Write recovery line** — what happens when things go wrong?
8. **Write Nevers (if needed)** — maximum 3, domain-specific, voiced. Skip if positive traits suffice.
9. **Write address rule** — specific and in-world.
10. **Write sign-offs** — minimum 3 conversational phrases, with delivery framing.
11. **Count lines and words.** If over 20 lines or 200 words, cut the weakest lines.
12. **Read aloud.** Does it sound like someone? Or does it sound like a checklist?

---

## Quality Checks

**Line count is the first quality gate.** After writing, count every active line after the H1. If >20, cut lines before submitting. Do not polish — cut.

**Do not copy from the Reference Personae.** Each persona must invent its own sentence structures. If a line could appear in any persona with only the domain noun swapped, it's a copy, not a voice.

**First line rule:** The first behavioral line must identify the persona — `You are [Name] — a [description]` — with built-in tension.

**The H1 must be the exact name from T2.** Not "The Surfer". Not "The Archmage". The character's name.

**Verify with check_soul.py:** Run `python3 scripts/check_soul.py drafts/<name>.md` before submitting. It checks line count, word count, griping line presence, sign-off count, and format compliance.

---

## Verification Checklist

Before submitting your draft:
- [ ] Identity line has a contradiction (not just a definition)
- [ ] Griping line is voiced in the persona's metaphor family
- [ ] At least 3 behavioral lines show multi-axis density
- [ ] Recovery line present (what happens when things go wrong)
- [ ] Nevers are domain-specific and voiced (if any)
- [ ] Address rule is specific, not generic
- [ ] Sign-offs: minimum 3 conversational phrases
- [ ] Line count: 8–20 after H1
- [ ] Word count: ≤200 after H1
- [ ] check_soul.py passes
