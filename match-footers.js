const fs = require('fs');
const path = require('path');

// Read the homepage footer
const indexContent = fs.readFileSync(path.join(__dirname, 'index.html'), 'utf8');

// Extract footer from homepage (from <!-- Footer --> to </footer>)
const footerMatch = indexContent.match(/(<!-- Footer -->[\s\S]*?<\/footer>)/);

if (!footerMatch) {
    console.log('❌ Could not find footer in index.html');
    process.exit(1);
}

const homepageFooter = footerMatch[1];
console.log('✅ Extracted homepage footer\n');

const files = [
    'home-theatre.html',
    'wifi-networking.html',
    'multi-room-audio.html',
    'video-distribution.html',
    'security-cctv.html',
    'electrical-installation.html',
    'smart-shading.html',
    'smart-home-design.html'
];

files.forEach(file => {
    const filePath = path.join(__dirname, file);

    if (!fs.existsSync(filePath)) {
        console.log(`⚠️  Skipping ${file} - file not found`);
        return;
    }

    let content = fs.readFileSync(filePath, 'utf8');

    // Find and replace the footer in service pages
    const serviceFooterMatch = content.match(/(<!-- Footer -->[\s\S]*?<\/footer>)/);

    if (serviceFooterMatch) {
        content = content.replace(serviceFooterMatch[1], homepageFooter);
        fs.writeFileSync(filePath, content, 'utf8');
        console.log(`✅ ${file}: Replaced footer with homepage footer`);
    } else {
        console.log(`⚠️  ${file}: Could not find footer section`);
    }
});

console.log('\n🎉 Finished matching footers!');
