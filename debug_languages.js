const fs = require('fs');
const content = fs.readFileSync('/Users/jet/.accio/accounts/1661502182/agents/DID-F456DA-2B0D4C/project/expresswater-v7-final/index.html', 'utf8');

const startTag = 'languages: {';
const startIndex = content.indexOf(startTag);
if (startIndex === -1) {
    console.log("Could not find start tag");
    process.exit(1);
}

// Find the matching brace
let braceCount = 1;
let endIndex = -1;
for (let i = startIndex + startTag.length; i < content.length; i++) {
    if (content[i] === '{') braceCount++;
    if (content[i] === '}') braceCount--;
    if (braceCount === 0) {
        endIndex = i;
        break;
    }
}

if (endIndex === -1) {
    console.log("Could not find matching brace");
    process.exit(1);
}

const languagesPart = content.substring(startIndex + startTag.length - 1, endIndex + 1);

try {
    // We wrap it in an object and try to evaluate it
    const obj = eval('(' + languagesPart + ')');
    console.log("SUCCESS: Languages object is valid JS");
    console.log("Number of languages:", Object.keys(obj).length);
} catch (e) {
    console.log("SYNTAX ERROR in languages object:");
    console.log(e.message);
    // Try to find the position
    if (e.stack) {
        console.log(e.stack);
    }
}
