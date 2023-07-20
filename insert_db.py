import sqlite3 as sql


con = sql.connect("first_my_databes.db")
cur = con.cursor()

# cur.execute("INSERT INTO students(name,age,coin) VALUES (?,?,?)",("Ozodbek",9,200))
# cur.execute("INSERT INTO students(name,age,coin) VALUES (?,?,?)",("Abduloh",11,300))
# cur.execute("INSERT INTO students(name,age,coin) VALUES (?,?,?)",("Umarhoja",13,400))
# cur.execute("INSERT INTO students(name,age,coin) VALUES (?,?,?)",("Asadbeyaka",14,500))
# cur.execute("INSERT INTO students(name,age,coin) VALUES (?,?,?)",("Saidkarim bot",11,1))
# cur.execute("INSERT INTO students(name,age,coin) VALUES (?,?,?)",("SHahzod tvar",9,1))
# cur.execute("INSERT INTO students(name,age,coin) VALUES (?,?,?)",("Ustoz",24,"VIP"))

while True:
    name=input("Ism:")
    if name == 'stop':
        break

    age=input("Yosh:")
    if name == 'stop':
        break

    coin=input("Coin:")
    if name == 'stop':
        break
    cur.execute("INSERT INTO students(name,age,coin) VALUES (?,?,?)",("name",age,"coin"))
    con.commit()
con.close()