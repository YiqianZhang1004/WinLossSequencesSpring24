import accuracy_rates
import matplotlib.pyplot as plt

seasons = []
elo_accuracy = []
elo_num = []
poll_accuracy = []
poll_num = []

top25 = []
for i in range(1,26):
    top25.append(i)

for season in range(1980, 2024):
    seasons.append(season)

    elo_rate = accuracy_rates.get_accuracy("e", [season], [], [], top25, top25, "", "")
    poll_rate = accuracy_rates.get_accuracy("p", [season], [], [], top25, top25, "", "")

    if elo_rate == (0, 0):
        elo_accuracy.append(None)
        elo_num.append(None)
    else:
        elo_accuracy.append(float(elo_rate[0]))
        elo_num.append(int(elo_rate[1]))


    if poll_rate == (0, 0):
        poll_accuracy.append(None)
        poll_num.append(None)
    else:
        poll_accuracy.append(float(poll_rate[0]))
        poll_num.append(int(poll_rate[1]))

elo_line, = plt.plot(seasons, elo_accuracy, label='Elo', color='blue')
for i, _ in enumerate(elo_num):
    if elo_num[i] is not None:
        plt.text(seasons[i], elo_accuracy[i], "", fontsize=8, color='blue', ha='center', va='bottom')


poll_line, = plt.plot([], [], label='Poll', color='red')
plt.plot(seasons, poll_accuracy, color='red')
for i, _ in enumerate(poll_num):
    if poll_num[i] is not None:
        plt.text(seasons[i], poll_accuracy[i], "", fontsize=8, color='red', ha='center', va='bottom')

plt.xlabel('Season')
plt.ylabel('Accuracy')
plt.title('Elo and Poll Accuracy of Top 25 Teams (1980 - 2019)')
plt.legend()
plt.legend(handles=[elo_line, poll_line])
plt.grid(True)

plt.savefig('data/accuracy_rates/visualizations/ep25.png')
plt.show()
