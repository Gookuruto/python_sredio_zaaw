import json
import sqlite3

# Read JSON file
with open('data.json', 'r') as file:
    json_data = json.load(file)

# Create a connection to the database
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS people (
                    name TEXT,
                    age INTEGER,
                    city TEXT,
                    email TEXT
                )''')

# Insert data into the table
for entry in json_data:
    cursor.execute("INSERT INTO people VALUES (?, ?, ?, ?)",
                   (entry['name'], entry['age'], entry['city'], entry['email']))

# Commit changes and close connection
conn.commit()
conn.close()