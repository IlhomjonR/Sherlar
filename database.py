import sqlite3 as sql


async def sql_connector():
    con = sql.connect('sher.db')
    cur = con.cursor()
    return con, cur


async def create_tables():
    con, cur = await sql_connector()

    cur.execute('''CREATE TABLE IF NOT EXISTS sherlar(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text VARCHAR(500) NOT NULL
        )''')


async def add_sher():
    con, cur = await sql_connector()
    data = cur.execute('''SELECT * FROM sherlar''').fetchall()
    return data