import pandas as pd
import numpy as np

df = pd.read_csv("D:/Jaldhi Shukla/Python & DS/Python-DS/Week 1/Day 4/Dataset/ipl/deliveries.csv")
matches = pd.read_csv("D:/Jaldhi Shukla/Python & DS/Python-DS/Week 1/Day 4/Dataset/ipl/matches.csv")
# print first 5 rows
df.head()

# 1. Data Exploration
# ---------------------------

print("Data Shape:", df.shape)
print("Data Types:\n", df.dtypes)
print("Columns:\n", df.columns.tolist())
print("Missing Values:\n", df.isnull().sum())

# 2. Descriptive Statistics
# -------------------------------

print(df.describe())

# 3. Basic Insights
# ------------------------------

# top_batsman = df.groupby('batter')['batsman_runs'].sum().sort_values(ascending=False).head()
# print("Top 10 Run Scorers:\n", top_batsman)