key = "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"

for fname in ['financial.html', 'social.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # Find first occurrence and extract the messy headers block
    import re
    # Replace ALL header variations with one clean version
    pattern = r"'Content-Type':'application/json'(?:[^}](?!body:))*?'anthropic-dangerous-allow-browser':'true'"
    replacement = f"'Content-Type':'application/json','x-api-key':'{key}','anthropic-version':'2023-06-01','anthropic-dangerous-allow-browser':'true'"
    
    c_new = re.sub(pattern, replacement, c)
    count = c_new.count("anthropic-dangerous-allow-browser")
    
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(c_new)
    
    print(f"{fname}: {count} ocurrencias (esperado: 2 para financial, 4 para social)")