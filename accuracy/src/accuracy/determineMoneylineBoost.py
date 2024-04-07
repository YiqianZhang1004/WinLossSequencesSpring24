import adjustedMoneylineAccuracyFunction

def acc(boost):
    seasons = list(range(2007, 2024))
    m = float(adjustedMoneylineAccuracyFunction.getAccuracy(seasons, [], [], [], [], [],"","","","", boost)[0])
    return m

def overUnderPredictions(boost):
    seasons = list(range(2007, 2024))
    m = adjustedMoneylineAccuracyFunction.getAccuracy(seasons, [],[],[],[],[],'','','','', boost)
    overPercentage = float(m[2])/float(m[1])
    underPercentage = float(m[3])/float(m[1])

    return abs(overPercentage - underPercentage)


accBoost = 300
accuracy = acc(300)
ouBoost = 300
oup = overUnderPredictions(300)

for boost in range(-300, 300):
    a = acc(boost)
    if a > accuracy:
        accuracy = a
        accBoost = boost
    ou = overUnderPredictions(boost)
    if ou < oup:
        oup = ou
        ouBoost = boost

print(accBoost)
print(ouBoost)