#!/usr/bin/env python3
"""
Phase 2: More complex feedback changes
- Restore scroll-locked process section
- Fix footer layout
- Revert slider to click-and-drag
- Add pricing to case study cards
- Create case studies page
"""

import re

def restore_scroll_jacking(content):
    """Restore the scroll-locked process section with bulletproof implementation"""

    # Find the process section and add back the scroll-jacking JavaScript
    scroll_js = '''
    <script>
        // Robust scroll-jacking for process section
        (function() {
            const processSection = document.getElementById('process-section');
            if (!processSection) return;

            const steps = ['introductory-call', 'showroom-visit', 'design', 'permitting', 'manufacturing', 'installation', 'move-in'];
            let currentStepIndex = 0;
            let isLocked = false;
            let scrollAccumulator = 0;
            const scrollThreshold = 100; // Pixels needed to trigger step change

            function setActiveStep(index) {
                if (index < 0 || index >= steps.length) return;
                currentStepIndex = index;
                steps.forEach((step, i) => {
                    const element = document.getElementById(step);
                    if (element) {
                        element.classList.toggle('active', i === index);
                    }
                });
            }

            function handleScroll(e) {
                if (!isLocked) return;

                const delta = e.deltaY || e.detail || -e.wheelDelta;
                scrollAccumulator += delta;

                // Check if we've scrolled enough to change steps
                if (Math.abs(scrollAccumulator) >= scrollThreshold) {
                    if (scrollAccumulator > 0 && currentStepIndex < steps.length - 1) {
                        // Scrolling down
                        currentStepIndex++;
                        setActiveStep(currentStepIndex);
                        scrollAccumulator = 0;
                    } else if (scrollAccumulator < 0 && currentStepIndex > 0) {
                        // Scrolling up
                        currentStepIndex--;
                        setActiveStep(currentStepIndex);
                        scrollAccumulator = 0;
                    } else if (scrollAccumulator > 0 && currentStepIndex === steps.length - 1) {
                        // At last step, scrolling down - unlock
                        isLocked = false;
                        scrollAccumulator = 0;
                        return; // Allow normal scroll
                    } else if (scrollAccumulator < 0 && currentStepIndex === 0) {
                        // At first step, scrolling up - unlock
                        isLocked = false;
                        scrollAccumulator = 0;
                        return; // Allow normal scroll
                    } else {
                        scrollAccumulator = 0;
                    }
                }

                // Prevent default scroll
                e.preventDefault();
                e.stopPropagation();
            }

            // Observer to detect when section is in viewport
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting && entry.intersectionRatio > 0.5) {
                        // Section is in view, lock scrolling
                        isLocked = true;
                        if (currentStepIndex === 0) {
                            setActiveStep(0);
                        }
                    } else if (!entry.isIntersecting) {
                        // Section out of view, unlock
                        isLocked = false;
                        scrollAccumulator = 0;
                    }
                });
            }, { threshold: [0, 0.5, 1] });

            observer.observe(processSection);

            // Listen to wheel events on entire document
            document.addEventListener('wheel', handleScroll, { passive: false });
            document.addEventListener('touchmove', handleScroll, { passive: false });

            // Initialize first step
            setActiveStep(0);
        })();
    </script>'''

    # Remove old comment about scroll hijacking being removed
    content = re.sub(r'// Scroll hijacking removed[^\n]+\n[^\n]+\n', '', content)

    # Add new scroll-jacking script before closing body
    content = re.sub(r'(</body>)', scroll_js + r'\n\1', content)

    return content

