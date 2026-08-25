
import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression

dataset_path = r"C:\Users\anany\DWSIM Surrogate Model\dwsim_dataset_100.csv"

df = pd.read_csv(dataset_path)

input_columns = [
    "Feed Temperature",
    "Feed Pressure",
    "Feed Benzene Mole Fraction",
    "Number of Stages",
    "Feed Stage",
    "Reflux Ratio",
    "Bottoms Withdrawal Rate"
]

output_columns = [
    "Distillate Purity",
    "Bottoms Purity",
    "Condenser Heat Duty",
    "Reboiler Heat Duty"
]

X = df[input_columns]
y = df[output_columns]

model = Pipeline([
    ("scaler", StandardScaler()),
    ("poly", PolynomialFeatures(degree=2)),
    ("regressor", LinearRegression())
])

model.fit(X, y)

predictions = model.predict(X)

predicted_df = pd.DataFrame(
    predictions,
    columns=output_columns
)

print("")
print("========================================")
print("PHYSICAL CONSISTENCY VALIDATION")
print("========================================")

print("")
print("PURPOSE")
print("Checking whether surrogate predictions remain")
print("physically meaningful.")

print("")
print("----------------------------------------")
print("PURITY CHECKS")
print("----------------------------------------")

xd_valid = (
    (predicted_df["Distillate Purity"] >= 0) &
    (predicted_df["Distillate Purity"] <= 1)
)

xb_valid = (
    (predicted_df["Bottoms Purity"] >= 0) &
    (predicted_df["Bottoms Purity"] <= 1)
)

print(
    "Valid xD predictions:",
    xd_valid.sum(),
    "/",
    len(df)
)

print(
    "Valid xB predictions:",
    xb_valid.sum(),
    "/",
    len(df)
)

print("")
print("----------------------------------------")
print("HEAT DUTY CHECKS")
print("----------------------------------------")

qc_valid = (
    predicted_df["Condenser Heat Duty"] > 0
)

qr_valid = (
    predicted_df["Reboiler Heat Duty"] > 0
)

print(
    "Valid QC predictions:",
    qc_valid.sum(),
    "/",
    len(df)
)

print(
    "Valid QR predictions:",
    qr_valid.sum(),
    "/",
    len(df)
)

print("")
print("----------------------------------------")
print("PREDICTION RANGES")
print("----------------------------------------")

for column in output_columns:

    actual_min = y[column].min()
    actual_max = y[column].max()

    predicted_min = predicted_df[column].min()
    predicted_max = predicted_df[column].max()

    print("")
    print(column)
    print("DWSIM minimum:", actual_min)
    print("DWSIM maximum:", actual_max)
    print("Predicted minimum:", predicted_min)
    print("Predicted maximum:", predicted_max)

print("")
print("----------------------------------------")
print("REFLUX BEHAVIOR CHECK")
print("----------------------------------------")

reflux_values = sorted(
    df["Reflux Ratio"].unique()
)

for reflux in reflux_values:

    subset = df[
        df["Reflux Ratio"] == reflux
    ]

    X_subset = subset[input_columns]

    predictions_subset = model.predict(
        X_subset
    )

    average_xd = np.mean(
        predictions_subset[:, 0]
    )

    average_xb = np.mean(
        predictions_subset[:, 1]
    )

    print("")
    print("Reflux ratio:", reflux)
    print("Average predicted xD:", average_xd)
    print("Average predicted xB:", average_xb)

print("")
print("========================================")
print("PHYSICAL VALIDATION COMPLETE")
print("========================================")
