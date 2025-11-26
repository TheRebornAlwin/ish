#!/usr/bin/env python3
"""Fix horizontal scroll overflow issues on mobile and tablet viewports"""

import re

files_to_update = [
    'index.html',
    'smart-home-design.html',
    'home-theatre.html',
    'wifi-networking.html',
    'multi-room-audio.html',
    'video-distribution.html',
    'smart-shading.html',
    'security-cctv.html',
    'electrical-installation.html'
]

# CSS overflow fix to add before closing </style> tag
overflow_fix_css = '''
        /* Overflow fix applied */
        * { box-sizing: border-box; }
        html, body { overflow-x: hidden; max-width: 100vw; }
        .container { max-width: 100%; padding-left: 1.5rem; padding-right: 1.5rem; }

        /* Fix dropdown menu overflow on mobile */
        @media (max-width: 768px) {
            .services-dropdown-menu {
                width: 240px !important;
                left: auto !important;
                right: 0 !important;
                transform: none !important;
            }
        }

        /* Ensure all sections respect viewport width */
        section { max-width: 100vw; overflow-x: hidden; }

        /* Fix grid layouts on mobile and tablet */
        @media (max-width: 768px) {
            .grid { overflow-x: hidden; width: 100%; }
            .max-w-7xl, .max-w-6xl, .max-w-5xl, .max-w-4xl { max-width: 100%; padding-left: 0; padding-right: 0; }
        }
'''

for filename in files_to_update:
    filepath = f'/home/ac311673555/ish-main/{filename}'

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Skip if already fixed
        if '/* Overflow fix applied */' in content:
            print(f'⏭️  Skipped {filename} - already fixed')
            continue

        # Find the last CSS rule before </style> and add overflow fix
        # Look for the services-dropdown-menu a:hover rule
        pattern = r'(\.services-dropdown-menu a:hover[^}]+})\s*(</style>)'

        if re.search(pattern, content):
            content = re.sub(pattern, r'\1' + overflow_fix_css + r'\2', content, count=1)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            print(f'✅ Fixed {filename}')
        else:
            print(f'⚠️  Could not find style section in {filename}')

    except Exception as e:
        print(f'❌ Error updating {filename}: {e}')

print('\n✅ Horizontal scroll fixes applied!')