def fix_footer_layout(content):
    """Fix footer: combine services lists, put legal on same row"""

    # Find and replace entire footer section
    old_footer_pattern = r'<!-- Footer -->.*?</footer>'

    new_footer = '''<!-- Footer -->
    <footer class="bg-[#2C2C2C] text-white py-12">
        <div class="container mx-auto px-6">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-8">
                <!-- Services -->
                <div>
                    <h3 class="text-lg font-semibold mb-4 text-[#cbaf82]">Services</h3>
                    <ul class="space-y-2 text-sm">
                        <li><a href="/smart-home-design.html" class="hover:text-[#cbaf82] transition">Smart Home Design</a></li>
                        <li><a href="/home-theatre.html" class="hover:text-[#cbaf82] transition">Home Theatre</a></li>
                        <li><a href="/wifi-networking.html" class="hover:text-[#cbaf82] transition">Wi-Fi & Networking</a></li>
                        <li><a href="/multi-room-audio.html" class="hover:text-[#cbaf82] transition">Multi-Room Audio</a></li>
                        <li><a href="/video-distribution.html" class="hover:text-[#cbaf82] transition">Video Distribution</a></li>
                        <li><a href="/smart-shading.html" class="hover:text-[#cbaf82] transition">Smart Shading</a></li>
                        <li><a href="/security-cctv.html" class="hover:text-[#cbaf82] transition">Security & CCTV</a></li>
                        <li><a href="/electrical-installation.html" class="hover:text-[#cbaf82] transition">Electrical Installation</a></li>
                    </ul>
                </div>

                <!-- Company -->
                <div>
                    <h3 class="text-lg font-semibold mb-4 text-[#cbaf82]">Company</h3>
                    <ul class="space-y-2 text-sm">
                        <li><a href="#about" class="hover:text-[#cbaf82] transition">About Us</a></li>
                        <li><a href="#case-studies" class="hover:text-[#cbaf82] transition">Case Studies</a></li>
                        <li><a href="#process" class="hover:text-[#cbaf82] transition">Our Process</a></li>
                    </ul>
                </div>

                <!-- Contact -->
                <div>
                    <h3 class="text-lg font-semibold mb-4 text-[#cbaf82]">Contact</h3>
                    <ul class="space-y-2 text-sm">
                        <li><a href="tel:01443123456" class="hover:text-[#cbaf82] transition">01443 123456</a></li>
                        <li><a href="mailto:hello@infinitysmarthomes.co.uk" class="hover:text-[#cbaf82] transition">hello@infinitysmarthomes.co.uk</a></li>
                        <li class="text-gray-400">Pontypridd, South Wales</li>
                        <li class="text-gray-400">70-mile service radius</li>
                    </ul>
                </div>
            </div>

            <!-- Bottom Row: Copyright and Legal on same line -->
            <div class="border-t border-gray-700 pt-6 flex flex-col md:flex-row justify-between items-center text-sm text-gray-400">
                <p>&copy; 2025 Infinity Smart Home Systems. All rights reserved.</p>
                <div class="flex gap-6 mt-4 md:mt-0">
                    <a href="/privacy-policy.html" class="hover:text-[#cbaf82] transition">Privacy Policy</a>
                    <a href="/terms-conditions.html" class="hover:text-[#cbaf82] transition">Terms & Conditions</a>
                    <a href="/cookies-policy.html" class="hover:text-[#cbaf82] transition">Cookies</a>
                </div>
            </div>
        </div>
    </footer>'''

    content = re.sub(old_footer_pattern, new_footer, content, flags=re.DOTALL)

    return content

