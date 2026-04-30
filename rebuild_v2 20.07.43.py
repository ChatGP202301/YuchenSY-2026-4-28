import os

js_path = "/Users/jet/.accio/accounts/1661502182/agents/DID-F456DA-2B0D4C/project/assets 15.45.13/languages.js"
with open(js_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the start of English products
start_marker = 'window.LANGUAGES_DATA.en = {'
start_idx = content.find(start_marker)
if start_idx != -1:
    products_marker = 'products: ['
    prod_start = content.find(products_marker, start_idx)
    if prod_start != -1:
        # Find the closing bracket of the products array
        # We look for the '],' that follows the array
        prod_end = content.find('],', prod_start)
        if prod_end != -1:
            products_block = content[prod_start:prod_end+1]
            # Count the number of products by looking for "id:"
            count = products_block.count('id:')
            print(f"Total Products Found in EN section: {count}")
