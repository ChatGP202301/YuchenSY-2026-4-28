import json
import os

# Load the source of truth
with open('master_manifest.json', 'r') as f:
    manifest = json.load(f)

product_source = {p['id']: p for p in manifest['products']}

ui_updates = {
    "hero_eyebrow": "✦ Leading China Water Filter Manufacturer | NSF & ISO Certified Factory",
    "hero_title": "Industrial-Grade Water Purification & OEM Solutions",
    "hero_desc": "Global bulk wholesale supplier of high-performance PP Melt Blown, CTO, GAC filters, and RO membranes. Since 1998, we provide NSF/ISO certified OEM/ODM technical support for 50+ countries.",
    "about_feat_3": "NSF, ISO, CE, and Halal certified manufacturing center",
    "about_feat_4": "Professional OEM/ODM technical support for global brands",
    "footer_brand_desc": "Leading China manufacturer of water filtration solutions since 1998. Specialized in PP Melt Blown, CTO Carbon Block, GAC, and RO membranes for global bulk wholesale and OEM/ODM partners.",
    "topbar_tag": "Global Bulk Wholesale · OEM/ODM Specialist · Since 1998"
}

i18n_dirs = ['assets/i18n', 'expresswater_v26_04_26_1700/assets/i18n']

for i18n_dir in i18n_dirs:
    if not os.path.exists(i18n_dir):
        continue
    langs = [f for f in os.listdir(i18n_dir) if f.endswith('.json')]
    print(f"Processing directory: {i18n_dir}")
    for lang_file in langs:
        path = os.path.join(i18n_dir, lang_file)
        with open(path, 'r') as f:
            data = json.load(f)
        
        # 1. Update UI Strings
        if 'ui' in data:
            for key, val in ui_updates.items():
                data['ui'][key] = val
        
        # 2. Update Products
        if 'products' in data:
            new_products = []
            for p in data['products']:
                pid = p['id']
                if pid in product_source:
                    src = product_source[pid]
                    p['name'] = src['name']
                    p['desc'] = src['desc']
                    p['specs'] = src['specs']
                new_products.append(p)
            data['products'] = new_products
        
        with open(path, 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Propagated updates to {len(langs)} language files.")
