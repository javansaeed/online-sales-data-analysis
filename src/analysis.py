import pandas as pd

# Read sales data
df = pd.read_csv("data/sales_data.csv")

# Calculate total revenue
df["total"] = df["quantity"] * df["price"]

# Total revenue
print("💰 Total Revenue:", df["total"].sum())

# Sales by product
top_products = df.groupby("product")["total"].sum().sort_values(ascending=False)
print("\n🏆 Sales by Product:")
print(top_products)
