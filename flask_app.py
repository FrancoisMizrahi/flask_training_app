from flask import Flask
import requests

app = Flask(__name__)


@app.route("/")
def home():
    response = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
    return f"<h1>Hey Roman, just wanted to tell you...<h1>\n<h3>{response.json()['insult']}<h3>"


if __name__ == "__main__":
    app.run()
