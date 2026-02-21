import re

html = open('discover.html', 'r', encoding='utf-8').read()

# 1. Change gradient transition from dark navy to transparent
html = html.replace('linear-gradient(90deg, var(--c-adhd), var(--navy))', 'linear-gradient(90deg, var(--c-adhd), transparent)')
html = html.replace('linear-gradient(90deg, var(--c-asd), var(--navy))', 'linear-gradient(90deg, var(--c-asd), transparent)')
html = html.replace('linear-gradient(90deg, var(--c-dys), var(--navy))', 'linear-gradient(90deg, var(--c-dys), transparent)')
html = html.replace('linear-gradient(90deg, var(--c-disc), var(--navy))', 'linear-gradient(90deg, var(--c-disc), transparent)')
html = html.replace('linear-gradient(90deg, var(--c-dcd), var(--navy))', 'linear-gradient(90deg, var(--c-dcd), transparent)')
html = html.replace('linear-gradient(90deg, var(--c-ptsd), var(--navy))', 'linear-gradient(90deg, var(--c-ptsd), transparent)')
html = html.replace('linear-gradient(90deg, var(--c-anx), var(--navy))', 'linear-gradient(90deg, var(--c-anx), transparent)')
html = html.replace('linear-gradient(90deg, var(--c-ocd), var(--navy))', 'linear-gradient(90deg, var(--c-ocd), transparent)')
html = html.replace('linear-gradient(90deg, var(--c-sen), var(--navy))', 'linear-gradient(90deg, var(--c-sen), transparent)')

# 2. Fix print height (remove min-height: 297mm constraint inside @media print)
css_injection = """
            .page {
                box-shadow: none;
                width: 100%;
                min-height: auto !important;
                height: auto !important;
                padding: 2mm 5mm;
                page-break-after: always;
                break-after: page;
                margin: 0;
            }
"""
html = re.sub(r'\.page\s*\{\s*box-shadow:\s*none;\s*width:\s*100%;\s*padding:\s*2mm\s+5mm;\s*page-break-after:\s*always;\s*break-after:\s*page;\s*margin:\s*0\s*\}', css_injection, html)

# 3. Footer text and gradient (Regex match due to multiline wrapping)
old_footer = r'<div\s+style="background:var\(--teal\);color:#fff;text-align:center;padding:5px;font-size:7pt;font-weight:600;margin-top:8px;border-radius:3px">\s*Ми об\'єднуємось, бо система не готова до нас. Разом — ми сильніші. / Wir vereinen uns. Gemeinsam sind wir\s*stärker.\s*</div>'

new_footer = """        <div style="font-size:8pt;font-weight:800;text-align:center;padding:8px;margin-top:10px;border-radius:4px;background:var(--gradient);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;">
            Wir vereinen uns. Gemeinsam sind wir stärker. / We unite because the system is not ready for us. Together we are stronger. / Ми об'єднуємось, бо система не готова до нас. Разом — ми сильніші.
        </div>"""

html = re.sub(old_footer, new_footer, html)

with open('discover.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated gradients, footer text, and print height.")
