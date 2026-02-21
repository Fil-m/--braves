const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

(async () => {
    console.log("Launching browser...");
    const browser = await chromium.launch();
    const page = await browser.newPage();

    const fileUrl = 'file:///' + path.join(__dirname, 'discover.html').replace(/\\/g, '/');
    console.log("Loading page: " + fileUrl);

    await page.goto(fileUrl, { waitUntil: 'networkidle' });

    // Fill all answers so the results panel expands like a user would see it
    await page.evaluate(() => {
        const radios = document.querySelectorAll('input[type="radio"][value="3"]');
        radios.forEach(r => r.click());
    });

    console.log("Generating PDF...");
    const pdfBuffer = await page.pdf({
        format: 'A4',
        printBackground: true,
        margin: { top: '0', bottom: '0', left: '0', right: '0' } // handled by @page
    });

    fs.writeFileSync('test_print.pdf', pdfBuffer);
    console.log("Saved test_print.pdf");

    await browser.close();
})();
