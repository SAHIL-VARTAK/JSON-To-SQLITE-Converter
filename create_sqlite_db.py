import sqlite3

# Give your own name for database
connection = sqlite3.connect("demo_db.db")

connection.close()

print("Database created successfully!")