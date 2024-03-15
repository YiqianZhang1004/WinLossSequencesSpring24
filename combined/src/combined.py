import csv
import json


with open("team_dictionary/processed_data/SBROtoCFBD.json", "r") as file:
    SBROtoCBFD = json.load(file)


def getMatch(date, home, away):
    with open("sportsbookreviewsonline/ncaaf/processsed_data/sbro.csv", "r") as file:
        sbro = csv.DictReader(file)
        for game in sbro:
            if game["date"] == date and int(SBROtoCBFD[game["homeTeam"]]) == home and int(SBROtoCBFD[game["awayTeam"]]) == away:
                return game
    return "NaN"


def getAverage(data1, data2):
    if data1 == "NaN":
        return data2
    if data2 == "NaN":
        return data1
    return (float(data1) + float(data2))/2

with open("cfbd/processed_data/cfbd.csv", "r") as cfbd:
    games = csv.DictReader(cfbd)
    finalData = [games.fieldnames]
    count = 0
    for game in games:
        count = count + 1
        date = game["date"]
        homeID = int(game["homeID"])
        awayID = int(game["awayID"])

        match = getMatch(date, homeID, awayID)

        if match!="NaN":
            
            game["openingOverUnder"] = getAverage(game["openingOverUnder"], match["openingOverUnder"])
            game["overUnder"] = getAverage(game["overUnder"], match["closingOverUnder"])
            game["openingSpread"] = getAverage(game["openingSpread"], match["openingSpread"])
            game["spread"] = getAverage(game["spread"], match["closingSpread"])
            game["homeMoneyline"] = getAverage(game["homeMoneyline"], match["homeMoneyline"])
            game["awayMoneyline"] = getAverage(game["awayMoneyline"], match["awayMoneyline"])

            gameData = list(game.values())
            finalData.append(gameData)

        else:
            finalData.append(list(game.values()))

    with open("combined/processed/combinedF.csv", 'w', newline='') as processed:
        csv_writer = csv.writer(processed)
        csv_writer.writerows(finalData)



