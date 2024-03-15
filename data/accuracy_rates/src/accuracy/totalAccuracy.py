import accuracy_rates
import matplotlib.pyplot as plt
import csv

seasons = list(range(2007, 2020))

outList = [["method", "accuracy", "total", "over", "under"]]

e = accuracy_rates.getAccuracy("e", seasons, [],[], [], [], [], -1, -1, -1, -1)
m = accuracy_rates.getAccuracy("m", seasons, [],[], [], [], [], -1, -1, -1, -1)
p = accuracy_rates.getAccuracy("p", seasons, [],[], [], [], [], -1, -1, -1, -1)

elo_accuracy = e[0]
moneyline_accuracy = m[0]
poll_accuracy = p[0]

outList.append(["e"] + list(e))
outList.append(["m"] + list(m))
outList.append(["p"] + list(p))


categories = ["Moneyline","Elo" ,"Poll"]
values = [moneyline_accuracy, elo_accuracy, poll_accuracy]
colors = ['green', 'blue', 'red']

plt.bar(categories, values, color=colors)

plt.ylabel('Total Accuracy Rate')
plt.title('Elo, Moneyline, and Poll Total Accuracy Rates of All Teams (2007 - 2019)')

plt.ylim(50, 80)

plt.savefig('data/accuracy_rates/visualizations/empTotalFull.png')

plt.show()


with open("data/accuracy_rates/visualization_data/totalAccuracy.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(outList)

