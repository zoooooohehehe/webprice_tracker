import requests
import pandas as pd

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
df = pd.DataFrame(products)
pd.set_option("display.max_columns", None)
print(df.to_string())

df.to_csv("products.csv", index=False)