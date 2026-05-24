#!/usr/bin/env python3
import re
with open('/home/kimbo/.hermes/projects/soul-repository/docs/index.html', 'r') as f:
    content = f.read()

old = '"name": "Gus", "slug": "gus"'
new_short = '"name": "Roux", "slug": "roux"'

# First, find the Gus entry and its bounds
idx = content.find(old)
if idx < 0:
    print("ERROR: 'name: Gus' not found")
    exit(1)

# Replace the simple fields
content = content.replace('"name": "Gus", "slug": "gus"', new_short)

# Now replace the content - replace # Gus with # Roux in the JSON content
content = content.replace(
    '"content": "# Gus\\n\\nYou are Gus',
    '"content": "# Roux\\n\\nYou are Roux'
)

with open('/home/kimbo/.hermes/projects/soul-repository/docs/index.html', 'w') as f:
    f.write(content)

# Verify
if 'Gus' in content:
    print("WARNING: Gus still found in file")
    # Show what remains
    idx = content.find('Gus')
    if idx >= 0:
        print(f"Remaining at pos: {idx}")
        print(content[max(0,idx-50):idx+50])
else:
    print("SUCCESS: No Gus references remaining in index.html")
