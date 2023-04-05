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


async def insert_expenses(amount, category=""):
    "Insert into sql table called expenses"
    query = "INSERT INTO expenses VALUES(?, ?, datetime(), strftime('%m', 'now', '+3 hours'))"
    cursor.execute(query, (amount, category))
    conn.commit()


async def insert_monthly_limit(amount):
    "Insert into sql table limits"
    query = "INSERT INTO limits VALUES(strftime('%m', 'now', '+3 hours'), ?)"
    cursor.execute(query, (amount,))
    conn.commit()


async def update_monthly_limit(amount):
    "Update sql table limits"
    query = "UPDATE limits SET monthly_limit=? WHERE month=strftime('%m', 'now', '+3 hours')"
    cursor.execute(query, (amount,))
    conn.commit()


async def get_monthly_limit() -> str:
    "Returns string with current monthly limit from sql table"
    query = "SELECT monthly_limit FROM limits WHERE month=strftime('%m', 'now', '+3 hours')"
    try:
        res = cursor.execute(query)
        return str(res.fetchone()[0])
    except TypeError:
        return "0"


async def get_todays_expenses() -> str:
    "Returns how much money was spent today"
    query = """SELECT SUM(amount) FROM expenses 
                WHERE strftime('%m-%d', time, '+3 hours') AND category!='0' 
                AND category!=0"""
    try:
        res = cursor.execute(query)
        return str(res.fetchone()[0])
    except TypeError:
        return "0"


async def get_this_month_expenses() -> str:
    "Returns how much money was spent today"
    query = """SELECT SUM(amount) FROM expenses 
                WHERE limit_id=strftime('%m', 'now', '+3 hours') AND category!='0' 
                AND category!=0"""
    try:
        res = cursor.execute(query)
        return str(res.fetchone()[0])
    except TypeError:
        return "0"

# insert_expenses(2000, "haircut")
# insert_expenses(111, 0)
# try:
    # insert_monthly_limit(60000)
# except sqlite3.IntegrityError:
    # update_monthly_limit(7777)
# print(get_monthly_limit())
# print(get_todays_expenses())
