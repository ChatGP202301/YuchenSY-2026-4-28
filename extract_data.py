
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract products array
products_match = re.search(r'products:\s*\[(.*?)\],', content, re.DOTALL)
if products_match:
    products_str = products_match.group(1).strip()
    with open('extracted_products.txt', 'w', encoding='utf-8') as f:
        f.write(products_str)
else:
    print("Products not found")

# Extract languages dictionary
# This is trickier because of nested braces.
# We know it starts with "languages: {" and ends before "t(key) {"
lang_start = content.find('languages: {')
if lang_start != -1:
    # Find the end by counting braces
    bracket_count = 0
    lang_end = -1
    for i in range(lang_start + len('languages: {') - 1, len(content)):
        if content[i] == '{':
            bracket_count += 1
        elif content[i] == '}':
            bracket_count -= 1
            if bracket_count == 0:
                lang_end = i + 1
                break
    
    if lang_end != -1:
        lang_str = content[lang_start:lang_end]
        # We want the content inside "languages: { ... }"
        # No, we want "languages: { ... },"
        with open('extracted_languages.txt', 'w', encoding='utf-8') as f:
            f.write(lang_str)
    else:
        print("Languages end not found")
else:
    print("Languages start not found")
