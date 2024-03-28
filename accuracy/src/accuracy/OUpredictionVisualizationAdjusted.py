import accuracyFunction
import adjustedEloAccuracyFunction
import matplotlib.pyplot as plt

seasons = []
eloOver = []
moneylineOver = []
pollOver = []
eloUnder = []
moneylineUnder = []
pollUnder = []

ae43Over = []
ae43Under = []
ae73Over = []
ae73Under = []
ae88Over = []
ae88Under = []

top25 = list(range(1,26))

for season in range(2007, 2024):
    seasons.append(season)

    elo_rate = accuracyFunction.getAccuracy("e", [season], [],[], [], top25, top25, '','','','')
    moneyline_rate = accuracyFunction.getAccuracy("m", [season],[], [], [], top25, top25, '','','','')
    poll_rate = accuracyFunction.getAccuracy("p", [season],[], [], [], top25, top25, '','','','')

    ae43 = adjustedEloAccuracyFunction.getAccuracy([season],[],[],[],[],[],'','','','',43)
    ae73 = adjustedEloAccuracyFunction.getAccuracy([season],[],[],[],[],[],'','','','',73)
    ae88 = adjustedEloAccuracyFunction.getAccuracy([season],[],[],[],[],[],'','','','',88)

    if elo_rate == (0, 0,0,0):
        eloOver.append(None)
        eloUnder.append(None)
    else:
        eloOver.append(float(elo_rate[2])/float(elo_rate[1]))
        eloUnder.append(float(elo_rate[3])/float(elo_rate[1]))

    if moneyline_rate == (0, 0,0,0):
        moneylineOver.append(None)
        moneylineUnder.append(None)
    else:
        moneylineOver.append(float(moneyline_rate[2])/float(moneyline_rate[1]))
        moneylineUnder.append(float(moneyline_rate[3])/float(moneyline_rate[1]))

    if poll_rate == (0, 0,0,0):
        pollOver.append(None)
        pollUnder.append(None)
    else:
        pollOver.append(float(poll_rate[2])/float(poll_rate[1]))
        pollUnder.append(float(poll_rate[3])/float(poll_rate[1]))


    if ae43 == (0, 0,0,0):
        ae43Over.append(None)
        ae43Under.append(None)
    else:
        ae43Over.append(float(ae43[2])/float(ae43[1]))
        ae43Under.append(float(ae43[3])/float(ae43[1]))

    if ae73 == (0, 0,0,0):
        ae73Over.append(None)
        ae73Under.append(None)
    else:
        ae73Over.append(float(ae73[2])/float(ae73[1]))
        ae73Under.append(float(ae73[3])/float(ae73[1]))

    if ae88 == (0, 0,0,0):
        ae88Over.append(None)
        ae88Under.append(None)
    else:
        ae88Over.append(float(ae88[2])/float(ae88[1]))
        ae88Under.append(float(ae88[3])/float(ae88[1]))



plt.plot(seasons, eloOver, color="blue", label = "Elo+")
plt.plot(seasons, moneylineOver, color="green", label = "ML+")
plt.plot(seasons, pollOver, color="red", label = "Poll+")

plt.plot(seasons, eloUnder, color="cyan", label = "Elo-")
plt.plot(seasons, moneylineUnder, color="gold", label = "ML-")
plt.plot(seasons, pollUnder, color="magenta", label = "Poll-")

plt.plot(seasons, ae43Over, color = 'navy', label = 'AE43+')
plt.plot(seasons, ae43Under, color = 'steelblue', label = 'AE43-')
plt.plot(seasons, ae73Over, color = 'darkblue', label = 'AE73+')
plt.plot(seasons, ae73Under, color = 'skyblue', label = 'AE73-')
plt.plot(seasons, ae88Over, color = 'midnightblue', label = 'AE88+')
plt.plot(seasons, ae88Under, color = 'cornflowerblue', label = 'AE88-')


plt.xlabel('Season')
plt.ylabel('Percentage of Games')
plt.title('Elo, Adjusted Elo, ML, and Poll Over/Under (+/-) Predictions Top 25 Teams (2007 - 2024)')
plt.grid(True)
plt.legend()

plt.savefig('accuracy/visualizations/OUemp25Adjusted.png')
plt.show()