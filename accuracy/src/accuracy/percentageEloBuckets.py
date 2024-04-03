import accuracyFunction
import matplotlib.pyplot as plt
import csv

eloDiffs = []

with open("combined/processed/combinedF.csv", "r") as file:
    games = csv.DictReader(file)
    for game in games:
        elo1 = game["homePreElo"]
        elo2 = game["awayPreElo"]

        if elo1 != "NaN" and elo2 != "NaN":
            diff = abs(float(elo1) - float(elo2))
            eloDiffs.append(diff)

eloDiffs = sorted(eloDiffs)


percentiles = [0]

for i in range(1, 20):
    index = int(i/20 *len(eloDiffs))
    percentiles.append(eloDiffs[index])

percentiles.append(eloDiffs[-1] + 1)


seasons = list(range(2007, 2024))

accuracies = []
binLabels = []

outList = [["bucket", "accuracy", "total", "over", "under"]]

for i in range(0, len(percentiles)-1):
    minPercentile = percentiles[i]
    maxPercentile = percentiles[i+1]

    tup = accuracyFunction.getAccuracy("m", seasons, [], [], [], [], [], "", "", minPercentile, maxPercentile)
    accuracies.append(tup[0])

    outList.append([str(minPercentile) + "-" + str(maxPercentile)] + list(tup))
    binLabels.append(str(minPercentile) + "-" + str(maxPercentile))



plt.bar(binLabels, accuracies, color="blue")
plt.xlabel('Buckets')
plt.ylabel('Accuracy Rates')
plt.title('Accuracy Rates Across Elo Difference Buckets (5% each)')
plt.xticks(rotation=45, ha='right')  
plt.tight_layout() 

plt.savefig('accuracy/visualizations/percentageEloBuckets.png')
plt.show()

with open("accuracy/visualization_data/percentageEloBuckets.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(outList)

