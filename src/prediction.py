
import joblib
import pandas as pd
from pathlib import Path

print("House Price Prediction")

# Project Path
BASE_DIR = Path(__file__).resolve().parent.parent

# Load Model
MODEL_PATH = BASE_DIR / "models" / "house_price_model.pkl"

model = joblib.load(MODEL_PATH)

# Take House Details
area = float(input("Enter House Area: "))
bedrooms = int(input("Enter Bedrooms: "))
bathrooms = int(input("Enter Bathrooms: "))
floors = int(input("Enter Floors: "))
year = int(input("Enter Year Built: "))

location = input("Enter Location: ")
condition = input("Enter Condition: ")
garage = input("Enter Garage (Yes/No): ")

# Create DataFrame
new_house = pd.DataFrame([{
    "Area": area,
    "Bedrooms": bedrooms,
    "Bathrooms": bathrooms,
    "Floors": floors,
    "YearBuilt": year,
    "Location": location,
    "Condition": condition,
    "Garage": garage
}])

# Predict Price
predicted_price = model.predict(new_house)

print("\nPredicted House Price:", round(predicted_price[0], 2))
