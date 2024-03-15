import accuracy_rates
import matplotlib.pyplot as plt
import csv

seasons = list(range(2007, 2020))

accuracies = []

outList = [["bucket", "accuracy", "total", "over", "under"]]


for i in range(2, 10):
    tup = accuracy_rates.getAccuracy("m", seasons,[], [],[],[],[],i*100, (i+1)*100 - 1, -1,-1)
    accuracies.append(tup[0])

    outList.append([str(i*100) + "-" + str((i+1)*100 - 1)] + list(tup))


accuracies.append(accuracy_rates.getAccuracy("m", seasons, [],[],[],[],[],1000,1000000, -1, -1)[0])

bin_labels = [f'{i*100}-{(i+1)*100-1}' for i in range(2, 10)]
bin_labels.append('>1000')

plt.bar(bin_labels, accuracies, color="green")
plt.xlabel('Buckets')
plt.ylabel('Accuracy Rates')
plt.title('Accuracy Rates Across Moneyline Difference Buckets')
plt.xticks(rotation=45, ha='right')  
plt.tight_layout() 

plt.savefig('data/accuracy_rates/visualizations/moneylineBuckets.png')
plt.show()


with open("data/accuracy_rates/visualization_data/moneylineBuckets.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(outList)

