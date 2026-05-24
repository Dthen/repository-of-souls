#!/usr/bin/env python3
import sys

path = '/home/kimbo/.hermes/projects/soul-repository/docs/index.html'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# The file has literal \n (backslash + n, not actual newlines)
old = 'the book you keep and the name you answer to are the same thing.'
new = 'the tally is your trade, the ledger is your instrument, and every figure must account for itself.'

if old in content:
    # Count occurrences to make sure we're targeting the right one
    count = content.count(old)
    content = content.replace(old, new, 1)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'SUCCESS: replaced 1 of {count} occurrences')
    sys.exit(0)
else:
    print('ERROR: old string not found')
    # check if it's on line 801
    lines = content.split('\n')
    line801 = lines[800]  # 0-indexed
    if 'the book you keep' in line801:
        print('Found on line 801 but with different formatting')
        idx = line801.find('the book you keep')
        print(f'Context around match: ...{line801[idx-40:idx+80]}...')
    sys.exit(1)
