const fs = require('fs');
const path = require('path');

const servicePages = [
    'home-theatre.html',
    'wifi-networking.html',
    'multi-room-audio.html',
    'video-distribution.html',
    'security-cctv.html',
    'electrical-installation.html',
    'smart-shading.html',
    'smart-home-design.html'
];

servicePages.forEach(page => {
    const filePath = path.join(__dirname, page);
    let content = fs.readFileSync(filePath, 'utf8');
    
    console.log(`Processing ${page}...`);
    
    // 1. Add header transparency script (add before </body>)
    if (!content.includes('// Header transparency on scroll')) {
        const headerScript = `
    <script>
    // Header transparency on scroll
    window.addEventListener('scroll', function() {
        const header = document.getElementById('main-header');
        if (window.scrollY > 50) {
            header.classList.remove('header-transparent');
            header.classList.add('bg-black');
        } else {
            header.classList.add('header-transparent');
            header.classList.remove('bg-black');
        }
    });
    </script>`;
        content = content.replace('</body>', headerScript + '\n</body>');
    }
    
    // 2. Add mobile menu animation and black background
    content = content.replace(
        /id="mobile-menu"\s+class="hidden/g,
        'id="mobile-menu" style="background: black; transition: all 0.3s ease;" class="hidden'
    );
    
    // 3. Center text on mobile for headings and paragraphs
    content = content.replace(
        /<h2 class="text-4xl md:text-5xl font-semibold/g,
        '<h2 class="text-4xl md:text-5xl font-semibold text-center md:text-left'
    );
    content = content.replace(
        /<h3 class="text-2xl font-semibold/g,
        '<h3 class="text-2xl font-semibold text-center md:text-left'
    );
    content = content.replace(
        /<p class="text-xl text-gray-600/g,
        '<p class="text-xl text-gray-600 text-center md:text-left'
    );
    content = content.replace(
        /<p class="text-gray-600/g,
        '<p class="text-gray-600 text-center md:text-left'
    );
    
    // 4. Change "Number • Speak to Tim" to "Call Tim"
    content = content.replace(/Number\s*•\s*Speak to Tim/g, 'Call Tim');
    content = content.replace(/Number.*Speak to Tim/g, 'Call Tim');
    
    // Save the file
    fs.writeFileSync(filePath, content, 'utf8');
    console.log(`✅ Fixed ${page}`);
});

console.log('\n✅ All service pages updated!');
