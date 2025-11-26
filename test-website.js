const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

// Create screenshots directory
const screenshotsDir = path.join(__dirname, 'test-screenshots');
if (!fs.existsSync(screenshotsDir)) {
    fs.mkdirSync(screenshotsDir);
}

const testResults = {
    timestamp: new Date().toISOString(),
    pages: [],
    criticalIssues: [],
    warnings: [],
    passed: []
};

const pagesToTest = [
    { name: 'Home', url: 'http://localhost:8000/index.html' },
    { name: 'Smart Home Design', url: 'http://localhost:8000/smart-home-design.html' },
    { name: 'Home Theatre', url: 'http://localhost:8000/home-theatre.html' },
    { name: 'WiFi Networking', url: 'http://localhost:8000/wifi-networking.html' },
    { name: 'Multi-Room Audio', url: 'http://localhost:8000/multi-room-audio.html' },
    { name: 'Video Distribution', url: 'http://localhost:8000/video-distribution.html' },
    { name: 'Smart Shading', url: 'http://localhost:8000/smart-shading.html' },
    { name: 'Security CCTV', url: 'http://localhost:8000/security-cctv.html' },
    { name: 'Electrical Installation', url: 'http://localhost:8000/electrical-installation.html' },
    { name: 'Privacy Policy', url: 'http://localhost:8000/privacy.html' },
    { name: 'Terms & Conditions', url: 'http://localhost:8000/terms.html' },
    { name: 'Cookies Policy', url: 'http://localhost:8000/cookies.html' }
];

async function testPage(browser, pageInfo) {
    const page = await browser.newPage();
    const pageResult = {
        name: pageInfo.name,
        url: pageInfo.url,
        issues: [],
        consoleErrors: [],
        networkErrors: [],
        screenshots: {}
    };

    console.log(`\n🔍 Testing: ${pageInfo.name}`);

    // Capture console errors
    page.on('console', msg => {
        if (msg.type() === 'error') {
            pageResult.consoleErrors.push(msg.text());
        }
    });

    // Capture network failures
    page.on('response', response => {
        if (!response.ok() && response.url().includes('localhost:8000')) {
            pageResult.networkErrors.push({
                url: response.url(),
                status: response.status(),
                statusText: response.statusText()
            });
        }
    });

    try {
        // Navigate to page
        await page.goto(pageInfo.url, { waitUntil: 'networkidle', timeout: 30000 });

        // Take full page screenshot
        const screenshotPath = path.join(screenshotsDir, `${pageInfo.name.toLowerCase().replace(/\s+/g, '-')}.png`);
        await page.screenshot({ path: screenshotPath, fullPage: true });
        pageResult.screenshots.desktop = screenshotPath;
        console.log(`  ✅ Screenshot saved: ${screenshotPath}`);

        // Take mobile screenshot
        await page.setViewportSize({ width: 375, height: 667 });
        const mobileScreenshotPath = path.join(screenshotsDir, `${pageInfo.name.toLowerCase().replace(/\s+/g, '-')}-mobile.png`);
        await page.screenshot({ path: mobileScreenshotPath, fullPage: true });
        pageResult.screenshots.mobile = mobileScreenshotPath;
        console.log(`  ✅ Mobile screenshot saved`);

        // Reset viewport
        await page.setViewportSize({ width: 1920, height: 1080 });

        // Check for critical issues

        // 1. Check if CSS is loaded
        const styles = await page.evaluate(() => {
            return Array.from(document.styleSheets).length;
        });
        if (styles === 0) {
            pageResult.issues.push({ severity: 'CRITICAL', message: 'No CSS loaded - styles missing!' });
            testResults.criticalIssues.push(`${pageInfo.name}: No CSS loaded`);
        } else {
            console.log(`  ✅ CSS loaded (${styles} stylesheets)`);
        }

        // 2. Check for broken images
        const brokenImages = await page.evaluate(() => {
            const images = Array.from(document.images);
            return images.filter(img => !img.complete || img.naturalHeight === 0).map(img => img.src);
        });
        if (brokenImages.length > 0) {
            pageResult.issues.push({ severity: 'HIGH', message: `${brokenImages.length} broken images`, images: brokenImages });
            testResults.warnings.push(`${pageInfo.name}: ${brokenImages.length} broken images`);
            console.log(`  ⚠️  ${brokenImages.length} broken images found`);
        } else {
            console.log(`  ✅ All images loaded`);
        }

        // 3. Check for JavaScript errors in console
        if (pageResult.consoleErrors.length > 0) {
            pageResult.issues.push({ severity: 'HIGH', message: `${pageResult.consoleErrors.length} console errors`, errors: pageResult.consoleErrors });
            testResults.warnings.push(`${pageInfo.name}: ${pageResult.consoleErrors.length} console errors`);
            console.log(`  ⚠️  ${pageResult.consoleErrors.length} console errors`);
        } else {
            console.log(`  ✅ No console errors`);
        }

        // 4. Check for 404/network errors
        if (pageResult.networkErrors.length > 0) {
            pageResult.issues.push({ severity: 'CRITICAL', message: `${pageResult.networkErrors.length} network errors (404s, etc.)`, errors: pageResult.networkErrors });
            testResults.criticalIssues.push(`${pageInfo.name}: Network errors detected`);
            console.log(`  ❌ ${pageResult.networkErrors.length} network errors (404s)`);
        } else {
            console.log(`  ✅ No network errors`);
        }

        // 5. Check for missing content
        const bodyText = await page.textContent('body');
        if (bodyText.length < 100) {
            pageResult.issues.push({ severity: 'CRITICAL', message: 'Very little content on page - possible blank page' });
            testResults.criticalIssues.push(`${pageInfo.name}: Minimal content detected`);
            console.log(`  ❌ Very little content detected`);
        } else {
            console.log(`  ✅ Content present (${bodyText.length} chars)`);
        }

        // 6. Check all links on page
        const brokenLinks = await page.evaluate(() => {
            const links = Array.from(document.querySelectorAll('a[href]'));
            return links.map(a => ({
                text: a.textContent.trim(),
                href: a.href
            })).filter(link =>
                link.href.startsWith('http://localhost:8000') &&
                !link.href.includes('#')
            );
        });

        console.log(`  📋 Found ${brokenLinks.length} internal links to test`);

        // 7. Test responsive design breakpoints
        const viewports = [
            { name: 'Mobile', width: 375, height: 667 },
            { name: 'Tablet', width: 768, height: 1024 },
            { name: 'Desktop', width: 1920, height: 1080 }
        ];

        for (const viewport of viewports) {
            await page.setViewportSize(viewport);
            await page.waitForTimeout(500); // Let layout settle

            // Check for horizontal scrollbar (indicates overflow issue)
            const hasHorizontalScroll = await page.evaluate(() => {
                return document.documentElement.scrollWidth > document.documentElement.clientWidth;
            });

            if (hasHorizontalScroll) {
                pageResult.issues.push({
                    severity: 'MEDIUM',
                    message: `Horizontal scroll detected at ${viewport.name} (${viewport.width}px) - layout overflow`
                });
                testResults.warnings.push(`${pageInfo.name}: Horizontal overflow at ${viewport.name}`);
                console.log(`  ⚠️  Horizontal scroll at ${viewport.name}`);
            }
        }

        // 8. Check for accessibility issues
        const missingAltText = await page.evaluate(() => {
            const images = Array.from(document.images);
            return images.filter(img => !img.alt || img.alt.trim() === '').length;
        });

        if (missingAltText > 0) {
            pageResult.issues.push({ severity: 'MEDIUM', message: `${missingAltText} images missing alt text` });
            testResults.warnings.push(`${pageInfo.name}: ${missingAltText} images without alt text`);
            console.log(`  ⚠️  ${missingAltText} images missing alt text`);
        }

        // If no critical issues, mark as passed
        if (pageResult.issues.filter(i => i.severity === 'CRITICAL').length === 0) {
            testResults.passed.push(pageInfo.name);
        }

    } catch (error) {
        pageResult.issues.push({ severity: 'CRITICAL', message: `Test failed: ${error.message}` });
        testResults.criticalIssues.push(`${pageInfo.name}: Test execution failed - ${error.message}`);
        console.log(`  ❌ Test failed: ${error.message}`);
    } finally {
        await page.close();
    }

    testResults.pages.push(pageResult);
    return pageResult;
}

