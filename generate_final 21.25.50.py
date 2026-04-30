import os

langs = {
    "no": {
        "lang_attr": "no",
        "dir": "ltr",
        "title": "Moderne Industriell Kvalitet",
        "hero_h1": "Pionerarbeid for fremtidens industriteknologi",
        "hero_p": "Presisjonsteknikk, global innvirkning og bærekraftig innovasjon.",
        "services_h2": "Våre tjenester",
        "card1_h3": "Avansert produksjon",
        "card1_p": "Toppmoderne fasiliteter som utnytter AI og robotikk for uovertruffen presisjon.",
        "card2_h3": "Bærekraftig energi",
        "card2_p": "Innovative løsninger for en grønnere industriell fremtid gjennom ren energiteknologi.",
        "card3_h3": "Global logistikk",
        "card3_p": "Smarte styringssystemer for forsyningskjeden som sikrer sømløs global drift.",
        "footer": "© 2026 Industrial Excellence Corp. Med enerett."
    },
    "uk": {
        "lang_attr": "uk",
        "dir": "ltr",
        "title": "Сучасна промислова досконалість",
        "hero_h1": "Провадження майбутнього промислових технологій",
        "hero_p": "Прецизійне проектування, глобальний вплив та сталі інновації.",
        "services_h2": "Наші послуги",
        "card1_h3": "Передове виробництво",
        "card1_p": "Найсучасніші потужності, що використовують ШІ та робототехніку для неперевершеної точності.",
        "card2_h3": "Стала енергетика",
        "card2_p": "Інноваційні рішення для екологічнішого промислового майбутнього завдяки технологіям чистої енергії.",
        "card3_h3": "Глобальна логістика",
        "card3_p": "Розумні системи управління ланцюгами поставок, що забезпечують безперебійну глобальну діяльність.",
        "footer": "© 2026 Industrial Excellence Corp. Усі права захищено."
    },
    "bg": {
        "lang_attr": "bg",
        "dir": "ltr",
        "title": "Модерно индустриално съвършенство",
        "hero_h1": "Пионерство в бъдещето на индустриалните технологии",
        "hero_p": "Прецизно инженерство, глобално въздействие и устойчиви иновации.",
        "services_h2": "Нашите услуги",
        "card1_h3": "Усъвършенствано производство",
        "card1_p": "Съвременни съоръжения, използващи ИИ и роботика за ненадмината прецизност.",
        "card2_h3": "Устойчива енергия",
        "card2_p": "Иновативни решения за по-зелено индустриално бъдеще чрез технологии за чиста енергия.",
        "card3_h3": "Глобална логістика",
        "card3_p": "Интелигентни системи за управление на веригата за доставки, осигуряващи безпроблемни глобални операции.",
        "footer": "© 2026 Industrial Excellence Corp. Всички права запазени."
    },
    "hr": {
        "lang_attr": "hr",
        "dir": "ltr",
        "title": "Moderna industrijska izvrsnost",
        "hero_h1": "Predvodnik budućnosti industrijske tehnologije",
        "hero_p": "Precizno inženjerstvo, globalni utjecaj i održive inovacije.",
        "services_h2": "Naše usluge",
        "card1_h3": "Napredna proizvodnja",
        "card1_p": "Najsuvremeniji pogoni koji koriste umjetnu inteligenciju i robotiku za neviđenu preciznost.",
        "card2_h3": "Održiva energija",
        "card2_p": "Inovativna rješenja za zeleniju industrijsku budućnost kroz tehnologiju čiste energije.",
        "card3_h3": "Globalna logistika",
        "card3_p": "Pametni sustavi upravljanja opskrbnim lancem koji osiguravaju besprijekorno globalno poslovanje.",
        "footer": "© 2026 Industrial Excellence Corp. Sva prava pridržana."
    },
    "sr": {
        "lang_attr": "sr",
        "dir": "ltr",
        "title": "Moderna industrijska izvrsnost",
        "hero_h1": "Predvodnik budućnosti industrijske tehnologije",
        "hero_p": "Precizno inženjerstvo, globalni uticaj i održive inovacije.",
        "services_h2": "Naše usluge",
        "card1_h3": "Napredna proizvodnja",
        "card1_p": "Najsavremeniji pogoni koji koriste veštačku inteligenciju i robotiku za neprevaziđenu preciznost.",
        "card2_h3": "Održiva energija",
        "card2_p": "Inovativna rešenja za zeleniju industrijsku budućnost kroz tehnologiju čiste energije.",
        "card3_h3": "Globalna logistika",
        "card3_p": "Pametni sistemi upravljanja lancem snabdevanja koji osiguravaju besprekorno globalno poslovanje.",
        "footer": "© 2026 Industrial Excellence Corp. Sva prava zadržana."
    },
    "sk": {
        "lang_attr": "sk",
        "dir": "ltr",
        "title": "Moderná priemyselná dokonalosť",
        "hero_h1": "Priekopníci budúcnosti priemyselných technológií",
        "hero_p": "Precízne inžinierstvo, globálny vplyv a udržateľné inovácie.",
        "services_h2": "Naše služby",
        "card1_h3": "Pokročilá výroba",
        "card1_p": "Najmodernejšie zariadenia využívajúce AI a robotiku pre bezkonkurenčnú presnosť.",
        "card2_h3": "Udržateľná energia",
        "card2_p": "Inovatívne riešenia pre zelenšiu priemyselnú budúcnost prostredníctvom technológií čistej energie.",
        "card3_h3": "Globálna logistika",
        "card3_p": "Inteligentné systémy riadenia dodávateľského reťazca zabezpečujúce plynulé globálne operácie.",
        "footer": "© 2026 Industrial Excellence Corp. Všetky práva vyhradené."
    },
    "sl": {
        "lang_attr": "sl",
        "dir": "ltr",
        "title": "Sodobna industrijska odličnost",
        "hero_h1": "Pionirji prihodnosti industrijske tehnologije",
        "hero_p": "Natančen inženiring, globalni vpliv in trajnostne inovacije.",
        "services_h2": "Naše storitve",
        "card1_h3": "Napredna proizvodnja",
        "card1_p": "Najsodobnejši objekti, ki uporabljajo AI in robotiko za neprekosljivo natančnost.",
        "card2_h3": "Trajnostna energija",
        "card2_p": "Inovativne rešitve za zeleno industrijsko prihodnost s tehnologijo čiste energije.",
        "card3_h3": "Globalna logistika",
        "card3_p": "Pametni sistemi upravljanja dobavne verige, ki zagotavljajo brezhibno globalno poslovanje.",
        "footer": "© 2026 Industrial Excellence Corp. Vse pravice pridržane."
    },
    "lt": {
        "lang_attr": "lt",
        "dir": "ltr",
        "title": "Šiuolaikinė pramoninė kompetencija",
        "hero_h1": "Pramonės technologijų ateities kūrimas",
        "hero_p": "Tikslioji inžinerija, pasaulinis poveikis ir tvarios inovacijos.",
        "services_h2": "Mūsų paslaugos",
        "card1_h3": "Pažangi gamyba",
        "card1_p": "Pažangiausios įmonės, naudojančios DI ir robotiką neprilygstamam tikslumui užtikrinti.",
        "card2_h3": "Tvari energija",
        "card2_p": "Inovatyvūs sprendimai ekologiškesnei pramonės ateičiai per švarios energijos technologijas.",
        "card3_h3": "Globali logistika",
        "card3_p": "Išmaniosios tiekimo grandinės valdymo sistemos, užtikrinančios sklandžią pasaulinę veiklą.",
        "footer": "© 2026 Industrial Excellence Corp. Visos teisės saugomos."
    }
}

