import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("calibration_plot/data/elo_moneyline_prob.csv")
bins = [0.1 * i for i in range(11)]

df['P_Homewins_Elo_group'] = pd.cut(df["P Homewins Elo"], bins=bins, labels=[f"{i / 10}-{(i + 1) / 10}" for i in range(10)])
df['MoneylineProb_group'] = pd.cut(df["MoneylineProb"], bins=bins, labels=[f"{i / 10}-{(i + 1) / 10}" for i in range(10)])


grouped_P_Homewins_Elo = df.groupby('P_Homewins_Elo_group')['result'].mean().reset_index()
grouped_MoneylineProb = df.groupby('MoneylineProb_group')['result'].mean().reset_index()

plt.figure(figsize=(22, 11))
plt.plot(range(10), grouped_MoneylineProb['result'], marker='s', linestyle='-', color='g', label='Betting Market', linewidth=5, markersize=10)
plt.plot(range(10), [(i + 1) / 10 for i in range(10)], linestyle='--', color='k', label='Perfect Calibration', linewidth=5, markersize=10)
plt.xlabel('Predicted Win Probability', fontsize=40)
plt.ylabel('Actual Frequency', fontsize=40)
plt.legend(fontsize=30)
plt.xticks(range(10), [f'{i * 0.1:.1f}' for i in range(10)], fontsize=30) 
plt.yticks([i * 0.1 for i in range(11)], [f'{i * 0.1:.1f}' for i in range(11)], fontsize=30) 
plt.grid(True)

plt.savefig("calibration_plot/calibration.png")
plt.show()