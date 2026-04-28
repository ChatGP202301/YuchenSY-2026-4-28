
const fs = require('fs');
const path = require('path');

const showcasePath = '/Users/jet/Downloads/ecoexpresswater-showcase.html';
const languagesPath = 'languages_no_zh.json';
const productsPath = 'products_clean.json';

const showcase = fs.readFileSync(showcasePath, 'utf8');
const headMatch = showcase.match(/<head>([\s\S]*?)<\/head>/);
const css = headMatch ? headMatch[1] : '';

const html_part1 = `
<!DOCTYPE html>
<html :lang="currentLang" :dir="isRtl ? 'rtl' : 'ltr'" x-data="siteData()" x-cloak>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title x-text="t('heroTitle') + ' | Eco Express Water'"></title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,300&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js" defer></script>
    <style>
        \${css.replace(/<style>|<\\/style>/g, '').replace(/html\\s*\{/, '[x-cloak] { display: none !important; }\\nhtml {')}
        
        /* Language Selector Styles */
        .lang-selector-wrap { position: fixed; top: 20px; right: 20px; z-index: 2000; }
        .lang-btn { 
            background: var(--white); border: 1px solid var(--line); 
            padding: 8px 16px; border-radius: 100px; cursor: pointer;
            display: flex; align-items: center; gap: 8px; font-weight: 600; font-size: 14px;
            box-shadow: var(--shadow); transition: all 0.3s;
        }
        .lang-btn:hover { border-color: var(--blue); transform: translateY(-2px); }
        .lang-dropdown {
            position: absolute; top: calc(100% + 10px); right: 0;
            background: var(--white); border: 1px solid var(--line);
            border-radius: 16px; box-shadow: var(--shadowH);
            width: 320px; max-height: 480px; overflow-y: auto;
            padding: 12px; display: grid; grid-template-columns: 1fr 1fr; gap: 8px;
            opacity: 0; transform: translateY(10px); pointer-events: none;
            transition: all 0.3s;
        }
        .lang-dropdown.open { opacity: 1; transform: translateY(0); pointer-events: auto; }
        .lang-item {
            padding: 8px 12px; border-radius: 8px; font-size: 13px; cursor: pointer;
            transition: background 0.2s; display: flex; align-items: center; justify-content: space-between;
        }
        .lang-item:hover { background: var(--ice); color: var(--blue); }
        .lang-item.active { background: var(--blue); color: var(--white); }

        /* RTL Adjustments */
        [dir="rtl"] .lang-selector-wrap { right: auto; left: 20px; }
        [dir="rtl"] .lang-dropdown { right: auto; left: 0; }
        [dir="rtl"] .hero-eyebrow .eyebrow-line { margin-left: 0; margin-right: 0; margin-left: 12px; }
        [dir="rtl"] .btn-primary svg { transform: scaleX(-1); margin-left: 0; margin-right: 8px; }
        
        /* Product Detail Styles */
        .detail-view { padding: 120px 0 80px; background: var(--white); min-height: 100vh; }
        .detail-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 64px; align-items: start; }
        .detail-image { border-radius: var(--rL); overflow: hidden; background: var(--chalk); border: 1px solid var(--line); }
        .detail-content h1 { font-family: 'Syne', sans-serif; font-size: 42px; font-weight: 800; margin-bottom: 16px; color: var(--navy); }
        .detail-desc { font-size: 18px; color: var(--sub); margin-bottom: 32px; line-height: 1.8; }
        .spec-card { background: var(--chalk); border: 1px solid var(--line); border-radius: var(--r); padding: 24px; margin-bottom: 32px; }
        .spec-item { display: flex; justify-content: space-between; padding: 12px 0; border-bottom: 1px solid var(--line); }
        .spec-item:last-child { border-bottom: none; }
        .spec-label { font-weight: 700; color: var(--navy2); }
        .spec-value { color: var(--sub); }
        
        @media (max-width: 768px) {
            .detail-grid { grid-template-columns: 1fr; gap: 32px; }
            .detail-content h1 { font-size: 32px; }
            .lang-dropdown { width: 280px; grid-template-columns: 1fr; }
        }
    </style>
</head>
<body :class="isRtl ? 'rtl' : ''">

    <!-- ─── LANGUAGE SELECTOR ───────────────────────────────────── -->
    <div class="lang-selector-wrap" x-data="{ open: false }" @click.away="open = false">
        <button class="lang-btn" @click="open = !open">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
            <span x-text="languages[currentLang].name"></span>
        </button>
        <div class="lang-dropdown" :class="open ? 'open' : ''">
            <template x-for="(lang, code) in languages" :key="code">
                <div class="lang-item" :class="currentLang === code ? 'active' : ''" @click="changeLang(code); open = false">
                    <span x-text="lang.name"></span>
                    <span style="opacity: 0.5; font-size: 10px;" x-text="code.toUpperCase()"></span>
                </div>
            </template>
        </div>
    </div>

    <!-- ─── HEADER ────────────────────────────────────────────── -->
    <header id="site-header" :class="scrolled ? 'scrolled' : ''">
        <div class="header-inner">
            <div class="logo-wrap" @click="view = 'home'; window.scrollTo(0,0)" style="cursor:pointer">
                <div class="logo-mark">E</div>
                <div class="logo-text">
                    Eco Express Water
                    <div class="logo-sub">Professional Water Filtration Manufacturer</div>
                </div>
            </div>
            <nav>
                <a href="#products" @click.prevent="view = 'home'; setTimeout(() => document.getElementById('products').scrollIntoView({behavior:'smooth'}), 100)" x-text="t('navProducts')"></a>
                <a href="#about" @click.prevent="view = 'home'; setTimeout(() => document.getElementById('about').scrollIntoView({behavior:'smooth'}), 100)" x-text="t('navAbout')"></a>
                <a href="#tech" @click.prevent="view = 'home'; setTimeout(() => document.getElementById('tech').scrollIntoView({behavior:'smooth'}), 100)" x-text="t('workshopTitle')"></a>
                <a :href="'https://wa.me/8619908311885?text=' + encodeURIComponent('Hi, I am interested in your products.')" class="nav-cta" x-text="t('navContact')"></a>
            </nav>
        </div>
    </header>

    <!-- ─── HOME VIEW ─────────────────────────────────────────── -->
    <div x-show="view === 'home'">
        <!-- HERO -->
        <section class="hero" id="home">
            <div class="hero-bg">
                <img src="https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=1920,fit=crop/A85Dpv78OotyVQVx/img_5611-Yyvy7nEvNPUO3M3M.JPG" alt="Factory" loading="eager">
            </div>
            <div class="hero-gradient"></div>
            <div class="hero-rings"><div class="ring"></div><div class="ring"></div><div class="ring"></div></div>
            <div class="hero-content">
                <div class="hero-eyebrow reveal visible">
                    <div class="eyebrow-line"></div>
                    <span class="eyebrow-text">NSF Certified · ISO Certified · 15 Years Experience</span>
                </div>
                <h1 class="reveal visible delay-1" x-html="t('heroTitle').replace(/Water/g, 'Water,<br><em>Innovation</em>')"></h1>
                <p class="hero-sub reveal visible delay-2" x-text="t('heroSub')"></p>
                <div class="hero-btns reveal visible delay-3">
                    <a href="#products" class="btn-primary" @click.prevent="document.getElementById('products').scrollIntoView({behavior:'smooth'})">
                        <span x-text="t('viewProducts')"></span>
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                    </a>
                    <a :href="'https://wa.me/8619908311885?text=' + encodeURIComponent('Hi, I want a quote for your water filters.')" class="btn-secondary" x-text="t('getQuote')"></a>
                </div>
            </div>
        </section>

        <!-- STATS STRIP -->
        <div class="stats-strip">
            <div class="container">
                <div class="stats-inner">
                    <div class="stat-item"><div class="stat-num">15+</div><div class="stat-label" x-text="t('yearsExp')"></div></div>
                    <div class="stat-item"><div class="stat-num">NSF</div><div class="stat-label" x-text="t('certified')"></div></div>
                    <div class="stat-item"><div class="stat-num">50+</div><div class="stat-label" x-text="t('countries')"></div></div>
                    <div class="stat-item"><div class="stat-num">ISO</div><div class="stat-label">9001/14001</div></div>
                </div>
            </div>
        </div>

        <!-- PRODUCTS SECTION -->
        <section class="section" id="products" style="background: var(--white)">
            <div class="container">
                <div class="section-header reveal visible">
                    <div class="tag" x-text="t('productsTag')"></div>
                    <h2 x-text="t('productsTitle')"></h2>
                    <p x-text="t('aboutP1')"></p>
                </div>
                <div class="product-grid">
                    <template x-for="product in products" :key="product.id">
                        <div class="product-card reveal visible" @click="selectProduct(product)">
                            <div class="product-img">
                                <img :src="product.image" :alt="t(product.nameKey)" loading="lazy">
                                <div class="product-overlay">
                                    <div class="btn-view" x-text="t('inquire')"></div>
                                </div>
                            </div>
                            <div class="product-info">
                                <div class="product-tag" x-text="t(product.tagKey)"></div>
                                <h3 x-text="t(product.nameKey)"></h3>
                                <p x-text="t(product.descKey).substring(0, 80) + '...'"></p>
                            </div>
                        </div>
                    </template>
                </div>
            </div>
        </section>

        <!-- ABOUT / SGS SECTION -->
        <section class="section" id="about">
            <div class="container">
                <div class="about-grid">
                    <div class="about-text reveal visible reveal-left">
                        <div class="tag" x-text="t('aboutTag')"></div>
                        <h2 x-text="t('aboutSgsTitle')"></h2>
                        <p x-text="t('aboutSgsDesc')"></p>
                        <div class="about-features">
                            <div class="feat-item"><div class="feat-icon">✓</div><span x-text="t('sgsReport1')"></span></div>
                            <div class="feat-item"><div class="feat-icon">✓</div><span x-text="t('sgsReport2')"></span></div>
                            <div class="feat-item"><div class="feat-icon">✓</div><span x-text="t('sgsReport3')"></span></div>
                        </div>
                    </div>
                    <div class="about-visual reveal visible reveal-right">
                        <img src="https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=800,fit=crop/A85Dpv78OotyVQVx/img_5613-YleP96EV09Uv44M4.JPG" alt="SGS Report" style="border-radius:var(--rL);box-shadow:var(--shadowH)">
                    </div>
                </div>
            </div>
        </section>

        <!-- TECHNOLOGY / WORKSHOP -->
        <section class="section" id="tech" style="background:var(--navy); color:var(--white)">
            <div class="container">
                <div class="section-header reveal visible">
                    <div class="tag tag-white" x-text="t('workshopTitle')"></div>
                    <h2 style="color:var(--white)" x-text="t('workshopTitle')"></h2>
                    <p style="color:rgba(255,255,255,.6)" x-text="t('workshopDesc')"></p>
                </div>
                <div class="tech-grid">
                    <div class="tech-card reveal visible">
                        <div class="tech-icon">⚙️</div>
                        <h3 x-text="t('workshopPP')"></h3>
                    </div>
                    <div class="tech-card reveal visible delay-1">
                        <div class="tech-icon">🔬</div>
                        <h3 x-text="t('workshopCarbon')"></h3>
                    </div>
                    <div class="tech-card reveal visible delay-2">
                        <div class="tech-icon">⚡</div>
                        <h3 x-text="t('workshopQuick')"></h3>
                    </div>
                    <div class="tech-card reveal visible delay-3">
                        <div class="tech-icon">🛡️</div>
                        <h3 x-text="t('workshopLeak')"></h3>
                    </div>
                </div>
            </div>
        </section>

        <!-- EXHIBITION -->
        <section class="section">
            <div class="container">
                <div class="about-grid" style="grid-template-columns: 1.2fr 1fr">
                    <div class="about-visual reveal visible reveal-left">
                        <img src="https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=800,fit=crop/A85Dpv78OotyVQVx/img_5454-YleP9XvR07Uv44M4.JPG" alt="Exhibition" style="border-radius:var(--rL);box-shadow:var(--shadowH)">
                    </div>
                    <div class="about-text reveal visible reveal-right">
                        <div class="tag">Global Presence</div>
                        <h2 x-text="t('exhibitionTitle')"></h2>
                        <p x-text="t('exhibitionDesc')"></p>
                        <div class="about-features">
                            <div class="feat-item"><div class="feat-icon">📍</div><span x-text="t('exhibitionBooth')"></span></div>
                            <div class="feat-item"><div class="feat-icon">✨</div><span x-text="t('exhibitionDisplay')"></span></div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- OEM STRIP -->
        <div class="oem-strip">
            <div class="container">
                <div class="tag tag-white reveal visible" style="margin:0 auto 24px">✦ OEM / ODM Partnership</div>
                <h2 class="reveal visible" x-text="t('contactTitle')"></h2>
                <p class="reveal visible" style="color:rgba(255,255,255,0.6); margin-bottom:40px" x-text="t('contactSub')"></p>
                <div class="oem-points reveal visible">
                    <div class="oem-point">📦 Custom Packaging</div>
                    <div class="oem-point">🏷️ Private Label</div>
                    <div class="oem-point">⚙️ Custom Specs</div>
                    <div class="oem-point">🌍 Worldwide Shipping</div>
                    <div class="oem-point">📋 Low MOQ</div>
                </div>
                <a :href="'https://wa.me/8619908311885?text=' + encodeURIComponent('Hi, I want to discuss an OEM project with you.')" class="btn-primary reveal visible">
                    <span x-text="t('inquire')"></span> →
                </a>
            </div>
        </div>
    </div>

    <!-- ─── DETAIL VIEW ───────────────────────────────────────── -->
    <div x-show="view === 'detail'" class="detail-view">
        <div class="container">
            <div style="margin-bottom: 40px">
                <button @click="view = 'home'" class="btn-secondary" style="padding: 10px 20px; border-radius: 100px; display: flex; align-items: center; gap: 8px">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
                    <span x-text="t('backToHome')"></span>
                </button>
            </div>
            <div class="detail-grid" x-if="selectedProduct">
                <div class="detail-image">
                    <img :src="selectedProduct.image" :alt="t(selectedProduct.nameKey)">
                </div>
                <div class="detail-content">
                    <div class="tag" x-text="t(selectedProduct.tagKey)"></div>
                    <h1 x-text="t(selectedProduct.nameKey)"></h1>
                    <p class="detail-desc" x-text="t(selectedProduct.descKey)"></p>
                    
                    <div class="spec-card">
                        <h3 style="margin-bottom: 20px" x-text="t('detailSpecs')"></h3>
                        <div class="spec-item"><span class="spec-label" x-text="t('detailMaterial')"></span><span class="spec-value">Premium Food-Grade</span></div>
                        <div class="spec-item"><span class="spec-label" x-text="t('detailCert')"></span><span class="spec-value">NSF / ISO / CE</span></div>
                        <div class="spec-item"><span class="spec-label" x-text="t('detailLead')"></span><span class="spec-value">15-25 Business Days</span></div>
                        <div class="spec-item"><span class="spec-label">OEM/ODM</span><span class="spec-value">Available</span></div>
                    </div>

                    <a :href="'https://wa.me/8619908311885?text=' + encodeURIComponent('I am interested in ' + t(selectedProduct.nameKey))" class="btn-primary" style="width: 100%; justify-content: center; padding: 18px">
                        <span x-text="t('detailWhatsApp')"></span>
                    </a>
                </div>
            </div>
        </div>
    </div>

    <!-- ─── FOOTER ────────────────────────────────────────────── -->
    <footer>
        <div class="container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <div class="footer-logo">
                        <div class="footer-logo-mark">E</div>
                        <div class="footer-logo-text">Eco Express Water</div>
                    </div>
                    <p x-text="t('aboutP1')"></p>
                </div>
                <div class="footer-col">
                    <h4 x-text="t('navProducts')"></h4>
                    <ul>
                        <li><a href="#" @click.prevent="view = 'home'">Carbon Block</a></li>
                        <li><a href="#" @click.prevent="view = 'home'">UF Membrane</a></li>
                        <li><a href="#" @click.prevent="view = 'home'">GAC Filter</a></li>
                        <li><a href="#" @click.prevent="view = 'home'">RO Systems</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4 x-text="t('navAbout')"></h4>
                    <ul>
                        <li><a href="#" @click.prevent="view = 'home'" x-text="t('navAbout')"></a></li>
                        <li><a href="#" @click.prevent="view = 'home'">Certifications</a></li>
                        <li><a href="#" @click.prevent="view = 'home'">Factory</a></li>
                    </ul>
                </div>
                <div class="footer-col footer-contact">
                    <h4 x-text="t('navContact')"></h4>
                    <p><strong>Factory Address:</strong><br>No.1 Chuangxin Road, Yuanhua Town, Haining, China</p>
                    <div class="footer-subscribe">
                        <input type="email" placeholder="Email">
                        <button>→</button>
                    </div>
                </div>
            </div>
            <div class="footer-bottom">
                <p>© 2026 Eco Express Water. All rights reserved.</p>
                <div class="footer-social">
                    <div class="social-btn">▶</div>
                    <div class="social-btn">in</div>
                    <div class="social-btn">W</div>
                </div>
            </div>
        </div>
    </footer>

    <script>
        const langData = `;

