const fs = require('fs');
const html = fs.readFileSync('page.html', 'utf8');

// Find all props attributes in astro-island tags
const islandRegex = /<astro-island[^>]+props="([^"]+)"/g;
let match;
while ((match = islandRegex.exec(html)) !== null) {
    let propsStr = match[1];
    // Unescape HTML entities
    propsStr = propsStr.replace(/&quot;/g, '"').replace(/&amp;/g, '&').replace(/&#39;/g, "'");
    
    try {
        const props = JSON.parse(propsStr);
        // Look for content in the props
        // Zyro props usually have a "page" or "blocks" structure
        console.log("Found props block");
        // Deep search for "MT-900G"
        const findText = (obj, path = "") => {
            if (typeof obj === 'string') {
                if (obj.includes("MT-900G") || obj.includes("MT-V-E300A")) {
                    console.log(`Found text at ${path}: ${obj}`);
                }
            } else if (Array.isArray(obj)) {
                obj.forEach((item, i) => findText(item, `${path}[${i}]`));
            } else if (typeof obj === 'object' && obj !== null) {
                Object.entries(obj).forEach(([key, value]) => findText(value, `${path}.${key}`));
            }
        };
        findText(props);
        
        // Find image paths in the same structure
        const findImages = (obj, path = "") => {
            if (typeof obj === 'string' && (obj.endsWith('.png') || obj.endsWith('.jpg') || obj.endsWith('.jpeg'))) {
                console.log(`Found image at ${path}: ${obj}`);
            } else if (Array.isArray(obj)) {
                obj.forEach((item, i) => findImages(item, `${path}[${i}]`));
            } else if (typeof obj === 'object' && obj !== null) {
                Object.entries(obj).forEach(([key, value]) => findImages(value, `${path}.${key}`));
            }
        };
        // findImages(props);
    } catch (e) {
        // console.error("Failed to parse props", e);
    }
}
