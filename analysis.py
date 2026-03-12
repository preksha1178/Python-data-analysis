import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("dataset.csv")

print("Dataset Preview")
print(data.head())

# Create total sales column
data["Total"] = data["Price"] * data["Quantity"]

# Total revenue
print("Total Revenue:", data["Total"].sum())

# Sales by category
category_sales = data.groupby("Category")["Total"].sum()
print(category_sales)

# Plot graph
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.show()