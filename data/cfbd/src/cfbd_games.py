import json
import csv

def check_valid(game):
    # checks if game is a regular season game and doesn't have missing essential values
    if game["season_type"] != "regular":
        return False
    if game["id"] is None:
        return False
    if game["start_date"] is None:
        return False
    if game["season"] is None:
        return False
    if game["home_team"] is None:
        return False
    if game["home_id"] is None:
        return False
    if game["away_team"] is None:
        return False
    if game["away_id"] is None:
        return False
    if game["home_points"] is None:
        return False
    if game["away_points"] is None:
        return False
    
    return True

def search_line_by_id(id, season):
    # no line data for seasons prior to 2013
    if (season < 2013):
        return None
    
    with open ("data/cfbd/raw_data/cfbd_lines_" + str(season) + ".json", "r") as file:
        lines_data = json.load(file)
    
    for games in lines_data:
        if int(games["id"]) == id:
            return games
    
    return None



def get_average_lines(lines_list):
    average_data = ["NaN","NaN","NaN","NaN","NaN","NaN"]
    if lines_list is None or len(lines_list) == 0:
        return average_data
    
    # multiple sources used for betting line data
    # finding average data 
    # some stats are missing for some sources
    # so have to manually count the total and number of non-missing data
    total_spread = 0
    num_spread = 0
    total_spread_open = 0
    num_spread_open = 0
    total_over_under = 0
    num_over_under = 0
    total_over_under_open = 0
    num_over_under_open = 0
    total_home_money_line = 0
    num_home_money_line = 0
    total_away_money_line = 0
    num_away_money_line = 0

    for line in lines_list:
        if line["spread"] is not None:
            total_spread += float(line["spread"])
            num_spread+=1
        if line["spreadOpen"] is not None:
            total_spread_open += float(line["spreadOpen"])
            num_spread_open+=1
        if line["overUnder"] is not None:
            total_over_under += float(line["overUnder"])
            num_over_under+=1
        if line["overUnderOpen"] is not None:
            total_over_under_open += float(line["overUnderOpen"])
            num_over_under_open+=1
        if line["homeMoneyline"] is not None:
            total_home_money_line += float(line["homeMoneyline"])
            num_home_money_line+=1
        if line["awayMoneyline"] is not None:
            total_away_money_line += float(line["awayMoneyline"])
            num_away_money_line+=1
    if num_spread != 0:
        average_data[0] = round(total_spread/num_spread,3)
    if num_spread_open!=0:
        average_data[1] = round(total_spread_open/num_spread_open,3)
    if num_over_under!=0:
        average_data[2] = round(total_over_under/num_over_under,3)
    if num_over_under_open!=0:
        average_data[3] = round(total_over_under_open/num_over_under_open,3)
    if num_home_money_line!=0:
        average_data[4] = round(total_home_money_line/num_home_money_line,3)
    if num_away_money_line!=0:
        average_data[5] = round(total_away_money_line/num_away_money_line,3)

    return average_data



seasons = [2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
final_data = [["date", "season", "team1", "team1ID", "team2", "team2ID", "score1", "score2","result", "spread", "spreadOpen", "overUnder", "overUnderOpen","homeMoneyLine","awayMoneyLine"]]

for season in seasons:
    with open("data/cfbd/raw_data/cfbd_" + str(season) + ".json", 'r') as file:
        raw_data = json.load(file)

    for game in raw_data:
        # checks if each game is valid (doesn't have missing values and is a regular season game) by searching up its unique id
        if check_valid(game):
            id = int(game["id"])
            date = game["start_date"].split("T")[0]
            game_season = int(game["season"])
            team1 = game["home_team"].lower()
            team1ID = int(game["home_id"])
            team2 = game["away_team"].lower()
            team2ID = int(game["away_id"])
            score1 = int(game["home_points"])
            score2 = int(game["away_points"])

            # determing who won
            result = 0
            if score1 > score2:
                result = 1
            elif score1 == score2:
                result = 0.5


            betting_data = ["NaN","NaN","NaN","NaN","NaN","NaN"]
            # search each game by id to find the lines data
            lines_data = search_line_by_id(id, season)
            if lines_data is not None:
                lines_list = lines_data["lines"]
                
                # there are multiple sources used to find line data, so this averages them
                betting_data = get_average_lines(lines_list)


            game_data = [date, game_season, team1, team1ID, team2, team2ID, score1, score2, result]
            for bet in betting_data:
                game_data.append(bet)
            final_data.append(game_data)



with open("data/cfbd/processed_data/cfbd_all_seasons.csv", 'w', newline='') as file:
    csv_writer = csv.writer(file)

    csv_writer.writerows(final_data)
