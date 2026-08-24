# DWSIM Surrogate Model – Benzene–Toluene Binary Distillation

## 1. Project Overview

This project develops a machine-learning surrogate model for a binary benzene–toluene distillation column simulated in DWSIM.

The DWSIM simulations use the ****Peng–Robinson (PR)**** thermodynamic model. The surrogate model predicts four column performance variables:

* Distillate purity (xD)

* Bottoms purity (xB)

* Condenser heat duty (QC)

* Reboiler heat duty (QR)

Three machine-learning methods were implemented and compared:

1. Polynomial Regression

2. Random Forest

3. Support Vector Regression (SVR)

Based on the test-set results, 5-fold cross-validation, and physical consistency checks, ****Polynomial Regression was selected as the final surrogate model**** for the investigated operating region.

---

## 2. Folder Structure

```text
DWSIM Surrogate Model Submission/

│
├── Code/
│   ├── cross_validation.py
│   ├── generate_dataset.py
│   ├── inspect_dataset.py
│   ├── physical_validation.py
│   ├── plot_rmse_comparison.py
│   ├── surrogate_model.py
│   └── train_models.py
│
├── Dataset/
│   └── dwsim_dataset_100.csv
│
├── DWSIM/
│   ├── benzene_toluene
│   └── benzene_toluene_base
│
├── Plots/
│   ├── Polynomial_Regression_Bottoms_Purity
│   ├── Polynomial_Regression_Condenser_Heat_Duty
│   ├── Polynomial_Regression_Distillate_Purity
│   ├── Polynomial_Regression_Reboiler_Heat_Duty
│   ├── Random_Forest_Bottoms_Purity
│   ├── Random_Forest_Condenser_Heat_Duty
│   ├── Random_Forest_Distillate_Purity
│   ├── Random_Forest_Reboiler_Heat_Duty
│   ├── RMSE_Comparison
│   ├── SVR_Bottoms_Purity
│   ├── SVR_Condenser_Heat_Duty
│   ├── SVR_Distillate_Purity
│   └── SVR_Reboiler_Heat_Duty
│
├── Report/
│   └── Report.docx
│
├── Results/
│   ├── cross_validation_results.csv
│   ├── detailed_model_results.csv
│   ├── model_comparison.csv
│   └── Results_Summary.txt
│


```

---

## 3. DWSIM Model

The simulated system is a binary benzene–toluene distillation column.

****Thermodynamic model:**** Peng–Robinson (PR)

The DWSIM flowsheet is located in the `DWSIM` folder.

The basic column configuration used for the dataset consists of:

* Binary benzene–toluene feed

* 10 theoretical stages

* Feed entering at stage 5

* Condenser

* Reboiler

* Distillate product stream

* Bottoms product stream

The feed benzene mole fraction was fixed at ****0.50**** for the generated dataset.

The DWSIM simulations provide the reference values used to train and evaluate the surrogate models.

---

## 4. Dataset

The final dataset contains:

* ****100 successful DWSIM simulation cases****

* ****11 columns****

* ****7 input variables****

* ****4 output variables****

* ****0 missing values****

* ****0 duplicate rows****

**### Input Variables**

* Feed Temperature

* Feed Pressure

* Feed Benzene Mole Fraction

* Number of Stages

* Feed Stage

* Reflux Ratio

* Bottoms Withdrawal Rate

**### Output Variables**

* Distillate Purity (xD)

* Bottoms Purity (xB)

* Condenser Heat Duty (QC)

* Reboiler Heat Duty (QR)

The dataset is located at:

```text
Dataset/dwsim_dataset_100.csv
```

---

## 5. Operating Range

The dataset covers the following operating region:

| Variable                   |     Minimum |     Maximum |
| -------------------------- | ----------: | ----------: |
| Feed Temperature           |    351.15 K |    355.90 K |
| Feed Pressure              |   99,000 Pa |  102,000 Pa |
| Feed Benzene Mole Fraction |        0.50 |        0.50 |
| Number of Stages           |          10 |          10 |
| Feed Stage                 |           5 |           5 |
| Reflux Ratio               |        3.00 |        4.35 |
| Bottoms Withdrawal Rate    | 13.70 mol/s | 13.97 mol/s |

Only feed temperature, feed pressure, reflux ratio, and bottoms withdrawal rate were varied.

Feed composition, number of stages, and feed stage were kept fixed.

The surrogate model should therefore be treated as a model for this investigated operating region rather than as a universal distillation-column model.

---

## 6. Dataset Generation

The dataset was generated from DWSIM simulations.

For each case, the automation procedure:

1. Sets the feed temperature and pressure.

2. Sets the benzene feed composition.

3. Sets the column number of stages and feed stage.

4. Sets the reflux ratio.

5. Sets the bottoms withdrawal rate.

6. Solves the DWSIM column.

7. Extracts xD, xB, QC, and QR.

8. Checks that the calculated values are valid.

9. Records the successful case in the CSV dataset.

The dataset generation procedure retained ****100 successful cases****.

The generated CSV was then inspected using Python and Pandas before machine-learning training.

---

## 7. Data Preprocessing

