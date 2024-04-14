import accuracyFunction
import matplotlib.pyplot as plt

elo_accuracy = []
moneyline_accuracy = []
poll_accuracy = []

top25 = list(range(1, 26))


e = accuracyFunction.getAccuracy("e", [], [],[], [], top25, top25,"","","","")[0]
m = accuracyFunction.getAccuracy("m", [], [],[], [], top25, top25, "","","","")[0]
p = accuracyFunction.getAccuracy("p", [], [],[], [], top25, top25, "","","","")[0]


categories = ["Moneyline", "Elo", "Rank"]
values = [m, e, p]
colors = ['green', 'blue','red']

plt.bar(categories, values, color=colors)

plt.ylabel('Total Accuracy Rate')
plt.title('ML, Elo, and Rank Total Accuracy Rates of Top 25 Matchups')

plt.ylim(60, 75)

plt.savefig('accuracy/visualizations/presentation/emp25TotalPresentation.png')

plt.show()
