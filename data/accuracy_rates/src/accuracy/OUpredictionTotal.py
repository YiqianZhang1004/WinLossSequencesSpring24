import accuracy_rates
import matplotlib.pyplot as plt
import csv

seasons = list(range(2007, 2020))

outList = [["method", "accuracy", "total", "over", "under"]]

e = accuracy_rates.getAccuracy("e", seasons, [], [], [], [], [], -1, -1, -1, -1)
m = accuracy_rates.getAccuracy("m", seasons, [], [], [], [], [], -1, -1, -1, -1)
p = accuracy_rates.getAccuracy("p", seasons, [], [], [], [], [], -1, -1, -1, -1)

outList.append(["e"] + list(e))
outList.append(["m"] + list(m))
outList.append(["p"] + list(p))

eloOver = e[2]
eloUnder = e[3]
moneylineOver = m[2]
moneylineUnder = m[3]
pollUnder = p[2]
pollOver = p[3]

categories = ["Elo+","Elo-","ML+","ML-","Poll+","Poll-"]
values = [eloOver, eloUnder, moneylineOver,moneylineUnder,pollOver,pollUnder]
colors = ['blue','cyan','green','yellow','red','magenta']


plt.bar(categories, values, color=colors)

plt.ylabel('Number of Games')
plt.title('Elo, Moneyline, and Poll Over/Under (+/-) Predictions (2007 - 2019)')

plt.savefig('data/accuracy_rates/visualizations/OUempTotal.png')

plt.show()


with open("data/accuracy_rates/visualization_data/OUpredictionTotal.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(outList)

