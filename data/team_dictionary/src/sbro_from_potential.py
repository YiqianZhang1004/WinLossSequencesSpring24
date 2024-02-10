import csv
import json

with open("data/team_dictionary/processed_data/cfbd_id_to_potential.json","r") as file:
    potential_names = json.load(file)

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
unautomatic = []

for team in sbro_ncaaf_teams:
    found = False
    for key, value in potential_names.items():
        if team.lower() in value:
            found=True
            found_teams[team] = int(key)
            break
    if not found:
        unautomatic.append(team)


manual = {}
manual["MiamiOhio"] = 193
manual["MiamiFlorida"] = 2390

manual["UL-Monroe"] = 2433
manual["ULMonroe"] = 2433

manual["MiddleTennSt"] = 2393
manual["MiddleTennesseeState"] = 2393
manual["MidTennesseeState"] = 2393

manual["NichollsSt"] = 2447
manual["NichollsState"] = 2884

manual["TennChat"] = 236
manual["UT-Chattanooga"] = 236

manual["St.ThomasMinn"] = 2900
manual["St.Thomas-Minn"] = 2900

manual["SouthernMiss"] = 2572
manual["SanJoseState"] = 23
manual["Hawaii"] = 62
manual["FloridaIntl"] = 2229
manual["ULLafayette"] = 322
manual["GardnerWebb"] =2241
manual["Tenn.Martin"] = 2630
manual["LongIsland"] = 2341
manual["Cal.PolySLO"] = 13
manual["CentralConn."] = 2115
manual["St.Francis(PA)" ] = 2598
manual["NO.Colorado"] =2458
manual["Kent"] = 2309
manual["Mississippi"] = 145
manual["SELouisiana"] = 2545
manual["NCCentral"] = 2428
manual["EastWashington"] = 331
manual["CentralFlorida"] = 2116
manual["SEMissouriSt"] = 2546
manual["McNeeseSt"] = 2377
manual["Presbyterian"] = 2506
manual["CSSacramento"] = 16
manual["ArkPineBluff"] = 2029
manual["Massachusetts"] = 113
manual["CharlestonSou"] = 2127
manual["SoCarolinaSt"] = 2569
manual["TennesseeMartin"] = 2630
manual["TexSanAntonio"] = 2636
manual["Miss.ValleySt"] = 2400
manual["N.CarolinaA&T"] = 2448
manual["HoustonBaptist"] = 2277
manual["N.CarolinaAT"] = 2448
manual["WilliamMary"] = 2729
manual["DixieState"]=3101
manual["StThomas"] = 125730
manual["VirginiaMilitary"] = 2678
manual["PortlandSt."] = 2502

unfound = [["team"]]
for team in unautomatic:
    if team not in manual:
        print(team)
        unfound.append([team])

found_teams.update(manual)



with open("data/team_dictionary/processed_data/sbro_to_cfbd_id.json", "w") as file:
    json.dump(found_teams, file, indent=4)

with open("data/team_dictionary/processed_data/sbro_unfound.csv", 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(unfound)