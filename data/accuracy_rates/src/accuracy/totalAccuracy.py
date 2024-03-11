import accuracy_rates
import matplotlib.pyplot as plt

seasons = list(range(2007, 2020))


elo_accuracy = accuracy_rates.getAccuracy("e", seasons, [], [], [], [], -1, -1, -1, -1, "", "")[0]
moneyline_accuracy = accuracy_rates.getAccuracy("m", seasons, [], [], [], [], -1, -1, -1, -1, "", "")[0]
poll_accuracy = accuracy_rates.getAccuracy("p", seasons, [], [], [], [], -1, -1, -1, -1, "", "")[0]

categories = ["Moneyline","Elo" ,"Poll"]
values = [moneyline_accuracy, elo_accuracy, poll_accuracy]
colors = ['green', 'blue', 'red']

plt.bar(categories, values, color=colors)

plt.ylabel('Total Accuracy Rate')
plt.title('Elo, Moneyline, and Poll Total Accuracy Rates of All Teams (2007 - 2019)')

plt.ylim(50, 80)


plt.savefig('data/accuracy_rates/visualizations/empTotalFull.png')

plt.show()
