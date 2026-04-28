#!/usr/bin/env python3
"""Build the final index.html for Eco Express Water - Filterpur-inspired design"""
import json
import html as html_lib

with open("master_manifest.json", "r", encoding="utf-8") as f:
    M = json.load(f)

co = M["company"]
products = M["products"]
categories = M["categories"]
workshop = M["workshop_images"]
exhibition = M["exhibition_images"]

VERSION = "26.4.26.16.00"

# Color palette inspired by filterpur.com but adapted for water filtration
PRIMARY = "#1085CF"      # filterpur blue
PRIMARY_DARK = "#0a6bb0"
ACCENT = "#00C4F0"       # cyan accent
DARK_TEXT = "#1a1a1a"
LIGHT_BG = "#F7F8FA"
DARK_BG = "#0E1A2B"      # deeper than filterpur for hi-end feel

def esc(s):
    return html_lib.escape(s) if s else ""

# Build product card HTML
def product_card(p):
    return f'''
        <div class="product-card" data-cat="{esc(p["category"])}">
            <a href="#product-{p["id"]}" @click.prevent="openProduct('{p["id"]}')" class="product-link">
                <div class="product-img-wrap">
                    <img loading="lazy" decoding="async" src="{esc(p["image_local"])}" alt="{esc(p["name"])}" width="400" height="400" />
                </div>
                <div class="product-info">
                    <div class="product-cat">{esc(p["category"])}</div>
                    <h3 class="product-title">{esc(p["name"])}</h3>
                    <span class="product-more">View Details &rarr;</span>
                </div>
            </a>
        </div>'''

# Build category filter buttons
def cat_buttons():
    btns = ['<button class="cat-btn active" @click="filter=\'all\'" :class="{active: filter===\'all\'}">All Products</button>']
    for c in categories:
        btns.append(f'<button class="cat-btn" @click="filter=\'{esc(c)}\'" :class="{{active: filter===\'{esc(c)}\'}}">{esc(c)}</button>')
    return "\n            ".join(btns)

# Build product modal data (alpine reactive)
products_json = json.dumps([{
    "id": p["id"],
    "name": p["name"],
    "category": p["category"],
    "image": p["image_local"],
    "desc": p["desc"],
    "specs": p.get("specs", {})
} for p in products], ensure_ascii=False)

# Build workshop / exhibition gallery
def gallery_item(item, alt):
    return f'''<figure class="gal-item">
        <img loading="lazy" decoding="async" src="{esc(item["url_local"])}" alt="{esc(alt)}" width="600" height="400" />
        <figcaption>{esc(item["caption"])}</figcaption>
    </figure>'''

workshop_html = "\n        ".join(gallery_item(w, w["caption"]) for w in workshop)
exhibition_html = "\n        ".join(gallery_item(e, e["caption"]) for e in exhibition)

# Stats - filterpur-style stats bar
STATS = [
    {"num": "20+", "label": "Years Experience"},
    {"num": "42+", "label": "Product Models"},
    {"num": "50+", "label": "Countries Served"},
    {"num": "10000m\u00b2", "label": "Manufacturing Area"},
]

stats_html = "\n            ".join(
    f'<div class="stat-item"><div class="stat-num">{esc(s["num"])}</div><div class="stat-label">{esc(s["label"])}</div></div>'
    for s in STATS
)

# All product cards
products_html = "\n        ".join(product_card(p) for p in products)

# Generate the full HTML
HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(co["name"])} - {esc(co["tagline"])} | Water Filter Cartridges, Dispensers, RO Systems</title>
<meta name="description" content="{esc(co["name"])} is a leading manufacturer of industrial water filtration solutions since {co["founded"]}. PP, Carbon Block, GAC, T33, RO membranes, water dispensers and OEM/ODM services from Haining, China.">
<meta name="keywords" content="water filter manufacturer, PP filter, carbon block filter, RO membrane, water dispenser, OEM water filter, China filter factory">
<meta name="theme-color" content="{PRIMARY}">
<link rel="canonical" href="https://www.yuchensy.com/">

<!-- Open Graph / SEO -->
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(co["name"])} - Industrial Water Filtration Manufacturer">
<meta property="og:description" content="High-quality water filter cartridges, dispensers and RO systems. OEM/ODM since 1998.">
<meta property="og:image" content="assets/hero.jpg">
<meta name="twitter:card" content="summary_large_image">

