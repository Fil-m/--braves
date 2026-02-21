import re

with open('discover.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Provide test-specific gradient for category headers
html = re.sub(r'style="background:var\(--c-([a-z]+)\)"', r'style="background:linear-gradient(90deg, var(--c-\1), var(--navy))"', html)

# 2. Fix the print issue by adjusting .a-col inside @media print
# First, let's remove any existing .a-col in @media print if we somehow added it, 
# then inject the correct print width.
# Also REMOVE the var(--gradient) !important from .section-hdr in print.
html = html.replace('background: var(--gradient) !important;', '')

if '.a-col {' not in html.split('@media print {')[1]:
    css_injection = """
            .a-col {
                width: 35% !important;
                min-width: 170px !important;
                padding-left: 5px !important;
            }
            .radio-group {
                gap: 2px !important;
            }
"""
    html = html.replace('@media print {', '@media print {' + css_injection)

# 3. Fix the "other headers" to be gradient text by replacing pseudo-h1s with real h1s
html = html.replace('<div style="font-size:14pt; font-weight:900; letter-spacing:1px">INFINITY BRAVES</div>', '<h1 style="font-size: 14pt; margin: 0;">INFINITY BRAVES</h1>')

with open('discover.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated CSS widths, print overrides, and gradients.")
