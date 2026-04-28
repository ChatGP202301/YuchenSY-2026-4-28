import re

path = '/Users/jet/.accio/accounts/1661502182/agents/DID-F456DA-2B0D4C/project/expresswater-v7-final/index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern: end of a language block followed by start of another
# e.g., } \s* [a-z]{2}: {
# We want to replace it with }, \n [a-z]{2}: {

def fix_commas(match):
    return '},\n    ' + match.group(1)

# Regex to find language starts that are missing a preceding comma
# We look for a closing brace followed by a key like 'id: {' or 'th: {'
# but without a comma in between.
new_content = re.sub(r'\}\s*([a-z]{2,3}:\s*\{)', fix_commas, content)

# Check if we accidentally created double commas
new_content = new_content.replace('},,', '},')

with open(path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Fix applied.")
