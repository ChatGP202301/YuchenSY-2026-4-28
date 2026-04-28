const fs = require('fs');
const html = fs.readFileSync('page.html', 'utf8');

const islandRegex = /<astro-island[^>]+props="([^"]+)"/g;
let match;
while ((match = islandRegex.exec(html)) !== null) {
    let propsStr = match[1];
    propsStr = propsStr.replace(/&quot;/g, '"').replace(/&amp;/g, '&').replace(/&#39;/g, "'");
    
    try {
        const props = JSON.parse(propsStr);
        if (props.pageData && props.pageData[1] && props.pageData[1].elements) {
            const elements = props.pageData[1].elements[1];
            // Iterate through all keys in elements to find images and text
            console.log("Exploring elements...");
            for (const [key, value] of Object.entries(elements)) {
                // value is usually an array [version, data]
                const data = value[1];
                if (data.content && data.content[1]) {
                    const content = data.content[1];
                    if (content.includes("MT-900G")) {
                        console.log(`Key ${key} contains MT-900G`);
                    }
                    if (content.includes("MT-V-E300A")) {
                        console.log(`Key ${key} contains MT-V-E300A`);
                    }
                }
                if (data.imagePath && data.imagePath[1]) {
                    console.log(`Key ${key} is an image: ${data.imagePath[1]}`);
                }
            }
        }
    } catch (e) {}
}
