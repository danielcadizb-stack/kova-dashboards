with open('logo_b64.txt', 'r') as f:
    logo = f.read().strip()

with open('social.html', 'r', encoding='utf-8') as f:
    c = f.read()

# FIX 1: Replace select with all social networks
old_sel = '<select class="cm-sl" id="ds-type">'
idx = c.find(old_sel)
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
print("Fix 1 optgroup:", 'optgroup' in c)

# FIX 2: Add logo to makeSlideHTML
old_logo = 'font-weight:800;font-size:14px;color:#000;">K</div>'
new_logo = f'"><img src="{logo}" style="width:28px;height:28px;border-radius:6px;object-fit:cover;" alt="KOVA"></div>'
count2 = c.count(old_logo)
c = c.replace(old_logo, new_logo)
print("Fix 2 logo:", count2, "reemplazos")

# FIX 2b: Also fix header logo-k
old_logok = '>K</div>'
if 'logo-k' in c:
    idx_k = c.find('logo-k')
    chunk = c[idx_k:idx_k+200]
    if '>K</div>' in chunk:
        c = c[:idx_k] + chunk.replace('>K</div>', f'><img src="{logo}" style="width:100%;height:100%;border-radius:10px;object-fit:cover;" alt="KOVA"></div>', 1) + c[idx_k+200:]
        print("Fix 2b header logo: ok")

# FIX 3: Robust JSON parsing
old_parse = "    let txt = d.content?.[0]?.text || '{}';\n    txt = txt.replace(/```json|```/g,'').trim();\n    const data = JSON.parse(txt);"
new_parse = """    let txt = d.content?.[0]?.text || '{}';
    txt = txt.replace(/```json|```/g,'').trim();
    const jsonMatch = txt.match(/\\{[\\s\\S]*\\}/);
    if(jsonMatch) txt = jsonMatch[0];
    let data;
    try { data = JSON.parse(txt); }
    catch(e) {
      data = {
        slides:[{titulo:'KOVA VENTAS CON IA',contenido:'Responde objeciones en segundos con NOVA. kova-app.net'},{titulo:'DESCARGA GRATIS',contenido:'kova-app.net'}],
        caption:'KOVA transforma como vendes con IA. Descarga gratis en kova-app.net',
        hashtags:'#KOVA #ventas #IA #emprendimiento #pymes',
        instrucciones:'Descarga y publica en tus redes.'
      };
    }"""

count3 = c.count(old_parse)
c = c.replace(old_parse, new_parse)
print("Fix 3 JSON:", count3, "reemplazos")

# FIX 4: Add platGuides for all networks
old_guides = "  const platGuides = {"
idx_g = c.find(old_guides)
end_g = c.find("  };", idx_g) + 4
old_guides_block = c[idx_g:end_g]

new_guides_block = """  const platGuides = {
    'carrusel': '📱 <strong>Instagram Carrusel:</strong><br>1. Descarga todos los slides (boton Descargar todos PNG)<br>2. Instagram → + → Post → selecciona las 5 imagenes en orden<br>3. Pega caption + hashtags<br>4. ⏰ Hora ideal: 18:00-20:00',
    'post-cuadrado': '📱 <strong>Instagram Post:</strong><br>1. Descarga como PNG<br>2. Instagram → + → Post → sube imagen<br>3. Pega caption y hashtags<br>4. ⏰ Hora ideal: 18:00-20:00',
    'story-ig': '📖 <strong>Instagram Story:</strong><br>1. Descarga como PNG<br>2. Instagram → tu foto → + Story → sube imagen<br>3. Añade sticker enlace → kova-app.net<br>4. ⏰ Hora ideal: 9:00 o 20:00',
    'reel-cover': '🎬 <strong>Portada Reel:</strong><br>1. Descarga como PNG<br>2. Al subir el Reel → Editar portada → sube esta imagen<br>3. Mejora el CTR del reel en el feed',
    'tiktok-cover': '🎵 <strong>TikTok Portada:</strong><br>1. Descarga como PNG<br>2. Al subir video en TikTok → Seleccionar portada → sube imagen<br>3. ⏰ Hora ideal: 18:00-21:00',
    'tiktok-overlay': '🎵 <strong>TikTok Overlay:</strong><br>1. Graba screen recording de KOVA en iPhone<br>2. Importa en CapCut → añade texto generado como overlay<br>3. Activa subtitulos automaticos<br>4. ⏰ Hora ideal: 18:00-21:00',
    'tiktok-gancho': '🎵 <strong>TikTok Gancho:</strong><br>1. Usa el texto como primeros 3 segundos del video<br>2. Graba cara a camara diciendo el gancho<br>3. ⏰ Hora ideal: 18:00-21:00',
    'linkedin-post': '💼 <strong>LinkedIn Post:</strong><br>1. Descarga como PNG<br>2. LinkedIn → + → Post → adjunta imagen<br>3. Pega el caption (LinkedIn permite posts largos)<br>4. ⏰ Hora ideal: 9:00 o 12:00',
    'linkedin-carrusel': '💼 <strong>LinkedIn Carrusel PDF:</strong><br>1. Descarga todos los slides como PNG<br>2. Convierte a PDF (une las imagenes)<br>3. LinkedIn → + → Documento → sube el PDF<br>4. ⏰ Hora ideal: 9:00-12:00',
    'linkedin-quote': '💼 <strong>LinkedIn Quote:</strong><br>1. Descarga como PNG<br>2. Adjunta al post de LinkedIn<br>3. Añade reflexion personal sobre la frase<br>4. ⏰ Hora ideal: 9:00',
    'facebook-post': '📘 <strong>Facebook Post:</strong><br>1. Descarga como PNG<br>2. Facebook → Crear publicacion → añade imagen<br>3. Pega el caption<br>4. ⏰ Hora ideal: 18:00-20:00',
    'facebook-story': '📘 <strong>Facebook Story:</strong><br>1. Descarga como PNG<br>2. Facebook → + Historia → sube imagen<br>3. Añade enlace → kova-app.net<br>4. ⏰ Hora ideal: 9:00 o 20:00',
    'quote': '💬 <strong>Todas las plataformas:</strong><br>1. Descarga como PNG<br>2. Publica en Instagram, LinkedIn, Facebook y Twitter/X<br>3. En TikTok usalo como overlay de video<br>4. Ideal tambien para Stories',
    'stat': '📊 <strong>Estadistica — todas las redes:</strong><br>1. Descarga como PNG<br>2. Publica en todas las plataformas<br>3. Estadisticas generan alto engagement<br>4. Añade fuente en el caption',
    'antes-despues': '🔄 <strong>Antes y Despues:</strong><br>1. Descarga como PNG<br>2. Publica en Instagram, LinkedIn y Facebook<br>3. Muy alto engagement en todas las redes',
  };"""

c = c.replace(old_guides_block, new_guides_block)
print("Fix 4 guides:", 'tiktok-gancho' in c)

with open('social.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("\nEstado final:")
print("  html2canvas:", 'html2canvas' in c)
print("  optgroup:", 'optgroup' in c)
print("  logo img:", c.count('data:image/png;base64'))
print("  jsonMatch:", 'jsonMatch' in c)
print("  downloadPackItem:", 'downloadPackItem' in c)
print("  pack overflow:", 'overflow-x:auto' in c)
print("  platGuides all:", 'tiktok-gancho' in c)