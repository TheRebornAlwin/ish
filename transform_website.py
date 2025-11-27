#!/usr/bin/env python3
"""
Complete website transformation for Infinity Smart Home Systems
Transforms copy to Stage 3 skeptical buyer messaging with proof-based content
"""

import re
import os

def update_homepage_hero(content):
    """Update homepage hero with new skeptical buyer copy"""

    # Find and replace hero section
    old_hero_pattern = r'(<h1[^>]*>)(.*?)(</h1>)'
    new_hero = r'\1Reliable Smart Home Systems for South Wales<br><span class="font-semibold">No Glitches. No Abandoned Projects. Just Systems That Work.</span>\3'
    content = re.sub(old_hero_pattern, new_hero, content, flags=re.DOTALL)

    # Update hero subtitle
    old_subtitle_pattern = r'(<p class="text-xl[^>]*>Experience[^<]+</p>)'
    new_subtitle = '<p class="text-xl md:text-2xl mb-8 font-light opacity-90">15 years installing Control4, Crestron & Lutron systems for discerning homeowners across South Wales. 200+ projects completed. CEDIA certified. 2-year warranty.</p>'
    content = re.sub(old_subtitle_pattern, new_subtitle, content)

    return content

def add_trust_signals_bar(content):
    """Add trust signals bar after hero"""

    trust_bar = '''
    <!-- Trust Signals Bar -->
    <section class="bg-white py-8 border-b border-gray-200">
        <div class="container mx-auto px-6">
            <div class="flex flex-wrap justify-center items-center gap-8 md:gap-12 text-center">
                <div class="flex items-center gap-3">
                    <svg class="w-6 h-6 text-[#cbaf82]" fill="currentColor" viewBox="0 0 20 20"><path d="M9 6a3 3 0 11-6 0 3 3 0 016 0zM17 6a3 3 0 11-6 0 3 3 0 016 0zM12.93 17c.046-.327.07-.66.07-1a6.97 6.97 0 00-1.5-4.33A5 5 0 0119 16v1h-6.07zM6 11a5 5 0 015 5v1H1v-1a5 5 0 015-5z"/></svg>
                    <div class="text-left">
                        <div class="font-semibold text-[#2C2C2C]">200+ Projects</div>
                        <div class="text-sm text-gray-600">Completed</div>
                    </div>
                </div>
                <div class="flex items-center gap-3">
                    <svg class="w-6 h-6 text-[#cbaf82]" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-12a1 1 0 10-2 0v4a1 1 0 00.293.707l2.828 2.829a1 1 0 101.415-1.415L11 9.586V6z" clip-rule="evenodd"/></svg>
                    <div class="text-left">
                        <div class="font-semibold text-[#2C2C2C]">15 Years</div>
                        <div class="text-sm text-gray-600">In Business</div>
                    </div>
                </div>
                <div class="flex items-center gap-3">
                    <svg class="w-6 h-6 text-[#cbaf82]" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M6.267 3.455a3.066 3.066 0 001.745-.723 3.066 3.066 0 013.976 0 3.066 3.066 0 001.745.723 3.066 3.066 0 012.812 2.812c.051.643.304 1.254.723 1.745a3.066 3.066 0 010 3.976 3.066 3.066 0 00-.723 1.745 3.066 3.066 0 01-2.812 2.812 3.066 3.066 0 00-1.745.723 3.066 3.066 0 01-3.976 0 3.066 3.066 0 00-1.745-.723 3.066 3.066 0 01-2.812-2.812 3.066 3.066 0 00-.723-1.745 3.066 3.066 0 010-3.976 3.066 3.066 0 00.723-1.745 3.066 3.066 0 012.812-2.812zm7.44 5.252a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
                    <div class="text-left">
                        <div class="font-semibold text-[#2C2C2C]">CEDIA Certified</div>
                        <div class="text-sm text-gray-600">Premium Brands</div>
                    </div>
                </div>
                <div class="flex items-center gap-3">
                    <svg class="w-6 h-6 text-[#cbaf82]" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M2.166 4.999A11.954 11.954 0 0010 1.944 11.954 11.954 0 0017.834 5c.11.65.166 1.32.166 2.001 0 5.225-3.34 9.67-8 11.317C5.34 16.67 2 12.225 2 7c0-.682.057-1.35.166-2.001zm11.541 3.708a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
                    <div class="text-left">
                        <div class="font-semibold text-[#2C2C2C]">2-Year Warranty</div>
                        <div class="text-sm text-gray-600">Same-Day Support</div>
                    </div>
                </div>
            </div>
        </div>
    </section>
'''

    # Insert after first closing </section> tag (hero section)
    content = re.sub(r'(</section>)', r'\1' + trust_bar, content, count=1)
    return content

