import sqlite3

conn = sqlite3.connect("production.db")
cursor = conn.cursor()

cursor.execute("""
SELECT
    nimi,
    myyntihinta - valmistuskustannus AS kate
FROM tuotteet
""")

for rivi in cursor.fetchall():
    print(rivi)
conn.commit()
conn.close()