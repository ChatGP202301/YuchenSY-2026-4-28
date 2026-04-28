const fs = require('fs');
const html = fs.readFileSync('page.html', 'utf8');

const islandRegex = /<astro-island[^>]+props="([^"]+)"/g;
let match;
while ((match = islandRegex.exec(html)) !== null) {
    let propsStr = match[1];
    propsStr = propsStr.replace(/&quot;/g, '"').replace(/&amp;/g, '&').replace(/&#39;/g, "'");
    
    try {
        const props = JSON.parse(propsStr);
        if (props.pageData) {
            console.log("Searching pageData...");
            const findPairs = (obj) => {
                if (typeof obj === 'object' && obj !== null) {
                    for (const key in obj) {
                        const val = obj[key];
                        if (val && val[1]) {
                            if (val[1].imagePath) {
                                console.log(`Found image: ${val[1].imagePath[1]} near key ${key}`);
                            }
                            if (val[1].content) {
                                console.log(`Found content: ${val[1].content[1].substring(0, 100)} near key ${key}`);
                            }
                        }
                        findPairs(val);
                    }
                }
            };
            findPairs(props.pageData);
        }
    } catch (e) {}
}