<!-- Preload critical assets -->
<link rel="preload" as="image" href="assets/hero.jpg" fetchpriority="high">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet">

<!-- Structured data for SEO -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Manufacturer",
  "name": "{esc(co["name"])}",
  "url": "https://www.yuchensy.com/",
  "logo": "assets/logo.png",
  "description": "{esc(co["about"][:200])}",
  "address": {{
    "@type": "PostalAddress",
    "streetAddress": "{esc(co["factory_address"])}",
    "addressCountry": "CN"
  }},
  "telephone": "{esc(co["phone"])}",
  "email": "{esc(co["email"])}",
  "foundingDate": "{co["founded"]}"
}}
</script>

<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
:root{{
  --primary:{PRIMARY};
  --primary-dark:{PRIMARY_DARK};
  --accent:{ACCENT};
  --dark:{DARK_TEXT};
  --light:{LIGHT_BG};
  --bg-dark:{DARK_BG};
  --text:#333;
  --muted:#666;
  --border:#e5e7eb;
}}
html{{scroll-behavior:smooth;-webkit-text-size-adjust:100%}}
body{{
  font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;
  color:var(--text);
  line-height:1.6;
  background:#fff;
  font-size:16px;
}}
img{{max-width:100%;height:auto;display:block}}
h1,h2,h3,h4{{font-family:'Playfair Display',Georgia,serif;font-weight:700;color:var(--dark);line-height:1.2}}
h2{{font-size:clamp(1.7rem,3.5vw,2.5rem);margin-bottom:.5rem}}
h3{{font-size:1.25rem}}
a{{color:var(--primary);text-decoration:none;transition:color .2s}}
a:hover{{color:var(--primary-dark)}}
.container{{max-width:1280px;margin:0 auto;padding:0 24px}}

