# College Football Data Dataset Description

This dataset contains detailed information about College Football Data, including various aspects like game results, team information, and betting data. Below is a description of each column in the dataset:

- **id**: Unique integer ID of each game played.
- **date**: The date the game took place, formatted.
- **season**: The year/season the game was played.
- **team1**: Home team.
- **team1ID**: ID of the home team.
- **team2**: Away team.
- **team2ID**: ID of the away team.
- **score1**: Home team's score.
- **score2**: Away team's score.
- **result**: Indicates the game result. 1 if the home team won, 0 if the away team won, 0.5 if the game was a draw.
- **spread**: Predicted difference in points.
- **spreadOpen**: ?
- **overUnder**: Over/under for each game.
- **overUnderOpen**: ?
- **homeMoneyline**: Betting line for the home team.
- **awayMoneyline**: Betting line for the away team.

## Additional Notes:

- **Seasons Prior to 2013**: The dataset does not contain betting line data for seasons before 2013.
- **Missing Betting Data**: Some games are missing certain betting data elements.
- **Multiple Sources and Averaging**: In cases where there are multiple sources with different betting data, the betting data is averaged to provide a single value.
