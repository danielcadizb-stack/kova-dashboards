import re

# Fix financial.html
with open('financial.html', 'r', encoding='utf-8') as f:
    c = f.read()

print("Before - anthropic.com count:", c.count('anthropic.com'))
print("Before - vercel count:", c.count('vercel'))

# Replace API constant
c = c.replace(
    "const API='https://api.anthropic.com/v1/messages'",
    "const API='https://kova-api.vercel.app/api/proxy'"
)

print("After - anthropic.com count:", c.count('anthropic.com'))
print("After - vercel count:", c.count('vercel'))

with open('financial.html', 'w', encoding='utf-8') as f:
    f.write(c)

# Fix social.html
with open('social.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace(
    "const API='https://api.anthropic.com/v1/messages'",
    "const API='https://kova-api.vercel.app/api/proxy'"
)

with open('social.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Done")