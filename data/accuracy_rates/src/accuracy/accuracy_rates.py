import csv

with open("data/combined_football/processed/combined.csv", "r") as file:
    games = list(csv.reader(file))

# column ids
SEASON = 2
ID1 = 4
ID2 = 6
RESULT = 9
ELO1 = 16
ELO2 = 17
MONEY1 = 12
MONEY2 = 13
RANK1 = 14
RANK2 = 15



# checks if game fit criteria
def perform_checks(season, seasons, team1, argTeam1, team2, argTeam2, rank1, argRank1, rank2, argRank2):
    if season not in seasons:
        return False
    if len(argTeam1) != 0:
        if team1 not in argTeam1:
            return False
    if len(argTeam2) != 0:
        if team2 not in argTeam2:
            return False
    if len(argRank1) != 0:
        if rank1 == "NaN":
            return False
        if int(rank1) not in argRank1:
            return False
    if len(argRank2) != 0:
        if rank2 == "NaN":
            return False
        if int(rank2) not in argRank2:
            return False
    return True

# checks if data is unfound
def check_null(method, stat1, stat2):
    if method == "m":
        return stat1 == "NaN" and stat2 == "NaN"
    return stat1 == "NaN" or stat2 == "NaN"

# checks if prediction was right
def check_prediction(method, stat1, stat2, result):
    if method == "e":
        if float(stat1) > float(stat2):
            return result == 1
        else:
            return result == 0
    elif method == "m":
        if stat1 == "NaN":
            if float(stat2) > 0:
                return result == 1
            return result == 0
        if float(stat1) < 0 :
            return result == 1
        return result == 0
    elif method == "p":
        if float(stat1) < float(stat2):
            return result == 1
        return result == 0
    

# write predicted and unpredicted data to files
def write(predicted, success_file, unpredicted, failure_file):
    if success_file != "":
        with open("data/accuracy_rates/processed_data/" + success_file, "w", newline='') as sfile:
            csv_writer = csv.writer(sfile)
            csv_writer.writerows(predicted)
    if failure_file != "":
        with open("data/accuracy_rates/processed_data/" + failure_file, "w", newline='') as ffile:
            csv_writer = csv.writer(ffile)
            csv_writer.writerows(unpredicted)


# main accuracy function
def get_accuracy(method, seasons, argTeam1, argTeam2, argRank1, argRank2, successFile, failureFile):
    # games predicted and unpredicted
    predicted =[]
    unpredicted =[]

    # get method and stat column indices based on method
    stat1_col = -1
    stat2_col = -1
    if method == "e":
        stat1_col = ELO1
        stat2_col = ELO2
    elif method == "m":
        stat1_col = MONEY1
        stat2_col = MONEY2
    elif method == "p":
        stat1_col = RANK1
        stat2_col = RANK2
    else:
        return "invalid method"
    

    total_count = 0
    total_predicted = 0
    
    # looping through each game
    for i in range(1, len(games)):
        game = games[i]


        # if the game passes checks and data wasn't null, then the game is accounted for
        if perform_checks(int(game[SEASON]), seasons, 
                          int(game[ID1]), argTeam1, 
                          int(game[ID2]), argTeam2, 
                          game[RANK1], argRank1, 
                          game[RANK2], argRank2,) and not check_null(method, game[stat1_col], game[stat2_col]):

            total_count = total_count + 1
            # if the game was predicted correctly
            if check_prediction(method, game[stat1_col], game[stat2_col], float(game[RESULT])):
                predicted.append(game)
                total_predicted = total_predicted + 1

            # if the game was predicted incorrectly
            else:
                unpredicted.append(game)


    write(predicted, successFile, unpredicted, failureFile)
            

    if total_count == 0:
        print("no games")
        return (0,0)
    else:
        accuracy = round(100* total_predicted / total_count, 4)
        print(f"Prediction of accuracy of {accuracy:.4f}% with {total_count} games")
        return (accuracy, total_count)

    
# testing
get_accuracy("p",[1985],[],[],[],[], "succes.csv","fail.csv")
