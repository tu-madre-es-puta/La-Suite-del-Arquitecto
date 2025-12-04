import requests
import json
import datetime
import getpass
import os

def pillar_modelos_gemini():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key: api_key = getpass.getpass("Pásame la Key de Google: ")
    if not api_key: return
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
    print("[*] Llamando a Google...")
    try:
        response = requests.get(url)
        data = response.json()
        if "models" not in data: return
        recomendaciones = []
        for m in data["models"]:
            name = m.get("name", "").replace("models/", "")
            if "gemini" in name.lower() and "generateContent" in m.get("supportedGenerationMethods", []):
                recomendaciones.append({"keyword": name, "title": m.get("displayName", name), "text": m.get("description", ""), "stats": f"Input: {m.get('inputTokenLimit',0)}"})
        
        output = {"updated_at": datetime.datetime.now().isoformat(), "source": "Google API", "data": recomendaciones}
        print(json.dumps(output, indent=2))
        with open("gemini_models.json", "w") as f: f.write(json.dumps(output, indent=2))
        print(f"\n[*] Guardao.")
    except Exception as e: print(f"[ERROR] {e}")

if __name__ == "__main__": pillar_modelos_gemini()