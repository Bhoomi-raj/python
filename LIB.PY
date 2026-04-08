import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


data = {
    "Team": ["CSK", "MI", "RCB", "KKR", "DC"],
    "Matches": [10, 10, 10, 10, 10],
    "Wins": [7, 6, 5, 4, 3]
}

df = pd.DataFrame(data)

print("Cricket Tournament Data:\n")
print(df)

wins_array = np.array(df["Wins"])
avg_wins = np.mean(wins_array)

print("\nAverage Wins:", avg_wins)

max_win = np.max(wins_array)
min_win = np.min(wins_array)
mode_win = stats.mode(wins_array)

print("Maximum Wins:", max_win)
print("Minimum Wins:", min_win)
print("Most Common Wins (Mode):", mode_win.mode)


plt.bar(df["Team"], df["Wins"])
plt.xlabel("Teams")
plt.ylabel("Wins")
plt.title("Cricket Tournament Wins")
plt.show()