/* ===== Top bar ===== */
.topbar{{background:var(--bg-dark);color:#cfd8e3;font-size:13px;padding:8px 0}}
.topbar-inner{{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px}}
.topbar a{{color:#cfd8e3}}
.topbar a:hover{{color:#fff}}
.tb-info{{display:flex;gap:18px;flex-wrap:wrap}}
.tb-info span{{display:inline-flex;align-items:center;gap:6px}}
.tb-icon{{width:14px;height:14px;display:inline-block;vertical-align:middle}}

/* ===== Header ===== */
.header{{position:sticky;top:0;background:#fff;z-index:100;box-shadow:0 1px 8px rgba(0,0,0,.06);transition:box-shadow .2s}}
.header-inner{{display:flex;align-items:center;justify-content:space-between;padding:14px 0;gap:24px}}
.logo{{display:flex;align-items:center;gap:12px;text-decoration:none}}
.logo img{{height:46px;width:auto}}
.logo-text{{display:flex;flex-direction:column;line-height:1.1}}
.logo-name{{font-family:'Playfair Display',serif;font-size:1.2rem;font-weight:700;color:var(--dark)}}
.logo-tag{{font-size:.7rem;color:var(--muted);letter-spacing:.5px;text-transform:uppercase}}
.nav{{display:flex;gap:6px;align-items:center}}
.nav a{{color:var(--dark);font-weight:500;padding:10px 16px;border-radius:6px;transition:all .2s;font-size:.95rem}}
.nav a:hover,.nav a.active{{color:var(--primary);background:rgba(16,133,207,.08)}}
.cta{{display:inline-flex;align-items:center;gap:8px;background:var(--primary);color:#fff;padding:10px 20px;border-radius:6px;font-weight:600;font-size:.95rem;border:none;cursor:pointer;transition:all .2s}}
.cta:hover{{background:var(--primary-dark);color:#fff;transform:translateY(-1px);box-shadow:0 6px 14px rgba(16,133,207,.3)}}
.cta-wa{{background:#25D366}}
.cta-wa:hover{{background:#1da851}}
.menu-btn{{display:none;background:none;border:none;cursor:pointer;padding:8px;width:42px;height:42px;flex-direction:column;justify-content:space-around}}
.menu-btn span{{display:block;height:2px;background:var(--dark);transition:.3s}}

/* ===== Hero ===== */
.hero{{position:relative;color:#fff;overflow:hidden;min-height:560px;display:flex;align-items:center;background:#0E1A2B}}
.hero-bg{{position:absolute;inset:0;z-index:0}}
.hero-bg img{{width:100%;height:100%;object-fit:cover;opacity:.42}}
.hero-bg::after{{content:'';position:absolute;inset:0;background:linear-gradient(135deg,rgba(14,26,43,.85) 0%,rgba(16,133,207,.55) 100%)}}
.hero-inner{{position:relative;z-index:1;padding:90px 0 140px;width:100%}}
.hero-eyebrow{{display:inline-block;background:rgba(255,255,255,.12);backdrop-filter:blur(10px);color:#fff;padding:6px 16px;border-radius:50px;font-size:.85rem;font-weight:500;margin-bottom:24px;border:1px solid rgba(255,255,255,.18)}}
.hero h1{{color:#fff;font-size:clamp(2rem,5vw,3.6rem);font-weight:700;margin-bottom:20px;letter-spacing:-.5px;text-shadow:0 2px 12px rgba(0,0,0,.3)}}
.hero p{{font-size:clamp(1rem,1.6vw,1.18rem);max-width:680px;margin-bottom:32px;color:#e6f0fa;line-height:1.7}}
.hero-ctas{{display:flex;gap:14px;flex-wrap:wrap}}
.btn-outline{{background:transparent;border:2px solid #fff;color:#fff}}
.btn-outline:hover{{background:#fff;color:var(--primary)}}

/* ===== Stats Bar (filterpur-inspired floating) ===== */
.stats-bar{{position:relative;z-index:5;margin-top:-70px;background:#fff;border-radius:14px;box-shadow:0 16px 40px rgba(0,0,0,.10);padding:36px 24px;display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin-bottom:40px}}
.stat-item{{text-align:center}}
.stat-num{{font-family:'Playfair Display',serif;font-size:clamp(1.8rem,3.5vw,2.8rem);font-weight:700;color:var(--primary);line-height:1}}
.stat-label{{font-size:.92rem;color:var(--muted);margin-top:8px;font-weight:500}}

/* ===== Section ===== */
.section{{padding:80px 0}}
.section.bg-light{{background:var(--light)}}
.section.bg-dark{{background:var(--bg-dark);color:#dbe6f1}}
.section.bg-dark h2{{color:#fff}}
.section.bg-dark p{{color:#bcc7d2}}
.section-head{{text-align:center;max-width:760px;margin:0 auto 50px}}
.section-eyebrow{{color:var(--primary);font-weight:600;font-size:.9rem;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:8px;display:block}}
.section-head p{{color:var(--muted);margin-top:14px;font-size:1.05rem}}

/* ===== About 2-column ===== */
.about-grid{{display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:center}}
.about-img{{position:relative;border-radius:12px;overflow:hidden;box-shadow:0 20px 50px rgba(0,0,0,.12)}}
.about-img img{{width:100%;aspect-ratio:4/3;object-fit:cover;transition:transform .6s}}
.about-img:hover img{{transform:scale(1.04)}}
.about-text h2{{margin-bottom:20px}}
.about-text p{{margin-bottom:20px;color:var(--text)}}
.about-feats{{list-style:none;display:grid;gap:14px;margin-top:24px}}
.about-feats li{{padding-left:32px;position:relative;font-weight:500;color:var(--dark)}}
.about-feats li::before{{content:'\\2713';position:absolute;left:0;width:20px;height:20px;background:var(--primary);color:#fff;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.7rem;font-weight:700;top:3px}}

/* ===== Product Grid ===== */
.cat-filter{{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;margin-bottom:40px}}
.cat-btn{{background:#fff;border:1px solid var(--border);color:var(--dark);padding:10px 20px;border-radius:50px;cursor:pointer;font-size:.92rem;font-weight:500;transition:all .2s}}
.cat-btn:hover{{border-color:var(--primary);color:var(--primary)}}
.cat-btn.active{{background:var(--primary);color:#fff;border-color:var(--primary)}}
.product-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:24px}}
.product-card{{background:#fff;border-radius:12px;overflow:hidden;border:1px solid var(--border);transition:all .3s;cursor:pointer}}
.product-card:hover{{transform:translateY(-6px);box-shadow:0 18px 38px rgba(0,0,0,.10);border-color:var(--primary)}}
.product-link{{display:block;color:inherit}}
.product-img-wrap{{aspect-ratio:1/1;background:#f7f8fa;display:flex;align-items:center;justify-content:center;overflow:hidden;padding:18px}}
.product-img-wrap img{{max-width:100%;max-height:100%;object-fit:contain;transition:transform .4s}}
.product-card:hover .product-img-wrap img{{transform:scale(1.06)}}
.product-info{{padding:18px 20px 22px}}
.product-cat{{font-size:.75rem;font-weight:600;color:var(--primary);text-transform:uppercase;letter-spacing:1px;margin-bottom:8px}}
.product-title{{font-family:'Inter',sans-serif;font-size:1.02rem;font-weight:600;color:var(--dark);margin-bottom:12px;line-height:1.4;min-height:2.8em;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}}
.product-more{{font-size:.88rem;color:var(--primary);font-weight:600}}

/* ===== Modal ===== */
.modal-backdrop{{position:fixed;inset:0;background:rgba(14,26,43,.75);backdrop-filter:blur(4px);z-index:200;display:flex;align-items:center;justify-content:center;padding:20px;animation:fadeIn .25s}}
@keyframes fadeIn{{from{{opacity:0}}to{{opacity:1}}}}
.modal{{background:#fff;border-radius:14px;max-width:960px;width:100%;max-height:90vh;overflow:auto;box-shadow:0 30px 80px rgba(0,0,0,.4);animation:slideUp .3s}}
@keyframes slideUp{{from{{transform:translateY(20px);opacity:0}}to{{transform:translateY(0);opacity:1}}}}
.modal-grid{{display:grid;grid-template-columns:1fr 1fr;gap:0}}
.modal-img{{background:#f7f8fa;display:flex;align-items:center;justify-content:center;padding:30px;min-height:380px}}
.modal-img img{{max-width:100%;max-height:420px;object-fit:contain}}
.modal-body{{padding:36px}}
.modal-cat{{color:var(--primary);font-weight:600;font-size:.78rem;text-transform:uppercase;letter-spacing:1.5px;margin-bottom:10px}}
.modal-body h3{{font-size:1.7rem;margin-bottom:16px;color:var(--dark);font-family:'Playfair Display',serif}}
.modal-body p{{color:var(--text);margin-bottom:22px;line-height:1.7}}
.modal-specs{{margin:20px 0;border-top:1px solid var(--border);padding-top:18px}}
.modal-specs h4{{font-size:.92rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;color:var(--dark);margin-bottom:14px}}
.spec-row{{display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px dashed var(--border);font-size:.93rem}}
.spec-row:last-child{{border-bottom:none}}
.spec-key{{color:var(--muted);font-weight:500}}
.spec-val{{color:var(--dark);font-weight:600;text-align:right}}
.modal-close{{position:absolute;top:18px;right:18px;background:rgba(0,0,0,.55);color:#fff;border:none;width:38px;height:38px;border-radius:50%;font-size:20px;cursor:pointer;line-height:1;z-index:10;transition:background .2s}}
.modal-close:hover{{background:rgba(0,0,0,.85)}}
.modal-actions{{display:flex;gap:10px;flex-wrap:wrap;margin-top:24px}}

/* ===== Workshop / Exhibition Gallery ===== */
.gallery{{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}}
.gal-item{{background:#fff;border-radius:10px;overflow:hidden;box-shadow:0 4px 14px rgba(0,0,0,.06);transition:transform .3s}}
.gal-item:hover{{transform:translateY(-4px);box-shadow:0 14px 30px rgba(0,0,0,.10)}}
.gal-item img{{width:100%;aspect-ratio:4/3;object-fit:cover}}
.gal-item figcaption{{padding:12px 14px;font-size:.88rem;color:var(--dark);font-weight:500;text-align:center}}

/* ===== Why Us cards ===== */
.why-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:24px}}
.why-card{{background:#fff;padding:32px 24px;border-radius:12px;text-align:center;transition:all .3s;border:1px solid var(--border)}}
.why-card:hover{{transform:translateY(-6px);box-shadow:0 16px 30px rgba(0,0,0,.10);border-color:var(--primary)}}
.why-icon{{width:64px;height:64px;background:linear-gradient(135deg,var(--primary),var(--accent));border-radius:50%;display:inline-flex;align-items:center;justify-content:center;margin-bottom:18px;color:#fff;font-size:28px;font-weight:700}}
.why-card h3{{font-family:'Inter',sans-serif;font-size:1.1rem;margin-bottom:10px}}
.why-card p{{font-size:.92rem;color:var(--muted)}}

/* ===== Contact section ===== */
.contact-grid{{display:grid;grid-template-columns:1fr 1fr;gap:48px}}
.contact-info h2{{margin-bottom:20px}}
.contact-list{{list-style:none;margin-top:30px}}
.contact-list li{{display:flex;align-items:flex-start;gap:18px;padding:18px 0;border-bottom:1px solid rgba(255,255,255,.1)}}
.contact-list li:last-child{{border-bottom:none}}
.contact-icon{{flex:none;width:44px;height:44px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.15);border-radius:50%;display:flex;align-items:center;justify-content:center;color:var(--accent);font-size:18px}}
.contact-detail strong{{display:block;color:#fff;margin-bottom:4px;font-weight:600}}
.contact-detail a{{color:#bcc7d2}}
.contact-detail a:hover{{color:var(--accent)}}
.contact-form{{background:rgba(255,255,255,.05);padding:36px;border-radius:14px;border:1px solid rgba(255,255,255,.1)}}
.contact-form h3{{color:#fff;margin-bottom:8px;font-family:'Playfair Display',serif}}
.contact-form .sub{{color:#bcc7d2;margin-bottom:24px;font-size:.92rem}}
.contact-form input,.contact-form textarea{{width:100%;padding:13px 16px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.15);border-radius:8px;color:#fff;font-family:inherit;font-size:.95rem;margin-bottom:14px;transition:border-color .2s}}
.contact-form input:focus,.contact-form textarea:focus{{outline:none;border-color:var(--accent)}}
.contact-form input::placeholder,.contact-form textarea::placeholder{{color:#8da0b3}}
.contact-form button{{width:100%;padding:14px;background:var(--primary);color:#fff;border:none;border-radius:8px;font-weight:600;cursor:pointer;font-size:1rem;transition:background .2s}}
.contact-form button:hover{{background:var(--primary-dark)}}

/* ===== Footer ===== */
.footer{{background:#0a131f;color:#a0b0c0;padding:60px 0 0;font-size:.92rem}}
.footer-grid{{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:40px;margin-bottom:40px}}
.footer-brand img{{height:50px;margin-bottom:16px;filter:brightness(0) invert(1)}}
.footer-brand p{{color:#8da0b3;margin-bottom:20px;line-height:1.7}}
.footer h4{{color:#fff;font-family:'Inter',sans-serif;font-size:1rem;font-weight:600;margin-bottom:18px;letter-spacing:.5px}}
.footer ul{{list-style:none}}
.footer ul li{{margin-bottom:10px}}
.footer ul a{{color:#8da0b3;transition:color .2s}}
.footer ul a:hover{{color:var(--accent)}}
.footer-bottom{{border-top:1px solid #1a2738;padding:22px 0;text-align:center;color:#5e7185;font-size:.85rem}}
.social-row{{display:flex;gap:12px;margin-top:18px}}
.social-row a{{display:inline-flex;width:38px;height:38px;align-items:center;justify-content:center;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:50%;color:#fff;transition:all .2s}}
.social-row a:hover{{background:var(--primary);border-color:var(--primary);transform:translateY(-2px)}}

/* ===== Floating WhatsApp ===== */
.fab-wa{{position:fixed;bottom:24px;right:24px;width:60px;height:60px;background:#25D366;color:#fff;border-radius:50%;display:flex;align-items:center;justify-content:center;box-shadow:0 8px 24px rgba(37,211,102,.45);z-index:90;transition:all .25s;font-size:30px;text-decoration:none}}
.fab-wa:hover{{transform:scale(1.08);color:#fff}}

/* ===== Responsive ===== */
@media (max-width:980px){{
  .nav{{display:none;position:absolute;top:100%;left:0;right:0;background:#fff;flex-direction:column;padding:16px;box-shadow:0 6px 14px rgba(0,0,0,.1);gap:0}}
  .nav.open{{display:flex}}
  .nav a{{padding:12px 16px;width:100%}}
  .menu-btn{{display:flex}}
  .header-cta-desktop{{display:none}}
  .stats-bar{{grid-template-columns:repeat(2,1fr);padding:24px}}
  .product-grid{{grid-template-columns:repeat(2,1fr);gap:16px}}
  .gallery{{grid-template-columns:repeat(2,1fr)}}
  .why-grid{{grid-template-columns:repeat(2,1fr)}}
  .about-grid,.contact-grid{{grid-template-columns:1fr;gap:32px}}
  .modal-grid{{grid-template-columns:1fr}}
  .modal-img{{min-height:240px;padding:18px}}
  .modal-body{{padding:24px}}
  .footer-grid{{grid-template-columns:1fr 1fr;gap:30px}}
  .section{{padding:60px 0}}
  .hero-inner{{padding:60px 0 100px}}
  .topbar .tb-info{{justify-content:center;width:100%}}
}}
@media (max-width:560px){{
  .product-grid{{grid-template-columns:1fr 1fr;gap:12px}}
  .product-info{{padding:14px}}
  .product-title{{font-size:.92rem}}
  .gallery,.why-grid,.footer-grid{{grid-template-columns:1fr 1fr;gap:14px}}
  .stats-bar{{grid-template-columns:1fr 1fr;padding:20px;gap:14px}}
  .footer-grid{{grid-template-columns:1fr}}
}}
</style>
</head>
<body x-data="site()">

<!-- Top bar -->
<div class="topbar">
  <div class="container topbar-inner">
    <div class="tb-info">
      <span>📞 <a href="tel:{esc(co["phone"])}">{esc(co["phone"])}</a></span>
      <span>✉ <a href="mailto:{esc(co["email"])}">{esc(co["email"])}</a></span>
    </div>
    <div class="tb-info">
      <span>🌍 OEM/ODM Worldwide · Since {co["founded"]}</span>
    </div>
  </div>
</div>

<!-- Header -->
<header class="header">
  <div class="container header-inner">
    <a href="#home" class="logo">
      <img src="assets/logo.png" alt="{esc(co["name"])}" width="180" height="46">
      <div class="logo-text">
        <span class="logo-name">{esc(co["name"])}</span>
        <span class="logo-tag">Industrial Water Filtration</span>
      </div>
    </a>
    <nav class="nav" :class="{{open: mobileNav}}" @click="mobileNav=false">
      <a href="#home">Home</a>
      <a href="#products">Products</a>
      <a href="#about">About Us</a>
      <a href="#workshop">Workshop</a>
      <a href="#exhibition">Exhibitions</a>
      <a href="#contact">Contact</a>
    </nav>
    <a href="https://wa.me/{co["phone"].replace("-","").replace("+","")}" target="_blank" rel="noopener" class="cta cta-wa header-cta-desktop">
      WhatsApp Us
    </a>
    <button class="menu-btn" @click="mobileNav=!mobileNav" aria-label="Menu">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>

<!-- Hero -->
<section id="home" class="hero">
  <div class="hero-bg">
    <img src="assets/hero.jpg" alt="Water filtration manufacturing" fetchpriority="high">
  </div>
  <div class="container hero-inner">
    <span class="hero-eyebrow">✦ Trusted Water Filtration Manufacturer Since {co["founded"]}</span>
    <h1>Industrial-Grade Water Filtration Solutions</h1>
    <p>Specialized in PP, Carbon Block, GAC, T33, RO membranes, and water dispenser manufacturing. NSF · ISO · CE · Halal certified. OEM/ODM partners across 50+ countries.</p>
    <div class="hero-ctas">
      <a href="#products" class="cta">Explore Products</a>
      <a href="https://wa.me/{co["phone"].replace("-","").replace("+","")}" target="_blank" rel="noopener" class="cta btn-outline">Get a Quote</a>
    </div>
  </div>
</section>

<!-- Stats Bar -->
<div class="container">
  <div class="stats-bar">
    {stats_html}
  </div>
</div>

<!-- About Section -->
<section id="about" class="section">
  <div class="container">
    <div class="about-grid">
      <div class="about-img">
        <img loading="lazy" src="{esc(workshop[1]["url_local"])}" alt="Carbon Block Filter Production" width="600" height="450">
      </div>
      <div class="about-text">
        <span class="section-eyebrow">About Us</span>
        <h2>20+ Years of Water Filtration Excellence</h2>
        <p>{esc(co["about"])}</p>
        <ul class="about-feats">
          <li>Established in {co["founded"]} – Over two decades of manufacturing expertise</li>
          <li>Full vertical integration: R&D, Manufacturing, QC, Logistics</li>
          <li>NSF, ISO, CE, and Halal certified production lines</li>
          <li>OEM/ODM service for global brands across 50+ countries</li>
          <li>Located in Haining, Zhejiang – China's water filtration hub</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- Why Us -->
<section class="section bg-light">
  <div class="container">
    <div class="section-head">
      <span class="section-eyebrow">Why Choose Us</span>
      <h2>Trusted Manufacturing Partner</h2>
      <p>From raw materials to final inspection, every product passes our rigorous quality control system.</p>
    </div>
    <div class="why-grid">
      <div class="why-card">
        <div class="why-icon">✓</div>
        <h3>Certified Quality</h3>
        <p>NSF / ISO / CE / Halal certifications backed by every batch we produce.</p>
      </div>
      <div class="why-card">
        <div class="why-icon">⚙</div>
        <h3>OEM / ODM Ready</h3>
        <p>Custom branding, packaging, and product specifications to match your market.</p>
      </div>
      <div class="why-card">
        <div class="why-icon">🏭</div>
        <h3>In-House Production</h3>
        <p>4 dedicated production lines covering PP, Carbon, Quick-connect, and Leak Test.</p>
      </div>
      <div class="why-card">
        <div class="why-icon">🌐</div>
        <h3>Worldwide Shipping</h3>
        <p>Lead time 7–15 days with established export logistics to 50+ countries.</p>
      </div>
    </div>
  </div>
</section>

<!-- Products -->
<section id="products" class="section">
  <div class="container">
    <div class="section-head">
      <span class="section-eyebrow">Our Products</span>
      <h2>Complete Water Filtration Portfolio</h2>
      <p>{len(products)} models across {len(categories)} categories – from inline cartridges to vertical dispensers and complete RO systems.</p>
    </div>

    <div class="cat-filter">
      {cat_buttons()}
    </div>

    <div class="product-grid">
      <template x-for="p in filteredProducts" :key="p.id">
        <div class="product-card">
          <div class="product-link" @click="openProduct(p.id)">
            <div class="product-img-wrap">
              <img loading="lazy" decoding="async" :src="p.image" :alt="p.name" width="400" height="400">
            </div>
            <div class="product-info">
              <div class="product-cat" x-text="p.category"></div>
              <h3 class="product-title" x-text="p.name"></h3>
              <span class="product-more">View Details &rarr;</span>
            </div>
          </div>
        </div>
      </template>
    </div>
  </div>
</section>

<!-- Workshop -->
<section id="workshop" class="section bg-light">
  <div class="container">
    <div class="section-head">
      <span class="section-eyebrow">Manufacturing</span>
      <h2>Inside Our Workshop</h2>
      <p>4 specialized production lines: PP filter, Carbon block, Quick-connect inline, and Automatic leak detection.</p>
    </div>
    <div class="gallery">
      {workshop_html}
    </div>
  </div>
</section>

<!-- Exhibition -->
<section id="exhibition" class="section">
  <div class="container">
    <div class="section-head">
      <span class="section-eyebrow">Trade Shows</span>
      <h2>Global Exhibitions</h2>
      <p>Meet our team at AquaTech Shanghai and other major industry events.</p>
    </div>
    <div class="gallery">
      {exhibition_html}
    </div>
  </div>
</section>

<!-- Contact -->
<section id="contact" class="section bg-dark">
  <div class="container">
    <div class="contact-grid">
      <div class="contact-info">
        <span class="section-eyebrow">Get in Touch</span>
        <h2>Let's Build Together</h2>
        <p>Tell us about your project. Our sales engineers respond within 24 hours.</p>
        <ul class="contact-list">
          <li>
            <div class="contact-icon">📍</div>
            <div class="contact-detail">
              <strong>Factory Address</strong>
              {esc(co["factory_address"])}
            </div>
          </li>
          <li>
            <div class="contact-icon">📞</div>
            <div class="contact-detail">
              <strong>Phone / WhatsApp</strong>
              <a href="tel:{esc(co["phone"])}">{esc(co["phone"])}</a>
            </div>
          </li>
          <li>
            <div class="contact-icon">✉</div>
            <div class="contact-detail">
              <strong>Email</strong>
              <a href="mailto:{esc(co["email"])}">{esc(co["email"])}</a>
            </div>
          </li>
        </ul>
      </div>
      <form class="contact-form" onsubmit="event.preventDefault(); window.open('https://wa.me/{co["phone"].replace("-","").replace("+","")}?text=' + encodeURIComponent('Hi, I am ' + this.name.value + ' (' + this.email.value + '). ' + this.msg.value),'_blank');">
        <h3>Send an Inquiry</h3>
        <p class="sub">We respond within 24 hours.</p>
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <input type="text" name="company" placeholder="Company Name (optional)">
        <textarea name="msg" rows="4" placeholder="Tell us what you need..." required></textarea>
        <button type="submit">Send via WhatsApp →</button>
      </form>
    </div>
  </div>
</section>

<!-- Footer -->
<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <img src="assets/logo.png" alt="{esc(co["name"])}" width="200" height="50">
        <p>Trusted manufacturer of water filtration solutions since {co["founded"]}. PP, Carbon Block, GAC, T33, RO membranes, and water dispensers for global OEM/ODM partners.</p>
        <div class="social-row">
          <a href="https://wa.me/{co["phone"].replace("-","").replace("+","")}" target="_blank" rel="noopener" aria-label="WhatsApp">💬</a>
          <a href="mailto:{esc(co["email"])}" aria-label="Email">✉</a>
          <a href="tel:{esc(co["phone"])}" aria-label="Phone">📞</a>
        </div>
      </div>
      <div>
        <h4>Products</h4>
        <ul>
          <li><a href="#products" @click="filter='Water Dispenser'">Water Dispensers</a></li>
          <li><a href="#products" @click="filter='Filter Cartridge'">Filter Cartridges</a></li>
          <li><a href="#products" @click="filter='Inline Filter'">Inline Filters</a></li>
          <li><a href="#products" @click="filter='RO System'">RO Systems</a></li>
          <li><a href="#products" @click="filter='Industrial Filter'">Industrial Filters</a></li>
        </ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="#about">About Us</a></li>
          <li><a href="#workshop">Workshop</a></li>
          <li><a href="#exhibition">Exhibitions</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li>{esc(co["factory_address"])}</li>
          <li><a href="tel:{esc(co["phone"])}">{esc(co["phone"])}</a></li>
          <li><a href="mailto:{esc(co["email"])}">{esc(co["email"])}</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      © {co["founded"]}–2026 {esc(co["name"])}. All rights reserved. | Industrial Water Filtration Manufacturer | Haining, China
    </div>
  </div>
</footer>

<!-- Floating WhatsApp -->
<a class="fab-wa" href="https://wa.me/{co["phone"].replace("-","").replace("+","")}" target="_blank" rel="noopener" aria-label="WhatsApp Chat">💬</a>

<!-- Modal -->
<template x-if="modalProduct">
  <div class="modal-backdrop" @click.self="modalProduct=null">
    <div class="modal" style="position:relative">
      <button class="modal-close" @click="modalProduct=null" aria-label="Close">×</button>
      <div class="modal-grid">
        <div class="modal-img">
          <img :src="modalProduct.image" :alt="modalProduct.name">
        </div>
        <div class="modal-body">
          <div class="modal-cat" x-text="modalProduct.category"></div>
          <h3 x-text="modalProduct.name"></h3>
          <p x-text="modalProduct.desc"></p>
          <div class="modal-specs" x-show="Object.keys(modalProduct.specs).length > 0">
            <h4>Specifications</h4>
            <template x-for="(v, k) in modalProduct.specs" :key="k">
              <div class="spec-row">
                <span class="spec-key" x-text="k"></span>
                <span class="spec-val" x-text="v"></span>
              </div>
            </template>
          </div>
          <div class="modal-actions">
            <a :href="'https://wa.me/{co["phone"].replace("-","").replace("+","")}?text=' + encodeURIComponent('Hi, I am interested in ' + modalProduct.name)" target="_blank" rel="noopener" class="cta cta-wa">Inquire on WhatsApp</a>
            <a :href="'mailto:{esc(co["email"])}?subject=Inquiry: ' + encodeURIComponent(modalProduct.name)" class="cta">Email Us</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
const PRODUCTS_DATA = {products_json};
function site() {{
  return {{
    filter: 'all',
    mobileNav: false,
    modalProduct: null,
    products: PRODUCTS_DATA,
    get filteredProducts() {{
      if (this.filter === 'all') return this.products;
      return this.products.filter(p => p.category === this.filter);
    }},
    openProduct(id) {{
      this.modalProduct = this.products.find(p => p.id === id);
      document.body.style.overflow = 'hidden';
    }},
    init() {{
      this.$watch('modalProduct', v => {{
        document.body.style.overflow = v ? 'hidden' : '';
      }});
    }}
  }}
}}
</script>
<script defer src="assets/alpine.min.js"></script>

</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(HTML)

# Versioned backup
import os
backup_name = f"index.{VERSION}.html"
with open(backup_name, "w", encoding="utf-8") as f:
    f.write(HTML)

print(f"Generated index.html ({len(HTML)} chars)")
print(f"Versioned backup: {backup_name}")
print(f"Products: {len(products)}, Categories: {len(categories)}")
