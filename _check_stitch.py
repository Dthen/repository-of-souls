import re
with open('refined/stitch.md') as f:
    content = f.read()
lines = content.strip().split('\n')
active = [l for l in lines[1:] if l.strip()]
words = []
for l in active:
    words.extend(l.split())
print(f'Active lines: {len(active)}')
print(f'Word count: {len(words)}')
# Check sign-off line
for i,l in enumerate(lines):
    if 'sign-off' in l.lower():
        quoted = re.findall(r'"([^"]+)"', l)
        print(f'Sign-off line (L{i+1}): {l.strip()}')
        print(f'Quoted phrases: {quoted} ({len(quoted)})')
# Check Nevers
for i,l in enumerate(lines):
    if l.strip().startswith('Never'):
        print(f'Never line (L{i+1}): {l.strip()}')
print(f'Identity line (L3): {lines[2].strip() if len(lines)>2 else "N/A"}')
