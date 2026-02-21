import re

with open('discover.html', 'r', encoding='utf-8') as f:
    base_html = f.read()

def create_ua(html):
    # Titles & general UI
    html = html.replace('Breites Screening · Broad Screening · Широкий скринінг нейровідмінності', 'Широкий скринінг нейровідмінності')
    html = html.replace('Discover · Infinity Braves — Широкий скринінг нейровідмінності', 'Infinity Braves — Широкий скринінг нейровідмінності (UA)')
    html = html.replace('✨ ALLES KOSTENLOS / ALL FREE / ВСЕ БЕЗКОШТОВНО', '✨ ВСЕ БЕЗКОШТОВНО')
    html = html.replace('🚀 Beitreten / Join us / ПРИЄДНУЙСЯ', '🚀 ПРИЄДНУЙСЯ')
    html = html.replace('Telegram · Online · Kostenlos / Безкоштовно', 'Telegram · Онлайн · Безкоштовно')
    html = html.replace("Wir vereinen uns. Gemeinsam sind wir stärker. / We unite because the system is not ready for us.\n                Together we are stronger. / Ми об'єднуємось, бо система не готова до нас. Разом — ми сильніші.", "Ми об'єднуємось, бо система не готова до нас. Разом — ми сильніші.")
    html = html.replace('🖨️ Друкувати / Print', '🖨️ Друкувати')
    
    # Section headers
    html = html.replace('⚡ ADHD / СДУГ / Aufmerksamkeitsdefizit (1–5)', '⚡ СДУГ (1–5)')
    html = html.replace('🧩 ASD / Аутизм / Autism (6–10)', '🧩 Аутизм (6–10)')
    html = html.replace('📖 Dyslexie / Dyslexia / Дислексія (11–15)', '📖 Дислексія (11–15)')
    html = html.replace('🔢 Dyskalkulie / Dyscalculia / Дискалькулія (16–20)', '🔢 Дискалькулія (16–20)')
    html = html.replace('🎾 Dyspraxie / Dyspraxia / Диспраксія (21–24)', '🎾 Диспраксія (21–24)')
    html = html.replace('🌪️ Trauma / C-PTSD / Травма (25–28)', '🌪️ C-PTSD / Травма (25–28)')
    html = html.replace('😰 Angststörung / Anxiety / Тривожність (29–32)', '😰 Тривожність (29–32)')
    html = html.replace('🔁 Zwangsstörung / OCD / ОКР (33–36)', '🔁 ОКР (33–36)')
    html = html.replace('🎧 Sensorik / Sensory / Сенсорна (37–40)', '🎧 Сенсорна інтеграція (37–40)')

    # Results section
    html = html.replace('📊 Твій профіль / Dein Profil / Your Profile', '📊 Твій профіль')
    html = html.replace('Пояснення показників / Erklärung / Explanation', 'Пояснення показників')
    html = html.replace('Імовірність / Wahrscheinlichkeit / Probability', 'Ймовірність')
    html = html.replace('Що це означає / Was das bedeutet / What it means', 'Що це означає')
    html = html.replace('Висока / Hoch / High', 'Висока')
    html = html.replace('🔴 (>=70%)', '🔴 (>=70%)')
    html = html.replace('Рекомендована професійна діагностика / Fachdiagnostik empfohlen / Professional diagnosis recommended', 'Рекомендована професійна діагностика')
    html = html.replace('Середня / Mittel / Mid', 'Середня')
    html = html.replace('🟡 (40-69%)', '🟡 (40-69%)')
    html = html.replace('Є виражені ознаки, варто дослідити глибше / Deutliche Anzeichen / Clear signs present', 'Є виражені ознаки, варто дослідити глибше')
    html = html.replace('Низька / Niedrig / Low', 'Низька')
    html = html.replace('🟢 (<40%)', '🟢 (<40%)')
    html = html.replace('Ознаки відсутні або слабко виражені / Keine oder schwache Anzeichen / Few or no signs', 'Ознаки відсутні або слабко виражені')

    # Legal rights section
    html = html.replace('⚖️ Ваші права у Німеччині / Ihre Rechte / Your rights (Nachteilsausgleich)', '⚖️ Ваші права у Німеччині (Nachteilsausgleich)')
    html = html.replace('🎓 Поза школою / Außerhalb der Schule / Beyond school', '🎓 Поза школою / Університет / Робота') # Simplified
    html = html.replace('Більше часу на іспитах (університет / IHK) / Mehr Zeit bei Prüfungen / Extra time for exams', 'Більше часу на іспитах (університет / IHK)')
    html = html.replace('Адаптація робочого місця (наприклад, навушники) / Arbeitsplatzanpassung / Workplace adaptation', 'Адаптація робочого місця (наприклад, навушники)')
    html = html.replace('Можливість працювати з дому (Home-Office) / Home-Office-Möglichkeit / Option for home-office', 'Можливість працювати з дому (Home-Office)')
    html = html.replace('Захист від звільнення (для працівників з інвалідністю) / Kündigungsschutz / Protection against dismissal', 'Захист від звільнення (для працівників із Schwerbehindertenausweis)')
    html = html.replace('🏥 Здоров\'я та фінанси / Gesundheit & Finanzen / Health & Finance', '🏥 Здоров\'я та фінанси')
    html = html.replace('100% оплата психотерапії касою / Therapie von der Kasse bezahlt / Therapy paid by health insurance', '100% оплата психотерапії касою (Krankenkasse)')
    html = html.replace('Ерготерапія для дорослих (СДУГ/Аутизм) / Ergotherapie für Erwachsene / Ergotherapy for adults', 'Ерготерапія для дорослих (допомога з організацією)')
    html = html.replace('Ліки за рецептом (~5€ доплата) / Medikamente auf Rezept (~5€) / Prescription meds (~5€)', 'Ліки за рецептом (~5€ доплата)')
    html = html.replace('Соціальна підтримка та супровід / Soziale Begleitung / Social support services', 'Соціальна підтримка та супровід')
    html = html.replace('🌍 Для мігрантів / Für Migranten / For migrants', '🌍 Для мігрантів')
    html = html.replace('Права діють з будь-яким дозволом на проживання / Alle Aufenthaltstitel / Any residence permit', 'Права діють з будь-яким дозволом на проживання')
    html = html.replace('Статус біженця — не перешкода / Flüchtlingsstatus kein Hindernis / Refugee status is no barrier', 'Статус біженця (§24) — не перешкода')
    html = html.replace('Держустанови зобов\'язані дати перекладача / Dolmetscher ist Pflicht / Translator is mandatory', 'Держустанови зобов\'язані надати перекладача')
    html = html.replace('Infinity Braves допомагає з документами UA/DE/EN / Wir helfen mit Dokumenten / We help with paperwork', 'Infinity Braves допомагає з документами і розумінням системи')
    html = html.replace('🗺 Шлях до діагнозу / Weg zur Diagnose / Path to diagnosis', '🗺 Шлях до діагнозу')
    html = html.replace('1. 🇺🇦 Сімейний лікар (Hausarzt) → направлення до психіатра / To family doctor → referral to psychiatrist / Zum Hausarzt → Überweisung zum Psychiater', '1. 🇺🇦 Сімейний лікар (Hausarzt) → направлення (Überweisung) до психіатра')
    html = html.replace('2. 🇩🇪 Psychologische Praxis або Psychiater (черга 6–18 міс., але є швидші шляхи / Wartezeit 6–18 Mo., aber schnellere Wege möglich / Queue 6–18 months but faster options exist)', '2. 🇩🇪 Psychologische Praxis або Psychiater (стандартна черга 6–18 міс., але є швидкі шляхи)')
    html = html.replace('3. ✅ Infinity Braves допомагає знайти фахівців які <em>реально діагностують нейровідмінність</em> у дорослих / Wir helfen Spezialisten zu finden, die <em>Neurodivergenz bei Erwachsenen wirklich diagnostizieren</em> / We help find specialists who <em>actually diagnose neurodivergence</em> in adults', '3. ✅ Infinity Braves допомагає знайти фахівців, які <em>реально діагностують нейровідмінність</em> у дорослих')

    # Radio Options
    html = html.replace('Nein / No / Ні', 'Ні')
    html = html.replace('Manchmal / Sometimes / Іноді', 'Іноді')
    html = html.replace('Ja / Yes / Так', 'Так')

    # Parse questions
    # Format is <td class="q-text"><strong>DE / EN</strong><br><em>UA</em>
    # We replace it with <td class="q-text"><strong>UA</strong>
    
    html = re.sub(r'<td class="q-text"><strong>(.*?)</strong><br><em>(.*?)</em>', 
                  r'<td class="q-text"><strong>\2</strong>', html, flags=re.DOTALL)

    # Parse notes
    # Format: <span class="q-note">DE / EN / UA</span>
    # The splitting logic: split by ' / ' and take the last element, BUT there might be multiple '/'
    # Let's match typical format: <span class="q-note">DE / EN / UA</span>
    # It's always 3 parts separated by ' / ' ... wait, some are 2 parts if DE and EN are identical.
    # Actually, we can just split by ' / ' and grab the last part.
    def replace_note_ua(match):
        parts = match.group(1).split(' / ')
        return f'<span class="q-note">{parts[-1]}</span>'
        
    html = re.sub(r'<span class="q-note">(.*?)</span>', replace_note_ua, html, flags=re.DOTALL)

    # JS Updates (labels)
    html = re.sub(r"label:\s*'Aufmerksamkeits-Defizit / ADHD / СДУГ'", "label: 'СДУГ (ADHD)'", html)
    html = re.sub(r"label:\s*'Autismus / ASD / Аутизм'", "label: 'Аутизм (ASD)'", html)
    html = re.sub(r"label:\s*'Dyslexie / Dyslexia / Дислексія'", "label: 'Дислексія'", html)
    html = re.sub(r"label:\s*'Dyskalkulie / Dyscalculia / Дискалькулія'", "label: 'Дискалькулія'", html)
    html = re.sub(r"label:\s*'Dyspraxie / Dyspraxia / Диспраксія'", "label: 'Диспраксія'", html)
    html = re.sub(r"label:\s*'Trauma / C-PTSD / Травma'", "label: 'C-PTSD (Травма)'", html)
    html = re.sub(r"label:\s*'Angststörung / Anxiety / Тривожність'", "label: 'Тривожність'", html)
    html = re.sub(r"label:\s*'Zwangsstörung / OCD / ОКР'", "label: 'ОКР'", html)
    html = re.sub(r"label:\s*'Sensorik / Sensory / Сенсорна'", "label: 'Сенсорна інтеграція'", html)

    html = html.replace("🔴 Hoch / Сильно", "🔴 Сильно")
    html = html.replace("🟡 Mittel / Середньо", "🟡 Середньо")
    html = html.replace("🟢 Niedrig / Низько", "🟢 Низько")

    # Increase print sizes & adjust margins
    # Since we have much more space, let's bump up readability
    html = html.replace('.q-table {\n            width: 100%;\n            border-collapse: collapse;\n            font-size: 9pt;\n            margin-bottom: 6px\n        }', 
                        '.q-table {\n            width: 100%;\n            border-collapse: collapse;\n            font-size: 11pt;\n            margin-bottom: 8px\n        }')
    html = html.replace('.q-text {\n            line-height: 1.4\n        }', '.q-text {\n            line-height: 1.6; font-size: 11.5pt;\n        }')
    html = html.replace('.q-note {\n            font-size: 6pt;', '.q-note {\n            font-size: 8pt;')
    html = html.replace('.section-hdr {\n            display: flex;\n            align-items: center;\n            background: var(--gradient);\n            color: #ffffff;\n            padding: 8px 14px;\n            font-size: 10.5pt;',
                        '.section-hdr {\n            display: flex;\n            align-items: center;\n            background: var(--gradient);\n            color: #ffffff;\n            padding: 10px 14px;\n            font-size: 13pt;')
    html = html.replace('.q-table td {\n            padding: 4px 6px;', '.q-table td {\n            padding: 8px 8px;')
    html = html.replace('font-size: 6.5pt;\n            line-height: 1.2;', 'font-size: 9pt;\n            line-height: 1.4;') # target radio-label
    html = html.replace('.radio-box {\n            width: 10px;\n            height: 10px;', '.radio-box {\n            width: 12px;\n            height: 12px;')

    return html

