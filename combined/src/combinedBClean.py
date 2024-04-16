import pandas as pd




df = pd.read_csv("combined/processed/combinedB.csv")

df["result"] = None

potential_missing = ["rank1",'rank2','points1','points2']

for index, row in df.iterrows():
    for d in potential_missing:
        if pd.isna(df.at[index,d]):
            df.at[index, d] = "NaN"

    if row["regular"] == "V":
        tempTeam = row['team1']
        tempScore = row['score1']
        tempML = row['moneyline1']
        tempRank = row['rank1']
        tempPoints = row['points1']

        df.at[index, 'team1'] = row['team2']
        df.at[index, 'score1'] = row['score2']
        df.at[index, 'moneyline1'] = row['moneyline2']
        df.at[index, 'rank1'] = row['rank2']
        df.at[index, 'points1'] = row['points2']

        df.at[index, 'team2'] = tempTeam
        df.at[index, 'score2'] = tempScore
        df.at[index, 'moneyline2'] = tempML
        df.at[index, 'rank2'] = tempRank
        df.at[index, 'points2'] = tempPoints

    score1 = row['score1']
    score2 = row['score2']

    if score1 > score2:
        df.at[index, 'result'] = 1
    else:
        df.at[index, 'result'] = 0

df.to_csv('combined/processed/combinedBClean.csv', index=False)
