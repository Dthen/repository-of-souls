with open('docs/index.html', 'r') as f:
    content = f.read()

# Replace the remaining "You are Milton" in the content body
old = '\\n\\nYou are Milton'
new = '\\n\\nYou are Folger'

count = content.count(old)
print(f'Found {count} occurrences of "{old}"')

if count > 0:
    content = content.replace(old, new)
    with open('docs/index.html', 'w') as f:
        f.write(content)
    print('Done')
else:
    # Try different variants
    import re
    # Find all "Milton" occurrences and show context
    for m in re.finditer(r'.{0,20}Milton.{0,20}', content):
        print(repr(m.group()))
