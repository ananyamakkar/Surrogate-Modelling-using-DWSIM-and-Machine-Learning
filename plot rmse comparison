import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

data = {
    "Output": [
        "Distillate Purity",
        "Bottoms Purity",
        "Condenser Duty",
        "Reboiler Duty"
    ],
    "Polynomial Regression": [
        0.000040,
        0.000033,
        0.003770,
        0.003669
    ],
    "Random Forest": [
        0.001207,
        0.000236,
        6.642152,
        8.983348
    ],
    "SVR": [
        0.002248,
        0.001050,
        59.515579,
        60.686081
    ]
}

df = pd.DataFrame(data)

ax = df.set_index("Output").plot(
    kind="bar",
    figsize=(10, 6)
)

ax.set_yscale("log")
ax.set_xlabel("Output Variable")
ax.set_ylabel("RMSE (log scale)")
ax.set_title("RMSE Comparison of Machine Learning Models")

plt.xticks(rotation=0)
plt.tight_layout()

project_folder = Path(__file__).resolve().parent.parent
plots_folder = project_folder / "Plots"

plots_folder.mkdir(exist_ok=True)

output_file = plots_folder / "RMSE_Comparison.png"

plt.savefig(output_file, dpi=300, bbox_inches="tight")
plt.show()

print(f"Plot saved to: {output_file}")
