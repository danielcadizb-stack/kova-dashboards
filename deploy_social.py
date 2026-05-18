# This script applies the logo and creates the final social.html
# Run from the kova-dashboards folder

import base64, os, sys

SOCIAL_PATH = 'social.html'
LOGO_PATH = 'logo_b64.txt'

# Read the clean social.html from the same directory as this script
script_dir = os.path.dirname(os.path.abspath(__file__))
clean_src = os.path.join(script_dir, 'social_clean_v8.html')

if not os.path.exists(clean_src):
    print('ERROR: social_clean_v8.html not found. Run this from kova-dashboards folder after copying the file.')
    sys.exit(1)

with open(clean_src, 'r', encoding='utf-8') as f:
    content = f.read()

# Apply logo if available
if os.path.exists(LOGO_PATH):
    with open(LOGO_PATH, 'r') as f:
        logo = f.read().strip()
    # Replace LOGO_SRC placeholder
    content = content.replace("var LOGO_SRC = '';", "var LOGO_SRC = '" + logo + "';")
    # Also fix header logo
    content = content.replace('<div class="logo-k-text">K</div>', '<img src="' + logo + '" style="width:100%;height:100%;object-fit:cover;border-radius:10px;" alt="KOVA">')
    print('Logo applied: True')
else:
    print('Logo: not found (logo_b64.txt missing) - using K placeholder')

with open(SOCIAL_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print('Done! social.html written:', len(content), 'bytes')
print('switchTab:', 'function switchTab' in content)
print('renderOv:', 'function renderOv' in content)
print('addMetric:', 'function addMetric' in content)
print('m-views form:', 'm-views' in content)
print('mensual:', 'mensual' in content)
print('28 days:', 'd:28' in content)
