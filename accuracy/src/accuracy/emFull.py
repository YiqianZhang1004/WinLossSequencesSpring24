import accuracyFunction
import matplotlib.pyplot as plt
import csv

seasons = []
elo_accuracy = []
moneyline_accuracy = []

outList = [["method", "season", "accuracy", "total", "over", "under"]]

for season in range(2007, 2024):
    seasons.append(season)

    elo_rate = accuracyFunction.getAccuracy("e", [season], [], [], [], [], [],"","","","")
    moneyline_rate = accuracyFunction.getAccuracy("m", [season], [], [], [], [], [], "","","","")

    outList.append(["e", season] + list(elo_rate))
    outList.append(["m", season] + list(moneyline_rate))

    if elo_rate == (0, 0, 0, 0):
        elo_accuracy.append(None)
    else:
        elo_accuracy.append(float(elo_rate[0]))

    if moneyline_rate == (0, 0, 0, 0):
        moneyline_accuracy.append(None)
    else:
        moneyline_accuracy.append(float(moneyline_rate[0]))

plt.plot(seasons, elo_accuracy, color="blue", label = "Elo")
plt.plot(seasons, moneyline_accuracy, color="green", label = "Moneyline")

plt.xlabel('Season')
plt.ylabel('Accuracy')
plt.title('Elo and Moneyline Accuracy of All Teams (2007 - 2019)')
plt.legend()
plt.grid(True)

plt.savefig('accuracy/visualizations/emFull.png')
plt.show()


with open("accuracy/visualization_data/emFull.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(outList)

