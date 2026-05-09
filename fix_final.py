with open('social.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Find header logo
for search in ['logo-k"', 'hdr', '<header', 'SOCIAL INTELLIGENCE']:
    idx = c.find(search)
    if idx > 0:
        print(f"'{search}' at {idx}:")
        print(repr(c[idx:idx+200]))
        print()