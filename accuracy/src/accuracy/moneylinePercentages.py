import accuracyFunctionPositiveMoneylines
import matplotlib.pyplot as plt

seasons = list(range(2007, 2024))

accuracies = []
labels = []
expected = []


for i in range(1, 11):
    lower = i * 100
    upper = lower + 99
    label = lower + 50
    labels.append(label)
    result = accuracyFunctionPositiveMoneylines.getAccuracy(seasons, lower, upper)
    accuracies.append(result[0])
    expected.append(100 * 100/(label+100))


plt.plot(labels, accuracies, color='green', label='Actual Win Rate')
plt.plot(labels, expected, color='red', label='Expected Win Rate')

plt.xlabel("Positive Moneyline Score")
plt.ylabel("Win Rate (%)")
plt.legend()
plt.savefig('accuracy/visualizations/moneylinePercentages.png')
plt.savefig('accuracy/visualizations/presentation/moneylinePercentagesPresentation.png')

plt.show()


