import adjustedEloAccuracyFunction
import accuracyFunction

def getDiff(boost):
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


min = getDiff(500)
minBoost = 500

for i in range(0, 500):
    diff = getDiff(i)
    if diff < min:
        min = diff
        minBoost = i


def getAverage(boost):
    adjusted_elo_accuracy = []
    for season in range(2007, 2024):
        e = float(adjustedEloAccuracyFunction.getAccuracy([season], [], [], [], [], [],"","","","", boost)[0])
        adjusted_elo_accuracy.append(e)

    return sum(adjusted_elo_accuracy)/len(adjusted_elo_accuracy)

max = 0
maxBoost = 0

for i in range(0, 500):
    avg = getAverage(i)
    if avg > max:
        max = avg
        maxBoost = i


print(minBoost)
print(maxBoost)


