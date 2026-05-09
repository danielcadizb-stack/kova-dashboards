with open('logo_b64.txt', 'r') as f:
    logo = f.read().strip()

files = ['ops.html', 'financial.html', 'command.html', 'index.html']

for fname in files:
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            c = f.read()
        
        original = c
        
        # Replace K text logos — all variations
        replacements = [
            ('>K</div>', f'><img src="{logo}" style="width:28px;height:28px;border-radius:6px;object-fit:cover;" alt="KOVA"></div>'),
            ('logo-k">K<', f'logo-k"><img src="{logo}" style="width:100%;height:100%;border-radius:10px;object-fit:cover;" alt="KOVA"><'),
            ('>⚙</div>', f'><img src="{logo}" style="width:28px;height:28px;border-radius:6px;object-fit:cover;" alt="KOVA"></div>'),
        ]
        
        count = 0
        for old, new in replacements:
            n = c.count(old)
            if n > 0:
                c = c.replace(old, new)
                count += n
        
        if c != original:
            with open(fname, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f'{fname}: {count} reemplazos')
        else:
            print(f'{fname}: sin cambios — buscando logo existente...')
            print(f'  logo img: {c.count("data:image/png;base64")}')
    except FileNotFoundError:
        print(f'{fname}: no encontrado')