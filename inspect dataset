import pandas as pd

file_path = r"C:\Users\anany\DWSIM Surrogate Model\dwsim_dataset_100.csv"

df = pd.read_csv(file_path)

print("=== DATASET SHAPE ===")
print(df.shape)

print("\n=== COLUMN NAMES ===")
print(df.columns.tolist())

print("\n=== FIRST 5 ROWS ===")
print(df.head())

print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

print("\n=== DUPLICATE ROWS ===")
print(df.duplicated().sum())

print("\n=== DATA TYPES ===")
print(df.dtypes)

print("\n=== SUMMARY STATISTICS ===")
print(df.describe())
