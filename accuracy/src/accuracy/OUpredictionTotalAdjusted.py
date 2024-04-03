import accuracyFunction
import adjustedEloAccuracyFunction
import matplotlib.pyplot as plt
import csv

seasons = list(range(2007, 2024))

outList = [["method", "accuracy", "total", "over", "under"]]

e = accuracyFunction.getAccuracy("e", seasons, [], [], [], [], [], '','','','')
m = accuracyFunction.getAccuracy("m", seasons, [], [], [], [], [], '','','','')
p = accuracyFunction.getAccuracy("p", seasons, [], [], [], [], [], '','','','')

ae73 = adjustedEloAccuracyFunction.getAccuracy(seasons, [],[],[],[],[],'','','','', 73)
ae88 = adjustedEloAccuracyFunction.getAccuracy(seasons, [],[],[],[],[],'','','','',88)
ae43 = adjustedEloAccuracyFunction.getAccuracy(seasons, [],[],[],[],[],'','','','',43)

outList.append(["e"] + list(e))
outList.append(["m"] + list(m))
outList.append(["p"] + list(p))

eloOver = e[2]/e[1]
eloUnder = e[3]/e[1]
moneylineOver = m[2]/m[1]
moneylineUnder = m[3]/m[1]
pollUnder = p[2]/p[1]
pollOver = p[3]/p[1]

ae73Over = ae73[2]/ae73[1]
ae73Under = ae73[3]/ae73[1]
ae88Over = ae88[2]/ae88[1]
ae88Under = ae88[3]/ae88[1]
ae43Over = ae43[2]/ae43[1]
ae43Under = ae43[3]/ae43[1]


categories = ["Elo+","Elo-","ML+","ML-","Poll+","Poll-", "AE73+", 'AE73-', 'AE88+', 'AE88-', 'AE43+', 'AE43-']
values = [eloOver, eloUnder, moneylineOver,moneylineUnder,pollOver,pollUnder, ae73Over, ae73Under, ae88Over, ae88Under, ae43Over, ae43Under]
colors = ['blue','cyan','green','gold','red','magenta', 'navy','skyblue','royalblue','deepskyblue', 'midnightblue', 'steelblue']


plt.bar(categories, values, color=colors)

plt.ylabel('Percentage of Games')
plt.title('Elo, Adjusted Elo, ML, and Poll Over/Under (+/-) Predictions (2007 - 2024)')

plt.savefig('accuracy/visualizations/OUempTotalAdjusted.png')

plt.show()
