# Debug: trace exactly what check_soul.py does
path = 'refined/stitch.md'
with open(path) as f:
    lines = f.readlines()

active = [l.strip() for l in lines[1:] if l.strip()]

# This is exactly what check_soul.py does
text = ' '.join([l.replace('\u2014', ' ').replace('\u2013', ' ') for l in active])
words = text.split()
print(f"check_soul.py method: {len(words)} words")

# Count lines with em-dashes
em_dash_count = 0
for i, l in enumerate(active):
    if '\u2014' in l:
        em_dash_count += 1
        # Show what happens after replacement
        replaced = l.replace('\u2014', ' ')
        orig_words = l.split()
        repl_words = replaced.split()
        print(f"  L{i+1}: orig={len(orig_words)}, replaced={len(repl_words)} | '{l[:60]}...'")

print(f"\nLines with em-dash: {em_dash_count}")

# Now count the actual words manually
# The em-dash replacement turns "X — Y" into "X   Y" (space-space-space)
# split() treats multiple spaces as one separator, so word count should be same
# Unless... the em-dash is glued to adjacent words
for i, l in enumerate(active):
    if '\u2014' in l:
        # Check chars around em-dash
        idx = l.index('\u2014')
        before = l[idx-1] if idx > 0 else '<START>'
        after = l[idx+1] if idx+1 < len(l) else '<END>'
        print(f"  L{i+1} around em-dash: ...'{before}' — '{after}'...")
