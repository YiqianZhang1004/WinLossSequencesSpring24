# Sportsbook Reviews Online NCAAF Dataset Description

This dataset contains detailed information about College Football Data, including various aspects like game results, team information, and betting data. The data is taken from "sportsbookreviewsonline.com". The raw data includes game and betting data from the 2007 to the 2022 season. Below is a description of each column in the dataset: 

## Essential Data (game is not accounted for if any of this info is missing):
- **date**: The formatted date of the game.
- **season**: The year/season the game was played.
- **homeTeam**: Home team name.
- **awayTeam**: Away team name.
- **homeScore**: Home team's score.
- **awayScore**: Away team's score.
- **result**: Indicates the game result. 1 if the home team won, 0 if the away team won, 0.5 if the game was a draw. (not in original database and was calculated)

## Non-essential Data (invalid data is replaced with "NaN"):
- **spreadOpen**: The opening spread bet.
- **spreadClose**: The closing spread bet.
- **spreadHalf**: The spread bet at half time.
- **overUnderOpen**: The opening over under bet.
- **overUnderClose**: The closing over under bet.
- **overUnderHalf**: The over under bet at half time.
- **homeMoneyline**: The home team's moneyline bet.
- **awayMoneyline**: The away team's moneyline bet.

# Additional Notes:

- **Original Data Representation**: In the original dataset, games are represented by two consecutive rows. In the processed dataset, the rows were combined.
- **Betting Data Organization**: In the original dataset, the over under bet was placed on the row with the team with the negative moneyline, while the spread bet was placed on the row with the team with the positive moneyline. In the processed dataset, the spread and over under bets were correctly determined and organized accordingly. 
- **Neutral Games**: Neutral games were not accounted for in the processed dataset. 
- **Missing Betting Data**: Some games are missing certain betting data elements.
- **Typo in Original Data**: In the original dataset, the game between WashingtonU and California on November 2, 2012 (2012 season), the data is mistyped as 1192 instead of 1102. This is the only typo in the dataset and was dealt accordingly in the script. 
- **Unaccounted Games**: Some games are missing essential data and are added to a file called "sbro_ncaaf_error.csv".

