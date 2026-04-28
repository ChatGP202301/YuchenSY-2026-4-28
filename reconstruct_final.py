import json
import re

# Source of design
with open('/Users/jet/Downloads/ecoexpresswater-showcase.html', 'r', encoding='utf-8') as f:
    showcase = f.read()

# Source of data
with open('expresswater-v7-final/index.html', 'r', encoding='utf-8') as f:
    data_file = f.read()

# Extract products array
p_match = re.search(r'products:\s*(\[.*?\]),', data_file, re.DOTALL)
products_json = p_match.group(1) if p_match else "[]"

# Extract languages object
# Since it's huge, we'll find the start and balance braces
l_start = data_file.find('languages: {')
if l_start != -1:
    brace_count = 0
    l_end = -1
    for i in range(l_start + 11, len(data_file)):
        if data_file[i] == '{':
            brace_count += 1
        elif data_file[i] == '}':
            if brace_count == 0:
                l_end = i + 1
                break
            else:
                brace_count -= 1
    languages_json = data_file[l_start+11:l_end]
else:
    languages_json = "{}"

# Prepare the template based on showcase
# We need to replace the static content in showcase with Alpine.js t() calls
# But the showcase is complex. I'll create a clean Alpine-ready version.

# Helper to remove zh from languages_json string (not perfect but will do)
# Actually, better to parse as object
# But the string is large and has JS keys. 
# We'll do it in JS later or use a safer regex.

head = showcase[:showcase.find('</head>')]
# Add Alpine and extra CSS
head += """
<script src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js" defer></script>
<style>
    [x-cloak] { display: none !important; }
    .lang-dropdown {
        position: absolute; top: 100%; right: 0; 
        background: white; color: var(--navy); 
        border-radius: 12px; box-shadow: var(--shadowH);
        padding: 10px; display: grid; grid-template-columns: repeat(2, 1fr); gap: 5px;
        width: 320px; z-index: 2000; border: 1px solid var(--line);
        max-height: 400px; overflow-y: auto;
    }
    @media (max-width: 480px) { .lang-dropdown { width: 280px; grid-template-columns: 1fr; } }
    .lang-btn {
        font-size: 12px; padding: 8px; border-radius: 6px; text-align: left;
        transition: background .2s; cursor: pointer; color: var(--text);
    }
    .lang-btn:hover { background: var(--ice); color: var(--blue); }
    .active-lang { background: var(--blue); color: white !important; }
    .rtl { direction: rtl; }
    .modal-overlay {
        position: fixed; inset: 0; background: rgba(6,16,30,.85);
        backdrop-filter: blur(8px); z-index: 3000;
        display: flex; align-items: center; justify-content: center; padding: 20px;
    }
    .modal-content {
        background: white; width: 100%; max-width: 1000px; max-height: 90vh;
        border-radius: var(--rL); overflow-y: auto; position: relative;
        box-shadow: var(--shadowH);
    }
    .close-modal {
        position: absolute; top: 20px; right: 20px;
        width: 40px; height: 40px; border-radius: 50%;
        background: var(--chalk); display: flex; align-items: center; justify-content: center;
        cursor: pointer; z-index: 10; transition: background .2s;
    }
    /* Fix potential text deformation */
    h1, h2, h3 { line-height: 1.1; letter-spacing: -0.01em; }
    .hero-sub { line-height: 1.6; }
</style>
</head>
"""

