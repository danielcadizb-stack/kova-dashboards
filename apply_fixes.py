with open('social.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Fix 1: Replace type select with all social networks
old = '<select class="cm-sl" id="ds-type">'
idx = c.find(old)
end = c.find('</select>', idx) + 9
old_block = c[idx:end]

new_block = '''<select class="cm-sl" id="ds-type">
  <optgroup label="── INSTAGRAM ──">
    <option value="carrusel">Carrusel Instagram (5 slides 1080x1080)</option>
    <option value="post-cuadrado">Post cuadrado Instagram (1080x1080)</option>
    <option value="story-ig">Story Instagram (1080x1920)</option>
    <option value="reel-cover">Portada Reel Instagram</option>
  </optgroup>
  <optgroup label="── TIKTOK ──">
    <option value="tiktok-cover">Portada TikTok (1080x1920)</option>
    <option value="tiktok-overlay">Texto overlay TikTok</option>
    <option value="tiktok-gancho">Slide gancho TikTok</option>
  </optgroup>
  <optgroup label="── LINKEDIN ──">
    <option value="linkedin-post">Post LinkedIn con imagen (1200x628)</option>
    <option value="linkedin-carrusel">Carrusel LinkedIn PDF (5 slides)</option>
    <option value="linkedin-quote">Quote profesional LinkedIn</option>
  </optgroup>
  <optgroup label="── FACEBOOK ──">
    <option value="facebook-post">Post Facebook (1200x630)</option>
    <option value="facebook-story">Story Facebook (1080x1920)</option>
  </optgroup>
  <optgroup label="── UNIVERSAL ──">
    <option value="quote">Quote impactante (todas las redes)</option>
    <option value="stat">Estadistica impactante</option>
    <option value="antes-despues">Antes y despues de KOVA</option>
  </optgroup>
</select>'''

c = c.replace(old_block, new_block)
print('Select replaced:', new_block[:30] in c)

# Fix 2: Robust JSON parsing - add fallback
old_parse = "    let txt = d.content?.[0]?.text || '{}';\n    txt = txt.replace(/```json|```/g,'').trim();\n    const data = JSON.parse(txt);"
new_parse = """    let txt = d.content?.[0]?.text || '{}';
    txt = txt.replace(/```json|```/g,'').trim();
    const jsonMatch = txt.match(/\\{[\\s\\S]*\\}/);
    if(jsonMatch) txt = jsonMatch[0];
    let data;
    try { data = JSON.parse(txt); }
    catch(e) {
      data = {
        slides:[{titulo:'KOVA VENTAS CON IA',contenido:'Responde objeciones en segundos. Practica con ALEX. Planifica con MAIA.'},{titulo:'PRUEBALO GRATIS',contenido:'kova-app.net · Sin tarjeta de credito'}],
        caption:'KOVA transforma como vendes con IA. Descarga gratis.',
        hashtags:'#KOVA #ventas #IA #emprendimiento #pymes',
        instrucciones:'Descarga el diseno y publícalo en tus redes.'
      };
    }"""

c = c.replace(old_parse, new_parse)
print('JSON fix applied:', 'jsonMatch' in c)

# Fix 3: Truncate context
old_ctx = "    const prompt = `Eres un experto en diseño de contenido para redes sociales de KOVA"
new_ctx_prefix = "    const ctxShort = ctx ? ctx.substring(0,150) : '';\n    " + old_ctx
c = c.replace(old_ctx, new_ctx_prefix, 1)

with open('social.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Done - size:', len(c))