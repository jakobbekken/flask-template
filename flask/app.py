from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/test")
def test():
    answer = 42
    return f"This is the test answer: {answer}"
