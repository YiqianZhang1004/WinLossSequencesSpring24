import csv

final_data = [["gameID", "date", "season", "regular", "team1", "team1ID", "team2", "team2ID", 
               "score1", "score2","result", "homePostWinProb", "awayPostWinProb","homePreElo",
               "homePostElo","awayPreElo","awayPostElo", "overUnder", "spread", "openingOverUnder", 
               "openingSpread", "homeMoneyline", "awayMoneyline", "homeRank", "homeFirstPlaceVotes", 
               "homePollPoints", "awayRank", "awayFirstPlaceVotes","awayPollPoints"]]

errors = [["gameID","date","season","regular","team1","team1ID","team2","team2ID","score1","score2"]]

seasons = []
for i in range(1980, 2024):
    seasons.append(i)

# column indices change based on year
def get_indices(season):
    if season == 2009:
        return [0, 4, 1, 3, 13, 12, 26, 25, 16, 29, 22, 35, 23, 24, 36, 37]
    elif season == 2023 or season <= 2001:
        return [0, 4, 1, 3, 13, 12, 22, 21, 16, 25, 18, 27, 19, 20, 28, 29]
    else:
        return [0, 4, 1, 3, 13, 12, 25, 24, 16, 28, 21, 33, 22, 23, 34, 35]

# determine winner based on their scores
def determine_winner(score1, score2):
    if score1 > score2:
        return 1
    elif score1 == score2:
        return 0.5
    return 0

# returns the proper representation of betting data
def get_betting_data(data):
    try: 
        return round(float(data), 3)
    except:
        return "NaN"

# finds averages of betting data
def find_averages(raw_betting):
    averages=["NaN","NaN","NaN","NaN","NaN","NaN"]
    for i in range(len(raw_betting)):
        total = 0.0
        num = 0
        for j in range(len(raw_betting[i])):
            if raw_betting[i][j] != "NaN":
                total = total + raw_betting[i][j]
                num = num + 1
        if num != 0:
            averages[i] = round(float(total/num), 3)
    return averages

# returns proper representation of polling data
def get_individual_polls(data):
    try:
        return int(data)
    except:
        return "NaN"

# iterates through an entire season of polls to find correct poll data
def get_polling_data(polls, week):
    homeRanking = homeVotes = homePoints = awayRanking = awayVotes = awayPoints = "NaN"
    # searching for home team
    for row_index in range(1,len(polls)):
        # checks to see if the poll is for the correct week and from the right source
        poll_week = int(polls[row_index][2])
        poll_source = str(polls[row_index][3]).lower()
        poll_team = str(polls[row_index][5]).lower()
        if poll_team == home_team and poll_week == week and poll_source == "ap top 25":
            # ranking
            homeRanking = get_individual_polls(polls[row_index][4])
            # number of first place votes
            homeVotes = get_individual_polls(polls[row_index][7])
            # points
            homePoints = get_individual_polls(polls[row_index][8])
            break

    # searching for away team
    for row_index in range(1, len(polls)):
        poll_week = int(polls[row_index][2])
        poll_source = str(polls[row_index][3]).lower()
        poll_team = str(polls[row_index][5]).lower()
        if poll_team == away_team and poll_week == week and poll_source == "ap top 25":
            # ranking
            awayRanking = get_individual_polls(polls[row_index][4])
            # number of first place votes
            awayVotes = get_individual_polls(polls[row_index][7])
            # points
            awayPoints = get_individual_polls(polls[row_index][8])
            break
    return [homeRanking, homeVotes, homePoints, awayRanking, awayVotes, awayPoints]

