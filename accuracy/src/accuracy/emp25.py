import accuracyFunction
import matplotlib.pyplot as plt
import csv

seasons = []
elo_accuracy = []
moneyline_accuracy = []
poll_accuracy = []

top25 = []
for i in range(1,26):
    top25.append(i)


outList = [["method", "season", "accuracy", "total", "over", "under"]]

for season in range(2007, 2024):
    seasons.append(season)

    elo_rate = accuracyFunction.getAccuracy("e", [season], [],[], [], top25, top25,"","","","")
    moneyline_rate = accuracyFunction.getAccuracy("m", [season], [],[], [], top25, top25, "","","","")
    poll_rate = accuracyFunction.getAccuracy("p", [season], [],[], [], top25, top25, "","","","")

    outList.append(["e", season] + list(elo_rate))
    outList.append(["m", season] + list(moneyline_rate))
    outList.append(["p", season] + list(poll_rate))


    if elo_rate == (0, 0,0,0):
        elo_accuracy.append(None)
    else:
        elo_accuracy.append(float(elo_rate[0]))

    if moneyline_rate == (0, 0,0,0):
        moneyline_accuracy.append(None)
    else:
        moneyline_accuracy.append(float(moneyline_rate[0]))

    if poll_rate == (0, 0,0,0):
        poll_accuracy.append(None)
    else:
        poll_accuracy.append(float(poll_rate[0]))

plt.plot(seasons, elo_accuracy, color="blue", label = "Elo")
plt.plot(seasons, moneyline_accuracy, color="green", label = "Moneyline")
plt.plot(seasons, poll_accuracy, color="red", label = "Poll")

plt.xlabel('Season')
plt.ylabel('Accuracy')
plt.title('Elo, Moneyline, and Poll Accuracy of Top 25 Teams (2007 - 2024)')
plt.legend()
plt.grid(True)

plt.savefig('accuracy/visualizations/emp25.png')
plt.show()


with open("accuracy/visualization_data/emp25.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(outList)

