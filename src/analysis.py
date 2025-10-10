import pandas as pd
import matplotlib.pyplot as plt

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

# Plot sales by product
top_products.plot(kind='bar', color='skyblue')
plt.title("💵 Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Revenue ($)")
plt.tight_layout()
plt.show()
