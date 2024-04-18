import accuracyFunction
import matplotlib.pyplot as plt
import numpy as np
import basketball_accuracy_function

top25 = list(range(1, 26))

football_e = accuracyFunction.getAccuracy("e", [], [],[], [], top25, top25,"","","","")[0]
football_m = accuracyFunction.getAccuracy("m", [], [],[], [], top25, top25, "","","","")[0]
football_p = accuracyFunction.getAccuracy("p", [], [],[], [], top25, top25, "","","","")[0]

basketball_m = basketball_accuracy_function.getAccuracy("m",[],top25, top25,'','')[0]
basketball_p = basketball_accuracy_function.getAccuracy("p", [], top25, top25, '','')[0]

sports = ("Football", "Basketball")
data = {
    'Betting Market': (football_m, basketball_m),
    'Poll Ranking': (football_p, basketball_p),
    'Elo Rating': (football_e, 0),
}

x = np.arange(len(sports)) 
width = 0.25  
multiplier = 0

fig, ax = plt.subplots()

colors = {'Betting Market': 'green', 'Poll Ranking': 'red', 'Elo Rating': 'blue'}

for attribute, measurement in data.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute, color=colors[attribute])
    multiplier += 1

ax.set_ylabel('Percentage of Correct Predictions')

red_bar_center_football = x[0] + width
red_bar_center_basketball = x[1] + width

ax.set_xticks([red_bar_center_football, red_bar_center_basketball]) 
ax.set_xticklabels(sports)
ax.legend(loc='upper left', ncol=3)
ax.set_ylim(50, 75)

ax.tick_params(axis='x', which='major', pad=15)


plt.savefig("accuracy/visualizations/presentation/emp25TotalPresentation.png")
plt.show()
