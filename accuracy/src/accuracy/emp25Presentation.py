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

for season in range(2007, 2019):
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

plt.figure(figsize=(20, 10))


plt.plot(seasons, moneyline_accuracy, color="green", label = "Betting Market", linewidth=5)
plt.plot(seasons, poll_accuracy, color="red", label = "Poll Ranking", linewidth=5)
plt.plot(seasons, elo_accuracy, color="blue", label = "Elo Rating", linewidth=5)


plt.xlabel('Season', fontsize=40)
plt.ylabel('Percentage of\nCorrect Predictions', fontsize=45)
plt.yticks(fontsize=35)
plt.xticks(fontsize=35)
plt.legend(fontsize=30,loc='upper left')
plt.grid(True)
plt.savefig('accuracy/visualizations/presentation/emp25Presentation.png')
# plt.show()

