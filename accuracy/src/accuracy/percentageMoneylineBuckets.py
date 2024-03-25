import accuracyFunction
import matplotlib.pyplot as plt
import csv

moneylineDiffs = []

with open("combined/processed/combinedF.csv", "r") as file:
    games = csv.DictReader(file)
    for game in games:
        moneyline1 = game["homeMoneyline"]
        moneyline2 = game["awayMoneyline"]

        if moneyline1 != "NaN" or moneyline2 != "NaN":
            diff = 0
            if moneyline1 == "NaN" :
                diff = 2*abs(float(moneyline2))
                moneylineDiffs.append(diff)
            elif moneyline2 == "NaN":
                diff = 2*abs(float(moneyline1))
                moneylineDiffs.append(diff)
            else:
                diff = abs(float(moneyline1) - float(moneyline2))
                moneylineDiffs.append(diff)

    



moneylineDiffs = sorted(moneylineDiffs)


percentiles = [0]

for i in range(1, 5):
    index = int(i/50 *len(moneylineDiffs))
    percentiles.append(moneylineDiffs[index])

percentiles.append(moneylineDiffs[-1])


seasons = list(range(2007, 2024))

accuracies = []
binLabels = []

outList = [["bucket", "accuracy", "total", "over", "under"]]

for i in range(0, len(percentiles)-1):
    minPercentile = percentiles[i]
    maxPercentile = percentiles[i+1]

    tup = accuracyFunction.getAccuracy("m", seasons, [], [], [], [], [], minPercentile, maxPercentile, "", "")
    accuracies.append(tup[0])

    outList.append([str(minPercentile) + "-" + str(maxPercentile)] + list(tup))
    binLabels.append(str(minPercentile) + "-" + str(maxPercentile))



plt.bar(binLabels, accuracies, color="green")
plt.xlabel('Buckets')
plt.ylabel('Accuracy Rates')
plt.title('Accuracy Rates Across Moneyline Difference Buckets (20% each)')
plt.xticks(rotation=45, ha='right')  
plt.tight_layout() 

plt.savefig('accuracy/visualizations/percentageMoneylineBuckets.png')
plt.show()

with open("accuracy/visualization_data/percentageMoneylineBuckets.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(outList)

