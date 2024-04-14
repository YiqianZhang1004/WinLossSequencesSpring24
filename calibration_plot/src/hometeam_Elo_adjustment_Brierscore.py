import matplotlib.pyplot as plt

# Data
values_added = list(range(0, 211, 10))
brier_scores = [
    0.18424832934722404, 0.18297634527832923, 0.1818986523495954, 0.18101510833940537, 0.1803251947898067,
    0.17982801925864234, 0.17952231886563144, 0.17940646512937214, 0.17947847008295695, 0.17973599364670437,
    0.1801763522276374, 0.18079652850694874, 0.1815931823689302, 0.18256266291778783, 0.18370102152246534,
    0.1850040258240449, 0.18646717463545603, 0.1880857136590293, 0.1898546519438042, 0.1917687790013569,
    0.19382268249617998, 0.19601076642426465
]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(values_added, brier_scores, marker='o', color='b', linestyle='-')
plt.title('Adjusted Brier Score vs Values Added to homePreElo')
plt.xlabel('Values Added to homePreElo')
plt.ylabel('Adjusted Brier Score')
plt.grid(True)
plt.xticks(values_added)
plt.show()