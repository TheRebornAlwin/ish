#!/usr/bin/env python3
import re

# Read index.html
with open('/home/ac311673555/ish-main/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: Center modal content and add styling
content = re.sub(
    r'<h2 class="text-3xl font-semibold mb-2 text-\[#2C2C2C\]">Get Started</h2>',
    '<h2 class="text-3xl font-semibold mb-2 text-[#2C2C2C] text-center">Get Started</h2>',
    content
)
content = re.sub(
    r'<p class="text-gray-600 mb-2">We\'ll reply within 24 hours</p>',
    '<p class="text-gray-600 mb-2 text-center">We\'ll reply within 24 hours</p>',
    content
)
content = re.sub(
    r'<p class="text-sm text-gray-500 mb-6">Don\'t want to wait\? <a href="tel:01443123456" class="text-\[#cbaf82\] hover:underline font-semibold">Call us now</a></p>',
    '<p class="text-sm text-gray-500 mb-6 text-center">Don\'t want to wait? <a href="tel:01443123456" class="text-[#cbaf82] hover:underline font-semibold">Call us now</a></p>',
    content
)

# Fix 2: Add black footer to modal
content = re.sub(
    r'<p class="text-center text-sm text-gray-500 mt-4">\s*Or, email us: <a href="mailto:hello@infinitysmarthomes\.co\.uk" class="text-\[#cbaf82\] hover:underline">hello@infinitysmarthomes\.co\.uk</a>\s*</p>',
    '<div class="mt-6 pt-6 border-t border-gray-200 bg-[#2C2C2C] -mx-8 -mb-8 px-8 py-4 rounded-b-2xl"><p class="text-center text-sm text-gray-400">Or, email us: <a href="mailto:hello@infinitysmarthomes.co.uk" class="text-[#cbaf82] hover:underline">hello@infinitysmarthomes.co.uk</a></p></div>',
    content
)

# Write back
with open('/home/ac311673555/ish-main/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed modal centering and footer")
