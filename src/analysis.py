import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
import os
base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, '..', 'data', 'sales_data.csv')
data = pd.read_csv(csv_path)


# Initial review
print("✅ Data loaded successfully!")
print(data.head())

# Simple analysis: Total sales by category
summary = data.groupby('category')['sales'].sum().reset_index()

# Save summary to new file
summary.to_csv('sales_summary.csv', index=False)
print("📁 Saved summary to sales_summary.csv")

# Draw a chart
plt.figure(figsize=(6,4))
plt.bar(summary['category'], summary['sales'], color='skyblue')
plt.title('Total Sales by Category')
plt.xlabel('Category')
plt.ylabel('Sales')

# save chart
plt.tight_layout()
plt.savefig('sales_chart.png')
print("🖼️ Chart saved as sales_chart.png")
