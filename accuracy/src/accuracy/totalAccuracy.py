import accuracyFunction
import matplotlib.pyplot as plt
import csv

seasons = list(range(2007, 2024))

outList = [["method", "accuracy", "total", "over", "under"]]

e = accuracyFunction.getAccuracy("e", seasons, [],[], [], [], [], '','','','')
m = accuracyFunction.getAccuracy("m", seasons, [],[], [], [], [], '','','','')
p = accuracyFunction.getAccuracy("p", seasons, [],[], [], [], [], '','','','')

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
plt.title('Elo, Moneyline, and Poll Total Accuracy Rates of All Teams (2007 - 2024)')

plt.ylim(50, 80)

plt.savefig('accuracy/visualizations/empTotalFull.png')

plt.show()


with open("accuracy/visualization_data/totalAccuracy.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(outList)

