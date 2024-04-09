import csv

def checkContain(data, set):
    if len(set) != 0:
        return data in set
    return True

def getMin(data1, data2):
    if data1 <= data2:
        return data1
    return data2

def checkMoneyline(min, max, home, away):
    if min == "" and max == "":
        return True
    if min == "":
        if home == "NaN" and away == "NaN":
            return False
        if home == "NaN":
            return abs(float(away)) < max
        if away == "NaN":
            return abs(float(home)) < max
        else:
            return getMin(abs(float(home)), abs(float(away))) < max
    if max == "":
        if home == "NaN" and away == "NaN":
            return False
        if home == "NaN":
            return abs(float(away)) >= min
        if away == "NaN":
            return abs(float(home)) >= min
        else:
            return getMin(abs(float(home)), abs(float(away))) >= min
    else:
        if home == "NaN" and away == "NaN":
            return False
        if home == "NaN":
            return abs(float(away)) >= min and abs(float(away)) < max
        if away == "NaN":
            return abs(float(home)) >= min and abs(float(home)) < max
        else:
            return getMin(abs(float(home)), abs(float(away))) >= min and getMin(abs(float(home)), abs(float(away))) < max
    

def checkNull(home, away):
    return home != "NaN" or away != "NaN"

def performChecks(season, seasons,
                   minMoneyline, maxMoneyline, homeMoneyline, awayMoneyline):
    contain = checkContain(season, seasons)
    moneyline = checkMoneyline(minMoneyline, maxMoneyline, homeMoneyline, awayMoneyline)
    notNull = checkNull(homeMoneyline, awayMoneyline)

    return contain and moneyline and notNull


def getPrediction(homeMoneyline, awayMoneyline):
    if homeMoneyline == "NaN":
        return float(awayMoneyline) > 0
    return float(homeMoneyline) < 0
    


def getAccuracy(seasons, minMoneyline, maxMoneyline):
    with open("combined/processed/combinedF.csv", "r") as file:
        games = csv.DictReader(file)

        predicted = 0
        total = 0
        totalOver = 0
        totalUnder = 0

        for game in games:
            season = int(game["season"])
    
            homeMoneyline = game["homeMoneyline"]
            awayMoneyline = game["awayMoneyline"]
 

            if performChecks(season, seasons, 
                             minMoneyline, maxMoneyline, homeMoneyline, awayMoneyline):
                total = total + 1

                prediction = getPrediction(homeMoneyline, awayMoneyline)
                result = float(game["result"])
                if (prediction and result == 1) or (not prediction and result == 0):
                    predicted = predicted + 1            

                else:
                    if prediction:
                        totalOver = totalOver + 1
                    else:
                        totalUnder = totalUnder + 1
        if total == 0:
            print("no games")
            return (0,0, 0, 0)
        else:
            accuracy = round(100* predicted / total, 4)
            print((accuracy, total, totalOver, totalUnder))
            return (accuracy, total, totalOver, totalUnder)


getAccuracy([],"","")
