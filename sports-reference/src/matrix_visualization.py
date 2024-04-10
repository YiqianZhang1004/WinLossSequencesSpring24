import pandas as pd

df = pd.read_csv("sports-reference/raw_data/matchup_selector.csv")
data = []
for i in range(1,14):
    dftemp = df[(df.AwayRank == 2*i-1) | (df.AwayRank == 2*i)]
    # for every i, make a list of their winpct against every j
    iwinpct = []
    for j in range(1,13):
        dftemp2 = dftemp[(dftemp.HomeRank == 2*j-1) | (dftemp.HomeRank == 2*j)]
        results = dftemp2["Result"].to_list()
        winPct = sum(results) / len(results)
        iwinpct.append(winPct)
    data.append(iwinpct)
df2 = pd.DataFrame(data)
df2.to_csv("sports-reference/processed_data/matrix_visualization.csv")