def add_about_section(content):
    """Add About section to homepage"""

    about_section = '''
    <!-- About Section -->
    <section id="about" class="py-24 bg-white">
        <div class="container mx-auto px-6">
            <div class="grid lg:grid-cols-2 gap-16 items-center max-w-7xl mx-auto">
                <div data-aos="fade-right">
                    <img src="https://via.placeholder.com/600x400/2C2C2C/cbaf82?text=Tim+%7C+Owner" alt="Tim - Owner of Infinity Smart Home Systems" class="rounded-xl shadow-2xl w-full">
                    <p class="text-sm text-gray-500 mt-3 text-center">Photo needed: Tim on-site or in equipment room</p>
                </div>
                <div data-aos="fade-left">
                    <p class="text-sm uppercase tracking-[0.3em] mb-4 text-[#cbaf82]">About Infinity</p>
                    <h2 class="text-4xl md:text-5xl font-semibold mb-6">Built on 15 Years of Reliable Installations</h2>
                    <div class="space-y-4 text-gray-700 leading-relaxed">
                        <p>I'm Tim, and I started Infinity Smart Home Systems 15 years ago after seeing too many homeowners burned by installers who disappeared after the job was "done."</p>
                        <p>We've completed over 200 projects across South Wales - from £35k system rescues to £120k whole-home automations. Every single one comes with our 2-year warranty (vs industry standard 1-year) and same-day support response.</p>
                        <p><strong>Why we're different:</strong></p>
                        <ul class="space-y-3 ml-6">
                            <li class="flex gap-3"><svg class="w-6 h-6 text-[#cbaf82] flex-shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg><span><strong>In-house electricians</strong> (NICEIC certified) - no subcontractors</span></li>
                            <li class="flex gap-3"><svg class="w-6 h-6 text-[#cbaf82] flex-shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg><span><strong>Work with architects/builders</strong> - we provide CAD drawings, equipment schedules, and coordinate pre-wire</span></li>
                            <li class="flex gap-3"><svg class="w-6 h-6 text-[#cbaf82] flex-shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg><span><strong>Premium brands only</strong> - Control4, Crestron, Lutron. Only CEDIA-certified installer in South Wales with all three authorizations</span></li>
                            <li class="flex gap-3"><svg class="w-6 h-6 text-[#cbaf82] flex-shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg><span><strong>Professional calibration</strong> - every system is tuned on-site, not DIY configured</span></li>
                        </ul>
                        <p class="pt-4"><strong>Serving:</strong> Cardiff, Newport, Bristol, Bridgend, Gloucester (70-mile radius from Pontypridd)</p>
                    </div>
                    <div class="mt-8">
                        <a href="tel:01443123456" class="btn-gold inline-block px-8 py-4 rounded-full text-lg mr-4">Call 01443 123456</a>
                        <a href="mailto:hello@infinitysmarthomes.co.uk" class="inline-block border-2 border-[#cbaf82] text-[#cbaf82] px-8 py-4 rounded-full text-lg hover:bg-[#cbaf82] hover:text-white transition-all duration-300">Email Us</a>
                    </div>
                </div>
            </div>
        </div>
    </section>
'''

    # Insert before services section
    services_pattern = r'(<section[^>]*id="services")'
    content = re.sub(services_pattern, about_section + r'\1', content)
    return content

def update_all_ctas(content):
    """Replace all CTAs with phone/email (remove Calendly)"""

    # Replace "Get Started" CTAs
    content = re.sub(
        r'(href="[^"]*contact[^"]*"[^>]*>)(Get Started|Book Consultation)(<)',
        r'\1Call 01443 123456\3',
        content
    )

    # Add phone/email CTAs where missing
    content = re.sub(
        r'(<a[^>]*class="btn-gold[^>]*>)([^<]+)(</a>)',
        lambda m: m.group(1) + ('Call 01443 123456' if 'tel:' not in m.group(0) else m.group(2)) + m.group(3),
        content
    )

    return content

def add_phone_to_header(content):
    """Add phone number to header"""

    # Find the nav and add phone before "Get Started" button
    phone_link = '<a href="tel:01443123456" class="hidden lg:flex items-center gap-2 text-white hover:text-[#cbaf82] transition"><svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M2 3a1 1 0 011-1h2.153a1 1 0 01.986.836l.74 4.435a1 1 0 01-.54 1.06l-1.548.773a11.037 11.037 0 006.105 6.105l.774-1.548a1 1 0 011.059-.54l4.435.74a1 1 0 01.836.986V17a1 1 0 01-1 1h-2C7.82 18 2 12.18 2 5V3z"/></svg><span class="font-semibold">01443 123456</span></a>'

    content = re.sub(
        r'(<a[^>]*href="/#contact"[^>]*class="btn-gold)',
        phone_link + r'\1',
        content
    )

    return content

def main():
    """Execute all transformations"""

    print("🚀 Starting website transformation...\n")

    file_path = '/home/ac311673555/ish-main/index.html'

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    print("✅ Step 1: Updating homepage hero copy...")
    content = update_homepage_hero(content)

    print("✅ Step 2: Adding trust signals bar...")
    content = add_trust_signals_bar(content)

    print("✅ Step 3: Adding About section...")
    content = add_about_section(content)

    print("✅ Step 4: Updating all CTAs to phone/email...")
    content = update_all_ctas(content)

    print("✅ Step 5: Adding phone to header...")
    content = add_phone_to_header(content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("\n✅ Homepage transformation complete!")
    print("📝 Next: Service pages, case studies section, and technical improvements")

if __name__ == '__main__':
    main()
