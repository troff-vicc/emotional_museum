import sqlite3

conn = sqlite3.connect('emotional_museum.db')
cur = conn.cursor()

cur.execute("DELETE FROM exhibits")
#cur.execute("""CREATE TABLE IF NOT EXISTS exhibits(
#            id text,
#            name text,
#            date text,
#            description text
#            )""")
#cur.execute("""CREATE TABLE IF NOT EXISTS login(
#            id text,
#            name text,
#            password text,
#            email text,
#            clas text);
#            """)

conn.commit()