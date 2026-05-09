with open('command.html', 'r', encoding='utf-8') as f:
    c = f.read()

old = "  if(ttViews >= 500) alerts.push({type:'ok',icon:'🟢',title:'TikTok con tracción orgánica',desc:`${(KD.tt_views||0).toLocaleString()} views con €0 en ads. Canal más efectivo actualmente.`});"

new = "  const ttViews = KD.tt_views || 0;\n  if(ttViews >= 500) alerts.push({type:'ok',icon:'🟢',title:'TikTok con tracción orgánica',desc:`${(KD.tt_views||0).toLocaleString()} views con €0 en ads. Canal más efectivo actualmente.`});"

count = c.count(old)
c = c.replace(old, new)
print(f"Fix aplicado: {count} reemplazos")

with open('command.html', 'w', encoding='utf-8') as f:
    f.write(c)