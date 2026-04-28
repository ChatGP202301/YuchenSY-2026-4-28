const fs = require('fs');
const content = fs.readFileSync('/Users/jet/.accio/accounts/1661502182/agents/DID-F456DA-2B0D4C/project/expresswater-v7-final/index.html', 'utf8');

const startTag = 'function siteData() {';
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

const functionPart = content.substring(startIndex, endIndex + 1);

try {
    // We try to evaluate the function definition
    eval('(' + functionPart + ')');
    console.log("SUCCESS: siteData function is valid JS");
} catch (e) {
    console.log("SYNTAX ERROR in siteData function:");
    console.log(e.message);
}