for season in seasons:
    # only have betting data starting in 2013
    if season>=2013:
        with open("data/cfbd/raw_data/sorted_lines/sorted_"+str(season)+"_lines.csv","r") as bets_file:
            bets = list(csv.reader(bets_file))
    with open("data/cfbd/raw_data/polls/" + str(season) + "_polls.csv", "r") as polls_file:
        polls = list(csv.reader(polls_file))
    with open("data/cfbd/raw_data/sorted_games/sorted_"+str(season)+"_games.csv", 'r') as games_file:
        games = list(csv.reader(games_file))

        (ID_index, date_index, season_index, regular_index, 
         home_name_index, home_ID_index, away_name_index, 
         away_ID_index, home_score_index, away_score_index, 
         home_post_win_prob_index, away_post_win_prob_index, 
         home_pre_elo_index, home_post_elo_index, 
         away_pre_elo_index, away_post_elo_index) = get_indices(season)

        row_index = 1
        lastIndex=1
        while row_index < len(games):
            try:
                game_id = int(games[row_index][ID_index])
                date = str(games[row_index][date_index])[0:10]
                regular = str(games[row_index][regular_index])=="regular"
                home_team = str(games[row_index][home_name_index]).lower()
                home_id = int(games[row_index][home_ID_index])
                away_team = str(games[row_index][away_name_index]).lower()
                away_id = int(games[row_index][away_ID_index])
                home_score = int(float(games[row_index][home_score_index]))
                away_score = int(float(games[row_index][away_score_index]))
                
                # the below data is non essential data
                home_post_win_prob = get_betting_data(games[row_index][home_post_win_prob_index])
                away_post_win_prob = get_betting_data(games[row_index][away_post_win_prob_index])
                home_pre_elo = get_betting_data(games[row_index][home_pre_elo_index])
                home_post_elo = get_betting_data(games[row_index][home_post_elo_index])
                away_pre_elo = get_betting_data(games[row_index][away_pre_elo_index])
                away_post_elo = get_betting_data(games[row_index][away_post_elo_index])
               
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
                            # over under
                            raw_betting[0].append(get_betting_data(bets[lastIndex+incrementor][6]))
                            
                            # spread
                            raw_betting[1].append(get_betting_data(bets[lastIndex+incrementor][7]))
                           
                            # opening over under
                            raw_betting[2].append(get_betting_data(bets[lastIndex+incrementor][10]))

                            # opening spread
                            raw_betting[3].append(get_betting_data(bets[lastIndex+incrementor][9]))

                            # home moneyline
                            raw_betting[4].append(get_betting_data(bets[lastIndex+incrementor][11]))

                            # away moneyline
                            raw_betting[5].append(get_betting_data(bets[lastIndex+incrementor][12]))

                        elif foundFirst:
                            foundAll = True

                        else:
                            incrementor=incrementor+1

                        if incrementor>0 and not foundAll:
                            incrementor = incrementor+1

                        elif foundFirst and not foundAll:
                            lastIndex=lastIndex+1
                
                average_bets = find_averages(raw_betting)
                overUnder = average_bets[0]
                spread = average_bets[1]
                openingOverUnder = average_bets[2]
                openingSpread = average_bets[3]
                homeMoneyline = average_bets[4]
                awayMoneyline = average_bets[5]

                homeRanking, homeVotes, homePoints, awayRanking, awayVotes, awayPoints = get_polling_data(polls, int(games[row_index][2]))
            
                game_data = [game_id, date, season, regular, 
                             home_team, home_id, away_team, away_id, 
                             home_score, away_score, determine_winner(home_score, away_score),
                             home_post_win_prob, away_post_win_prob, home_pre_elo, home_post_elo,
                             away_pre_elo, away_post_elo, overUnder, spread, openingOverUnder,
                             openingSpread, homeMoneyline, awayMoneyline, homeRanking, homeVotes, 
                             homePoints, awayRanking, awayVotes, awayPoints]

                final_data.append(game_data)

            except:   
                error_row =[games[row_index][ID_index], games[row_index][date_index], games[row_index][season_index],
                            games[row_index][regular_index], games[row_index][home_name_index], games[row_index][home_ID_index],
                            games[row_index][away_name_index], games[row_index][away_ID_index],
                            games[row_index][home_score_index], games[row_index][away_score_index]]

                errors.append(error_row)

            row_index = row_index + 1


with open("data/cfbd/processed_data/cfbd.csv", 'w', newline='') as processed_file:
    csv_writer = csv.writer(processed_file)
    csv_writer.writerows(final_data)

with open("data/cfbd/processed_data/cfbd_error.csv", "w", newline='') as error_file:
    csv_writer = csv.writer(error_file)
    csv_writer.writerows(errors)
