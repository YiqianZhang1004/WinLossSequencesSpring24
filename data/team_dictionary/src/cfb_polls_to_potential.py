import json
import pandas as pd

df = pd.read_csv("data/college_poll_archive/processed_data/cfb_polls_trim.csv")
dictionary = json.load(open("data/team_dictionary/processed_data/sbro_to_cfbd_id.json","r"))
teams = df["Team"].to_list()
StandardID = []
not_assigned = []
for i in range(len(teams)):
    original_string = teams[i].strip()
    no_space = original_string.replace(" ","")
    if original_string in dictionary:
        StandardID.append(dictionary.get(original_string))
    elif (original_string+"U") in dictionary:
        StandardID.append(dictionary.get(original_string+"U"))
    elif no_space in dictionary:
        StandardID.append(dictionary.get(no_space))
    elif original_string == "Penn":
        StandardID.append(dictionary.get("Pennsylvania"))
    elif original_string == "Texas A&M":
        StandardID.append(dictionary.get("TexasA&M"))
    elif original_string == "Miami (FL)":
        StandardID.append(dictionary.get("MiamiFlorida"))
    elif original_string == "Miami (OH)":
        StandardID.append(dictionary.get("MiamiOhio"))
    elif original_string == "UCF":
        StandardID.append(dictionary.get("CentralFlorida"))
    else:
        StandardID.append("")
        not_assigned.append(original_string)
df2 = pd.DataFrame({"Date":df["Date"].to_list(),"Rank":df["Rank"].to_list(),"Team":teams,"TeamID":df["TeamID"].to_list(),"StandardID":StandardID,"Points":df["Points"].to_list()})
df2.to_csv("data/team_dictionary/processed_data/cfb_polls_standardized.csv")
pd.DataFrame(not_assigned).to_csv("data/team_dictionary/processed_data/not_assigned.csv")