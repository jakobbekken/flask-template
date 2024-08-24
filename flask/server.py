from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/test")
def test():
    answer = 42
    return f"This is the test answer: {answer}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
