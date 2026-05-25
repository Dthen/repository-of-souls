import re
text = open('refined/morse.md').read()
lines = text.strip().split('\n')[2:]  # skip '# Morse' and blank
lines = [l for l in lines if l.strip()]
print('Active line count:', len(lines))
all_tokens = []
for l in lines:
    tokens = l.split()
    all_tokens.extend(tokens)
words = [t for t in all_tokens if re.search(r'[A-Za-z0-9]', t)]
print('Word count (tokens with alphanumeric chars):', len(words))
print('Raw whitespace-split token count:', len(all_tokens))
print()
for i, l in enumerate(lines, 1):
    ws = l.split()
    actual = [t for t in ws if re.search(r'[A-Za-z0-9]', t)]
    print(f'L{i}: {len(actual)} words | {l}')