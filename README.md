# 🌿 Aplicación Web Flask - Stack & Arquitecturas de Software

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0.0-000000?style=for-the-badge&logo=flask&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Render](https://img.shields.io/badge/Render-Deployed-46E3B7?style=for-the-badge&logo=render&logoColor=white)
![Licencia](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

Aplicación web construida con **Python** y **Flask**, con estilo orgánico inspirado en la naturaleza
(*glassmorphism*, SVG y micro-animaciones). Incluye una **sección creativa personal**, un **quiz
interactivo sobre Stack y Arquitecturas de Software** validado por el servidor, y está lista para
desplegarse en la nube con **Gunicorn y Render**.

> 👤 Autor: **Pedro Juan Mendoza Ovallos** — Estudiante de Ingeniería de Software II

---

## ✨ Funcionalidades

- **Página principal** con hero, estado del servidor y tarjetas ilustrativas del stack elegido.
- **Sección creativa "Sobre mí"** con el nombre, rol animado (efecto de escritura), biografía y
  etiquetas del stack tecnológico.
- **Quiz: Stack y Arquitecturas de Software**
  - 10 preguntas sobre stacks tecnológicos y estilos arquitectónicos (monolito, capas,
    cliente-servidor, microservicios, SOA, REST…).
  - Interfaz en JavaScript sin recarga de página.
  - Validación en el servidor Flask con puntaje, porcentaje, estados correcto/incorrecto y
    explicación de cada respuesta.

---

## 🛠️ Tecnologías Utilizadas

- **Backend**: Python 3, Flask, Gunicorn
- **Frontend**: HTML5, CSS3 (variables, Grid, Flexbox, Glassmorphism), JavaScript (Fetch API)
- **Recursos**: SVG vectorial, Google Fonts (*Playfair Display* & *Plus Jakarta Sans*)
- **Control de versiones**: Git & GitHub
- **Despliegue**: Render (nube)

---

## 🧪 Endpoints de la API

| Método | Ruta                | Descripción                                                        |
| ------ | ------------------- | ------------------------------------------------------------------ |
| `GET`  | `/`                 | Página principal (HTML).                                           |
| `GET`  | `/api/quiz`         | Devuelve las preguntas del quiz en JSON (sin las respuestas).      |
| `POST` | `/api/quiz/submit`  | Recibe `{ "answers": { "<id>": índice } }` y devuelve el resultado. |

Ejemplo de respuesta de `/api/quiz/submit`:

```json
{
  "score": 8,
  "total": 10,
  "percentage": 80,
  "passed": true,
  "results": [ { "id": 1, "is_correct": true, "explanation": "..." } ]
}
```

---

## 🚀 Ejecutar Localmente

```bash
# 1. Crear y activar el entorno virtual (Windows PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar el servidor
python app.py
```

Abre tu navegador en `http://127.0.0.1:5000/`.

---

## 🌐 Despliegue en la Nube (Render)

El archivo `Procfile` indica a la plataforma cómo iniciar la app:

```text
web: gunicorn app:app
```

Pasos:

1. **Subir el proyecto a GitHub:**
   ```bash
   git init
   git add .
   git commit -m "App Flask con sección creativa y quiz de Stack y Arquitecturas"
   git branch -M main
   git remote add origin https://github.com/TU_USUARIO/TU_REPOSITORIO.git
   git push -u origin main
   ```
2. **Configurar en [Render.com](https://render.com):**
   - `+ New` → **Web Service** → conecta GitHub y selecciona el repositorio.
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Create Web Service** 🎉

Render te entrega un enlace HTTPS público para acceder a tu aplicación desde cualquier dispositivo.

---

## 📄 Licencia

MIT — ver archivo [LICENSE](LICENSE).