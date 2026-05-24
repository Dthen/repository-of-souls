import re
path = '/home/kimbo/.hermes/projects/soul-repository/docs/index.html'

with open(path, 'r') as f:
    content = f.read()

# Show entry in JSON blob starts with "name": "Show", "slug": "show"
# Replace "name": "Show" and "slug": "show" but only in the JSON blob section
old_name = '"name": "Show"'
new_name = '"name": "Huck"'
old_slug = '"slug": "show"'
new_slug = '"slug": "huck"'

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
    print("Replaced name: Show -> Huck")
else:
    print("WARNING: name Show not found in blob")

# Replace slug
if old_slug in blob:
    blob = blob.replace(old_slug, new_slug)
    print("Replaced slug: show -> huck")
else:
    print("WARNING: slug show not found in blob")

# Replace # Show in content
old_content_name = '"# Show\\n'
new_content_name = '"# Huck\\n'
if old_content_name in blob:
    blob = blob.replace(old_content_name, new_content_name)
    print("Replaced content # Show -> # Huck")
else:
    # Try without extra escape
    old_content_name2 = '"# Show\n'
    new_content_name2 = '"# Huck\n'
    if old_content_name2 in blob:
        blob = blob.replace(old_content_name2, new_content_name2)
        print("Replaced content # Show -> # Huck (no-escape)")
    else:
        print("WARNING: content # Show not found")
        
# Replace "You are Show" -> "You are Huck"
old_you_are = '"You are Show'
new_you_are = '"You are Huck'
if old_you_are in blob:
    blob = blob.replace(old_you_are, new_you_are)
    print("Replaced 'You are Show' -> 'You are Huck'")
else:
    print("WARNING: 'You are Show' not found in blob")

content = before_blob + blob + after_blob

with open(path, 'w') as f:
    f.write(content)

print("Done - index.html updated successfully")
