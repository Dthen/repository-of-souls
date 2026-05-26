import re
with open('refined/dale.md') as f:
    lines = f.readlines()

active_lines = [l for l in lines if l.strip() and not l.startswith('# ')]
print(f'Total lines: {len(lines)}')
print(f'Active lines: {len(active_lines)}')

total_words = 0
for l in active_lines:
    words = re.findall(r"[A-Za-z0-9'\-]+", l)
    total_words += len(words)
    print(f'  {len(words):3d}w: {l.strip()}')

print(f'\nTotal word count (alphanumeric tokens): {total_words}')