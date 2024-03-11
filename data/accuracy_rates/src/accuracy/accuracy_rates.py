import csv

with open("data/combined_football/processed/combined.csv", "r") as file:
    games = list(csv.reader(file))

# column ids
SEASON = 2
WEEK = 3
ID1 = 5
ID2 = 7
RESULT = 10
ELO1 = 17
ELO2 = 18
MONEY1 = 13
MONEY2 = 14
RANK1 = 15
RANK2 = 16


# checks if game fit criteria
def performChecks(season, seasons,week, weeks, team1, argTeam1, team2, argTeam2, rank1, argRank1, rank2, argRank2, minMoneylineDiff, maxMoneylineDiff, money1, money2, minEloDiff, maxEloDiff, elo1, elo2):
    if len(seasons) != 0 and season not in seasons:
        return False
    if len(weeks) != 0 and week not in weeks:
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
    if maxMoneylineDiff != -1 and minMoneylineDiff!= -1:
        if money1 == "NaN" and money2 == "NaN":
            return False
        elif money1 == "NaN":
            diff = abs(2 * float(money2))
            if diff < minMoneylineDiff or diff > maxMoneylineDiff:
                return False
        elif money2 == "NaN":
            diff = abs(2*float(money1))
            if diff < minMoneylineDiff or diff > maxMoneylineDiff:
                return False
        else:
            diff = abs(float(money1)-float(money2))
            if diff < minMoneylineDiff or diff > maxMoneylineDiff:
                return False
    if minEloDiff != -1 and maxEloDiff != -1:
        if elo1== "NaN" or elo2 == "NaN":
            return False
        else:
            diff = abs(float(elo1) - float(elo2))
            if diff < minEloDiff or diff > maxEloDiff:
                return False
                
    return True

# checks if data is unfound
def checkNull(method, stat1, stat2):
    if method == "m":
        return stat1 == "NaN" and stat2 == "NaN"
    
    return stat1 == "NaN" or stat2 == "NaN"

# returns if team 1 was predicted to win   
def getPrediction(method, stat1, stat2):
    if method == "e":
        return float(stat1) > float(stat2)
    elif method == "m":
        if stat1 == "NaN":
            return float(stat2) > 0
        return float(stat1) < 0
    elif method == "p":
        return float(stat1) < float(stat2)
    

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
def getAccuracy(method,seasons,weeks, argTeam1, argTeam2, argRank1, argRank2, minMoneylineDiff, maxMoneylineDiff, minEloDiff, maxEloDiff, successFile, failureFile):
    # games predicted and unpredicted
    predicted =[]
    unpredicted = []
    underPredicted =[]
    overPredicted = []

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
    total_over = 0
    total_under = 0
    
    # looping through each game
    for i in range(1, len(games)):
        game = games[i]


        # if the game passes checks and data wasn't null, then the game is accounted for
        if performChecks(int(game[SEASON]), seasons, int(game[WEEK]), weeks, 
                          int(game[ID1]), argTeam1, 
                          int(game[ID2]), argTeam2, 
                          game[RANK1], argRank1, 
                          game[RANK2], argRank2,
                          minMoneylineDiff, maxMoneylineDiff,
                          game[MONEY1], game[MONEY2],
                          minEloDiff, maxEloDiff,
                          game[ELO1], game[ELO2]) and not checkNull(method, game[stat1_col], game[stat2_col]):

            total_count = total_count + 1

            prediction = getPrediction(method, game[stat1_col], game[stat2_col])
            result = float(game[RESULT])
            if (prediction and result == 1) or (not prediction and result == 0):
                predicted.append(game)
                total_predicted = total_predicted + 1            

            # if the game was predicted incorrectly
            else:
                unpredicted.append(game)
                if prediction:
                    overPredicted.append(game)
                    total_over = total_over + 1
                else:
                    underPredicted.append(game)
                    total_under = total_under + 1

    write(predicted, successFile, unpredicted, failureFile)
            

    if total_count == 0:
        print("no games")
        return (0,0, 0, 0)
    else:
        accuracy = round(100* total_predicted / total_count, 4)
        
        print((accuracy, total_count, total_over, total_under))
        return (accuracy, total_count, total_over, total_under)

    
# testing
#getAccuracy("e",[],[2],[],[],[],[], -1,  -1, -1, -1, "succes.csv","fail.csv")