async function runTests() {
    console.log('🚀 Starting comprehensive website testing...\n');
    console.log('📸 Screenshots will be saved to: test-screenshots/\n');

    const browser = await chromium.launch({ headless: true });

    for (const pageInfo of pagesToTest) {
        await testPage(browser, pageInfo);
    }

    await browser.close();

    // Generate report
    console.log('\n' + '='.repeat(80));
    console.log('📊 TEST RESULTS SUMMARY');
    console.log('='.repeat(80));
    console.log(`\n✅ Passed: ${testResults.passed.length}/${pagesToTest.length} pages`);
    console.log(`❌ Critical Issues: ${testResults.criticalIssues.length}`);
    console.log(`⚠️  Warnings: ${testResults.warnings.length}`);

    if (testResults.criticalIssues.length > 0) {
        console.log('\n🚨 CRITICAL ISSUES:');
        testResults.criticalIssues.forEach(issue => console.log(`  - ${issue}`));
    }

    if (testResults.warnings.length > 0) {
        console.log('\n⚠️  WARNINGS:');
        testResults.warnings.forEach(warning => console.log(`  - ${warning}`));
    }

    // Save detailed report
    const reportPath = path.join(__dirname, 'test-report.json');
    fs.writeFileSync(reportPath, JSON.stringify(testResults, null, 2));
    console.log(`\n📄 Full report saved: ${reportPath}`);

    console.log('\n' + '='.repeat(80));

    // Exit with code 1 if critical issues found
    if (testResults.criticalIssues.length > 0) {
        console.log('\n❌ Tests failed - critical issues found');
        process.exit(1);
    } else {
        console.log('\n✅ All tests passed!');
        process.exit(0);
    }
}

runTests().catch(err => {
    console.error('Fatal error running tests:', err);
    process.exit(1);
});
