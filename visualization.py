
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file
df = pd.read_csv("data.csv")

# Display product sales
print(df[["Product", "Sales"]])

# Create the bar chart
plt.figure(figsize=(10, 6))

sns.barplot(data=df, x="Product", y="Sales")

# Add title and labels
plt.title("Product-wise Sales Analysis")
plt.xlabel("Product Name")
plt.ylabel("Sales Amount")

# Rotate product names
plt.xticks(rotation=45)

# Display the chart
plt.tight_layout()
plt.show()
