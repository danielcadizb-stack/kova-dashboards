key = "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"

correct = f"'Content-Type':'application/json','x-api-key':'{key}','anthropic-version':'2023-06-01','anthropic-dangerous-allow-browser':'true'"

for fname in ['financial.html', 'social.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # Remove all variations and replace with clean version
    import re
    # Replace everything between Content-Type and the closing brace of headers
    c = re.sub(
        r"'Content-Type':'application/json'[^}]*?(?='anthropic-dangerous-allow-browser':'true')'anthropic-dangerous-allow-browser':'true'",
        correct,
        c
    )
    # Final clean replacement
    c = re.sub(
        r"'Content-Type':'application/json'(?:,'x-api-key':'[^']*')+(?:,'anthropic-version':'[^']*')+(?:,'anthropic-dangerous-allow-browser':'[^']*')+",
        correct,
        c
    )
    
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(c)
    
    # Verify
    count = c.count("anthropic-dangerous-allow-browser")
    print(f"{fname}: {count} ocurrencias de dangerous-allow-browser")