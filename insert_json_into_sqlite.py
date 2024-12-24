import json
import sqlite3

# Load the JSON data from file
with open('demo.json', 'r') as file:
    data = json.load(file)

# Connect to the SQLite database
connection = sqlite3.connect('demo_db.db')
cursor = connection.cursor()

# Create table for storing data in sqlite database
cursor.execute("""
CREATE TABLE IF NOT EXISTS demo_table (
    Name TEXT NOT NULL,
    Age INTEGER NOT NULL,
    Rating REAL NOT NULL
)
""")

# Insert the data into the sqlite database
for i, row in enumerate(data):
    cursor.execute('''
    INSERT INTO demo_table (
        Name, Age, Rating
    ) VALUES (?, ?, ?)
    ''', (
        row['Name'],
        row['Age'],
        row['Rating']
    ))
    print("Inserted entry :", i + 1)

# Commit the changes and close the connection
connection.commit()
connection.close()
