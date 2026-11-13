import sqlite3

conn = sqlite3.connect("production.db")
cursor = conn.cursor()

cursor.execute("""
INSERT INTO tuotteet
VALUES ('Tuote A', 15, 9)
""")

cursor.execute("""
INSERT INTO tuotteet
VALUES ('Tuote B', 25, 14)
""")

cursor.execute("""
INSERT INTO tuotteet
VALUES ('Tuote C', 40, 22)
""")

conn.commit()
conn.close()
