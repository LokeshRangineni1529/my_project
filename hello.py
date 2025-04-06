from preswald import text, plotly, connect, get_df, table, slider, query, button
import pandas as pd
import plotly.express as px
import random

# Welcome Text
text("# Welcome to Preswald!")
text("This is your first app. 🎉")

# Load the dataset
connect()  # Initialize connection
df = get_df("icc_wc_23_bat")

# Query or manipulate the data
sql = "SELECT * FROM icc_wc_23_bat WHERE runs > 50"
filtered_df = query(sql, "icc_wc_23_bat")

# Build an interactive UI
text("# 🏏 ICC World Cup 2023 - Batting Analysis App")
text("Explore players who scored more than 50 runs in the tournament.")
table(filtered_df, title="Filtered Data: Runs > 50")

# Add user controls
threshold = slider("Select Minimum Runs", min_val=0, max_val=int(df["runs"].max()), default=50)
filtered_data = df[df["runs"] > threshold]
table(filtered_data, title=f"Players with Runs > {threshold}")

# Create a Random Player Selector Widget
random_player_button = button("Get Random Player")
if random_player_button:
    random_player = filtered_data.sample(n=1)  # Randomly select 1 player from the filtered data
    random_player_info = random_player[['player', 'runs', 'balls', 'team']]  # Show only relevant stats
    text(f"🎲 **Random Player Selected** 🎲")
    table(random_player_info, title="Random Player Stats")

# Create a visualization
fig = px.scatter(
    df,
    x="balls",
    y="runs",
    color="team",
    text="player",
    title="Balls Faced vs Runs Scored",
    labels={"balls": "Balls Faced", "runs": "Runs Scored"}
)
fig.update_traces(textposition="top center", marker=dict(size=10))
fig.update_layout(template="plotly_white")
plotly(fig)
