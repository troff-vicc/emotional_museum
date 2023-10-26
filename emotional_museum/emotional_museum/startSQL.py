import sqlite3
import sqlite3
name = input()
password = input()
conn = sqlite3.connect('emotional_museum.db')
cur = conn.cursor()
cur.execute(f'''SELECT password from login WHERE name = "{name}" ''')
passwordTrue = cur.fetchall()
if passwordTrue[0][0] == password:
    print(00000)
print(passwordTrue)

#cur.execute("""CREATE TABLE IF NOT EXISTS exhibits(
        
#    )""")
#cur.execute("""CREATE TABLE IF NOT EXISTS login(
#            id text,
#            name text,
#            password text,
#            email text,
#            clas text);
#            """)

conn.commit()