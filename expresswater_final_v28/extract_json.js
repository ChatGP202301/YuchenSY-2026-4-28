
const fs = require('fs');

const content = fs.readFileSync('index.html', 'utf8');

// Extract products
// We know it starts at line 506 and ends before line 547
const lines = content.split('\n');
const productsLines = lines.slice(505, 546); // 506 is index 505
const productsRaw = productsLines.join('\n');
const productsArray = eval('[' + productsRaw + ']');
fs.writeFileSync('products.json', JSON.stringify(productsArray, null, 2));
console.log('Saved products.json');

// Extract languages
// Starts at line 547 (index 546)
// Ends at line 3831 (index 3830)
const languagesLines = lines.slice(546, 3831);
let languagesRaw = languagesLines.join('\n');
// Remove the "languages: " prefix from the first line if present
languagesRaw = languagesRaw.replace(/^\s*languages:\s*/, '').trim();
// Remove trailing comma if it exists
if (languagesRaw.endsWith(',')) {
    languagesRaw = languagesRaw.slice(0, -1);
}
const languagesObject = eval('(' + languagesRaw + ')');
fs.writeFileSync('languages.json', JSON.stringify(languagesObject, null, 2));
console.log('Saved languages.json');

// Verify counts
console.log('Products count:', productsArray.length);
console.log('Languages count:', Object.keys(languagesObject).length);
