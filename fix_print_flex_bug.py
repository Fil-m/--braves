import re

html = open('discover.html', 'r', encoding='utf-8').read()

# Fix the CSS for print mode to remove display:flex from body, 
# which prevents page-break-before from working in Chromium browsers.
html = html.replace('body {\n                background: none;\n                padding: 0;\n                font-size: 8.5pt\n            }', 'body {\n                display: block !important;\n                background: none;\n                padding: 0;\n                font-size: 8.5pt\n            }')

# Add explicit page breaks to page1c (page 3) and page2 (page 4)
# Just to be absolutely safe
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
                display: block !important;
            }

            #page1, #page1b, #page1c, #page2 {
                position: relative;
                float: none !important;
            }

            #page1b, #page1c, #page2 {
                page-break-before: always !important;
                break-before: page !important;
            }
"""
# Replace the previous .page CSS injected from the last step
html = re.sub(r'\.page\s*\{\s*box-shadow:\s*none;\s*width:\s*100%;\s*min-height:\s*auto\s*!important;\s*height:\s*auto\s*!important;\s*padding:\s*0;\s*page-break-after:\s*auto;\s*break-inside:\s*auto;\s*margin:\s*0;\s*\}\s*#page2\s*\{\s*page-break-before:\s*always\s*!important;\s*break-before:\s*page\s*!important;\s*\}', css_injection, html)

with open('discover.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Applied display: block to body and explicit page breaks to elements.")
