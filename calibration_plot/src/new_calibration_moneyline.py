import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("elo_moneyline_prob.csv")
bins = [0.1 * i for i in range(11)]

df['P_Homewins_Elo_group'] = pd.cut(df["P Homewins Elo"], bins=bins, labels=[f"{i / 10}-{(i + 1) / 10}" for i in range(10)])
df['MoneylineProb_group'] = pd.cut(df["MoneylineProb"], bins=bins, labels=[f"{i / 10}-{(i + 1) / 10}" for i in range(10)])


grouped_P_Homewins_Elo = df.groupby('P_Homewins_Elo_group')['result'].mean().reset_index()
grouped_MoneylineProb = df.groupby('MoneylineProb_group')['result'].mean().reset_index()

l = [0.05, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.95]
l2 = [0.1, 0.2,0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
# plt.plot(l, grouped_P_Homewins_Elo['result'], marker='o', linestyle='-', color='b', label='Elo Rating')
plt.plot(l, grouped_MoneylineProb['result'], marker='s', linestyle='-', color='g', label='Moneyline') 
plt.plot(l2, [(i + 1) / 10 for i in range(10)], linestyle='--', color='k', label='Perfect Calibration')
plt.xlabel('Predicted Win Probability')
plt.ylabel('Actual Frequency of Wins')
plt.title('') #'Accuracy of Probabilistic Predictions'
plt.legend()
#plt.xticks(rang, [f'{i * 0.1:.1f}' for i in range(10)]) 
plt.xticks([i * 0.1 for i in range(11)], [f'{i * 0.1:.1f}' for i in range(11)])
plt.yticks([i * 0.1 for i in range(11)], [f'{i * 0.1:.1f}' for i in range(11)]) 
plt.grid(True)
plt.show()