const fs = require('fs');
const path = require('path');

const files = [
    'home-theatre.html',
    'wifi-networking.html',
    'multi-room-audio.html',
    'video-distribution.html',
    'security-cctv.html',
    'electrical-installation.html',
    'smart-shading.html',
    'smart-home-design.html',
    'index.html'
];

files.forEach(file => {
    const filePath = path.join(__dirname, file);

    if (!fs.existsSync(filePath)) {
        console.log(`⚠️  Skipping ${file} - file not found`);
        return;
    }

    let content = fs.readFileSync(filePath, 'utf8');
    let changes = 0;

    // Change h-screen to min-h-screen on mobile (allow sections to grow naturally)
    // Keep h-screen on desktop with md:h-screen
    const beforeCount = (content.match(/class="[^"]*\bh-screen\b/g) || []).length;

    content = content.replace(
        /class="([^"]*)(\bh-screen\b)/g,
        (match, before, hscreen) => {
            // Only replace if it's not already min-h-screen md:h-screen
            if (!before.includes('min-h-screen') && !before.includes('md:h-screen')) {
                changes++;
                return `class="${before}min-h-screen md:h-screen`;
            }
            return match;
        }
    );

    const afterCount = (content.match(/class="[^"]*h-screen/g) || []).length;

    if (changes > 0) {
        fs.writeFileSync(filePath, content, 'utf8');
        console.log(`✅ ${file}: Changed ${changes} h-screen instance(s) to min-h-screen md:h-screen`);
    } else {
        console.log(`✓  ${file}: No changes needed`);
    }
});

console.log('\n🎉 Finished removing section scroll issues!');
