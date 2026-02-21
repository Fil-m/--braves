import re

html = open('discover.html', 'r', encoding='utf-8').read()

# 1. Base Body Font Size
# from 8.5pt -> 9.0pt
html = html.replace('font-size: 8.5pt\n            }', 'font-size: 9.0pt\n            }')

# 2. Section Headers (ADHD, ASD, etc.)
# from 7.8pt -> 9pt, increased padding
html = re.sub(r'\.section-hdr\s*\{\s*font-size:\s*7\.8pt;\s*padding:\s*3px\s*8px;\s*margin-top:\s*5px;', r'.section-hdr {\n                font-size: 9.0pt;\n                padding: 5px 8px;\n                margin-top: 8px;', html)

# 3. Question Table (The core bulk of the text)
# from 7.8pt -> 8.5pt, line-height 1.25 -> 1.35
html = re.sub(r'\.q-table\s*\{\s*font-size:\s*7\.8pt;\s*line-height:\s*1\.25;', r'.q-table {\n                font-size: 8.5pt;\n                line-height: 1.35;', html)

# 4. Question Table Padding (Vertical Spacing) 
# from 4px -> 6px (This stretches the rows significantly)
html = html.replace('.q-table td {\n                padding: 4px 0 !important;\n            }', '.q-table td {\n                padding: 6px 0 !important;\n            }')

with open('discover.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Drastically scaled up print CSS variables.")
