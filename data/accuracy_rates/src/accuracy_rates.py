import csv

with open("data/cfbd/processed_data/cfbd_close_only.csv", "r") as file:
    cfbd = list(csv.reader(file))

with open("data/sportsbookreviewsonline/ncaaf/processsed_data/sbro_ncaaf_close_only_with_ranks.csv", "r") as file:
    sbro = list(csv.reader(file))


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

SBRO_SEASON = 1
SBRO_TEAM1ID = 4
SBRO_TEAM2ID = 6
SBRO_RESULT = 9
SBRO_PRE_ELO1 = -1
SBRO_PRE_ELO2 = -1
SBRO_MONEYLINE1 = 16
SBRO_MONEYLINE2 = 17
SBRO_RANK1 = 18
SBRO_RANK2 = 20

def get_source(source_index):
    if source_index == 0:
        return cfbd
    elif source_index == 1:
        return sbro

def get_indices(source_index):
    if source_index == 0:
        return [CFBD_SEASON, CFBD_TEAM1ID, CFBD_TEAM2ID, CFBD_RESULT, CFBD_PRE_ELO1, CFBD_PRE_ELO2, CFBD_MONEYLINE1, CFBD_MONEYLINE2, CFBD_RANK1, CFBD_RANK2]
    elif source_index == 1:
        return [SBRO_SEASON, SBRO_TEAM1ID, SBRO_TEAM2ID, SBRO_RESULT, SBRO_PRE_ELO1, SBRO_PRE_ELO2, SBRO_MONEYLINE1, SBRO_MONEYLINE2, SBRO_RANK1, SBRO_RANK2]
    
def perform_checks(season, seasons_list, team_id1, arg_team_id1, team_id2, arg_team_id2, rank1, arg_rank1, rank2, arg_rank2):
    if season not in seasons_list:
        return False
    if arg_team_id1 != -1 and team_id1 != arg_team_id1:
        return False
    if arg_team_id2 != -1 and team_id2 != arg_team_id2:
        return False
    if arg_rank1 != -1 and rank1 != arg_rank1:
        return False
    if arg_rank2 != -1 and rank2 != arg_rank2:
        return False
    if arg_rank1 == -2:
        return False
    if arg_rank2 == -2:
        return False

    return True
    

def check_prediction(method, stat1, stat2, result):
    if stat1 == -2 or stat2 == -2:
        return False
    if method == 0:
        if stat1 > stat2:
            return result == 1.0
        elif stat1 < stat2:
            return result == 0.0
        else:
            return result == 0.5
    else:
        if stat1 < stat2:
            return result == 1.0
        elif stat1 > stat2:
            return result == 0.0
        else:
            return result == 0.5

predicted = []
def get_accuracy(source, method, seasons_list, arg_team_id1, arg_team_id2, arg_rank1, arg_rank2):
    source_index = -1
    if source == "cfbd":
        source_index = 0
    elif source == "sbro":
        source_index = 1
    else:
        return "invalid source"
    
    games = get_source(source_index)


    season_col, team_id1_col, team_id2_col, result_col, pre1_col, pre2_col, money1_col, money2_col, rank1_col, rank2_col = get_indices(source_index)
    
    
    total_count = 0
    total_predicted = 0

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
    
    for i in range(1, len(games)):
        game = games[i]
        try:
            rank1 = int(game[rank1_col])
            rank2 = int(game[rank2_col])
        except:
            rank1 = -2
            rank2 = -2

        try:
            stat1 = float(game[stat1_col])
            stat2 = float(game[stat2_col])
        except:
            stat1 = -2
            stat2 = -2
        
        if perform_checks(int(game[season_col]), seasons_list, 
                          int(game[team_id1_col]), arg_team_id1, 
                          int(game[team_id2_col]), arg_team_id2, 
                          rank1, arg_rank1, 
                          rank2, arg_rank2):
            total_count = total_count + 1
            if check_prediction(method_index, stat1, stat2, float(game[result_col])):
                predicted.append(i)
                total_predicted = total_predicted + 1

    if total_count == 0:
        return "no games"
    else:
        return "prediction of accuracy of " + str(100*round(total_predicted/total_count,4)) + "% with "  + str(total_count) + " games"
    




print(get_accuracy("cfbd", "elo",[2020,2021, 2022],-1, -1, -1, -1))



