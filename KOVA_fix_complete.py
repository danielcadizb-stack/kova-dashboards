#!/usr/bin/env python3
"""KOVA Social Dashboard - Complete Fixer Script"""

with open("social.html", "r", encoding="utf-8") as f:
    content = f.read()

lines = content.split("\n")
total = len(lines)
print(f"File has {total} lines")

# Find the captionHtml section
caption_start = -1
for i, line in enumerate(lines):
    if "var captionHtml = " in line and i > 480:
        caption_start = i
        break

if caption_start == -1:
    print("ERROR: captionHtml not found")
    exit(1)

print(f"Found captionHtml at line {caption_start+1}")

# Find the end of the if(data.caption) block
caption_end = caption_start
for i in range(caption_start, min(caption_start+20, total)):
    if lines[i].strip() == "}":
        caption_end = i
        break

# Find instr.innerHTML line
instr_line = -1
for i in range(caption_end, min(caption_end+5, total)):
    if "instr.innerHTML" in lines[i]:
        instr_line = i
        break

print(f"Block: lines {caption_start+1} to {caption_end+1}, instr at {instr_line+1}")

# Replace with clean version
new_lines = lines[:caption_start] + [
    "    var captionHtml = '';",
    "    if(data.caption) {",
    "      window._designCaption = (data.caption||'') + ' ' + (data.hashtags||'');",
    "      var d1 = document.createElement('div');",
    "      d1.style.marginTop = '14px';",
    "      var lbl = document.createElement('div');",
    "      lbl.style.cssText = 'font-family:JetBrains Mono;font-size:10px;color:var(--text3);margin-bottom:6px;';",
    "      lbl.textContent = 'CAPTION LISTO PARA COPIAR';",
    "      var txt = document.createElement('div');",
    "      txt.style.cssText = 'background:var(--bg3);border-radius:8px;padding:12px;font-size:12px;color:var(--text2);line-height:1.7;';",
    "      txt.textContent = data.caption||'';",
    "      var btn = document.createElement('button');",
    "      btn.className = 'cbtn';",
    "      btn.style.cssText = 'margin-top:8px;width:100%;';",
    "      btn.textContent = 'Copiar caption + hashtags';",
    "      btn.onclick = function(){ cpDesignCaption(); };",
    "      d1.appendChild(lbl); d1.appendChild(txt); d1.appendChild(btn);",
    "      captionHtml = d1.outerHTML;",
    "    }",
] + lines[caption_end+1:]

# Now fix instr.innerHTML - find it in new_lines
for i, line in enumerate(new_lines):
    if "instr.innerHTML" in line and i > 480:
        new_lines[i] = "    instr.innerHTML = '<div style="font-size:13px;color:var(--text2);line-height:1.9;">' + guide + '</div>' + captionHtml;"
        print(f"Fixed instr.innerHTML at line {i+1}")
        break

# Also fix updKPI if still broken
for i, line in enumerate(new_lines):
    if "updKPI" in line and "''" in line and i > 480:
        import re
        fixed = re.sub(r"onchange="updKPI\(''[^']*'\s*\+\s*([\w.]+)\s*\+\s*'',", 
                      r'data-id="\1" onchange="updKPI(this.dataset.id,', line)
        if fixed != line:
            new_lines[i] = fixed
            print(f"Fixed updKPI at line {i+1}")

# Also fix updPlat if still broken
for i, line in enumerate(new_lines):
    if "updPlat" in line and "''" in line and i > 480:
        import re
        fixed = re.sub(r"onchange="updPlat\(''[^']*'',[^']*'',",
                      r'data-plat="\1" data-key="\2" onchange="updPlat(this.dataset.plat,this.dataset.key,', line)
        if fixed != line:
            new_lines[i] = fixed
            print(f"Fixed updPlat at line {i+1}")

with open("social.html", "w", encoding="utf-8") as f:
    f.write("\n".join(new_lines))

print(f"Done! File now has {len(new_lines)} lines")
print("Run: git add . && git commit -m fix && git push")
