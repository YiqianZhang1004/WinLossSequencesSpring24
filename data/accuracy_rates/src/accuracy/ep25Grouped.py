import accuracy_rates
import matplotlib.pyplot as plt

s = ["80 - 84", "85 - 89", "90 - 94", "95 - 99", "00 - 04",
     "05 - 09", "10 - 14", "15 - 19"]

elo_accuracy = []
poll_accuracy = []

seasons = list(range(1980, 2020))
grouped_seasons = [seasons[i:i+5] for i in range(0, len(seasons), 5)]
top25 = [i for i in range(1, 26)]

for groupedList in grouped_seasons:    
    elo_rate = accuracy_rates.get_accuracy("e", groupedList, [], [], top25, top25, "", "")
    poll_rate = accuracy_rates.get_accuracy("p", groupedList, [], [], top25, top25, "", "")

    if elo_rate == (0, 0):
        elo_accuracy.append(None)
    else:
        elo_accuracy.append(float(elo_rate[0]))

    if poll_rate == (0, 0):
        poll_accuracy.append(None)
    else:
        poll_accuracy.append(float(poll_rate[0]))



plt.plot(s, elo_accuracy, color='blue', label='Elo')
plt.plot(s, poll_accuracy, color='red', label='Poll')


plt.xlabel('Season')
plt.ylabel('Accuracy')
plt.title('Elo and Poll Accuracy of Top 25 Teams (1980 - 2019, Grouped)')
plt.legend()
plt.grid(True)

plt.savefig('data/accuracy_rates/visualizations/ep25Grouped.png')
plt.show()
