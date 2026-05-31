import re

content = open('refined/coffer.md').read()
lines = content.strip().split('\n')
h1 = lines[0]
active_lines = [l for l in lines[2:] if l.strip()]

print(f'Active lines: {len(active_lines)}')
print()

all_words = []
for i, line in enumerate(active_lines, 3):
    words = line.split()
    clean_words = [w for w in words if re.sub(r'[—,.\-!?:;\"/()\' ]', '', w) != '']
    print(f'Line {i}: {len(clean_words)} words')
    all_words.extend(clean_words)

print(f'\nTotal words after H1: {len(all_words)}')

never_lines = []
for i, line in enumerate(active_lines, 3):
    if line.strip().startswith('Never'):
        never_lines.append((i, line))
print(f'\nNever lines: {len(never_lines)}')
for num, l in never_lines:
    print(f'  Line {num}: {l}')

signoff_line = active_lines[-1]
print(f'\nSign-off line: {signoff_line}')
quotes = re.findall(r'"([^"]+)"', signoff_line)
print(f'Sign-off quotes: {len(quotes)} — {quotes}')

# Check for 'Never' in non-Never lines
print('\n--- Never in non-Never lines ---')
for i, line in enumerate(active_lines, 3):
    if not line.strip().startswith('Never') and 'never' in line.lower():
        print(f'  Line {i}: {line}')

# Check identity opening
print(f'\n--- Identity opening ---')
print(f'Line 3: {active_lines[0] if active_lines else "MISSING"}')

# Check for recovery line
print('\n--- Recovery line check ---')
for i, line in enumerate(active_lines, 3):
    lower = line.lower()
    if any(w in lower for w in ['wrong', 'break', 'error', 'fix', 'fail', 'balance', 'foot']):
        print(f'  Line {i}: {line}')

# Pipeline fingerprints
print('\n--- Pipeline fingerprints ---')
fingerprints = ['You reach for every tool', 'because follow-through is', 'You read the', 'You reads the', 'You grumble about']
for i, line in enumerate(active_lines, 3):
    for fp in fingerprints:
        if fp.lower() in line.lower():
            print(f'  Line {i}: MATCH "{fp}" in: {line}')

# Tool names
print('\n--- Tool names ---')
tool_names = ['grep', 'sed', 'curl', 'awk', 'find', 'cat', 'echo']
for i, line in enumerate(active_lines, 3):
    for tool in tool_names:
        if re.search(r'\b' + tool + r'\b', line, re.IGNORECASE):
            print(f'  Line {i}: tool name "{tool}" in: {line}')

# Dense repetition check
print('\n--- Dense repetition check ---')
concepts = {}
for i, line in enumerate(active_lines, 3):
    lower = line.lower()
    for concept in ['stores', 'seal', 'ledger', 'chest', 'signature', 'slip']:
        if concept in lower:
            if concept not in concepts:
                concepts[concept] = []
            concepts[concept].append((i, line))
for concept, lines_list in concepts.items():
    if len(lines_list) > 2:
        print(f'  Concept "{concept}" appears {len(lines_list)} times:')
        for num, l in lines_list:
            print(f'    Line {num}: {l}')

# Check for double negatives
print('\n--- Double negatives ---')
for i, line in enumerate(active_lines, 3):
    lower = line.lower()
    if 'never' in lower and ('nothing' in lower or 'no ' in lower):
        print(f'  Line {i}: {line}')

# Check sign-off framing
print(f'\n--- Sign-off framing ---')
print(f'Line: {signoff_line}')
framing = signoff_line.split(':')[0] if ':' in signoff_line else 'N/A'
print(f'Framing: {framing}')

# Check for physical action in sign-off framing
physical = ['nod', 'sound', 'gesture', 'rubber', 'falling', 'cut', 'tap']
for p in physical:
    if p in framing.lower():
        print(f'  ⚠️ Physical action in framing: "{p}"')

print('\n--- All active lines ---')
for i, line in enumerate(active_lines, 3):
    print(f'  Line {i}: {line}')
