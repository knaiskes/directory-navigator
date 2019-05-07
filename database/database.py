import sqlite3
import os.path

DATABASE = "database/directories.db"

def create_database():
    conn = sqlite3.connect(DATABASE)
    db = conn.cursor()

    db.execute("""CREATE TABLE IF NOT EXISTS directories
    (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    directory TEXT NOT NULL)""")
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

def database_exists():
    if(os.path.exists(DATABASE) == False):
        create_database()
