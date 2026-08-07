#!/usr/bin/env python3
"""SOUL.md constraint checker — automated compliance gate.

Usage: python3 scripts/check_soul.py <path/to/soul.md>

Checks all mechanical compliance rules so reviewers (Evaluator, Publisher) can focus on quality.

Exit: 0 if all pass, 1 if any fail.
"""
import sys, re, os

if len(sys.argv) < 2:
    print("Usage: python3 scripts/check_soul.py <path/to/soul.md>")
    sys.exit(1)

path = sys.argv[1]

# --- filename case check ---
filename = os.path.basename(path)
if filename != filename.lower():
    print(f'FAIL: filename is not lowercase ({filename}) — rename to {filename.lower()}')
    sys.exit(1)

with open(path) as f:
    lines = f.readlines()

name_slug = filename.replace('.md', '')

active = [l.strip() for l in lines[1:] if l.strip()]  # after H1
if not active:
    print("FAIL: no content after H1")
    sys.exit(1)

results = []

def check(name, passed, detail=""):
    results.append((name, passed, detail))
    if detail:
        print(f'  {name}: {"PASS" if passed else "FAIL"} — {detail}')
    else:
        print(f'  {name}: {"PASS" if passed else "FAIL"}')
    return passed

# H1 check — v5.2.2.1: relaxed from exact-match to prefix. Multi-word names/titles are
# legitimate and the reference persona proves it: Brendan's H1 is "# Brendan the Wizen"
# (reference-personae.md) — the old exact-match rule rejected the reference persona.
# Hyphenated/compound slugs split on '-' and compare against the first words of the H1,
# so 'brendan-the-wizen.md' with H1 "# Brendan the Wizen" passes.
h1 = lines[0].strip()
name_words = name_slug.split('-')
h1_words = h1.lstrip('#').strip().split()
pass_h1 = len(h1_words) >= len(name_words) and all(
    a.lower().strip('.,:;!?()') == b.lower().strip('.,:;!?()')
    for a, b in zip(h1_words, name_words)
)
check('H1 starts with "# Name"', pass_h1, f'got "{h1[:50]}"' if not pass_h1 else '')

# First active line — v5.2.2.1: relaxed from "You are [Name]" to "You are ...". The
# identity line must come first (attention research), but it need not repeat the name —
# Brendan's first line is "You are an eighth-level Wizard of the Stack." because his H1
# already carries the name. The name-repeat requirement was a proxy, not evidence.
first = active[0]
pass_first = first.startswith("You are")
check('First line is "You are ..." identity', pass_first, f'got "{first[:50]}"' if not pass_first else '')

# Line count — v5.2.2: floor lowered from 8 to 5. The 8-line floor had no evidence
# and failed the reference personae (reference personae fit: Kimbo works at 6 lines).
# The cap stays — it is the context-economy bound.
total_lines = len(active)
pass_lines = 5 <= total_lines <= 20
check('Lines 5–20', pass_lines, f'{total_lines} lines' if not pass_lines else '')

# Word count
text = ' '.join([l.replace('—', ' ').replace('–', ' ') for l in active])
words = text.split()
total_words = len(words)
pass_words = total_words <= 200
check('Words ≤200', pass_words, f'{total_words} words' if not pass_words else '')

# Nevers
never_lines = [l for l in active if l.startswith('Never')]
nevers = len(never_lines)
pass_nevers = nevers <= 3
check('Nevers ≤3', pass_nevers, f'{nevers} Nevers' if not pass_nevers else '')

# Multiple Nevers on one line — check REMOVED in v5.2.2: Brendan's reference persona
# clusters three voiced Nevers on one line ("Never Gandalf. Never cryptic. Never
# withhold aid — merely process it duly.") as a deliberate stylistic trio. The ≤3
# total cap above is the evidence-backed constraint; line placement is voice.

# Griping-line check REMOVED in v5.2.1 — the automated checker must not enforce creative content.
# Compliance = mechanical format; vitality = LLM-judged quality (per research-prompt-engineering:
# quality evaluation belongs to the Evaluator, not to regexes). The old regex list literally
# required "always the \w+" / "You'd think" / "cheap \w+" patterns — it force-fed pipeline
# fingerprints into every soul that passed. A soul carries vitality through any channel
# (complaint, quiet pride, protectiveness, whimsy, ...); no regex can judge that.

