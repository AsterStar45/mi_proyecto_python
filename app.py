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