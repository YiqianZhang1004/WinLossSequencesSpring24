import adjustedEloAccuracyFunction
import matplotlib.pyplot as plt

seasons = list(range(2007, 2024))
accuracies = []
labels = []

for i in range(0, 211, 10):
    e = adjustedEloAccuracyFunction.getAccuracy(seasons, [],[],[],[],[],'','','','',i)[0]
    labels.append(i)
    accuracies.append(e)

brier_scores = [
    0.18424832934722404, 0.18297634527832923, 0.1818986523495954, 0.18101510833940537, 0.1803251947898067,
    0.17982801925864234, 0.17952231886563144, 0.17940646512937214, 0.17947847008295695, 0.17973599364670437,
    0.1801763522276374, 0.18079652850694874, 0.1815931823689302, 0.18256266291778783, 0.18370102152246534,
    0.1850040258240449, 0.18646717463545603, 0.1880857136590293, 0.1898546519438042, 0.1917687790013569,
    0.19382268249617998, 0.19601076642426465
]

fig, ax1 = plt.subplots(figsize=(15, 7.5))

color = 'tab:blue'
ax1.set_xlabel('Home Adjustment', fontsize=50) 
ax1.set_ylabel('Accuracy', color=color, fontsize=50)
ax1.plot(labels, accuracies, color=color, marker='o', label='Accuracy', linewidth=5, markersize=10)
ax1.tick_params(axis='y', labelcolor=color, labelsize=30)

ax2 = ax1.twinx()  
color = 'tab:red'
ax2.set_ylabel('Brier Score', color=color, fontsize=50)
ax2.plot(labels, brier_scores, color=color, marker='s', label='Brier Score', linewidth=5, markersize=10)
ax2.tick_params(axis='y', labelcolor=color, labelsize=30)

ax1.tick_params(axis='x', labelsize=30)

fig.tight_layout()  

plt.savefig("accuracy/visualizations/presentation/eloAdjustmentWithBrierPresentation.png")
plt.show()
