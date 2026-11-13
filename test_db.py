import sqlite3

conn = sqlite3.connect("production.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM tuotteet")

for rivi in cursor.fetchall():
    print(rivi)

conn.close()