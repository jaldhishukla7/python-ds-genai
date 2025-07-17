import pandas as pd
import numpy as np

df = pd.read_csv("D:/Jaldhi Shukla/Python & DS/Python-DS/Week 1/Day 2/Dataset/titanic/tested.csv")
# Alternative : df = pd.read_csv(r"D:\Jaldhi Shukla\Python & DS\Python-DS\Week 1\Day 2\Dataset\titanic\tested.csv")
#The r before the string means “raw string”, so Python doesn’t treat backslashes as escape characters.

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

# Value counts for 'Survived' column
print("\n--- Survival Counts ---")
print(df['Survived'].value_counts())

# Value counts for 'Pclass' column
print("\n--- Passenger Class Counts ---")
print(df['Pclass'].value_counts())

# Value counts for 'Sex' column
print("\n--- Gender Counts ---")
print(df['Sex'].value_counts())

df['Age'].fillna(df['Age'].median(), inplace=True)

df['Embarked'].fillna(df['Embarked'].mode().iloc[0], inplace=True)

df.drop(['Cabin', 'PassengerId', 'Name', 'Ticket'], axis=1, inplace=True)

df['Survived'] = df['Survived'].astype('category')

# 3. Data Visualization
# -------------------------------
import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(data=df, x='Sex', hue='Survived')
plt.title('Survival Counts by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(8,5))
sns.histplot(data=df, x='Age', bins=20, kde=True, color='skyblue')
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Number of Passengers')
plt.show()

plt.figure(figsize=(10,6))
sns.heatmap(df.select_dtypes(include=[np.number]).corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()