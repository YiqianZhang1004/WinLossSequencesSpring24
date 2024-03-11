import accuracy_rates
import matplotlib.pyplot as plt


seasons = list(range(2007, 2020))

accuracies = []

for i in range(0, 10):

    accuracies.append(accuracy_rates.getAccuracy("e", seasons, [],[],[],[],[],-1, -1, i*100,(i+1)*100 -1,"","")[0])

accuracies.append(accuracy_rates.getAccuracy("e", seasons,[], [],[],[],[],-1,-1, 1000, 10000000, "", "")[0])

bin_labels = [f'{i*100}-{(i+1)*100-1}' for i in range(0, 10)]
bin_labels.append('>1000')

plt.bar(bin_labels, accuracies, color="blue")
plt.xlabel('Buckets')
plt.ylabel('Accuracy Rates')
plt.title('Accuracy Rates Across Elo Difference Buckets')
plt.xticks(rotation=45, ha='right')  
plt.tight_layout() 

plt.savefig('data/accuracy_rates/visualizations/eloBuckets.png')
plt.show()

