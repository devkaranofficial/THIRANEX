# ==========================================
# HOUSE PRICE PREDICTION USING LINEAR REGRESSION
# ==========================================

# Import Required Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
    mean_absolute_percentage_error
)

# ==========================================
# LOAD DATASET
# ==========================================

df = pd.read_csv("train.csv")

print("=" * 50)
print("HOUSE PRICE PREDICTION PROJECT")
print("=" * 50)

# Dataset Overview

print("\nDataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# ==========================================
# FEATURE SELECTION
# ==========================================

X = df[
    [
        "GrLivArea",
        "BedroomAbvGr",
        "FullBath"
    ]
]

y = df["SalePrice"]

# ==========================================
# TRAIN TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)

# ==========================================
# MODEL TRAINING
# ==========================================

model = LinearRegression()

model.fit(X_train, y_train)

print("\nModel Training Completed Successfully!")

# ==========================================
# PREDICTIONS
# ==========================================

predictions = model.predict(X_test)

print("\nFirst 10 Predictions")

for i in range(min(10, len(y_test))):
    print(
        f"Actual: {y_test.iloc[i]:,.0f} | "
        f"Predicted: {predictions[i]:,.0f}"
    )

# ==========================================
# MODEL EVALUATION
# ==========================================

mae = mean_absolute_error(y_test, predictions)

mse = mean_squared_error(y_test, predictions)

rmse = np.sqrt(mse)

r2 = r2_score(y_test, predictions)

mape = mean_absolute_percentage_error(
    y_test,
    predictions
)

print("\n" + "=" * 50)
print("MODEL PERFORMANCE")
print("=" * 50)

print(f"MAE  : {mae:,.2f}")
print(f"MSE  : {mse:,.2f}")
print(f"RMSE : {rmse:,.2f}")
print(f"R² Score : {r2:.4f}")
print(f"MAPE : {mape:.4f}")

# ==========================================
# MODEL COEFFICIENTS
# ==========================================

print("\nFeature Importance")

for feature, coefficient in zip(
        X.columns,
        model.coef_
):
    print(f"{feature}: {coefficient:.2f}")

print(f"Intercept: {model.intercept_:.2f}")

# ==========================================
# ACTUAL VS PREDICTED TABLE
# ==========================================

results = pd.DataFrame({
    "Actual Price": y_test.values,
    "Predicted Price": predictions
})

print("\nPrediction Sample")

print(results.head(10))

# ==========================================
# VISUALIZATION 1
# ACTUAL VS PREDICTED
# ==========================================

plt.figure(figsize=(8, 6))

plt.scatter(
    y_test,
    predictions,
    alpha=0.7
)

plt.xlabel("Actual House Prices")
plt.ylabel("Predicted House Prices")
plt.title("Actual vs Predicted House Prices")

plt.tight_layout()
plt.show()

# ==========================================
# VISUALIZATION 2
# REGRESSION PERFORMANCE
# ==========================================

plt.figure(figsize=(8, 6))

plt.plot(
    y_test.values,
    label="Actual Prices"
)

plt.plot(
    predictions,
    label="Predicted Prices"
)

plt.title("Actual vs Predicted Prices")
plt.legend()

plt.tight_layout()
plt.show()

# ==========================================
# VISUALIZATION 3
# RESIDUAL PLOT
# ==========================================

residuals = y_test - predictions

plt.figure(figsize=(8, 6))

plt.scatter(
    predictions,
    residuals,
    alpha=0.7
)

plt.axhline(y=0)

plt.xlabel("Predicted Prices")
plt.ylabel("Residuals")
plt.title("Residual Plot")

plt.tight_layout()
plt.show()

# ==========================================
# FUTURE HOUSE PRICE PREDICTION
# ==========================================

print("\nFuture House Price Prediction")

new_house = pd.DataFrame({
    "GrLivArea": [2000],
    "BedroomAbvGr": [3],
    "FullBath": [2]
})

future_price = model.predict(new_house)

print(
    f"Predicted Price of House: "
    f"${future_price[0]:,.2f}"
)

# ==========================================
# END OF PROJECT
# ==========================================