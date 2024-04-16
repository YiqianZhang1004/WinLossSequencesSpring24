import pandas as pd

rows = []

for season in range(2007, 2021):
    df = pd.read_excel('sportsbookreviewsonline/ncaab/raw_data/sbro_ncaab_'+str(season)+'.xlsx')
    for i in range(0, len(df), 2):
        row1 = df.iloc[i]
        row2 = df.iloc[i+1]

        date = str(row1["Date"])
        processed_date = date
        if len(date) == 4:
            processed_date = str(season) + "-" + date[0:2] + "-" + date[2:]
        else:
            processed_date = str(season + 1) + "-0" + date[0:1] + "-" + date[1:]

        location = row1["VH"]

        homeRow = row1
        awayRow = row2
        if location == "V":
            homeRow = row2
            awayRow = row1

        team1 = homeRow["Team"]
        team2 = awayRow["Team"]

        score1 = homeRow["Final"]
        score2 = awayRow["Final"]

        moneyline1 = homeRow["ML"]
        moneyline2 = awayRow["ML"]

        rows.append({
            "season": str(season),
            'date': processed_date,
            'regular': location != "N",
            'team1': team1,
            'team2': team2,
            'score1': score1,
            'score2': score2,
            'moneyline1': moneyline1,
            'moneyline2': moneyline2
        })

games = pd.DataFrame(rows)

games.to_csv('sportsbookreviewsonline/ncaab/processed_data/sbrob.csv', index=False)
