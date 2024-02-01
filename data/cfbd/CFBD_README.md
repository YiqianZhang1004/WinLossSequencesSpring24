# College Football Data Dataset Description

This dataset contains detailed information about College Football Data, including various aspects like game results, team information, and betting data. The data is taken from "collegefootballdata.com". The raw data includes exported game data from 1980 to 2023, betting line data from 2013 to 2023, and poll data from 1980 to 2023. The game data and the betting line data was first sorted by game ID to have a more efficient algorithm. Below is a description of each column in the dataset: 

## Essential Data (game is not accounted for if any of this info is missing):
- **id**: Unique integer ID of each game played.
- **date**: The formatted date of the game.
- **season**: The year/season the game was played.
- **team1**: Home team name.
- **team1ID**: ID of the home team.
- **team2**: Away team name.
- **team2ID**: ID of the away team.
- **score1**: Home team's score.
- **score2**: Away team's score.
- **result**: Indicates the game result. 1 if the home team won, 0 if the away team won, 0.5 if the game was a draw.

## Non-essential Data (invalid data is replaced with "NaN"):
- **homePostWinProb**: The probability that the home team wins.
- **awwayPostWinProb**: The probability that the away team wins. (complementary to the homePostWinProb)
- **homePreElo**: The elo rating of the home team before the game. (elo rating is based on chess elo, with a greater number indicating a stronger team)
- **homePostElo**: The elo rating of the home team after the game.
- **awayPreElo**: The elo rating of the away team before the game.
- **awayPostElo**: The elo rating of the away team after the game.
- **overUnder**: The over under bet for each game.
- **spread**: Predicted difference in points.
- **openingOverUnder**: The over under bet at the time of opening.
- **openingSpread**: The spread bet at the time of opening.
- **homeMoneyline**: The money line bet for the home team.
- **awayMoneyline**: The money line bet for the away team.
- **homeRank**: The AP Top 25 rank for the home team in that week.
- **homeVotes**: Home team's number of first place votes in the AP Top 25 poll for that week.
- **homePoints**: Home team's number of points in the AP Top 25 poll for that week.
- **awayRank**: The AP Top 25 rank for the away team in that week.
- **awayVotes**: Away team's number of first place votes in the AP Top 25 poll for that week.
- **awayPoints**: Away team's number of points in the AP Top 25 poll for that week.

## Additional Notes:

- **Seasons Prior to 2013**: The dataset does not contain betting line data for seasons before 2013.
- **Original Data Organization**: The 2023 season and seasons before 2002 do not include line/quarter scores for each team. 2009 include 5 line/quarter scores for each team (including overtime), the rest of the seasons include 4 line/quarter scores for each team.
- **Missing Betting Data**: Some games are missing certain betting data elements.
- **Multiple Sources and Averaging**: In cases where there are multiple sources with different betting data, the betting data is averaged to provide a single value.
- **Unaccounted Games**: Some games are missing essential data and are added to a file called "skipped.csv".

