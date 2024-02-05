from selenium import webdriver  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import csv

options = Options()
# must be kept false
options.headless = False

# column indices
DATE_INDEX = 0
LOCATION_INDEX = 2
TEAM_INDEX = 3
SCORE_INDEX = 8
OPEN_INDEX = 9
CLOSE_INDEX = 10
MONEYLINE_INDEX = 11
HALF_INDEX = 12

def check_valid(row1, row2):
    # checks if the two rows have the same date
    if (row1[DATE_INDEX].text != row2[DATE_INDEX].text):
        return False
    # checks if the game is not at neutral grounds
    if row1[LOCATION_INDEX].text == row2[LOCATION_INDEX].text:
        return False
    return True

# gets processed date
def determine_date(season, date):
    year = str(season)
    if len(str(date)) == 3:
        month = "0" + date[0]
        day = date[1:3]
        if int(date[0]) <= 5:
            year = str(season+1)
    else:
        month = date[0:2]
        day = date[2:4]
    
    return year + "-" + month + "-" + day

# determines winner based on score
def determine_winner(score1, score2):
    if score1>score2:
        return 1
    elif score1==score2:
        return 0.5
    else:
        return 0
    
# home and away team is based on location
def get_team_and_score(team1, team2, score1, score2, moneyline1, moneyline2, location):
    if location == "H":
        return [team1, team2, score1, score2, moneyline1, moneyline2]
    return [team2, team1, score2, score1, moneyline2, moneyline1]

# returns proper representation of data
# betting data is non essential data so can use try except blocks
def get_betting_data(field):
    try:
        return float(field)
    except:
        if field == "pk":
            return 0.0
        return "NaN"

# determines which data is which based on moneyline comparison and column comparison
def classify_data(open1, open2, close1, close2, half1, half2, moneyline1, moneyline2):
    list1 = [open1, close1, half1, open2, close2, half2]
    list2 = [open2, close2, half2, open1, close1, half1]
    nullList = ["NaN", "NaN", "NaN", "NaN", "NaN", "NaN"]
    if moneyline1 != "NaN" and moneyline2 != "NaN":
        if moneyline2 > moneyline1:
            return list1
        return list2
    elif open1 != "NaN" and open2 != "NaN":
        if open1 < open2:
            return list1
        return list2
    elif close1 != "NaN" and close2 != "NaN":
        if close1 < close2:
            return list1
        return list2
    elif half1 != "NaN" and half2 != "NaN":
        if half1 < half2:
            return list1
        return list2
    return nullList

# returns the data of an error row
def get_error_data(row1, row2):
    error =[]
    error.append(row1[DATE_INDEX].text)
    error.append(row1[LOCATION_INDEX].text == "N")
    error.append(season)
    error.append(row1[TEAM_INDEX].text)
    error.append(row2[TEAM_INDEX].text)
    error.append(row1[SCORE_INDEX].text)
    error.append(row2[SCORE_INDEX].text)
    error.append(row1[OPEN_INDEX].text)
    error.append(row2[OPEN_INDEX].text)
    error.append(row1[CLOSE_INDEX].text)
    error.append(row2[CLOSE_INDEX].text)
    error.append(row1[HALF_INDEX].text)
    error.append(row2[HALF_INDEX].text)
    error.append(row1[MONEYLINE_INDEX].text)
    error.append(row2[MONEYLINE_INDEX].text)

    return error


driver = webdriver.Chrome(options = options)

final_data = [["date", "season", "homeTeam","awayTeam","homeScore","awayScore", "result","spreadOpen", "spreadClose","spreadH2", "overUnderOpen","overUnderClose", "overUnderH2", "homeMoneyline", "awayMoneyline"]]
error_data = [["date", "neutral", "season", "team1", "team2", "score1", "score2", "open1","close1", "open2","close2", "oneH2", "twoH2", "moneyline1","moneyline2"]]

seasons = []
for i in range(2013, 2014):
    seasons.append(i)

for season in seasons:     
    driver.get("https://www.sportsbookreviewsonline.com/scoresoddsarchives/ncaa-football-" + str(season) + "-" + str(season+1)[2:4] + "/") 
    driver.implicitly_wait(5)

    table = driver.find_element(By.CSS_SELECTOR, "table")
    rows = table.find_elements(By.CSS_SELECTOR, "tr")

    # loops through two rows at a time
    for i in range(1,len(rows),2):
        
        row1 = rows[i].find_elements(By.CSS_SELECTOR, "td")
        row2 = rows[i+1].find_elements(By.CSS_SELECTOR, "td")

        # checking to make sure the game is valid
        if check_valid(row1, row2):
            try:
                processed_date = determine_date(season, row1[DATE_INDEX].text)

                team1 = str(row1[TEAM_INDEX].text).lower()
                team2 = str(row2[TEAM_INDEX].text).lower()

                score1 = int(row1[SCORE_INDEX].text)
                score2 = int(row2[SCORE_INDEX].text)

                moneyline1 = get_betting_data(row1[MONEYLINE_INDEX].text)
                moneyline2 = get_betting_data(row2[MONEYLINE_INDEX].text)

                home_team, away_team, home_score, away_score, home_moneyline, away_moneyline = get_team_and_score(team1, team2, score1, score2, moneyline1, moneyline2, str(row1[LOCATION_INDEX].text))
                
                result = determine_winner(home_score, away_score)

                open1 = get_betting_data(row1[OPEN_INDEX].text)
                open2 = get_betting_data(row2[OPEN_INDEX].text)
                close1 = get_betting_data(row1[CLOSE_INDEX].text)
                close2 = get_betting_data(row2[CLOSE_INDEX].text)
                half1 = get_betting_data(row1[HALF_INDEX].text)
                half2 = get_betting_data(row2[HALF_INDEX].text)
              
                spreadOpen, spreadClose, spreadHalf, overUnderOpen, overUnderClose, overUnderHalf = classify_data(open1, open2, close1, close2, half1, half2, moneyline1, moneyline2)

                game_data = [processed_date, season, home_team, away_team, 
                             home_score, away_score, result, 
                             spreadOpen, spreadClose, spreadHalf, 
                             overUnderOpen, overUnderClose, overUnderHalf, 
                             home_moneyline, away_moneyline]
                
                final_data.append(game_data)

            except:
                # adding row to error file if encounter exception
                error_data.append(get_error_data(row1, row2))
        else:
            # adding row to error file if game is invalid
            error_data.append(get_error_data(row1, row2))


with open("data/sportsbookreviewsonline/ncaaf/processsed_data/sbro_ncaaf.csv", 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(final_data)

with open("data/sportsbookreviewsonline/ncaaf/processsed_data/sbro_ncaaf_error.csv", 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(error_data)
