import os, re

def process_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Fix the logo tag globally - strip any backslashes or extra quotes
    # Match the whole tag and replace with a clean one
    content = re.sub(r"<img src=[^>]*logo\.png[^>]*>", 
                     r"<img src=\"../assets/logo.png\" alt=\"Express Water Logo\" width=\"120\" height=\"32\">" if ".." in file_path else r"<img src=\"assets/logo.png\" alt=\"Express Water Logo\" width=\"120\" height=\"32\">", 
                     content)

    # 2. Fix Header CSS for coordination
    if "/* Header & Logo Polish */" in content:
        # Update the height to be even smaller if needed, but 32px is good.
        # Ensure the nav links are centered
        content = content.replace(".logo img {", ".logo img { height: 32px !important; ")
        content = content.replace(".header-inner {", ".header-inner { display: flex; align-items: center; padding: 10px 0; ")

    # 3. Hero Spacing & Title coordination
    # Shrink Hero Title slightly for better "coordination"
    content = content.replace("font-size:clamp(2.5rem,6vw,4.2rem)", "font-size:clamp(1.8rem,5vw,3.2rem)")
    
    # Add Margin Top to Hero
    if ".hero{" in content and "margin-top" not in content:
        content = content.replace(".hero{", ".hero{margin-top:20px;")
    elif ".hero {" in content and "margin-top" not in content:
        content = content.replace(".hero {", ".hero { margin-top: 20px; ")

    # 4. Final safety check on quotes in the logo src
    content = content.replace("src=\\\"../assets/logo.png\\\"", "src=\"../assets/logo.png\"")
    content = content.replace("src=\\\"assets/logo.png\\\"", "src=\"assets/logo.png\"")
    content = content.replace("src=\"\"../assets/logo.png\"\"", "src=\"../assets/logo.png\"")

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

