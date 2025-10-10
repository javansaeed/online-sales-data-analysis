import os
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset


# Initial review


# Simple analysis: Total sales by category
base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, '..', 'data', 'sales_data.csv')
# Save summary to new file

data['sales'] = data['quantity'] * data['price']
print("💰 Total Revenue by Category:")
print(summary)
# Draw a chart
plt.figure(figsize=(6, 4))
plt.bar(summary['category'], summary['Total Sales'], color='skyblue')
plt.title('Sales by Category')
plt.xlabel('Category')
plt.ylabel('Total Sales ($)')
plt.tight_layout()

# save chart
output_path = os.path.join(base_dir, '..', 'output', 'sales_by_category.png')
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path)
print(f"📊 Chart saved to: {output_path}")
