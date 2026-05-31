with open('refined/stitch.md') as f:
    lines = f.readlines()

active = [l.strip() for l in lines[1:] if l.strip()]

# Method 1: raw split
all_words = []
for l in active:
    all_words.extend(l.split())
print(f"Raw split count: {len(all_words)}")

# Method 2: em-dash replacement (like check_soul.py)
text = ' '.join([l.replace('\u2014', ' ').replace('\u2013', ' ') for l in active])
words = text.split()
print(f"Em-dash replaced count: {len(words)}")

# Show each line's word count (raw)
print("\nLine-by-line (raw):")
for i, l in enumerate(active):
    wc = len(l.split())
    print(f"  L{i+1}: {wc:2d} | {l[:80]}")
