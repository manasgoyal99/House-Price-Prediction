
import pandas as pd 

from pathlib import Path

print("Program Started!")

# Project main folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Dataset path
DATA_PATH = BASE_DIR / "dataset" / "house_price_prediction.csv"

# Load Dataset
df = pd.read_csv(DATA_PATH)

print("\nDataset Loaded Successfully!")

# First 5 Rows
print("\nFirst 5 Rows:")
print(df.head())

# Dataset Shape
print("\nDataset Shape:")
print(df.shape)

# Column Names
print("\nDataset Columns:")
print(df.columns.tolist())

# Dataset Information
print("\nDataset Information:")
df.info()


# Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Check Duplicate Rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Statistical Summary
print("\nStatistical Summary:")
print(df.describe())

print("\nData Quality Check Completed!")


# Remove Duplicate Rows
df = df.drop_duplicates()

# Handle Missing Values

for column in df.columns:

    if df[column].dtype in ["int64", "float64"]:

        df[column] = df[column].fillna(df[column].median())

    else:

        df[column] = df[column].fillna(df[column].mode()[0])


print("\nMissing Values After Handling:")
print(df.isnull().sum())

print("\nMissing Values Handled Successfully!")
# Check Missing Values Again
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Check Dataset Shape
print("\nDataset Shape After Cleaning:")
print(df.shape)

print("\nData Cleaning Completed!")


# Save Cleaned Dataset

OUTPUT_PATH = BASE_DIR / "dataset" / "cleaned_house_price.csv"

df.to_csv(OUTPUT_PATH, index=False)

print("\nCleaned Dataset Saved Successfully!")
print("File Location:", OUTPUT_PATH)


print("\nProgram Completed!")
