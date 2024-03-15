import pandas as pd
import re
from datetime import datetime
cfb = pd.read_csv("college_poll_archive/raw_data/combined_cfb_poll_data.csv")
cbb = pd.read_csv("college_poll_archive/raw_data/combined_cbb_poll_data.csv")
cfb_teams = cfb["Team (FPV)"].to_list()
for i in range(len(cfb_teams)):
    new_string = re.sub("\\(\\d+\\)$","",cfb_teams[i])
    new_string = re.sub(r"\(\d+\.\d+\)","",new_string)
    cfb_teams[i] = new_string
cbb_teams = cbb["Team (FPV)"].to_list()
for i in range(len(cbb_teams)):
    new_string = re.sub("\\(\\d+\\)$","",cbb_teams[i])
    cbb_teams[i] = new_string
cfb = cfb[["Date","Rank","TeamID","Points"]]
cbb = cbb[["Date","Rank","TeamID","Points"]]
cfb["Team"] = cfb_teams
cbb["Team"] = cbb_teams

def formatDatesCBB(date_string):
    if "Preseason" in date_string:
        return date_string
    elif "Final" in date_string:
        return date_string
    date_object = datetime.strptime(date_string, "%B %d, %Y")
    if date_object.year > 2022:  # Assuming current year is 2022
        date_object = date_object.replace(year=date_object.year - 100)
    return date_object.strftime("%Y-%m-%d")
cbb["Date"] = cbb["Date"].apply(formatDatesCBB)

def formatDatesCFB(date_string):
    if "Preseason" in date_string:
        return date_string
    elif "Final" in date_string:
        return date_string
    date_object = datetime.strptime(date_string, "%B %d, %Y")
    if date_object.year > 2022:  # Assuming current year is 2022
        date_object = date_object.replace(year=date_object.year - 100)
    return date_object.strftime("%Y-%m-%d")
cfb["Date"] = cfb["Date"].apply(formatDatesCFB)

cfb.to_csv("college_poll_archive/processed_data/cfb_polls_trim.csv")
cbb.to_csv("college_poll_archive/processed_data/cbb_polls_trim.csv")