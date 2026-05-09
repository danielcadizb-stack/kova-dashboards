with open('logo_b64.txt', 'r') as f:
    logo = f.read().strip()

with open('social.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace K text in slides - all variations
old1 = 'font-weight:800;font-size:14px;color:#000;">K</div>'
new1 = f'"><img src="{logo}" style="width:28px;height:28px;border-radius:6px;object-fit:cover;" alt="KOVA"></div>'

count = c.count(old1)
c = c.replace(old1, new1)
print(f'Replaced: {count}')

with open('social.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Done')