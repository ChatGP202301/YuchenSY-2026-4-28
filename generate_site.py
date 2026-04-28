import os
import re

languages = ["en", "es", "ar", "pt", "fr", "de", "ru", "ja", "ko", "it", "nl", "tr", "vi", "th", "id", "ms", "pl", "sv", "no", "da", "fi", "he", "ta", "my", "km", "lo", "fa", "kk", "uz", "ps", "sw", "ha", "zu", "uk", "cs", "hu", "ro", "el"]

def generate():
    if not os.path.exists("index.html"):
        print("Error: index.html not found in current directory.")
        return

    with open("index.html", "r", encoding="utf-8") as f:
        original_html = f.read()

    for lang in languages:
        if not os.path.exists(lang):
            os.makedirs(lang)
        
        html = original_html
        
        # 1. Update asset paths to use relative parent paths
        # Handle href="assets/ and src="assets/
        html = html.replace('href="assets/', 'href="../assets/')
        html = html.replace('src="assets/', 'src="../assets/')
        
        # Handle master_manifest.json
        html = html.replace("fetch('master_manifest.json')", "fetch('../master_manifest.json')")
        
        # Handle i18n fetch in changeLang
        html = html.replace('fetch(`assets/i18n/${lang}.json`)', 'fetch(`../assets/i18n/${lang}.json`)')
        
        # 2. Set initial Alpine.js currentLang
        html = html.replace("currentLang: 'en'", f"currentLang: '{lang}'")
        
        # 3. Update language switcher to navigate between directories
        # Original: <select x-model="currentLang" @change="changeLang($event.target.value)" class="lang-select">
        # We change it to redirect instead of just changing internal state
        html = html.replace('@change="changeLang($event.target.value)"', '@change="window.location.href=\'/\' + $event.target.value + \'/\'"')
        
        # 4. Update canonical links and meta URLs
        # Replace base URL with language-specific URL
        html = html.replace('<link rel="canonical" href="https://www.yuchensy.com/">', f'<link rel="canonical" href="https://www.yuchensy.com/{lang}/">')
        html = html.replace('<meta property="og:url" content="https://www.yuchensy.com/">', f'<meta property="og:url" content="https://www.yuchensy.com/{lang}/">')
        html = html.replace('<meta name="twitter:url" content="https://www.yuchensy.com/">', f'<meta name="twitter:url" content="https://www.yuchensy.com/{lang}/">')
        
        # Update JSON-LD URLs
        html = html.replace('"url": "https://www.yuchensy.com/"', f'"url": "https://www.yuchensy.com/{lang}/"')
        html = html.replace('"@id": "https://www.yuchensy.com/#organization"', f'"@id": "https://www.yuchensy.com/{lang}/#organization"')
        html = html.replace('"parentOrganization": { "@id": "https://www.yuchensy.com/#organization" }', f'"parentOrganization": {{ "@id": "https://www.yuchensy.com/{lang}/#organization" }}')

        # 5. Ensure navigation links point to sections (they already do with #hash)
        # No change needed for <a href="#products"> etc.
        
        with open(os.path.join(lang, "index.html"), "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Generated {lang}/index.html")

    # 6. Create ROOT index.html for redirection
    root_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Express Water - Redirecting...</title>
    <script>
        (function() {{
            var languages = {languages};
            var userLang = (navigator.language || navigator.userLanguage).toLowerCase().split('-')[0];
            if (languages.indexOf(userLang) !== -1) {{
                window.location.href = '/' + userLang + '/';
            }} else {{
                window.location.href = '/en/';
            }}
        }})();
    </script>
</head>
<body>
    <p>Redirecting... If you are not redirected, <a href="/en/">click here</a>.</p>
</body>
</html>
"""
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(root_html)
    print("Updated root index.html with redirect logic.")

if __name__ == "__main__":
    generate()
