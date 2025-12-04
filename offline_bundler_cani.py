import os
import requests

INPUT_HTML = "prompt_architect_app_cani.html"
OUTPUT_DIR = "offline_dist"
LIBS_DIR = "libs"
DEPENDENCIES = {
    "https://cdn.tailwindcss.com": "tailwindcss.js",
    "https://unpkg.com/react@18/umd/react.development.js": "react.development.js",
    "https://unpkg.com/react-dom@18/umd/react-dom.development.js": "react-dom.development.js",
    "https://unpkg.com/@babel/standalone/babel.min.js": "babel.min.js",
    "https://unpkg.com/lucide@latest": "lucide.js"
}

def main():
    if not os.path.exists(INPUT_HTML):
        print(f"[!] No encuentro {INPUT_HTML}")
        return
    if not os.path.exists(os.path.join(OUTPUT_DIR, LIBS_DIR)): os.makedirs(os.path.join(OUTPUT_DIR, LIBS_DIR))
    
    print(f"=== Modo Búnker ===")
    for url, filename in DEPENDENCIES.items():
        print(f"[*] Bajando {url}...")
        try:
            r = requests.get(url)
            with open(os.path.join(OUTPUT_DIR, LIBS_DIR, filename), 'wb') as f: f.write(r.content)
        except: print(f"[!] Error bajando {url}")

    with open(INPUT_HTML, 'r', encoding='utf-8') as f: content = f.read()
    for url, filename in DEPENDENCIES.items():
        content = content.replace(url, f"./{LIBS_DIR}/{filename}")
    
    with open(os.path.join(OUTPUT_DIR, "index_offline.html"), 'w', encoding='utf-8') as f: f.write(content)
    print("\n[TRIUNFADA] Ya lo tienes en offline_dist/")

if __name__ == "__main__": main()