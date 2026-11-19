
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

print("EDA Started!")

# Load Dataset
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "dataset" / "improved_house_price.csv"

df = pd.read_csv(DATA_PATH)

print("\nDataset Loaded Successfully!")
print("Dataset Shape:", df.shape)

# Dataset Information
print("\nDataset Information:")
df.info()

# Statistical Summary
print("\nStatistical Summary:")
print(df.describe())

# Correlation
numerical_columns = df.select_dtypes(include="number").columns

print("\nCorrelation with Price:")
print(
    df[numerical_columns]
    .corr()["Price"]
    .sort_values(ascending=False)
)

# Area vs Price Graph
plt.figure(figsize=(8, 5))

sns.scatterplot(data=df, x="Area", y="Price")

plt.title("Area vs House Price")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(10, 6))

sns.heatmap(
    df[numerical_columns].corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Feature Correlation")
plt.show()

print("\nEDA Completed!")