switcher_html = """            <select onchange="window.location.href=this.value">
                <option value="/en/">English (EN)</option>
                <option value="/ar/">العربية (AR)</option>
                <option value="/es/">Español (ES)</option>
                <option value="/fr/">Français (FR)</option>
                <option value="/de/">Deutsch (DE)</option>
                <option value="/ru/">Русский (RU)</option>
                <option value="/pt/">Português (PT)</option>
                <option value="/ja/">日本語 (JA)</option>
                <option value="/ko/">한국어 (KO)</option>
                <option value="/it/">Italiano (IT)</option>
                <option value="/bn/">বাংলা (BN)</option>
                <option value="/cs/">Čeština (CS)</option>
                <option value="/da/">Dansk (DA)</option>
                <option value="/el/">Ελληνικά (EL)</option>
                <option value="/fa/">فارسی (FA)</option>
                <option value="/fi/">Suomi (FI)</option>
                <option value="/he/">עברית (HE)</option>
                <option value="/hi/">हिन्दी (HI)</option>
                <option value="/hu/">Magyar (HU)</option>
                <option value="/id/">Bahasa Indonesia (ID)</option>
                <option value="/ms/">Bahasa Melayu (MS)</option>
                <option value="/nl/">Nederlands (NL)</option>
                <option value="/pl/">Polski (PL)</option>
                <option value="/ro/">Română (RO)</option>
                <option value="/sv/">Svenska (SV)</option>
                <option value="/th/">ไทย (TH)</option>
                <option value="/tl/">Tagalog (TL)</option>
                <option value="/tr/">Türkçe (TR)</option>
                <option value="/ur/">اردو (UR)</option>
                <option value="/vi/">Tiếng Việt (VI)</option>
                <option value="/no/">Norsk (NO)</option>
                <option value="/uk/">Українська (UK)</option>
                <option value="/bg/">Български (BG)</option>
                <option value="/hr/">Hrvatski (HR)</option>
                <option value="/sr/">Srpski (SR)</option>
                <option value="/sk/">Slovenčina (SK)</option>
                <option value="/sl/">Slovenščina (SL)</option>
                <option value="/lt/">Lietuvių (LT)</option>
            </select>"""