const html_part2 = `;

        function siteData() {
            return {
                currentLang: 'en',
                view: 'home',
                selectedProduct: null,
                scrolled: false,
                products: productData,
                languages: langData,
                init() {
                    window.addEventListener('scroll', () => {
                        this.scrolled = window.scrollY > 60;
                    }, { passive: true });
                    
                    const browserLang = navigator.language.split('-')[0];
                    if (this.languages[browserLang]) {
                        this.changeLang(browserLang);
                    }
                },
                get currentDictionary() {
                    return this.languages[this.currentLang] || this.languages['en'];
                },
                t(key) {
                    if (!key) return '';
                    return this.currentDictionary[key] || this.languages['en'][key] || key;
                },
                get isRtl() {
                    return ['ar', 'fa', 'ps', 'prs'].includes(this.currentLang);
                },
                changeLang(lang) {
                    this.currentLang = lang;
                    document.documentElement.lang = lang;
                    document.documentElement.dir = this.isRtl ? 'rtl' : 'ltr';
                },
                selectProduct(product) {
                    this.selectedProduct = product;
                    this.view = 'detail';
                    window.scrollTo(0, 0);
                }
            }
        }
    </script>
</body>
</html>
\`;

const fd = fs.openSync('index.html', 'w');
fs.writeSync(fd, html_part1);
fs.writeSync(fd, languages);
fs.writeSync(fd, ';\\n        const productData = ');
fs.writeSync(fd, products);
fs.writeSync(fd, html_part2);
fs.closeSync(fd);

console.log('index.html created successfully.');
