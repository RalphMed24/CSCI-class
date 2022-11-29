import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("game-ratings-by-top-10-genres.csv")

# Group by metrics.
df_follow = df.groupby(["genre_name"])["follow_count"].sum().reset_index()

df_follow = df_follow.rename(columns = {"follow_count": "total_follows"})

df_hype = df.groupby(["genre_name"])["hype_count"].sum().reset_index()

df_hype = df_hype.rename(columns = {"hype_count": "total_hypes"})

# analyze data through visualizations.
BAR_WIDTH = 0.4

plt.bar(df_follow.index - BAR_WIDTH / 2, df_follow["total_follows"], color = "blue", label = "number of follows", width = BAR_WIDTH)

plt.bar(df_hype.index + BAR_WIDTH / 2, df_hype["total_hypes"], color = "red", label = "Number of Hypes", width = BAR_WIDTH)

plt.xticks(df_follow.index, df_follow["game_name"])

plt.legend(loc = "upper left")

plt.show()