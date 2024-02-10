import csv
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
        potential.append(team.replace(" State", " st").lower())
        potential.append(team.replace("State","st").replace(" ","").lower())
    potential.append((team+"U").lower())
    if team.find(" A&M")!=-1:
        potential.append(team.replace(" A&M","am").lower())
    potential.append(team.replace("-","").replace(" ","").lower())
    if team.find("Northern ")!=-1:
        potential.append(team.replace("Northern ", "no").lower())
    if team.find("Southern ")!=-1:
        potential.append(team.replace("Southern ", "so").lower())
    if team.find("North ")!=-1:
        potential.append(team.replace("North ", "no").replace(" ","").lower())
    if team.find("South ")!=-1:
        potential.append(team.replace("South ","so").replace(" ","").lower())
    if team.find("-")!=-1:
        potential.append(team.replace("-","").lower())

    potential_names[int(team_id[i])] = potential


with open("data/team_dictionary/processed_data/cfbd_id_to_potential.json", "w") as json_file:
    json.dump(potential_names, json_file,indent=4)