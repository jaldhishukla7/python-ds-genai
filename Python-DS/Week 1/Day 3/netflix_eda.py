import pandas as pd
import numpy as np

df = pd.read_csv("D:/Jaldhi Shukla/Python & DS/Python-DS/Week 1/Day 3/Dataset/netflix/netflix_titles.csv")

# print first 5 rows
df.head()

# 1. Data Exploration
# -------------------------------
print("Data Shape:", df.shape)
print("Data Types:\n", df.dtypes)
print("Missing Values:\n", df.isnull().sum())

# 2. Descriptive Statistics
# -------------------------------
# Descriptive statistics for numerical columns
print("\n--- Descriptive Statistics (Numerical) ---")
print(df.describe())

# Descriptive statistics for categorical columns
print("\n--- Descriptive Statistics (Categorical) ---")
print(df.describe(include=['object']))

# 3. Value Counts
# -------------------------------
print("\n--- Value Counts for 'type' ---")
print(df['type'].value_counts())

# 4. Missing Data Handling
# --------------------------------

df[df.isnull().any(axis=1)]
print(f"\nMissing 'director': {df['director'].isnull().sum()}")

# Drop rows with any missing values
df_dropped = df.dropna()
print(f"\nShape after dropping rows with any missing values: {df_dropped.shape}")

# Drop rows with missing values only in specific columns (example: 'director')
df_director_dropped = df.dropna(subset=['director'])
print(f"\nShape after dropping rows with missing 'director': {df_director_dropped.shape}")

df_dropped = df.dropna()
print(f"\nShape after dropping rows with any missing values: {df_dropped.shape}")
df_director_dropped = df.dropna(subset=['director'])

df['rating'].value_counts()
df['country'].value_counts().head(10)


# 5. Data Visualization
# -------------------------------------------------

import seaborn as sns
import matplotlib.pyplot as plt

# Country of TV Shows vs Movies
sns.countplot(data=df, x='type')
plt.title("Content Type Distribution")

top_countries = df['country'].value_counts().head(10)
sns.barplot(x=top_countries.values, y=top_countries.index)
plt.title("Top 10 Countries with most content")
plt.show()


# 6. Correlation Heatmap
# --------------------------------

corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.show()