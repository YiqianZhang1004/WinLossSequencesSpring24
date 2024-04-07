import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("sports-reference/raw_data/matchup_selector.csv")

def ignorelocation(df):
    df["rankdiff"] = df["AwayRank"] - df["HomeRank"]
    rankdiff = df["rankdiff"].to_list()
    result = df["Result"].to_list()

    rankdiff2 = []
    result2 = []
    for i in range(len(df)):
        if ((rankdiff[i] < 0) & (result[i] == 1)):
            rankdiff2.append(0-rankdiff[i])
            result2.append(0)
        elif ((rankdiff[i] < 0) & (result[i] == 0)):
            rankdiff2.append(0-rankdiff[i])
            result2.append(1)
        else:
            rankdiff2.append(rankdiff[i])
            result2.append(result[i])

    return pd.DataFrame({"rankdiff":rankdiff2,"result":result2})

df2 = ignorelocation(df)
X = pd.DataFrame(df2["rankdiff"])
y = df2["result"]

###########################################
# PREDICTED WIN PCT USING LOGISTIC REGRESSION
log_reg = LogisticRegression(random_state=0,fit_intercept=True).fit(X,y)
numbers = list(range(1,25))
pred = [sublist[1] for sublist in log_reg.predict_proba(pd.DataFrame(numbers)).tolist()]
print(pred)

#############################################
# ACTUAL WIN PCT BY RANK DIFF
wins = df2.groupby("rankdiff").agg("sum").reset_index()
games = df2.groupby("rankdiff").agg("count").reset_index()
wins["wins"] = wins["result"]
wins = wins[["rankdiff","wins"]]
games["games"] = games["result"]
games = games[["rankdiff","games"]]
df = pd.merge(games,wins,how="outer",on="rankdiff")
df["WinPct"] = df["wins"] / df["games"]
act = df["WinPct"].to_list()
num_events = df["games"].to_list()

############################################
# MAKE DATAFRAME
table4 = pd.DataFrame({"rankdiff":numbers,"pred":pred,"act":act,"num_events":num_events})
table4.to_csv("sports-reference/processed_data/table4.csv")