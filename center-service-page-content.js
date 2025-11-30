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

    // 1. Center icon circles in feature cards on mobile
    // Add mx-auto md:mx-0 to icon circle divs
    const iconCirclePattern = /<div class="w-16 h-16 bg-gradient-to-br from-\[#cbaf82\] to-\[#ede9df\] rounded-full flex items-center justify-center mb-6">/g;
    const iconCircleReplacement = '<div class="w-16 h-16 bg-gradient-to-br from-[#cbaf82] to-[#ede9df] rounded-full flex items-center justify-center mb-6 mx-auto md:mx-0">';

    if (content.includes('w-16 h-16 bg-gradient-to-br from-[#cbaf82]')) {
        content = content.replace(iconCirclePattern, iconCircleReplacement);
        changes++;
    }

    // 2. Center checkmark sections on mobile
    // Change flex containers to be centered on mobile
    const checkmarkContainerPattern = /<div class="flex gap-4">/g;
    const checkmarkContainerReplacement = '<div class="flex gap-4 justify-center md:justify-start">';

    content = content.replace(checkmarkContainerPattern, checkmarkContainerReplacement);

    // 3. Center h4 headings on mobile
    const h4Pattern = /<h4 class="text-xl font-semibold mb-2">/g;
    const h4Replacement = '<h4 class="text-xl font-semibold mb-2 text-center md:text-left">';

    content = content.replace(h4Pattern, h4Replacement);

    // 4. Center the "space-y-6" container on mobile
    const spaceYPattern = /<div class="space-y-6">/g;
    const spaceYReplacement = '<div class="space-y-6 flex flex-col items-center md:items-start">';

    content = content.replace(spaceYPattern, spaceYReplacement);

    if (changes > 0 || content !== fs.readFileSync(filePath, 'utf8')) {
        fs.writeFileSync(filePath, content, 'utf8');
        console.log(`✅ ${file}: Centered all content for mobile`);
    } else {
        console.log(`✓  ${file}: No changes needed`);
    }
});

console.log('\n🎉 Finished centering service page content!');
