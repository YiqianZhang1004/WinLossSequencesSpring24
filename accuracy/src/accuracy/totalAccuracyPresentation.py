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

categories = ["Betting Market", "Poll Ranking", "Elo Rating", 'Adjusted Elo Rating (+25)', 'Adjusted Elo Rating (+50)', 'Adjusted Elo Rating (+73)', 'Adjusted Elo Rating (+100)', 'Adjusted Elo Rating (+125)']
values = [m, p,e, e25, e50, e73, e100, e125]
colors = ['green', 'red', 'blue', 'lightblue', 'skyblue', 'steelblue','darkblue','navy']

plt.bar(categories, values, color=colors)

plt.ylabel('Total Accuracy Rate (%)')

plt.ylim(60, 80)

plt.xticks(rotation=45)

plt.savefig('accuracy/visualizations/presentation/totalWithAdjustedPresentation.png')

plt.show()
