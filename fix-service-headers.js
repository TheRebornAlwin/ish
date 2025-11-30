const fs = require('fs');

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
    let content = fs.readFileSync(file, 'utf8');
    
    // Fix header background color to pure black
    content = content.replace(
        /background: rgba\(20, 20, 20, 0\.95\)/g,
        'background: rgb(0, 0, 0)'
    );
    
    fs.writeFileSync(file, content, 'utf8');
    console.log(`✅ ${file}: Updated header background to pure black`);
});

console.log('\n🎉 All service pages updated!');
