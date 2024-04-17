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

plt.scatter(cfb["rankdiff"].to_list(),cfb["act"].to_list(),color="red",label="Actual Win Probability (Football)")
plt.plot(x,y_cfb,color="red",label="Probit Regression Line (Football)")
plt.scatter(cbb["rankdiff"].to_list(),cbb["act"].to_list(),color="blue",label="Actual Win Probability (Basketball)")
plt.plot(x,y_cbb,color="blue",label="Probit Regression Line (Basketball)")
plt.xlabel("Difference in Poll Ranking")
plt.ylabel("Win Probability")
plt.xticks([0,4,8,12,16,20])
plt.legend()
plt.show()