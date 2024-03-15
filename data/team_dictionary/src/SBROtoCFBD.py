from fuzzywuzzy import process
import csv
import json

CFBDnames = []
CFBDnameToID = {}

with open("data/cfbd/processed_data/cfbd.csv", "r") as file:
    games = csv.DictReader(file)
    for game in games:
        if game["homeTeam"] not in CFBDnames:
            CFBDnames.append(game["homeTeam"])
            CFBDnameToID[game["homeTeam"]] = game["homeID"]
        if game["awayTeam"] not in CFBDnames:
            CFBDnames.append(game["awayTeam"])
            CFBDnameToID[game["awayTeam"]] = game["awayID"]

SBROnames = []

with open("data/sportsbookreviewsonline/ncaaf/processsed_data/sbro_ncaaf.csv", "r") as file:
    games = csv.DictReader(file)
    for game in games:
        if game["homeTeam"] not in SBROnames:
            SBROnames.append(game["homeTeam"])
        if game["awayTeam"] not in SBROnames:
            SBROnames.append(game["awayTeam"])

SBROtoCFBD = {}


threshold = 80
for name in SBROnames:
    best, score = process.extractOne(name, CFBDnames)

    if score >= threshold:
        SBROtoCFBD[name] = CFBDnameToID[best]

SBROtoCFBD["ULMonroe"] = 2433
SBROtoCFBD["MiddleTennSt"] = 2393
SBROtoCFBD["SoMississippi"] = 2572
SBROtoCFBD["WeberSt"] = 2692
SBROtoCFBD["BOISEST"] = 68
SBROtoCFBD["SoCarolinaSt"] = 2569
SBROtoCFBD["CSSacramento"] = 16
SBROtoCFBD["ArkPineBluff"] = 2029
SBROtoCFBD["Massachusetts"] = 113
SBROtoCFBD["TennChat"] = 236
SBROtoCFBD["UTSA"] = 2636
SBROtoCFBD["DixieState"] = 3101
SBROtoCFBD["StThomas"] = 2900

with open("data/team_dictionary/processed_data/SBROtoCFBD.json", 'w') as json_file:
    json.dump(SBROtoCFBD, json_file, indent=4)

