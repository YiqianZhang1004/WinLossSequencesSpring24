import pandas as pd
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import numpy as np
import math

df = pd.read_csv("sports-reference/football/processed_data/cfb_games_with_ranks.csv")

###########################################
# MAKE COLUMN FOR RESULT OF HIGHER RANKED TEAM
winnerRanking = df["winnerRanking"].to_list()
loserRanking = df["loserRanking"].to_list()
result = []
for i in range(len(df)):
    # Upset = 0, no upset = 1
    if winnerRanking[i] < loserRanking[i]:
        result.append(1)
    else:
        result.append(0)
df["result"] = pd.Series(result)
# rankdiff is always positive, but the higher the rank difference, the less likely the upset should be
df["rankdiff"] = df["loserRanking"] - df["winnerRanking"]
df["rankdiff"] = df["rankdiff"].abs()
df = df[(df.rankdiff <= 20) & (df.rankdiff > 0)]

###########################################
# PREDICTED WIN PCT USING LOGISTIC REGRESSION
X = pd.DataFrame(df["rankdiff"])
y= df["result"]
log_reg = LogisticRegression(random_state=0,fit_intercept=True).fit(X,y)
numbers = list(range(1,21))
pred = [sublist[1] for sublist in log_reg.predict_proba(pd.DataFrame(numbers)).tolist()]
print(pred)

# CURVE
print(log_reg.coef_)
print(log_reg.intercept_)
x = np.linspace(0,20,100)

def equation(number):
    return 1/(1+math.exp(-0.06235689*number-0.06171751))
y = [equation(number) for number in x]

#############################################
# ACTUAL WIN PCT BY RANK DIFF
wins = df.groupby("rankdiff").agg("sum").reset_index()
games = df.groupby("rankdiff").agg("count").reset_index()
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
table4.to_csv("sports-reference/football/processed_data/table4.csv")

#########################################
# PLOT
#plt.plot(table4["rankdiff"].to_list(),table4["pred"].to_list(),color="dodgerblue",label="pred")
plt.plot(x,y,color="dodgerblue",label="pred")
plt.scatter(table4["rankdiff"].to_list(),table4["act"].to_list(),color="saddlebrown",label="act")
plt.xlabel("Difference in Poll Ranking")
plt.ylabel("Win Probability")
plt.xticks([0,4,8,12,16,20])
plt.legend()
plt.show()