import pandas as pd
from scipy.stats import binom

data = pd.read_csv("sports-reference/raw_data/matchup_selector.csv")
data = data[["HomeRank","AwayRank","Result"]]
data["MatchupPair"] = str(data["HomeRank"]) + "-" + str(data["AwayRank"])
wins = data.groupby(by="MatchupPair").agg("sum").reset_index()
wins["wins"] = wins["Result"]
wins = wins[["MatchupPair","wins"]]
games = data.groupby(by="MatchupPair").agg("count").reset_index()
games["games"] = games["Result"]
games = games[["MatchupPair","games"]]
df = pd.merge(games,wins,how="outer",on="MatchupPair")

df["p-value"] = binom(n=df["games"],p=0.5).cdf(df["games"])
df["HomeRank"] = df["MatchupPair"].split("-")[0]
df["AwayRank"] = df["MatchupPair"].split("-")[1]
#df["p-value"] = binom.cdf(n=df["games"],p=0.5,k=df="wins")
print(df)