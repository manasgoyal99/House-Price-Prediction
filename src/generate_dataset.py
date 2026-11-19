
import pandas as pd
import random
from pathlib import Path

print("Dataset Generation Started!")

# Project Path
BASE_DIR = Path(__file__).resolve().parent.parent

# Categories
locations = ["Downtown", "Rural", "Suburban", "Urban"]
conditions = ["Excellent", "Good", "Fair", "Poor"]
garages = ["Yes", "No"]

data = []

# Generate 2000 Houses
for i in range(2000):

    area = random.randint(500, 5000)
    bedrooms = random.randint(1, 5)
    bathrooms = random.randint(1, 4)
    floors = random.randint(1, 3)
    year_built = random.randint(1990, 2025)

    location = random.choice(locations)
    condition = random.choice(conditions)
    garage = random.choice(garages)

    # Calculate Price
    price = area * 100

    price += bedrooms * 15000
    price += bathrooms * 10000
    price += floors * 12000

    if location == "Downtown":
        price += 100000
    elif location == "Urban":
        price += 70000
    elif location == "Suburban":
        price += 40000

    if condition == "Excellent":
        price += 50000
    elif condition == "Good":
        price += 30000
    elif condition == "Poor":
        price -= 20000

    if garage == "Yes":
        price += 25000

    price += random.randint(-20000, 20000)

    data.append({
        "Id": i + 1,
        "Area": area,
        "Bedrooms": bedrooms,
        "Bathrooms": bathrooms,
        "Floors": floors,
        "YearBuilt": year_built,
        "Location": location,
        "Condition": condition,
        "Garage": garage,
        "Price": price
    })

# Create DataFrame
df = pd.DataFrame(data)

# Save Dataset
OUTPUT_PATH = BASE_DIR / "dataset" / "improved_house_price.csv"

df.to_csv(OUTPUT_PATH, index=False)

print("\nDataset Generated Successfully!")
print("Dataset Shape:", df.shape)
print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Saved:", OUTPUT_PATH)
