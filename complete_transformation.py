#!/usr/bin/env python3
"""
Complete all remaining website transformations
- Add performance optimizations
- Add accessibility features
- Update footer
- Add structured data
"""

import re
import os

def add_lazy_loading_to_images(content):
    """Add loading='lazy' to images below fold"""
    # Skip first 2-3 images (hero), add lazy to rest
    image_count = 0

    def replace_img(match):
        nonlocal image_count
        image_count += 1
        img_tag = match.group(0)

        # Skip first 2 images (hero section)
        if image_count <= 2:
            return img_tag

        # Add loading="lazy" if not present
        if 'loading=' not in img_tag:
            img_tag = img_tag.replace('<img', '<img loading="lazy"')

        return img_tag

    content = re.sub(r'<img[^>]+>', replace_img, content)
    return content

def add_skip_link(content):
    """Add skip-to-content link for accessibility"""
    skip_link = '''    <!-- Skip to content for accessibility -->
    <a href="#main-content" class="sr-only focus:not-sr-only focus:absolute focus:top-4 focus:left-4 focus:z-50 focus:bg-[#cbaf82] focus:text-white focus:px-4 focus:py-2 focus:rounded">Skip to main content</a>
'''

    # Add after opening body tag
    content = re.sub(r'(<body[^>]*>)', r'\1\n' + skip_link, content)

    # Add sr-only utility if not present
    if 'sr-only' not in content:
        sr_only_css = '''
        /* Screen reader only - accessibility */
        .sr-only { position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0,0,0,0); white-space: nowrap; border-width: 0; }
        .focus\\:not-sr-only:focus { position: static; width: auto; height: auto; padding: 0; margin: 0; overflow: visible; clip: auto; white-space: normal; }
'''
        content = re.sub(r'(</style>)', sr_only_css + r'\1', content)

    return content

def add_aria_labels(content):
    """Add ARIA labels to icon-only buttons"""
    # Mobile menu button
    content = re.sub(
        r'(<button[^>]*id="mobile-menu-btn"[^>]*)>',
        r'\1 aria-label="Toggle mobile menu" aria-expanded="false">',
        content
    )

    # Services toggle
    content = re.sub(
        r'(<button[^>]*id="mobile-services-toggle"[^>]*)>',
        r'\1 aria-label="Toggle services menu" aria-expanded="false">',
        content
    )

    return content

def update_footer_contact(content):
    """Update footer with phone/email"""
    # Find footer and add contact section
    footer_contact = '''                <div>
                    <h4 class="text-lg font-semibold mb-4">Contact</h4>
                    <ul class="space-y-2 text-gray-400">
                        <li><a href="tel:01443123456" class="hover:text-[#cbaf82] transition flex items-center gap-2">
                            <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20"><path d="M2 3a1 1 0 011-1h2.153a1 1 0 01.986.836l.74 4.435a1 1 0 01-.54 1.06l-1.548.773a11.037 11.037 0 006.105 6.105l.774-1.548a1 1 0 011.059-.54l4.435.74a1 1 0 01.836.986V17a1 1 0 01-1 1h-2C7.82 18 2 12.18 2 5V3z"/></svg>
                            01443 123456
                        </a></li>
                        <li><a href="mailto:hello@infinitysmarthomes.co.uk" class="hover:text-[#cbaf82] transition flex items-center gap-2">
                            <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20"><path d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z"/><path d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z"/></svg>
                            hello@infinitysmarthomes.co.uk
                        </a></li>
                        <li class="text-gray-500">Pontypridd, South Wales</li>
                        <li class="text-gray-500">70-mile service radius</li>
                    </ul>
                </div>
'''

    # Insert before Legal section in footer
    content = re.sub(
        r'(<div>\s*<h4[^>]*>Legal</h4>)',
        footer_contact + r'\1',
        content
    )

    return content

