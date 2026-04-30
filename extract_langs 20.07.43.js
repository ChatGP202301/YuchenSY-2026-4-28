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

const languagesPart = content.substring(startIndex + startTag.length - 1, endIndex + 1);
// The object might have keys without quotes, so we need a safer way to parse or just evaluate
const languages = eval('(' + languagesPart + ')');

// Extract specific languages
const targets = ['tr', 'hi', 'bn', 'id', 'vi', 'th', 'pl', 'nl', 'fa', 'ur'];
const result = {};
const allLangs = {};

for (const lang in languages) {
    allLangs[lang] = languages[lang].name;
    if (targets.includes(lang)) {
        result[lang] = languages[lang];
    }
}

fs.writeFileSync('extracted_langs.json', JSON.stringify({targets: result, allLangs: allLangs}, null, 2));
console.log("Extracted " + Object.keys(result).length + " target languages.");
console.log("Total languages found: " + Object.keys(languages).length);
