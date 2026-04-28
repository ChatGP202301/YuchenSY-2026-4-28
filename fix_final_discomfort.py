import os, re

rtl_css = """
    /* RTL Layout Fixes */
    [dir="rtl"] { text-align: right; }
    [dir="rtl"] .hero-inner, [dir="rtl"] .about-inner, [dir="rtl"] .contact-inner { text-align: right; }
    [dir="rtl"] .about-inner { display: flex; flex-direction: row-reverse; }
    [dir="rtl"] .contact-form input, [dir="rtl"] .contact-form textarea { text-align: right; direction: rtl; }
    [dir="rtl"] .hero-btns { justify-content: flex-start; gap: 1rem; }
    [dir="rtl"] .topbar-info { flex-direction: row-reverse; }
    [dir="rtl"] .header-inner { flex-direction: row-reverse; }
    [dir="rtl"] .nav { flex-direction: row-reverse; }
    [dir="rtl"] .stat-item { border-right: none; border-left: 1px solid var(--border); }
    [dir="rtl"] .stat-item:last-child { border-left: none; }
    @media (max-width: 992px) {
        [dir="rtl"] .about-inner { flex-direction: column; }
    }
"""

def process_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Fix the escaping bug from previous sub
    content = content.replace("<img src=\\\"../assets/logo.png\\\"", "<img src=\"../assets/logo.png\"")
    content = content.replace("<img src=\\\"assets/logo.png\\\"", "<img src=\"assets/logo.png\"")
    content = content.replace("alt=\\\"Express Water Logo\\\"", "alt=\"Express Water Logo\"")
    content = content.replace("width=\\\"180\\\"", "width=\"180\"")
    content = content.replace("height=\\\"50\\\"", "height=\"50\"")
    
    # 2. Add RTL CSS fix if not present
    if "/* RTL Layout Fixes */" not in content:
        content = content.replace("</style>", rtl_css + "\n  </style>")
        
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

# Root index.html
if os.path.exists("index.html"):
    process_file("index.html")

# Subdirectories
langs = ["en", "es", "ar", "pt", "fr", "de", "ru", "ja", "ko", "it", "nl", "tr", "vi", "th", "id", "ms", "pl", "sv", "no", "da", "fi", "he", "ta", "my", "km", "lo", "fa", "kk", "uz", "ps", "sw", "ha", "zu", "uk", "cs", "hu", "ro", "el"]
for lang in langs:
    path = os.path.join(lang, "index.html")
    if os.path.exists(path):
        process_file(path)
        print(f"Polished {path}")

