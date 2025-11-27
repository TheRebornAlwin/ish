#!/usr/bin/env python3
"""
Rewrite all 8 service pages with:
- Specific pricing
- Who needs this sections
- Technical specs
- Real examples
- FAQ sections
- Differentiated content
"""

import re
import os

SERVICE_DATA = {
    'smart-home-design': {
        'title': 'Smart Home Design & Integration',
        'subtitle': 'Whole-Home Automation Designed Right From Day One',
        'who_needs': 'New build homeowners, architects needing pre-wire specs, major renovation projects',
        'tech': 'Control4 EA series controllers, Lutron lighting systems, Ubiquiti enterprise networking',
        'starting_price': '£15,000',
        'price_range': '£40,000-£150,000 for complete whole-home systems',
        'example': 'New build in Cardiff Bay - 5-bed penthouse with whole-home Control4, 40-zone Lutron lighting, automated shading across 12 windows',
        'approach': 'We provide CAD drawings and equipment schedules for your builder. We coordinate pre-wire walk-throughs, test points before drywall, and program scenes after install.',
        'faqs': [
            ('How early should we involve you in a new build?', 'As soon as architectural plans are finalized - ideally 6-12 months before move-in. We need to coordinate with your electrician during first fix (before walls are closed).'),
            ('Do you work with architects and builders?', 'Yes - we provide CAD drawings, equipment schedules, and attend site meetings. Your builder gets exact cable routes, box locations, and a clear timeline.'),
            ('What if our builder has never done smart homes?', 'We guide them through every step. We provide labeled cable plans, coordinate site visits, and test every connection before drywall goes up.'),
            ('Can you retrofit an existing home?', 'Yes, though it\'s more complex and expensive. Wireless systems (Lutron RA3, Control4) work well for retrofits without rewiring.'),
        ]
    },
    'home-theatre': {
        'title': 'Home Theatre & Cinema Rooms',
        'subtitle': 'Cinema-Quality Entertainment Without Leaving Home',
        'who_needs': 'Homeowners with dedicated media rooms, basements, spare bedrooms, or luxury properties wanting private cinema experiences',
        'tech': 'Sony/JVC 4K laser projectors, Triad/KEF speakers, Stewart Filmscreen, Control4/Crestron control, professional acoustic treatment',
        'starting_price': '£25,000',
        'price_range': '£80,000+ for full custom cinema with Dolby Atmos',
        'example': '5-bed in Clifton - 16-seat dedicated cinema with JVC NX7 projector, Dolby Atmos 7.2.4 surround, acoustic panels, motorized recliners',
        'approach': 'We do acoustic modeling before install, design seating layouts for optimal sound/picture, calibrate professionally (not DIY), include 2-year warranty.',
        'faqs': [
            ('How big does the room need to be?', 'Minimum 12x15 feet for basic setup. Ideal is 16x20+ for proper seating distance and surround sound. We can work with most spaces.'),
            ('Projector vs large TV - which is better?', 'For true cinema feel, projector wins (100-150" screens). For bright rooms or casual viewing, high-end 85"+ TV works well.'),
            ('What\'s Dolby Atmos and do I need it?', 'Overhead speakers for 3D sound - helicopters fly over you, rain falls around you. Worth it for dedicated cinemas, optional for casual setups.'),
            ('Can you soundproof the room?', 'Yes - acoustic treatment (absorbs echo) and soundproofing (blocks noise to neighbors) are different. We handle both.'),
        ]
    },
    'wifi-networking': {
        'title': 'Enterprise WiFi & Networking',
        'subtitle': 'Rock-Solid Connectivity for Smart Homes',
        'who_needs': 'Anyone with dead zones, dropouts, buffering, or 50+ connected devices (smart homes need robust enterprise-grade WiFi)',
        'tech': 'Ubiquiti UniFi, Ruckus, Cisco Meraki - enterprise access points, managed switches, VLAN segmentation for security',
        'starting_price': '£3,000',
        'price_range': '£8,000+ for large properties with outdoor coverage and 10Gb backbone',
        'example': '6-bed new build in Newport - 12 UniFi access points, wired backhaul, separate VLANs for IoT/guests/security, 10Gb backbone for 4K streaming',
        'approach': 'We site-survey with heat mapping, install wired backhaul (no mesh drop-offs), configure VLANs for security, provide ongoing cloud monitoring.',
        'faqs': [
            ('Why not just use BT/Sky router?', 'Consumer routers fail with 30+ devices. Smart homes have 50-100+ devices. You need enterprise gear that won\'t crash.'),
            ('What\'s a VLAN and why do I need it?', 'Separates IoT devices (security risk) from your main network. If smart bulb gets hacked, they can\'t access your laptop.'),
            ('How many access points do I need?', '1 per 800-1000 sq ft for solid coverage. Thick walls, concrete, or outdoor areas need more. We survey first.'),
            ('Can you fix existing WiFi issues?', 'Yes - we diagnose (usually too few APs, wrong placement, or interference), then upgrade to enterprise system.'),
        ]
    },
    'multi-room-audio': {
        'title': 'Multi-Room Audio Systems',
        'subtitle': 'Music Throughout Your Home, Controlled From Anywhere',
        'who_needs': 'Homeowners wanting music in every room, outdoor entertaining spaces, whole-home background audio',
        'tech': 'Control4/Sonos multi-room systems, Triad in-ceiling speakers, KEF architectural speakers, Autonomic streaming servers',
        'starting_price': '£8,000',
        'price_range': '£25,000+ for high-end distributed audio with outdoor zones',
        'example': '4-bed in Bristol - 12-zone audio with Triad speakers, outdoor patio system, Control4 app control, Spotify/Tidal/Apple Music integration',
        'approach': 'We match speaker placement to room acoustics, hide all wiring in walls/ceilings, tune EQ per zone, integrate with lighting scenes (dinner party mode).',
        'faqs': [
            ('Sonos vs Control4 - which is better?', 'Sonos is easier DIY, great sound. Control4 integrates with lighting/shades/security for whole-home scenes. We install both.'),
            ('Can I play different music in each room?', 'Yes - each zone is independent. Kitchen plays Radio 2, bedroom plays Spotify, living room plays vinyl. All from one app.'),
            ('What about outdoor speakers?', 'Weather-resistant models rated IP65+. We install underground conduit, weatherproof connections. 2-year warranty covers outdoor.'),
            ('Can you add to existing system?', 'Usually yes - depends on current equipment capacity. We can expand or replace if maxed out.'),
        ]
    },
    'video-distribution': {
        'title': 'Video Distribution Systems',
        'subtitle': 'Watch Any Source on Any TV - No Boxes in Every Room',
        'who_needs': 'Properties with multiple TVs wanting centralized source control (Sky box in utility room, viewed anywhere)',
        'tech': '4K HDBaseT matrix switchers, Crestron DM, Control4 video distribution over CAT6 cabling',
        'starting_price': '£4,000',
        'price_range': '£12,000+ for 8+ displays with 4K/HDR support',
        'example': 'New build in Cardiff - 8-TV 4K distribution, centralized Sky/Apple TV/PS5 in equipment closet, any source to any TV',
        'approach': 'Single equipment rack in utility room, CAT6 to every TV location (hidden in walls), 4K certified, IR control from any room.',
        'faqs': [
            ('Why not just buy multiple Sky boxes?', '£100+/year per extra box. Video distribution is one-time cost, cleaner install, easier to use.'),
            ('Does 4K work over long cable runs?', 'Yes - HDBaseT sends 4K/HDR up to 100 meters over single CAT6. No quality loss.'),
            ('Can I watch different sources on different TVs?', 'Yes - living room watches Sky Sports, bedroom watches Netflix, kitchen watches Apple TV. Matrix switcher handles routing.'),
            ('What if I add another TV later?', 'Easy - we install spare CAT6 runs during build. Just add TV and program matrix. Takes 30 minutes.'),
        ]
    },
    'smart-shading': {
        'title': 'Smart Shading & Motorized Blinds',
        'subtitle': 'Automated Light Control for Comfort & Energy Savings',
        'who_needs': 'Properties with large windows, conservatories, south-facing rooms (glare/heat control), cinema rooms needing blackout',
        'tech': 'Lutron motorized blinds, Somfy motors, Silent Gliss tracks, integrated with lighting and whole-home automation',
        'starting_price': '£8,000',
        'price_range': '£20,000+ for whole-home with blackout fabrics',
        'example': 'Penthouse in Cardiff Bay - 18 motorized blinds with sun-tracking automation, blackout for cinema room, dawn simulation in bedrooms',
        'approach': 'We integrate with lighting scenes (movie mode = blinds close + lights dim), sunrise wake-up routines, energy savings in summer heat.',
        'faqs': [
            ('Battery vs mains powered - which is better?', 'Battery: easier retrofit, no wiring. Mains: never needs charging, faster motors. New builds get mains, retrofits often battery.'),
            ('Can they open/close on schedule?', 'Yes - sunrise/sunset automation, or fixed times. Also manual control via app, remote, or voice.'),
            ('What about sun tracking?', 'Advanced: blinds close when direct sun hits windows, open when it passes. Keeps rooms cool, reduces AC costs.'),
            ('How long do motors last?', '10-15 years typical. Lutron/Somfy have best reliability. We provide 2-year warranty, motors have 5-year manufacturer warranty.'),
        ]
    },
    'security-cctv': {
        'title': 'Security & CCTV Systems',
        'subtitle': 'Professional Protection for High-Value Properties',
        'who_needs': 'All properties, especially remote/high-value homes, rental properties, estates, properties with previous break-ins',
        'tech': 'Hikvision/Axis 4K AI cameras, Control4/Loxone integration, Yale/Paxton smart locks, monitored alarm systems',
        'starting_price': '£4,000',
        'price_range': '£15,000+ for full perimeter with AI detection and smart home integration',
        'example': 'Rural property near Bridgend - 12 AI cameras with person/vehicle detection, alerts to phone, integrated with lighting (lights flash on intrusion)',
        'approach': 'AI detection reduces false alarms (ignores cats/rain), integration with smart home (auto-arm when you leave), remote viewing, optional 24/7 monitoring.',
        'faqs': [
            ('Wired vs WiFi cameras - which is better?', 'Wired (PoE) is more reliable, can\'t be jammed, no battery changes. WiFi works for hard-to-reach spots. We prefer wired for main system.'),
            ('How long is footage stored?', '30 days typical on local NVR. Cloud backup available. 4K cameras use ~1TB per camera per month.'),
            ('Can it integrate with smart home?', 'Yes - arm/disarm based on location, flash lights when motion detected, get alerts on TV/phone, unlock door for deliveries via camera.'),
            ('What about facial recognition?', 'Available but has privacy concerns. We do person/vehicle detection (alerts you to humans vs cats) without storing faces.'),
        ]
    },
    'electrical-installation': {
        'title': 'Electrical Installation & Pre-Wire',
        'subtitle': 'NICEIC Certified Electricians for Smart Home Projects',
        'who_needs': 'New builds needing pre-wire, renovations adding smart systems, homes needing proper circuits/containment for automation',
        'tech': 'NICEIC certified in-house electricians, proper containment, surge protection, smart distribution boards, 18th Edition compliant',
        'starting_price': '£5,000',
        'price_range': '£15,000+ for full smart home electrical infrastructure',
        'example': 'New build in Gloucester - full pre-wire for smart home (data to every room, ceiling speaker cutouts, equipment closet setup, surge protection)',
        'approach': 'We\'re NICEIC certified, work with your builder\'s schedule, provide test certificates, install to 18th edition regs, coordinate AV/network/lighting trades.',
        'faqs': [
            ('Why do I need a specialist electrician for smart homes?', 'Standard sparkies don\'t understand low-voltage wiring, network cabling, or equipment rack layouts. We coordinate all trades.'),
            ('What\'s included in pre-wire?', 'CAT6 to every room, speaker wire to ceiling, conduit for future, equipment closet wiring, surge protection, labeled cables.'),
            ('Can you work with our existing electrician?', 'Yes - we provide plans, they do rough-in, we do low-voltage/final connections. Or we handle everything in-house.'),
            ('What certifications do you have?', 'NICEIC certified (electrical), CEDIA certified (AV), 18th Edition trained. Fully insured with £10M public liability.'),
        ]
    }
}

