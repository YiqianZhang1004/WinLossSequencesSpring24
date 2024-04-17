import accuracyFunction
import matplotlib.pyplot as plt
import csv
import numpy as np

seasons = list(range(2007, 2024))

accuracies = []

outList = [["bucket", "accuracy", "total", "over", "under"]]


for i in range(2, 10):
    tup = accuracyFunction.getAccuracy("m", seasons,[], [],[],[],[],i*100, (i+1)*100 - 1, '','')
    accuracies.append(tup[0])

    outList.append([str(i*100) + "-" + str((i+1)*100 - 1)] + list(tup))


accuracies.append(accuracyFunction.getAccuracy("m", seasons, [],[],[],[],[],1000,1000000, '','')[0])

bin_labels = [f'{i*100}-{(i+1)*100-1}' for i in range(2, 10)]
bin_labels.append('>1000')

plt.bar(bin_labels, accuracies, color="green")
plt.xlabel('Buckets')
plt.ylabel('Accuracy Rates')
plt.title('Accuracy Rates Across Moneyline Difference Buckets')
plt.xticks(rotation=45, ha='right')  
plt.tight_layout() 

plt.savefig('accuracy/visualizations/moneylineBuckets.png')
plt.show()

with open("accuracy/visualization_data/moneylineBuckets.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(outList)


plt.close()
labels = [200,300,400,500,600,700,800,900,1000]
plt.scatter(labels, accuracies)
plt.xlabel("Bucket Thresholds")
plt.ylabel("Accuracy Rate (%)")

slope, intercept = np.polyfit(labels, accuracies, 1)
plt.plot(labels, np.polyval([slope, intercept], labels), color='red', label='Linear Regression')

equation_text = f'y = {slope:.2f}x + {intercept:.2f}'
plt.annotate(equation_text, xy=(labels[0], accuracies[0]), xytext=(labels[0]+0.5, max(accuracies)), verticalalignment='top')

plt.savefig('accuracy/visualizations/moneylineRegression.png')
plt.savefig('accuracy/visualizations/presentation/moneylineRegressionPresentation.png')


plt.show()


