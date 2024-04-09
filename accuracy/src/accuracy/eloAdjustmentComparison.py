import adjustedEloAccuracyFunction
import matplotlib.pyplot as plt

seasons = list(range(2007, 2024))
accuracies = []
labels = []

for i in range(0, 200):
    e = adjustedEloAccuracyFunction.getAccuracy(seasons, [],[],[],[],[],'','','','',i)[0]
    labels.append(i)
    accuracies.append(e)



plt.plot(labels, accuracies, color = "blue")

plt.xlabel("Home Adjustment")
plt.ylabel("Accuracy")
plt.title("Accuracies of Different Home Team Adjustments")

plt.savefig("accuracy/visualizations/display/eloAdjustmentComparisonDisplay.png")
plt.show()
