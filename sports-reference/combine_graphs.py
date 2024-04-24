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

def coinflipprob(number):
    return 0.5
y_coinflip = [coinflipprob(number) for number in x]

plt.figure(figsize=(16,8))

plt.scatter(cfb["rankdiff"].to_list(),cfb["act"].to_list(),color="red",label="Actual Win Probability (Football)", s=100)
plt.plot(x,y_cfb,color="red",label="Probit Regression Line (Football)", linewidth=5)
plt.scatter(cbb["rankdiff"].to_list(),cbb["act"].to_list(),color="blue",label="Actual Win Probability (Basketball)",s=100)
plt.plot(x,y_cbb,color="blue",label="Probit Regression Line (Basketball)", linewidth=5)
plt.plot(x,y_coinflip,color="black",label="0.5 Win Probability (Coin Flip Model)",linewidth=3)
plt.xlabel("Difference in Poll Ranking", fontsize=40)
plt.ylabel("Win Probability", fontsize=40)
plt.xticks([0,2,4,6,8,10,12,14,16,18,20],fontsize=20)
plt.yticks(fontsize=20)
plt.legend(fontsize=20, loc='upper left')
plt.savefig("sports-reference/combinedGraph.png")
plt.show()