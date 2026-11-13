# import_data.py

import sqlite3

conn = sqlite3.connect("production.db")
cursor = conn.cursor()

with open("data/tuotanto.csv", "r", encoding="utf-8") as f:
    next(f)

    for rivi in f:
        rivi = rivi.strip()
        tehdas, paiva, maara = rivi.split(",")

        cursor.execute("""
            INSERT INTO tuotanto
            VALUES (?, ?, ?)
        """, (tehdas, paiva, int(maara)))

conn.commit()
conn.close()

print("Data tuotu tietokantaan.")