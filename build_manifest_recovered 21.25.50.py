import json

ZYRO_BASE = "https://assets.zyrosite.com/A85Dpv78OotyVQVx/"
ECO_BASE = "https://www.ecoexpresswater.com/wp-content/uploads"

PRODUCTS = [
    # === Wall-Mounted Water Dispensers (from expresswater.cn) ===
    {
        "id": "mt-900g",
        "name": "Golden Color Water Dispenser MT-900G",
        "category": "Water Dispenser",
        "image": ZYRO_BASE + "ee2ae-3-4-m5KPNbPPwluQy8no.png",
        "desc": "Wall-mounted pipeline water dispenser with 5 stages of water volume (150ml–850ml) and 5 levels of water temperature (25°C–100°C). 316L titanium gold stainless steel heating element. Child safety lock. Premium golden glass panel.",
        "specs": {"Power": "2200W", "Volume": "5 stages 150–850ml", "Temperature": "25–100°C", "Material": "316L Stainless Steel"}
    },
    {
        "id": "mt-s800",
        "name": "White Color Water Dispenser MT-S800",
        "category": "Water Dispenser",
        "image": ZYRO_BASE + "ee2ae-3-4-copy-mePynXO7bpcqML47.png",
        "desc": "Wall-mounted pipeline water dispenser with 2200W rated power. Fast 3-second hot water output. 5 stages water volume and temperature adjustment. White glass panel.",
        "specs": {"Power": "2200W", "Hot Output": "3 seconds", "Color": "White Glass Panel"}
    },
    {
        "id": "mt-600dg",
        "name": "Dark Green Water Dispenser MT-600DG",
        "category": "Water Dispenser",
        "image": ZYRO_BASE + "ac-c-e2c-r-co-aeoaepsec-mp8M9o3jKVHDxrn2.png",
        "desc": "Wall-mounted pipeline water dispenser with sleek modern design in unique dark green color. Saves floor space and provides continuous supply of clean water.",
        "specs": {"Mount": "Wall-mounted", "Color": "Dark Green", "Power": "2200W"}
    },
    {
        "id": "mt-b600",
        "name": "Black Color Water Dispenser MT-B600",
        "category": "Water Dispenser",
        "image": ZYRO_BASE + "c1-2e2-1-copy-YD0r4gjVybULQ1pw.png",
        "desc": "Wall-mounted pipeline water dispenser with 2200W rated power and fast 3-second heating. Whole glass panel with matte spray plastic parts.",
        "specs": {"Power": "2200W", "Hot Output": "3 seconds", "Color": "Black Glass Panel"}
    },
    {
        "id": "mt-e600",
        "name": "Wall Mounted Water Dispenser MT-E600",
        "category": "Water Dispenser",
        "image": ZYRO_BASE + "e-600-bw-dWxeGeNwMWu0NzBY.png",
        "desc": "Black & white dual-color wall-mounted pipeline water dispenser. Compact, energy-saving, with multi-stage water output.",
        "specs": {"Mount": "Wall-mounted", "Color": "Black/White"}
    },
    {
        "id": "mt-dv-e600",
        "name": "1000W Vertical Water Dispenser MT-DV-E600",
        "category": "Water Dispenser",
        "image": ZYRO_BASE + "mt-dv-e600-mxBj0l5gB4U8pZwq.png",
        "desc": "High-power vertical water dispenser with 304 stainless steel tank and 1KW heating power. LED digital screen.",
        "specs": {"Power": "1000W", "Tank": "304 Stainless Steel", "Display": "LED Digital"}
    },
    {
        "id": "mt-v-e300a",
        "name": "Vertical Water Dispenser MT-V-E300A",
        "category": "Water Dispenser",
        "image": ZYRO_BASE + "mt-v-e300a-black-white-dWxeGwbOrkf1yWW0.png",
        "desc": "Vertical floor-standing water dispenser with 304 stainless steel water tank and multiple water outlet options. Black/White design.",
        "specs": {"Type": "Vertical", "Tank": "304 Stainless Steel", "Color": "Black/White"}
    },
    # === RO Systems & Housings (from ecoexpresswater) ===
    {
        "id": "ro-undersink",
        "name": "Under-Sink Reverse Osmosis Water Filter",
        "category": "RO System",
        "image": f"{ECO_BASE}/2022/08/IMG_5846-scaled-768x1024.jpg",
        "desc": "Gravity-fed RO system relying on incoming water pressure to push water through the RO membrane. Multi-stage: sediment filter, carbon filter, RO membrane.",
        "specs": {"Stages": "Multi-stage", "Type": "No Pump Required", "Membrane": "RO 75GPD"}
    },
    {
        "id": "big-blue-3stage",
        "name": "30-inch Three Stage Big Blue Water Filter",
        "category": "Filter Housing",
        "image": f"{ECO_BASE}/2022/08/IMG_8856-scaled-768x1024.jpg",
        "desc": "Three-stage filtration: PP filter (large particles), RO membrane (heavy metals, bacteria, viruses), CTO Carbon Block (chlorine, taste).",
        "specs": {"Size": "30 inches", "Stages": "3", "Type": "Big Blue"}
    },
    {
        "id": "uv-purifier",
        "name": "Three Stage Plus UV Water Purifier",
        "category": "Water Purifier",
        "image": f"{ECO_BASE}/2022/08/ed1b75a2f9de969d15bf4904160302e-768x1024.jpg",
        "desc": "Three-stage water purification system enhanced with UV sterilization for superior water safety.",
        "specs": {"Stages": "3 + UV", "Sterilization": "UV-C"}
    },
    {
        "id": "mid-filter",
        "name": "Medium Size Water Filter w/ Copper Connector",
        "category": "Filter Cartridge",
        "image": f"{ECO_BASE}/2022/08/MG_9234-scaled.jpg",
        "desc": "Medium-sized water filter cartridge featuring a copper connector for robust installation and performance.",
        "specs": {"Size": "Medium", "Connector": "Copper"}
    },
    {
        "id": "housing-filter",
        "name": "Eco Express Water Housing Filter",
        "category": "Filter Housing",
        "image": f"{ECO_BASE}/2022/04/IMG_5618-scaled-1024x768.jpg",
        "desc": "Carbon block filter using activated carbon compressed into a block. Removes chlorine, chloramines, pesticides, and odors.",
        "specs": {"Type": "Carbon Block Housing", "Connector": "Various"}
    },
    # === Filter Cartridges (from ecoexpresswater) ===
    {
        "id": "carbon-block",
        "name": "Carbon Block Filter (Coconut Shell)",
        "category": "Filter Cartridge",
        "image": f"{ECO_BASE}/2022/04/carbon-block-filter-copy.jpg",
        "desc": "Coconut shell activated carbon with high iodine value (1000) for effective purification. 10 inches length, 2.5 inch outer diameter.",
        "specs": {"Iodine": "1000", "Material": "Coconut Carbon", "Size": "10×2.5 inch"}
    },
    {
        "id": "pp-spun",
        "name": "PP Spun Sediment Filter",
        "category": "Filter Cartridge",
        "image": f"{ECO_BASE}/2022/04/PP-Spun-Filter-copy.jpg",
        "desc": "Melt-blown 100% pure polypropylene microfibers. Removes rust, silt, scale, sediment, dirt. Available in 10/20/30/40 inches.",
        "specs": {"Material": "100% Polypropylene", "Sizes": "10–40 inch", "Removes": "Sediment 5μm"}
    },
    {
        "id": "udf-cartridge",
        "name": "UDF Granular Activated Carbon Filter",
        "category": "Filter Cartridge",
        "image": f"{ECO_BASE}/2022/04/UDF-Filter-cartridge-copy.jpg",
        "desc": "Standard 10-inch GAC filter from high iodine value carbon. Reduces chlorine, organic chemicals, unnatural tastes and odors.",
        "specs": {"Type": "GAC", "Size": "10 inch", "Iodine": "1000"}
    },
    {
        "id": "ceramic-filter",
        "name": "Ceramic Filter Cartridge",
        "category": "Filter Cartridge",
        "image": f"{ECO_BASE}/2022/04/WeChat8b6176de1327055fb109da157c1d47dd-845x1024.png",
        "desc": "High-quality ceramic filter cartridge for removing fine particles and bacteria.",
        "specs": {"Filtration": "0.2μm", "Type": "Ceramic"}
    },
    {
        "id": "resin-filter",
        "name": "Ion-Exchange Resin Filter",
        "category": "Filter Cartridge",
        "image": f"{ECO_BASE}/2022/04/WeChat48b644654d6e0f5e709716ba2298b556-889x1024.png",
        "desc": "Ion-exchange resin cartridge for water softening and removal of heavy metals.",
        "specs": {"Function": "Water Softening", "Removes": "Ca/Mg/Heavy Metals"}
    },
    {
        "id": "uf-cartridge",
        "name": "Ultrafiltration (UF) Cartridge",
        "category": "Filter Cartridge",
        "image": f"{ECO_BASE}/2022/04/Ultra-FilterUF-copy.jpg",
        "desc": "Hollow-fiber ultrafiltration membrane cartridge for removing bacteria, viruses, and colloidal matter.",
        "specs": {"Membrane": "Hollow Fiber", "Filtration": "0.01μm"}
    },
    {
        "id": "maifan-inline",
        "name": "Maifan Stone Inline Filter",
        "category": "Inline Filter",
        "image": f"{ECO_BASE}/2022/04/Maifan-stone-Filter-copy.jpg",
        "desc": "Inline filter containing Maifan stones to mineralize water and improve taste.",
        "specs": {"Mineral": "Maifan Stone", "Function": "Mineralization"}
    },
    {
        "id": "mineral-inline",
        "name": "Inline Mineral Filter",
        "category": "Inline Filter",
        "image": f"{ECO_BASE}/2022/04/Mineral-Filter-copy.jpg",
        "desc": "Adds essential minerals back into purified water to enhance health benefits and taste.",
        "specs": {"Function": "Mineralization", "Adds": "Ca/Mg/K minerals"}
    },
    {
        "id": "ro-membrane",
        "name": "RO Membrane Filter Cartridge",
        "category": "Filter Cartridge",
        "image": f"{ECO_BASE}/2022/04/RO-Membrane-Filter-Cartridge-copy.jpg",
        "desc": "Reverse osmosis membrane cartridge — the core component of RO systems for desalination and purification.",
        "specs": {"Type": "RO TFC Membrane", "Capacity": "75/100/400 GPD"}
    },
    {
        "id": "filter-combo",
        "name": "Multi-Stage Filter Cartridge Combination",
        "category": "Filter Cartridge",
        "image": f"{ECO_BASE}/2022/04/Filter-cartridge-combination-copy.jpg",
        "desc": "Combination of various filter cartridges designed for multi-stage purification.",
        "specs": {"Stages": "3–5", "Combination": "Custom"}
    },
    {
        "id": "post-t33",
        "name": "Post T33 Inline Carbon Filter",
        "category": "Inline Filter",
        "image": f"{ECO_BASE}/2022/04/Post-T33-Filter-copy.jpg",
        "desc": "Post-filtration inline carbon filter for polishing water taste and removing residual odors.",
        "specs": {"Position": "Final stage", "Material": "Activated Carbon"}
    },
    {
        "id": "inline-pp",
        "name": "Inline PP Cartridge",
        "category": "Inline Filter",
        "image": f"{ECO_BASE}/2022/04/PP-filter-copy.jpg",
        "desc": "Inline polypropylene sediment filter for compact water purification systems.",
        "specs": {"Material": "Polypropylene", "Filtration": "5μm"}
    },
    {
        "id": "ppf-cartridge",
        "name": "PPF Polypropylene Fiber Cartridge",
        "category": "Filter Cartridge",
        "image": f"{ECO_BASE}/2022/04/PPF-Filter-copy.jpg",
        "desc": "Polypropylene fiber filter cartridge for sediment removal.",
        "specs": {"Material": "PP Fiber", "Function": "Sediment"}
    },
    {
        "id": "pre-udf",
        "name": "Pre-UDF Activated Carbon Cartridge",
        "category": "Filter Cartridge",
        "image": f"{ECO_BASE}/2022/04/Pre-UDF-Filter-copy.jpg",
        "desc": "Pre-filtration granular activated carbon cartridge to protect downstream membranes.",
        "specs": {"Position": "Pre-filter", "Material": "GAC"}
    },
    {
        "id": "t33-post",
        "name": "T33 Post Filter Cartridge",
        "category": "Inline Filter",
        "image": f"{ECO_BASE}/2022/04/T33-post-Filter-copy.jpg",
        "desc": "High-quality post-carbon filter for final stage purification.",
        "specs": {"Position": "Post-filter", "Function": "Polishing"}
    },
    {
        "id": "ultra-film",
        "name": "Ultra Film Filter Cartridge",
        "category": "Filter Cartridge",
        "image": f"{ECO_BASE}/2022/04/Ultra-Film-Filter-copy.jpg",
        "desc": "Advanced ultrafiltration film cartridge for high-efficiency filtration.",
        "specs": {"Type": "Ultra Film", "Filtration": "0.01μm"}
    },
    {
        "id": "uf-filter-2",
        "name": "UF Hollow Fiber Filter",
        "category": "Filter Cartridge",
        "image": f"{ECO_BASE}/2022/04/UF-Filter-copy.jpg",
        "desc": "Ultrafiltration cartridge for fine suspended-solids removal.",
        "specs": {"Material": "Hollow Fiber", "Removes": "Bacteria"}
    },
    # === Industrial PP & Carbon (from cn) ===
    {
        "id": "pp-soe-doe",
        "name": "Industrial PP Filter (SOE/DOE)",
        "category": "Industrial Filter",
        "image": ZYRO_BASE + "pp-filter-soe-and-doe-A0x4xbrBOPcpr4nX.png",
        "desc": "Industrial-grade PP melt-blown filter, available in SOE (Single Open End) and DOE (Double Open End) configurations.",
        "specs": {"Type": "SOE/DOE", "Material": "Polypropylene", "Industry": "Industrial"}
    },
    {
        "id": "pp-fin-cap",
        "name": "PP Filter with Fin End Cap",
        "category": "Industrial Filter",
        "image": ZYRO_BASE + "pp-filter-with-fin-end-cap-AQEXE9JgGXIjQaoo.jpg",
        "desc": "Industrial PP cartridge with a fin-style end cap for secure, leak-free seating in housing units.",
        "specs": {"End Cap": "Fin Type", "Material": "Polypropylene"}
    },
    {
        "id": "pp-silicon-ring",
        "name": "PP Filter with Silicon Ring",
        "category": "Industrial Filter",
        "image": ZYRO_BASE + "pp-filter-with-silicon-ring-YrDLDBNea9fG9Q5k.jpg",
        "desc": "PP filter cartridge equipped with food-grade silicon sealing ring for high-reliability sealing.",
        "specs": {"Ring": "Food-grade Silicon", "Material": "Polypropylene"}
    },
    {
        "id": "carbon-block-industrial",
        "name": "Industrial Carbon Block Filter",
        "category": "Industrial Filter",
        "image": ZYRO_BASE + "wechatimg25665-YbNbr1krr7SvNJV0.jpeg",
        "desc": "Industrial-grade activated carbon block filter for high-flow chemical absorption applications.",
        "specs": {"Type": "Carbon Block", "Industry": "Industrial"}
    },
    {
        "id": "carbon-block-2",
        "name": "Compressed Activated Carbon Block",
        "category": "Industrial Filter",
        "image": ZYRO_BASE + "wechatimg25674-mk3lrNoaEaUvnLg7.jpeg",
        "desc": "High-density compressed carbon block for superior chlorine and VOC removal.",
        "specs": {"Density": "High", "Removes": "Chlorine, VOCs"}
    },
    # === Inline Filters (from cn) ===
    {
        "id": "inline-t33-mineral",
        "name": "Mineralized Small T33 Inline Water Filter",
        "category": "Inline Filter",
        "image": ZYRO_BASE + "mineralized-small-t33-inline-water-filter-AQEX6g58g7ikZgwl.png",
        "desc": "Improves taste and odor by removing chlorine and adding beneficial minerals to water for improved health and hydration.",
        "specs": {"Function": "Mineralization + Polishing", "Connector": "Quick-connect"}
    },
    {
        "id": "inline-small-mol",
        "name": "Small Molecule Antibacterial Mineralization Filter",
        "category": "Inline Filter",
        "image": ZYRO_BASE + "inline-small-molecule-antibacterial-mineralization-filter-cartridge-m2WbO3PQ8rSyVBbJ.png",
        "desc": "Advanced filtration removing harmful bacteria and viruses while adding beneficial minerals to water.",
        "specs": {"Function": "Antibacterial + Mineralization", "Connector": "Quick-connect"}
    },
    {
        "id": "antibacterial-mineralization",
        "name": "Antibacterial Mineralization Filter Cartridge",
        "category": "Inline Filter",
        "image": ZYRO_BASE + "antibacterial-mineralization-filter-cartridge-YBgoD6orwBUllOa2.png",
        "desc": "Effectively removes harmful bacteria and viruses and adds beneficial minerals.",
        "specs": {"Function": "Antibacterial + Mineralization"}
    },
    {
        "id": "inline-cation-resin",
        "name": "Inline Cation Resin Filter Cartridge",
        "category": "Inline Filter",
        "image": ZYRO_BASE + "inline-cation-resin-filter-cartridge-AGBr0XGDo7t0NDKE.png",
        "desc": "Softens water by removing hard minerals such as calcium and magnesium, reducing scale buildup in appliances.",
        "specs": {"Function": "Water Softening", "Resin": "Cation Exchange"}
    },
    {
        "id": "inline-t33-coconut",
        "name": "T33 Coconut Shell Carbon Inline Filter",
        "category": "Inline Filter",
        "image": ZYRO_BASE + "wechatimg25674-m7V2npvka6TLValG.jpeg",
        "desc": "Post-filter T33 inline cartridge with premium coconut shell activated carbon for taste polishing.",
        "specs": {"Carbon": "Coconut Shell", "Position": "Post-filter"}
    },
    # === Flat Cap Filter Series (from cn) ===
    {
        "id": "flat-cap-gac",
        "name": "Flat Cap GAC Filter",
        "category": "Flat Cap Filter",
        "image": ZYRO_BASE + "a13apsudf-mp8MqXBP8ptD7oab.jpg",
        "desc": "Universal GAC filter with Flat Cap connection. Made with silicon rubber flat cap. Effectively removes chlorine, sediment, and other contaminants.",
        "specs": {"Cap": "Silicon Rubber Flat Cap", "Material": "GAC"}
    },
    {
        "id": "flat-cap-cto",
        "name": "Flat Cap CTO Carbon Block Filter",
        "category": "Flat Cap Filter",
        "image": ZYRO_BASE + "1676798539834-dOqM8JyQL5fj99OO.jpg",
        "desc": "Compressed Activated Carbon Block filter with flat cap connection for universal compatibility with standard housings.",
        "specs": {"Type": "CTO", "Cap": "Flat Cap"}
    },
    {
        "id": "flat-cap-pp",
        "name": "Flat Cap PP Sediment Filter",
        "category": "Flat Cap Filter",
        "image": ZYRO_BASE + "1676799952716-A0x3EWL3l7teXEKl.jpg",
        "desc": "Polypropylene melt-blown sediment filter with flat cap design. Designed for use in standard 10\" filter housings.",
        "specs": {"Type": "PP Melt-blown", "Cap": "Flat Cap"}
    },
]

