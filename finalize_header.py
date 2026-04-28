import os, re

# New CSS to be injected/updated
header_polish_css = """
    /* Header & Logo Polish */
    .header-inner {
      padding: 12px 0;
      gap: 20px;
    }
    .logo img {
      height: 32px; /* Standard sleek height */
      width: auto;
      display: block;
      object-fit: contain;
    }
    .nav {
      gap: 2px;
    }
    .nav a {
      padding: 8px 14px;
      font-size: 0.9rem;
    }
    .header-lang {
      margin-left: auto;
      margin-right: 10px;
    }
    .header-lang .lang-select {
      border: 1px solid var(--border);
      padding: 6px 10px;
      border-radius: 6px;
      font-size: 0.85rem;
      background: #fff;
    }
    .cta {
      padding: 10px 20px;
      font-size: 0.9rem;
      white-space: nowrap;
    }
    @media (max-width: 1100px) {
      .nav a { padding: 8px 8px; font-size: 0.85rem; }
    }
    @media (max-width: 992px) {
      .header-lang { display: none; } /* Hide in mobile header, show in mobile menu instead */
    }
"""

def process_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update CSS
    if "/* Header & Logo Polish */" not in content:
        content = content.replace("</style>", header_polish_css + "\n  </style>")
    else:
        # Overwrite if exists to be sure
        content = re.sub(r"/\* Header & Logo Polish \*/.*?@media", header_polish_css.split("@media")[0] + "\n    @media", content, flags=re.DOTALL)

    # 2. Move Language Switcher
    # Find the switcher in topbar
    switcher_pattern = r"<div class=\"topbar-lang\">.*?</div>"
    switcher_match = re.search(switcher_pattern, content, re.DOTALL)
    
    if switcher_match:
        switcher_html = switcher_match.group(0)
        # Remove from topbar
        content = content.replace(switcher_html, "")
        # Clean up topbar-lang class name for header use
        header_switcher = switcher_html.replace("topbar-lang", "header-lang")
        
        # Insert between Contact (nav) and WhatsApp (cta)
        # The nav ends at </nav>, then cta starts with <a href="https://wa.me...
        content = content.replace("</nav>", f"</nav>\n    {header_switcher}")

    # 3. Ensure Logo height/width in HTML is sleek
    content = re.sub(r"<img src=\"([^\"]+logo\.png)\" alt=\"([^\"]+)\" width=\"\d+\" height=\"\d+\">",
                     r"<img src=\"\1\" alt=\"\2\" width=\"120\" height=\"32\">", content)

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
        print(f"Finalized Header for {path}")

