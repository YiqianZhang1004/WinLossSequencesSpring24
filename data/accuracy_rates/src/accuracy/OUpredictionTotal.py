import accuracy_rates
import matplotlib.pyplot as plt

seasons = list(range(2007, 2020))

e = accuracy_rates.getAccuracy("e", seasons, [], [], [], [], [], -1, -1, -1, -1, "", "")
m = accuracy_rates.getAccuracy("m", seasons, [], [], [], [], [], -1, -1, -1, -1, "", "")
p = accuracy_rates.getAccuracy("p", seasons, [], [], [], [], [], -1, -1, -1, -1, "", "")

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

plt.ylabel('Total Accuracy Rate')
plt.title('Elo, Moneyline, and Poll Over/Under (+/-) Predictions (2007 - 2019)')



plt.savefig('data/accuracy_rates/visualizations/OUempTotal.png')

plt.show()
