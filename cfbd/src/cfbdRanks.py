import csv
from datetime import datetime
import json


with open("team_dictionary/processed_data/SBROtoCFBD.json", "r") as file:
    teamDictionary = json.load(file)

dates = []
teams = []
ranks = []
points = []

with open("team_dictionary/processed_data/cfb_polls_standardized.csv", "r") as file:
    rawRanks = csv.DictReader(file)

    for rank in rawRanks:
        date = rank["Date"]
        if rank["Date"].find("Preseason") != -1:
            date = rank["Date"][:4] + "-06-01"
        elif rank["Date"].find("Final") != -1:
            year = int(rank["Date"][:4]) + 1
            date = str(year) + "-02-01"

        dates.append(datetime.strptime(date, "%Y-%m-%d"))
        try:
            teams.append(int(rank["StandardID"]))
        except:
            teams.append(0)
        try:
            ranks.append(int(float(rank["Rank"])))
        except:
            ranks.append("NaN")
        try:
            points.append(int(float(rank["Points"])))
        except:
            points.append("NaN")


def getProceeding(date):
    for i in range(len(dates)):
        if dates[i] >= date:
            return i
    return len(dates)

def getPrevious(date):
    proceeding = getProceeding(date)
    preceedingDate = dates[proceeding - 1]
    i = proceeding - 1
    while i >= 0 and dates[i] == preceedingDate:
        i = i - 1
    
    return (i + 1, proceeding)


with open("cfbd/processed_data/cfbdPre.csv", "r") as file:
    games = csv.DictReader(file)
    finalData = [games.fieldnames + ["homeRank", "homePoints", "awayRank", "awayPoints"]]
    for game in games:
        gameData = list(game.values()) + ["NaN", "NaN", "NaN", "NaN"]

        date = datetime.strptime(game["date"], "%Y-%m-%d")

        homeTeamID = int(game["homeID"])
        awayTeamID = int(game["awayID"])

        indices = getPrevious(date)

 
        for i in range(indices[0],indices[1]):
            if teams[i] == homeTeamID:
                gameData[-4] = ranks[i]
                gameData[-3] = points[i]
            elif teams[i] == awayTeamID:
                gameData[-2] = ranks[i]
                gameData[-1] = points[i]
   
        finalData.append(gameData)

    with open("cfbd/processed_data/cfbd.csv", 'w', newline='') as outFile:
        csv_writer = csv.writer(outFile)
        csv_writer.writerows(finalData)
        

