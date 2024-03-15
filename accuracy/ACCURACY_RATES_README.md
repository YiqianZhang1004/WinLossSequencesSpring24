# Accuracy Rate Description

This function calculates the accuracy rate of college football game predictions based on various factors such as Elo rankings, moneylines, and poll rankings. Users can specify the source of data (cfbd or sbro), the prediction method (elo, moneyline, or poll), and filter games based on specific criteria.

## get_accuracy() Parameters

- **source**: 
  - "cfbd": CollegeFootballData.com
  - "sbro": SportsBookReviewsOnline.com

- **method**:
  - "elo": Pre-match Elo rankings (cfbd only)
  - "moneyline": Moneyline bets
  - "poll": Poll rankings

- **seasons_list**: 
  - List of seasons (as integers) to search through

- **arg_team_id1**: 
  - Restricts to games with a specific home team playing. Use -1 to search for any home team.

- **arg_team_id2**: 
  - Restricts to games with a specific away team playing. Use -1 to search for any away team.

- **arg_rank1**: 
  - Restricts to games with a specific home rank playing. Use -1 to search for any home rank.

- **arg_rank2**: 
  - Restricts to games with a specific away rank playing. Use -1 to search for any away rank.

- **success_file**:
  - Name of file to save correctly predicted games to

- **fail_file**:
  - Name of file to save incorrectly predicted games to
