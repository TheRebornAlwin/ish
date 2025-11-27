#!/usr/bin/env python3
import re

# Read index.html to extract header and footer
with open('/home/ac311673555/ish-main/index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract header (from <header to </header>)
header_match = re.search(r'(<header.*?</header>)', index_content, re.DOTALL)
header = header_match.group(1) if header_match else None

# Extract footer (from <footer to </footer>)
footer_match = re.search(r'(<footer.*?</footer>)', index_content, re.DOTALL)
footer = footer_match.group(1) if footer_match else None

if not header or not footer:
    print("ERROR: Could not extract header/footer")
    exit(1)

# Service pages
service_pages = [
    'home-theatre.html',
    'wifi-networking.html',
    'multi-room-audio.html',
    'video-distribution.html',
    'security-cctv.html',
    'electrical-installation.html',
    'smart-shading.html',
    'smart-home-design.html'
]

for page in service_pages:
    filepath = f'/home/ac311673555/ish-main/{page}'
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace header
        content = re.sub(r'<header.*?</header>', header, content, flags=re.DOTALL)
        
        # Replace footer
        content = re.sub(r'<footer.*?</footer>', footer, content, flags=re.DOTALL)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Updated {page}")
    except Exception as e:
        print(f"✗ Error with {page}: {e}")

print("\n✅ All service pages synced")
