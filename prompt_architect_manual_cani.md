# La Suite del Arquitecto de Prompts: Manual Oficial (Barna Edition)

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
- **Chain of Thought:** Obligar a la IA a pensar antes de hablar.