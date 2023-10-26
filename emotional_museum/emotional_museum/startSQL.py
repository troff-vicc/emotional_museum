import sqlite3
con = sqlite3.connect('emotional_museum.db')
cur = con.cursor()
cur.execute("CREATE TABLE login(id text, name text, email text, password text, clas text)")

con.commit()