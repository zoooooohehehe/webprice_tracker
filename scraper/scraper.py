import requests
import pandas as pd
import sqlite3

connection = sqlite3.connect("data/price_tracker.db")
cursor = connection.cursor()

urls = [
    "https://dummyjson.com/products/1",
    "https://dummyjson.com/products/2"
]
products = []

for url in urls:
    response = requests.get(url)

    print(response.status_code)

    data = response.json()

    product = {
        "Product": data["title"],
        "Price": data["price"],
        "Description": data["description"],
        "Category": data["category"],
        "Discount Percentage": data["discountPercentage"],
        "Rating": data["rating"],
        "Available Stock": data["stock"],
        "URL": url
    }

    products.append(product)
    cursor.execute("""
    INSERT OR IGNORE INTO products
    (name, description, category, price, discount, rating, stock, url)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        product["Product"],
        product["Description"],
        product["Category"],
        product["Price"],
        product["Discount Percentage"],
        product["Rating"],
        product["Available Stock"],
        product["URL"]
        ))
    
df = pd.DataFrame(products)
pd.set_option("display.max_columns", None)
print(df.to_string())

connection.commit()
connection.close()
print("Products saved to database!")

df.to_csv("products.csv", index=False)