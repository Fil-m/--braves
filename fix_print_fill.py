import re

html = open('discover.html', 'r', encoding='utf-8').read()

# 1. Remove "DE | EN | UA" throughout the document
html = html.replace('<div class="langs">DE | EN | UA</div>', '')
html = html.replace('<div class="langs-sm">Telegram · DE | EN | UA · Online · Kostenlos / Безкоштовно</div>', '<div class="langs-sm">Telegram · Online · Kostenlos / Безкоштовно</div>')

# 2. Adjust margins and spacing to fill the space without edge clipping
# Up from margin: 5mm -> margin: 10mm (safe printable area)
html = html.replace('margin: 5mm;', 'margin: 10mm;')

# Increase base font size for print from 7.2pt to 8.5pt so questions take more vertical space genuinely
html = re.sub(r'body\s*\{\s*background:\s*none;\s*padding:\s*0;\s*font-size:\s*7\.2pt\s*\}', r'body {\n                background: none;\n                padding: 0;\n                font-size: 8.5pt\n            }', html)

# Increase q-table row sizing for print
html = re.sub(r'\.q-table\s*\{\s*font-size:\s*6\.8pt;\s*line-height:\s*1\.15;', r'.q-table {\n                font-size: 7.8pt;\n                line-height: 1.25;', html)

# Increase the padding of the q-table td to give questions more breathing room
html = re.sub(r'\.q-table td\s*\{\s*padding:\s*2px\s*0\n\s*\}', r'.q-table td {\n                padding: 4px 0 !important;\n            }', html)


with open('discover.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Removed DE|EN|UA markers, expanded print margins, and upscaled font to fill empty page space.")
