import os
import pandas as pd
import matplotlib.pyplot as plt
import uuid

# ------------------------------
# مسیر فایل CSV ورودی
base_dir = os.path.dirname(os.path.abspath(__file__))  # مسیر فولدر src
data_path = os.path.join(base_dir, '..', 'data', 'sales_data.csv')

# ------------------------------
# مسیر فولدر خروجی
output_dir = os.path.join(base_dir, '..', 'output')
os.makedirs(output_dir, exist_ok=True)

# ------------------------------
# 1️⃣ خواندن داده‌ها
data = pd.read_csv(data_path)
print("✅ Data loaded successfully!")
print("📄 Input Data (first 5 rows):")
print(data.head())

# ------------------------------
# اضافه کردن UUID برای هر run تا commit واقعی داشته باشیم
data['run_id'] = str(uuid.uuid4())

# ------------------------------
# ذخیره جدول ورودی در CSV
input_csv_path = os.path.join(output_dir, 'input_data_output.csv')
data.to_csv(input_csv_path, index=False)
print(f"✅ Input data saved to: {input_csv_path}")

# ------------------------------
# 2️⃣ ایجاد ستون مجموع فروش
data['sales'] = data['quantity'] * data['price']

# ------------------------------
# 3️⃣ گروه‌بندی بر اساس دسته‌بندی (category)
summary = data.groupby('category')['sales'].sum().reset_index()
summary = summary.rename(columns={'sales': 'Total Sales'})

# اضافه کردن UUID به summary برای commit واقعی
summary['run_id'] = str(uuid.uuid4())

print("💰 Total Revenue by Category:")
print(summary)

# ------------------------------
# ذخیره جدول summary در CSV
summary_csv_path = os.path.join(output_dir, 'sales_summary.csv')
summary.to_csv(summary_csv_path, index=False)
print(f"✅ Summary data saved to: {summary_csv_path}")

# ------------------------------
# 4️⃣ رسم نمودار فروش بر اساس دسته‌بندی
plt.figure(figsize=(6, 4))
plt.bar(summary['category'], summary['Total Sales'], color='skyblue')
plt.title('Sales by Category')
plt.xlabel('Category')
plt.ylabel('Total Sales ($)')
plt.tight_layout()

# ذخیره نمودار
chart_path = os.path.join(output_dir, 'sales_by_category.png')
plt.savefig(chart_path)
plt.show()
print(f"📊 Chart saved to: {chart_path}")

# ------------------------------
# چاپ مسیرها برای بررسی در log
print("\n🔹 Paths for verification:")
print("Output folder:", output_dir)
print("Input CSV path:", input_csv_path)
print("Summary CSV path:", summary_csv_path)
print("Chart path:", chart_path)
