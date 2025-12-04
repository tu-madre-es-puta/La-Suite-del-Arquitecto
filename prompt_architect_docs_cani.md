# La Suite del Arquitecto: Documentación Full (Versión 1.3.1)
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
Stack: React + Tailwind + Babel (CDN). No uses `npm install` o te caneo.