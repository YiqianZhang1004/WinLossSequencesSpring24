import csv
import matplotlib.pyplot as plt

lineProviders =[]

seasons = []

for i in range(2013, 2024):
    seasons.append(i)
    with open("cfbd/raw_data/lines/"+str(i)+"_lines.csv","r") as bets_file:
        bets = csv.DictReader(bets_file)
        for line in bets:
            provider = line["LineProvider"]
            if provider not in lineProviders:
                lineProviders.append(provider)



data = []

for provider in lineProviders:
    providerData = []
    for season in seasons:
        count = 0
        with open("cfbd/raw_data/lines/"+str(i)+"_lines.csv","r") as bets_file:
            bets = csv.DictReader(bets_file)
            for line in bets:
                p = line["LineProvider"]
                if provider ==p:
                    count = count + 1
        providerData.append(count)
    data.append(providerData)


for i in range(len(data)):
    providerData = data[i]
    plt.plot(seasons, providerData, label = lineProviders[i])

plt.xlabel('Season')
plt.ylabel('Frequency')
plt.title('CFBD Line Provider Frequency')
plt.legend()

plt.savefig("cfbd/processed_data/lineProviderFrequency")

plt.show()

