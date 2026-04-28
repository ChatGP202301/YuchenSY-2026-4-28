import json

with open('master_manifest.json', 'r') as f:
    manifest = json.load(f)

# 1. Update Company
manifest['company']['tagline'] = "Leading China Water Filter Manufacturer | OEM/ODM Specialist"

# 2. Enrich Products
b2b_suffix = " Wholesale factory supply, customizable for OEM/ODM. NSF/ISO certified for industrial and commercial water treatment."

name_map = {
    "PP Spun Sediment Filter": "PP Melt Blown Sediment Filter Cartridge",
    "Carbon Block Filter (Coconut Shell)": "CTO Coconut Shell Carbon Block Filter Cartridge",
    "UDF Granular Activated Carbon Filter": "GAC Granular Activated Carbon (UDF) Filter Cartridge",
    "RO Membrane Filter Cartridge": "Reverse Osmosis (RO) Membrane Element Element",
    "304 Stainless Steel Jumbo Filter Housing": "304/316L Stainless Steel Industrial Jumbo Filter Housing",
    "Industrial PP Filter (SOE/DOE)": "Industrial PP Melt Blown Sediment Filter (SOE/DOE)",
    "Industrial Carbon Block Filter": "Industrial High-Flow CTO Carbon Block Filter",
    "400GPD High Flow RO Membrane": "400GPD High-Flow Reverse Osmosis (RO) Membrane Element",
    "PP Sediment Filter": "PP Melt Blown Sediment Filter",
    "PP Filter": "PP Melt Blown Filter",
    "Carbon Block": "CTO Carbon Block",
}

for p in manifest['products']:
    # Refine Name
    for old, new in name_map.items():
        if old in p['name'] and new not in p['name']:
            p['name'] = p['name'].replace(old, new)
            break
    
    # Refine Category specific names
    if p['category'] == "Filter Cartridge":
        if "PP" in p['name'] and "Melt Blown" not in p['name']:
            p['name'] = p['name'].replace("PP", "PP Melt Blown")
        if "Carbon Block" in p['name'] and "CTO" not in p['name']:
            p['name'] = p['name'].replace("Carbon Block", "CTO Carbon Block")

    # Enhance Description
    if b2b_suffix not in p['desc']:
        p['desc'] += b2b_suffix

with open('master_manifest.json', 'w') as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)

print("Updated master_manifest.json")
