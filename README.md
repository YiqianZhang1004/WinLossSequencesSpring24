# Win Loss Sequences Spring 2024 Project

- Faculty Mentor: AJ Hildebrand.
- Project Leader: Bingyan Liu.
- IML Scholars: Yihan Gao, Sam Lam, David Xia.

## Directory Description

### CFBD

- Football game data from collegefootballdata.com.
- Game scores, teams, Elo, and win probabilities from 1980 to 2024.
- Betting data from 2013 to 2024.
- Polling data was added from college_poll_archive.

### sportsbookreviewsonline

- Football and basketball game data from sportsbookreviewsonline.com.
- Game scores, teams, betting data from 2007 to 2023.

### college_poll_archive

- Football and basketball poll data from collegepollarchive.com.
- Includes football ranks, votes, and points from 1936 to 2023.
- Includes basketball ranks, votes, and points from 1949 to 2024.

### team_dictionary

- Master dictionary that standardizes team names across multiple data sources.
- Team IDs from the CFBD source were used to standardize and match with team names in sportsbookreviewsonline.

### combined

- Combines the CFBD and sportsbookreviewsonline football data sources by matching respective games and compiling data.
- Polls and Elo are only found in the CFBD source, while betting data is found more ubiquitously in the sportsbookreviewsonline source.

### accuracy

- Analyzes the accuracy of different prediction methods throughout history.
- Determines the accuracy of (Elo/Moneyline/Poll) prediction over a specified set of games and plots the visualizations. 