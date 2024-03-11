import csv
import json
from datetime import datetime

dateToWeekDictionary = {}

with open("data/team_dictionary/processed_data/cfb_polls_standardized.csv", "r") as file:
    polls = list(csv.reader(file))

dates = []
weeks = []

for i in range(1, len(polls)):
    week = polls[i][1]
    year = week.split(" ")[0].split("-")[0]
    if week.find("Preseason") !=-1:
        date = datetime.strptime(year + "-08-01", "%Y-%m-%d")
        if date not in dates:
            dates.append(date)
            weeks.append(year)
    elif week.find("Final")!=-1:
        date = datetime.strptime(str(int(year)+1) + "-02-01","%Y-%m-%d")
        if date not in dates:
            dates.append(date)
            weeks.append(year)
    else:
        date = datetime.strptime(week, "%Y-%m-%d")
        if date not in dates:
            dates.append(date)
            weeks.append(year)

dates = sorted(dates)
weeks = sorted(weeks)

counts = {}
mapped_list = []

for item in weeks:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1
    mapped_list.append(counts[item])

for i in range(len(dates)):
    dateToWeekDictionary[dates[i].strftime('%Y-%m-%d')] = mapped_list[i]

with open("data/sportsbookreviewsonline/ncaaf/processsed_data/dateToWeek.json", 'w') as json_file:
    json.dump(dateToWeekDictionary, json_file, indent=4)