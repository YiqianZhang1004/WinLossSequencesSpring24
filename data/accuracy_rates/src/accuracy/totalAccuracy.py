import accuracy_rates
import matplotlib.pyplot as plt

seasons = list(range(2007, 2020))


elo_accuracy = accuracy_rates.get_accuracy("e", seasons, [], [], [], [], "", "")[0]
moneyline_accuracy = accuracy_rates.get_accuracy("m", seasons, [], [], [], [], "", "")[0]
poll_accuracy = accuracy_rates.get_accuracy("p", seasons, [], [], [], [], "", "")[0]

categories = ["elo", "moneyline", "poll"]
values = [elo_accuracy, moneyline_accuracy, poll_accuracy]

plt.bar(categories, values, color='skyblue')

plt.ylabel('Total Accuracy Rate')
plt.title('Elo, Moneyline, and Poll Total Accuracy Rates of All Teams (2007 - 2019)')

plt.savefig('data/accuracy_rates/visualizations/empTotalFull.png')

plt.show()
