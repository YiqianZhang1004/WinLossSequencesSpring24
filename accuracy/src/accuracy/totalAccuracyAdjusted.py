import accuracyFunction
import adjustedEloAccuracyFunction
import adjustedMoneylineAccuracyFunction
import matplotlib.pyplot as plt

seasons = list(range(2007, 2024))

e = accuracyFunction.getAccuracy("e", seasons, [],[], [], [], [], '','','','')[0]
m = accuracyFunction.getAccuracy("m", seasons, [],[], [], [], [], '','','','')[0]
p = accuracyFunction.getAccuracy("p", seasons, [],[], [], [], [], '','','','')[0]


e43 = adjustedEloAccuracyFunction.getAccuracy(seasons, [],[],[],[],[],'','','','',43)[0]
e73 = adjustedEloAccuracyFunction.getAccuracy(seasons, [],[],[],[],[],'','','','',73)[0]
e88 = adjustedEloAccuracyFunction.getAccuracy(seasons, [],[],[],[],[],'','','','',88)[0]

m125 = adjustedMoneylineAccuracyFunction.getAccuracy(seasons, [],[],[],[],[],'','','','',-125)[0]
m140 = adjustedMoneylineAccuracyFunction.getAccuracy(seasons, [],[],[],[],[],'','','','',-140)[0]


categories = ["ML", 'ML-125', 'ML-140',"Elo", "AE43", "AE73", "AE88", "Rank"]
values = [m,m125, m140, e, e43, e73, e88, p]
colors = ['green', 'lightgreen', 'seagreen', 'blue', "steelblue", 'royalblue', 'cornflowerblue','red']

plt.bar(categories, values, color=colors)

plt.ylabel('Total Accuracy Rate')
plt.title('ML, Adjusted ML, Elo, Adjusted Elo, and Rank Total Accuracy Rates')

plt.ylim(60, 80)

plt.savefig('accuracy/visualizations/totalWithAdjusted.png')

plt.show()


