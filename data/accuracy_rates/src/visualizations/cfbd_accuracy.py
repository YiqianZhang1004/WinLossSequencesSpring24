import accuracy_rates
import matplotlib.pyplot as plt

seasons = []
elo_accuracy = []
elo_num = []
moneyline_accuracy = []
moneyline_num =[]
poll_accuracy = []
poll_num = []

for season in range(1980, 2024):
    seasons.append(season)

    elo_rate = accuracy_rates.get_accuracy("cfbd", "elo", [season], -1, -1, -1, -1, "", "")
    moneyline_rate = accuracy_rates.get_accuracy("cfbd", "moneyline", [season],-1,-1,-1,-1, "", "")
    poll_rate = accuracy_rates.get_accuracy("cfbd", "poll", [season], -1, -1, -1, -1, "", "")

    if elo_rate == "no games":
        elo_accuracy.append(None)
        elo_num.append(None)
    else:
        elo_accuracy.append(float(elo_rate.split(" ")[4].replace("%","")))
        elo_num.append(int(elo_rate.split(" ")[6]))

    if moneyline_rate == "no games":
        moneyline_accuracy.append(None)
        moneyline_num.append(None)
    else:
        moneyline_accuracy.append(float(moneyline_rate.split(" ")[4].replace("%","")))
        moneyline_num.append(int(moneyline_rate.split(" ")[6]))


    if poll_rate == "no games":
        poll_accuracy.append(None)
        poll_num.append(None)
    else:
        poll_accuracy.append(float(poll_rate.split(" ")[4].replace("%","")))
        poll_num.append(int(poll_rate.split(" ")[6]))

elo_line, = plt.plot(seasons, elo_accuracy, label='Elo', color='blue')
for i, txt in enumerate(elo_num):
    if txt is not None:
        plt.text(seasons[i], elo_accuracy[i], str(txt), fontsize=8, color='blue', ha='center', va='bottom')

moneyline_line, = plt.plot([], [], label='Moneyline', color='green')  
plt.plot(seasons, moneyline_accuracy, color='green')
for i, txt in enumerate(moneyline_num):
    if txt is not None:
        plt.text(seasons[i], moneyline_accuracy[i], str(txt), fontsize=8, color='green', ha='center', va='bottom')

poll_line, = plt.plot([], [], label='Poll', color='red') 
plt.plot(seasons, poll_accuracy, color='red')
for i, txt in enumerate(poll_num):
    if txt is not None:
        plt.text(seasons[i], poll_accuracy[i], str(txt), fontsize=8, color='red', ha='center', va='bottom')

plt.xlabel('Season')
plt.ylabel('Accuracy')
plt.title('CFBD Accuracy of Methods Over the Years')
plt.legend()
plt.legend(handles=[elo_line, moneyline_line, poll_line])
plt.grid(True)

plt.savefig(r'data\accuracy_rates\visualizations\cfbd_accuracy.png')
plt.show()



