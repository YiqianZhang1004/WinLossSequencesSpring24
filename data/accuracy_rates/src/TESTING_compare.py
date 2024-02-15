import csv
with open("data/accuracy_rates/src/testing.csv", "r") as file:
    function = list(csv.reader(file))[0]

with open("data/accuracy_rates/src/real_testing.csv", "r") as file:
    real = list(csv.reader(file))[0]

with open("data/cfbd/processed_data/cfbd_close_only.csv", "r") as file:
    cfbd = list(csv.reader(file))

with open("data/sportsbookreviewsonline/ncaaf/processsed_data/sbro_ncaaf_close_only_with_ranks.csv", "r") as file:
    sbro = list(csv.reader(file))

diff = []
for i in real:
    if i not in function:
        diff.append(i)
print(cfbd[0])
for i in diff:
    print(cfbd[int(i)])

print(diff)