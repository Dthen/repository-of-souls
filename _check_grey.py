import re

with open('refined/grey.md') as f:
    lines = f.readlines()

# Active lines: non-blank lines after H1 (line 1)
active = [l.strip() for l in lines[1:] if l.strip()]
print(f'Active lines ({len(active)}):')
for i, l in enumerate(active):
    print(f'  L{i+1}: {l}')

# Word count for all behavioural lines
words = sum(len(re.findall(r"\b\w+\b", l)) for l in active)
print(f'\nTotal word count (excl H1): {words}')

# Sign-off line - count quoted phrases
so_line = [l for l in active if 'sign-off' in l.lower() or 'Your sign-offs' in l]
if so_line:
    quotes = re.findall(r'"[^"]*"', so_line[0])
    print(f'Sign-off line: {so_line[0]}')
    print(f'Quoted phrases ({len(quotes)}): {quotes}')