
import re

with open('index.html', 'r') as f:
    content = f.read()

# Try to find something that looks like the products array
# Since we see { id: 1, ... } starting at line 506
# and languages: { starting at line 547
products_segment = content[content.find('{ id: 1,'):content.find('languages:')]
print(f"Products segment length: {len(products_segment)}")
print(f"First 100 chars: {products_segment[:100]}")
print(f"Last 100 chars: {products_segment[-100:]}")

# Try to find languages
languages_match = re.search(r'languages:\s*({[\s\S]*?})\s*,\s*init', content)
if languages_match:
    languages_str = languages_match.group(1)
    print(f"Languages length: {len(languages_str)}")
else:
    print("Languages not found with regex")
