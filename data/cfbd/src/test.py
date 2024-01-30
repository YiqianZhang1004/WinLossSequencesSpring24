import csv

with open("data/cfbd/raw_data/x/2021_games.csv","r", newline='') as file:
    csv_data = list(csv.reader(file))
    print(len(csv_data))

with open("data/cfbd/raw_data/x/2021_bet.csv","r",newline = '') as file:
    csv_data = list(csv.reader(file))
    sorted_data = sorted(csv_data, key = lambda x: x[0])
    print(len(csv_data))

with open("data/cfbd/raw_data/x/random.csv", "w", newline='') as file:
    csv.writer(file).writerows(sorted_data)