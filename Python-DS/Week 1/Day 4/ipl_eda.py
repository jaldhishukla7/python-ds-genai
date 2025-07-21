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

# Get the top 10 run scorers
top_batsman = df.groupby('batter')['batsman_runs'].sum().sort_values(ascending=False).head(10) # type: ignore
print("Top 10 Run Scorers:\n", top_batsman)

# Get the top 10 batsman with most fours
fours = df[df['batsman_runs'] == 4].groupby('batter').size().sort_values(ascending=False).head(10) # type: ignore
print("Top 10 Players with most fours:\n", fours)

# Get the top 10 batsman with most sixes
sixes = df[df['batsman_runs'] == 6].groupby('batter').size().sort_values(ascending=False).head(10) #type: ignore
print("Top 10 Players with most sixes:\n", sixes)

# Get the top 10 bowlers with most wickets
wickets = df[df['is_wicket'] == 1].groupby('bowler').size().sort_values(ascending=False).head(10) #type: ignore
print("Top 10 Bowlers with most wickets:\n", wickets)

# Most Dismissal types
dismissals = df['dismissal_kind'].value_counts()
print("Dismissal by type:\n", dismissals)

# Total Runs by each team
team_runs = df.groupby('batting_team')['total_runs'].sum().sort_values(ascending=False) # type: ignore
print("Total Runs by each team:\n", team_runs)


# 4. Data Visualization
# -----------------------------

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
sns.barplot(x=top_batsman.values, y=top_batsman.index, palette="viridis")
plt.title("Top 10 Run Scorers in IPL")
plt.xlabel("Total Runs")
plt.ylabel("Batsman")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,6))
sns.barplot(x=wickets.values, y=wickets.index, palette="rocket")
plt.title("Top 10 Wicket Takers in IPL")
plt.xlabel("Wickets Taken")
plt.ylabel("Bowler")
plt.tight_layout()
plt.show()