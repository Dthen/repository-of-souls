# Check the actual bytes around the em-dash
with open('refined/stitch.md', 'rb') as f:
    raw = f.read()

# Find the first em-dash (U+2014 = \xe2\x80\x94 in UTF-8)
idx = raw.find(b'\xe2\x80\x94')
print(f"First em-dash at byte {idx}")
# Show bytes around it
start = max(0, idx - 5)
end = min(len(raw), idx + 10)
print(f"Bytes around: {raw[start:end]}")
print(f"Hex: {raw[start:end].hex()}")

# Check if there's also a hyphen-minus nearby
line1 = raw.split(b'\n')[2]  # Line 3 (0-indexed from line 1)
print(f"\nLine 1 (active): {line1}")
print(f"Hex: {line1.hex()}")

# Check each character
chars = list(line1.decode('utf-8'))
print(f"\nCharacters in line 1:")
for i, c in enumerate(chars):
    print(f"  [{i}] U+{ord(c):04X} '{c}' (type={type(c).__name__})")
