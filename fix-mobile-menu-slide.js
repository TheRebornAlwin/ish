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

    // 1. Update mobile menu structure to be a slide-in overlay
    const oldMenuPattern = /<div id="mobile-menu" style="background: black; transition: all 0\.3s ease;" class="hidden md:hidden mt-4 pb-4 space-y-4">/g;
    const newMenuStructure = `<div id="mobile-menu" class="fixed top-0 right-0 h-full w-80 bg-black transform translate-x-full transition-transform duration-300 ease-in-out z-50 md:hidden overflow-y-auto">
            <div class="p-6 space-y-4">
                <div class="flex justify-between items-center mb-6">
                    <span class="text-white text-xl font-semibold">Menu</span>
                    <button id="mobile-menu-close" class="text-white hover:text-[#cbaf82]" aria-label="Close menu">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                        </svg>
                    </button>
                </div>`;

    if (content.includes('id="mobile-menu"')) {
        content = content.replace(oldMenuPattern, newMenuStructure);
        changes++;

        // 2. Close the mobile menu div properly
        // Find the closing div for mobile menu and add closing wrapper div
        // The mobile menu ends before the </nav> tag, so we need to close the wrapper div
        // Actually, we need to be more careful. Let me find where the mobile menu ends.

        // 3. Update the JavaScript to handle slide-in animation
        const oldScript = /document\.getElementById\('mobile-menu-btn'\)\.addEventListener\('click',\s*\(\)\s*=>\s*\{\s*document\.getElementById\('mobile-menu'\)\.classList\.toggle\('hidden'\);\s*\}\);/g;

        const newScript = `// Mobile menu slide-in from right
        const mobileMenuBtn = document.getElementById('mobile-menu-btn');
        const mobileMenu = document.getElementById('mobile-menu');
        const mobileMenuClose = document.getElementById('mobile-menu-close');

        if (mobileMenuBtn && mobileMenu) {
            mobileMenuBtn.addEventListener('click', () => {
                mobileMenu.classList.remove('translate-x-full');
                mobileMenu.classList.add('translate-x-0');
            });
        }

        if (mobileMenuClose && mobileMenu) {
            mobileMenuClose.addEventListener('click', () => {
                mobileMenu.classList.remove('translate-x-0');
                mobileMenu.classList.add('translate-x-full');
            });
        }

        // Close menu when clicking outside
        document.addEventListener('click', (e) => {
            if (mobileMenu && !mobileMenu.contains(e.target) && !mobileMenuBtn?.contains(e.target)) {
                mobileMenu.classList.remove('translate-x-0');
                mobileMenu.classList.add('translate-x-full');
            }
        });`;

        content = content.replace(oldScript, newScript);

        // 4. Wrap the mobile menu content and close divs properly
        // Add closing </div> before </nav>
        const mobileMenuEndPattern = /(Get Started<\/button>\s*<\/div>)(\s*<\/nav>)/g;
        content = content.replace(mobileMenuEndPattern, '$1\n            </div>\n        </div>$2');
    }

    if (changes > 0) {
        fs.writeFileSync(filePath, content, 'utf8');
        console.log(`✅ ${file}: Updated mobile menu to slide in from right`);
    } else {
        console.log(`✓  ${file}: No changes needed`);
    }
});

console.log('\n🎉 Finished updating mobile menu!');
