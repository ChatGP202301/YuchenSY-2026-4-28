import json
import re

file_path = 'expresswater-v7-final/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Try to find languages: { ... }
# We use a non-greedy search but since it's nested we might need to balance braces or find a marker
start_marker = 'languages: {'
start_index = content.find(start_marker)
if start_index == -1:
    print("Could not find languages marker")
    exit(1)

# Extract from start_index + len('languages: ')
# We will find the end by looking for the closing } of the siteData return object or similar
# Actually, let's find the products array too.
products_marker = 'products: ['
p_start = content.find(products_marker)

# SiteData structure:
# function siteData() {
#   return {
#     ...
#     products: [...],
#     languages: {...}
#   }
# }

# Let's extract everything inside the return { ... }
return_marker = 'return {'
r_start = content.find(return_marker, content.find('function siteData()'))
# Find the matching closing brace for return {
brace_count = 0
r_end = -1
for i in range(r_start + 7, len(content)):
    if content[i] == '{':
        brace_count += 1
    elif content[i] == '}':
        if brace_count == 0:
            r_end = i + 1
            break
        else:
            brace_count -= 1

if r_end == -1:
    print("Could not find end of return object")
    exit(1)

data_str = content[r_start:r_end]
# This string contains products: [...], languages: {...}
# It's not valid JSON because of keys without quotes and potential trailing commas.
# We'll save it as a JS file and use node to export it to JSON.

with open('raw_data.js', 'w', encoding='utf-8') as f:
    f.write("console.log(JSON.stringify(" + data_str.replace('return ', '') + "))")
