const fs = require('fs');
const manifest = JSON.parse(fs.readFileSync('master_manifest.json', 'utf8'));

const ui = {
  nav_home: "Home",
  nav_products: "Products",
  nav_about: "About Us",
  nav_workshop: "Workshop",
  nav_exhibition: "Exhibitions",
  nav_contact: "Contact",
  cta_whatsapp: "WhatsApp Us",
  hero_eyebrow: "✦ Trusted Water Filtration Manufacturer Since 1998",
  hero_title: "Industrial-Grade Water Filtration Solutions",
  hero_desc: "Specialized in PP, Carbon Block, GAC, T33, RO membranes, and water dispenser manufacturing. NSF · ISO · CE · Halal certified. OEM/ODM partners across 50+ countries.",
  hero_btn_explore: "Explore Products",
  hero_btn_quote: "Get a Quote",
  stats_years: "Years Experience",
  stats_models: "Product Models",
  stats_countries: "Countries Served",
  stats_area: "Manufacturing Area",
  about_eyebrow: "About Us",
  about_title: "20+ Years of Water Filtration Excellence",
  about_desc: "Eco Express Water is a high-tech environment protection enterprise specializing in filter materials and filter equipment for water purification. Established in 1998, our products integrate the full stream from research and development, manufacturing, marketing to technical support. Our company is located in Yuanhua Town, Haining City, Zhejiang Province. We have a first-class technical expert team, integrated functional middle test/expanding test, and a large-scale manufacturing center. We are a certified supplier of halal water filters, catering to the unique needs and requirements of Muslim consumers in Malaysia, Indonesia, and other Muslim countries.",
  about_feat_1: "Established in 1998 – Over two decades of manufacturing expertise",
  about_feat_2: "Full vertical integration: R&D, Manufacturing, QC, Logistics",
  about_feat_3: "NSF, ISO, CE, and Halal certified production lines",
  about_feat_4: "OEM/ODM service for global brands across 50+ countries",
  about_feat_5: "Located in Haining, Zhejiang – China's water filtration hub",
  why_eyebrow: "Why Choose Us",
  why_title: "Trusted Manufacturing Partner",
  why_desc: "From raw materials to final inspection, every product passes our rigorous quality control system.",
  why_card1_title: "Certified Quality",
  why_card1_desc: "NSF / ISO / CE / Halal certifications backed by every batch we produce.",
  why_card2_title: "OEM / ODM Ready",
  why_card2_desc: "Custom branding, packaging, and product specifications to match your market.",
  why_card3_title: "In-House Production",
  why_card3_desc: "4 dedicated production lines covering PP, Carbon, Quick-connect, and Leak Test.",
  why_card4_title: "Worldwide Shipping",
  why_card4_desc: "Lead time 7–15 days with established export logistics to 50+ countries.",
  products_eyebrow: "Our Products",
  products_title: "Complete Water Filtration Portfolio",
  products_desc: "42 models across 8 categories – from inline cartridges to vertical dispensers and complete RO systems.",
  cat_all: "All Products",
  product_view_details: "View Details",
  workshop_eyebrow: "Manufacturing",
  workshop_title: "Inside Our Workshop",
  workshop_desc: "4 specialized production lines: PP filter, Carbon block, Quick-connect inline, and Automatic leak detection.",
  workshop_pp: "PP Filter Production Line",
  workshop_carbon: "Carbon Block Filter Production",
  workshop_quick: "Quick-Connect Filter Production",
  workshop_leak: "Automatic Leak Testing",
  exhibition_eyebrow: "Trade Shows",
  exhibition_title: "Global Exhibitions",
  exhibition_desc: "Meet our team at AquaTech Shanghai and other major industry events.",
  exhibition_aqua1: "AquaTech Shanghai Booth",
  exhibition_aqua2: "AquaTech Shanghai Display",
  exhibition_show: "Trade Show Booth",
  exhibition_customers: "Trade Show Customers",
  contact_eyebrow: "Get in Touch",
  contact_title: "Let's Build Together",
  contact_desc: "Tell us about your project. Our sales engineers respond within 24 hours.",
  contact_address_label: "Factory Address",
  contact_address: "1# Chuangxin Road, Yuanhua Town, Haining, Zhejiang Province, China",
  contact_phone_label: "Phone / WhatsApp",
  contact_email_label: "Email Address",
  form_title: "Send Inquiry",
  form_sub: "Get a detailed quote for your specifications.",
  form_name: "Your Name",
  form_email: "Email Address",
  form_company: "Company Name",
  form_msg: "Message / Specifications",
  form_btn: "Send Inquiry",
  footer_products: "Products",
  footer_company: "Company",
  footer_contact: "Contact",
  footer_rights: "All rights reserved.",
  modal_specs_title: "Technical Specifications",
  modal_btn_wa: "Inquiry via WhatsApp",
  modal_btn_email: "Inquiry via Email"
};

const categories = {
  "Filter Cartridge": "Filter Cartridge",
  "Filter Housing": "Filter Housing",
  "Flat Cap Filter": "Flat Cap Filter",
  "Industrial Filter": "Industrial Filter",
  "Inline Filter": "Inline Filter",
  "RO System": "RO System",
  "Water Dispenser": "Water Dispenser",
  "Water Purifier": "Water Purifier"
};

const products = manifest.products.map(p => ({
  id: p.id,
  name: p.name,
  category: p.category,
  desc: p.desc,
  specs: p.specs
}));

const data = {
  en: {
    ui,
    categories,
    products
  }
};

fs.writeFileSync('en_source.json', JSON.stringify(data, null, 2));
console.log('en_source.json created');
