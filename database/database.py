import sqlite3

connection = sqlite3.connect("data/price_tracker.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    description TEXT,
    category TEXT,
    price REAL,
    discount REAL,
    rating REAL,
    stock INTEGER,
    url TEXT
)
""")

connection.commit()

print("Products table created successfully!")

connection.close()