import re

html = open('discover.html', 'r', encoding='utf-8').read()

# 1. Increase padding in .q-table td for print to comfortably spread the 40 questions over 3 full pages
html = html.replace('.q-table td {\n                padding: 1px 0\n            }', '.q-table td {\n                padding: 2px 0\n            }')

# 2. Add page-break-before: always to #page2 inside @media print to force it onto the 4th page
css_injection = """
            .page {
                box-shadow: none;
                width: 100%;
                min-height: auto !important;
                height: auto !important;
                padding: 0;
                page-break-after: auto;
                break-inside: auto;
                margin: 0;
            }

            #page2 {
                page-break-before: always !important;
                break-before: page !important;
            }
"""
html = html.replace('.page {\n                box-shadow: none;\n                width: 100%;\n                min-height: auto !important;\n                height: auto !important;\n                padding: 0;\n                page-break-after: auto;\n                break-inside: auto;\n                margin: 0;\n            }', css_injection)

with open('discover.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated CSS for exact 4-page print layout.")