body_start = """
<body x-data="siteData()" x-cloak :class="currentLang === 'ar' || currentLang === 'fa' || currentLang === 'ps' || currentLang === 'prs' ? 'rtl' : ''">
    <!-- HEADER -->
    <header id="site-header" :class="scrolled ? 'scrolled' : ''" @scroll.window="scrolled = (window.pageYOffset > 50)">
        <div class="header-inner">
            <div class="logo-wrap" @click="view = 'home'; window.scrollTo(0,0)" style="cursor:pointer">
                <div class="logo-mark">E</div>
                <div class="logo-text">
                    Express Water
                    <div class="logo-sub" x-text="t('navTitleSub') || '20+ Years of Excellence'"></div>
                </div>
            </div>
            <nav>
                <a href="#products" x-text="t('navProducts')"></a>
                <a href="#about" x-text="t('navAbout')"></a>
                <div style="position:relative" x-data="{ open: false }">
                    <button @click="open = !open" class="btn-ghost" style="padding: 8px 14px; font-size: 13px;">
                        🌐 <span x-text="languages[currentLang] ? languages[currentLang].name : 'English'"></span>
                    </button>
                    <div x-show="open" @click.away="open = false" class="lang-dropdown">
                        <template x-for="(lang, code) in languages">
                            <div class="lang-btn" :class="currentLang === code ? 'active-lang' : ''" 
                                 @click="currentLang = code; open = false; document.documentElement.dir = (code === 'ar' || code === 'fa' || code === 'ps' || code === 'prs') ? 'rtl' : 'ltr'">
                                <span x-text="lang.name"></span>
                            </div>
                        </template>
                    </div>
                </div>
                <a :href="'https://wa.me/8619908311885?text=' + encodeURIComponent('Hi, I am interested in ' + (selectedProduct ? t(selectedProduct.nameKey) : 'Express Water products'))" 
                   class="nav-cta" target="_blank" x-text="t('navContact')"></a>
            </nav>
        </div>
    </header>

    <!-- HERO -->
    <section class="hero" x-show="view === 'home'">
        <div class="hero-bg">
            <img src="https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=1920,fit=crop/A85Dpv78OotyVQVx/img_5611-Yyvy7nEvNPUO3M3M.JPG" alt="Factory">
        </div>
        <div class="hero-gradient"></div>
        <div class="hero-rings"><div class="ring"></div><div class="ring"></div><div class="ring"></div></div>
        <div class="hero-content">
            <div class="hero-eyebrow">
                <div class="eyebrow-line"></div>
                <span class="eyebrow-text">NSF Certified · ISO Certified · 20+ Years Experience</span>
            </div>
            <h1 x-html="t('heroTitle')"></h1>
            <p class="hero-sub" x-text="t('heroSub')"></p>
            <div class="hero-actions">
                <a href="#products" class="btn-primary">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><polyline points="12 8 16 12 12 16"/><line x1="8" y1="12" x2="16" y2="12"/></svg>
                    <span x-text="t('viewProducts')"></span>
                </a>
                <a :href="'https://wa.me/8619908311885?text=' + encodeURIComponent('Hi, I want to discuss OEM/ODM partnership')" class="btn-ghost" target="_blank">OEM / ODM →</a>
            </div>
        </div>
    </section>

    <!-- STATS -->
    <div class="stats-strip" x-show="view === 'home'">
        <div class="stats-inner">
            <div class="stat-item"><div class="stat-num">20<span>+</span></div><div class="stat-label" x-text="t('yearsExp')"></div></div>
            <div class="stat-item"><div class="stat-num">57<span>+</span></div><div class="stat-label" x-text="t('countries')"></div></div>
            <div class="stat-item"><div class="stat-num">0.01<span>μm</span></div><div class="stat-label">Precision</div></div>
            <div class="stat-item"><div class="stat-num">NSF</div><div class="stat-label" x-text="t('certified')"></div></div>
        </div>
    </div>

    <!-- PRODUCTS GRID -->
    <section class="products" id="products">
        <div class="container">
            <div class="section-header">
                <div class="tag">✦ <span x-text="t('navProducts')"></span></div>
                <h2 x-text="t('productsTitle')"></h2>
                <p x-text="t('productsSub') || 'World-class filtration systems for diverse industrial needs.'"></p>
            </div>
            <div class="product-grid">
                <template x-for="product in products" :key="product.id">
                    <div class="product-card" @click="selectedProduct = product; view = 'detail'; window.scrollTo(0,0)">
                        <div class="product-img">
                            <img :src="product.image" :alt="t(product.nameKey)" loading="lazy" style="background:white; object-fit:contain; padding:20px;">
                            <div class="cert-badge" x-show="product.tagKey" x-text="t(product.tagKey)"></div>
                        </div>
                        <div class="product-body">
                            <div class="product-name" x-text="t(product.nameKey)"></div>
                            <p class="product-desc" x-text="t(product.descKey).substring(0, 100) + '...'"></p>
                            <div class="product-link"><span x-text="t('viewDetails') || 'View Details'"></span> →</div>
                        </div>
                    </div>
                </template>
            </div>
        </div>
    </section>

    <!-- ABOUT SECTION -->
    <section class="about" id="about" x-show="view === 'home'">
        <div class="container">
            <div class="about-grid">
                <div class="about-visual">
                    <img src="https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=1920,fit=crop/A85Dpv78OotyVQVx/img_5611-Yyvy7nEvNPUO3M3M.JPG" alt="Factory">
                    <div class="about-stat-badge"><span class="n">20</span><span class="l">YEARS<br>EXPERT</span></div>
                </div>
                <div class="about-content">
                    <div class="tag" style="margin-bottom:20px">✦ <span x-text="t('navAbout')"></span></div>
                    <h2 x-text="t('aboutTitle')"></h2>
                    <p x-text="t('aboutP1')"></p>
                    <div class="about-pills">
                        <div class="about-pill">NSF Certified ✓</div><div class="about-pill">ISO 9001 ✓</div>
                        <div class="about-pill">Halal ✓</div><div class="about-pill">OEM / ODM</div>
                    </div>
                </div>
            </div>
            <div style="margin-top: 80px; display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 30px;">
                <div class="tech-card"><h3 x-text="t('aboutSgsTitle')"></h3><p x-text="t('aboutSgsDesc')"></p></div>
                <div class="tech-card"><h3 x-text="t('workshopTitle')"></h3><p x-text="t('workshopDesc')"></p></div>
                <div class="tech-card"><h3 x-text="t('exhibitionTitle')"></h3><p x-text="t('exhibitionDesc')"></p></div>
            </div>
        </div>
    </section>

    <!-- PRODUCT DETAIL MODAL -->
    <div class="modal-overlay" x-show="view === 'detail'" x-transition @click.self="view = 'home'">
        <div class="modal-content">
            <div class="close-modal" @click="view = 'home'">✕</div>
            <div class="container" style="padding: 40px;">
                <div class="dispenser-showcase" style="grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 40px; align-items: start;">
                    <div class="dispenser-images">
                        <div class="disp-img-wrap active" style="background:white; padding:20px; border-radius:20px; border:1px solid #eee;">
                            <img :src="selectedProduct?.image" :alt="t(selectedProduct?.nameKey)" style="max-height:450px; width:auto; margin:0 auto;">
                        </div>
                    </div>
                    <div class="dispenser-info">
                        <div class="tag" style="margin-bottom:20px" x-show="selectedProduct?.tagKey" x-text="t(selectedProduct?.tagKey)"></div>
                        <h2 x-text="t(selectedProduct?.nameKey)" style="font-size:32px; margin-bottom:16px;"></h2>
                        <p x-text="t(selectedProduct?.descKey)" style="color:var(--sub); margin-bottom:24px; font-size:15px;"></p>
                        
                        <h4 style="font-family:'Syne'; text-transform:uppercase; font-size:12px; color:var(--blue); margin-bottom:12px; letter-spacing:0.1em;">Technical Specs</h4>
                        <table class="spec-table">
                            <tr><td>Material Grade</td><td x-text="t('specIndustrial') || 'NSF Certified Industrial Grade'"></td></tr>
                            <tr><td>Application</td><td x-text="t('specApp') || 'Commercial / Household'"></td></tr>
                            <tr><td>Lead Time</td><td x-text="t('specLead') || '15-25 Days'"></td></tr>
                            <tr><td>Certification</td><td>NSF, ISO, Halal, CE</td></tr>
                        </table>

                        <div style="margin-top:32px">
                            <a :href="'https://wa.me/8619908311885?text=' + encodeURIComponent('Inquiry: ' + (selectedProduct ? t(selectedProduct.nameKey) : ''))" 
                               class="btn-primary" target="_blank" style="width:100%; justify-content:center;">
                                <span x-text="t('inquireNow') || 'Inquire Now'"></span> →
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- OEM PARTNER -->
    <div class="oem-strip">
        <div class="container">
            <div class="tag tag-white" style="margin:0 auto 24px">✦ OEM / ODM Partnership</div>
            <h2 x-text="t('contactTitle')"></h2>
            <p x-text="t('contactSub')" style="color:rgba(255,255,255,0.6); margin-bottom:40px;"></p>
            <a href="https://wa.me/8619908311885" class="btn-primary" style="margin:0 auto;">Get a Free Quote →</a>
        </div>
    </div>

    <!-- FOOTER -->
    <footer style="background:var(--navy); color:white; padding: 80px 0 40px;">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <div class="footer-logo"><div class="footer-logo-mark">E</div><div class="footer-logo-text">Express Water</div></div>
                    <p style="opacity:0.5; font-size:14px; margin-top:16px;">Leading manufacturer of NSF-certified water filtration systems since 2005.</p>
                </div>
                <div class="footer-col">
                    <h4 style="color:rgba(255,255,255,0.3); font-size:12px; margin-bottom:20px;">Support</h4>
                    <p style="font-size:14px; opacity:0.6;">WhatsApp: +86 19908311885</p>
                    <p style="font-size:14px; opacity:0.6;">Email: expresswater025@gmail.com</p>
                </div>
                <div class="footer-col">
                    <h4 style="color:rgba(255,255,255,0.3); font-size:12px; margin-bottom:20px;">Address</h4>
                    <p style="font-size:14px; opacity:0.6;">No.1 Chuangxin Road, Yuanhua Town, Haining, China</p>
                </div>
            </div>
            <div style="margin-top:60px; padding-top:20px; border-top:1px solid rgba(255,255,255,0.1); text-align:center; font-size:12px; opacity:0.3;">
                &copy; 2026 Express Water. All Rights Reserved.
            </div>
        </div>
    </footer>

    <script>
        function siteData() {{
            return {{
                scrolled: false,
                currentLang: 'en',
                view: 'home',
                selectedProduct: null,
                products: {products_json},
                languages: {{{languages_json}}},
                t(key) {{
                    if (!this.languages[this.currentLang]) return key;
                    let val = this.languages[this.currentLang][key] || this.languages['en'][key] || key;
                    // Handle specific showcase improvements for heroTitle
                    if (key === 'heroTitle' && this.currentLang === 'en' && !val.includes('<em>')) {{
                        return "Pure Water,<br><em>Pure Innovation</em>";
                    }}
                    return val;
                }}
            }}
        }}

        document.addEventListener('DOMContentLoaded', () => {{
            const observer = new IntersectionObserver((entries) => {{
                entries.forEach(entry => {{
                    if (entry.isIntersecting) entry.target.classList.add('visible');
                }});
            }}, {{ threshold: 0.1 }});
            document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
        }});
    </script>
</body>
</html>
"""

# Assemble
final_html = head + body_start

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("index.html reconstructed with v7-final data and showcase design.")
