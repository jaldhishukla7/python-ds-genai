# ========================================================
# Data Exploration Basics – Based on Codecademy Curriculum
# Author: Jaldhi Shukla
# Week 1 - Day 1
# ========================================================

import pandas as pd
import numpy as np

# -------------------------------
# 1. Create or Load Sample Dataset
# -------------------------------
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, np.nan, 22, 29],
    "Department": ["HR", "IT", "Finance", "HR", "IT"],
    "Salary": [50000, 60000, 65000, np.nan, 58000]
}

df = pd.DataFrame(data)
print("\n--- Initial DataFrame ---\n", df)

# -------------------------------
# 2. Exploring the Data
# -------------------------------
print("\n--- First 3 Rows ---\n", df.head(3))
print("\n--- Data Types ---\n", df.dtypes)
print("\n--- Summary Stats ---\n", df.describe())
print("\n--- Column Names ---\n", df.columns.tolist())
print("\n--- Null Values ---\n", df.isnull().sum())

# -------------------------------
# 3. Sorting and Filtering Rows
# -------------------------------
# Sort by Salary (descending)
sorted_df = df.sort_values("Salary", ascending=False)
print("\n--- Sorted by Salary ---\n", sorted_df)

# Filter: Only HR department
hr_only = df[df["Department"] == "HR"]
print("\n--- HR Department Only ---\n", hr_only)

# Filter: Age > 25 and Department is IT
filtered = df[(df["Age"] > 25) & (df["Department"] == "IT")]
print("\n--- Age > 25 and Dept = IT ---\n", filtered)

# -------------------------------
# 4. Cleaning and Transforming Columns
# -------------------------------
# Fill missing Age with mean
df["Age"].fillna(df["Age"].mean(), inplace=True)

# Fill missing Salary with median
df["Salary"].fillna(df["Salary"].median(), inplace=True)

# Create new column: Salary in Lakhs
df["Salary_Lakhs"] = df["Salary"] / 100000

# Rename a column
df.rename(columns={"Department": "Dept"}, inplace=True)

print("\n--- Cleaned and Transformed Data ---\n", df)

# -------------------------------
# 5. Exporting & Saving Cleaned Data
# -------------------------------
df.to_csv("cleaned_employee_data.csv", index=False)
print("\n✅ Cleaned data saved to 'cleaned_employee_data.csv'")

# ========================================================
# End of Codecademy-style Data Exploration Script
# ========================================================