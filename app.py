from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

QUIZ_QUESTIONS = [
    {
        "id": 1,
        "question": "¿Qué es un \"stack\" tecnológico o stack de software?",
        "options": [
            "El conjunto de tecnologías que trabajan en conjunto para construir y ejecutar una aplicación (frontend, backend, base de datos, servidores).",
            "Un marco de trabajo exclusivamente para diseñar interfaces de usuario.",
            "Un servidor web que se utiliza únicamente en producción.",
            "La documentación técnica de un proyecto.",
        ],
        "correct": 0,
        "explanation": "Un stack es el ecosistema tecnológico completo de una aplicación; elegirlo bien define rendimiento, escalabilidad y productividad del equipo.",
    },
    {
        "id": 2,
        "question": "¿Qué estilo arquitectónico organiza la aplicación en capas como presentación, negocio (lógica) y datos?",
        "options": [
            "Arquitectura en capas (multicapa).",
            "Arquitectura de microservicios.",
            "Arquitectura de evento único.",
            "Arquitectura peer-to-peer.",
        ],
        "correct": 0,
        "explanation": "La arquitectura en capas separa responsabilidades en niveles, facilitando el mantenimiento y la evolución del software.",
    },
    {
        "id": 3,
        "question": "¿Cuál es la principal característica de la arquitectura cliente-servidor?",
        "options": [
            "Un cliente solicita servicios y el servidor responde, centralizando los recursos.",
            "Todos los nodos comparten la misma jerarquía.",
            "Las aplicaciones no necesitan red para comunicarse.",
            "El cliente almacena toda la base de datos localmente.",
        ],
        "correct": 0,
        "explanation": "En el modelo cliente-servidor, el servidor concentra datos y lógica, y los clientes consumen sus servicios a través de la red.",
    },
    {
        "id": 4,
        "question": "En la arquitectura de microservicios, ¿cómo se organiza la aplicación?",
        "options": [
            "Servicios pequeños, independientes y desplegables de forma autónoma.",
            "Un único bloque de código que se despliega completo.",
            "Una única base de datos monolítica para todo el sistema.",
            "Una sola clase que controla todas las funcionalidades.",
        ],
        "correct": 0,
        "explanation": "Cada microservicio es autónomo: tiene su propio ciclo de vida y se comunica con los demás mediante APIs.",
    },
    {
        "id": 5,
        "question": "¿Qué es una API REST?",
        "options": [
            "Un estilo arquitectónico que expone recursos mediante HTTP con verbos como GET, POST, PUT y DELETE.",
            "Un protocolo de base de datos relacional.",
            "Un lenguaje de programación para frontend.",
            "Un framework de Python para pruebas.",
        ],
        "correct": 0,
        "explanation": "REST usa HTTP puro, recursos direccionables por URL y operaciones estándar, lo que facilita la integración entre sistemas.",
    },
    {
        "id": 6,
        "question": "¿Cuál de las siguientes opciones NO es una capa típica de un stack web full-stack?",
        "options": [
            "Frontend (HTML, CSS, JavaScript).",
            "Backend (Python, Node.js, Java).",
            "Base de datos (PostgreSQL, MySQL).",
            "Tarjeta gráfica (GPU).",
        ],
        "correct": 3,
        "explanation": "Un stack full-stack abarca frontend, backend, base de datos y servidor; la GPU es hardware, no parte del stack de software.",
    },
    {
        "id": 7,
        "question": "¿En qué capa debe vivir la lógica de negocio (las reglas del dominio)?",
        "options": [
            "Capa de presentación.",
            "Capa de aplicación / dominio (negocio).",
            "Capa de datos / persistencia.",
            "Capa de red.",
        ],
        "correct": 1,
        "explanation": "La lógica de negocio se aísla en su propia capa para no depender ni de la interfaz ni de la base de datos.",
    },
    {
        "id": 8,
        "question": "En este stack, ¿para qué sirve Gunicorn?",
        "options": [
            "Es un servidor WSGI de producción que ejecuta la aplicación Flask.",
            "Es una base de datos en memoria.",
            "Es un framework de estilos CSS.",
            "Es el motor de plantillas de Flask.",
        ],
        "correct": 0,
        "explanation": "Gunicorn actúa como servidor WSGI estable y eficiente para servir la app en producción, a diferencia del servidor de desarrollo de Flask.",
    },
    {
        "id": 9,
        "question": "¿Qué herramienta permite versionar el código y colaborar en equipo mostrando el historial de cambios?",
        "options": [
            "Git / GitHub.",
            "PostgreSQL.",
            "Gunicorn.",
            "Bootstrap.",
        ],
        "correct": 0,
        "explanation": "Git lleva el control de versiones y GitHub permite alojar repositorios, colaborar y conectar despliegues en la nube.",
    },
    {
        "id": 10,
        "question": "¿Qué estilo arquitectónico describe una aplicación dividida en servicios que intercambian mensajes a través de la organización?",
        "options": [
            "Arquitectura monolítica.",
            "Arquitectura orientada a servicios (SOA).",
            "Arquitectura de capas únicamente.",
            "Arquitectura de una sola página.",
        ],
        "correct": 1,
        "explanation": "SOA organiza el software como servicios reutilizables que se comunican mediante mensajes, favoreciendo la interoperabilidad.",
    },
]


def public_question(q):
    return {"id": q["id"], "question": q["question"], "options": q["options"]}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/quiz")
def api_quiz():
    return jsonify([public_question(q) for q in QUIZ_QUESTIONS])


@app.route("/api/quiz/submit", methods=["POST"])
def api_quiz_submit():
    payload = request.get_json(silent=True) or {}
    answers = payload.get("answers", {})
    results = []
    correct_count = 0

    for q in QUIZ_QUESTIONS:
        try:
            raw = answers.get(str(q["id"]))
            user_answer = int(raw) if raw is not None else None
        except (TypeError, ValueError):
            user_answer = None

        is_correct = user_answer is not None and user_answer == q["correct"]
        if is_correct:
            correct_count += 1

        results.append(
            {
                "id": q["id"],
                "question": q["question"],
                "user_answer": user_answer,
                "correct_answer": q["correct"],
                "is_correct": is_correct,
                "explanation": q["explanation"],
            }
        )

    total = len(QUIZ_QUESTIONS)
    percentage = round((correct_count / total) * 100) if total else 0

    return jsonify(
        {
            "score": correct_count,
            "total": total,
            "percentage": percentage,
            "passed": percentage >= 60,
            "results": results,
        }
    )


if __name__ == "__main__":
    app.run(debug=True)