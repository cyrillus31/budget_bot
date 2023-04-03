"This module deals with SQLite database"

import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()


def create_database():
    "Creates tables within the 'data.db' database"

    with open("create_database.sql", "r", encoding="UTF-8") as file:
        init_db = file.read()
    conn.executescript(init_db)


create_database()