CATEGORIES = sorted(set(p["category"] for p in PRODUCTS))

manifest = {
    "company": {
        "name": "Eco Express Water",
        "tagline": "Industrial Water Filtration Manufacturer",
        "founded": 1998,
        "factory_address": "1# Chuangxin Road, Yuanhua Town, Haining, Zhejiang Province, China",
        "phone": "+86-19908311885",
        "whatsapp": "+86-19908311885",
        "email": "info@ecoexpresswater.com",
        "about": "Eco Express Water is a high-tech environment protection enterprise specializing in filter materials and filter equipment for water purification. Established in 1998, our products integrate the full stream from research and development, manufacturing, marketing to technical support. Our company is located in Yuanhua Town, Haining City, Zhejiang Province. We have a first-class technical expert team, integrated functional middle test/expanding test, and a large-scale manufacturing center. We are a certified supplier of halal water filters, catering to the unique needs and requirements of Muslim consumers in Malaysia, Indonesia, and other Muslim countries."
    },
    "hero_image": "https://www.ecoexpresswater.com/wp-content/uploads/2022/04/IMG_5611-scaled.jpg",
    "categories": CATEGORIES,
    "products": PRODUCTS,
    "workshop_images": [
        {"url": "https://www.ecoexpresswater.com/wp-content/uploads/2022/08/PP-滤芯-生产线-300x170.png", "caption": "PP Filter Production Line"},
        {"url": "https://www.ecoexpresswater.com/wp-content/uploads/2022/08/Carbon-Block-Filter碳棒生产-1024x577.png", "caption": "Carbon Block Filter Production"},
        {"url": "https://www.ecoexpresswater.com/wp-content/uploads/2022/08/快接生产线-300x167.png", "caption": "Quick-Connect Filter Production"},
        {"url": "https://www.ecoexpresswater.com/wp-content/uploads/2022/08/自动测漏机-300x169.png", "caption": "Automatic Leak Testing"}
    ],
    "exhibition_images": [
        {"url": "https://www.ecoexpresswater.com/wp-content/uploads/2023/06/Waterfilters-1024x576.jpeg.webp", "caption": "AquaTech Shanghai Booth"},
        {"url": "https://www.ecoexpresswater.com/wp-content/uploads/2023/06/water-filters-1024x576.jpg.webp", "caption": "AquaTech Shanghai Display"},
        {"url": "https://www.ecoexpresswater.com/wp-content/uploads/2022/04/WechatIMG7861-1024x768.jpeg", "caption": "Trade Show Booth"},
        {"url": "https://www.ecoexpresswater.com/wp-content/uploads/2022/04/WechatIMG7860-1024x768.jpeg", "caption": "Trade Show Customers"}
    ]
}

with open("master_manifest.json", "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)

print(f"Saved manifest with {len(PRODUCTS)} products across {len(CATEGORIES)} categories")
print(f"Categories: {CATEGORIES}")