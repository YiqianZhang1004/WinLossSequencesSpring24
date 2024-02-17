import csv

with open("data/cfbd/processed_data/cfbd_close_only.csv", "r") as file:
    cfbd = list(csv.reader(file))

with open("data/sportsbookreviewsonline/ncaaf/processsed_data/sbro_ncaaf_close_only_with_ranks.csv", "r") as file:
    sbro = list(csv.reader(file))

# CFBD column ids
CFBD_SEASON = 2
CFBD_TEAM1ID = 5
CFBD_TEAM2ID = 7
CFBD_RESULT = 10
CFBD_PRE_ELO1 = 13
CFBD_PRE_ELO2 = 15
CFBD_MONEYLINE1 = 19
CFBD_MONEYLINE2 = 20
CFBD_RANK1 = 21
CFBD_RANK2 = 24

# SBRO column ids
SBRO_SEASON = 1
SBRO_TEAM1ID = 4
SBRO_TEAM2ID = 6
SBRO_RESULT = 9
SBRO_PRE_ELO1 = -1
SBRO_PRE_ELO2 = -1
SBRO_MONEYLINE1 = 12
SBRO_MONEYLINE2 = 13
SBRO_RANK1 = 14
SBRO_RANK2 = 16

# games predicted and unpredicted
predicted =[]
unpredicted =[]

# returns the game csv of the right source
def get_source(source_index):
    if source_index == 0:
        return cfbd
    elif source_index == 1:
        return sbro

# gets the column ids based on source
def get_indices(source_index):
    if source_index == 0:
        return [CFBD_SEASON, CFBD_TEAM1ID, CFBD_TEAM2ID, CFBD_RESULT, CFBD_PRE_ELO1, CFBD_PRE_ELO2, CFBD_MONEYLINE1, CFBD_MONEYLINE2, CFBD_RANK1, CFBD_RANK2]
    elif source_index == 1:
        return [SBRO_SEASON, SBRO_TEAM1ID, SBRO_TEAM2ID, SBRO_RESULT, SBRO_PRE_ELO1, SBRO_PRE_ELO2, SBRO_MONEYLINE1, SBRO_MONEYLINE2, SBRO_RANK1, SBRO_RANK2]

# checks if game fit criteria
def perform_checks(season, seasons_list, team_id1, arg_team_id1, team_id2, arg_team_id2, rank1, arg_rank1, rank2, arg_rank2):
    # season is a season we are looking into
    if season not in seasons_list:
        return False
    # team1 parameter is specified but doesn't match
    if arg_team_id1 != -1 and team_id1 != arg_team_id1:
        return False
    # team2 parameter is specified but doesn't match
    if arg_team_id2 != -1 and team_id2 != arg_team_id2:
        return False
    # rank1 parameter is specified but doesn't match or is unfound
    if arg_rank1 != -1 and (rank1 != arg_rank1 or rank1 == -2):
        return False
    # rank2 parameter is specified but doesn't match or is unfound
    if arg_rank2 != -1 and (rank2 != arg_rank2 or rank2 == -2):
        return False
    return True

# checks if data is unfound
def check_null(method, stat1, stat2):
    # if predicting by elo, both stats must exist
    if method == 0:
        return stat1 == -2 or stat2 == -2
    # if predicting by moneyline or poll rank, only one stat must exist
    else:
        return stat1 == -2  and stat2 == -2

# checks if prediction was right
def check_prediction(method, stat1, stat2, result):
    # predicting by elo
    if method == 0:
        # higher elo team beat lower elo team
        if stat1 > stat2:
            return result == 1.0
        elif stat1 < stat2:
            return result == 0.0
        else:
            return result == 0.5
    # predicting by moneyline
    elif method == 1:
        # positive moneyline team lost
        if stat1 == -2:
            return result == (1.0 if stat2 > 0 else 0.0)
        else:
            return result == (0.0 if stat1 > 0 else 1.0)
    # predicting by poll rank
    else:
        # higher rank beat lower rank or unranked team
        if stat1 == -2:
            return result == 0.0
        elif stat2 == -2:
            return result == 1.0
        elif stat1 < stat2:
            return result == 1.0
        else:
            return result == 0.0

# write predicted and unpredicted data to files
def write(success_file, failure_file):
    global predicted, unpredicted
    with open("data/accuracy_rates/processed_data/" + success_file, "w", newline='') as sfile:
        csv_writer = csv.writer(sfile)
        csv_writer.writerows(predicted)
    with open("data/accuracy_rates/processed_data/" + failure_file, "w", newline='') as ffile:
        csv_writer = csv.writer(ffile)
        csv_writer.writerows(unpredicted)


# main accuracy function
def get_accuracy(source, method, seasons_list, arg_team_id1, arg_team_id2, arg_rank1, arg_rank2, success_file, failure_file):
    global predicted, unpredicted

    # get source index
    source_index = -1
    if source == "cfbd":
        source_index = 0
    elif source == "sbro":
        source_index = 1
    else:
        return "invalid source"
    
    # get games based on source index
    games = get_source(source_index)

    # get column indices based on source index
    season_col, team_id1_col, team_id2_col, result_col, pre1_col, pre2_col, money1_col, money2_col, rank1_col, rank2_col = get_indices(source_index)
    
    # get method and stat column indices based on method
    method_index = -1
    stat1_col = -1
    stat2_col = -1
    if method == "elo":
        method_index = 0
        stat1_col = pre1_col
        stat2_col = pre2_col
    elif method == "moneyline":
        method_index = 1
        stat1_col = money1_col
        stat2_col = money2_col
    elif method == "poll":
        method_index = 2
        stat1_col = rank1_col
        stat2_col = rank2_col
    else:
        return "invalid method"
    
    # no elo data for SBRO games
    if method_index == 0 and source_index == 1:
        write(success_file, failure_file)
        return "no games"
    

    total_count = 0
    total_predicted = 0
    
    # looping through each game
    for i in range(1, len(games)):
        game = games[i]

        # -2 represents data was missing
        try:
            rank1 = int(game[rank1_col])
        except:
            rank1 = -2
        
        try:
            rank2 = int(game[rank2_col])
        except:
            rank2 = -2
        
        try:
            stat1 = int(float(game[stat1_col]))
        except:
            stat1 = -2

        try:
            stat2 = int(float(game[stat2_col]))
        except:
            stat2 = -2

        # if the game passes checks and data wasn't null, then the game is accounted for
        if perform_checks(int(game[season_col]), seasons_list, 
                          int(game[team_id1_col]), arg_team_id1, 
                          int(game[team_id2_col]), arg_team_id2, 
                          rank1, arg_rank1, 
                          rank2, arg_rank2,) and not check_null(method_index, stat1, stat2):

            total_count = total_count + 1
            # if the game was predicted correctly
            if check_prediction(method_index, stat1, stat2, float(game[result_col])):
                predicted.append(game)
                total_predicted = total_predicted + 1
            # if the game was predicted incorrectly
            else:
                unpredicted.append(game)

        
    write(success_file, failure_file)
            

    if total_count == 0:
        return "no games"
    else:
        accuracy = round(100* total_predicted / total_count, 4)
        return f"prediction of accuracy of {accuracy:.4f}% with {total_count} games"

    

# testing
print(get_accuracy("sbro", "moneyline",[2021],-1, -1, -1, -1, "succes.csv","fail.csv"))