The dataset was checked for:

* Missing values

* Duplicate rows

* Data types

* Summary statistics

* Variable ranges

The final dataset contained ****no missing values and no duplicate rows****.

The seven input variables were separated from the four target variables.

The dataset was divided into:

* ****80 training cases****

* ****20 testing cases****

The test set was kept separate from model fitting and was used to evaluate predictions on unseen data.

For Polynomial Regression, polynomial features were generated from the input variables.

Random Forest was trained using the numerical input features directly.

For SVR, feature scaling was applied because the input variables have different numerical magnitudes.

---

## 8. Machine-Learning Models

The following three models were implemented:

**### Polynomial Regression**

Polynomial Regression was used to model nonlinear relationships between the operating conditions and column outputs.

**### Random Forest**

Random Forest uses an ensemble of decision trees and can capture nonlinear relationships and interactions between the input variables.

**### Support Vector Regression**

SVR was used as a third regression approach. Input features were scaled before training.

Each model was evaluated separately for:

* xD

* xB

* QC

* QR

---

## 9. Model Evaluation

The models were evaluated using:

* ****R²****

* ****MAE****

* ****RMSE****

An ****80/20 train-test split**** was used for the primary test-set evaluation.

In addition, ****5-fold cross-validation**** was performed to check the stability of the model results across different subsets of the dataset.

---

## 10. Running the Python Code

Install Python and the required machine-learning libraries before running the scripts.

Open a terminal in the project directory and move into the Code folder:

```text
cd Code
```

**### Inspect the Dataset**

Run:

```text
python inspect\_dataset.py
```

This checks:

* Dataset dimensions

* Column names

* Missing values

* Duplicate rows

* Data types

* Summary statistics

**### Train and Compare Models**

Run:

```text
python train\_models.py
```

This trains and evaluates:

* Polynomial Regression

* Random Forest

* SVR

The model comparison results are saved as CSV files in the `Results` folder.

**### Cross-Validation**

Run:

```text
python cross\_validation.py
```

This performs 5-fold cross-validation and evaluates the three models across the four target variables.

The results are saved in:

```text
Results/cross\_validation\_results.csv
```

**### Physical Validation**

Run:

```text
python physical\_validation.py
```

This checks the surrogate predictions against basic physical validity conditions and compares the predicted ranges with the DWSIM reference ranges.

---

## 11. Results

Polynomial Regression was selected as the final surrogate model.

Its test-set performance was:

| Target |        R² |
| ------ | --------: |
| xD     |  0.999963 |
| xB     |  0.999968 |
| QC     | ≈1.000000 |
| QR     | ≈1.000000 |

The model also maintained mean R² values above ****0.9997**** for all four targets during 5-fold cross-validation.

Random Forest was the second-best overall model, while SVR produced the lowest overall performance for the present dataset.

Detailed numerical results are stored in:

```text
Results/
```

Prediction and comparison plots are stored in:

```text
Plots/
```

The complete discussion of the results is provided in:

```text
Report/Report.pdf
```

---

## 12. Physical Validation

The surrogate predictions were checked for basic physical validity.

For the final Polynomial Regression model:

* xD: ****100/100 valid predictions****

* xB: ****100/100 valid predictions****

* QC: ****100/100 valid predictions****

* QR: ****100/100 valid predictions****

The predicted ranges were also very close to the corresponding DWSIM ranges.

The model reproduced the general trend of improved separation with increasing reflux ratio within the investigated operating region.

These checks support the use of Polynomial Regression as the final surrogate model for the simulated operating space.

---

## 13. Reproducibility

To reproduce the machine-learning results:

1. Open the project folder.

2. Place the DWSIM-generated dataset in `Dataset/`.

3. Run `inspect_dataset.py`.

4. Run `train_models.py`.

5. Run `cross_validation.py`.

6. Run `physical_validation.py`.

7. Compare the newly generated results with the files in `Results/`.

8. Compare generated plots with the files in `Plots/`.

The DWSIM flowsheet is provided in the `DWSIM/` folder for inspection and reproduction of the process model.

The final dataset contains the 100 successful simulation cases used for the reported machine-learning results.

---

## 14. Important Assumptions and Limitations

The surrogate model is intended primarily for predictions within the operating domain represented by the 100 DWSIM simulation cases.

The following variables were fixed:

* Feed benzene mole fraction = ****0.50****

* Number of stages = ****10****

* Feed stage = ****5****

The main varied variables were:

* Feed temperature = ****351.15–355.90 K****

* Feed pressure = ****99,000–102,000 Pa****

* Reflux ratio = ****3.00–4.35****

* Bottoms withdrawal rate = ****13.70–13.97 mol/s****

Predictions outside these ranges involve extrapolation and should not be considered reliable without additional DWSIM simulations.

The dataset contains only 100 cases, so the reported accuracy should be interpreted within the investigated operating region.

---

## 15. Results Summary

A separate summary of the final model, performance metrics, validation results, and important observations is provided in:

```text
Results\_Summary/Results\_Summary.txt
```

The complete technical discussion is provided in:

```text
Report/Report.pdf
```

---
