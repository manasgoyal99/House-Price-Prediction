
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# Project Path
BASE_DIR = Path(__file__).resolve().parent

# Load Model
MODEL_PATH = BASE_DIR / "models" / "house_price_model.pkl"
model = joblib.load(MODEL_PATH)

# App Title
st.title("House Price Prediction")

st.write("Enter house details to predict its price.")

# House Details
area = st.number_input("Area", min_value=500, max_value=5000, value=2000)

bedrooms = st.number_input("Bedrooms", min_value=1, max_value=5, value=3)

bathrooms = st.number_input("Bathrooms", min_value=1, max_value=4, value=2)

floors = st.number_input("Floors", min_value=1, max_value=3, value=2)

year_built = st.number_input("Year Built", min_value=1990, max_value=2025, value=2015)

location = st.selectbox(
    "Location",
    ["Downtown", "Rural", "Suburban", "Urban"]
)

condition = st.selectbox(
    "Condition",
    ["Excellent", "Good", "Fair", "Poor"]
)

garage = st.selectbox("Garage", ["Yes", "No"])

# Prediction Button
if st.button("Predict Price"):

    new_house = pd.DataFrame([{
        "Area": area,
        "Bedrooms": bedrooms,
        "Bathrooms": bathrooms,
        "Floors": floors,
        "YearBuilt": year_built,
        "Location": location,
        "Condition": condition,
        "Garage": garage
    }])

    predicted_price = model.predict(new_house)[0]

    st.success(
        f"Predicted House Price: ₹{predicted_price:,.2f}"
    )
