import json
import os

# 1. Load data
with open('master_manifest.json', 'r') as f:
    manifest = json.load(f)

with open('assets/i18n/en.json', 'r') as f:
    en_i18n = json.load(f)

# 2. Combine Products
master_products = {p['id']: p for p in manifest['products']}
for p in en_i18n['products']:
    if p['id'] not in master_products:
        master_products[p['id']] = p
        print(f"Added missing product from en.json: {p['id']}")

# 3. Enrichment Logic
b2b_suffix = " Wholesale factory supply, customizable for OEM/ODM. NSF/ISO certified for industrial and commercial water treatment."
name_map = {
    "PP Spun Sediment Filter": "PP Melt Blown Sediment Filter Cartridge",
    "Carbon Block Filter (Coconut Shell)": "CTO Coconut Shell Carbon Block Filter Cartridge",
    "UDF Granular Activated Carbon Filter": "GAC Granular Activated Carbon (UDF) Filter Cartridge",
    "RO Membrane Filter Cartridge": "Reverse Osmosis (RO) Membrane Element",
    "304 Stainless Steel Jumbo Filter Housing": "304/316L Stainless Steel Industrial Jumbo Filter Housing",
    "Industrial PP Filter (SOE/DOE)": "Industrial PP Melt Blown Sediment Filter (SOE/DOE)",
    "Industrial Carbon Block Filter": "Industrial High-Flow CTO Carbon Block Filter",
    "400GPD High Flow RO Membrane": "400GPD High-Flow Reverse Osmosis (RO) Membrane Element",
    "PP Sediment Filter": "PP Melt Blown Sediment Filter",
    "PP Filter": "PP Melt Blown Filter",
    "Carbon Block": "CTO Carbon Block",
}

for pid, p in master_products.items():
    # Refine Name
    for old, new in name_map.items():
        if old in p['name'] and new not in p['name']:
            p['name'] = p['name'].replace(old, new)
            break
    
    if p['category'] == "Filter Cartridge":
        if "PP" in p['name'] and "Melt Blown" not in p['name']:
            p['name'] = p['name'].replace("PP", "PP Melt Blown")
        if "Carbon Block" in p['name'] and "CTO" not in p['name']:
            p['name'] = p['name'].replace("Carbon Block", "CTO Carbon Block")

    # Enhance Description
    if b2b_suffix not in p['desc']:
        p['desc'] += b2b_suffix

# 4. Update Manifest
manifest['products'] = sorted(master_products.values(), key=lambda x: x['id'])
manifest['company']['tagline'] = "Leading China Water Filter Manufacturer | OEM/ODM Specialist"

with open('master_manifest.json', 'w') as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)

# 5. UI Updates
ui_updates = {
    "hero_eyebrow": "✦ Leading China Water Filter Manufacturer | NSF & ISO Certified Factory",
    "hero_title": "Industrial-Grade Water Purification & OEM Solutions",
    "hero_desc": "Global bulk wholesale supplier of high-performance PP Melt Blown, CTO, GAC filters, and RO membranes. Since 1998, we provide NSF/ISO certified OEM/ODM technical support for 50+ countries.",
    "about_feat_3": "NSF, ISO, CE, and Halal certified manufacturing center",
    "about_feat_4": "Professional OEM/ODM technical support for global brands",
    "footer_brand_desc": "Leading China manufacturer of water filtration solutions since 1998. Specialized in PP Melt Blown, CTO Carbon Block, GAC, and RO membranes for global bulk wholesale and OEM/ODM partners.",
    "topbar_tag": "Global Bulk Wholesale · OEM/ODM Specialist · Since 1998"
}

# 6. Propagate to i18n
i18n_dirs = ['assets/i18n', 'expresswater_v26_04_26_1700/assets/i18n']
product_list = manifest['products']

# Special logic for product specs in i18n
for d in i18n_dirs:
    if not os.path.exists(d): continue
    for f_name in os.listdir(d):
        if not f_name.endswith('.json'): continue
        path = os.path.join(d, f_name)
        with open(path, 'r') as f:
            data = json.load(f)
        
        # Update UI
        if 'ui' in data:
            for k, v in ui_updates.items():
                data['ui'][k] = v
        
        # Update Products (Full Sync)
        # We replace the product list entirely with the enriched one
        # to ensure all products are present and optimized.
        # For non-English languages, we'll keep it English as requested for "standard industrial terms"
        # and "B2B keyword enrichment".
        data['products'] = product_list
        
        with open(path, 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Super Sync completed. Manifest updated with {len(product_list)} products.")
