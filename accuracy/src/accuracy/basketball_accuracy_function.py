import csv

def checkContain(data, set):
    if len(set) != 0:
        return data in set
    
    return True

def checkMoneylineDiff(min, max, home, away):
    if min == "" and max == "":
        return True
    if min == "":
        if home == "NaN" and away == "NaN":
            return False
        if home == "NaN":
            return abs(float(away)*2) < float(max)
        if away == "NaN":
            return abs(float(home)*2) < float(max)
        return abs(float(home)-float(away)) < float(max)
    if max == "":
        if home == "NaN" and away == "NaN":
            return False
        if home == "NaN":
            return abs(float(away)*2) >= float(min)
        if away == "NaN":
            return abs(float(home)*2) >= float(min)
        return abs(float(home)-float(away)) >= float(min)
    else:
        if home == "NaN" and away == "NaN":
            return False
        if home == "NaN":
            diff = abs(float(away)*2)
            return diff >= float(min) and diff < float(max)
        if away == "NaN":
            diff = abs(float(home)*2)
            return diff >= float(min) and diff < float(max)
        diff = abs(float(home)-float(away))
        return diff >= float(min) and diff < float(max)
    

def checkNull(method, ml1, ml2, rank1, rank2):
    if method == "m":
        return ml1 != "NaN" or ml1 != "NaN"
    return rank1 != "NaN" and rank2 != "NaN"



def performChecks(season, seasons, 
                   rank1, ranks1, rank2, ranks2, 
                   minMoneylineDiff, maxMoneylineDiff, ml1, ml2, method):
    global a,b,c
    contain = all(checkContain(item, items) for item, items in [(season, seasons), (rank1, ranks1), (rank2, ranks2), ])
    moneylineDiff = checkMoneylineDiff(minMoneylineDiff, maxMoneylineDiff, ml1, ml2)
    notNull = checkNull(method, ml1, ml2, rank1, rank2)

    return contain and moneylineDiff and notNull


def getPrediction(method, ml1, ml2, rank1, rank2):
    if method == "m":
        if ml1 == "NaN":
            return float(ml2) > 0
        return float(ml1) < 0
    elif method == "p":
        return float(rank1) < float(rank2)


def getAccuracy(method,seasons, ranks1, ranks2, minMoneylineDiff, maxMoneylineDiff):
    with open("combined/processed/combinedBClean.csv", "r") as file:
        games = csv.DictReader(file)

        predicted = 0
        total = 0
        totalOver = 0
        totalUnder = 0

        for game in games:
            season = int(game["season"])

            location = game["regular"]
            if location == "N":
                continue

            rank1 = "NaN"
            try:
                rank1 = int(float(game["rank1"]))
            except:
                pass
            rank2 = "NaN"
            try:
                rank2 = int(float(game["rank2"]))
            except:
                pass
            ml1 = "NaN"
            try:
                ml1 = int(game["moneyline1"])
            except:
                pass
            ml2 = "NaN"
            try:
                ml2 = int(game["moneyline2"])
            except:
                pass


            if performChecks(season, seasons, 
                             rank1, ranks1, rank2, ranks2, 
                             minMoneylineDiff, maxMoneylineDiff, ml1, ml2, 
                             method):
                total = total + 1

                prediction = getPrediction(method, ml1, ml2, rank1, rank2)
                result = int(game["result"])
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


getAccuracy("m",[],list(range(1,26)),list(range(1,26)),"","")