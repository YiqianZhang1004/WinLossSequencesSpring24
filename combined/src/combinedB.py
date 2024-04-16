import pandas as pd
import json
from datetime import datetime


games = pd.read_csv("sportsbookreviewsonline/ncaab/processed_data/sbrob.csv")
ranks = pd.read_csv("college_poll_archive/processed_data/cbb_2007_to_2021.csv")


with open("team_dictionary/processed_data/SBROBtoCPA.json", "r") as json_file:
    dict = json.load(json_file)


games["rank1"] = None
games["rank2"] = None
games["points1"] = None
games["points2"] = None


dates = []
for index, row in ranks.iterrows():
    date = row["Date"]
    if "Final" in date:
        date = date[0:4] + "-06-01"
    elif "Preseason" in date:
        date = str(int(date[0:4])-1) + "-07-01"

    if date not in dates:
        dates.append(date)

for i in range(len(dates)):
    dates[i] = datetime.strptime(dates[i], '%Y-%m-%d')
    

sorted = sorted(dates)

for index, row in games.iterrows():
    print(index)
    date = row["date"]
    date = datetime.strptime(date, '%Y-%m-%d')
    previous_index = 0
    while previous_index < len(sorted) and sorted[previous_index] < date:
        previous_index = previous_index + 1
    previous_index = previous_index - 1

    previous_date = sorted[previous_index]
    date_string = previous_date.strftime('%Y-%m-%d')
    if previous_date.month == 6:
        date_string = str(previous_date.year) + " Final"
    elif previous_date.month == 7:
        date_string = str(previous_date.year + 1) + " Preseason"
    

    team1 = row["team1"]
    team2 = row["team2"]
    team1_id = dict[team1]
    team2_id = dict[team2]    

    if team1_id != -1:
        for i, r in ranks.iterrows():
            if r["Date"] == date_string and str(r["TeamID"]) == str(team1_id):
                games.at[index, 'rank1'] = r["Rank"]
                games.at[index, 'points1'] = r["Points"]
    if team2_id != -1:
        for i, r in ranks.iterrows():
            if r["Date"] == date_string and str(r["TeamID"]) == str(team2_id):
                games.at[index, 'rank2'] = r["Rank"]
                games.at[index, 'points2'] = r["Points"]

games.to_csv('combined/processed/combinedB.csv', index=False)

    

