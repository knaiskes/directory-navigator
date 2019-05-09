from flask import Flask, render_template, request, url_for, redirect
from database.database import *

app = Flask(__name__)

database_exists()

def open_file_in_path(path):
    import platform
    if(platform.system() == "Linux"):
        from subprocess import call
        call((("xdg-open", path)))
    elif(platform.system() == "Windows"):
        from os import startfile
        startfile(path)
    else:
        print("This operation is not supported in this operating system")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/directories")
def directories():
    all_directories = all_directories_db()
    return render_template("directories.html", all_directories=all_directories)

@app.route("/results")
def results():
    from os import listdir
    from os.path import join
    list_of_files = []
    all_directories = all_directories_db()

    for directory in all_directories:
        files = listdir(directory)
        for f in files:
            path = join(directory, f)
            #path = directory + f
            list_of_files.append(path)

    return render_template("results.html", list_of_files=list_of_files)

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

@app.route("/open_file", methods=["POST"])
def open_file():
    filename = request.form["filename"]
    open_file_in_path(filename)
    return redirect(url_for("results"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
