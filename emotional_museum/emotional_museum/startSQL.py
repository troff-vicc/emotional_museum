import sqlite3
conn = sqlite3.connect('emotional_museum.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS login(
            id text,
            name text,
            email text,
            password text,
            clas text);
            """)

conn.commit()