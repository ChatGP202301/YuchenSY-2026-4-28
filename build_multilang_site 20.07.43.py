import json
import os

# Load translations
with open('multi_lang_data/translations_38.json', 'r', encoding='utf-8') as f:
    translations = json.load(f)

# Language list for switcher
langs = sorted(translations.keys())
lang_names = {
    "EN": "English (EN)", "AR": "العربية (AR)", "ES": "Español (ES)", "FR": "Français (FR)", 
    "DE": "Deutsch (DE)", "RU": "Русский (RU)", "PT": "Português (PT)", "JA": "日本語 (JA)", 
    "KO": "한국어 (KO)", "IT": "Italiano (IT)", "TR": "Türkçe (TR)", "HI": "हिन्दी (HI)", 
    "BN": "বাংলা (BN)", "ID": "Bahasa Indonesia (ID)", "VI": "Tiếng Việt (VI)", "TH": "ไทย (TH)", 
    "PL": "Polski (PL)", "NL": "Nederlands (NL)", "FA": "فارسی (FA)", "UR": "اردو (UR)", 
    "MS": "Bahasa Melayu (MS)", "TL": "Tagalog (TL)", "HE": "עברית (HE)", "EL": "Ελληνικά (EL)", 
    "CS": "Čeština (CS)", "HU": "Magyar (HU)", "RO": "Română (RO)", "SV": "Svenska (SV)", 
    "DA": "Dansk (DA)", "FI": "Suomi (FI)", "NO": "Norsk (NO)", "UK": "Українська (UK)", 
    "BG": "Български (BG)", "HR": "Hrvatski (HR)", "SR": "Srpski (SR)", "SK": "Slovenčina (SK)", 
    "SL": "Slovenščina (SL)", "LT": "Lietuvių (LT)"
}

# Template for the v7 Modern Industrial design
template = """<!DOCTYPE html>
<html lang="{lang_lower}" dir="{direction}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{site_title}</title>
    <meta name="description" content="{meta_desc}">
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Lexend:wght@300;400;500;700;900&family=Inter:wght@300;400;600&display=swap');
        :root {{ --brand-cobalt: #2563eb; --brand-slate: #334155; }}
        body {{ font-family: 'Inter', sans-serif; color: var(--brand-slate); background-color: #ffffff; }}
        h1, h2, h3, h4 {{ font-family: 'Lexend', sans-serif; color: #0f172a; }}
        .glass-nav {{ background: rgba(255, 255, 255, 0.85); backdrop-filter: blur(12px); }}
        .btn-primary {{ background-color: var(--brand-cobalt); transition: all 0.3s ease; }}
        .card-modern {{ background: #ffffff; border: 1px solid #f1f5f9; transition: all 0.4s ease; }}
        .card-modern:hover {{ transform: translateY(-5px); border-color: var(--brand-cobalt); }}
        html {{ scroll-behavior: smooth; }}
    </style>
</head>
<body class="antialiased">
    <nav class="fixed top-0 w-full z-[100] glass-nav border-b border-slate-100">
        <div class="container mx-auto px-6 h-20 flex justify-between items-center">
            <a href="#" class="flex items-center space-x-3">
                <img src="https://www.solarwaterheatermachinery.com/wp-content/uploads/2021/10/cropped-Screen-Shot-2021-01-01-at-8.56.14-PM-1-120x40.png" alt="Logo" class="h-8">
                <span class="text-xl font-black text-slate-900 uppercase">Metatecno</span>
            </a>
            <div class="hidden lg:flex items-center space-x-8 text-[13px] font-semibold text-slate-600 uppercase">
                <a href="#home">{nav_home}</a>
                <a href="#about">{nav_company}</a>
                <a href="#solutions">{nav_solutions}</a>
                <a href="#contact">{nav_contact}</a>
                <select class="bg-transparent border-none focus:ring-0 cursor-pointer" onchange="window.location.href=this.value">
                    {lang_options}
                </select>
            </div>
        </div>
    </nav>

    <section id="home" class="min-h-screen flex items-center pt-20 bg-slate-50">
        <div class="container mx-auto px-6 grid lg:grid-cols-2 gap-16 items-center">
            <div>
                <h1 class="text-5xl md:text-7xl font-black mb-8 text-slate-900 leading-tight">{hero_title}</h1>
                <p class="text-lg text-slate-500 mb-12">{hero_sub}</p>
                <div class="flex gap-4">
                    <a href="#solutions" class="px-10 py-4 bg-blue-600 text-white font-bold rounded-xl btn-primary">{hero_cta1}</a>
                    <a href="#contact" class="px-10 py-4 border border-slate-200 text-slate-900 font-bold rounded-xl hover:bg-white">{hero_cta2}</a>
                </div>
            </div>
            <img src="http://www.solarwaterheatermachinery.com/wp-content/uploads/2021/10/IMG_0963.jpg-%E6%8B%B7%E8%B4%9D-scaled.jpg" class="rounded-3xl shadow-2xl">
        </div>
    </section>

    <section id="about" class="py-32 bg-white">
        <div class="container mx-auto px-6 grid lg:grid-cols-2 gap-20 items-center">
            <div>
                <h2 class="text-4xl font-black mb-8">{about_title}</h2>
                <p class="text-slate-500 mb-6">{about_p1}</p>
                <p class="text-slate-500">{about_p2}</p>
            </div>
            <img src="https://www.solarwaterheatermachinery.com/wp-content/uploads/2021/10/E578D664-9460-43AE-B871-E28522213316-1608-000002AB870E91F9_tmp-1-1024x683.jpg" class="rounded-3xl">
        </div>
    </section>

    <section id="solutions" class="py-32 bg-slate-50">
        <div class="container mx-auto px-6">
            <h2 class="text-center text-4xl font-black mb-20">{nav_solutions}</h2>
            <div class="grid md:grid-cols-3 gap-8">
                <div class="p-10 card-modern rounded-3xl">
                    <h4 class="text-xl font-bold mb-4">{prod_1_title}</h4>
                    <p class="text-slate-500 text-sm">{prod_1_desc}</p>
                </div>
                <div class="p-10 card-modern rounded-3xl">
                    <h4 class="text-xl font-bold mb-4">{prod_2_title}</h4>
                    <p class="text-slate-500 text-sm">{prod_2_desc}</p>
                </div>
                <div class="p-10 card-modern rounded-3xl">
                    <h4 class="text-xl font-bold mb-4">{prod_3_title}</h4>
                    <p class="text-slate-500 text-sm">{prod_3_desc}</p>
                </div>
                <div class="p-10 card-modern rounded-3xl">
                    <h4 class="text-xl font-bold mb-4">{prod_4_title}</h4>
                    <p class="text-slate-500 text-sm">{prod_4_desc}</p>
                </div>
                <div class="p-10 card-modern rounded-3xl">
                    <h4 class="text-xl font-bold mb-4">{prod_5_title}</h4>
                    <p class="text-slate-500 text-sm">{prod_5_desc}</p>
                </div>
                <div class="p-10 card-modern rounded-3xl">
                    <h4 class="text-xl font-bold mb-4">{prod_6_title}</h4>
                    <p class="text-slate-500 text-sm">{prod_6_desc}</p>
                </div>
            </div>
        </div>
    </section>

    <section id="contact" class="py-32 bg-slate-900 text-white">
        <div class="container mx-auto px-6 grid lg:grid-cols-2 gap-20">
            <div>
                <h3 class="text-4xl font-black mb-8">{contact_title}</h3>
                <p class="text-slate-400 mb-12">{contact_sub}</p>
                <div class="space-y-4 text-sm">
                    <p>{contact_china}</p>
                    <p>{contact_mexico}</p>
                    <p>{contact_email}</p>
                    <p>{contact_phone}</p>
                </div>
            </div>
            <div class="bg-white p-10 rounded-3xl text-slate-900">
                <form class="space-y-6">
                    <input type="text" placeholder="Name" class="w-full p-4 bg-slate-50 rounded-xl outline-none">
                    <input type="email" placeholder="Email" class="w-full p-4 bg-slate-50 rounded-xl outline-none">
                    <textarea rows="4" placeholder="Message" class="w-full p-4 bg-slate-50 rounded-xl outline-none"></textarea>
                    <button class="w-full py-4 bg-blue-600 text-white font-bold rounded-xl">Send</button>
                </form>
            </div>
        </div>
    </section>

    <footer class="py-12 bg-white text-center text-xs font-bold text-slate-400">
        <p>{footer_copy}</p>
    </footer>
</body>
</html>
"""