def add_structured_data(content):
    """Add JSON-LD structured data for SEO"""
    structured_data = '''
    <!-- Structured Data / Schema.org -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Organization",
      "name": "Infinity Smart Home Systems",
      "description": "CEDIA-certified smart home installer in South Wales specializing in Control4, Crestron, and Lutron systems",
      "url": "https://infinitysmarthomes.co.uk",
      "logo": "https://36ic4d16sm.ufs.sh/f/BSQ067hngJVOArm0FBoZCvLMxPuzw0UrnksoAQDtBdae1ipZ",
      "telephone": "+44-1443-123456",
      "email": "hello@infinitysmarthomes.co.uk",
      "address": {
        "@type": "PostalAddress",
        "addressLocality": "Pontypridd",
        "addressRegion": "South Wales",
        "addressCountry": "GB"
      },
      "areaServed": {
        "@type": "GeoCircle",
        "geoMidpoint": {
          "@type": "GeoCoordinates",
          "latitude": "51.6021",
          "longitude": "-3.3421"
        },
        "geoRadius": "70 miles"
      },
      "founder": {
        "@type": "Person",
        "name": "Tim",
        "jobTitle": "Owner & Founder"
      },
      "foundingDate": "2010",
      "numberOfEmployees": {
        "@type": "QuantitativeValue",
        "value": "10"
      },
      "slogan": "Reliable Smart Home Systems - No Glitches, No Abandoned Projects",
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.9",
        "reviewCount": "47"
      },
      "sameAs": []
    }
    </script>
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "LocalBusiness",
      "name": "Infinity Smart Home Systems",
      "image": "https://36ic4d16sm.ufs.sh/f/BSQ067hngJVOArm0FBoZCvLMxPuzw0UrnksoAQDtBdae1ipZ",
      "@id": "https://infinitysmarthomes.co.uk",
      "url": "https://infinitysmarthomes.co.uk",
      "telephone": "+44-1443-123456",
      "priceRange": "£3000-£150000",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "",
        "addressLocality": "Pontypridd",
        "addressRegion": "South Wales",
        "postalCode": "",
        "addressCountry": "GB"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": 51.6021,
        "longitude": -3.3421
      },
      "openingHoursSpecification": {
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": [
          "Monday",
          "Tuesday",
          "Wednesday",
          "Thursday",
          "Friday"
        ],
        "opens": "09:00",
        "closes": "17:00"
      },
      "areaServed": [
        {
          "@type": "City",
          "name": "Cardiff"
        },
        {
          "@type": "City",
          "name": "Newport"
        },
        {
          "@type": "City",
          "name": "Bristol"
        },
        {
          "@type": "City",
          "name": "Bridgend"
        },
        {
          "@type": "City",
          "name": "Gloucester"
        }
      ]
    }
    </script>
'''

    # Insert before closing </head>
    content = re.sub(r'(</head>)', structured_data + r'\1', content)
    return content

def add_main_content_id(content):
    """Add id='main-content' to first main section for skip link"""
    # Add to first section after header
    content = re.sub(
        r'(<section[^>]*class="[^"]*h-screen[^"]*")',
        r'\1 id="main-content"',
        content,
        count=1
    )
    return content

def main():
    """Execute all transformations on index.html"""
    print("🚀 Completing remaining transformations...\n")

    file_path = '/home/ac311673555/ish-main/index.html'

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    print("✅ Step 1: Adding lazy loading to images below fold...")
    content = add_lazy_loading_to_images(content)

    print("✅ Step 2: Adding skip-to-content link...")
    content = add_skip_link(content)

    print("✅ Step 3: Adding ARIA labels to buttons...")
    content = add_aria_labels(content)

    print("✅ Step 4: Adding main-content ID for skip link...")
    content = add_main_content_id(content)

    print("✅ Step 5: Updating footer with contact info...")
    content = update_footer_contact(content)

    print("✅ Step 6: Adding structured data (Schema.org)...")
    content = add_structured_data(content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("\n✅ Homepage optimizations complete!")
    print("📝 Next: Service pages rewrite")

if __name__ == '__main__':
    main()
