import csv
with open("data/combined_football/processed/combined.csv", "r") as file:
    games = list(csv.reader(file))

count = 0
for i in range(1,len(games)):
    game = games[i]
    if game[3] == "8":
        count=count+1
print(count)