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
def directories():
    all_directories = all_directories_db()
    return render_template("directories.html", all_directories=all_directories)

@app.route("/files")
def files():
    from os import listdir
    from os.path import join
    list_of_files = []
    all_directories = all_directories_db()

    for directory in all_directories:
        try:
            files = listdir(directory)
        except OSError:
            print("Could not open directory!", directory)
    try:
        for f in files:
            path = join(directory, f)
            #path = directory + f
            list_of_files.append(path)
    except OSError:
        print("Could not open directory!")

    return render_template("files.html", list_of_files=list_of_files,
            file_is_in_favorites=file_is_in_favorites)

@app.route("/add_directory", methods=["POST"])
def add_directory():
    from os.path import isdir
    new_directory = request.form["newDirectory"]
    if(isdir(new_directory) == True):
        add_directory_db(new_directory)
    return redirect(url_for("directories"))

@app.route("/delete_directory", methods=["POST"])
def delete_directory():
    delete_dir = request.form["deleteDir"]
    delete_directory_db(delete_dir)
    return redirect(url_for("directories"))

@app.route("/favorites")
def favorites():
    favorite_files_list = all_favorites_db()
    return render_template("favorites.html", favorite_files_list=favorite_files_list)

@app.route("/add_favorite", methods=["POST"])
def add_favorite():
    new_filename = request.form["newFavoriteFile"]
    if(file_is_in_favorites(new_filename) == False):
        add_favorite_db(new_filename)
    # else print msg
    return redirect(request.referrer)

@app.route("/delete_favorite", methods=["POST"])
def delete_favorite():
    delete_favorite = request.form["delFavorite"]
    delete_filename_db(delete_favorite)
    return redirect(url_for("favorites"))

@app.route("/open_file", methods=["POST"])
def open_file():
    filename = request.form["filename"]
    try:
        open_file_in_path(filename)
    except OSError:
        print("Could not open file!")
    return redirect(request.referrer)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
