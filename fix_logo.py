# Read logo base64
with open('logo_b64.txt', 'r') as f:
    logo = f.read().strip()

with open('social.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace K text logo with real image in makeSlideHTML function
old = '''<div style="width:32px;height:32px;background:${accentColor};border-radius:8px;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:14px;color:#000;">K</div>'''
new = f'''<img src="{logo}" style="width:32px;height:32px;border-radius:8px;object-fit:cover;" alt="KOVA">'''
count = c.count(old)
c = c.replace(old, new)
print(f'Slides logo replaced: {count}')

# Also replace in header of social dashboard if exists
old2 = '''<div class="logo-k">K</div>'''
new2 = f'''<img src="{logo}" style="width:42px;height:42px;border-radius:12px;object-fit:cover;" alt="KOVA">'''
count2 = c.count(old2)
c = c.replace(old2, new2)
print(f'Header logo replaced: {count2}')

with open('social.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Done')