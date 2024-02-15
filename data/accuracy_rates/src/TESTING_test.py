import csv

with open("data/cfbd/processed_data/cfbd_close_only.csv", "r") as file:
    cfbd = list(csv.reader(file))

with open("data/sportsbookreviewsonline/ncaaf/processsed_data/sbro_ncaaf_close_only_with_ranks.csv", "r") as file:
    sbro = list(csv.reader(file))

count = 0
predict = 0
predicted= []
for i in range(1, len(cfbd)):
    game = cfbd[i]
    if game[2] ==  "2021" or game[2] == "2020":
        count= count+1
        result = float(game[10])
        elo1 = float(game[13])
        elo2 = float(game[15])
       

        if i==39620:
            print(game)
            print(elo1)
        
        if elo1 != "nan":
            if i == 39620:
                print("hello")
            if elo1>elo2:
                if result == 1.0:
                    predicted.append(i)
                    predict+=1
            elif elo1 == elo2:
                if result == 0.5:
                    predicted.append(i)
                    predict+=1
            else:
                if result == 0.0:
                    predicted.append(i)
                    predict+=1

print(float("NaN"))

print(count)
print(predict)

if count!=0:
    print(predict/count)

with open("data/accuracy_rates/src/real_testing.csv", "w") as outfile:
    csv_writer = csv.writer(outfile)
    
    csv_writer.writerows([predicted])