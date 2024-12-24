import sqlite3

connection = sqlite3.connect("demo_db.db")
cursor = connection.cursor()

# Fetch and display data from the colleges table
cursor.execute("SELECT * FROM demo_table")
rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()
