import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("sports-reference/basketball/raw_data/matchup_selector.csv")

#########################
# BRIER
def brier(predict_list,actual_list):
        if (len(predict_list) != len(actual_list)):
            return False
        N = len(predict_list)
        sum = 0
        for j in range(N):
            sum = sum + (predict_list[j] - actual_list[j])**2
        return sum / N

###########################
# CONVERT BOOSTED RANK TO REAL RANK
def boostedtoreal(boosted, boost):
     return boosted - boost

def realtoboosted(real, boost):
     return real + boost

####################################
# REAL WIN PCT
df["RankDiff"] = df["AwayRank"] - df["HomeRank"]
wins = df.groupby("RankDiff").agg("sum").reset_index()
games = df.groupby("RankDiff").agg("count").reset_index()
wins["wins"] = wins["Result"]
wins = wins[["RankDiff","wins"]]
games["games"] = games["Result"]
games = games[["RankDiff","games"]]
df2 = pd.merge(games,wins,how="outer",on="RankDiff")
df2["WinPct"] = df2["wins"] / df2["games"]
act = df2["WinPct"].to_list()

#############################
# BOOST HOME RANK AND FIND BRIER SCORE
brierscores = []
for i in range(14):
    dftemp = pd.read_csv("sports-reference/basketball/raw_data/matchup_selector.csv")
    dftemp["HomeRank"] = dftemp["HomeRank"] - i
    dftemp["rankdiff"] = dftemp["AwayRank"] - dftemp["HomeRank"]
    X = pd.DataFrame(dftemp["rankdiff"])
    y = dftemp["Result"]
    log_reg = LogisticRegression(random_state=0,fit_intercept=True).fit(X,y)
    numbers = list(range(realtoboosted(-24,i),0)) + list(range(1,realtoboosted(25,i)))
    pred = [sublist[1] for sublist in log_reg.predict_proba(pd.DataFrame(numbers)).tolist()]
    #df3 = pd.DataFrame({"realrankdiff":[boostedtoreal(number,i) for number in numbers],"pred":pred})
    brierscore = brier(pred,act)
    brierscores.append({"boost":i,"brierscore":brierscore})
results = pd.DataFrame(brierscores)
print(results)