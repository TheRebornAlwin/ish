#!/usr/bin/env python3
"""
Apply comprehensive user feedback to homepage:
1. Revert hero to "INFINITE CONTROL" with better font
2. Optimize trust signals bar
3. Preload tab images
4. Revert slider to click-and-drag
5. Improve features copy
6. Add pricing to case study cards
7. Create case studies page
8. Restore and fix scroll-locked process section
9. Fix footer layout
10. Add contact modal with form
11. Performance optimizations
"""

import re

def revert_hero_section(content):
    """Revert hero to original INFINITE CONTROL design with improved font"""

    old_hero = r'<h1 class="text-5xl md:text-7xl lg:text-8xl mb-6 leading-tight">Reliable Smart Home Systems for South Wales<br><span class="font-semibold">No Glitches\. No Abandoned Projects\. Just Systems That Work\.</span></h1>'

    new_hero = '''<h1 class="text-5xl md:text-7xl lg:text-8xl mb-6 leading-tight">
                <span class="font-light italic gold-shine-text">Your Home.</span><br>
                <span class="font-bold uppercase tracking-wide" style="font-family: 'Playfair Display', serif; letter-spacing: 0.05em;">INFINITE CONTROL.</span>
            </h1>'''

    content = re.sub(old_hero, new_hero, content)
    return content

def optimize_trust_signals(content):
    """Make trust signals more subtle and refined"""

    old_trust = r'(<section class="bg-white py-8 border-b border-gray-200">)'
    new_trust = r'<section class="bg-gradient-to-b from-white to-[#F5F3EF] py-12">'

    content = re.sub(old_trust, new_trust, content)

    # Make the trust signal icons slightly smaller and more refined
    content = re.sub(
        r'<svg class="w-6 h-6 text-\[#cbaf82\]"',
        r'<svg class="w-5 h-5 text-[#cbaf82] opacity-80"',
        content
    )

    return content

def add_image_preloading(content):
    """Add preload hints for tab images to eliminate delay"""

    preload_links = '''
    <!-- Preload tab images for instant switching -->
    <link rel="preload" as="image" href="https://36ic4d16sm.ufs.sh/f/BSQ067hngJVOx4vHNO6cQbMu0KGa5jrqEo2nPvYJD1NZX9mt">
    <link rel="preload" as="image" href="https://36ic4d16sm.ufs.sh/f/BSQ067hngJVOb3Pl4GlYJMm76SBwLAiX35duWt12saDTIRkv">
    <link rel="preload" as="image" href="https://36ic4d16sm.ufs.sh/f/BSQ067hngJVOFqwq5NeHjt9LVvTpJRXb1i3GYmZNxSlCUa2e">
    <link rel="preload" as="image" href="https://36ic4d16sm.ufs.sh/f/BSQ067hngJVOWxI1PnTf7DJVAHLSkb9Q6W1dFXPwgN8Oyqm5">'''

    # Insert before </head>
    content = re.sub(r'(</head>)', preload_links + r'\n    \1', content)

    return content

def change_header_cta(content):
    """Change header CTA button to 'Get Started' that opens modal"""

    # Desktop CTA
    content = re.sub(
        r'<a href="#contact" class="btn-gold px-6 py-2 rounded-full text-sm font-medium">Call 01443 123456</a>',
        r'<button onclick="openContactModal()" class="btn-gold px-6 py-2 rounded-full text-sm font-medium">Get Started</button>',
        content
    )

    # Mobile CTA
    content = re.sub(
        r'<a href="#contact" class="block text-center btn-gold px-6 py-2 rounded-full">Call 01443 123456</a>',
        r'<button onclick="openContactModal()" class="block w-full text-center btn-gold px-6 py-2 rounded-full">Get Started</button>',
        content
    )

    return content

