import requests
import json
import datetime

# CONFIGURACIÓN TOCHA
HF_API_URL = "https://huggingface.co/api/models"
LIMIT = 10
TAGS = ["gguf"]

def pillar_modelos_top():
    params = {"sort": "downloads", "direction": "-1", "limit": LIMIT, "filter": "gguf", "full": "true"}
    print(f"[*] Ojo, preguntando a Hugging Face por los {LIMIT} modelos más tochos...")
    try:
        response = requests.get(HF_API_URL, params=params)
        response.raise_for_status()
        models = response.json()
        recomendaciones = []
        for m in models:
            model_id = m.get('modelId', 'Ni idea')
            likes = m.get('likes', 0)
            downloads = m.get('downloads', 0)
            desc = f"Modelo GGUF top con {downloads:,} descargas."
            recomendaciones.append({"keyword": model_id.split('/')[-1], "title": model_id, "text": desc, "stats": f"⭐ {likes} | ⬇️ {downloads}"})
        
        output = {"updated_at": datetime.datetime.now().isoformat(), "source": "HF API", "data": recomendaciones}
        print(json.dumps(output, indent=2))
        with open("recommendations.json", "w") as f: f.write(json.dumps(output, indent=2))
        print("\n[*] Guardao en recommendations.json, merci.")
    except Exception as e: print(f"[LIADA] {e}")

if __name__ == "__main__": pillar_modelos_top()