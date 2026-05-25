#!/usr/bin/env python3
"""
SOUL.md constraint checker.
Usage: python3 scripts/check_soul.py <path/to/soul.md>
Checks: line count (8-20 active), word count (≤200), nevers (≤3),
        sign-off phrase count (≥3), first line starts with "You are Name",
        H1 matches name slug.
"""
import sys, re, os

if len(sys.argv) < 2:
    print("Usage: python3 scripts/check_soul.py <path/to/soul.md>")
    sys.exit(1)

path = sys.argv[1]
with open(path) as f:
    lines = f.readlines()

name_slug = os.path.basename(path).replace('.md', '')

active = [l.strip() for l in lines[1:] if l.strip()]  # after H1
if not active:
    print("FAIL: no content after H1")
    sys.exit(1)

# H1 check
h1 = lines[0].strip()
pass_h1 = h1 == f"# {name_slug.capitalize()}"
print(f'  H1 exact? {"PASS" if pass_h1 else "FAIL"} ({h1})')

# First active line
first = active[0]
pass_first = first.startswith(f"You are {name_slug.capitalize()}") or first.startswith(f"You are {name_slug}")
print(f'  First line starts with "You are Name"? {"PASS" if pass_first else "FAIL"}')

# Line count
total_lines = len(active)
pass_lines = 8 <= total_lines <= 20
print(f'  Lines 8-20? {"PASS" if pass_lines else "FAIL"} ({total_lines})')

# Word count
text = ' '.join([l.replace('\u2014', ' ').replace('\u2013', ' ') for l in active])
words = text.split()
total_words = len(words)
pass_words = total_words <= 200
print(f'  Words <=200? {"PASS" if pass_words else "FAIL"} ({total_words})')

# Nevers
never_lines = [l for l in active if l.startswith('Never')]
nevers = len(never_lines)
pass_nevers = nevers <= 3
print(f'  Nevers <=3? {"PASS" if pass_nevers else "FAIL"} ({nevers})')

# Sign-off phrases
quotes = []
for l in active:
    if 'sign-off' in l.lower():
        quotes = re.findall(r'"([^"]*)"', l)
        break
pass_quotes = len(quotes) >= 3
print(f'  Sign-off phrases >=3? {"PASS" if pass_quotes else "FAIL"} ({len(quotes)})')
for q in quotes:
    print(f'    - "{q}"')

# Any fails?
all_pass = all([pass_h1, pass_first, pass_lines, pass_words, pass_nevers, pass_quotes])
print(f'\n{"ALL PASS" if all_pass else "SOME CHECKS FAILED"}')
sys.exit(0 if all_pass else 1)
