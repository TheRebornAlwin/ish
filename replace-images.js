const fs = require('fs');

// Read index.html
let content = fs.readFileSync('index.html', 'utf8');

// 1. First card in Features section - "Everything concealed"
content = content.replace(
    /photo-1558618666-fcd25c85cd64\?q=80&w=800/g,
    '36ic4d16sm.ufs.sh/f/BSQ067hngJVOL35YxZOXdi03bFNVhYyUPOr1lJ7kIvMAEKHt'
);

// 2. "One Tap, Everything Responds" - second card
content = content.replace(
    /photo-1556912173-46c336c7fd55\?q=80&w=800/g,
    '36ic4d16sm.ufs.sh/f/BSQ067hngJVO77zY4hmVU1kR5np8h3MbP6F9WYtLHX4QayIj'
);

// 3. "Voice, Touch, or Phone" - third card
content = content.replace(
    /photo-1600210492486-724fe5c67fb0\?q=80&w=800/g,
    '36ic4d16sm.ufs.sh/f/BSQ067hngJVOgWwTwdnZQ48UycnJiKEWxDOAkphSMNw3F1PV'
);

// 4. Cardiff Bay Penthouse Cinema
content = content.replace(
    /photo-1489599849927-2ee91cede3ba\?w=800&h=600&fit=crop/g,
    '36ic4d16sm.ufs.sh/f/BSQ067hngJVOJ5cILY4MoOrZU0tLBj8pxGX9uKd3lFAbPgEJ'
);

// 5. Newport Retrofit
content = content.replace(
    /photo-1558618666-fcd25c85cd64\?w=800&h=600&fit=crop/g,
    '36ic4d16sm.ufs.sh/f/BSQ067hngJVOol72SEFqNVSDayJbHCELw5mGdfOsXlkcx4ui'
);

// 6. Built on 15 Years section image
// Find the about section image
content = content.replace(
    /https:\/\/images\.unsplash\.com\/photo-1600566753376-12c8ab7fb75b\?w=800&fit=crop/g,
    'https://36ic4d16sm.ufs.sh/f/BSQ067hngJVOEY5LihpIStAwm1jioMlaJY8G4E9vdQDnpqzO'
);

fs.writeFileSync('index.html', content, 'utf8');
console.log('✅ All images replaced successfully!');
