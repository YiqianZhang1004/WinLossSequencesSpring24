import accuracyFunction
import adjustedEloAccuracyFunction
import adjustedMoneylineAccuracyFunction
import matplotlib.pyplot as plt

seasons = list(range(2007, 2024))

e = accuracyFunction.getAccuracy("e", seasons, [], [], [], [], [], '','','','')
m = accuracyFunction.getAccuracy("m", seasons, [], [], [], [], [], '','','','')
p = accuracyFunction.getAccuracy("p", seasons, [], [], [], [], [], '','','','')

ae73 = adjustedEloAccuracyFunction.getAccuracy(seasons, [],[],[],[],[],'','','','', 73)
ae88 = adjustedEloAccuracyFunction.getAccuracy(seasons, [],[],[],[],[],'','','','',88)
ae43 = adjustedEloAccuracyFunction.getAccuracy(seasons, [],[],[],[],[],'','','','',43)

am125 = adjustedMoneylineAccuracyFunction.getAccuracy(seasons, [],[],[],[],[],'','','','',-125)
am140 = adjustedMoneylineAccuracyFunction.getAccuracy(seasons, [],[],[],[],[],'','','','',-140)

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

am125Over = am125[2]/am125[1]
am125Under = am125[3]/am125[1]
am140Over = am140[2]/am140[1]
am140Under = am140[3]/am140[1]

categories = ["E+","E-","M+","M-","P+","P-", "E73+", 'E73-', 'E88+', 'E88-', 'E43+', 'E43-', "M125+",'M125-','M140+', 'M140-']
values = [eloOver, eloUnder, moneylineOver,moneylineUnder,pollOver,pollUnder, ae73Over, ae73Under, ae88Over, ae88Under, ae43Over, ae43Under, am125Over, am125Under, am140Over, am140Under]
colors = ['blue','cyan','green','gold','red','magenta', 'navy','skyblue','royalblue','deepskyblue', 'midnightblue', 'steelblue', 'forestgreen','lightgreen','darkgreen','seagreen']

plt.xticks(rotation=45)
plt.bar(categories, values, color=colors)

plt.ylabel('Percentage of Games')
plt.title('Elo, Adjusted Elo, ML, Adjusted ML, and Poll Over/Under (+/-) Predictions')

plt.savefig('accuracy/visualizations/OUempTotalAdjusted.png')

plt.show()
