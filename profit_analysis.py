
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("data.csv")

# Profit Analysis Chart
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x="Product", y="Profit")

plt.title("Product-wise Profit Analysis")
plt.xlabel("Product Name")
plt.ylabel("Profit Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Correlation Heatmap
plt.figure(figsize=(6, 4))

correlation = df[["Sales", "Profit"]].corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Sales and Profit Correlation")
plt.tight_layout()
plt.show()

print("Profit analysis completed successfully!")
