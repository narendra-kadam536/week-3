import pandas as pd

# Load dataset
csv_1 = pd.read_csv("sales_data.csv")

# Display first rows
print(csv_1.head())

# Total sales
total_sales = csv_1["Sales"].sum()
print("Total Sales:", total_sales)

# Sales by product
product_sales = csv_1.groupby("Product")["Sales"].sum()
print(product_sales)

# Best selling product
best_product = product_sales.idxmax()
print("Best Selling Product:", ibest_product)
