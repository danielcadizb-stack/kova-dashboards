with open('logo_b64.txt', 'r') as f:
    logo = f.read().strip()

img_tag = f'<img src="{logo}" style="width:28px;height:28px;border-radius:8px;object-fit:cover;" alt="KOVA">'

files = {
    'financial.html': [
        ('font-family:Fraunces;font-weight:700;font-size:22px;color:#000;">&#x20BF;</div>', f'">{img_tag}</div>'),
        ('font-family:Fraunces;font-weight:700;font-size:22px;color:#000;">₿</div>', f'">{img_tag}</div>'),
        ('>₿<', f'>{img_tag}<'),
    ],
    'command.html': [
        ('>⌘<', f'>{img_tag}<'),
        ('"font-size:20px;color:var(--ink);">⌘</div>', f'">{img_tag}</div>'),
    ],
    'index.html': [
        ('>₿<', f'>{img_tag}<'),
        ('>⌘<', f'>{img_tag}<'),
    ]
}

for fname, replacements in files.items():
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            c = f.read()
        count = 0
        for old, new in replacements:
            n = c.count(old)
            if n > 0:
                c = c.replace(old, new)
                count += n
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f'{fname}: {count} reemplazos | logo count: {c.count("data:image/png")}')
    except FileNotFoundError:
        print(f'{fname}: no encontrado')