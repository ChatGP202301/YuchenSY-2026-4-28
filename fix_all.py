import re

path = '/Users/jet/.accio/accounts/1661502182/agents/DID-F456DA-2B0D4C/project/expresswater-v7-final/index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

langs = ['en', 'zh', 'ru', 'es', 'ja', 'fr', 'ar', 'it', 'nl', 'pl', 'pt', 'tr', 'sv', 'el', 'cs', 'hu', 'da', 'no', 'fi', 'ro', 'sr', 'kk', 'uz', 'id', 'th', 'vi', 'my', 'km', 'ne', 'az', 'ka', 'hy', 'prs', 'fa', 'ps', 'et', 'lv', 'lt', 'sl', 'sk', 'mt', 'is', 'ti', 'so', 'ht', 'sw', 'zu', 'af', 'ha', 'yo', 'ig', 'wo', 'am', 'tn', 'rw']

for lang in langs:
    # Pattern: } followed by optional whitespace, then lang: {
    # Replace with },\n    lang: {
    pattern = r'\}\s*(' + lang + r':\s*\{)'
    content = re.sub(pattern, r'},\n    \1', content)

# Clean up double commas
content = content.replace('},,', '},')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Replacement done.")
