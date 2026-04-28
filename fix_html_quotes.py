import os, re

def process_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Fix the escaped quotes which broke the image path
    content = content.replace("<img src=\\\"../assets/logo.png\\\"", "<img src=\"../assets/logo.png\"")
    content = content.replace("<img src=\\\"assets/logo.png\\\"", "<img src=\"assets/logo.png\"")
    content = content.replace("alt=\\\"Express Water Logo\\\"", "alt=\"Express Water Logo\"")
    content = content.replace("width=\\\"120\\\"", "width=\"120\"")
    content = content.replace("height=\\\"32\\\"", "height=\"32\"")

    # Add Hero spacing for coordination
    if ".hero {" in content and "margin-top: 10px;" not in content:
        content = content.replace(".hero{", ".hero{margin-top:10px;")

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

