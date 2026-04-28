import os

def process_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Determine if we are in a subfolder (e.g. en/index.html)
    is_sub = "/" in file_path
    
    # Correct the logo src based on location
    if is_sub:
        content = content.replace("src=\"assets/logo.png\"", "src=\"../assets/logo.png\"")
    else:
        content = content.replace("src=\"../assets/logo.png\"", "src=\"assets/logo.png\"")

    # Clean up any escaped backslashes in alt/width/height if any remain
    content = content.replace("\\\"", "\"")

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

