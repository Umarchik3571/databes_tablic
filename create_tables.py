import sqlite3 as sql


con = sql.connect("first_my_databes.db")
cur = con.cursor()

# #TEXT,INTEGER,BIGINT,REAL,VARCHAR(100)
cur.execute("""CREATE TABLE IF NOT EXISTS students(
            name TEXT,
            age INTEGER,
            coin INTEGER
)""")

cur.execute("""CREATE TABLE IF NOT EXISTS books(
            name TEXT,
            price INTEGER,
            pages INTEGER
)""")


cur.execute("ISERT INTO students(name,age,coin) VALUES (?,?,?)",("Ozodbek",11,200))

con.close()