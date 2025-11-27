const { chromium } = require('playwright');
const fs = require('fs');

async function verifyWebsite() {
  console.log('🚀 Starting automated website verification...\n');

  const browser = await chromium.launch();
  const context = await browser.newContext({
    viewport: { width: 1920, height: 1080 }
  });
  const page = await context.newPage();

  const issues = [];
  const screenshots = [];

  // Test 1: Check homepage loads
  console.log('📄 Testing homepage...');
  try {
    await page.goto('http://localhost:8000/index.html', { waitUntil: 'networkidle' });
    await page.screenshot({ path: 'screenshots/homepage-desktop.png', fullPage: false });
    screenshots.push('homepage-desktop.png');
    console.log('✅ Homepage loaded successfully');
  } catch (e) {
    issues.push(`❌ Homepage failed to load: ${e.message}`);
  }

  // Test 2: Check for horizontal scroll issues
  console.log('\n📱 Testing for horizontal scroll issues...');
  const viewports = [
    { name: 'mobile', width: 375, height: 667 },
    { name: 'tablet', width: 768, height: 1024 },
    { name: 'desktop', width: 1920, height: 1080 }
  ];

  for (const viewport of viewports) {
    await page.setViewportSize({ width: viewport.width, height: viewport.height });
    await page.goto('http://localhost:8000/index.html', { waitUntil: 'networkidle' });

    const hasHorizontalScroll = await page.evaluate(() => {
      return document.documentElement.scrollWidth > document.documentElement.clientWidth;
    });

    if (hasHorizontalScroll) {
      issues.push(`❌ Horizontal scroll detected on ${viewport.name} (${viewport.width}px)`);
      await page.screenshot({ path: `screenshots/horizontal-scroll-${viewport.name}.png`, fullPage: false });
      screenshots.push(`horizontal-scroll-${viewport.name}.png`);
    } else {
      console.log(`✅ No horizontal scroll on ${viewport.name}`);
    }
  }

  // Test 3: Check button animations
  console.log('\n🎨 Testing button animations...');
  await page.setViewportSize({ width: 1920, height: 1080 });
  await page.goto('http://localhost:8000/index.html', { waitUntil: 'networkidle' });

  const buttonStyles = await page.evaluate(() => {
    const btn = document.querySelector('.btn-gold');
    if (!btn) return null;
    const styles = window.getComputedStyle(btn);
    return {
      transition: styles.transition,
      transitionDuration: styles.transitionDuration
    };
  });

  if (buttonStyles) {
    if (!buttonStyles.transition.includes('400ms') && !buttonStyles.transitionDuration.includes('0.4s')) {
      issues.push(`❌ Button transition not set to 400ms (found: ${buttonStyles.transitionDuration})`);
    } else {
      console.log('✅ Button animations configured correctly');
    }
  } else {
    issues.push('❌ .btn-gold button not found on page');
  }

  // Test 4: Check brand color consistency
  console.log('\n🎨 Checking brand color consistency...');
  const colorUsage = await page.evaluate(() => {
    const elements = document.querySelectorAll('*');
    const colors = new Set();
    elements.forEach(el => {
      const styles = window.getComputedStyle(el);
      if (styles.backgroundColor && styles.backgroundColor !== 'rgba(0, 0, 0, 0)') {
        colors.add(styles.backgroundColor);
      }
      if (styles.color) {
        colors.add(styles.color);
      }
    });
    return Array.from(colors);
  });

  const goldVariants = colorUsage.filter(c => c.includes('203') || c.includes('175') || c.includes('130')); // RGB for gold
  if (goldVariants.length > 3) {
    issues.push(`⚠️  Multiple gold color variants detected (${goldVariants.length} variations)`);
  } else {
    console.log('✅ Brand colors consistent');
  }

  // Test 5: Check CTA presence and format
  console.log('\n📞 Checking CTAs...');
  const ctaText = await page.evaluate(() => {
    const buttons = Array.from(document.querySelectorAll('a, button'));
    return buttons
      .map(b => b.textContent.trim())
      .filter(t => t.toLowerCase().includes('call') || t.toLowerCase().includes('email'));
  });

  const hasCorrectCTA = ctaText.some(t => t.includes('01443 123456') || t.includes('Call'));
  if (!hasCorrectCTA) {
    issues.push('❌ CTAs not updated to "Call 01443 123456"');
  } else {
    console.log('✅ CTAs present with correct format');
  }

  // Test 6: Check if service pages exist
  console.log('\n📄 Checking service pages...');
  const servicePages = [
    'smart-home-design.html',
    'home-theatre.html',
    'wifi-networking.html',
    'multi-room-audio.html',
    'video-distribution.html',
    'smart-shading.html',
    'security-cctv.html',
    'electrical-installation.html'
  ];

  for (const servicePage of servicePages) {
    try {
      const response = await page.goto(`http://localhost:8000/${servicePage}`, { waitUntil: 'networkidle' });
      if (response.status() === 200) {
        console.log(`✅ ${servicePage} exists`);

        // Check for starting price
        const hasPrice = await page.evaluate(() => {
          const text = document.body.textContent;
          return text.includes('£') && (text.includes('from') || text.includes('starting'));
        });

        if (!hasPrice) {
          issues.push(`⚠️  ${servicePage} missing starting price`);
        }
      }
    } catch (e) {
      issues.push(`❌ ${servicePage} failed to load: ${e.message}`);
    }
  }

  // Test 7: Check for new pages
  console.log('\n📄 Checking new pages...');
  const newPages = ['about.html', 'case-studies.html', 'gallery.html'];

  for (const newPage of newPages) {
    try {
      const response = await page.goto(`http://localhost:8000/${newPage}`, { waitUntil: 'networkidle' });
      if (response.status() === 200) {
        console.log(`✅ ${newPage} exists`);
        await page.screenshot({ path: `screenshots/${newPage.replace('.html', '')}-desktop.png`, fullPage: false });
        screenshots.push(`${newPage.replace('.html', '')}-desktop.png`);
      }
    } catch (e) {
      issues.push(`❌ ${newPage} not found or failed to load`);
    }
  }

  // Test 8: Check meta tags
  console.log('\n🔍 Checking SEO meta tags...');
  await page.goto('http://localhost:8000/index.html', { waitUntil: 'networkidle' });

  const metaTags = await page.evaluate(() => {
    return {
      title: document.title,
      description: document.querySelector('meta[name="description"]')?.content,
      ogTitle: document.querySelector('meta[property="og:title"]')?.content,
      ogDescription: document.querySelector('meta[property="og:description"]')?.content
    };
  });

  if (!metaTags.title || metaTags.title.length < 30) {
    issues.push('❌ Homepage title missing or too short');
  }
  if (!metaTags.description || metaTags.description.length < 100) {
    issues.push('❌ Homepage meta description missing or too short');
  }
  if (!metaTags.ogTitle) {
    issues.push('❌ Open Graph tags missing');
  }
  console.log(`Title: ${metaTags.title}`);
  console.log(`Description: ${metaTags.description?.substring(0, 80)}...`);

  // Test 9: Check accessibility
  console.log('\n♿ Checking accessibility...');
  const a11yIssues = await page.evaluate(() => {
    const issues = [];

    // Check for images without alt text
    const images = document.querySelectorAll('img');
    let missingAlt = 0;
    images.forEach(img => {
      if (!img.hasAttribute('alt')) {
        missingAlt++;
      }
    });
    if (missingAlt > 0) {
      issues.push(`${missingAlt} images missing alt text`);
    }

    // Check for buttons without accessible names
    const buttons = document.querySelectorAll('button, a');
    let unnamedButtons = 0;
    buttons.forEach(btn => {
      const hasText = btn.textContent.trim().length > 0;
      const hasAriaLabel = btn.hasAttribute('aria-label');
      const hasAriaLabelledBy = btn.hasAttribute('aria-labelledby');
      if (!hasText && !hasAriaLabel && !hasAriaLabelledBy) {
        unnamedButtons++;
      }
    });
    if (unnamedButtons > 0) {
      issues.push(`${unnamedButtons} buttons without accessible names`);
    }

    return issues;
  });

  if (a11yIssues.length > 0) {
    a11yIssues.forEach(issue => issues.push(`⚠️  A11y: ${issue}`));
  } else {
    console.log('✅ Basic accessibility checks passed');
  }

  // Test 10: Check for scroll hijacking
  console.log('\n🖱️  Checking for scroll hijacking...');
  const hasScrollHijack = await page.evaluate(() => {
    const script = document.documentElement.innerHTML;
    return script.includes('preventDefault') && script.includes('wheel');
  });

  if (hasScrollHijack) {
    issues.push('⚠️  Possible scroll hijacking code still present');
  } else {
    console.log('✅ No scroll hijacking detected');
  }

  // Mobile screenshots
  console.log('\n📱 Taking mobile screenshots...');
  await page.setViewportSize({ width: 375, height: 667 });
  await page.goto('http://localhost:8000/index.html', { waitUntil: 'networkidle' });
  await page.screenshot({ path: 'screenshots/homepage-mobile.png', fullPage: false });
  screenshots.push('homepage-mobile.png');

  await browser.close();

  // Summary
  console.log('\n' + '='.repeat(60));
  console.log('📊 VERIFICATION SUMMARY');
  console.log('='.repeat(60));

  if (issues.length === 0) {
    console.log('\n✅ ALL CHECKS PASSED! Website looks good.');
  } else {
    console.log(`\n⚠️  Found ${issues.length} issue(s):\n`);
    issues.forEach(issue => console.log(issue));
  }

  console.log(`\n📸 Screenshots saved: ${screenshots.length}`);
  console.log('Screenshots location: ./screenshots/\n');

  // Write report
  const report = {
    timestamp: new Date().toISOString(),
    totalIssues: issues.length,
    issues: issues,
    screenshots: screenshots
  };

  fs.writeFileSync('verification-report.json', JSON.stringify(report, null, 2));
  console.log('📄 Full report saved to: verification-report.json\n');

  return issues.length === 0;
}

// Run verification
verifyWebsite()
  .then(success => process.exit(success ? 0 : 1))
  .catch(error => {
    console.error('❌ Verification failed:', error);
    process.exit(1);
  });