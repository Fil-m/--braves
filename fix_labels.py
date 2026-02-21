import re

html = open('discover.html', 'r', encoding='utf-8').read()

# 1. Standardize radio button labels across ALL 40 questions
# We look for <span class="radio-box"></span><span>...</span>
# Replace whatever is in the second span with the standard trilingual text based on value.
html = re.sub(r'<label class="radio-label"><input\s*type="radio" name="([^"]+)" value="0"><span\s*class="radio-box"></span><span>[^<]+</span></label>', 
              r'<label class="radio-label"><input type="radio" name="\1" value="0"><span class="radio-box"></span><span>Nein / No / Ні</span></label>', html)

html = re.sub(r'<label class="radio-label"><input\s*type="radio" name="([^"]+)" value="0.5"><span\s*class="radio-box"></span><span>[^<]+</span></label>', 
              r'<label class="radio-label"><input type="radio" name="\1" value="0.5"><span class="radio-box"></span><span>Manchmal / Sometimes / Іноді</span></label>', html)

html = re.sub(r'<label class="radio-label"><input\s*type="radio" name="([^"]+)" value="1"><span\s*class="radio-box"></span><span>[^<]+</span></label>', 
              r'<label class="radio-label"><input type="radio" name="\1" value="1"><span class="radio-box"></span><span>Ja / Yes / Так</span></label>', html)

# 2. Fix Q4 specifically which was missed due to newlines
# Original: <td class="q-text">Можеш годинами не відриватись від цікавого — і забути їсти/спати?<em>Stundenlang\n                        vertieft, Essen/Schlafen vergessen? / Hyperfocus — lost in interesting things for hours?</em>\n                </td>
def fix_q(match):
    ua = match.group(1).strip()
    de = match.group(2).strip()
    # clean up any stray newlines or extra spaces
    de = re.sub(r'\s+', ' ', de)
    ua = re.sub(r'\s+', ' ', ua)
    return f'<td class="q-text"><strong>{de}</strong><br><em>{ua}</em></td>'

html = re.sub(r'<td class="q-text">([^<]+)<em>(.*?)</em>\s*</td>', fix_q, html, flags=re.DOTALL)

with open('discover.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Standardized radio labels and question formats.")
