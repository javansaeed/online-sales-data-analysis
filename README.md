# online-sales-data-analysis
Data analysis project using Python
#================================
# Online Sales Data Analysis

A **data analysis project** that processes and visualizes sales data using **Python (pandas, matplotlib)**.

---

## 📂 Project Overview

This project reads sales data from a CSV file, calculates total sales per category, and generates visualizations for insights.  
It demonstrates:

- Reading and processing CSV data with Python and pandas
- Summarizing and aggregating data by category
- Generating charts with matplotlib
- Saving output (tables and charts) for reporting

---

## ⚙️ Features

1. **Input Data Processing**
   - Reads sales data from `data/sales_data.csv`
   - Adds calculated fields like total sales per product

2. **Summary Data**
   - Aggregates sales by category
   - Saves summary to CSV (`output/sales_summary.csv`)

3. **Visualization**
   - Bar chart of total sales per category
   - Saved as `output/sales_by_category.png`

4. **Automated Workflow**
   - GitHub Actions workflow runs analysis automatically on data changes
   - Commits output to a separate branch and creates a Pull Request

---

## 🛠️ Tech Stack

- **Python 3.10**
- **pandas** for data manipulation
- **matplotlib** for visualization
- **GitHub Actions** for automation

---

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/javansaeed/online-sales-data-analysis.git
cd online-sales-data-analysis
