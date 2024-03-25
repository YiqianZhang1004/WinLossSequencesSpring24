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
    
def checkEloDiff(min, max, home, away):
    if min == "" and max == "":
        return True
    if min == "":
        if home == "NaN" or away == "NaN":
            return False
        return abs(float(home)-float(away)) < float(max)
    if max == "":
        if home == "NaN" or away == "NaN":
            return False
        return abs(float(home)-float(away)) >= float(min)
    else:
        if home == "NaN" or away == "NaN":
            return False
        diff = abs(float(home)-float(away))
        return diff >= float(min) and diff < float(max)


def checkNull(method, stat1, stat2):
    if method == "m":
        return stat1 != "NaN" or stat2 != "NaN"
    return stat1 != "NaN" and stat2 != "NaN"

def performChecks(season, seasons, week, weeks,
                   homeTeam, homeTeams, awayTeam, awayTeams, 
                   homeRank, homeRanks, awayRank, awayRanks, 
                   minMoneylineDiff, maxMoneylineDiff, homeMoneyline, awayMoneyline, 
                   minEloDiff, maxEloDiff, homeElo, awayElo, method, stat1, stat2):
    contain = all(checkContain(item, items) for item, items in [(season, seasons), (week, weeks), (homeTeam, homeTeams), (awayTeam, awayTeams), (homeRank, homeRanks), (awayRank, awayRanks), ])
    moneylineDiff = checkMoneylineDiff(minMoneylineDiff, maxMoneylineDiff, homeMoneyline, awayMoneyline)
    eloDiff = checkEloDiff(minEloDiff, maxEloDiff, homeElo, awayElo)
    notNull = checkNull(method, stat1, stat2)

    return contain and moneylineDiff and eloDiff and notNull


def getPrediction(method, stat1, stat2):
    if method == "e":
        return float(stat1) > float(stat2)
    elif method == "m":
        if stat1 == "NaN":
            return float(stat2) > 0
        return float(stat1) < 0
    elif method == "p":
        return float(stat1) < float(stat2)


def getAccuracy(method,seasons,weeks, homeTeams, awayTeams, homeRanks, awayRanks, minMoneylineDiff, maxMoneylineDiff, minEloDiff, maxEloDiff):
    with open("combined/processed/combinedF.csv", "r") as file:
        games = csv.DictReader(file)

        predicted = 0
        total = 0
        totalOver = 0
        totalUnder = 0


        for game in games:
            season = int(game["season"])
            week = int(game["week"])
            homeTeam = int(game["homeID"])
            awayTeam = int(game["awayID"])
            homeRank = "NaN"
            try:
                homeRank = int(game["homeRank"])
            except:
                pass
            awayRank = "NaN"
            try:
                awayRank = int(game["awayRank"])
            except:
                pass
            homeMoneyline = game["homeMoneyline"]
            awayMoneyline = game["awayMoneyline"]
            homeElo = game["homePreElo"]
            awayElo = game["awayPreElo"]

            stat1 = homeElo
            stat2 = awayElo
            if method == "m":
                stat1 = homeMoneyline
                stat2 = awayMoneyline
            elif method == "p":
                stat1 = homeRank
                stat2 = awayRank

            if performChecks(season, seasons, week, weeks, 
                             homeTeam, homeTeams, awayTeam, awayTeams, 
                             homeRank, homeRanks, awayRank, awayRanks, 
                             minMoneylineDiff, maxMoneylineDiff, homeMoneyline, awayMoneyline, 
                             minEloDiff, maxEloDiff, homeElo, awayElo, method, stat1, stat2):
                total = total + 1

                prediction = getPrediction(method, stat1, stat2)
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


getAccuracy("p",[],[],[],[],[],[],"","","","")
