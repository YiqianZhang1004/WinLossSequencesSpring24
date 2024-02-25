import accuracy_rates
import matplotlib.pyplot as plt

seasons = []
elo_accuracy = []
moneyline_accuracy = []

for season in range(2007, 2019):
    seasons.append(season)

    elo_rate = accuracy_rates.get_accuracy("e", [season], [], [], [], [], "", "")
    moneyline_rate = accuracy_rates.get_accuracy("m", [season], [], [], [], [], "", "")

    if elo_rate == (0, 0):
        elo_accuracy.append(None)
    else:
        elo_accuracy.append(float(elo_rate[0]))

    if moneyline_rate == (0, 0):
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

plt.savefig('data/accuracy_rates/visualizations/emFull.png')
plt.show()
