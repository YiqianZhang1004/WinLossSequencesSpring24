import adjustedEloAccuracyFunction
import accuracyFunction
import matplotlib.pyplot as plt

seasons = []
elo_accuracy = []
moneyline_accuracy = []
adjusted_elo_accuracy = []
closest_accuracy = []
evenest_accuracy = []


for season in range(2007, 2024):
    seasons.append(season)

    adjusted_elo_rate = adjustedEloAccuracyFunction.getAccuracy([season], [], [], [], [], [],"","","","",73)
    closest_rate = adjustedEloAccuracyFunction.getAccuracy([season], [], [], [], [], [],"","","","",88)
    evenest_rate = adjustedEloAccuracyFunction.getAccuracy([season], [],[],[],[],[], '','','','',43)
    elo_rate = accuracyFunction.getAccuracy("e", [season], [], [], [], [], [], "","","","")
    moneyline_rate = accuracyFunction.getAccuracy("m", [season], [], [], [], [], [], "","","","")


    if elo_rate == (0, 0, 0, 0):
        elo_accuracy.append(None)
    else:
        elo_accuracy.append(float(elo_rate[0]))

    if moneyline_rate == (0, 0, 0, 0):
        moneyline_accuracy.append(None)
    else:
        moneyline_accuracy.append(float(moneyline_rate[0]))

    if adjusted_elo_rate == (0,0,0,0):
        adjusted_elo_accuracy.append(None)
    else:
        adjusted_elo_accuracy.append(float(adjusted_elo_rate[0]))

    if closest_rate == (0,0,0,0):
        closest_accuracy.append(None)
    else:
        closest_accuracy.append(float(closest_rate[0]))

    if evenest_rate == (0,0,0,0):
        evenest_accuracy.append(None)
    else:
        evenest_accuracy.append(float(evenest_rate[0]))
    
        

plt.plot(seasons, elo_accuracy, color="blue", label = "Elo")
plt.plot(seasons, moneyline_accuracy, color="green", label = "Moneyline")
plt.plot(seasons, adjusted_elo_accuracy, color = "black", label = "Highest Avg (+73)")
plt.plot(seasons, closest_accuracy, color = "purple", label = "Closest to ML (+88)")
plt.plot(seasons, evenest_accuracy, color = 'darkorange', label = "Evenest (+43)")



plt.xlabel('Season')
plt.ylabel('Accuracy')
plt.title('Elo, Adjusted Elo, and Moneyline Accuracy of All Teams (2007 - 2024)')
plt.legend()
plt.grid(True)

plt.savefig('accuracy/visualizations/emAdjustedFull.png')
plt.show()
