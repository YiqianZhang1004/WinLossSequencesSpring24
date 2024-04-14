import accuracyFunction
import adjustedEloAccuracyFunction
import matplotlib.pyplot as plt

seasons = list(range(2007, 2024))

e = accuracyFunction.getAccuracy("e", seasons, [],[], [], [], [], '','','','')[0]
m = accuracyFunction.getAccuracy("m", seasons, [],[], [], [], [], '','','','')[0]
p = accuracyFunction.getAccuracy("p", seasons, [],[], [], [], [], '','','','')[0]

e25 = adjustedEloAccuracyFunction.getAccuracy(seasons, [],[],[],[],[],'','','','',25)[0]
e50 = adjustedEloAccuracyFunction.getAccuracy(seasons, [],[],[],[],[],'','','','',50)[0]
e73 = adjustedEloAccuracyFunction.getAccuracy(seasons, [],[],[],[],[],'','','','',73)[0]
e100 = adjustedEloAccuracyFunction.getAccuracy(seasons, [],[],[],[],[],'','','','',100)[0]
e125 = adjustedEloAccuracyFunction.getAccuracy(seasons, [],[],[],[],[],'','','','',125)[0]


categories = ["ML","Elo", 'AE25', 'AE50', 'AE73', 'AE100', 'AE125', "Rank"]
values = [m,e, e25, e50, e73, e100, e125, p]
colors = ['green','blue', 'lightblue', 'skyblue', 'steelblue','darkblue','navy', 'red']

plt.bar(categories, values, color=colors)

plt.ylabel('Total Accuracy Rate')
plt.title('ML, Elo, Adjusted Elo, and Rank Total Accuracy Rates')

plt.ylim(60, 80)

plt.savefig('accuracy/visualizations/presentation/totalWithAdjustedPresentation.png')

plt.show()


