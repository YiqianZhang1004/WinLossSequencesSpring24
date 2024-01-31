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
    if season>=2013:
        with open("data/cfbd/raw_data/sorted_lines/sorted_"+str(season)+"_lines.csv","r") as file:
            bets = list(csv.reader(file))
    with open("data/cfbd/raw_data/polls/" + str(season) + "_polls.csv", "r") as file:
        polls = list(csv.reader(file))
    with open("data/cfbd/raw_data/sorted_games/sorted_"+str(season)+"_games.csv", 'r') as file:
        games = list(csv.reader(file))

        ID_index = 0
        date_index = 4
        season_index = 1
        regular_index = 3
        home_name_index = 13
        home_ID_index = 12
        away_name_index = 25
        away_ID_index = 24
        home_score_index = 16
        away_score_index = 28
        home_post_win_prob_index = 21
        away_post_win_prob_index = 33
        home_pre_elo_index = 22
        home_post_elo_index = 23
        away_pre_elo_index = 34
        away_post_elo_index = 35

        if season == 2023 or season <=2001:
            home_post_win_prob_index = 18
            home_pre_elo_index = 19
            home_post_elo_index = 20
            away_ID_index = 21
            away_name_index = 22
            away_score_index = 25
            away_post_win_prob_index = 27
            away_pre_elo_index = 28
            away_post_elo_index = 29

        row_index = 1
        lastIndex=1
        while row_index < len(games):
            try:

                game_data = []
                # gameID
                game_data.append(int(games[row_index][ID_index]))

                # date
                game_data.append(str(games[row_index][date_index])[0:10])
                
                # season
                game_data.append(int(games[row_index][season_index]))

                # regular season or not
                game_data.append(str(games[row_index][regular_index])=="regular")
                
                # home team name
                game_data.append(str(games[row_index][home_name_index]).lower())

                # home team ID
                game_data.append(int(games[row_index][home_ID_index]))
                
                # away team name
                game_data.append(str(games[row_index][away_name_index]).lower())
                
                # away team ID
                game_data.append(int(games[row_index][away_ID_index]))
                
                # home team score
                game_data.append(int(float(games[row_index][home_score_index])))
                
                # away team score
                game_data.append(int(float(games[row_index][away_score_index])))
                
                # determining winner
                if int(float(games[row_index][home_score_index])) > int(float(games[row_index][away_score_index])):
                    game_data.append(1)
                elif int(float(games[row_index][home_score_index])) == int(float(games[row_index][away_score_index])):
                    game_data.append(0.5)
                else:
                    game_data.append(0)

                # the following are non essential data so individual try except blocks are used
                    
                # home post win prob
                try:
                    game_data.append(round(float(games[row_index][home_post_win_prob_index]),3))
                except:
                    game_data.append("NaN")

                #away post win prob
                try:
                    game_data.append(round(float(games[row_index][away_post_win_prob_index]),3))
                except:
                    game_data.append("NaN")

                # home pre game elo
                try:
                    game_data.append(round(float(games[row_index][home_pre_elo_index]),3))
                except:
                    game_data.append("NaN")

                # home post game elo
                try:
                    game_data.append(round(float(games[row_index][home_post_elo_index]),3))
                except:
                    game_data.append("NaN")

                # away pre game elo
                try:
                    game_data.append(round(float(games[row_index][away_pre_elo_index]),3))
                except:
                    game_data.append("NaN")

                # away post game elo
                try:
                    game_data.append(round(float(games[row_index][away_post_elo_index]),3))
                except:
                    game_data.append("NaN")


                raw_betting = [[],[],[],[],[],[]]
                
                # only have betting data starting in 2013
                if season >= 2013:

                    # algorithm accounts for multiple sources for the same game
                    # also accounts for games that have no betting data
                    # also accounts for potential missing games in both the betting and the game data
                    # uses sorted datasets so its a lot faster
                    foundFirst=False
                    foundAll = False
                    incrementor = 0
                    
                    while lastIndex+incrementor< len(bets) and not foundAll:
                        if int(bets[lastIndex+incrementor][0]) == int(games[row_index][0]):
                            foundFirst=True
                            # the following are non essential data so individual try except blocks are used

                            # over under
                            try:
                                raw_betting[0].append(round(float(bets[lastIndex+incrementor][6]),3))
                            except:
                                pass

                            #spread
                            try:
                                raw_betting[1].append(round(float(bets[lastIndex+incrementor][7]),3))
                            except:
                                pass

                            # opening over under
                            try:
                                raw_betting[2].append(round(float(bets[lastIndex+incrementor][10]),3))
                            except:
                                pass

                            # opening spread
                            try:
                                raw_betting[3].append(round(float(bets[lastIndex+incrementor][9]),3))
                            except:
                                pass

                            # home moneyline
                            try:
                                raw_betting[4].append(round(float(bets[lastIndex+incrementor][11]),3))
                            except:
                                pass

                            # away moneyline
                            try:
                                raw_betting[5].append(round(float(bets[lastIndex+incrementor][12]),3))
                            except:
                                pass

                        elif foundFirst:
                            foundAll = True

                        else:
                            incrementor=incrementor+1

                        if incrementor>0 and not foundAll:
                            incrementor = incrementor+1

                        elif foundFirst and not foundAll:
                            lastIndex=lastIndex+1


                average_bets = find_averages(raw_betting)
                # finds average of the betting data
                for average_bet in average_bets:
                    game_data.append(average_bet)
                
                
                poll_data = ["NaN","NaN","NaN","NaN"]
                for j in range(1, len(polls)):
                    # checks to see if the poll is for the correct week and from the right source
                    valid = True
                    if (int(polls[j][2]) != int(games[row_index][2])):
                        valid = False
                    elif (str(polls[j][3]).lower()!="ap top 25"):
                        valid = False
                    if (int(polls[j][2]) > int(games[row_index][2])):
                        break
                    if str(polls[j][5]).lower()==str(games[row_index][13]).lower() and valid:
                        poll_data[0] = int(polls[j][7])
                        poll_data[1] = int(polls[j][8])
                    elif str(polls[j][5]).lower()==str(games[row_index][25]).lower() and valid:
                        poll_data[2] = int(polls[j][7])
                        poll_data[3] = int(polls[j][8])
                
                for poll_datum in poll_data:
                    game_data.append(poll_datum)



                final_data.append(game_data)

                
            except:                
                pass

            row_index = row_index + 1


with open("data/cfbd/processed_data/cfbd.csv", 'w', newline='') as file:
    csv_writer = csv.writer(file)

    csv_writer.writerows(final_data)

