import accuracyFunction
import matplotlib.pyplot as plt
import numpy as np
import basketball_accuracy_function

top25 = list(range(1, 26))
seasons = list(range(2007, 2019))

football_e = accuracyFunction.getAccuracy("e", seasons, [],[], [], top25, top25,"","","","")[0]
football_m = accuracyFunction.getAccuracy("m", seasons, [],[], [], top25, top25, "","","","")[0]
football_p = accuracyFunction.getAccuracy("p", seasons, [],[], [], top25, top25, "","","","")[0]

basketball_m = basketball_accuracy_function.getAccuracy("m",seasons,top25, top25,'','')[0]
basketball_p = basketball_accuracy_function.getAccuracy("p", seasons, top25, top25, '','')[0]

sports = ("Football", "Basketball")
data = {
    'Betting Market': (football_m, basketball_m),
    'Poll Ranking': (football_p, basketball_p),
    'Elo Rating': (football_e, 0),
}

x = np.arange(len(sports)) 
width = 0.25  
multiplier = 0

fig, ax = plt.subplots(figsize=(20,10))

colors = {'Betting Market': 'green', 'Poll Ranking': 'red', 'Elo Rating': 'blue'}

for attribute, measurement in data.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute, color=colors[attribute])
    multiplier += 1

ax.set_ylabel('Percentage of Correct Predictions', fontsize=33)

red_bar_center_football = x[0] + width
red_bar_center_basketball = x[1] + width

ax.set_xticks([red_bar_center_football, red_bar_center_basketball]) 
ax.set_xticklabels(sports, fontsize=40)
ax.legend(loc='upper left', ncol=3, fontsize=33)
ax.set_ylim(50, 75)
ax.tick_params(axis='x', which='major', labelsize=55, pad=15)
ax.tick_params(axis='y', which='major', labelsize=30, pad=15)


plt.savefig("accuracy/visualizations/presentation/emp25TotalPresentation.png")
plt.show()
