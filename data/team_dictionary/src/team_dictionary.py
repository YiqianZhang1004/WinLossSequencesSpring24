import csv
import re
import json

def extract_capital_letters(input_string):
    capital_letters = ""
    for char in input_string:
        if char.isupper():
            capital_letters += char
    return capital_letters

teams = []
team_id=[]

with open("data/cfbd/processed_data/cfbd.csv", 'r') as games_file:
    games = list(csv.reader(games_file))

for game in games:
    team1 = game[4]
    team2 = game[6]
    team1ID = game[5]
    team2ID = game[7]
    if team1 not in teams:
        teams.append(team1)
        team_id.append(team1ID)
    if team2 not in teams:
        teams.append(team2)
        team_id.append(team2ID)



potential_names = {}

for i in range(2, len(teams)):
    potential=[]
    team = str(teams[i]).strip()
    potential.append(team.lower())
    if team.find(" ")!=-1:
        potential.append(team.replace(" ","").lower())
    if len(extract_capital_letters(team))>1:
        potential.append(extract_capital_letters(team).lower())
    if team.find(" State")!=-1:
        potential.append(team.replace(" State", "st").lower())
        potential.append(team.replace("State","st").lower())
    potential.append((team+"U").lower())
    potential_names[team_id[i]] = potential

with open("data/team_dictionary/processed_data/cfbd_id_to_potential.json", "w") as json_file:
    json.dump(potential_names, json_file,indent=4)

with open("data/sportsbookreviewsonline/ncaaf/processsed_data/sbro_ncaaf.csv", "r") as file:
    sbro = list(csv.reader(file))

sbro_ncaaf_teams = []
for i in range(1, len(sbro)):
    game = sbro[i]
    team1 = game[3]
    team2 = game[4]
    if team1 not in sbro_ncaaf_teams:
        sbro_ncaaf_teams.append(team1)
    if team2 not in sbro_ncaaf_teams:
        sbro_ncaaf_teams.append(team2)

found_teams = {}
unfound = []

for team in sbro_ncaaf_teams:
    found = False
    for key, value in potential_names.items():
        if team.lower() in value:
            found=True
            found_teams[team] = int(key)
            break
    if not found:
        unfound.append(team)


manual = {}
manual["MiamiOhio"] = 193
manual["ULMonroe"] = 2433
manual["MiamiFlorida"] = 2390
manual["NoIllinois"] = 2459
manual["SanJoseState"] = 23
manual["FloridaAM"] = 50
manual["FloridaIntl"] = 2229
manual["ULLafayette"] = 322
manual["MiddleTennSt"] = 2393
manual["Hawaii"] = 62
manual["GardnerWebb"] =2241
manual["Tenn.Martin"] = 2630
manual["NichollsSt"] = 2447
manual["LongIsland"] = 2341
manual["TexasAM"] = 245
manual["Cal.PolySLO"] = 13
manual["TexasA&MCommerce"] = 2837
manual["SamHoustonSt"] = 2534
manual["AlabamaAM"] = 2010
manual["ArkansasPineBluff"] = 2029
manual["UT-Chattanooga"] = 236
manual["St.Francis(PA)" ] = 2598
manual["NO.Colorado"] =2458
manual["EastTennesseeSt"] = 2193

for team in unfound:
    if team in manual:
        unfound.remove(team)

found_teams.update(manual)

with open("data/team_dictionary/processed_data/cfbd_id_to_sbro.json", "w") as file:
    json.dump(found_teams, file, indent=4)

print(unfound)
print(len(unfound))