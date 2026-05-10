with open('logo_b64.txt') as f:
    logo = f.read().strip()
with open('social_clean.html', encoding='utf-8') as f:
    c = f.read()
c = c.replace('class="logo-k">K<', 'class="logo-k"><img src="' + logo + '" style="width:100%;height:100%;border-radius:10px;object-fit:cover;" alt="KOVA"><')
import shutil
shutil.copy('social.html', 'social_backup.html')
with open('social.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Done! Logo applied, social.html updated')
print('Old file saved as social_backup.html')
