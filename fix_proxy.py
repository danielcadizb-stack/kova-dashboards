for fname in ['financial.html', 'social.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # Replace API URL
    c = c.replace(
        "const API='https://api.anthropic.com/v1/messages';",
        "const API='https://kova-api.vercel.app/api/proxy';"
    )
    
    # Remove API key and extra headers - use simple headers for proxy
    import re
    c = re.sub(
        r"headers:\{'Content-Type':'application/json'[^}]*\}",
        "headers:{'Content-Type':'application/json'}",
        c
    )
    
    count = c.count('kova-api.vercel.app/api/proxy')
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"{fname}: {count} reemplazos de URL")