# Sign-off line — v5.2.2: the ≥3-phrase requirement is gone. No evidence for a count of
# three; the reference personae fail it (Kimbo's entire sign-off is "Your sign-offs are
# brief." — zero quoted phrases, and it is perfect). What matters: a sign-off framing
# line exists (or quoted phrases), voiced in the character's own metaphor. Quality of
# sign-offs is Evaluator territory; the peak-end research supports sign-offs mattering,
# not a minimum count.
quotes = []
sign_off_line = ""
for l in active:
    if 'sign-off' in l.lower():
        quotes = re.findall(r'"([^"]*)"', l)
        sign_off_line = l
        break
pass_signoff = bool(sign_off_line) or len(quotes) >= 1
check('Sign-off framing present', pass_signoff, 'No sign-off line found' if not pass_signoff else '')

# Sign-off framing — not physical action
PHYSICAL_ACTIONS = [
    r'\bsound\b.*\bof\b',
    r'\bnod\b.*\bto\b',
    r'\bgesture\b',
    r'\bclose\b.*\bwith\b',
    r'\bshut\b',
    r'\bfalling\b',
    r'\brubber\b.*\bmeeting\b',
    r'\bthe\b\s+\bcraft\b',
]
physical_found = any(re.search(p, sign_off_line, re.I) for p in PHYSICAL_ACTIONS) if sign_off_line else False
check('Sign-off framing (not physical)', not physical_found,
      f'Physical action: "{sign_off_line[:60]}..."' if physical_found else '')

# Second person throughout — third-person intrusion AFTER identity line
third_person_lines = []
# Check for standalone "he" / "she" (not part of another word)
for l in active[1:]:  # skip identity line
    # "he" or "she" as standalone words
    if re.search(r'\bhe\b', l, re.I) and not re.search(r'\bthe\b', l, re.I):
        third_person_lines.append(l[:60])
    elif re.search(r'\bshe\b', l, re.I):
        third_person_lines.append(l[:60])
    # "a/the [noun] who" is third-person description — only flagged when the line ALSO
    # carries a third-person pronoun (he/she/his/her/they). Second-person lines like
    # "you're the one who remembers" are not intrusions.
    elif (re.search(r'\b(a|the)\s+\w+\s+\bwho\b', l, re.I)
          and re.search(r'\b(he|she|his|her|they)\b', l, re.I)):
        third_person_lines.append(l[:60])
pass_third_person = len(third_person_lines) == 0
check('Second person throughout', pass_third_person,
      f'Found: "{third_person_lines[0][:50]}..."' if third_person_lines else '')

# No literal system tool names
TOOL_NAMES = ['grep', 'sed', 'curl', 'python', 'bash', 'awk', 'perl', 'ruby', 'node', 'npm', 'git', 'ssh', 'scp', 'vim', 'nano']
tool_lines = []
for l in active:
    lower_l = f' {l.lower()} '
    for tool in TOOL_NAMES:
        if f' {tool} ' in lower_l:
            tool_lines.append(f'"{l[:40]}..." contains "{tool}"')
            break
pass_tools = len(tool_lines) == 0
check('No literal tool names', pass_tools,
      '; '.join(tool_lines[:2]) if tool_lines else '')

# No dense repetition — two lines with ≥80% word overlap
repetition_found = False
for i in range(len(active)):
    for j in range(i + 1, len(active)):
        w1 = set(active[i].lower().split())
        w2 = set(active[j].lower().split())
        if len(w1) > 3 and len(w2) > 3:
            overlap = len(w1 & w2) / max(len(w1), len(w2))
            if overlap >= 0.8:
                repetition_found = True
                break
    if repetition_found:
        break
check('No dense repetition', not repetition_found, 'Two lines share ≥80% words' if repetition_found else '')

# Recovery-line check REMOVED in v5.2.1 — same disease as the griping check: a regex list
# ("If \w+", "When \w+", "until", "wrong", "fail", ...) forced every soul to contain a
# formulaic recovery sentence. Recovery/fallibility is one character choice among many;
# whether the soul handles being wrong is Evaluator territory, not compliance.

# Summary
all_pass = all(r[1] for r in results)
passed = sum(1 for r in results if r[1])
print(f'\n{"ALL PASS" if all_pass else "SOME CHECKS FAILED"} — {passed}/{len(results)} checks passed')
sys.exit(0 if all_pass else 1)
