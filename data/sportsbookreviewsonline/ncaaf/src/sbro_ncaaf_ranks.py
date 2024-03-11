import csv
import json
from datetime import datetime


with open("data/sportsbookreviewsonline/ncaaf/processsed_data/sbro_ncaaf.csv", "r") as file:
    sbro_data = list(csv.reader(file))

with open("data/sportsbookreviewsonline/ncaaf/processsed_data/sbro_ncaaf_close_only.csv", "r") as file:
    sbro_data_close_only = list(csv.reader(file))

with open("data/team_dictionary/processed_data/cfb_polls_standardized.csv", "r") as file:
    rank_data = list(csv.reader(file))

with open("data/team_dictionary/processed_data/sbro_to_cfbd_id.json", "r") as file:
    team_to_id = json.load(file)

with open("data/sportsbookreviewsonline/ncaaf/processsed_data/dateToWeek.json", "r") as file:
    dateToWeek = json.load(file)

final_data = [["date", "season", "week", "neutral", "homeTeam", "homeTeamId", "awayTeam", "awayTeamId",
               "homeScore","awayScore", "result",
               "spreadOpen", "spreadClose","spreadH2", 
               "overUnderOpen","overUnderClose", "overUnderH2", 
               "homeMoneyline", "awayMoneyline",
               "homeTeamRank", "homeTeamPoints",
               "awayTeamRank", "awayTeamPoints"]]

final_data_close_only = [["date", "season", "week", "neutral", "homeTeam", "homeTeamId","awayTeam","awayTeamId",
               "homeScore","awayScore", "result",
               "spreadClose","overUnderClose",
               "homeMoneyline", "awayMoneyline",
               "homeTeamRank", "homeTeamPoints",
               "awayTeamRank", "awayTeamPoints"]]


weeks = []
for i in range(1, len(rank_data)):
    week = rank_data[i][1]
    year = week.split(" ")[0]
    if week.find("Preseason") !=-1:
        weeks.append(datetime.strptime(year + "-08-01", "%Y-%m-%d"))
    elif week.find("Final")!=-1:
        weeks.append(datetime.strptime(str(int(year)+1) + "-02-01","%Y-%m-%d"))
    else:
        weeks.append(datetime.strptime(week, "%Y-%m-%d"))


null = datetime.strptime("2000-01-01", "%Y-%m-%d")

for i in range(1, len(sbro_data)):
    game_data = sbro_data[i]

    game_data.append("NaN")
    game_data.append("NaN")
    game_data.append("NaN")
    game_data.append("NaN")

    game_data_close_only = sbro_data_close_only[i]
    game_data_close_only.append("NaN")
    game_data_close_only.append("NaN")
    game_data_close_only.append("NaN")
    game_data_close_only.append("NaN")


    date = datetime.strptime(sbro_data[i][0], "%Y-%m-%d")
    year = date.year


    team1 = sbro_data[i][3]

    team2 = sbro_data[i][4]

    team1Id = team_to_id[team1]
    team2Id = team_to_id[team2]

    game_data.insert(4, team1Id)
    game_data.insert(6, team2Id)
    game_data_close_only.insert(4, team1Id)
    game_data_close_only.insert(6, team2Id)

    last_week = null
    for j in range(len(weeks)-1):
        week_date = weeks[j]
        next_week_date = weeks[j+1]

        if date >= week_date and date < next_week_date:
            last_week = week_date
            break

    week_number = dateToWeek[last_week.strftime('%Y-%m-%d')]
    print(week_number)

    week_as_string = str(date.year)
    if last_week.month == 2 and last_week.day == 1:
        week_as_string = week_as_string + " Final"
    elif last_week.month == 8 and last_week.day == 1:
        week_as_string = week_as_string + " Preseason"
    else:
        week_as_string = last_week.strftime("%Y-%m-%d")

    for j in range(1,(len(rank_data))):
        try:
            if int(rank_data[j][5]) == team1Id and week_as_string == rank_data[j][1]:
                game_data[-4] = int(rank_data[j][2])
                game_data[-3] = float(rank_data[j][6])
                game_data_close_only[-4] = int(rank_data[j][2])
                game_data_close_only[-3] = float(rank_data[j][6])
            elif int(rank_data[j][5]) == team2Id and week_as_string == rank_data[j][1]:
                game_data[-2] = int(rank_data[j][2])
                game_data[-1] = float(rank_data[j][6])
                game_data_close_only[-2] = int(rank_data[j][2])
                game_data_close_only[-1] = float(rank_data[j][6])
            elif int(week_as_string.split(" ")[0].split("-")[0]) < int(rank_data[j][1].split(" ")[0].split("-")[0]):
                break
        except:
            pass

    game_data.insert(2, week_number)
    game_data_close_only.insert(2, week_number)
    
    final_data.append(game_data)
    final_data_close_only.append(game_data_close_only)

with open("data/sportsbookreviewsonline/ncaaf/processsed_data/sbro_ncaaf_with_ranks.csv", 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(final_data)

with open("data/sportsbookreviewsonline/ncaaf/processsed_data/sbro_ncaaf_close_only_with_ranks.csv", 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(final_data_close_only)



