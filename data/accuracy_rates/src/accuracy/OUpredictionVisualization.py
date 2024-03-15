import accuracy_rates
import matplotlib.pyplot as plt

seasons = []
eloOver = []
moneylineOver = []
pollOver = []
eloUnder = []
moneylineUnder = []
pollUnder = []

top25 = []
for i in range(1,26):
    top25.append(i)

for season in range(2007, 2019):
    seasons.append(season)

    elo_rate = accuracy_rates.getAccuracy("e", [season], [],[], [], top25, top25, -1, -1, -1, -1, "", "")
    moneyline_rate = accuracy_rates.getAccuracy("m", [season],[], [], [], top25, top25, -1, -1, -1, -1, "", "")
    poll_rate = accuracy_rates.getAccuracy("p", [season],[], [], [], top25, top25, -1, -1, -1, -1, "", "")

    if elo_rate == (0, 0,0,0):
        eloOver.append(None)
        eloUnder.append(None)
    else:
        eloOver.append(float(elo_rate[2]))
        eloUnder.append(float(elo_rate[3]))

    if moneyline_rate == (0, 0,0,0):
        moneylineOver.append(None)
        moneylineUnder.append(None)
    else:
        moneylineOver.append(float(moneyline_rate[2]))
        moneylineUnder.append(float(moneyline_rate[3]))

    if poll_rate == (0, 0,0,0):
        pollOver.append(None)
        pollUnder.append(None)
    else:
        pollOver.append(float(poll_rate[2]))
        pollUnder.append(float(poll_rate[3]))

plt.plot(seasons, eloOver, color="blue", label = "Elo+")
plt.plot(seasons, moneylineOver, color="green", label = "ML+")
plt.plot(seasons, pollOver, color="red", label = "Poll+")

plt.plot(seasons, eloUnder, color="cyan", label = "Elo-")
plt.plot(seasons, moneylineUnder, color="yellow", label = "ML-")
plt.plot(seasons, pollUnder, color="magenta", label = "Poll-")

plt.xlabel('Season')
plt.ylabel('Number of Games')
plt.title('Elo, ML, and Poll Over/Under (+/-) Predictions Top 25 Teams (2007 - 2019)')
plt.grid(True)
plt.legend()

plt.savefig('data/accuracy_rates/visualizations/OUemp25.png')
plt.show()
