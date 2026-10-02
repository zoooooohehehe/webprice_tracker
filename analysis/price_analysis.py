import sqlite3

connection = sqlite3.connect("data/price_tracker.db")
cursor = connection.cursor()

print("Connected to price database!")

cursor.execute("""
SELECT product_url, price, checked_at
FROM price_history
ORDER BY checked_at
""")

rows = cursor.fetchall()

for row in rows:
    print(row)