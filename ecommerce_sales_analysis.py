# Step 1: load data

import pandas as pd

df = pd.read_csv("ecommerce_sales_data.csv")
df.head()

# Step 2: Clean data

# Convert 'Order Date' to datetime format
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Check for missing values
print(df.isnull().sum())

# Check data types and structure
print(df.dtypes)

# Optional: round Sales and Profit
df["Sales"] = df["Sales"].round(2)
df["Profit"] = df["Profit"].round(2)

# Step 3: Explore Key insights \u20B9 is the Unicode code point for ₹.

#1. Total sales and profit
print("Total Sales: ₹", df["Sales"].sum())
print("Total Profit: ₹", df["Profit"].sum())

#2. Top product categories
df.groupby("Product Category")["Sales"].sum().sort_values(ascending=False)

#3. Top performing states by sales
df.groupby("State")["Sales"].sum().sort_values(ascending=False).head(10)

#4. Most profitable products
df.groupby("Product Name")["Profit"].sum().sort_values(ascending=False).head(10)

#5. Monthly sales trend
df["Month"] = df["Order Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Sales"].sum()
monthly_sales.plot(kind="bar", title="Monthly Sales")

#6. Sales by segment
segment_sales = df.groupby("Segment")["Sales"].sum().sort_values(ascending=False)
print(segment_sales)

#7. Average order value
aov = df.groupby("Order ID")["Sales"].sum().mean()
print("Average Order Value: ₹", round(aov, 2))

#8. Loss making products
loss_products = df.groupby("Product Name")["Profit"].sum()
loss_products = loss_products[loss_products < 0].sort_values()
print(loss_products.head(10))  # Worst 10

#9. Sales by month-year
df["Month"] = df["Order Date"].dt.to_period("M")
monthly_profit = df.groupby("Month")[["Sales", "Profit"]].sum()
print(monthly_profit.tail(6))  # Last 6 months