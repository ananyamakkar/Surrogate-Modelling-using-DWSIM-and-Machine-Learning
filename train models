
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

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

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

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

all_results = []

for output in output_columns:

    print("")
    print("========================================")
    print(output)
    print("========================================")

    y_train_single = y_train[output]
    y_test_single = y_test[output]

    for name, model in models.items():

        model.fit(X_train, y_train_single)

        prediction = model.predict(X_test)

        r2 = r2_score(
            y_test_single,
            prediction
        )

        mae = mean_absolute_error(
            y_test_single,
            prediction
        )

        rmse = np.sqrt(
            mean_squared_error(
                y_test_single,
                prediction
            )
        )

        all_results.append([
            output,
            name,
            r2,
            mae,
            rmse
        ])

        print("")
        print(name)
        print("R2 =", r2)
        print("MAE =", mae)
        print("RMSE =", rmse)

        plt.figure()

        plt.scatter(
            y_test_single,
            prediction
        )

        minimum = min(
            y_test_single.min(),
            prediction.min()
        )

        maximum = max(
            y_test_single.max(),
            prediction.max()
        )

        plt.plot(
            [minimum, maximum],
            [minimum, maximum]
        )

        plt.xlabel("DWSIM Actual")
        plt.ylabel("Surrogate Predicted")
        plt.title(name + " - " + output)

        plt.tight_layout()

        filename = (
            name.replace(" ", "_")
            + "_"
            + output.replace(" ", "_")
            + ".png"
        )

        plt.savefig(filename, dpi=300)
        plt.close()

results_df = pd.DataFrame(
    all_results,
    columns=[
        "Output",
        "Model",
        "R2",
        "MAE",
        "RMSE"
    ]
)

results_path = r"C:\Users\anany\DWSIM Surrogate Model\detailed_model_results.csv"

results_df.to_csv(
    results_path,
    index=False
)

print("")
print("========================================")
print("FINAL MODEL COMPARISON")
print("========================================")

print(
    results_df.to_string(index=False)
)

print("")
print("Results saved to:")
print(results_path)

print("")
print("Plots saved in:")
print(r"C:\Users\anany\DWSIM Surrogate Model")

print("")
print("=== EVALUATION COMPLETE ===")
