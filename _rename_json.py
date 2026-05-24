import re
path = '/home/kimbo/.hermes/projects/soul-repository/docs/index.html'

with open(path, 'r') as f:
    content = f.read()

# Silver entry in JSON blob starts with "name": "Silver", "slug": "silver"
# This script was originally used for Show->Huck, then Huck->Silver
# Now it's the final version.
old_name = '"name": "Huck"'
new_name = '"name": "Silver"'
old_slug = '"slug": "huck"'
new_slug = '"slug": "silver"'

# Find the JSON blob section (between const souls and ];)
blob_start = content.find('const souls = [')
blob_end = content.find('];', blob_start)

if blob_start < 0:
    print("ERROR: Could not find const souls section")
    exit(1)

before_blob = content[:blob_start]
blob = content[blob_start:blob_end + 2]
after_blob = content[blob_end + 2:]

# Replace name
if old_name in blob:
    blob = blob.replace(old_name, new_name)
    print("Replaced name: Huck -> Silver")
else:
    print("WARNING: name Huck not found in blob")

# Replace slug
if old_slug in blob:
    blob = blob.replace(old_slug, new_slug)
    print("Replaced slug: huck -> silver")
else:
    print("WARNING: slug huck not found in blob")

# Replace # Huck in content
old_content_name = '"# Huck\\n'
new_content_name = '"# Silver\\n'
if old_content_name in blob:
    blob = blob.replace(old_content_name, new_content_name)
    print("Replaced content # Huck -> # Silver")
else:
    # Try without extra escape
    old_content_name2 = '"# Huck\n'
    new_content_name2 = '"# Silver\n'
    if old_content_name2 in blob:
        blob = blob.replace(old_content_name2, new_content_name2)
        print("Replaced content # Huck -> # Silver (no-escape)")
    else:
        print("WARNING: content # Huck not found")
        
# Replace "You are Huck" -> "You are Silver"
old_you_are = '"You are Huck'
new_you_are = '"You are Silver'
if old_you_are in blob:
    blob = blob.replace(old_you_are, new_you_are)
    print("Replaced 'You are Huck' -> 'You are Silver'")
else:
    print("WARNING: 'You are Huck' not found in blob")

content = before_blob + blob + after_blob

with open(path, 'w') as f:
    f.write(content)

print("Done - index.html updated successfully")
print("Note: This script was originally Show->Huck, now updated to Huck->Silver")
