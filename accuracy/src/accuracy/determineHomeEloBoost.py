import adjustedEloAccuracyFunction
import accuracyFunction

def diff(boost):
    moneyline_accuracy = []
    adjusted_elo_accuracy = []
    for season in range(2007, 2024):
        e = float(adjustedEloAccuracyFunction.getAccuracy([season], [], [], [], [], [],"","","","", boost)[0])
        m = float(accuracyFunction.getAccuracy("m", [season], [], [], [], [], [], "","","","")[0])

        moneyline_accuracy.append(m)
        adjusted_elo_accuracy.append(e)

    totalDiff = 0

    for i in range(len(moneyline_accuracy)):
        mm = moneyline_accuracy[i]
        ee = adjusted_elo_accuracy[i]

        if mm != 0 and ee != 0:
            diff = mm - ee
            diff = diff * diff
            totalDiff = totalDiff + diff
    
    return totalDiff

def acc(boost):
    seasons = list(range(2007, 2024))
    e = float(adjustedEloAccuracyFunction.getAccuracy(seasons, [], [], [], [], [],"","","","", boost)[0])
    return e

def overUnderPredictions(boost):
    seasons = list(range(2007, 2024))
    e = adjustedEloAccuracyFunction.getAccuracy(seasons, [],[],[],[],[],'','','','', boost)
    overPercentage = float(e[2])/float(e[1])
    underPercentage = float(e[3])/float(e[1])

    return abs(overPercentage - underPercentage)

diffBoost = 100
difference = diff(100)
accBoost = 100
accuracy = acc(100)
ouBoost = 100
oup = overUnderPredictions(100)

for boost in range(1, 100):
    d = diff(boost)
    if d < difference:
        difference = d
        diffBoost = boost
    a = acc(boost)
    if a > accuracy:
        accuracy = a
        accBoost = boost
    ou = overUnderPredictions(boost)
    if ou < oup:
        oup = ou
        ouBoost = boost

print(diffBoost)
print(accBoost)
print(ouBoost)