def rewrite_service_page(filename, data):
    """Rewrite a single service page with new content"""
    filepath = f'/home/ac311673555/ish-main/{filename}.html'

    if not os.path.exists(filepath):
        print(f"⚠️  File not found: {filepath}")
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update title
    content = re.sub(
        r'(<title>)[^<]+(</title>)',
        fr'\1{data["title"]} | Infinity Smart Home Systems - From {data["starting_price"]}\2',
        content
    )

    # Update meta description
    content = re.sub(
        r'(<meta name="description" content=")[^"]+"',
        fr'\1{data["who_needs"]}. {data["tech"]}. Starting from {data["starting_price"]}. Call 01443 123456"',
        content
    )

    # Add pricing section after features
    pricing_section = f'''
    <!-- Pricing & Details Section -->
    <section class="py-24 bg-white">
        <div class="container mx-auto px-6">
            <div class="max-w-5xl mx-auto">
                <div class="text-center mb-12" data-aos="fade-up">
                    <h2 class="text-4xl md:text-5xl font-semibold mb-6">Investment & Pricing</h2>
                    <p class="text-xl text-gray-600">Transparent pricing for {data["title"].lower()}</p>
                </div>

                <div class="grid md:grid-cols-2 gap-8 mb-12">
                    <div class="bg-[#F5F3EF] p-8 rounded-xl" data-aos="fade-up">
                        <div class="text-sm uppercase tracking-wider text-[#cbaf82] mb-2">Starting From</div>
                        <div class="text-5xl font-bold text-[#2C2C2C] mb-4">{data["starting_price"]}</div>
                        <p class="text-gray-600">Basic system installation</p>
                    </div>
                    <div class="bg-[#F5F3EF] p-8 rounded-xl" data-aos="fade-up" data-aos-delay="100">
                        <div class="text-sm uppercase tracking-wider text-[#cbaf82] mb-2">Full Systems</div>
                        <div class="text-3xl font-bold text-[#2C2C2C] mb-4">{data["price_range"]}</div>
                        <p class="text-gray-600">Complete professional installation</p>
                    </div>
                </div>

                <div class="bg-white border-2 border-[#cbaf82] rounded-xl p-8" data-aos="fade-up">
                    <h3 class="text-2xl font-semibold mb-4">Who Needs This?</h3>
                    <p class="text-gray-700 mb-6">{data["who_needs"]}</p>

                    <h3 class="text-2xl font-semibold mb-4 mt-8">Technology We Use</h3>
                    <p class="text-gray-700 mb-6">{data["tech"]}</p>

                    <h3 class="text-2xl font-semibold mb-4 mt-8">Real Example</h3>
                    <p class="text-gray-700 mb-6">{data["example"]}</p>

                    <h3 class="text-2xl font-semibold mb-4 mt-8">Our Approach</h3>
                    <p class="text-gray-700">{data["approach"]}</p>
                </div>
            </div>
        </div>
    </section>

    <!-- FAQ Section -->
    <section class="py-24 bg-[#F5F3EF]">
        <div class="container mx-auto px-6">
            <div class="max-w-4xl mx-auto">
                <div class="text-center mb-12" data-aos="fade-up">
                    <h2 class="text-4xl md:text-5xl font-semibold mb-6">Frequently Asked Questions</h2>
                    <p class="text-xl text-gray-600">Everything you need to know about {data["title"].lower()}</p>
                </div>

                <div class="space-y-6">
'''

    # Add FAQ items
    for i, (question, answer) in enumerate(data['faqs']):
        pricing_section += f'''                    <div class="bg-white p-6 rounded-xl shadow-sm" data-aos="fade-up" data-aos-delay="{i * 100}">
                        <h3 class="text-xl font-semibold mb-3 text-[#2C2C2C]">{question}</h3>
                        <p class="text-gray-700">{answer}</p>
                    </div>
'''

    pricing_section += '''                </div>

                <div class="text-center mt-12" data-aos="fade-up">
                    <p class="text-lg text-gray-700 mb-6">Have more questions? Let's talk about your project.</p>
                    <a href="tel:01443123456" class="btn-gold inline-block px-8 py-4 rounded-full text-lg">Call 01443 123456 - Speak to Tim</a>
                </div>
            </div>
        </div>
    </section>
'''

    # Insert pricing section before CTA section
    content = re.sub(
        r'(<!-- CTA Section -->)',
        pricing_section + r'\1',
        content
    )

    # Update CTA button to phone
    content = re.sub(
        r'(<a[^>]*href="[^"]*contact[^"]*"[^>]*class="[^"]*btn[^"]*"[^>]*>)[^<]+(</a>)',
        r'\1Call 01443 123456 - Get Started\2',
        content
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return True

def main():
    """Rewrite all 8 service pages"""
    print("🚀 Rewriting all 8 service pages...\n")

    for filename, data in SERVICE_DATA.items():
        print(f"📝 Rewriting {filename}.html...")
        if rewrite_service_page(filename, data):
            print(f"   ✅ {data['title']} complete")
        else:
            print(f"   ❌ Failed")

    print("\n✅ All service pages rewritten!")
    print("📊 Added: Pricing, Who Needs This, Tech Specs, Examples, FAQs")

if __name__ == '__main__':
    main()
