import os, re

css_fix = """
    /* Logo and Header Fixes */
    .logo img {
      height: 50px;
      width: auto;
      display: block;
      object-fit: contain;
    }
    .header-inner {
      padding: 12px 0;
    }
    @media (max-width: 768px) {
      .logo img { height: 40px; }
      .header-inner { padding: 8px 0; }
    }
"""

def process_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Insert CSS fix before </style>
    if "</style>" in content and ".logo img" not in content:
        content = content.replace("</style>", css_fix + "\n  </style>")
    
    # Also fix the logo img tag in the HTML (ensure no hardcoded width/height overrides)
    content = re.sub(r"<img src=\"([^\"]+logo\.png)\" alt=\"([^\"]+)\" width=\"\d+\" height=\"\d+\">", 
                     r"<img src=\"\1\" alt=\"\2\" width=\"180\" height=\"50\">", content)

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
        print(f"Fixed {path}")

