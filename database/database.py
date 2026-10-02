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
    url TEXT UNIQUE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS price_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_url TEXT,
    price REAL,
    checked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

connection.commit()

print("Products table created successfully!")

connection.close()
