import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt

cbb = pd.read_csv("sports-reference/basketball/processed_data/table4.csv")
cfb = pd.read_csv("sports-reference/football/processed_data/table4.csv")

x = np.linspace(0,20,100)

def cbbcurve(number):
    return 1/(1+math.exp(-0.04863526*number+0.01395222))
y_cbb = [cbbcurve(number) for number in x]

def cfbcurve(number):
    return 1/(1+math.exp(-0.06235689*number-0.06171751))
y_cfb = [cfbcurve(number) for number in x]

plt.plot(x,y_cfb,color="green",label="Predicted Win Probability (Football)")
plt.scatter(cfb["rankdiff"].to_list(),cfb["act"].to_list(),color="green",label="Actual Win Pct (Football)")
plt.plot(x,y_cbb,color="darkorange",label="Predicted Win Probability (Basketball)")
plt.scatter(cbb["rankdiff"].to_list(),cbb["act"].to_list(),color="darkorange",label="Actual Win Pct (Basketball)")
plt.xlabel("Difference in Poll Ranking")
plt.ylabel("Win Probability")
plt.xticks([0,4,8,12,16,20])
plt.legend()
plt.show()