# Generate files
for lang, data in translations.items():
    lang_lower = lang.lower()
    direction = "rtl" if lang in ["AR", "FA", "UR", "HE"] else "ltr"
    
    # Create directory
    os.makedirs(lang_lower, exist_ok=True)
    
    # Prepare lang options
    options = []
    for l in langs:
        selected = 'selected' if l == lang else ''
        options.append(f'<option value="/{l.lower()}/index.html" {selected}>{lang_names[l]}</option>')
    
    # Populate template
    content = template.format(
        lang_lower=lang_lower,
        direction=direction,
        site_title=data['site_title'],
        meta_desc=data['meta_desc'],
        nav_home=data['nav_home'],
        nav_solutions=data['nav_solutions'],
        nav_company=data['nav_company'],
        nav_tech=data['nav_tech'],
        nav_contact=data['nav_contact'],
        hero_title=data['hero_title'],
        hero_sub=data['hero_sub'],
        hero_cta1=data['hero_cta1'],
        hero_cta2=data['hero_cta2'],
        about_title=data['about_title'],
        about_p1=data['about_p1'],
        about_p2=data['about_p2'],
        prod_1_title=data['prod_1_title'],
        prod_1_desc=data['prod_1_desc'],
        prod_2_title=data['prod_2_title'],
        prod_2_desc=data['prod_2_desc'],
        prod_3_title=data['prod_3_title'],
        prod_3_desc=data['prod_3_desc'],
        prod_4_title=data['prod_4_title'],
        prod_4_desc=data['prod_4_desc'],
        prod_5_title=data['prod_5_title'],
        prod_5_desc=data['prod_5_desc'],
        prod_6_title=data['prod_6_title'],
        prod_6_desc=data['prod_6_desc'],
        contact_title=data['contact_title'],
        contact_sub=data['contact_sub'],
        contact_china=data['contact_china'],
        contact_mexico=data['contact_mexico'],
        contact_email=data['contact_email'],
        contact_phone=data['contact_phone'],
        footer_copy=data['footer_copy'],
        lang_options="".join(options)
    )
    
    # Write file
    with open(f"{lang_lower}/index.html", "w", encoding="utf-8") as f:
        f.write(content)

# Root index.html redirect
with open("index.html", "w", encoding="utf-8") as f:
    f.write('<script>window.location.href = "/en/index.html";</script>')

print("Successfully generated 38 localized sites.")
