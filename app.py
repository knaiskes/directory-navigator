from flask import Flask, render_template, request
from os import listdir

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>It works</h1>"



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