def revert_slider_to_click_drag(content):
    """Revert before/after slider to click-and-drag instead of auto-follow"""

    # Find the slider JavaScript and modify it
    old_slider_js = r'container\.addEventListener\("mousemove".*?}\);'

    new_slider_js = '''let isDragging = false;

                container.addEventListener("mousedown", () => {
                    isDragging = true;
                });

                document.addEventListener("mouseup", () => {
                    isDragging = false;
                });

                container.addEventListener("mousemove", (e) => {
                    if (!isDragging) return;
                    const rect = container.getBoundingClientRect();
                    const x = Math.max(0, Math.min(e.clientX - rect.left, rect.width));
                    const percent = (x / rect.width) * 100;
                    updateSlider(percent);
                });

                container.addEventListener("touchstart", () => {
                    isDragging = true;
                });

                container.addEventListener("touchend", () => {
                    isDragging = false;
                });

                container.addEventListener("touchmove", (e) => {
                    if (!isDragging) return;
                    const rect = container.getBoundingClientRect();
                    const touch = e.touches[0];
                    const x = Math.max(0, Math.min(touch.clientX - rect.left, rect.width));
                    const percent = (x / rect.width) * 100;
                    updateSlider(percent);
                });'''

    content = re.sub(old_slider_js, new_slider_js, content, flags=re.DOTALL)

    # Add cursor style change
    content = re.sub(
        r'(\.before-after-container \{[^}]+)',
        r'\1 cursor: grab;',
        content
    )

    content = re.sub(
        r'(\.before-after-container:active \{)',
        r'.before-after-container:active { cursor: grabbing; }\n        \1',
        content
    )

    return content

def add_pricing_to_case_studies(content):
    """Add pricing prominently to each case study card"""

    # Cardiff Bay - add £85,000 prominently
    content = re.sub(
        r'(<div class="bg-white rounded-xl p-8 shadow-lg" data-aos="fade-up">.*?<h3 class="text-2xl font-semibold mb-4 text-\[#2C2C2C\]">Cardiff Bay Penthouse Cinema</h3>)',
        r'\1\n                        <div class="text-3xl font-bold text-[#cbaf82] mb-4">£85,000</div>',
        content,
        flags=re.DOTALL
    )

    # Bristol - add £120,000
    content = re.sub(
        r'(<div class="bg-white rounded-xl p-8 shadow-lg" data-aos="fade-up" data-aos-delay="100">.*?<h3 class="text-2xl font-semibold mb-4 text-\[#2C2C2C\]">Bristol New Build - Whole Home Automation</h3>)',
        r'\1\n                        <div class="text-3xl font-bold text-[#cbaf82] mb-4">£120,000</div>',
        content,
        flags=re.DOTALL
    )

    # Newport - add £35,000
    content = re.sub(
        r'(<div class="bg-white rounded-xl p-8 shadow-lg" data-aos="fade-up" data-aos-delay="200">.*?<h3 class="text-2xl font-semibold mb-4 text-\[#2C2C2C\]">Newport Retrofit - System Rescue</h3>)',
        r'\1\n                        <div class="text-3xl font-bold text-[#cbaf82] mb-4">£35,000</div>',
        content,
        flags=re.DOTALL
    )

    # Add "View All Case Studies" link after the grid
    view_all_link = '''
                <div class="text-center mt-12" data-aos="fade-up">
                    <a href="/case-studies.html" class="inline-flex items-center gap-2 text-[#cbaf82] hover:text-[#d4ba8f] transition text-lg font-semibold">
                        <span>View All Case Studies</span>
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
                        </svg>
                    </a>
                </div>'''

    # Add after the case studies grid
    content = re.sub(
        r'(</div>\s*</div>\s*</section>\s*<!-- About Section -->)',
        view_all_link + r'\n            \1',
        content
    )

    return content

def main():
    print("🚀 Applying Phase 2 feedback changes...")

    file_path = '/home/ac311673555/ish-main/index.html'

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    print("✅ Step 1: Restoring scroll-locked process section...")
    content = restore_scroll_jacking(content)

    print("✅ Step 2: Fixing footer layout...")
    content = fix_footer_layout(content)

    print("✅ Step 3: Reverting slider to click-and-drag...")
    content = revert_slider_to_click_drag(content)

    print("✅ Step 4: Adding pricing to case study cards...")
    content = add_pricing_to_case_studies(content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("\n✅ Phase 2 complete!")
    print("📝 Next: Case studies page, features copy improvement, performance optimizations...")

if __name__ == '__main__':
    main()
