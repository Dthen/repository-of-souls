with open('refined/stellan.md') as f:
    content = f.read()

lines = [l.strip() for l in content.split('\n') if l.strip()]
if lines[0].startswith('#'):
    lines = lines[1:]

print('Active lines: %d' % len(lines))
for i, l in enumerate(lines, 1):
    wc = len(l.split())
    print('  L%d: %2dw | %s' % (i, wc, l[:80]))

wc_total = sum(len(l.split()) for l in lines)
print('\nWord count after H1: %d' % wc_total)
print('Under 200: %s' % ('YES' if wc_total <= 200 else 'NO - over by %d' % (wc_total - 200)))
print('Lines 8-20: %s' % ('YES' if 8 <= len(lines) <= 20 else 'NO'))

# Nevers check
never_lines = [l for l in lines if l.startswith('Never')]
print('\nNever lines: %d' % len(never_lines))
for nl in never_lines:
    never_count = nl.count('Never')
    print('  %s (%d Never statements)' % (nl[:80], never_count))
    if never_count > 2:
        print('  FAIL: >2 Nevers on one line')

# Sign-off check
import re
for l in lines:
    if 'sign-off' in l.lower():
        quotes = re.findall(r'"([^"]*)"', l)
        print('\nSign-off phrases: %d' % len(quotes))
        for q in quotes:
            print('  - "%s"' % q)
        print('>=3: %s' % ('YES' if len(quotes) >= 3 else 'NO'))