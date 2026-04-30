import json
import os

# Define languages and native names
languages = {
    "EN": "English", "AR": "العربية", "ES": "Español", "FR": "Français", "DE": "Deutsch",
    "RU": "Русский", "PT": "Português", "JA": "日本語", "KO": "한국어", "IT": "Italiano",
    "TR": "Türkçe", "HI": "हिन्दी", "BN": "বাংলা", "ID": "Bahasa Indonesia", "VI": "Tiếng Việt",
    "TH": "ไทย", "PL": "Polski", "NL": "Nederlands", "FA": "فارسی", "UR": "اردو",
    "MS": "Bahasa Melayu", "TL": "Tagalog", "HE": "עברית", "EL": "Ελληνικά", "CS": "Čeština",
    "HU": "Magyar", "RO": "Română", "SV": "Svenska", "DA": "Dansk", "FI": "Suomi",
    "NO": "Norsk", "UK": "Українська", "BG": "Български", "HR": "Hrvatski", "SR": "Srpski",
    "SK": "Slovenčina", "SL": "Slovenščina", "LT": "Lietuvių"
}

# Load basic and detailed translations
with open('multi_lang_data/translations_38.json', 'r', encoding='utf-8') as f:
    basic_trans = json.load(f)

with open('detailed_translations/detailed_translations_38.json', 'r', encoding='utf-8') as f:
    detailed_trans = json.load(f)

# Combine translations
for lang in basic_trans:
    if lang in detailed_trans:
        basic_trans[lang].update(detailed_trans[lang])

# Template for detailed replica site
template = """<!DOCTYPE html>
<html lang="{lang_code}" dir="{direction}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{site_title}</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        body {{ font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; margin: 0; padding: 0; background: #fff; color: #333; }}
        header {{ background: #232323; color: #fff; padding: 15px 5%; display: flex; justify-content: space-between; align-items: center; position: sticky; top: 0; z-index: 1000; border-bottom: 3px solid #e60012; }}
        .logo {{ font-size: 1.6rem; font-weight: 800; display: flex; align-items: center; text-transform: uppercase; letter-spacing: 1px; }}
        .logo img {{ height: 40px; margin-right: 12px; background: #fff; padding: 3px; border-radius: 2px; }}
        nav {{ display: flex; gap: 25px; align-items: center; }}
        nav a {{ color: #fff; text-decoration: none; font-size: 13px; text-transform: uppercase; font-weight: 700; transition: 0.3s; }}
        nav a:hover {{ color: #e60012; }}
        .hero {{ height: 500px; background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), url('http://www.solarwaterheatermachinery.com/wp-content/uploads/2021/10/IMG_0963.jpg-%E6%8B%B7%E8%B4%9D-scaled.jpg'); background-size: cover; background-position: center; display: flex; flex-direction: column; justify-content: center; align-items: center; color: #fff; text-align: center; padding: 0 10%; }}
        .hero h1 {{ font-size: 3.5rem; margin-bottom: 25px; font-weight: 900; }}
        .btn {{ background: #e60012; color: #fff; padding: 15px 35px; text-decoration: none; font-weight: 800; border-radius: 2px; border: none; cursor: pointer; text-transform: uppercase; }}
        section {{ padding: 80px 10%; }}
        .section-title {{ font-size: 2.2rem; font-weight: 800; border-left: 6px solid #e60012; padding-left: 20px; margin-bottom: 45px; text-transform: uppercase; }}
        .product-box {{ border: 1px solid #eee; margin-bottom: 60px; padding: 40px; border-radius: 8px; background: #fafafa; }}
        .product-box h3 {{ font-size: 1.8rem; margin-top: 0; color: #232323; border-bottom: 2px solid #e60012; padding-bottom: 10px; display: inline-block; }}
        .product-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 40px; margin-top: 30px; }}
        .product-info {{ line-height: 1.7; color: #555; }}
        .spec-table {{ width: 100%; border-collapse: collapse; margin-top: 20px; font-size: 14px; background: #fff; }}
        .spec-table th, .spec-table td {{ border: 1px solid #ddd; padding: 12px; text-align: left; }}
        .spec-table th {{ background: #eee; color: #333; }}
        footer {{ background: #111; color: #666; padding: 50px 10%; text-align: center; font-size: 13px; }}
        [dir="rtl"] .section-title {{ border-left: none; border-right: 6px solid #e60012; padding-left: 0; padding-right: 20px; }}
        [dir="rtl"] .spec-table th, [dir="rtl"] .spec-table td {{ text-align: right; }}
    </style>
</head>
<body>
    <header>
        <div class="logo">
            <img src="https://www.solarwaterheatermachinery.com/wp-content/uploads/2021/10/cropped-Screen-Shot-2021-01-01-at-8.56.14-PM-1-120x40.png" alt="Metatecno">
            META<span style="color:#e60012">TECNO</span>
        </div>
        <nav>
            <a href="#home">{nav_home}</a>
            <a href="#about">{nav_about}</a>
            <a href="#products">{nav_solutions}</a>
            <select onchange="window.location.href='/'+this.value+'/index.html'" style="background:#333; color:#fff; border:1px solid #444; padding:6px 10px; font-size:12px; font-weight:700;">
                {lang_options}
            </select>
        </nav>
    </header>

    <div class="hero" id="home">
        <h1>{hero_title}</h1>
        <p>{hero_sub}</p>
        <a href="#contact" class="btn">{hero_cta2}</a>
    </div>

    <section id="about">
        <h2 class="section-title">{about_title}</h2>
        <div style="display:flex; gap:60px; align-items:center; flex-wrap:wrap;">
            <div style="flex:1; min-width:400px;">
                <p style="font-size:1.1rem; line-height:1.8; color:#555;">{about_p1}</p>
            </div>
            <img src="https://www.solarwaterheatermachinery.com/wp-content/uploads/2021/10/E578D664-9460-43AE-B871-E28522213316-1608-000002AB870E91F9_tmp-1-1024x683.jpg" style="width:100%; max-width:500px; border-radius:8px;">
        </div>
    </section>

    <section id="products">
        <h2 class="section-title">{nav_solutions}</h2>
        
        <!-- Enamel Tank Line -->
        <div class="product-box">
            <h3>{prod_1_title}</h3>
            <div class="product-grid">
                <div class="product-info">
                    <p>{detail_1}</p>
                </div>
                <img src="https://www.solarwaterheatermachinery.com/wp-content/uploads/2021/10/IMG_0269-1.jpg" style="width:100%; border-radius:4px;">
            </div>
        </div>

        <!-- SWH Line -->
        <div class="product-box">
            <h3>{prod_4_title}</h3>
            <div class="product-grid">
                <div class="product-info">
                    <p>{detail_2}</p>
                </div>
                <img src="http://www.solarwaterheatermachinery.com/wp-content/uploads/2021/10/IMG_0963.jpg-%E6%8B%B7%E8%B4%9D-scaled.jpg" style="width:100%; border-radius:4px;">
            </div>
        </div>

        <!-- PV Mounting -->
        <div class="product-box">
            <h3>{prod_5_title}</h3>
            <div class="product-info">
                <p>{detail_5}</p>
            </div>
        </div>

        <!-- IMU Sensor -->
        <div class="product-box">
            <h3>{imu_title}</h3>
            <div class="product-info">
                <p>{detail_6}</p>
            </div>
        </div>
    </section>

    <section id="contact">
        <h2 class="section-title">{contact_title}</h2>
        <div style="display:grid; grid-template-columns: 1fr 1.5fr; gap:50px;">
            <div>
                <p>{contact_sub}</p>
                <p><b>China:</b> #1 Chuangxin Road, Haining, China</p>
                <p><b>WhatsApp:</b> +86-19908311885</p>
                <p><b>Email:</b> info@solarwaterheatermachinery.com</p>
            </div>
            <div class="contact-form" style="display:flex; flex-direction:column; gap:20px;">
                <input type="text" placeholder="Name" style="padding:15px; border:1px solid #ddd;">
                <input type="email" placeholder="Email" style="padding:15px; border:1px solid #ddd;">
                <textarea rows="5" placeholder="Message" style="padding:15px; border:1px solid #ddd;"></textarea>
                <button class="btn">Send Request</button>
            </div>
        </div>
    </section>

    <footer>{footer_copy}</footer>
</body>
</html>
"""

