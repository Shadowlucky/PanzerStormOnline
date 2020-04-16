from flask import Flask
from flask_ngrok import run_with_ngrok

app = Flask(name)
run_with_ngrok(app)


@app.route("/")
def index():
    return "Привет от приложения Flask"


if name == 'main':
    app.run()
