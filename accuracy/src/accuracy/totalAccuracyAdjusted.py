import accuracyFunction
import adjustedEloAccuracyFunction
import matplotlib.pyplot as plt

seasons = list(range(2007, 2024))

e = accuracyFunction.getAccuracy("e", seasons, [],[], [], [], [], '','','','')
m = accuracyFunction.getAccuracy("m", seasons, [],[], [], [], [], '','','','')
p = accuracyFunction.getAccuracy("p", seasons, [],[], [], [], [], '','','','')

elo_accuracy = e[0]
moneyline_accuracy = m[0]
poll_accuracy = p[0]

e25 = adjustedEloAccuracyFunction.getAccuracy(seasons, [],[],[],[],[],'','','','',25)[0]
e43 = adjustedEloAccuracyFunction.getAccuracy(seasons, [],[],[],[],[],'','','','',43)[0]
e73 = adjustedEloAccuracyFunction.getAccuracy(seasons, [],[],[],[],[],'','','','',73)[0]
e88 = adjustedEloAccuracyFunction.getAccuracy(seasons, [],[],[],[],[],'','','','',88)[0]
e150 = adjustedEloAccuracyFunction.getAccuracy(seasons, [],[],[],[],[],'','','','',150)[0]


categories = ["ML","Elo", "AE25", "AE43", "AE73", "AE88", "AE150", "Poll"]
values = [moneyline_accuracy, elo_accuracy, e25, e43, e73, e88, e150, poll_accuracy]
colors = ['green', 'blue', "navy", 'steelblue', 'royalblue', 'skyblue', 'cornflowerblue','red']

plt.bar(categories, values, color=colors)

plt.ylabel('Total Accuracy Rate')
plt.title('Elo, ML, Adjusted Elo, Adjusted ML, and Poll Total Accuracy Rates (2007 - 2024)')

plt.ylim(60, 80)

plt.savefig('accuracy/visualizations/totalWithAdjusted.png')

plt.show()


