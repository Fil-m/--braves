import re

with open('discover.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace HTML radio values
text = text.replace('value="0"', 'value="1"')
text = text.replace('value="0.5"', 'value="2"')
text = text.replace('value="1"', 'value="3"')

# Replace instructional text in German
text = text.replace('Nein = 0', 'Nein = 1')
text = text.replace('Manchmal = 0.5', 'Manchmal = 2')
text = text.replace('Ja = 1', 'Ja = 3')

# Replace instructional text in English
text = text.replace('No = 0', 'No = 1')
text = text.replace('Sometimes = 0.5', 'Sometimes = 2')
text = text.replace('Yes = 1', 'Yes = 3')

# Replace instructional text in Ukrainian
text = text.replace('Ні = 0', 'Ні = 1')
text = text.replace('Іноді = 0.5', 'Іноді = 2')
text = text.replace('Так = 1', 'Так = 3')

# Replace JS Labels mappings used by the DOM
text = text.replace("'0': 'Nein", "'1': 'Nein")
text = text.replace("'0.5': 'Manchmal", "'2': 'Manchmal")
text = text.replace("'1': 'Ja", "'3': 'Ja")

# Replace Calculation Math in JS and HTML
text = text.replace('const max = p.qs.length;', 'const max = p.qs.length * 3;')
text = text.replace('_____ / ${p.qs.length}</td>', '_____ / ${p.qs.length * 3}</td>')

with open('discover.html', 'w', encoding='utf-8') as f:
    f.write(text)
    
print('Updated discover.html successfully')