template = """<!DOCTYPE html>
<html lang="{lang_attr}" dir="{dir}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        :root {{
            --primary: #f97316;
            --bg: #0f172a;
            --text: #f1f5f9;
            --card-bg: #1e293b;
        }}
        body {{
            margin: 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: var(--bg);
            color: var(--text);
            line-height: 1.6;
            {text_align}
        }}
        header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1.5rem 5%;
            background: rgba(15, 23, 42, 0.9);
            position: sticky;
            top: 0;
            z-index: 100;
        }}
        .logo {{
            font-size: 1.5rem;
            font-weight: 800;
            color: var(--primary);
            text-transform: uppercase;
            letter-spacing: 2px;
        }}
        .lang-switcher select {{
            background: var(--card-bg);
            color: var(--text);
            border: 1px solid #334155;
            padding: 0.5rem;
            border-radius: 4px;
        }}
        .hero {{
            padding: 100px 5%;
            text-align: center;
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            border-bottom: 4px solid var(--primary);
        }}
        .hero h1 {{
            font-size: 3.5rem;
            margin-bottom: 1rem;
            font-weight: 900;
        }}
        .hero p {{
            font-size: 1.25rem;
            color: #94a3b8;
            max-width: 800px;
            margin: 0 auto;
        }}
        .services {{
            padding: 80px 5%;
        }}
        .services h2 {{
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 3rem;
        }}
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }}
        .card {{
            background: var(--card-bg);
            padding: 2.5rem;
            border-radius: 8px;
            border-top: 4px solid var(--primary);
            transition: transform 0.3s ease;
        }}
        .card:hover {{
            transform: translateY(-10px);
        }}
        .card h3 {{
            font-size: 1.5rem;
            margin-bottom: 1rem;
        }}
        footer {{
            padding: 40px 5%;
            text-align: center;
            border-top: 1px solid #334155;
            color: #64748b;
        }}
    </style>
</head>
<body>
    <header>
        <div class="logo">IndEx Corp</div>
        <div class="lang-switcher">
{switcher}
        </div>
    </header>

    <section class="hero">
        <h1>{hero_h1}</h1>
        <p>{hero_p}</p>
    </section>

    <section class="services">
        <h2>{services_h2}</h2>
        <div class="grid">
            <div class="card">
                <h3>{card1_h3}</h3>
                <p>{card1_p}</p>
            </div>
            <div class="card">
                <h3>{card2_h3}</h3>
                <p>{card2_p}</p>
            </div>
            <div class="card">
                <h3>{card3_h3}</h3>
                <p>{card3_p}</p>
            </div>
        </div>
    </section>

    <footer>
        <p>{footer}</p>
    </footer>
</body>
</html>
"""

base_path = "/Users/jet/.accio/accounts/1661502182/agents/DID-F456DA-2B0D4C/project/multi_lang_v1"

# Generate new 8 languages
for code, data in langs.items():
    dir_path = os.path.join(base_path, code)
    os.makedirs(dir_path, exist_ok=True)
    
    # Update switcher to mark current language as selected
    current_switcher = switcher_html.replace(f'value="/{code}/"', f'value="/{code}/" selected')
    
    text_align = "text-align: right;" if data["dir"] == "rtl" else ""
    
    content = template.format(
        lang_attr=data["lang_attr"],
        dir=data["dir"],
        title=data["title"],
        text_align=text_align,
        switcher=current_switcher,
        hero_h1=data["hero_h1"],
        hero_p=data["hero_p"],
        services_h2=data["services_h2"],
        card1_h3=data["card1_h3"],
        card1_p=data["card1_p"],
        card2_h3=data["card2_h3"],
        card2_p=data["card2_p"],
        card3_h3=data["card3_h3"],
        card3_p=data["card3_p"],
        footer=data["footer"]
    )
    
    with open(os.path.join(dir_path, "index.html"), "w", encoding="utf-8") as f:
        f.write(content)

print("Generated 8 new language files.")

# Update Batch 1 languages
batch1 = ["en", "ar", "es", "fr", "de", "ru", "pt", "ja", "ko", "it"]

for code in batch1:
    file_path = os.path.join(base_path, code, "index.html")
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        
        start_line = -1
        end_line = -1
        for i, line in enumerate(lines):
            if '<div class="lang-switcher">' in line:
                start_line = i + 1
            if start_line != -1 and '</select>' in line:
                end_line = i + 1
                break
        
        if start_line != -1 and end_line != -1:
            # Update switcher to mark current language as selected
            current_switcher = switcher_html.replace(f'value="/{code}/"', f'value="/{code}/" selected')
            
            new_lines = lines[:start_line] + [current_switcher + "\n"] + lines[end_line:]
            with open(file_path, "w", encoding="utf-8") as f:
                f.writelines(new_lines)
            print(f"Updated {code}/index.html")
        else:
            print(f"Could not find switcher in {code}/index.html")
    else:
        print(f"File not found: {file_path}")
