import pandas as pd
from scipy.stats import binom
import math

data = pd.read_csv("sports-reference/raw_data/matchup_selector.csv")

#MAKE MATCHUP PAIRS
homeRanks = data["HomeRank"].to_list()
awayRanks = data["AwayRank"].to_list()
data["MatchupPair"] = 0
data["FakeMatchupPair"] = 0
matchupPairs = []
fakeMatchupPairs = []
for i in range(len(data)):
    homeRank = homeRanks[i]
    awayRank = awayRanks[i]
    fakeHomeRank = math.floor(homeRank/2+1)
    fakeAwayRank = math.floor(awayRank/2+1)
    matchupPairs.append(str(homeRank) + "-" + str(awayRank))
    fakeMatchupPairs.append(str(fakeHomeRank) + "-" + str(fakeAwayRank))
data.iloc[:,11] = pd.Series(matchupPairs)
data.iloc[:,12] = pd.Series(fakeMatchupPairs)
#####################################################
# COUNT NUMBER OF WINS AND GAMES
#data["MatchupPair"] = str(data["HomeRank"]) + "-" + str(data["AwayRank"])
wins = data.groupby(by="MatchupPair").agg("sum").reset_index()
wins["wins"] = wins["Result"]
wins = wins[["MatchupPair","wins"]]
games = data.groupby(by="MatchupPair").agg("count").reset_index()
games["games"] = games["Result"]
games = games[["MatchupPair","games"]]
df = pd.merge(games,wins,how="outer",on="MatchupPair")

combinedWins = data.groupby(by="FakeMatchupPair").agg("sum").reset_index()
combinedWins["wins"] = combinedWins["Result"]
combinedWins = combinedWins[["FakeMatchupPair","wins"]]
combinedGames = data.groupby(by="FakeMatchupPair").agg("count").reset_index()
combinedGames["games"] = combinedGames["Result"]
combinedGames = combinedGames[["FakeMatchupPair","games"]]
df2 = pd.merge(combinedGames,combinedWins,how="outer",on="FakeMatchupPair")

df["WinPct"] = df["wins"] / df["games"]
df2["WinPct"] = df2["wins"] / df2["games"]

###########################################################
# TURN MATCHUP PAIRS BACK INTO HOME AND AWAY RANKS
df["HomeRank"] = 0
df["AwayRank"] = 0
matchupPairs2 = df["MatchupPair"].to_list()
df2["HomeRank"] = 0
df2["AwayRank"] = 0
fakeMatchupPairs2 = df2["FakeMatchupPair"].to_list()

homeRanks2 = []
awayRanks2 = []
fakeHomeRanks2 = []
fakeAwayRanks2 = []
for i in range(len(matchupPairs2)):
    homeRanks2.append(matchupPairs2[i].split("-")[0])
    awayRanks2.append(matchupPairs2[i].split("-")[1])
df.iloc[:,4] = pd.Series(homeRanks2)
df.iloc[:,5] = pd.Series(awayRanks2)
for i in range(len(fakeMatchupPairs2)):
    fakeHomeRanks2.append(int(fakeMatchupPairs2[i].split("-")[0]))
    fakeAwayRanks2.append(int(fakeMatchupPairs2[i].split("-")[1]))
df2.iloc[:,4] = pd.Series(fakeHomeRanks2)
df2.iloc[:,5] = pd.Series(fakeAwayRanks2)
########################################
# MAKE P-VALUES
df["P-Value"] = 0
df2["P-Value"] = 0
winsList = df["wins"].to_list()
gamesList = df["games"].to_list()
combinedWinsList = df2["wins"].to_list()
combinedGamesList = df2["games"].to_list()
pvals = []
combinedpvals = []
for i in range(len(df)):
    k = winsList[i]
    n = gamesList[i]
    if (k < n/2):
        pval = binom.cdf(k=k,n=n,p=0.5)
    else:
        pval = 1-binom.cdf(k=k-1,n=n,p=0.5)
    pvals.append(pval)
for i in range(len(df2)):
    k = combinedWinsList[i]
    n = combinedGamesList[i]
    pval = binom.cdf(k=k-1,n=n,p=0.5)
    if (k < n/2):
        pval = binom.cdf(k=k,n=n,p=0.5)
    else:
        pval = 1-binom.cdf(k=k-1,n=n,p=0.5)
    combinedpvals.append(pval)
df.iloc[:,6] = pd.Series(pvals)
df2.iloc[:,6] = pd.Series(combinedpvals)

# TURN FAKE RANKS INTO CORRECT LABELS
realHomeLabels = []
realAwayLabels = []
for i in range(len(df2)):
    realHomeLabels.append(str(fakeHomeRanks2[i]*2 - 1) + "-" + str(fakeHomeRanks2[i]*2))
    realAwayLabels.append(str(fakeAwayRanks2[i]*2 - 1) + "-" + str(fakeAwayRanks2[i]*2))
df2.iloc[:,4] = pd.Series(realHomeLabels)
df2.iloc[:,5] = pd.Series(realAwayLabels)


df.to_csv("sports-reference/processed_data/p-values.csv")
df2.to_csv("sports-reference/processed_data/combined-p-values.csv")