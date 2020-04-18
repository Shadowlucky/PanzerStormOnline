from flask import Flask
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)


@app.route("/")
def index():
    return f"""<h1 align="center">Приветствуем на главной странице</h1>
               <a href="/game">Игра</a>"""


@app.route("/game")
def game():
    return f"""<h1 align="center">PanzerStorm</h1>
                <a href="/">На главную страницу</a>
                """


if __name__ == '__main__':
    app.run()
