#!/usr/bin/env python3
import json, os, urllib.request, ssl, re, concurrent.futures

with open("master_manifest.json", "r", encoding="utf-8") as f:
    m = json.load(f)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

os.makedirs("assets/products", exist_ok=True)
os.makedirs("assets/workshop", exist_ok=True)
os.makedirs("assets/exhibition", exist_ok=True)

def safe_filename(url):
    base = url.split("/")[-1].split("?")[0]
    base = re.sub(r"[^a-zA-Z0-9._\-]", "_", base)
    return base[:80]

def download(task):
    url, local = task
    if os.path.exists(local) and os.path.getsize(local) > 1000:
        return (url, local, "cached", os.path.getsize(local))
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=20, context=ctx) as r:
            data = r.read()
        with open(local, "wb") as f:
            f.write(data)
        return (url, local, "ok", len(data))
    except Exception as e:
        return (url, local, "ERR: " + str(e)[:80], 0)

tasks = []
mapping = {}

# hero
hero_local = "assets/hero.jpg"
tasks.append((m["hero_image"], hero_local))
mapping[m["hero_image"]] = hero_local

# products
for p in m["products"]:
    fn = safe_filename(p["image"])
    pid = p["id"]
    local = "assets/products/" + pid + "_" + fn
    tasks.append((p["image"], local))
    mapping[p["image"]] = local

# workshop
for i, w in enumerate(m["workshop_images"]):
    fn = safe_filename(w["url"])
    local = "assets/workshop/" + str(i + 1) + "_" + fn
    tasks.append((w["url"], local))
    mapping[w["url"]] = local

# exhibition
for i, e in enumerate(m["exhibition_images"]):
    fn = safe_filename(e["url"])
    local = "assets/exhibition/" + str(i + 1) + "_" + fn
    tasks.append((e["url"], local))
    mapping[e["url"]] = local

print("Downloading " + str(len(tasks)) + " images in parallel...")

results = {"ok": 0, "cached": 0, "err": 0}
errors = []
with concurrent.futures.ThreadPoolExecutor(max_workers=12) as ex:
    for url, local, status, size in ex.map(download, tasks):
        if status == "ok":
            results["ok"] += 1
        elif status == "cached":
            results["cached"] += 1
        else:
            results["err"] += 1
            errors.append((url, status))
            print("FAILED: " + url + " -> " + status)

print("\nDONE: %d downloaded, %d cached, %d errors" % (results["ok"], results["cached"], results["err"]))

# update manifest with local paths
m["hero_image_local"] = mapping[m["hero_image"]]
for p in m["products"]:
    p["image_local"] = mapping[p["image"]]
for w in m["workshop_images"]:
    w["url_local"] = mapping[w["url"]]
for e in m["exhibition_images"]:
    e["url_local"] = mapping[e["url"]]

with open("master_manifest.json", "w", encoding="utf-8") as f:
    json.dump(m, f, indent=2, ensure_ascii=False)

with open("image_mapping.json", "w") as f:
    json.dump(mapping, f, indent=2)

print("Manifest updated.")
