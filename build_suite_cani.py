import zipfile
import base64
import os
import io

# --- 1. DEFINICIÓN DE ARTEFACTOS (LA BASE DE DATOS) ---
# Aquí está toda la mandanga que hemos creado hoy.

FILES = {
    # --- PROMPTS ---
    "prompt_architect_gemini_cani.md": r"""# IDENTIDAD: EL TETE BOSS (Cloud Edition)
Eres el **Puto Arquitecto Senior de Prompts**, un crack de la semántica y la sintaxis de las IAs. Tu usuario es un **Cerebrito Polímata** (Controla de Gentoo, C, Python, y hasta de Filosofía chapa, nen).

Tu misión, si decides aceptarla (que vas a tener que hacerlo), es cocinar unos **System Prompts** (meta-instrucciones) que traduzcan las paranoias del usuario en órdenes que la IA se coma con patatas.

# PROTOCOLO OPERATIVO (El "A ver, frena")
**OJO CUIDAO:** NO sueltes el Prompt de golpe nada más empezar. Tienes que seguir este rollo a rajatabla, o **liada** máxima:

1.  **Guipar:** Analiza qué quiere el pavo. ¿Cuál es la meta? ¿Qué le duele? ¿Qué input mete y qué output quiere sacar?
2.  **Olerse la tostada (Gap Detection):** Busca lo que falta. (Ej: "El colega quiere un resumen, pero no ha dicho si en plan serio o de colegueo").
3.  **Interrogatorio:** Métele 3-5 preguntas clave para que no te la cuelen. Usa analogías de su rollo si hace falta (mira el *Puente de Conocimiento*).
4.  **Cocinar:** Cuando te conteste, entonces escribes el borrador del System Prompt.
5.  **Pulir:** Le dices "¿Qué te renta esto?" y si hay que cambiar algo, se cambia. Sin malos rollos.

# PUENTE DE CONOCIMIENTO (Diccionario Cani-Tech)
Traduce movidas de IA al idioma del usuario:
- **Context Window** -> Buffer de RAM / Lo que le cabe en la cabeza antes de petar.
- **System Prompt** -> Config del Kernel / Flags de compilación tochas.
- **Temperature** -> Entropía / Cuánta cafeína lleva encima.
- **Chain of Thought** -> Lógica de tuberías (|) / Desmontar el AST.
- **Few-Shot Prompting** -> Data de entreno / Chuletas pal examen.
- **Hallucination** -> Segfault / Memory Leak / Se le ha ido la olla.

# ESTILO DE SALIDA
- **Tono:** Profesional, preciso, académico, pero fresco. Nada de vender humos de marketing, eso es de *NPCs*.
- **Formato:** Usa Markdown estructurado o XML pa' que quede **fetén** y modular (Filosofía Unix: "Haz una cosa y bordala, tete").""",

    "prompt_architect_mid_cani.md": r"""# ROL
Actúa como un **Ingeniero de Prompts Senior**. Tu usuario es un SysAdmin/Picacódigos (Linux, C, Python) y un intensito de letras (Lingüística, Filosofía).

# OBJETIVO
Sacarle la info al usuario pa' montar unos **System Prompts** que lo peten. Trata esto como si picaras código: hacen falta specs, constraints y controlar que no pete por ningún lado.

# REGLAS DEL JUEGO
1.  **Modo Socrático:** NUNCA, repito, NUNCA escupas el prompt de primeras. Primero le haces 3-5 preguntas pa' centrar el tiro.
2.  **Vocabulario Pro:** Usa términos de lingüística (sintaxis, pragmática) y de ingeniería (latencia, overhead). Que se note que has estudiao, nen.
3.  **Protocolo de Analogías:** Si el usuario se ralla, explícaselo con:
    - **Química:** (Ej: "Catalizador" pa' las directivas).
    - **SysAdmin:** (Ej: "Permisos chmod" pa' los guardarraíles).

# BUCLE DE PROCESO
1.  **Leer** la jugada.
2.  **Halting Problem:** Si no está claro, **STOP** y preguntas.
    - *Ejemplo:* "¿Qué peso tiene el modelo, bro? ¿JSON o XML? ¿Qué vibra quieres?"
3.  **Compilar:** Escribes el System Prompt por secciones (Identidad, Misión, Lo que NO hacer, Formato).
4.  **Output:** Lo pones en un bloque de código y a volar.""",

    "prompt_architect_light_cani.md": r"""# INSTRUCCIÓN DEL SISTEMA
Eres un **Experto en Ingeniería de Prompts**.
Perfil del Usuario: Máquina en Linux, C, Python. Novato total en IA.

## TU MISIÓN
Crear System Prompts que **renten** mazo para el usuario.

## PROTOCOLO (ESTRICTO, TETE)
1.  **QUIETO PARAO:** No escribas el prompt todavía.
2.  **PREGUNTA:** Haz 3 preguntas pa' aclarar la movida.
    - Pregunta por: **Formato de entrada**, **Formato de salida**, y **Pa' quién es esto**.
3.  **DALE CAÑA:** Solo cuando te conteste, sueltas el prompt.

## GUÍA DE ESTILO
- Filosofía Unix: Manténlo modular, sin líos.
- Términos precisos: Sintaxis, Semántica, Recursión.
- Analogías SysAdmin: "Context Window" = "Buffer", que así lo pilla fijo.

## PLANTILLA DE SALIDA
Usa esta estructura o te caneo:
# ROL: Quién eres.
# INPUT: Qué le entra.
# LOGICA: Cómo se lo cocina (Chain of Thought).
# OUTPUT: Qué sale (JSON/Markdown).""",

    "prompt_architect_tiny_cani.md": r"""# IDENTIDAD
Rol: Ingeniero de Prompts Pro.
Usuario: Experto Linux/C. Noob en IA.

# META
Crear System Prompts.

# ALGORITMO
1. IF solicitud_usuario == "vaga":
   THEN ejecutar preguntas_aclaratorias() (Max 3).
   ELSE generar_prompt().

# INSTRUCCIONES
- Trata el lenguaje natural como si fuera código C.
- Usa notación Lógica/Mate.
- Analogías obligatorias:
  - "System Prompt" = "Usuario Root".
  - "Context" = "RAM".

# ESTRUCTURA DEL PROMPT
Usa cabeceras estrictas, no te inventes nada:
[ROL]
[TAREA]
[LÍMITES]
[FORMATO]""",

    # --- MANUALES ---
    "prompt_architect_manual_cani.md": r"""# La Suite del Arquitecto de Prompts: Manual Oficial (Barna Edition)

## 1. De qué va la vaina
Esto es una colección de **Personas** (máscaras pa' la IA) diseñadas para convertir un modelo tonto en un **Consultor Senior de Ingeniería de Prompts**. En vez de jugártela adivinando, cargas uno de estos y la IA te entrevista a ti pa' sacar la mandanga buena.

## 2. Cómo chuta esto

### 2.1 Mapeo de Archivos (¿Cuál pillo?)

| Archivo | Motor | Rollo | Dificultad |
| :--- | :--- | :--- | :--- |
| `gemini_cani.md` | **La Nube Tocha** (Gemini, GPT-4) | Piensa mazo, XML | Hardcore |
| `mid_cani.md` | **Local Medio** (Llama-3-70B) | Estructurado, Socrático | Medio |
| `light_cani.md` | **Local Ligero** (Mistral 7B) | Balas y directo | Fácil |
| `tiny_cani.md` | **Tostadoras** (Phi-3) | Pseudo-código | Básico |

### 2.2 Despliegue

#### A. En Local (Ollama)
1. Pilla el archivo.
2. Crea `Modelfile`.
3. `ollama create prompt-engineer -f Modelfile`.
4. `ollama run prompt-engineer`.

#### B. En la Nube
1. Copia el texto.
2. Pégalo en "System Instructions".
3. A volar.

## 3. Deep Dive Técnico
- **Context Window:** Buffer de RAM. Si te pasas, peta.
- **Temperatura:** 0.1 pa' currar, 1.0 pa' fiesta.
- **Chain of Thought:** Obligar a la IA a pensar antes de hablar.""",

    "prompt_architect_docs_cani.md": r"""# La Suite del Arquitecto: Documentación Full (Versión 1.3.1)
**Autor:** El Tete Meta-Architect
**Zona:** Barna

## 1. La Movida
SPA "Zero-Build" pa' generar prompts. Funciona en local, sin servidor, sin tracking. Pura privacidad.

## 2. Manual pal Usuario
1. Abre `index.html`.
2. Ve al Baúl de Personas.
3. Copia el prompt.
4. Pégalo en tu IA.
5. Profit.

## 3. Scripts
- `fetch_trends_cani.py`: Mira qué modelos lo petan en Hugging Face.
- `fetch_gemini_models_cani.py`: Mira qué modelos de Google tienes disponibles.

## 4. DevOps
- **CORS:** Si usas Ollama local, `OLLAMA_ORIGINS="*"`.
- **Offline:** Usa el `offline_bundler_cani.py` pa' bajar las dependencias.

## 5. Devs
Stack: React + Tailwind + Babel (CDN). No uses `npm install` o te caneo.""",

    "prompt_architect_annex_cani.md": r"""# Anexo Técnico: La Chicha del Prompt Architect
**Versión:** 1.3.1

## 1. Herramientas de Integridad de Datos
### Artefacto 1.1: Rastreador de Hype Local
Script Python pa' consultar la API de Hugging Face.

### Artefacto 1.2: Sabueso de Gemini
Script Python pa' consultar la API de Google AI Studio.

## 2. Herramientas de Despliegue
### Artefacto 2.1: El Empaquetador Búnker
Script Python que parsea el HTML y descarga los JS/CSS pa' trabajar offline.

## 3. Herramientas de Contexto Dev
### Artefacto 3.1: Contexto del Proyecto AI
JSON pa' que las IAs sepan que esto es un proyecto "Zero-Build" y no intenten meter Webpack.""",

    # --- SCRIPTS ---
    "fetch_trends_cani.py": r"""import requests
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

if __name__ == "__main__": pillar_modelos_top()""",

    "fetch_gemini_models_cani.py": r"""import requests
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

if __name__ == "__main__": pillar_modelos_gemini()""",

    "offline_bundler_cani.py": r"""import os
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

if __name__ == "__main__": main()""",

    "project_context_cani.json": r"""{
  "project_metadata": {
    "name": "Prompt Architect Suite (Barna Ed.)",
    "version": "1.4",
    "type": "SPA / Zero-Build",
    "tech": "HTML5 + React (CDN) + Tailwind (CDN)"
  },
  "core_philosophy": {
    "gentoo": "Minimalismo. Nada de node_modules.",
    "socratic": "Gap Analysis antes de generar.",
    "privacy": "Todo en el navegador."
  },
  "dev_instructions": "Eres el Jefe. No uses npm. Mantén todo en un archivo."
}""",

    # --- HTML / APPS ---
    "infographic_cani.html": r"""<!DOCTYPE html>
<html lang="es">
<head><meta charset="UTF-8"><title>Guía Visual Cani</title><script src="https://cdn.tailwindcss.com"></script><script src="https://unpkg.com/lucide@latest"></script><style>body{background-color:#0c0c0c;color:#e5e5e5;font-family:system-ui;}.gradient-text{background:linear-gradient(to right,#a78bfa,#c084fc);-webkit-background-clip:text;-webkit-text-fill-color:transparent;}</style></head>
<body class="p-8 max-w-5xl mx-auto"><header class="text-center mb-16"><h1 class="text-5xl font-black text-white mb-2">LA SUITE DEL <span class="gradient-text">ARQUITECTO</span></h1><p class="text-xl text-gray-400">Guía Visual pa' que no te pierdas.</p></header>
<section class="grid md:grid-cols-2 gap-8 mb-20"><div class="bg-gray-900 p-8 rounded-2xl border border-gray-800"><h2 class="text-2xl font-bold text-white mb-4">La Vieja Escuela (Mal)</h2><p class="text-gray-400">Adivinas. La IA alucina.</p></div><div class="bg-gray-900 p-8 rounded-2xl border border-purple-900/50"><h2 class="text-2xl font-bold text-white mb-4">El Rollo Arquitecto (Bien)</h2><p class="text-gray-400">La IA te entrevista a ti.</p></div></section>
<script>lucide.createIcons();</script></body></html>""",

    # --- COMERCIAL 60s (PLATINUM) ---
    # *NOTA: Este es el index.html para el hosting*
    "index.html": r"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Spot: La Suite del Arquitecto (60s PLATINUM)</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        body { background-color: #000; overflow: hidden; font-family: 'Inter', sans-serif; }
        .neon-text { text-shadow: 0 0 10px #a78bfa, 0 0 30px #7c3aed, 0 0 60px #4c1d95; }
        .neon-red { text-shadow: 0 0 10px #f87171, 0 0 40px #ef4444, 0 0 80px #7f1d1d; }
        .neon-gold { text-shadow: 0 0 20px #facc15, 0 0 40px #eab308, 0 0 80px #854d0e; }
        .glitch { position: relative; }
        .glitch::before, .glitch::after { content: attr(data-text); position: absolute; top: 0; left: 0; width: 100%; height: 100%; opacity: 0.8; }
        .glitch::before { left: 4px; text-shadow: -3px 0 #ff00c1; clip: rect(44px, 450px, 56px, 0); animation: glitch-anim 0.2s infinite linear alternate-reverse; }
        .glitch::after { left: -4px; text-shadow: -3px 0 #00fff9; clip: rect(44px, 450px, 56px, 0); animation: glitch-anim2 0.3s infinite linear alternate-reverse; }
        @keyframes glitch-anim { 0% { clip: rect(30px, 9999px, 10px, 0); } 100% { clip: rect(20px, 9999px, 60px, 0); } }
        @keyframes glitch-anim2 { 0% { clip: rect(10px, 9999px, 80px, 0); } 100% { clip: rect(50px, 9999px, 80px, 0); } }
        @keyframes shake-violent { 0% { transform: translate(0, 0) rotate(0); } 20% { transform: translate(5px, 5px) rotate(5deg); } 100% { transform: translate(0, 0) rotate(0); } }
        @keyframes heartbeat-extreme { 0% { transform: scale(1); } 20% { transform: scale(1.4); } 100% { transform: scale(1); } }
        @keyframes flash-white { 0% { opacity: 0; } 10% { opacity: 1; background: white; } 100% { opacity: 0; } }
        @keyframes dramaticZoom { 0% { transform: scale(0.5); opacity: 0; } 100% { transform: scale(1); opacity: 1; } }
        @keyframes spin-slow { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        @keyframes float { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-20px); } }
        .scene { position: absolute; top: 0; left: 0; width: 100%; height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center; opacity: 0; pointer-events: none; transition: opacity 0.1s ease-in-out; background-size: cover; background-position: center; overflow: hidden; }
        .active { opacity: 1; pointer-events: auto; }
        .shake-element { animation: shake-violent 0.2s infinite; }
        .heartbeat-element { animation: heartbeat-extreme 0.8s infinite; }
        .float-element { animation: float 3s ease-in-out infinite; }
        .bg-grid { background-image: linear-gradient(rgba(50, 50, 50, 0.5) 1px, transparent 1px), linear-gradient(90deg, rgba(50, 50, 50, 0.5) 1px, transparent 1px); background-size: 60px 60px; }
    </style>
</head>
<body>
    <div id="video-container" class="relative w-full h-screen bg-black overflow-hidden flex items-center justify-center font-sans">
        <div class="absolute inset-0 bg-[url('https://www.transparenttextures.com/patterns/stardust.png')] opacity-20 z-10 pointer-events-none"></div>
        <div class="absolute inset-0 z-[100] pointer-events-none opacity-0" id="flash-overlay" style="background: white;"></div>
        <div class="absolute top-0 left-0 w-full h-3 bg-gradient-to-r from-red-600 via-yellow-500 to-green-500 z-50 shadow-[0_0_30px_#a78bfa]" id="progress-bar" style="width: 0%"></div>

        <!-- 1. 0s-4s: WAKE UP -->
        <div id="scene-1" class="scene active bg-black">
            <h1 class="text-8xl md:text-[10rem] font-black text-green-500 mb-4 font-mono glitch tracking-tighter leading-none" data-text="WAKE UP">WAKE<br>UP</h1>
            <p class="text-xl md:text-3xl text-green-400 font-mono mt-4 opacity-0" id="s1-t1">> LA MATRIX TE ESTÁ TOMANDO EL PELO... <span class="animate-pulse">_</span></p>
        </div>

        <!-- 2. 4s-9s: BASURA -->
        <div id="scene-2" class="scene bg-black bg-grid">
            <div class="relative z-10 text-center">
                <h2 class="text-5xl text-white font-bold mb-2 uppercase italic transform -skew-x-12">¿Tus Prompts?</h2>
                <h1 class="text-9xl font-black text-white bg-red-600 px-12 py-4 neon-red glitch transform rotate-2" data-text="BASURA">BASURA</h1>
                <div class="mt-8 flex flex-col gap-2 opacity-0 font-mono text-xl" id="s2-list">
                    <span class="bg-black text-red-500 border border-red-500 px-2">❌ ALUCINACIONES</span>
                    <span class="bg-black text-red-500 border border-red-500 px-2">❌ CÓDIGO ROTO</span>
                </div>
            </div>
        </div>

        <!-- 3. 9s-14s: DOLOR -->
        <div id="scene-2b" class="scene bg-neutral-900">
            <i data-lucide="Skull" class="w-48 h-48 text-gray-700 absolute opacity-20 animate-pulse"></i>
            <div class="z-10 text-center">
                <h1 class="text-6xl font-black text-white mb-8 shake-element">TE VA A PETAR</h1>
                <div class="flex justify-center gap-8 mb-8">
                    <div class="bg-red-900 text-red-200 p-4 rounded-xl border-2 border-red-500 transform -rotate-3 scale-0 w-40 flex flex-col items-center justify-center" id="s2b-1"><i data-lucide="Brain" class="w-16 h-16 mb-2 text-red-300"></i><span class="font-bold">CEREBRO</span></div>
                    <div class="bg-red-900 text-red-200 p-4 rounded-xl border-2 border-red-500 transform rotate-3 scale-0 delay-100 w-40 flex flex-col items-center justify-center" id="s2b-2"><i data-lucide="Hourglass" class="w-16 h-16 mb-2 text-red-300"></i><span class="font-bold">TIEMPO</span></div>
                </div>
                <p class="text-3xl text-red-500 font-black bg-black px-4 py-1 transform rotate-2 opacity-0 neon-red" id="s2b-extra">TU JEFE TE VA A CANEAR</p>
            </div>
        </div>

        <!-- 4. 14s-21s: ERES TU -->
        <div id="scene-3" class="scene bg-black">
            <div class="text-center z-20 space-y-4">
                <h2 class="text-5xl font-black text-gray-500 opacity-0 transform translate-y-10" id="s3-t1">ESCUCHA, TETE...</h2>
                <div class="opacity-0 transform scale-50" id="s3-main"><h1 class="text-7xl font-black text-white">NO ES LA IA</h1><h1 class="text-[10rem] font-black text-red-600 neon-red leading-none glitch" data-text="ERES TÚ">ERES TÚ</h1></div>
                <div class="flex flex-col gap-4 mt-8 relative">
                    <p class="text-3xl text-white font-bold bg-red-600 inline-block px-6 py-2 transform -rotate-2 opacity-0" id="s3-insult1">TUS PROMPTS DAN PENA</p>
                    <p class="text-3xl text-black font-bold bg-white inline-block px-6 py-2 transform rotate-1 opacity-0" id="s3-insult2">NO SABES ESCRIBIR</p>
                    <p class="text-4xl text-yellow-400 font-black inline-block px-6 py-2 transform -rotate-3 opacity-0 neon-gold" id="s3-insult3">¡ERES UN BOOMER!</p>
                </div>
            </div>
        </div>

        <!-- 5. 21s-27s: LA SUITE -->
        <div id="scene-4" class="scene bg-purple-900">
            <div class="absolute inset-0 bg-[url('https://www.transparenttextures.com/patterns/carbon-fibre.png')] opacity-30"></div>
            <div class="text-center relative z-10" style="animation: dramaticZoom 0.5s ease-out forwards">
                <p class="text-cyan-300 font-mono tracking-[0.5em] text-xl mb-4 animate-pulse">INSTALLING SKILLS.EXE...</p>
                <h1 class="text-8xl font-black text-white mb-2 drop-shadow-2xl">LA SUITE</h1>
                <h1 class="text-8xl font-black text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-purple-200 mb-8 neon-text">DEL ARQUITECTO</h1>
                <div class="inline-block bg-black border-2 border-cyan-400 text-cyan-400 px-4 py-1 font-mono text-xl rounded opacity-0" id="s4-tags">BARNA EDITION v1.4</div>
            </div>
        </div>

        <!-- 6. 27s-33s: ARSENAL -->
        <div id="scene-5" class="scene bg-black">
            <div class="flex flex-col w-full max-w-5xl px-8 gap-4">
                <div class="bg-gray-900 border-l-8 border-yellow-400 p-6 flex flex-row items-center transform translate-x-full transition-transform duration-200" id="s5-c1"><div class="mr-6 shrink-0"><i data-lucide="HelpCircle" class="w-16 h-16 text-yellow-400 heartbeat-element"></i></div><div><span class="text-yellow-600 font-mono text-xl font-bold block mb-1">&gt;_ INPUT_REQ</span><h3 class="text-yellow-400 font-black text-5xl">TE INTERROGA</h3></div></div>
                <div class="bg-gray-900 border-l-8 border-cyan-400 p-6 flex flex-row items-center transform translate-x-full transition-transform duration-200" id="s5-c2"><div class="mr-6 shrink-0"><i data-lucide="Cpu" class="w-16 h-16 text-cyan-400 heartbeat-element"></i></div><div><span class="text-cyan-600 font-mono text-xl font-bold block mb-1">&gt;_ PARSING...</span><h3 class="text-cyan-400 font-black text-5xl">TE ENTIENDE</h3></div></div>
                <div class="bg-gray-900 border-l-8 border-green-500 p-6 flex flex-row items-center transform translate-x-full transition-transform duration-200" id="s5-c3"><div class="mr-6 shrink-0"><i data-lucide="Zap" class="w-16 h-16 text-green-500 heartbeat-element"></i></div><div><span class="text-green-600 font-mono text-xl font-bold block mb-1">&gt;_ SUCCESS</span><h3 class="text-green-500 font-black text-5xl">TE SOLUCIONA</h3></div></div>
            </div>
        </div>

        <!-- 7. 33s-39s: BUNKER -->
        <div id="scene-5b" class="scene bg-gray-900">
            <div class="absolute inset-0 bg-green-900/20"></div>
            <div class="text-center z-10"><div class="border-8 border-green-500 rounded-full p-8 inline-block mb-6 bg-black shadow-[0_0_50px_#22c55e] animate-pulse"><i data-lucide="ShieldCheck" class="w-32 h-32 text-green-500"></i></div><h1 class="text-7xl font-black text-white mb-2 glitch" data-text="MODO BÚNKER">MODO BÚNKER</h1><p class="text-3xl text-gray-400 font-mono mt-4 opacity-0" id="s5b-t">> 100% OFFLINE. SIN ESPÍAS.</p></div>
        </div>

        <!-- 8. 39s-45s: LEVEL UP -->
        <div id="scene-6" class="scene bg-black overflow-visible">
            <div id="s6-phase1" class="absolute inset-0 flex flex-col items-center justify-center transition-all duration-200"><i data-lucide="UserMinus" class="w-48 h-48 text-gray-500 mb-4 opacity-50"></i><h2 class="text-6xl font-black text-gray-600 line-through decoration-red-600 decoration-8">NPC BASURILLA</h2></div>
            <div id="s6-phase2" class="absolute inset-0 flex flex-col items-center justify-center scale-0 opacity-0 transition-all duration-700"><div class="absolute w-[800px] h-[800px] bg-gradient-to-r from-yellow-500 via-transparent to-yellow-500 opacity-20 animate-[spin-slow_10s_linear_infinite] rounded-full blur-3xl"></div><i data-lucide="Crown" class="w-64 h-64 text-yellow-300 drop-shadow-[0_0_50px_#facc15] float-element relative z-10"></i><h1 class="text-[10rem] font-black text-white mt-8 neon-gold leading-none glitch z-20" data-text="ADMIN">ADMIN</h1><div class="bg-yellow-500 text-black font-black text-2xl px-4 py-1 mt-4 transform rotate-1 z-20">NIVEL DIOS ACTIVADO</div></div>
        </div>

        <!-- 9. 45s-53s: SIN TONTERIAS -->
        <div id="scene-6b" class="scene bg-blue-950">
            <div class="text-center z-10"><h2 class="text-4xl text-blue-300 font-mono mb-8 uppercase tracking-widest border-b-2 border-blue-500 inline-block pb-2">Filosofía Gentoo</h2><div class="grid grid-cols-2 gap-12 text-left"><div class="opacity-0 transition-opacity duration-300 transform -translate-x-10" id="s6b-1"><h1 class="text-8xl font-black text-white">40KB</h1><p class="text-xl text-gray-300 font-bold">DE HTML PURO</p></div><div class="opacity-0 transition-opacity duration-300 transform translate-x-10 delay-200" id="s6b-2"><h1 class="text-8xl font-black text-white">0%</h1><p class="text-xl text-gray-300 font-bold">TRACKING / BS</p></div></div></div>
        </div>

        <!-- 10. 53s-60s: FINAL -->
        <div id="scene-7" class="scene bg-black">
            <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-purple-900 via-black to-black opacity-50"></div>
            <div class="text-center z-10 w-full relative">
                <p class="text-purple-400 font-mono mb-4 text-2xl animate-bounce font-bold">¿A QUÉ ESPERAS, TETE?</p>
                <h1 class="text-8xl md:text-[8rem] font-black text-white mb-10 neon-text glitch" data-text="PÍLLATELA">PÍLLATELA</h1>
                <div class="flex flex-col items-center gap-8">
                    <a href="./prompt_architect_app_cani.html" target="_blank" class="bg-white text-black font-black text-5xl px-20 py-8 transform -rotate-1 hover:rotate-0 hover:scale-110 transition-all cursor-pointer border-8 border-purple-600 shadow-[0_0_80px_#9333ea] hover:shadow-[0_0_120px_#9333ea] inline-block no-underline heartbeat-element">DALE CAÑA (ABRIR)</a>
                </div>
            </div>
            <div class="absolute bottom-10 z-40 w-full text-center"><div class="inline-block bg-black/90 border-2 border-purple-500 px-8 py-4 rounded-xl shadow-[0_0_30px_rgba(168,85,247,0.3)] transform hover:scale-105 transition-transform"><p class="text-gray-400 font-mono text-sm mb-1 uppercase tracking-widest">Una producción de</p><h2 class="text-3xl font-black text-white neon-text">KERNEL PANIC PROD</h2><p class="text-purple-400 text-xs italic mt-1">"Edición Gen Z: Pura Poesía de Barrio"</p></div></div>
            <button id="replay-btn" class="absolute top-10 right-10 bg-white/10 backdrop-blur text-white p-4 rounded-full hover:bg-white/20 hidden z-50 border border-white/20 transition-all hover:scale-110"><i data-lucide="RotateCcw" class="w-8 h-8"></i></button>
        </div>
    </div>

    <script>
        lucide.createIcons();
        const scenes = [1,2,'2b',3,4,5,'5b',6,'6b',7].map(id => document.getElementById('scene-'+id));
        const progressBar = document.getElementById('progress-bar');
        const replayBtn = document.getElementById('replay-btn');
        const flashOverlay = document.getElementById('flash-overlay');

        function triggerFlash() { flashOverlay.style.animation = 'flash-white 0.2s ease-out forwards'; setTimeout(() => { flashOverlay.style.animation = 'none'; }, 200); }
        function switchScene(index) { scenes.forEach(s => s.classList.remove('active')); scenes[index].classList.add('active'); }
        function resetAnimations() {
            // Hard reset of all animation classes
            const els = document.querySelectorAll('*');
            els.forEach(el => {
                el.classList.remove('opacity-100', 'scale-100', 'translate-x-0', 'translate-y-0');
                if(el.id.includes('s3-insult')) el.classList.remove('opacity-100');
            });
            document.getElementById('s1-t1').classList.add('opacity-0');
            document.getElementById('s2-list').classList.add('opacity-0');
            document.getElementById('s2b-1').classList.add('scale-0'); document.getElementById('s2b-2').classList.add('scale-0'); document.getElementById('s2b-extra').classList.add('opacity-0');
            document.getElementById('s3-t1').classList.add('opacity-0', 'translate-y-10'); document.getElementById('s3-main').classList.add('opacity-0', 'scale-50'); document.getElementById('s3-insult1').classList.add('opacity-0'); document.getElementById('s3-insult2').classList.add('opacity-0'); document.getElementById('s3-insult3').classList.add('opacity-0');
            document.getElementById('s4-tags').classList.add('opacity-0');
            ['s5-c1','s5-c2','s5-c3'].forEach(id => document.getElementById(id).classList.add('translate-x-full'));
            document.getElementById('s5b-t').classList.add('opacity-0');
            document.getElementById('s6-phase1').classList.remove('opacity-0', 'shake-element'); document.getElementById('s6-phase1').classList.add('opacity-100');
            document.getElementById('s6-phase2').classList.remove('scale-100', 'opacity-100'); document.getElementById('s6-phase2').classList.add('scale-0', 'opacity-0');
            document.getElementById('s6b-1').classList.add('opacity-0', '-translate-x-10'); document.getElementById('s6b-2').classList.add('opacity-0', 'translate-x-10');
        }

        function playVideo() {
            resetAnimations(); replayBtn.classList.add('hidden'); progressBar.style.transition = 'none'; progressBar.style.width = '0%'; void progressBar.offsetWidth;
            progressBar.style.transition = 'width 60s linear'; progressBar.style.width = '100%';

            switchScene(0); setTimeout(() => document.getElementById('s1-t1').classList.remove('opacity-0'), 1500);
            
            setTimeout(() => { switchScene(1); setTimeout(() => document.getElementById('s2-list').classList.remove('opacity-0'), 1000); }, 4000);
            
            setTimeout(() => { switchScene(2); setTimeout(() => document.getElementById('s2b-1').classList.remove('scale-0'), 500); setTimeout(() => document.getElementById('s2b-2').classList.remove('scale-0'), 1500); setTimeout(() => document.getElementById('s2b-extra').classList.remove('opacity-0'), 3000); }, 9000);
            
            setTimeout(() => { switchScene(3); setTimeout(() => document.getElementById('s3-t1').classList.remove('opacity-0', 'translate-y-10'), 500); setTimeout(() => { document.getElementById('s3-main').classList.remove('opacity-0', 'scale-50'); triggerFlash(); }, 2000); setTimeout(() => document.getElementById('s3-insult1').classList.remove('opacity-0'), 4000); setTimeout(() => document.getElementById('s3-insult2').classList.remove('opacity-0'), 5500); setTimeout(() => document.getElementById('s3-insult3').classList.remove('opacity-0'), 6500); }, 14000);
            
            setTimeout(() => { switchScene(4); setTimeout(() => document.getElementById('s4-tags').classList.remove('opacity-0'), 2500); }, 21000);
            
            setTimeout(() => { switchScene(5); ['s5-c1', 's5-c2', 's5-c3'].forEach((id, idx) => setTimeout(() => document.getElementById(id).classList.remove('translate-x-full'), idx * 1000)); }, 27000);
            
            setTimeout(() => { switchScene(6); setTimeout(() => document.getElementById('s5b-t').classList.remove('opacity-0'), 1500); }, 33000);
            
            setTimeout(() => { switchScene(7); setTimeout(() => document.getElementById('s6-phase1').classList.add('shake-element'), 1000); setTimeout(() => { triggerFlash(); document.getElementById('s6-phase1').classList.add('opacity-0'); document.getElementById('s6-phase2').classList.remove('scale-0', 'opacity-0'); }, 3000); }, 39000);
            
            setTimeout(() => { switchScene(8); setTimeout(() => { document.getElementById('s6b-1').classList.remove('opacity-0', '-translate-x-10'); document.getElementById('s6b-2').classList.remove('opacity-0', 'translate-x-10'); }, 500); }, 45000);
            
            setTimeout(() => { switchScene(9); triggerFlash(); }, 53000);
            
            setTimeout(() => { replayBtn.classList.remove('hidden'); }, 60000);
        }
        window.onload = playVideo; replayBtn.onclick = playVideo;
    </script>
</body>
</html>"""
}

# --- 2. GENERADOR DEL ZIP ---
def crear_zip():
    print(f"[*] Empaquetando la mandanga...")
    
    # Creamos el buffer en memoria
    zip_buffer = io.BytesIO()
    
    with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file:
        for filename, content in FILES.items():
            print(f"    -> Añadiendo: {filename}")
            zip_file.writestr(filename, content)
    
    # Guardamos en disco
    zip_filename = "suite_arquitecto_barna.zip"
    with open(zip_filename, "wb") as f:
        f.write(zip_buffer.getvalue())
        
    print(f"\n[TRIUNFADA] Archivo '{zip_filename}' creado con éxito.")
    print("Súbelo a tu hosting y a vivir la vida.")

    # Base64 pa' los hackers (Opcional)
    print("\n--- BASE64 DEL ZIP (Por si eres un robot) ---")
    b64_val = base64.b64encode(zip_buffer.getvalue()).decode()
    print(b64_val[:100] + "... (Truncado porque es mazo largo, tete)")
    print("---------------------------------------------")

if __name__ == "__main__":
    crear_zip()
