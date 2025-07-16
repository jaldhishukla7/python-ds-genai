# ==========================================
# Python Basics – Data Science Foundations
# Codecademy: Getting Started with Python for Data Science
# Created by: Jaldhi Shukla
# ==========================================

# 1. VARIABLES & DATA TYPES
# --------------------------
name = "Jaldhi"
age = 24
height = 5.8
is_coder = True

# Print and type checking
print("Name:", name)
print("Type of age:", type(age))

# 2. LISTS
# --------
skills = ["Python", "SQL", "Git"]
print("Skills:", skills)
skills.append("Pandas")  # Add item
print("Updated Skills:", skills)
print("First Skill:", skills[0])  # Indexing

# 3. DICTIONARIES
# ---------------
profile = {
    "name": "Jaldhi",
    "age": 24,
    "is_data_enthusiast": True
}
print("Profile Name:", profile["name"])
profile["city"] = "Ahmedabad"  # Add new key
print("Updated Profile:", profile)

# 4. CONDITIONALS
# ---------------
if age >= 18:
    print("You're an adult")
else:
    print("You're a minor")

# 5. LOOPS
# --------
# For loop
for skill in skills:
    print("Learning:", skill)

# While loop
counter = 0
while counter < 3:
    print("Counter:", counter)
    counter += 1

# 6. FUNCTIONS
# ------------
def greet(name):
    return f"Hello, {name}! Welcome to Data Science."

print(greet("Jaldhi"))

# Function with default param
def square(x=2):
    return x * x

print("Square of 5:", square(5))

# 7. IMPORTING LIBRARIES
# ----------------------
import math
import random

print("Random number:", random.randint(1, 100))
print("Square root of 25:", math.sqrt(25))

# 8. NUMPY BASICS
# ---------------
import numpy as np

array = np.array([1, 2, 3, 4])
print("NumPy Array:", array)
print("Array + 10:", array + 10)

matrix = np.array([[1, 2], [3, 4]])
print("2D Matrix:\n", matrix)

# 9. PANDAS BASICS
# ----------------
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Jaldhi"],
    "Age": [25, 30, 24],
    "Country": ["India", "USA", "India"]
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)
print("Ages:\n", df["Age"])
print("Filtered:\n", df[df["Country"] == "India"])

# 10. BASIC DATA CLEANING
# -----------------------
df.loc[1, "Age"] = np.nan  # Set missing value
print("With NaN:\n", df)
df["Age"].fillna(df["Age"].mean(), inplace=True)  # Fill NaN with mean
print("After Fill:\n", df)

# 11. BASIC DATA ANALYSIS
# -----------------------
print("Summary Stats:\n", df.describe())
print("Country Counts:\n", df["Country"].value_counts())

# 12. WORKING WITH CSV FILES
# --------------------------
# Save to CSV
df.to_csv("sample_data.csv", index=False)

# Read from CSV
df2 = pd.read_csv("sample_data.csv")
print("Loaded CSV:\n", df2)

# 13. PROJECT SNIPPET – BMI CALCULATOR
# ------------------------------------
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

weight = 68  # kg
height = 1.75  # meters
print(f"BMI is: {calculate_bmi(weight, height)}")

# ==========================================
# End of Python Basics Reference File
# ==========================================