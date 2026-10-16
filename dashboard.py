
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data.csv")

# Calculate key business metrics
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_products = df["Product"].nunique()

# Dashboard layout
sns.set_theme(style="whitegrid")

fig, axes = plt.subplots(2, 2, figsize=(14, 9))
fig.suptitle("PRODUCT SALES AND PROFIT DASHBOARD",
             fontsize=16, fontweight="bold")

# 1. Sales chart
sns.barplot(data=df, x="Product", y="Sales", ax=axes[0, 0])
axes[0, 0].set_title("Product-wise Sales")
axes[0, 0].tick_params(axis="x", rotation=45)

# 2. Profit chart
sns.barplot(data=df, x="Product", y="Profit", ax=axes[0, 1])
axes[0, 1].set_title("Product-wise Profit")
axes[0, 1].tick_params(axis="x", rotation=45)

# 3. Sales distribution
sns.histplot(df["Sales"], kde=True, ax=axes[1, 0])
axes[1, 0].set_title("Sales Distribution")
axes[1, 0].set_xlabel("Sales Amount")

# 4. Correlation heatmap
correlation = df[["Sales", "Profit"]].corr()
sns.heatmap(correlation, annot=True, cmap="coolwarm",
            fmt=".2f", ax=axes[1, 1])
axes[1, 1].set_title("Sales-Profit Correlation")

# Add summary metrics
fig.text(0.5, 0.02,
         f"Total Sales: {total_sales:,}  |  "
         f"Total Profit: {total_profit:,}  |  "
         f"Products: {total_products}",
         ha="center", fontsize=12)

plt.tight_layout(rect=[0, 0.06, 1, 0.94])

# Save dashboard image
plt.savefig("dashboard.png", dpi=300, bbox_inches="tight")

# Display dashboard
plt.show()

print("Dashboard created successfully!")
print("Total Sales:", total_sales)
print("Total Profit:", total_profit)
print("Unique Products:", total_products)
print("Saved as dashboard.png")
