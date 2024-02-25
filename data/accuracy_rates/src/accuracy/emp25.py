import accuracy_rates
import matplotlib.pyplot as plt

seasons = []
elo_accuracy = []
elo_num = []
moneyline_accuracy = []
moneyline_num = []
poll_accuracy = []
poll_num = []

top25 = []
for i in range(1,26):
    top25.append(i)

for season in range(2007, 2019):
    seasons.append(season)

    elo_rate = accuracy_rates.get_accuracy("e", [season], [], [], top25, top25, "", "")
    moneyline_rate = accuracy_rates.get_accuracy("m", [season], [], [], top25, top25, "", "")
    poll_rate = accuracy_rates.get_accuracy("p", [season], [], [], top25, top25, "", "")

    if elo_rate == (0, 0):
        elo_accuracy.append(None)
        elo_num.append(None)
    else:
        elo_accuracy.append(float(elo_rate[0]))
        elo_num.append(int(elo_rate[1]))

    if moneyline_rate == (0, 0):
        moneyline_accuracy.append(None)
        moneyline_num.append(None)
    else:
        moneyline_accuracy.append(float(moneyline_rate[0]))
        moneyline_num.append(int(moneyline_rate[1]))

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

moneyline_line, = plt.plot([], [], label='Moneyline', color='green')
plt.plot(seasons, moneyline_accuracy, color='green')
for i, _ in enumerate(moneyline_num):
    if moneyline_num[i] is not None:
        plt.text(seasons[i], moneyline_accuracy[i], "", fontsize=8, color='green', ha='center', va='bottom')

poll_line, = plt.plot([], [], label='Poll', color='red')
plt.plot(seasons, poll_accuracy, color='red')
for i, _ in enumerate(poll_num):
    if poll_num[i] is not None:
        plt.text(seasons[i], poll_accuracy[i], "", fontsize=8, color='red', ha='center', va='bottom')

plt.xlabel('Season')
plt.ylabel('Accuracy')
plt.title('Elo, Moneyline, and Poll Accuracy of Top 25 Teams (2007 - 2019)')
plt.legend()
plt.legend(handles=[elo_line, moneyline_line, poll_line])
plt.grid(True)

plt.savefig('data/accuracy_rates/visualizations/emp25.png')
plt.show()
