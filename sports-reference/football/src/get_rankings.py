import pandas as pd

df = pd.read_csv("sports-reference/football/raw_data/cfb_seasons.csv")
df['winnerRanking'] = df['winner'].str.extract(r'\((\d+)\)')
df['loserRanking'] = df['loser'].str.extract(r'\((\d+)\)')
df.drop("location", axis=1, inplace=True)
df = df.dropna()
df.to_csv("sports-reference/football/processed_data/cfb_games_with_ranks.csv")