def create_de_en(html):
    # Titles & general UI
    html = html.replace('Breites Screening · Broad Screening · Широкий скринінг нейровідмінності', 'Breites Screening · Broad Screening')
    html = html.replace('Discover · Infinity Braves — Широкий скринінг нейровідмінності', 'Infinity Braves — Broad Screening (DE/EN)')
    html = html.replace('✨ ALLES KOSTENLOS / ALL FREE / ВСЕ БЕЗКОШТОВНО', '✨ ALLES KOSTENLOS / ALL FREE')
    html = html.replace('🚀 Beitreten / Join us / ПРИЄДНУЙСЯ', '🚀 Beitreten / Join us')
    html = html.replace('Telegram · Online · Kostenlos / Безкоштовно', 'Telegram · Online · Free/Kostenlos')
    html = html.replace("Wir vereinen uns. Gemeinsam sind wir stärker. / We unite because the system is not ready for us.\n                Together we are stronger. / Ми об'єднуємось, бо система не готова до нас. Разом — ми сильніші.", "Wir vereinen uns. Gemeinsam sind wir stärker. / We unite because the system is not ready for us. Together we are stronger.")
    html = html.replace('🖨️ Друкувати / Print', '🖨️ Drucken / Print')
    
    # Section headers
    html = html.replace('⚡ ADHD / СДУГ / Aufmerksamkeitsdefizit (1–5)', '⚡ ADHD / Aufmerksamkeitsdefizit (1–5)')
    html = html.replace('🧩 ASD / Аутизм / Autism (6–10)', '🧩 ASD / Autismus (6–10)')
    html = html.replace('📖 Dyslexie / Dyslexia / Дислексія (11–15)', '📖 Dyslexia / Dyslexie (11–15)')
    html = html.replace('🔢 Dyskalkulie / Dyscalculia / Дискалькулія (16–20)', '🔢 Dyscalculia / Dyskalkulie (16–20)')
    html = html.replace('🎾 Dyspraxie / Dyspraxia / Диспраксія (21–24)', '🎾 Dyspraxia / Dyspraxie (21–24)')
    html = html.replace('🌪️ Trauma / C-PTSD / Травма (25–28)', '🌪️ Trauma / C-PTSD (25–28)')
    html = html.replace('😰 Angststörung / Anxiety / Тривожність (29–32)', '😰 Anxiety / Angststörung (29–32)')
    html = html.replace('🔁 Zwangsstörung / OCD / ОКР (33–36)', '🔁 OCD / Zwangsstörung (33–36)')
    html = html.replace('🎧 Sensorik / Sensory / Сенсорна (37–40)', '🎧 Sensory / Sensorik (37–40)')

    # Results section
    html = html.replace('📊 Твій профіль / Dein Profil / Your Profile', '📊 Dein Profil / Your Profile')
    html = html.replace('Пояснення показників / Erklärung / Explanation', 'Erklärung / Explanation')
    html = html.replace('Імовірність / Wahrscheinlichkeit / Probability', 'Wahrscheinlichkeit / Probability')
    html = html.replace('Що це означає / Was das bedeutet / What it means', 'Was das bedeutet / What it means')
    html = html.replace('Висока / Hoch / High', 'Hoch / High')
    html = html.replace('Рекомендована професійна діагностика / Fachdiagnostik empfohlen / Professional diagnosis recommended', 'Fachdiagnostik empfohlen / Professional diagnosis recommended')
    html = html.replace('Середня / Mittel / Mid', 'Mittel / Mid')
    html = html.replace('Є виражені ознаки, варто дослідити глибше / Deutliche Anzeichen / Clear signs present', 'Deutliche Anzeichen / Clear signs present')
    html = html.replace('Низька / Niedrig / Low', 'Niedrig / Low')
    html = html.replace('Ознаки відсутні або слабко виражені / Keine oder schwache Anzeichen / Few or no signs', 'Keine oder schwache Anzeichen / Few or no signs')

    # Legal rights section
    html = html.replace('⚖️ Ваші права у Німеччині / Ihre Rechte / Your rights (Nachteilsausgleich)', '⚖️ Ihre Rechte in Deutschland / Your rights in Germany (Nachteilsausgleich)')
    html = html.replace('🎓 Поза школою / Außerhalb der Schule / Beyond school', '🎓 Außerhalb der Schule / Beyond school')
    html = html.replace('Більше часу на іспитах (університет / IHK) / Mehr Zeit bei Prüfungen / Extra time for exams', 'Mehr Zeit bei Prüfungen / Extra time for exams')
    html = html.replace('Адаптація робочого місця (наприклад, навушники) / Arbeitsplatzanpassung / Workplace adaptation', 'Arbeitsplatzanpassung / Workplace adaptation')
    html = html.replace('Можливість працювати з дому (Home-Office) / Home-Office-Möglichkeit / Option for home-office', 'Home-Office-Möglichkeit / Option for home-office')
    html = html.replace('Захист від звільнення (для працівників з інвалідністю) / Kündigungsschutz / Protection against dismissal', 'Kündigungsschutz / Protection against dismissal')
    html = html.replace('🏥 Здоров\'я та фінанси / Gesundheit & Finanzen / Health & Finance', '🏥 Gesundheit & Finanzen / Health & Finance')
    html = html.replace('100% оплата психотерапії касою / Therapie von der Kasse bezahlt / Therapy paid by health insurance', 'Therapie von der Kasse bezahlt / Therapy paid by health insurance')
    html = html.replace('Ерготерапія для дорослих (СДУГ/Аутизм) / Ergotherapie für Erwachsene / Ergotherapy for adults', 'Ergotherapie für Erwachsene / Ergotherapy for adults')
    html = html.replace('Ліки за рецептом (~5€ доплата) / Medikamente auf Rezept (~5€) / Prescription meds (~5€)', 'Medikamente auf Rezept (~5€) / Prescription meds (~5€)')
    html = html.replace('Соціальна підтримка та супровід / Soziale Begleitung / Social support services', 'Soziale Begleitung / Social support services')
    html = html.replace('🌍 Для мігрантів / Für Migranten / For migrants', '🌍 Für Migranten / For migrants')
    html = html.replace('Права діють з будь-яким дозволом на проживання / Alle Aufenthaltstitel / Any residence permit', 'Gültig mit jedem Aufenthaltstitel / Valid with any residence permit')
    html = html.replace('Статус біженця — не перешкода / Flüchtlingsstatus kein Hindernis / Refugee status is no barrier', 'Flüchtlingsstatus kein Hindernis / Refugee status is no barrier')
    html = html.replace('Держустанови зобов\'язані дати перекладача / Dolmetscher ist Pflicht / Translator is mandatory', 'Dolmetscher ist Pflicht bei Behörden / Translator is mandatory at authorities')
    html = html.replace('Infinity Braves допомагає з документами UA/DE/EN / Wir helfen mit Dokumenten / We help with paperwork', 'Wir helfen mit Dokumenten / We help with paperwork')
    html = html.replace('🗺 Шлях до діагнозу / Weg zur Diagnose / Path to diagnosis', '🗺 Weg zur Diagnose / Path to diagnosis')
    html = html.replace('1. 🇺🇦 Сімейний лікар (Hausarzt) → направлення до психіатра / To family doctor → referral to psychiatrist / Zum Hausarzt → Überweisung zum Psychiater', '1. Zum Hausarzt → Überweisung zum Psychiater / Family doctor → referral to psychiatrist')
    html = html.replace('2. 🇩🇪 Psychologische Praxis або Psychiater (черга 6–18 міс., але є швидші шляхи / Wartezeit 6–18 Mo., aber schnellere Wege möglich / Queue 6–18 months but faster options exist)', '2. Psychologische Praxis oder Psychiater (Wartezeit 6–18 Mo., aber schnellere Wege möglich / Queue 6–18 months but faster options exist)')
    html = html.replace('3. ✅ Infinity Braves допомагає знайти фахівців які <em>реально діагностують нейровідмінність</em> у дорослих / Wir helfen Spezialisten zu finden, die <em>Neurodivergenz bei Erwachsenen wirklich diagnostizieren</em> / We help find specialists who <em>actually diagnose neurodivergence</em> in adults', '3. ✅ Wir helfen Spezialisten zu finden, die <em>Neurodivergenz bei Erwachsenen wirklich diagnostizieren</em> / We help find specialists who <em>actually diagnose neurodivergence in adults</em>')

    # Radio Options
    html = html.replace('Nein / No / Ні', 'Nein / No')
    html = html.replace('Manchmal / Sometimes / Іноді', 'Manchmal / Sometimes')
    html = html.replace('Ja / Yes / Так', 'Ja / Yes')

    # Parse questions
    # Format is <td class="q-text"><strong>DE / EN</strong><br><em>UA</em>
    # We replace it with <td class="q-text"><strong>DE / EN</strong>
    html = re.sub(r'<td class="q-text"><strong>(.*?)</strong><br><em>(.*?)</em>', 
                  r'<td class="q-text"><strong>\1</strong>', html, flags=re.DOTALL)

    # Parse notes
    # Format: <span class="q-note">DE / EN / UA</span>
    def replace_note_de_en(match):
        parts = match.group(1).split(' / ')
        if len(parts) >= 2:
            return f'<span class="q-note">{" / ".join(parts[:-1])}</span>'
        return match.group(0)
        
    html = re.sub(r'<span class="q-note">(.*?)</span>', replace_note_de_en, html, flags=re.DOTALL)

    # JS Updates (labels)
    html = re.sub(r"label:\s*'Aufmerksamkeits-Defizit / ADHD / СДУГ'", "label: 'Aufmerksamkeits-Defizit / ADHD'", html)
    html = re.sub(r"label:\s*'Autismus / ASD / Аутизм'", "label: 'Autismus / ASD'", html)
    html = re.sub(r"label:\s*'Dyslexie / Dyslexia / Дислексія'", "label: 'Dyslexie / Dyslexia'", html)
    html = re.sub(r"label:\s*'Dyskalkulie / Dyscalculia / Дискалькулія'", "label: 'Dyskalkulie / Dyscalculia'", html)
    html = re.sub(r"label:\s*'Dyspraxie / Dyspraxia / Диспраксія'", "label: 'Dyspraxie / Dyspraxia'", html)
    html = re.sub(r"label:\s*'Trauma / C-PTSD / Травma'", "label: 'Trauma / C-PTSD'", html)
    html = re.sub(r"label:\s*'Angststörung / Anxiety / Тривожність'", "label: 'Angststörung / Anxiety'", html)
    html = re.sub(r"label:\s*'Zwangsstörung / OCD / ОКР'", "label: 'Zwangsstörung / OCD'", html)
    html = re.sub(r"label:\s*'Sensorik / Sensory / Сенсорна'", "label: 'Sensorik / Sensory'", html)

    html = html.replace("🔴 Hoch / Сильно", "🔴 Hoch / High")
    html = html.replace("🟡 Mittel / Середньо", "🟡 Mittel / Medium")
    html = html.replace("🟢 Niedrig / Низько", "🟢 Niedrig / Low")

    # Increase print sizes & adjust margins
    html = html.replace('.q-table {\n            width: 100%;\n            border-collapse: collapse;\n            font-size: 9pt;\n            margin-bottom: 6px\n        }', 
                        '.q-table {\n            width: 100%;\n            border-collapse: collapse;\n            font-size: 11pt;\n            margin-bottom: 8px\n        }')
    html = html.replace('.q-text {\n            line-height: 1.4\n        }', '.q-text {\n            line-height: 1.6; font-size: 10.5pt;\n        }')
    html = html.replace('.q-note {\n            font-size: 6pt;', '.q-note {\n            font-size: 8pt;')
    html = html.replace('.section-hdr {\n            display: flex;\n            align-items: center;\n            background: var(--gradient);\n            color: #ffffff;\n            padding: 8px 14px;\n            font-size: 10.5pt;',
                        '.section-hdr {\n            display: flex;\n            align-items: center;\n            background: var(--gradient);\n            color: #ffffff;\n            padding: 10px 14px;\n            font-size: 13pt;')
    html = html.replace('.q-table td {\n            padding: 4px 6px;', '.q-table td {\n            padding: 8px 8px;')
    html = html.replace('font-size: 6.5pt;\n            line-height: 1.2;', 'font-size: 8.5pt;\n            line-height: 1.4;') # target radio-label
    html = html.replace('.radio-box {\n            width: 10px;\n            height: 10px;', '.radio-box {\n            width: 12px;\n            height: 12px;')

    return html

with open('discover_ua.html', 'w', encoding='utf-8') as f:
    f.write(create_ua(base_html))

with open('discover_de_en.html', 'w', encoding='utf-8') as f:
    f.write(create_de_en(base_html))

print("Created discover_ua.html and discover_de_en.html successfully.")
