import sqlite3
import os.path
import platform

if(platform.system() == "Linux"):
    DATABASE = "database/directories.db"
elif(platform.system() == "Windows"):
    DATABASE = r"C:\\database\\directories.db"

def create_database():
    conn = sqlite3.connect(DATABASE)
    db = conn.cursor()

    db.execute("""CREATE TABLE IF NOT EXISTS directories
    (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    directory TEXT NOT NULL)""")
    conn.commit()

    db.execute("""CREATE TABLE IF NOT EXISTS favorites
    (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    filename TEXT NOT NULL)""")
    conn.commit()

def directory_already_exists(directory):
    conn = sqlite3.connect(DATABASE)
    db = conn.cursor()

    db.execute("SELECT directory FROM directories WHERE directory = ?",
            (directory,))
    exists = db.fetchone()

    if(exists is not None):
        return True
    else:
        return False

def add_directory_db(directory):
    conn = sqlite3.connect(DATABASE)
    db = conn.cursor()

    if(directory_already_exists(directory) == True):
        return "Directory already exists in the database"
    else:
        db.execute("INSERT INTO directories VALUES(?,?)",(None, directory))
        conn.commit()
        return "Directory has successfully added in the database"

def delete_directory_db(directory):
    conn = sqlite3.connect(DATABASE)
    db = conn.cursor()

    db.execute("DELETE FROM directories WHERE directory = ?", (directory,))
    conn.commit()

def all_directories_db():
    conn = sqlite3.connect(DATABASE)
    db = conn.cursor()

    db.execute("SELECT directory FROM directories")
    rows = [item[0] for item in db.fetchall()]
    return rows

def favorite_already_exists(filename):
    conn = sqlite3.connect(DATABASE)
    db = conn.cursor()

    db.execute("SELECT filename FROM favorites WHERE filename = ?",(filename,))
    exists = db.fetchone()

    if(exists is not None):
        return True
    else:
        return False

def add_favorite_db(filename):
    conn = sqlite3.connect(DATABASE)
    db = conn.cursor()

    if(favorite_already_exists(filename) == True):
        return "Favorite is already in your list"
    else:
        db.execute("INSERT INTO favorites VALUES(?,?)",(None, filename))
        conn.commit()
        return "Filename has successfully add in your favorites"

def delete_filename_db(filename):
    conn = sqlite3.connect(DATABASE)
    db = conn.cursor()

    db.execute("DELETE FROM favorites WHERE filename = ?", (filename,))
    conn.commit()

def all_favorites_db():
    conn = sqlite3.connect(DATABASE)
    db = conn.cursor()

    db.execute("SELECT filename FROM favorites")
    rows = [item[0] for item in db.fetchall()]
    return rows

def database_exists():
    if(os.path.exists(DATABASE) == False):
        create_database()
