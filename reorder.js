const fs = require('fs');

let html = fs.readFileSync('discover.html', 'utf8');

// The q-text cells currently look like this:
// <td class="q-text">Невміння доводити справи до кінця: багато проектів, курсів, ідей, але фінал рідко.<em>Projekte, Kurse, Ideen - Begeisterung da, Abschluss selten / projects, courses, ideas - enthusiasm yes, completion rarely</em></td>

// We want them to look like this:
// <td class="q-text"><strong>Projekte, Kurse, Ideen - Begeisterung da, Abschluss selten / projects, courses, ideas - enthusiasm yes, completion rarely</strong><br><em>Невміння доводити справи до кінця: багато проектів, курсів, ідей, але фінал рідко.</em></td>

// Actually, in the current discover.html, they look like this:
// <td class="q-text">Український текст...<em>Deutscher Text / English text</em></td>

// Let's use Regex to find these patterns and replace them
const regex = /<td class="q-text">([^<]+)<em>([^<]+)<\/em><\/td>/g;

html = html.replace(regex, (match, uaText, deEnText) => {
    // Trim strings to avoid weird spacing
    uaText = uaText.trim();
    deEnText = deEnText.trim();

    // Construct new format: DE/EN first (bold), then UA (italic)
    return `<td class="q-text"><strong>${deEnText}</strong><br><em>${uaText}</em></td>`;
});

// We also need to do this for the category headers (section-hdr).
// e.g. <div class="section-hdr" style="...">⚡ ADHD / СДУГ / Aufmerksamkeits-Defizit (1–5)</div>
// Since these were just updated to be trilingual by me, let me check their current state.
// They are manually typed in HTML. I will manually update them.

// We also need to do this for header tags (UA | DE | EN -> DE | EN | UA)
html = html.replace(/UA \| DE \| EN/g, 'DE | EN | UA');

// Update labels
html = html.replace(/Широкий скринінг нейровідмінності · Breites Screening · Broad Screening/g, 'Breites Screening · Broad Screening · Широкий скринінг нейровідмінності');
html = html.replace(/Скринінг \(продовження\) · Screening \(Fortsetzung\) · Screening \(continued\)/g, 'Screening (Fortsetzung) · Screening (continued) · Скринінг (продовження)');
html = html.replace(/Твій профіль · Dein Profil · Your Profile/g, 'Dein Profil · Your Profile · Твій профіль');
html = html.replace(/Ми об'єднуємось, бо система не готова до нас. Разом — ми сильніші. \/ Wir vereinen uns. Gemeinsam sind wir stärker./g, 'Wir vereinen uns. Gemeinsam sind wir stärker. / Ми об\'єднуємось, бо система не готова до нас. Разом — ми сильніші.');

fs.writeFileSync('discover.html', html);
console.log('Reorder complete.');
