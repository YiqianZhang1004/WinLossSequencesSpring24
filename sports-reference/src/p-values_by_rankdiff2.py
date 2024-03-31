import pandas as pd
from scipy.stats import binom
import math

data = pd.read_csv("sports-reference/raw_data/matchup_selector.csv")

#######################################
# Group everything by rank difference
data["RankDiff"] = data["AwayRank"] - data["HomeRank"]
RankDiff = data["RankDiff"].to_list()
def div(x):
    return math.ceil(x/2)
data["RankDiff"] = pd.Series(map(div,RankDiff))
wins = data.groupby("RankDiff").agg("sum").reset_index()
games = data.groupby("RankDiff").agg("count").reset_index()
wins["wins"] = wins["Result"]
wins = wins[["RankDiff","wins"]]
games["games"] = games["Result"]
games = games[["RankDiff","games"]]
df = pd.merge(games,wins,how="outer",on="RankDiff")
df["WinPct"] = df["wins"] / df["games"]
########################################
# MAKE P-VALUES
df["P-Value"] = 0
winsList = df["wins"].to_list()
gamesList = df["games"].to_list()
pvals = []
for i in range(len(df)):
    k = winsList[i]
    n = gamesList[i]
    if (k < n/2):
        pval = binom.cdf(k=k,n=n,p=0.5)
    else:
        pval = 1-binom.cdf(k=k-1,n=n,p=0.5)
    pvals.append(pval)
df.iloc[:,4] = pd.Series(pvals)

RankDiff2 = df["RankDiff"].to_list()
def undiv(x):
    return str(x*2-1) + "-" + str(x*2)
df["Real RankDiff"] = pd.Series(map(undiv,RankDiff2))


df.to_csv("sports-reference/processed_data/p-values_by_rankdiff2.csv")