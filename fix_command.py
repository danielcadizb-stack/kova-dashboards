with open('command.html', 'r', encoding='utf-8') as f:
    c = f.read()

print("anthropic.com:", c.count('anthropic.com'))
print("vercel proxy:", c.count('kova-api.vercel.app'))