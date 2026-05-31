#!/usr/bin/env python3
import re
with open('refined/gage.md') as f:
    lines = f.readlines()
active = [l.strip() for l in lines[1:] if l.strip()]
for i, l in enumerate(active, 1):
    text = l.replace('\u2014', ' ').replace('\u2013', ' ')
    wc = len(text.split())
    print(f'  L{i}: {wc}w  {l[:80]}')
total = sum(len(l.replace('\u2014', ' ').replace('\u2013', ' ').split()) for l in active)
print(f'Total: {total} words, {len(active)} lines')
