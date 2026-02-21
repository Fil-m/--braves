import re

with open('discover.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update questions:
# <td class="q-text">UAText<em>DEENText</em></td> 
# -> <td class="q-text"><strong>DEENText</strong><br><em>UAText</em></td>
def replace_q_text(match):
    ua_text = match.group(1).strip()
    deen_text = match.group(2).strip()
    return f'<td class="q-text"><strong>{deen_text}</strong><br><em>{ua_text}</em></td>'

html = re.sub(r'<td class="q-text">(?:<strong>)?([^<]+)(?:</strong>)?<br><em>([^<]+)</em></td>', replace_q_text, html) # in case run twice
html = re.sub(r'<td class="q-text">([^<]+)<em>([^<]+)</em></td>', replace_q_text, html)

# 2. Update general headers / slogans
html = html.replace('UA | DE | EN', 'DE | EN | UA')
html = html.replace('Широкий скринінг нейровідмінності · Breites Screening · Broad Screening', 'Breites Screening · Broad Screening · Широкий скринінг нейровідмінності')
html = html.replace('Скринінг (продовження) · Screening (Fortsetzung) · Screening (continued)', 'Screening (Fortsetzung) · Screening (continued) · Скринінг (продовження)')
html = html.replace('Твій профіль · Dein Profil · Your Profile', 'Dein Profil · Your Profile · Твій профіль')
html = html.replace('Ми об\'єднуємось, бо система не готова до нас. Разом — ми сильніші. / Wir vereinen uns. Gemeinsam sind wir stärker.', 'Wir vereinen uns. Gemeinsam sind wir stärker. / Ми об\'єднуємось, бо система не готова до нас. Разом — ми сильніші.')

with open('discover.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Reorder complete")
