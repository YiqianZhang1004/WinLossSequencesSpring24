import pandas as pd

seasons = []
for i in range(1980, 2024):
    seasons.append(i)

for season in seasons:
    # sorting games by ID
    games_df = pd.read_csv("data/cfbd/raw_data/games/" + str(season) + "_games.csv")
    games_df.sort_values(by = "Id")
    games_df.to_csv("data/cfbd/raw_data/sorted_games/sorted_"+str(season)+"_games.csv",index=False)

    # sorting betting data by ID
    # only have betting data starting in 2013
    if (season>=2013):
        lines_df = pd.read_csv("data/cfbd/raw_data/lines/"+str(season) + "_lines.csv")
        lines_df.sort_values(by="Id")
        lines_df.to_csv("data/cfbd/raw_data/sorted_lines/sorted_"+str(season) + "_lines.csv",index=False)