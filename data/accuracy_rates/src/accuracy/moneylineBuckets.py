import accuracy_rates
import matplotlib.pyplot as plt


seasons = list(range(2007, 2020))

accuracies = []

for i in range(2, 10):

    accuracies.append(accuracy_rates.getAccuracy("m", seasons,[], [],[],[],[],i*100, (i+1)*100 - 1, -1,-1)[0])

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

