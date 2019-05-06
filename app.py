from flask import Flask, render_template, request, url_for, redirect
from database.database import *

app = Flask(__name__)

database_exists()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/directories")
def directories():
    return render_template("directories.html")

@app.route("/search")
def search():
    pass

@app.route("/results")
def results():
    pass

@app.route("/add_directory", methods=["POST"])
def add_directory():
    new_directory = request.form["newDirectory"]
    add_directory_db(new_directory)
    return redirect(url_for("directories"))

@app.route("/delete_directory", methods=["POST"])
def delete_directory():
    delete_dir = request.form["deleteDir"]
    delete_directory_db(delete_dir)
    return redirect(url_for("directories"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
