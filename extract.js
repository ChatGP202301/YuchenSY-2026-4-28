const fs = require('fs');
const html = fs.readFileSync('page.html', 'utf8');

// Find all image URLs and their associated text
const imgRegex = /<img[^>]+src="([^">]+)"/g;
const modelRegexes = {
    'MT-900G': /MT-900G/i,
    'MT-V-E300A': /MT-V-E300A/i
};

// Basic approach: Find all images and check the text around them
// Since this is a static site, images and text are often in the same container.
// We can split the HTML by common block elements or just look for the text.

const results = {};

for (const [model, regex] of Object.entries(modelRegexes)) {
    const index = html.indexOf(model);
    if (index !== -1) {
        // Look for the closest image before or after this text
        // This is a bit naive but can work for simple layouts.
        const fragment = html.substring(Math.max(0, index - 2000), Math.min(html.length, index + 2000));
        const matches = [...fragment.matchAll(/<img[^>]+src="([^">]+)"/g)];
        if (matches.length > 0) {
            results[model] = matches.map(m => m[1]);
        }
    }
}

// Also list all images
const allImages = [...html.matchAll(/<img[^>]+src="([^">]+)"/g)].map(m => m[1]);

console.log(JSON.stringify({ results, allImages }, null, 2));
