import accuracy_rates
import matplotlib.pyplot as plt

weeks = []
m=[]
e=[]
for i in range(1,21):
    weeks.append(i)
    mr = accuracy_rates.getAccuracy("m",[],[i],[],[],[],[],-1,-1,-1,-1,"","")
    er = accuracy_rates.getAccuracy("e",[],[i],[],[],[],[],-1,-1,-1,-1,"","")

    if mr == (0,0,0,0):
        m.append(None)
    else:
        m.append(float(mr[0]))
    if er == (0,0,0,0):
        e.append(None)
    else:
        e.append(float(er[0]))

    
plt.plot(weeks, e, color="blue", label = "Elo")
plt.plot(weeks, m, color="green", label = "Moneyline")

plt.xlabel('Week')
plt.ylabel('Accuracy')
plt.title('Elo and Moneyline Accuracy By Week')
plt.legend()
plt.grid(True)

plt.savefig('data/accuracy_rates/visualizations/emWeek.png')
plt.show()
