from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    pass

@app.route("/results")
def results():
    pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
