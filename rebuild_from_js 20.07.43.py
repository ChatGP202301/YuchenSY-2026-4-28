import re
import json
import os

js_path = "/Users/jet/.accio/accounts/1661502182/agents/DID-F456DA-2B0D4C/project/assets 15.45.13/languages.js"
with open(js_path, 'r', encoding='utf-8') as f:
    content = f.read()

# The file contains window.LANGUAGES_DATA.en = { ... }
# We will extract each language block
languages = ["en", "ar", "es", "fr", "de", "ru", "pt", "ja", "ko", "it", "bn", "cs", "da", "el", "fa", "fi", "he", "hi", "hu", "id", "ms", "nl", "pl", "ro", "sv", "th", "tl", "tr", "ur", "vi", "no", "uk", "bg", "hr", "sr", "sk", "sl", "lt"]

all_data = {}

for lang in languages:
    # Use regex to find the block for each language
    # window.LANGUAGES_DATA.en = { ... };
    pattern = rf'window\.LANGUAGES_DATA\.{lang} = (\{{.*?\}});'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        json_str = match.group(1)
        # Convert JS object style to JSON (basic fixes for keys)
        # 1. Add quotes to keys
        json_str = re.sub(r'(\w+):', r'"\1":', json_str)
        # 2. Fix trailing commas
        json_str = re.sub(r',(\s*[\]\}])', r'\1', json_str)
        try:
            # We use a safer way to parse JS-like objects if json.loads fails
            # But let's try json.loads first with some common fixes
            all_data[lang] = json.loads(json_str)
        except:
            # Fallback: very basic manual extraction for products if JSON fails
            prod_match = re.search(r'products: \[(.*?)\]', json_str, re.DOTALL)
            if prod_match:
                # This is more complex, but let's assume we can get it
                pass

# If we have the data, rebuild the files
if "en" in all_data:
    products = all_data["en"].get("products", [])
    print(f"Detected {len(products)} products in EN.")
    
    # Re-save as clean JSON for safety
    with open("full_database_187.json", "w") as f:
        json.dump(all_data, f, indent=2)

