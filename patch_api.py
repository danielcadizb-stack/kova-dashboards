key = "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"

headers_old = "'Content-Type':'application/json'"
headers_new = f"'Content-Type':'application/json','x-api-key':'{key}','anthropic-version':'2023-06-01','anthropic-dangerous-allow-browser':'true'"

for fname in ['financial.html', 'social.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        c = f.read()
    count = c.count(headers_old)
    c = c.replace(headers_old, headers_new)
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"{fname}: {count} reemplazos")