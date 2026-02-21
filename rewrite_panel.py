import re

def process_file():
    with open('discover.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. New HTML for Results Panel (Static Traffic Light Table)
    new_results_html = """        <div id="resultsPanel">
            <div id="resultsContent">
                <div class="results-header">📊 Dein Profil / Your Profile / Твій профіль</div>
                <div id="printTime" class="print-only print-time"></div>
                
                <div class="bars" id="barsGrid" style="display:none"></div>
                
                <div id="manualCalcGrid" class="manual-calc-grid">
                    <div class="manual-title">
                        ✍️ Auswertung (Nur für Papierausdruck) / Scoring (Paper version only) / Підрахунок (для паперового тесту):
                    </div>
                    <div class="manual-desc">
                        Zähle die Punkte für jede Gruppe: <strong>Nein = 1, Manchmal = 2, Ja = 3.</strong><br>
                        <em>Count points for each group: No = 1, Sometimes = 2, Yes = 3.</em><br>
                        Порахуйте бали для кожної групи: <strong>Ні = 1, Іноді = 2, Так = 3.</strong>
                    </div>
                    
                    <table class="manual-table">
                        <thead>
                            <tr>
                                <td>Kategorie / Category</td>
                                <td style="text-align: center;">Punkte / Points</td>
                                <td style="text-align: center;">Schlüssel / Key / Шкала</td>
                            </tr>
                        </thead>
                        <tbody>
                            <tr><td style="border-left: 3px solid var(--c-adhd);">Aufmerksamkeits-Defizit / ADHD / СДУГ (1–5)</td><td class="tc">____ / 15</td><td class="tc key-col">🔴&gt;11 &nbsp; 🟡9‒11 &nbsp; 🟢&lt;9</td></tr>
                            <tr><td style="border-left: 3px solid var(--c-asd);">Autismus / ASD / Аутизм (6–10)</td><td class="tc">____ / 15</td><td class="tc key-col">🔴&gt;11 &nbsp; 🟡9‒11 &nbsp; 🟢&lt;9</td></tr>
                            <tr><td style="border-left: 3px solid var(--c-dys);">Dyslexie / Dyslexia / Дислексія (11–15)</td><td class="tc">____ / 15</td><td class="tc key-col">🔴&gt;11 &nbsp; 🟡9‒11 &nbsp; 🟢&lt;9</td></tr>
                            <tr><td style="border-left: 3px solid var(--c-disc);">Dyskalkulie / Dyscalculia / Дискалькулія (16–20)</td><td class="tc">____ / 15</td><td class="tc key-col">🔴&gt;11 &nbsp; 🟡9‒11 &nbsp; 🟢&lt;9</td></tr>
                            <tr><td style="border-left: 3px solid var(--c-dcd);">Dyspraxie / Dyspraxia / Диспраксія (21–24)</td><td class="tc">____ / 12</td><td class="tc key-col">🔴&gt;9 &nbsp; 🟡7‒9 &nbsp; 🟢&lt;7</td></tr>
                            <tr><td style="border-left: 3px solid var(--c-ptsd);">Trauma / C-PTSD / Травmа (25–28)</td><td class="tc">____ / 12</td><td class="tc key-col">🔴&gt;9 &nbsp; 🟡7‒9 &nbsp; 🟢&lt;7</td></tr>
                            <tr><td style="border-left: 3px solid var(--c-anx);">Angststörung / Anxiety / Тривожність (29–32)</td><td class="tc">____ / 12</td><td class="tc key-col">🔴&gt;9 &nbsp; 🟡7‒9 &nbsp; 🟢&lt;7</td></tr>
                            <tr><td style="border-left: 3px solid var(--c-ocd);">Zwangsstörung / OCD / ОКР (33–36)</td><td class="tc">____ / 12</td><td class="tc key-col">🔴&gt;9 &nbsp; 🟡7‒9 &nbsp; 🟢&lt;7</td></tr>
                            <tr><td style="border-left: 3px solid var(--c-sen);">Sensorik / Sensory / Сенсорна (37–40)</td><td class="tc">____ / 12</td><td class="tc key-col">🔴&gt;9 &nbsp; 🟡7‒9 &nbsp; 🟢&lt;7</td></tr>
                        </tbody>
                    </table>
                    
                    <div class="manual-legend">
                        🔴 Starke Hinweise (zum Arzt) / Strong signs (see doctor) / Сильні ознаки (варто йти до лікаря)<br>
                        🟡 Hinweise vorhanden / Signs present / Є ознаки (продовжуйте спостерігати)<br>
                        🟢 Geringe Wahrscheinlichkeit / Low likelihood / Низька ймовірність
                    </div>
                </div>
            </div>
        </div>"""

    # Replace the old resultsPanel div block using regex between <div id="resultsPanel"... and the bottom warning
    content = re.sub(
        r'<div id="resultsPanel"[\s\S]*?<div class="warn">', 
        new_results_html + '\n\n        <div class="warn">', 
        content
    )

    # 2. Add new clean CSS for these results panels
    new_css = """
        /* Results Styles - Cleaned */
        #resultsPanel {
            background: var(--lgrey);
            border: 2px dashed #999;
            border-radius: 6px;
            padding: 15px;
            margin: 8px 0;
            min-height: 60px;
        }
        .results-header {
            font-size: 10pt; font-weight: 800; color: #fff; background: var(--gradient); 
            padding: 8px; border-radius: 4px; margin-bottom: 10px; text-align: center;
        }
        .print-time { font-size: 6.5pt; color: #888; text-align: center; margin-bottom: 5px; }
        .manual-calc-grid { margin-top: 5px; margin-bottom: 12px; }
        .manual-calc-grid .manual-title { font-size: 8pt; font-weight: 700; margin-bottom: 4px; color: var(--navy); }
        .manual-calc-grid .manual-desc { font-size: 7.5pt; color: var(--dgrey); margin-bottom: 8px; line-height: 1.4; }
        .manual-table { width: 100%; font-size: 7.5pt; border-collapse: collapse; margin-bottom: 8px; }
        .manual-table thead tr { border-bottom: 1px solid #ccc; font-weight: bold; background: #eee; }
        .manual-table td { padding: 4px; border-bottom: 1px solid #eee; }
        .manual-table .tc { text-align: center; }
        .manual-table .key-col { font-size: 6pt; font-weight: 600; white-space: nowrap; }
        .manual-legend { font-size: 7.5pt; font-weight: 700; color: var(--navy); margin-top: 10px; text-align: center; padding: 8px; background: #e8ezf0; border-radius: 4px; }
        @media print {
            #resultsPanel { padding: 10px; border-color: var(--navy); background: #fdfdfd; }
        }"""
    
    # Inject CSS after #resultsPanel rule in the <style> block
    content = re.sub(r'#resultsPanel \{\s*.*?\s*\}', new_css, content, flags=re.DOTALL)

    # 3. Clean up the JS (Remove the DOMContentLoaded table injection and percent level logic)
    # Remove: window.addEventListener('DOMContentLoaded', () => { ... });
    content = re.sub(
        r'window\.addEventListener\(\'DOMContentLoaded\', \(\) => \{\s*const table = document\.querySelector\(\'\#manualCalcGrid table\'\);[\s\S]*?\}\);',
        '// Removed dynamic table generation.',
        content
    )

    # Replace levelClass with levelClassAndLabel
    content = re.sub(
        r'function levelClass\(pct\) \{[\s\S]*?return \'low\';\s*\}',
        """function levelClassAndLabel(score, qsLength) {
            if (qsLength >= 5) {
                if (score >= 12) return { cls: 'high', label: '🔴 Hoch / Сильно' };
                if (score >= 9) return { cls: 'mid', label: '🟡 Mittel / Середньо' };
                return { cls: 'low', label: '🟢 Niedrig / Низько' };
            } else {
                if (score >= 10) return { cls: 'high', label: '🔴 Hoch / Сильно' };
                if (score >= 7) return { cls: 'mid', label: '🟡 Mittel / Середньо' };
                return { cls: 'low', label: '🟢 Niedrig / Низько' };
            }
        }""",
        content
    )

    # Update updateResults JS loop that generates bars
    old_loop = """            grid.innerHTML = '';
            PROFILES.forEach(p => {
                const score = getScore(p.qs);
                const max = p.qs.length * 3;
                const pct = score / max;
                const cls = levelClass(pct);
                const pctLabel = Math.round(pct * 100) + '%';
                grid.innerHTML += `
                    <div class="bar-row">
                        <div class="bar-label"><span>${p.label}</span><span>${pctLabel}</span></div>
                        <div class="bar-track"><div class="bar-fill ${cls}" style="width:${pctLabel};background:${p.color}"></div></div>
                    </div>`;
            });"""
    
    new_loop = """            grid.innerHTML = '';
            PROFILES.forEach(p => {
                const score = getScore(p.qs);
                const res = levelClassAndLabel(score, p.qs.length);
                const widthPct = Math.round((score / (p.qs.length * 3)) * 100) + '%';
                
                grid.innerHTML += `
                    <div class="bar-row">
                        <div class="bar-label"><span>${p.label}</span><span style="font-weight:600; font-size:6.5pt">${res.label}</span></div>
                        <div class="bar-track"><div class="bar-fill ${res.cls}" style="width:${widthPct};background:${p.color}"></div></div>
                    </div>`;
            });"""
    content = content.replace(old_loop, new_loop)

    with open('discover.html', 'w', encoding='utf-8') as f:
        f.write(content)

process_file()
