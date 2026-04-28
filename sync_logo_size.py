import os, re

# Reference dimensions from ecoexpresswater.com
REF_WIDTH = "120"
REF_HEIGHT = "118"

def process_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update CSS Logo height
    # Look for the Logo Polish block and update height
    if "/* Header & Logo Polish */" in content:
        content = re.sub(r"height: 32px !important;", f"height: {REF_HEIGHT}px !important;", content)
        content = re.sub(r"height: 32px;", f"height: {REF_HEIGHT}px;", content)

    # 2. Update the logo img tag in the HTML
    content = re.sub(r"<img src=\"([^\"]+logo\.png)\" alt=\"([^\"]+)\" width=\"\d+\" height=\"\d+\">",
                     f"<img src=\"\\1\" alt=\"\\2\" width=\"{REF_WIDTH}\" height=\"{REF_HEIGHT}\">", content)

    # 3. Adjust header padding if it is too tight for 118px
    # Original header-inner padding was 16px. 16+118+16 = 150px header.
    # We will ensure the header-inner allows the logo to breathe.
    content = content.replace("padding: 10px 0;", "padding: 15px 0;")

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

