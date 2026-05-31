# Direct test of the split behavior
line = "You are Stitch \u2014 a pattern matcher who sews the seams the world forgot to close."

words_raw = line.split()
print(f"Raw split: {len(words_raw)} words")
for i, w in enumerate(words_raw):
    print(f"  [{i}] '{w}'")

print()

# After em-dash replacement
line_replaced = line.replace('\u2014', ' ')
words_replaced = line_replaced.split()
print(f"Replaced split: {len(words_replaced)} words")
for i, w in enumerate(words_replaced):
    print(f"  [{i}] '{w}'")
