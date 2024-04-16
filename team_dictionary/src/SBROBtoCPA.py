from fuzzywuzzy import process
import pandas as pd
import json


games = pd.read_csv("sportsbookreviewsonline/ncaab/processed_data/sbrob.csv")
ranks = pd.read_csv("college_poll_archive/processed_data/cbb_polls_trim.csv")

sbroTeams = []

for index, row in games.iterrows():
    team1 = row["team1"]
    team2 = row["team2"]

    if team1 not in sbroTeams:
        sbroTeams.append(team1)

    if team2 not in sbroTeams:
        sbroTeams.append(team2)

cpaDict = {}
for index, row in ranks.iterrows():
    team = row["Team"]
    id = row["TeamID"]

    if team not in cpaDict.keys():
        cpaDict[team] = id


sbroToCPA = {}
unfound = []
for team in cpaDict.keys():
    best, score = process.extractOne(team, sbroTeams)
    if score >= 80:
        sbroToCPA[best] = cpaDict[team]
    else:
        unfound.append(team)
    
sbroToCPA["Tennessee"] = -1
sbroToCPA["Florida"] = -1
sbroToCPA["NewOrleansU"] = -1
sbroToCPA["MiamiOhio"] = 84
sbroToCPA["MiamiFlorida"] = 122
sbroToCPA["VaCommonwealth"] = 173
sbroToCPA["WiscGreenBay"] = 184
sbroToCPA["CentralFlorida"] = 208

for team in sbroTeams:
    if team not in sbroToCPA.keys():
        sbroToCPA[team] = -1


with open("team_dictionary/processed_data/SBROBtoCPA.json", "w") as json_file:
    json.dump(sbroToCPA, json_file, indent=4)

