import json
import os

# Define the 38 languages and their native names
languages = {
    "EN": "English", "AR": "العربية", "ES": "Español", "FR": "Français", "DE": "Deutsch",
    "RU": "Русский", "PT": "Português", "JA": "日本語", "KO": "한국어", "IT": "Italiano",
    "TR": "Türkçe", "HI": "हिन्दी", "BN": "বাংলা", "ID": "Bahasa Indonesia", "VI": "Tiếng Việt",
    "TH": "ไทย", "PL": "Polski", "NL": "Nederlands", "FA": "فارسی", "UR": "اردو",
    "MS": "Bahasa Melayu", "TL": "Tagalog", "HE": "עبري", "EL": "Ελληνικά", "CS": "Čeština",
    "HU": "Magyar", "RO": "Română", "SV": "Svenska", "DA": "Dansk", "FI": "Suomi",
    "NO": "Norsk", "UK": "Українська", "BG": "Български", "HR": "Hrvatski", "SR": "Srpski",
    "SK": "Slovenčina", "SL": "Slovenščina", "LT": "Lietuvių"
}

# Load the solar translations
with open('solar_translations/solar_translations_38.json', 'r', encoding='utf-8') as f:
    translations = json.load(f)

# Template replicating the ORIGINAL look of solarwaterheatermachinery.com
# Header: Dark Grey #232323, Button/Accent: Red #e60012
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
        .hero {{ height: 550px; background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), url('http://www.solarwaterheatermachinery.com/wp-content/uploads/2021/10/IMG_0963.jpg-%E6%8B%B7%E8%B4%9D-scaled.jpg'); background-size: cover; background-position: center; display: flex; flex-direction: column; justify-content: center; align-items: center; color: #fff; text-align: center; padding: 0 10%; }}
        .hero h1 {{ font-size: 3.5rem; margin-bottom: 25px; font-weight: 900; text-shadow: 2px 2px 10px rgba(0,0,0,0.5); }}
        .hero p {{ font-size: 1.2rem; margin-bottom: 35px; max-width: 800px; line-height: 1.6; }}
        .btn {{ background: #e60012; color: #fff; padding: 15px 35px; text-decoration: none; font-weight: 800; border-radius: 2px; border: none; cursor: pointer; text-transform: uppercase; transition: 0.3s; }}
        .btn:hover {{ background: #c00; transform: translateY(-2px); }}
        section {{ padding: 90px 10%; }}
        .section-title {{ font-size: 2.2rem; font-weight: 800; border-left: 6px solid #e60012; padding-left: 20px; margin-bottom: 45px; text-transform: uppercase; color: #232323; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 40px; }}
        .card {{ border: 1px solid #eee; padding: 0; transition: 0.4s; background: #fff; }}
        .card:hover {{ box-shadow: 0 15px 35px rgba(0,0,0,0.1); transform: translateY(-5px); }}
        .card-img {{ width: 100%; height: 240px; overflow: hidden; }}
        .card-img img {{ width: 100%; height: 100%; object-fit: cover; transition: 0.5s; }}
        .card:hover .card-img img {{ transform: scale(1.1); }}
        .card-body {{ padding: 25px; }}
        .card h3 {{ color: #232323; margin: 0 0 15px 0; font-size: 1.4rem; font-weight: 700; }}
        .card p {{ font-size: 0.95rem; color: #666; line-height: 1.6; margin-bottom: 20px; }}
        .card a {{ color: #e60012; font-weight: 800; text-decoration: none; font-size: 13px; text-transform: uppercase; }}
        .imu-section {{ background: #232323; color: #fff; text-align: center; }}
        .imu-section p {{ max-width: 800px; margin: 0 auto 40px; opacity: 0.8; }}
        .contact-grid {{ display: grid; grid-template-columns: 1fr 1.2fr; gap: 70px; }}
        .contact-info p {{ margin-bottom: 20px; font-size: 1rem; color: #555; }}
        .contact-info i {{ color: #e60012; width: 30px; }}
        .contact-form input, .contact-form textarea {{ width: 100%; padding: 15px; margin-bottom: 20px; border: 1px solid #ddd; background: #f9f9f9; outline: none; }}
        .contact-form input:focus, .contact-form textarea:focus {{ border-color: #e60012; }}
        footer {{ background: #111; color: #666; padding: 50px 10%; text-align: center; font-size: 13px; border-top: 1px solid #222; }}
        [dir="rtl"] .section-title {{ border-left: none; border-right: 6px solid #e60012; padding-left: 0; padding-right: 20px; text-align: right; }}
        [dir="rtl"] .logo img {{ margin-right: 0; margin-left: 12px; }}
        [dir="rtl"] .hero, [dir="rtl"] section, [dir="rtl"] footer {{ text-align: right; }}
        [dir="rtl"] .hero {{ text-align: center; }}
        [dir="rtl"] .contact-grid {{ text-align: right; }}
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
            <a href="#products">{nav_products}</a>
            <select onchange="window.location.href='/'+this.value+'/index.html'" style="background:#333; color:#fff; border:1px solid #444; padding:6px 10px; font-size:12px; font-weight:700; cursor:pointer;">
                {lang_options}
            </select>
        </nav>
    </header>

    <div class="hero" id="home">
        <h1>{hero_h1}</h1>
        <p>{hero_p}</p>
        <a href="#contact" class="btn">{btn_contact}</a>
    </div>

    <section id="about">
        <h2 class="section-title">{about_h2}</h2>
        <div style="display:flex; gap:60px; align-items:center; flex-wrap:wrap;">
            <div style="flex:1; min-width:400px;">
                <p style="font-size:1.1rem; line-height:1.8; color:#555;">{about_p}</p>
                <div style="margin-top:30px; display:flex; gap:30px;">
                    <div><b style="color:#232323; font-size:1.5rem;">25+</b><p style="font-size:12px; color:#999; margin:0;">YEARS EXP</p></div>
                    <div><b style="color:#232323; font-size:1.5rem;">50+</b><p style="font-size:12px; color:#999; margin:0;">COUNTRIES</p></div>
                </div>
            </div>
            <div style="flex:1; min-width:400px;">
                <img src="https://www.solarwaterheatermachinery.com/wp-content/uploads/2021/10/E578D664-9460-43AE-B871-E28522213316-1608-000002AB870E91F9_tmp-1-1024x683.jpg" style="width:100%; box-shadow: 20px 20px 0 #f4f4f4;">
            </div>
        </div>
    </section>

    <section id="products" style="background:#fcfcfc;">
        <div style="text-align:center; margin-bottom:60px;">
            <h2 style="font-size:2.5rem; font-weight:900; text-transform:uppercase; margin-bottom:10px;">{prod_h2}</h2>
            <div style="width:60px; height:4px; background:#e60012; margin:0 auto;"></div>
        </div>
        <div class="grid">
            <div class="card">
                <div class="card-img"><img src="https://www.solarwaterheatermachinery.com/wp-content/uploads/2021/10/IMG_0269-1.jpg"></div>
                <div class="card-body">
                    <h3>{prod_1}</h3>
                    <p>{prod_1_desc}</p>
                    <a href="#contact">INQUIRE NOW →</a>
                </div>
            </div>
            <div class="card">
                <div class="card-img"><img src="http://www.solarwaterheatermachinery.com/wp-content/uploads/2021/10/IMG_0963.jpg-%E6%8B%B7%E8%B4%9D-scaled.jpg"></div>
                <div class="card-body">
                    <h3>{prod_4}</h3>
                    <p>{prod_4_desc}</p>
                    <a href="#contact">INQUIRE NOW →</a>
                </div>
            </div>
            <div class="card">
                <div class="card-img"><img src="http://www.solarwaterheatermachinery.com/wp-content/uploads/2021/10/IMG_0963.jpg-%E6%8B%B7%E8%B4%9D-scaled.jpg"></div>
                <div class="card-body">
                    <h3>{prod_3}</h3>
                    <p>{prod_3_desc}</p>
                    <a href="#contact">INQUIRE NOW →</a>
                </div>
            </div>
        </div>
    </section>

    <section class="imu-section" id="imu">
        <h2 style="font-size:2.5rem; margin-bottom:20px;">{imu_h2}</h2>
        <p>{imu_p}</p>
        <div style="padding:50px;">
            <i class="fas fa-microchip" style="font-size:120px; color:#e60012; opacity:0.8;"></i>
        </div>
    </section>

    <section id="contact">
        <h2 class="section-title">{contact_h2}</h2>
        <div class="contact-grid">
            <div class="contact-info">
                <p>{contact_p}</p>
                <p><i class="fas fa-map-marker-alt"></i> <b>China Factory:</b> #1 Chuangxin Road, Haining, Zhejiang</p>
                <p><i class="fab fa-whatsapp"></i> <b>WhatsApp:</b> +86-19908311885</p>
                <p><i class="fas fa-envelope"></i> <b>Email:</b> info@solarwaterheatermachinery.com</p>
                <div style="margin-top:40px;">
                    <img src="https://www.solarwaterheatermachinery.com/wp-content/uploads/2021/10/cropped-Screen-Shot-2021-01-01-at-8.56.14-PM-1-120x40.png" style="height:30px; filter: grayscale(1); opacity:0.5;">
                </div>
            </div>
            <div class="contact-form">
                <input type="text" placeholder="Name">
                <input type="email" placeholder="Business Email">
                <textarea rows="5" placeholder="Project Requirements (Capacity, Location, etc.)"></textarea>
                <button class="btn" style="width:100%; border-radius:0;">SEND PROPOSAL REQUEST</button>
            </div>
        </div>
    </section>

    <footer>{footer}</footer>
</body>
</html>
"""

# Generate files
for lang_code, trans in translations.items():
    l_code = lang_code.lower()
    os.makedirs(l_code, exist_ok=True)
    
    direction = "rtl" if lang_code in ["AR", "FA", "UR", "HE"] else "ltr"
    
    lang_options = ""
    for lc, name in languages.items():
        selected = "selected" if lc == lang_code else ""
        lang_options += f'<option value="{lc.lower()}" {selected}>{name} ({lc})</option>'
    
    # Safely get translations with fallback
    def g(key, default=""):
        return trans.get(key, default)

    content = template.format(
        lang_code=l_code,
        direction=direction,
        site_title=g('site_title'),
        nav_home=g('nav_home', 'Home'),
        nav_about=g('nav_about', 'About'),
        nav_products=g('nav_products', 'Products'),
        lang_options=lang_options,
        hero_h1=g('hero_title'),
        hero_p=g('hero_sub'),
        btn_contact=g('hero_cta2', 'Contact Us'),
        about_h2=g('about_title', 'About Us'),
        about_p=g('about_p1'),
        prod_h2=g('nav_products', 'Products'),
        prod_1=g('prod_1_title'),
        prod_1_desc=g('prod_1_desc'),
        prod_3=g('prod_3_title'),
        prod_3_desc=g('prod_3_desc'),
        prod_4=g('prod_4_title'),
        prod_4_desc=g('prod_4_desc'),
        imu_h2=g('imu_title', 'IMU Tech'),
        imu_p=g('imu_desc'),
        contact_h2=g('contact_title', 'Contact'),
        contact_p=g('contact_sub'),
        footer=g('footer_copy', '© Metatecno')
    )
    
    with open(f"{l_code}/index.html", "w", encoding="utf-8") as f:
        f.write(content)

# Root redirect
with open("index.html", "w", encoding="utf-8") as f:
    f.write('<script>window.location.href="/en/index.html";</script>')

print("Metatecno Solar 38-language Replica Site Fixed and Generated.")
