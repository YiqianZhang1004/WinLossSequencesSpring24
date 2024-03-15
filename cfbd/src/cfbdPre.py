import csv

finalData = [["gameID", "date", "season", "week", "homeTeam", "homeID", "awayTeam", "awayID", 
               "homeScore", "awayScore","result", "homePostWinProb", "awayPostWinProb","homePreElo",
               "homePostElo","awayPreElo","awayPostElo", "overUnder", "spread", "openingOverUnder", 
               "openingSpread", "homeMoneyline", "awayMoneyline"]]

errors = [["gameID", "date", "season", "week", "homeTeam" ,"homeID", "awayTeam", "awayID"]]

seasons = []
for i in range(1980, 2024):
    seasons.append(i)

def floatData(data):
    try:
        return round(float(data),3)
    except:
        return "NaN" 

def getAverage(rawBetting): 
    averages = ["NaN", "NaN", "NaN", "NaN", "NaN", "NaN"]
    for i in range(len(rawBetting)):
        total = 0.0
        num = 0
        for j in range(len(rawBetting[i])):
            if rawBetting[i][j] != "NaN":
                total = total + rawBetting[i][j]
                num = num + 1
        if num != 0:
            averages[i] = round(float(total/num), 3)
    return averages

    

for season in seasons:

    with open("cfbd/raw_data/games/" + str(season)+"_games.csv", 'r') as gamesFile:
        games = csv.DictReader(gamesFile)
            
        for game in games:
            try:
                gameID = int(game['\ufeff"Id"'])
                date = str(game["Start Date"])[0:10]
                week = int(game["Week"])
                homeTeam = str(game["Home Team"])
                homeID = int(game["Home Id"])
                awayTeam = str(game["Away Team"])
                awayID = int(game["Away Id"])
                homeScore = int(float(game["Home Points"]))
                awayScore = int(float(game["Away Points"]))

                result = 0
                if homeScore >= awayScore:
                    result = 1

                homePostWinProb = floatData(game["Home Post Win Prob"])
                awayPostWinProb = floatData(game["Away Post Win Prob"])
                homePregameElo = floatData(game["Home Pregame Elo"])
                homePostgameElo = floatData(game["Home Postgame Elo"])
                awayPregameElo = floatData(game["Away Pregame Elo"])
                awayPostgameElo = floatData(game["Away Postgame Elo"])

                rawBetting = [[],[],[],[],[],[]]

                
                if season>=2013:
                    with open("cfbd/raw_data/lines/"+str(season)+"_lines.csv","r") as bets_file:
                        bets = csv.DictReader(bets_file)

                        foundFirst = False
                        foundAll = False
                        incrementor = 0

                        for bet in bets:
                            if int(bet['\ufeff"Id"']) == int(game['\ufeff"Id"']):
                                rawBetting[0].append(floatData(bet["OverUnder"]))
                                rawBetting[1].append(floatData(bet["Spread"]))
                                rawBetting[2].append(floatData(bet["OpeningOverUnder"]))
                                rawBetting[3].append(floatData(bet["OpeningSpread"]))
                                rawBetting[4].append(floatData(bet["HomeMoneyline"]))
                                rawBetting[5].append(floatData(bet["AwayMoneyline"]))
                
                
                averageBets = getAverage(rawBetting)
                overUnder = averageBets[0]
                spread = averageBets[1]
                openingOverUnder = averageBets[2]
                openingSpread = averageBets[3]
                homeMoneyline = averageBets[4]
                awayMoneyline = averageBets[5]

                game_data = [gameID, date, season, week, 
                            homeTeam, homeID, awayTeam, awayID,
                            homeScore, awayScore, result,
                            homePostWinProb, awayPostWinProb,
                            homePregameElo, homePostgameElo,
                            awayPregameElo, awayPostgameElo,
                            overUnder, spread, 
                            openingOverUnder, openingSpread,
                            homeMoneyline, awayMoneyline]
                
                finalData.append(game_data)

            except:
                errorGame = [game['\ufeff"Id"'], game["Start Date"], 
                            game["Season"], game["Week"], 
                            game["Home Team"], game["Home Id"],
                            game["Away Team"], game["Away Id"]]
                
                errors.append(errorGame)
    
with open("cfbd/processed_data/cfbdPre.csv", 'w', newline='') as processed:
    csv_writer = csv.writer(processed)
    csv_writer.writerows(finalData)

with open("cfbd/processed_data/cfbdMissing.csv", "w", newline='') as errorFile:
    csv_writer = csv.writer(errorFile)
    csv_writer.writerows(errors)

