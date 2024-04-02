import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("sports-reference/raw_data/matchup_selector.csv")

yearstrs = df["Year"].to_list()
yearints = []
for i in range(len(yearstrs)):
    yearint = yearstrs[i].split("-")[0]
    yearints.append(int(yearint))
df["Year"] = pd.Series(yearints)

def brier(predict_list,actual_list):
    if (len(predict_list) != len(actual_list)):
        return False
    N = len(predict_list)
    sum = 0
    for j in range(N):
        sum = sum + (predict_list[j] - actual_list[j])**2
    return sum / N

recursive_accuracy = []
for i in range(1949,2024):
    if (i == 1949):
        past = df[df.Year == 1949]
    else:
        past = df[df.Year < i]
    present = df[df.Year == i]
    X_train = past[["HomeRank","AwayRank"]]
    y_train = past["Result"]
    X_test = present[["HomeRank","AwayRank"]]
    y_test = present["Result"]
    log_reg = LogisticRegression(random_state=0,fit_intercept=True).fit(X_train,y_train)
    probit_predictions = log_reg.predict_proba(X_test).tolist()
    probit_predictions_list = [sublist[1] for sublist in probit_predictions]

    past_win_pct = len(past[((past.HomeRank < past.AwayRank) & (past.Result == 1))
                        |((past.AwayRank < past.HomeRank) & (past.Result == 0))])/len(past)
    
    HomeRanks = past["HomeRank"].to_list()
    AwayRanks = past["AwayRank"].to_list()
    Results = past["Result"].to_list()
    present = []
    for j in range(len(past)):
        if ((HomeRanks[j] < AwayRanks[j]) & (Results[j] == 1)):
            present.append(1)
        elif ((HomeRanks[j] > AwayRanks[j]) & (Results[j] == 0)):
            present.append(1)
        else:
            present.append(0)

    baserate = []
    for j in range(len(present)):
        baserate.append(past_win_pct)
    recursive_accuracy.append({"Year":i,"Probit Brier Scores":brier(probit_predictions_list,y_test.to_list()),
                               "Baserate Brier Scores":brier(baserate,present)})
    
recursive_accuracy_df = pd.DataFrame(recursive_accuracy)
recursive_accuracy_df.to_csv("sports-reference/processed_data/recursive_probit_brier_scores.csv")