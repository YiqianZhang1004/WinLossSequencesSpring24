import csv

final_data = [["gameID", "date", "season", "regular", "team1", "team1ID", "team2", "team2ID", 
               "score1", "score2","result", "homePostWinProb", "awayPostWinProb","homePreElo",
               "homePostElo","awayPreElo","awayPostElo", "overUnder", "spread", "openingOverUnder", 
               "openingSpread", "homeMoneyLine", "awayMoneyLine", "homeFirstPlaceVotes", "homePollPoints",
               "awayFirstPlaceVotes","awayPollPoints"]]

seasons = []
for i in range(1980, 2024):
    seasons.append(i)


def find_averages(raw_betting):
    averages=["NaN","NaN","NaN","NaN","NaN","NaN"]
    for i in range(len(raw_betting)):
        if len(raw_betting[i])!=0:
            averages[i] = round(float(sum(raw_betting[i])/len(raw_betting[i])),3)
    return averages


for season in seasons:
    with open("","r") as file:
        bets = csv.reader(file)
    with open("", "r") as file:
        polls = csv.reader(file)
    with open("", 'r') as file:
        
        games = csv.reader(file)
        lastIndex=0
        i = 0
        while i < len(games):
            
            try:
                game_data = []

                # gameID
                game_data.append(int(games[i][0]))

                # date
                game_data.append(str(games[i][4])[0:10])
                
                # season
                game_data.append(int(games[i][1]))

                # regular season or not
                game_data.append(str(games[i][3])=="regular")

                # home team name
                game_data.append(str(games[i][13]).lower())

                # home team ID
                game_data.append(int(games[i][12]))

                # away team name
                game_data.append(str(games[i][26]).lower())

                # away team ID
                game_data.append(int(games[i][25]))

                # home team score
                game_data.append(int(games[i][16]))

                # away team score
                game_data.append(int(games[i][29]))

                # determining winner
                if int(games[i][16]) > int(games[i][29]):
                    game_data.append(1)
                elif int(games[i][16]) == int(games[i][29]):
                    game_data.append(0.5)
                else:
                    game_data.append(0)

                # home post win prob
                try:
                    game_data.append(round(float(games[i][22]),3))
                except:
                    game_data.append("NaN")

                #away post win prob
                try:
                    game_data.append(round(float(games[i][35]),3))
                except:
                    game_data.append("NaN")

                # home pre game elo
                try:
                    game_data.append(int(games[i][23]))
                except:
                    game_data.append("NaN")

                # home post game elo
                try:
                    game_data.append(int(games[i][24]))
                except:
                    game_data.append("NaN")

                # away pre game elo
                try:
                    game_data.append(int[games[i][36]])
                except:
                    game_data.append("NaN")

                # away post game elo
                try:
                    game_data.append(int(games[i][37]))
                except:
                    game_data.append("NaN")


                raw_betting = [[],[],[],[],[],[]]
                foundFirst=False
                foundAll = False
                incrementer = 1
                while lastIndex + incrementer < len(bets) and not foundAll:
                    if bets[lastIndex][0] == games[i][0]:
                        foundFirst=True
                        try:
                            raw_betting[0].append(round(float(bets[lastIndex][6]),3))
                        except:
                            pass
                        try:
                            raw_betting[1].append(round(float(bets[lastIndex][7]),3))
                        except:
                            pass
                        try:
                            raw_betting[2].append(round(float(bets[lastIndex][10]),3))
                        except:
                            pass
                        try:
                            raw_betting[3].append(round(float(bets[lastIndex][9]),3))
                        except:
                            pass
                        try:
                            raw_betting[4].append(round(float(bets[lastIndex][11]),3))
                        except:
                            pass
                        try:
                            raw_betting[5].append(round(float(bets[lastIndex][12]),3))
                        except:
                            pass
                    elif foundFirst:
                        foundAll = True
                    incrementer=incrementer+1
                if foundFirst:
                    lastIndex=lastIndex+incrementer
                average_bets = find_averages(raw_betting)

                for average_bet in average_bets:
                    game_data.append(average_bet)
                

                poll_data = ["NaN","NaN","NaN","NaN"]
                for poll in polls:
                    valid1 = True
                    valid2 = True
                    if (int(poll[2]) != int(games[i][2])):
                        valid1 = False
                        valid2 = False
                    if (str(poll[3]).lower()!="ap top 25"):
                        valid1 = False
                        valid2 = False
                    if str(poll[5]).lower()==str(games[i][13]).lower() and valid1:
                        poll_data[0] = int(poll[7])
                        poll_data[1] = int(poll[8])
                    elif str(poll[5]).lower()==str(games[i][26]).lower() and valid2:
                        poll_data[2] = int(poll[7])
                        poll_data[3] = int(poll[8])

                for poll_datum in poll_data:
                    game_data.append(poll_datum)

                final_data.append(game_data)


                
            except:
                pass



with open("", 'w', newline='') as file:
    csv_writer = csv.writer(file)

    csv_writer.writerows(final_data)

