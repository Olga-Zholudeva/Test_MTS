from http import HTTPStatus

import requests
from flask import Flask, render_template

app = Flask(__name__)

URL = "https://jservice.io/api/random"
PARAMS = {"count": 10}


def get_data():
    """Получаем данные с внешного API."""
    response = requests.get(URL, PARAMS)
    if response.status_code == HTTPStatus.OK:
        data = response.json()
        return data
    else:
        return f"Ошибка при получении данных: {response.status_code}"


@app.route("/")
def base_view():
    """Обрабатываем данные и отдаем на рендеринг главной==единственной страницы."""
    data = get_data()
    questions = [item["question"] for item in data]
    answers = [item["answer"] for item in data]
    values = [item["value"] for item in data]
    context = {"questions": questions, "answers": answers, "values": values}
    return render_template("index.html", **context)


if __name__ == "__main__":
    app.run()
