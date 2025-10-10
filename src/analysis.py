import os
import pandas as pd
import matplotlib.pyplot as plt

# مسیر فایل CSV را مشخص کن
base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, '..', 'data', 'sales_data.csv')

# 1️⃣ خواندن داده‌ها
data = pd.read_csv(csv_path)
print("✅ Data loaded successfully!")
print(data.head())

# 2️⃣ ایجاد ستون مجموع فروش
data['sales'] = data['quantity'] * data['price']

# 3️⃣ گروه‌بندی بر اساس دسته‌بندی (category)
summary = data.groupby('category')['sales'].sum().reset_index()
summary = summary.rename(columns={'sales': 'Total Sales'})

# 4️⃣ چاپ نتایج در خروجی
print("💰 Total Revenue by Category:")
print(summary)

# 5️⃣ رسم نمودار فروش بر اساس دسته‌بندی
plt.figure(figsize=(6, 4))
plt.bar(summary['category'], summary['Total Sales'], color='skyblue')
plt.title('Sales by Category')
plt.xlabel('Category')
plt.ylabel('Total Sales ($)')
plt.tight_layout()

# 6️⃣ ذخیره خروجی نمودار
output_path = os.path.join(base_dir, '..', 'output', 'sales_by_category.png')
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path)

print(f"📊 Chart saved to: {output_path}")

