
import pandas as pd
from pathlib import Path
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

print("Model Training Started!")

# Load Dataset
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "dataset" / "improved_house_price.csv"

df = pd.read_csv(DATA_PATH)

print("\nDataset Loaded Successfully!")

# Separate Input and Output
X = df.drop(columns=["Price", "Id"])
y = df["Price"]

# Convert Categorical Data
categorical_columns = ["Location", "Condition", "Garage"]

encoder = ColumnTransformer(
    transformers=[
        ("encoder", OneHotEncoder(handle_unknown="ignore"), categorical_columns)
    ],
    remainder="passthrough"
)

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Model
model = Pipeline([
    ("encoder", encoder),
    ("regressor", LinearRegression())
])

# Train Model
model.fit(X_train, y_train)

print("\nModel Training Completed!")

# Make Prediction
y_pred = model.predict(X_test)

# Evaluate Model
print("\nMean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# Save Model
MODEL_DIR = BASE_DIR / "models"
MODEL_DIR.mkdir(exist_ok=True)

joblib.dump(model, MODEL_DIR / "house_price_model.pkl")

print("\nModel Saved Successfully!")
print("\nProgram Completed!")
