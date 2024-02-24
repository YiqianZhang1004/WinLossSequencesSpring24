import csv

with open("data/cfbd/processed_data/cfbd_close_only.csv", "r") as file:
    cfbd = list(csv.reader(file))

with open("data/sportsbookreviewsonline/ncaaf/processsed_data/sbro_ncaaf_close_only_with_ranks.csv", "r") as file:
    sbro = list(csv.reader(file))

final_data = [["gameId",
               "date","season",
               "homeTeam", "homeTeamId", 
               "awayTeam", "awayTeamId", 
               "homeScore","awayScore", 
               "result", 
               "spread","overUnder",
               "homeMoneyline","awayMoneyline", 
               "homeTeamRank", "awayTeamRank",
               "homeElo","awayElo"]]


def getMatch(date, team1Id, team2Id):
    for i in range(1, len(sbro)):
        sbro_game = sbro[i]

        if sbro_game[0] == date and sbro_game[4] == team1Id and sbro_game[6] == team2Id:
            return sbro_game

    return "NaN"



def getAverage(data1, data2):
    if data1 == "NaN" and data2 == "NaN":
        return "NaN"
    if data1 == "NaN":
        return data2
    if data2 == "NaN":
        return data1
    
    return (float(data1) + float(data2))/2


for i in range(1, len(cfbd)):
    cfbd_game = cfbd[i]
    sbro_game = getMatch(cfbd_game[1], cfbd_game[5], cfbd_game[7])
    game_data = [cfbd_game[0],
                cfbd_game[1],cfbd_game[2],
                cfbd_game[4], cfbd_game[5],
                cfbd_game[6], cfbd_game[7],
                cfbd_game[8], cfbd_game[9],
                cfbd_game[10],
                cfbd_game[18], cfbd_game[17],
                cfbd_game[19], cfbd_game[20],
                cfbd_game[21], cfbd_game[24],
                cfbd_game[13], cfbd_game[15]]

    if sbro_game == "NaN":
        final_data.append(game_data)
        continue

    for j in range(10, 14):
        game_data[j] = getAverage(game_data[j], sbro_game[j])

    final_data.append(game_data)

with open("data/combined_football/processed/combined.csv", "w", newline='') as outfile:
    csv_writer = csv.writer(outfile)
    csv_writer.writerows(final_data)
