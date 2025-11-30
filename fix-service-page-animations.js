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
    'smart-home-design.html'
];

files.forEach(file => {
    const filePath = path.join(__dirname, file);

    if (!fs.existsSync(filePath)) {
        console.log(`⚠️  Skipping ${file} - file not found`);
        return;
    }

    let content = fs.readFileSync(filePath, 'utf8');
    let changes = 0;

    // Count occurrences before
    const leftCount = (content.match(/data-aos="fade-left"/g) || []).length;
    const rightCount = (content.match(/data-aos="fade-right"/g) || []).length;

    // Replace fade-left with fade-up
    content = content.replace(/data-aos="fade-left"/g, 'data-aos="fade-up"');

    // Replace fade-right with fade-up
    content = content.replace(/data-aos="fade-right"/g, 'data-aos="fade-up"');

    changes = leftCount + rightCount;

    if (changes > 0) {
        fs.writeFileSync(filePath, content, 'utf8');
        console.log(`✅ ${file}: Changed ${leftCount} fade-left and ${rightCount} fade-right to fade-up (total: ${changes})`);
    } else {
        console.log(`✓  ${file}: No slide animations found`);
    }
});

console.log('\n🎉 Finished changing animations to fade only!');
