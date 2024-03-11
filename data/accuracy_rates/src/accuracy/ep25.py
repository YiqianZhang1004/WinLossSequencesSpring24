import accuracy_rates
import matplotlib.pyplot as plt

seasons = []
elo_accuracy = []
poll_accuracy = []

top25 = []
for i in range(1,26):
    top25.append(i)

for season in range(1980, 2024):
    seasons.append(season)

    elo_rate = accuracy_rates.getAccuracy("e", [season],[], [], [], top25, top25,-1, -1, -1, -1,  "", "")
    poll_rate = accuracy_rates.getAccuracy("p", [season],[], [], [], top25, top25, -1, -1, -1, -1, "", "")

    if elo_rate == (0, 0, 0, 0):
        elo_accuracy.append(None)
    else:
        elo_accuracy.append(float(elo_rate[0]))


    if poll_rate == (0, 0, 0, 0):
        poll_accuracy.append(None)
    else:
        poll_accuracy.append(float(poll_rate[0]))

plt.plot(seasons, elo_accuracy, color="blue", label = "Elo")
plt.plot(seasons, poll_accuracy, color="red", label = "Poll")

plt.xlabel('Season')
plt.ylabel('Accuracy')
plt.title('Elo and Poll Accuracy of Top 25 Teams (1980 - 2019)')
plt.legend()
plt.grid(True)

plt.savefig('data/accuracy_rates/visualizations/ep25.png')
plt.show()
