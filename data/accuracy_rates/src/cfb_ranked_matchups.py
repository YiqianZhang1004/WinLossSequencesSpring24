import pandas as pd
data = pd.read_csv("data/cfbd/processed_data/cfbd_close_only.csv")
matrix = pd.DataFrame(columns=range(1,26))

#If home team is ranked i:
for i in range(1,26):
    data_r = data[["homeRank","awayRank","result"]][data.homeRank == i]
    groups = data_r.groupby(["awayRank","result"]).agg("count").reset_index()

    wins_for_home = groups[groups.result == 1].reset_index()
    wins_for_home["wins"] = wins_for_home["homeRank"]
    wins_for_home = wins_for_home[["awayRank","wins"]]
    for j in range(1,26):
        if (wins_for_home["awayRank"].to_list().count(j) <= 0):
            wins_for_home.loc[len(wins_for_home)] = [j,0]


    games_for_home = groups.groupby("awayRank").agg("sum").reset_index()
    games_for_home["games"] = games_for_home["homeRank"]
    games_for_home = games_for_home[["awayRank","games"]]
    for k in range(1,26):
        if (games_for_home["awayRank"].to_list().count(k) <= 0):
            games_for_home.loc[len(games_for_home)] = [k,0]

    df = pd.merge(wins_for_home,games_for_home,how="outer",on="awayRank").sort_values(by="awayRank")
    df["homeWinrate"] = df["wins"] / df["games"]
    if len(df) == 25:
        matrix.loc[len(matrix)] = df["homeWinrate"].to_list()
matrix.to_csv("data/accuracy_rates/processed_data/cfb_ranked_matchups_matrix.csv")