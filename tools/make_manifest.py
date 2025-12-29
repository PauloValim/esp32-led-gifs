#!/usr/bin/env python3
import os, json, hashlib

# Diretório base dos GIFs
GIF_DIR = os.path.join(os.path.dirname(__file__), "..", "gifs")

BASE_URL = "https://raw.githubusercontent.com/PauloValim/esp32-led-gifs/main/gifs/"

manifest = {
    "version": 1,
    "base_url": BASE_URL,
    "files": []
}

def sha1sum(path):
    h = hashlib.sha1()
    with open(path, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

for name in sorted(os.listdir(GIF_DIR)):
    if not name.lower().endswith(".gif"):
        continue
    path = os.path.join(GIF_DIR, name)
    size = os.path.getsize(path)
    manifest["files"].append({
        "name": name,
        "bytes": size,
        "sha1": sha1sum(path)
    })

manifest_path = os.path.join(os.path.dirname(__file__), "..", "manifest.json")
with open(manifest_path, "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)

print(f"Manifesto gerado: {manifest_path}")