def add_contact_modal(content):
    """Add contact modal popup with form"""

    modal_html = '''
    <!-- Contact Modal -->
    <div id="contactModal" class="fixed inset-0 z-[100] hidden">
        <!-- Overlay -->
        <div class="absolute inset-0 bg-black/70 backdrop-blur-sm" onclick="closeContactModal()"></div>

        <!-- Modal Content -->
        <div class="relative flex items-center justify-center min-h-screen p-4">
            <div id="modalCard" class="bg-white rounded-2xl shadow-2xl max-w-lg w-full p-8 transform scale-95 opacity-0 transition-all duration-300">
                <!-- Close Button -->
                <button onclick="closeContactModal()" class="absolute top-4 right-4 text-gray-400 hover:text-gray-600 transition">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                    </svg>
                </button>

                <!-- Form State -->
                <div id="formState" class="form-state">
                    <h2 class="text-3xl font-semibold mb-2 text-[#2C2C2C]">Get Started</h2>
                    <p class="text-gray-600 mb-2">We'll reply within 24 hours</p>
                    <p class="text-sm text-gray-500 mb-6">Don't want to wait? <a href="tel:01443123456" class="text-[#cbaf82] hover:underline font-semibold">Call us now</a></p>

                    <form id="contactForm" class="space-y-4" onsubmit="handleFormSubmit(event)">
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-1">Name</label>
                            <input type="text" required class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#cbaf82] focus:border-transparent transition" placeholder="Your name">
                        </div>

                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-1">Phone or Email</label>
                            <input type="text" required class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#cbaf82] focus:border-transparent transition" placeholder="Best way to reach you">
                        </div>

                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-1">Project Details</label>
                            <textarea required rows="4" class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#cbaf82] focus:border-transparent transition resize-none" placeholder="Tell us about your property, what you're looking for, timeline, and any specific requirements..."></textarea>
                        </div>

                        <button type="submit" class="w-full btn-gold py-4 rounded-lg text-lg font-semibold">Submit</button>

                        <p class="text-center text-sm text-gray-500 mt-4">
                            Or, email us: <a href="mailto:hello@infinitysmarthomes.co.uk" class="text-[#cbaf82] hover:underline">hello@infinitysmarthomes.co.uk</a>
                        </p>
                    </form>
                </div>

                <!-- Success State -->
                <div id="successState" class="success-state hidden text-center">
                    <div class="checkmark-container mb-6">
                        <svg class="checkmark w-20 h-20 mx-auto text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                        </svg>
                    </div>
                    <h2 class="text-3xl font-semibold mb-4 text-[#2C2C2C]">Success!</h2>
                    <p class="text-lg text-gray-600">We'll respond within 24 hours</p>
                </div>
            </div>
        </div>
    </div>'''

    # Insert before closing body tag
    content = re.sub(r'(</body>)', modal_html + r'\n\1', content)

    return content

def add_modal_scripts(content):
    """Add JavaScript for modal functionality"""

    modal_js = '''
    <script>
        function openContactModal() {
            const modal = document.getElementById('contactModal');
            const card = document.getElementById('modalCard');
            modal.classList.remove('hidden');
            // Trigger animation after display
            setTimeout(() => {
                card.classList.remove('scale-95', 'opacity-0');
                card.classList.add('scale-100', 'opacity-100');
            }, 10);
            document.body.style.overflow = 'hidden';
        }

        function closeContactModal() {
            const modal = document.getElementById('contactModal');
            const card = document.getElementById('modalCard');
            card.classList.add('scale-95', 'opacity-0');
            card.classList.remove('scale-100', 'opacity-100');
            setTimeout(() => {
                modal.classList.add('hidden');
                document.body.style.overflow = 'auto';
                // Reset form
                document.getElementById('formState').classList.remove('hidden');
                document.getElementById('successState').classList.add('hidden');
                document.getElementById('contactForm').reset();
            }, 300);
        }

        function handleFormSubmit(event) {
            event.preventDefault();
            // Show success state with animation
            const formState = document.getElementById('formState');
            const successState = document.getElementById('successState');

            formState.style.opacity = '0';
            formState.style.transform = 'scale(0.95)';

            setTimeout(() => {
                formState.classList.add('hidden');
                successState.classList.remove('hidden');
                successState.style.opacity = '0';
                successState.style.transform = 'scale(0.95)';

                setTimeout(() => {
                    successState.style.opacity = '1';
                    successState.style.transform = 'scale(1)';
                }, 50);
            }, 300);

            // Auto-close after 3 seconds
            setTimeout(() => {
                closeContactModal();
            }, 3000);

            return false;
        }
    </script>'''

    # Insert before closing body tag
    content = re.sub(r'(</body>)', modal_js + r'\n\1', content)

    return content

def add_modal_styles(content):
    """Add CSS for modal animations"""

    modal_css = '''
        /* Modal animations */
        .form-state, .success-state {
            transition: all 300ms cubic-bezier(0.34, 1.56, 0.64, 1);
        }

        .checkmark {
            animation: checkmark 0.6s ease-in-out;
        }

        @keyframes checkmark {
            0% { transform: scale(0) rotate(0deg); opacity: 0; }
            50% { transform: scale(1.2) rotate(10deg); }
            100% { transform: scale(1) rotate(0deg); opacity: 1; }
        }'''

    # Insert before closing style tag
    content = re.sub(r'(</style>)', modal_css + r'\n    \1', content)

    return content

def main():
    print("🚀 Applying user feedback changes...")

    file_path = '/home/ac311673555/ish-main/index.html'

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    print("✅ Step 1: Reverting hero to INFINITE CONTROL...")
    content = revert_hero_section(content)

    print("✅ Step 2: Optimizing trust signals bar...")
    content = optimize_trust_signals(content)

    print("✅ Step 3: Adding image preloading...")
    content = add_image_preloading(content)

    print("✅ Step 4: Changing header CTA to 'Get Started'...")
    content = change_header_cta(content)

    print("✅ Step 5: Adding contact modal...")
    content = add_contact_modal(content)
    content = add_modal_scripts(content)
    content = add_modal_styles(content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("\n✅ Phase 1 complete! Hero, trust signals, modal added.")
    print("📝 Next: Footer fixes, scroll-jacking restoration, case studies page, slider fixes...")

if __name__ == '__main__':
    main()
