import csv
import re
import json

seasons = []
for i in range(1980, 2024):
    seasons.append(i)

def get_away_index(season):
    if season == 2009:
        return 26
    elif season == 2023 or season <= 2001:
        return 22
    else:
        return 25

teams = []
team_id=[]

for season in seasons:
    with open("data/cfbd/raw_data/sorted_games/sorted_"+str(season)+"_games.csv", 'r') as games_file:
        games = list(csv.reader(games_file))
    
    for game in games:
        team1 = game[13]
        team2 = game[get_away_index(season)]
        team1ID = game[12]
        team2ID = game[get_away_index(season)-1]
        if team1 not in teams:
            teams.append(team1)
            team_id.append(team1ID)
        if team2 not in teams:
            teams.append(team2)
            team_id.append(team2ID)



potential_names = {}

for i in range(len(teams)):
    potential = []
    team = str(teams[i]).strip()
    team = team.replace("&","")

    potential.append(team.lower())
    if team.find(" ")!= -1:
        potential.append(team.replace(" ","").lower())

    potential.append((team+"u").lower())

    potential.append(team.replace(" State","st").lower())

    potential.append(team.replace("Northern ", "no").lower())
    potential.append(team.replace("Southern ", "so").lower())
    potential.append(team.replace("i'i",'ii').lower())

    potential.append(team.replace("Miami (OH)", "MiamiOhio").lower())
    potential.append(team.replace("Miami","MiamiFlorida").lower())

    
    pattern = r"\([^()]*\)"

    without = re.sub(pattern, "",team)

    potential.append(without.lower())

    potential.append(without.replace(" ","").lower())

    capital_letters = [char for char in team if char.isupper()]

    potential.append(("".join(capital_letters)).lower())
    capital_letters = [char for char in without if char.isupper()]

    potential.append(("".join(capital_letters)).lower())

    potential_names[team_id[i]] = potential

with open("data/team_dictionary/processed_data/cfbd_id_to_potential.json", "w") as json_file:
    json.dump(potential_names, json_file,indent=4)

with open("data/sportsbookreviewsonline/ncaaf/processsed_data/sbro_ncaaf.csv", "r") as file:
    sbro = list(csv.reader(file))

sbro_ncaaf_teams = []
for game in sbro:
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
            found_teams[key] = team
            break
    if not found:
        unfound.append(team)

with open("data/team_dictionary/processed_data/cfbd_id_to_sbro.json", "w") as file:
    json.dump(found_teams, file, indent=4)

print(unfound)
print(len(unfound))