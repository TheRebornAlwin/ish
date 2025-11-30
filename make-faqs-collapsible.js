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

const collapsibleScript = `
    <script>
    // FAQ Collapsible functionality
    document.addEventListener('DOMContentLoaded', function() {
        const faqItems = document.querySelectorAll('.faq-item');

        faqItems.forEach(item => {
            const question = item.querySelector('.faq-question');
            const answer = item.querySelector('.faq-answer');
            const arrow = item.querySelector('.faq-arrow');

            if (question && answer && arrow) {
                question.addEventListener('click', function() {
                    const isOpen = !answer.classList.contains('hidden');

                    if (isOpen) {
                        // Close
                        answer.style.maxHeight = answer.scrollHeight + 'px';
                        setTimeout(() => {
                            answer.style.maxHeight = '0px';
                        }, 10);
                        setTimeout(() => {
                            answer.classList.add('hidden');
                        }, 300);
                        arrow.style.transform = 'rotate(0deg)';
                    } else {
                        // Open
                        answer.classList.remove('hidden');
                        answer.style.maxHeight = '0px';
                        setTimeout(() => {
                            answer.style.maxHeight = answer.scrollHeight + 'px';
                        }, 10);
                        setTimeout(() => {
                            answer.style.maxHeight = 'none';
                        }, 300);
                        arrow.style.transform = 'rotate(180deg)';
                    }
                });
            }
        });
    });
    </script>`;

files.forEach(file => {
    const filePath = path.join(__dirname, file);

    if (!fs.existsSync(filePath)) {
        console.log(`⚠️  Skipping ${file} - file not found`);
        return;
    }

    let content = fs.readFileSync(filePath, 'utf8');
    let changes = 0;

    // Transform FAQ items to collapsible format
    // Match FAQ items with the current structure
    const faqPattern = /<div class="bg-white p-6 rounded-xl shadow-sm" data-aos="fade-up"[^>]*>\s*<h3 class="text-xl font-semibold mb-3 text-\[#2C2C2C\]">([^<]+)<\/h3>\s*<p class="text-gray-700">([^<]+)<\/p>\s*<\/div>/g;

    content = content.replace(faqPattern, (match, question, answer) => {
        changes++;
        return `<div class="faq-item bg-white rounded-xl shadow-sm overflow-hidden" data-aos="fade-up">
                        <button class="faq-question w-full p-6 flex justify-between items-center text-left hover:bg-gray-50 transition-colors" aria-expanded="false">
                            <h3 class="text-xl font-semibold text-[#2C2C2C] pr-4">${question}</h3>
                            <svg class="faq-arrow w-6 h-6 text-[#cbaf82] flex-shrink-0 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                            </svg>
                        </button>
                        <div class="faq-answer hidden overflow-hidden transition-all duration-300" style="max-height: 0px;">
                            <p class="text-gray-700 px-6 pb-6">${answer}</p>
                        </div>
                    </div>`;
    });

    // Add the FAQ script before </body> if not already present
    if (!content.includes('FAQ Collapsible functionality')) {
        content = content.replace('</body>', collapsibleScript + '\n</body>');
    }

    if (changes > 0) {
        fs.writeFileSync(filePath, content, 'utf8');
        console.log(`✅ ${file}: Made ${changes} FAQ item(s) collapsible`);
    } else {
        console.log(`✓  ${file}: No FAQ items found or already collapsible`);
    }
});

console.log('\n🎉 Finished making FAQs collapsible!');
