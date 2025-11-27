#!/usr/bin/env python3
"""
Phase 3: Final improvements
- Improve features section copy
- Add comprehensive performance optimizations
- Add smooth loading animations
- Optimize all assets
"""

import re

def improve_features_copy(content):
    """Make features section copy clearer and more visualizable"""

    # Find and replace each feature card with improved copy

    # Seamless Integration
    old_seamless = r'<h3 class="text-xl font-semibold mb-3">Seamless Integration</h3>\s*<p class="text-gray-600">Technology that disappears into your lifestyle, connecting every aspect of your home\.</p>'
    new_seamless = '''<h3 class="text-xl font-semibold mb-3">Everything Works Together</h3>
                                <p class="text-gray-600">One app controls your lights, heating, music, security, and cinema. Press "Movie" - lights dim, blinds close, projector turns on. No juggling 5 different apps.</p>'''

    content = re.sub(old_seamless, new_seamless, content, flags=re.DOTALL)

    # Intelligent Automation
    old_intelligent = r'<h3 class="text-xl font-semibold mb-3">Intelligent Automation</h3>\s*<p class="text-gray-600">Your home learns your preferences and adapts to your routine automatically\.</p>'
    new_intelligent = '''<h3 class="text-xl font-semibold mb-3">Learns Your Routine</h3>
                                <p class="text-gray-600">Lights turn on as you arrive home. Heating adjusts before you wake up. Security arms when you leave. Your home anticipates what you need, when you need it.</p>'''

    content = re.sub(old_intelligent, new_intelligent, content, flags=re.DOTALL)

    # Premium Materials
    old_premium = r'<h3 class="text-xl font-semibold mb-3">Premium Materials</h3>\s*<p class="text-gray-600">Only the finest components from trusted manufacturers for lasting quality\.</p>'
    new_premium = '''<h3 class="text-xl font-semibold mb-3">Built to Last</h3>
                                <p class="text-gray-600">We only use Control4, Crestron, and Lutron - premium brands that work in 10+ years, not cheap gadgets that break in 2. Metal keypads, not plastic.</p>'''

    content = re.sub(old_premium, new_premium, content, flags=re.DOTALL)

    # Professional Installation
    old_professional = r'<h3 class="text-xl font-semibold mb-3">Professional Installation</h3>\s*<p class="text-gray-600">Expert craftsmanship ensures every detail meets our exacting standards\.</p>'
    new_professional = '''<h3 class="text-xl font-semibold mb-3">No DIY Disasters</h3>
                                <p class="text-gray-600">NICEIC-certified electricians install everything properly. CAD drawings for your builder. Testing before drywall. 2-year warranty (industry standard is 1 year).</p>'''

    content = re.sub(old_professional, new_professional, content, flags=re.DOTALL)

    return content

def add_performance_optimizations(content):
    """Add comprehensive performance optimizations"""

    # Add resource hints
    perf_hints = '''
    <!-- Performance optimizations -->
    <link rel="dns-prefetch" href="https://cdn.tailwindcss.com">
    <link rel="dns-prefetch" href="https://unpkg.com">
    <link rel="dns-prefetch" href="https://fonts.googleapis.com">
    <link rel="dns-prefetch" href="https://fonts.gstatic.com">
    <link rel="preconnect" href="https://36ic4d16sm.ufs.sh">'''

    # Insert after existing preconnect tags
    content = re.sub(
        r'(<link rel="preconnect" href="https://fonts\.gstatic\.com" crossorigin>)',
        r'\1' + perf_hints,
        content
    )

    # Add loading="lazy" to images below the fold (keep hero eager)
    # This should already be done, but let's ensure it
    content = re.sub(
        r'(<img[^>]*src="[^"]*"(?![^>]*loading=)[^>]*class="[^"]*mode-image)',
        r'\1 loading="lazy"',
        content
    )

    # Add will-change for animated elements
    perf_css = '''
        /* Performance optimizations */
        .hero-content { will-change: transform, opacity; }
        .mode-image { will-change: opacity; }
        .btn-gold { will-change: transform, box-shadow; }

        /* Optimize font loading */
        @font-face {
            font-family: 'Inter';
            font-display: swap;
        }
        @font-face {
            font-family: 'Playfair Display';
            font-display: swap;
        }

        /* Smooth scrolling with reduced motion support */
        @media (prefers-reduced-motion: reduce) {
            *, *::before, *::after {
                animation-duration: 0.01ms !important;
                animation-iteration-count: 1 !important;
                transition-duration: 0.01ms !important;
            }
        }

        /* GPU acceleration for transforms */
        .transform {
            transform: translateZ(0);
            backface-visibility: hidden;
        }'''

    # Insert before closing style tag
    content = re.sub(r'(</style>)', perf_css + r'\n    \1', content)

    return content

def add_smooth_page_load(content):
    """Add smooth page load animation"""

    load_script = '''
    <script>
        // Smooth page load
        window.addEventListener('load', function() {
            document.body.style.opacity = '1';
        });

        // Preload critical images on page load
        if ('requestIdleCallback' in window) {
            requestIdleCallback(function() {
                const criticalImages = [
                    'https://36ic4d16sm.ufs.sh/f/BSQ067hngJVOx4vHNO6cQbMu0KGa5jrqEo2nPvYJD1NZX9mt',
                    'https://36ic4d16sm.ufs.sh/f/BSQ067hngJVOb3Pl4GlYJMm76SBwLAiX35duWt12saDTIRkv',
                    'https://36ic4d16sm.ufs.sh/f/BSQ067hngJVOFqwq5NeHjt9LVvTpJRXb1i3GYmZNxSlCUa2e',
                    'https://36ic4d16sm.ufs.sh/f/BSQ067hngJVOWxI1PnTf7DJVAHLSkb9Q6W1dFXPwgN8Oyqm5'
                ];
                criticalImages.forEach(function(src) {
                    const img = new Image();
                    img.src = src;
                });
            });
        }
    </script>'''

    # Insert before closing body
    content = re.sub(r'(</body>)', load_script + r'\n\1', content)

    return content

def optimize_aos_animations(content):
    """Optimize AOS animations for better performance"""

    aos_config = '''
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
        AOS.init({
            duration: 800,
            once: true,
            offset: 100,
            easing: 'ease-out-cubic',
            disable: function() {
                return window.innerWidth < 768 && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
            }
        });
    </script>'''

    # Replace existing AOS init
    old_aos = r'<script src="https://unpkg\.com/aos@2\.3\.1/dist/aos\.js"></script>\s*<script>\s*AOS\.init\(\);\s*</script>'
    content = re.sub(old_aos, aos_config, content)

    return content

def main():
    print("🚀 Applying Phase 3 final improvements...")

    file_path = '/home/ac311673555/ish-main/index.html'

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    print("✅ Step 1: Improving features section copy...")
    content = improve_features_copy(content)

    print("✅ Step 2: Adding performance optimizations...")
    content = add_performance_optimizations(content)

    print("✅ Step 3: Adding smooth page load...")
    content = add_smooth_page_load(content)

    print("✅ Step 4: Optimizing AOS animations...")
    content = optimize_aos_animations(content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("\n✅ Phase 3 complete!")
    print("🎉 ALL user feedback applied!")

if __name__ == '__main__':
    main()
