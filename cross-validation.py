import pandas as pd
import numpy as np

from sklearn.model_selection import KFold, cross_val_score
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR

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

models = {
    "Polynomial Regression": Pipeline([
        ("scaler", StandardScaler()),
        ("poly", PolynomialFeatures(degree=2)),
        ("regressor", LinearRegression())
    ]),
    "Random Forest": RandomForestRegressor(
        n_estimators=300,
        random_state=42,
        max_depth=10,
        min_samples_leaf=2
    ),
    "SVR": Pipeline([
        ("scaler", StandardScaler()),
        ("regressor", SVR(
            kernel="rbf",
            C=100,
            epsilon=0.001
        ))
    ])
}

kf = KFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

results = []

print("")
print("========================================")
print("5-FOLD CROSS-VALIDATION")
print("========================================")

for output in output_columns:

    y = df[output]

    print("")
    print("----------------------------------------")
    print(output)
    print("----------------------------------------")

    for name, model in models.items():

        scores = cross_val_score(
            model,
            X,
            y,
            cv=kf,
            scoring="r2"
        )

        mean_score = scores.mean()
        std_score = scores.std()

        results.append([
            output,
            name,
            mean_score,
            std_score
        ])

        print("")
        print(name)
        print("Fold R2 scores:", scores)
        print("Mean R2:", mean_score)
        print("Standard deviation:", std_score)

results_df = pd.DataFrame(
    results,
    columns=[
        "Output",
        "Model",
        "Mean R2",
        "R2 Standard Deviation"
    ]
)

results_path = r"C:\Users\anany\DWSIM Surrogate Model\cross_validation_results.csv"

results_df.to_csv(
    results_path,
    index=False
)

print("")
print("========================================")
print("CROSS-VALIDATION SUMMARY")
print("========================================")

print(
    results_df.to_string(index=False)
)

print("")
print("Results saved to:")
print(results_path)

print("")
print("=== CROSS-VALIDATION COMPLETE ===")
