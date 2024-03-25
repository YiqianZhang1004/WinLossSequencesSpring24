import accuracyFunction
import matplotlib.pyplot as plt
import csv

seasons = list(range(2007, 2024))

outList = [["method", "accuracy", "total", "over", "under"]]

e = accuracyFunction.getAccuracy("e", seasons, [], [], [], [], [], '','','','')
m = accuracyFunction.getAccuracy("m", seasons, [], [], [], [], [], '','','','')
p = accuracyFunction.getAccuracy("p", seasons, [], [], [], [], [], '','','','')

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
plt.title('Elo, Moneyline, and Poll Over/Under (+/-) Predictions (2007 - 2024)')

plt.savefig('accuracy/visualizations/OUempTotal.png')

plt.show()


with open("accuracy/visualization_data/OUpredictionTotal.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(outList)

