import csv

final_data = [["gameID", "date", "season", "regular", "team1", "team1ID", "team2", "team2ID", 
               "score1", "score2","result", "homePostWinProb", "awayPostWinProb","homePreElo",
               "homePostElo","awayPreElo","awayPostElo", "overUnder", "spread", "openingOverUnder", 
               "openingSpread", "homeMoneyLine", "awayMoneyLine", "homeRank", "homeFirstPlaceVotes", 
               "homePollPoints", "awayRank", "awayFirstPlaceVotes","awayPollPoints"]]

errors = [["gameID","date","season","regular","team1","team1ID","team2","team2ID","score1","score2"]]

seasons = []
for i in range(1980, 2024):
    seasons.append(i)

def find_averages(raw_betting):
    averages=["NaN","NaN","NaN","NaN","NaN","NaN"]
    for i in range(len(raw_betting)):
        if len(raw_betting[i])!=0:
            averages[i] = round(float(sum(raw_betting[i])/len(raw_betting[i])),3)
    return averages
count = 0


for season in seasons:
    if season>=2013:
        with open("data/cfbd/raw_data/sorted_lines/sorted_"+str(season)+"_lines.csv","r") as bets_file:
            bets = list(csv.reader(bets_file))
    with open("data/cfbd/raw_data/polls/" + str(season) + "_polls.csv", "r") as polls_file:
        polls = list(csv.reader(polls_file))
    with open("data/cfbd/raw_data/sorted_games/sorted_"+str(season)+"_games.csv", 'r') as games_file:
        games = list(csv.reader(games_file))

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

        if season == 2009:
            away_name_index = 26
            away_ID_index = 25
            away_score_index = 29
            home_post_win_prob_index = 22
            away_post_win_prob_index = 35
            home_pre_elo_index = 23
            home_post_elo_index = 24
            away_pre_elo_index = 36
            away_post_elo_index = 37

        elif season == 2023 or season <=2001:
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
                game_id = int(games[row_index][ID_index])
                game_data.append(game_id)

                # date
                date = str(games[row_index][date_index])[0:10]
                game_data.append(date)
                
                # season
                game_data.append(season)

                # regular season or not
                regular = str(games[row_index][regular_index])=="regular"
                game_data.append(regular)
                
                # home team name
                home_team = str(games[row_index][home_name_index]).lower()
                game_data.append(home_team)

                # home team ID
                home_id = int(games[row_index][home_ID_index])
                game_data.append(home_id)
                
                # away team name
                away_team = str(games[row_index][away_name_index]).lower()
                game_data.append(away_team)
                
                # away team ID
                away_id = int(games[row_index][away_ID_index])
                game_data.append(away_id)
                
                # home team score
                home_score = int(float(games[row_index][home_score_index]))
                game_data.append(home_score)
                
                # away team score
                away_score = int(float(games[row_index][away_score_index]))
                game_data.append(away_score)
                
                # determining winner
                if home_score > away_score:
                    game_data.append(1)
                elif home_score == away_score:
                    game_data.append(0.5)
                else:
                    game_data.append(0)

                # the following are non essential data so individual try except blocks are used
                home_post_win_prob = away_post_win_prob = home_pre_elo = home_post_elo = away_pre_elo = away_post_elo = "NaN"
                
                # home post win prob
                try:
                    home_post_win_prob = round(float(games[row_index][home_post_win_prob_index]),3)
                except:
                    pass

                #away post win prob
                try:
                    away_post_win_prob = round(float(games[row_index][away_post_win_prob_index]),3)
                except:
                    pass

                # home pre game elo
                try:
                    home_pre_elo = round(float(games[row_index][home_pre_elo_index]),3)
                except:
                    pass

                # home post game elo
                try:
                    home_post_elo = round(float(games[row_index][home_post_elo_index]),3)
                except:
                    pass
                # away pre game elo
                try:
                    away_pre_elo = round(float(games[row_index][away_pre_elo_index]),3)
                except:
                    pass
                # away post game elo
                try:
                    away_post_elo = round(float(games[row_index][away_post_elo_index]),3)
                except:
                    pass
                
                game_data.append(home_post_win_prob)
                game_data.append(away_post_win_prob)
                game_data.append(home_pre_elo)
                game_data.append(home_post_elo)
                game_data.append(away_pre_elo)
                game_data.append(away_post_elo)
                
                
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
                                overUnder = round(float(bets[lastIndex+incrementor][6]),3)
                                raw_betting[0].append(overUnder)
                            except:
                                pass

                            # spread
                            try:
                                spread = round(float(bets[lastIndex+incrementor][7]),3)
                                raw_betting[1].append(spread)
                            except:
                                pass

                            # opening over under
                            try:
                                openingOverUnder = round(float(bets[lastIndex+incrementor][10]),3)
                                raw_betting[2].append(openingOverUnder)
                            except:
                                pass

                            # opening spread
                            try:
                                openingSpread = round(float(bets[lastIndex+incrementor][9]),3)
                                raw_betting[3].append(openingSpread)
                            except:
                                pass

                            # home moneyline
                            try:
                                homeMoneyline = round(float(bets[lastIndex+incrementor][11]),3)
                                raw_betting[4].append(homeMoneyline)
                            except:
                                pass

                            # away moneyline
                            try:
                                awayMoneyline = round(float(bets[lastIndex+incrementor][12]),3)
                                raw_betting[5].append(awayMoneyline)
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
                
                
                homeRanking = homeVotes = homePoints = awayRanking = awayVotes = awayPoints = "NaN"
                for poll_row in range(1, len(polls)):
                    # checks to see if the poll is for the correct week and from the right source
                    valid = True
                    poll_week = int(polls[poll_row][2])
                    game_week = int(games[row_index][2])
                    poll_source = str(polls[poll_row][3]).lower()
                    poll_team = str(polls[poll_row][5]).lower()
                    if poll_week != game_week or poll_source != "ap top 25":
                        valid = False
                    
                    if poll_team == home_team and valid:
                        # ranking
                        try:
                            homeRanking = int(polls[poll_row][4])
                        except:
                            pass
                        # number of first place votes
                        try:
                            homeVotes = int(polls[poll_row][7])
                        except:
                            pass
                        # points
                        try:
                            homePoints = int(polls[poll_row][8])
                        except:
                            pass
                    elif poll_team == away_team and valid:
                        # ranking
                        try:
                            awayRanking = int(polls[poll_row][4])
                        except:
                            pass
                        # number of first place votes
                        try:
                            awayVotes = int(polls[poll_row][7])
                        except:
                            pass
                        # points
                        try:
                            awayPoints = int(polls[poll_row][8])
                        except:
                            pass
                
                game_data.append(homeRanking)
                game_data.append(homeVotes)
                game_data.append(homePoints)
                game_data.append(awayRanking)
                game_data.append(awayVotes)
                game_data.append(awayPoints)
                

                final_data.append(game_data)

                
            except:   
                error_row = []
                error_row.append(games[row_index][ID_index])
                error_row.append(games[row_index][date_index])
                error_row.append(games[row_index][season_index])
                error_row.append(games[row_index][regular_index])
                error_row.append(games[row_index][home_name_index])
                error_row.append(games[row_index][home_ID_index])
                error_row.append(games[row_index][away_name_index])
                error_row.append(games[row_index][away_ID_index])
                error_row.append(games[row_index][home_score_index])
                error_row.append(games[row_index][away_score_index])

                errors.append(error_row)

                

            row_index = row_index + 1


with open("data/cfbd/processed_data/cfbd.csv", 'w', newline='') as processed_file:
    csv_writer = csv.writer(processed_file)
    csv_writer.writerows(final_data)

with open("data/cfbd/processed_data/skipped.csv", "w", newline='') as error_file:
    csv_writer = csv.writer(error_file)
    csv_writer.writerows(errors)