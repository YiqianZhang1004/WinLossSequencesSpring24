import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("sports-reference/raw_data/matchup_selector.csv")
X = df[["HomeRank","AwayRank"]]
y = df["Result"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.3, random_state=21)
log_reg = LogisticRegression(random_state=0,fit_intercept=True).fit(X_train,y_train)

print(log_reg.score(X_test,y_test))

print(log_reg.coef_)
print(log_reg.intercept_)