# Generate 38 files
for lang, data in basic_trans.items():
    l_code = lang.lower()
    os.makedirs(l_code, exist_ok=True)
    direction = "rtl" if lang in ["AR", "FA", "UR", "HE"] else "ltr"
    
    # Lang options
    lang_options = ""
    for lc, name in languages.items():
        selected = "selected" if lc == lang else ""
        lang_options += f'<option value="{lc.lower()}" {selected}>{name} ({lc})</option>'
    
    # Safe data retrieval
    def g(key, default=""): return data.get(key, default)

    content = template.format(
        lang_code=l_code,
        direction=direction,
        site_title=g('site_title'),
        nav_home=g('nav_home', 'Home'),
        nav_about=g('nav_about', 'About'),
        nav_solutions=g('nav_solutions', 'Products'),
        lang_options=lang_options,
        hero_title=g('hero_title'),
        hero_sub=g('hero_sub'),
        hero_cta2=g('hero_cta2', 'Contact Us'),
        about_title=g('about_title', 'About Us'),
        about_p1=g('about_p1'),
        prod_1_title=g('prod_1_title'),
        detail_1=g('1. Enamel Tank Line') or g('prod_1_title'),
        prod_4_title=g('prod_4_title'),
        detail_2=g('2. Solar Water Heater (SWH) Line') or g('prod_4_title'),
        prod_5_title=g('prod_5_title'),
        detail_5=g('5. PV Mounting Structure') or g('prod_5_title'),
        imu_title=g('imu_title'),
        detail_6=g('6. IMU Sensor System') or g('imu_title'),
        contact_title=g('contact_title'),
        contact_sub=g('contact_sub'),
        footer_copy=g('footer_copy', '© Metatecno'),
    )
    
    with open(f"{l_code}/index.html", "w", encoding="utf-8") as f:
        f.write(content)

# Root redirect
with open("index.html", "w", encoding="utf-8") as f:
    f.write('<script>window.location.href="/en/index.html";</script>')

print("38-language Detailed Site Generated.")
