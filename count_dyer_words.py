with open('refined/hugh.md') as f:
    lines = f.readlines()
body = ''.join(lines[2:])  # skip H1 and blank line
words = body.split()
print(f'Body word count: {len(words)}')
for i, line in enumerate(lines[2:], start=3):
    print(f"  L{i}: '{line.strip()}' -> {len(line.strip().split())} words")