# ------------------------------
# PROJECT 1: IPL DASHBOARD
# ------------------------------

# Import necessary Python libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


deliveries = pd.read_csv("D:/Jaldhi Shukla/Python & DS/Python-DS/Week 1/Day 5/Dataset/deliveries.csv")
matches = pd.read_csv("D:/Jaldhi Shukla/Python & DS/Python-DS/Week 1/Day 5/Dataset/matches.csv")

# Merge year into deliveries
matches['season'] = pd.to_datetime(matches['date']).dt.year
df = deliveries.merge(matches[['id', 'season']], left_on='match_id', right_on='id')

# Sidebar Filters
st.sidebar.header("Filters")
selected_season = st.sidebar.selectbox("Select Season", sorted(df['season'].dropna().unique(), reverse=True))
selected_team = st.sidebar.selectbox("Select Team", sorted(df['batting_team'].unique()))

# Filtered data
filtered_df = df[(df['season'] == selected_season) & (df['batting_team'] == selected_team)]

st.title(f"{selected_team} IPL Dashboard ({selected_season})")

# ---------- FIGURE 1: Top Run Scorers ----------
top_batsmen = filtered_df.groupby('batter')['batsman_runs'].sum().sort_values(ascending=False).head(10)
fig1, ax1 = plt.subplots()
top_batsmen.plot(kind='bar', ax=ax1, color='orange')
ax1.set_title("Top 10 Run Scorers")
ax1.set_xlabel("Batsman")
ax1.set_ylabel("Runs")

# ---------- FIGURE 2: Top Wicket Takers ----------
top_bowlers = filtered_df.groupby('bowler')['is_wicket'].sum().sort_values(ascending=False).head(10)
fig2, ax2 = plt.subplots()
top_bowlers.plot(kind='bar', ax=ax2, color='teal')
ax2.set_title("Top 10 Wicket Takers")
ax2.set_xlabel("Bowler")
ax2.set_ylabel("Wickets")

# ---------- FIGURE 3: Dismissal Types ----------
dismissals = filtered_df['dismissal_kind'].value_counts()
fig3, ax3 = plt.subplots()
dismissals.plot(kind='pie', autopct='%1.1f%%', ax=ax3, startangle=90)
ax3.set_title("Dismissal Types")
ax3.set_ylabel('')

# ---------- FIGURE 4: Total Runs per Match ----------
runs_per_match = filtered_df.groupby('match_id')['total_runs'].sum()
fig4, ax4 = plt.subplots()
runs_per_match.plot(kind='line', ax=ax4, color='purple', marker='o')
ax4.set_title("Total Runs per Match")
ax4.set_xlabel("Match ID")
ax4.set_ylabel("Total Runs")

# ---------- DISPLAY ALL FIGURES ----------
st.pyplot(fig1)
st.pyplot(fig2)
st.pyplot(fig3)
st.pyplot(fig4)