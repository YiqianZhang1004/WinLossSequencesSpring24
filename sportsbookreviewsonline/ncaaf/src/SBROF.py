from selenium import webdriver  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import csv
import time

options = Options()
options.headless = False

DATE_INDEX = 0
LOCATION_INDEX = 2
TEAM_INDEX = 3
SCORE_INDEX = 8
OPEN_INDEX = 9
CLOSE_INDEX = 10
MONEYLINE_INDEX = 11
HALF_INDEX = 12


def processDate(rawDate):
    if len(rawDate) == 3:
        month = "0" + rawDate[0]
        date = rawDate[1:]
        return "-" + month + "-" + date
    else:
        month = rawDate[:2]
        date = rawDate[2:]
        return "-" + month + "-" + date
    
def floatData(field):
    try:
        return round(float(field), 3)
    except:
        if field == "pk":
            return 0.0
        return "NaN"
    
def organizeData(m1, m2, open1, open2, close1, close2, half1, half2, location1, team1, team2, score1, score2):
    if m1 == "NaN" or m2 == "NaN":
        if location1 == "V":
            return [team2, team1, score2, score1, "NaN", "NaN", "NaN", "NaN", "NaN", "NaN", "NaN", "NaN"]
        return [team1, team2, score1, score2, "NaN", "NaN", "NaN", "NaN", "NaN", "NaN", "NaN", "NaN"]
    if m1 > 0 and m2 < 0:
        if location1 == "V":
            return [team2, team1, score2, score1, m2, m1, open2, close2, half2, open1, close1, half1]
        return [team1, team2, score1, score2, m1, m2, open2, close2, half2, open1, close1, half1]
    if m1 < 0 and m2 > 0:
        if location1 == "V":
            return [team2, team1, score2, score1, m2, m1, open1, close1, half1, open2, close2, half2]
        return [team1, team2, score1, score2, m1, m2, open1, close1, half1, open2, close2, half2]
    if abs(m1) > abs(m2):
        if location1 == "V":
            return [team2, team1, score2, score1, abs(m2), -abs(m1), open1, close1, half1, open2, close2, half2]
        return [team1, team2, score1, score2, -abs(m1), abs(m2), open1, close1, half1, open2, close2, half2]
    if abs(m1) < abs(m2):
        if location1 == "V":
            return [team2, team1, score2, score1, -abs(m2), abs(m1), open2, close2, half2, open1, close1, half1]
        return [team1, team2, score1, score2, abs(m1), -abs(m2), open2, close2, half2, open1, close1, half1]
    else:
        if location1 == "V":
            return [team2, team1, score2, score1, "NaN", "NaN", "NaN", "NaN", "NaN", "NaN", "NaN", "NaN"]
        return [team1, team2, score1, score2, "NaN", "NaN", "NaN", "NaN", "NaN", "NaN", "NaN", "NaN"]




driver = webdriver.Chrome(options = options)

finalData = [["date", "season", "regular", "homeTeam","awayTeam","homeScore","awayScore", "result","openingSpread", "closingSpread","halfSpread", "openingOverUnder","closingOverUnder", "halfOverUnder", "homeMoneyline", "awayMoneyline"]]
errorData = [["date", "season", "regular", "team1", "team2", "score1", "score2", "open1", "close1", "open2","close2", "half1", "half2", "moneyline1","moneyline2"]]
neutralData = [["date", "season", "regular", "homeTeam","awayTeam","homeScore","awayScore", "result","openingSpread", "closingSpread","halfSpread", "openingOverUnder","closingOverUnder", "halfOverUnder", "homeMoneyline", "awayMoneyline"]]

seasons = []
for i in range(2007, 2023):
    seasons.append(i)

for season in seasons:     
    driver.get("https://www.sportsbookreviewsonline.com/scoresoddsarchives/ncaa-football-" + str(season) + "-" + str(season+1)[2:4] + "/") 
    time.sleep(3)
    
    table = driver.find_element(By.CSS_SELECTOR, "table")
    rows = table.find_elements(By.CSS_SELECTOR, "tr")

    for i in range(1, len(rows), 2):
        try:
            row1 = rows[i].find_elements(By.CSS_SELECTOR, "td")
            row2 = rows[i+1].find_elements(By.CSS_SELECTOR, "td")

            rawDate = row1[DATE_INDEX].text
            processedDate = str(season) + processDate(rawDate)

            team1 = row1[TEAM_INDEX].text
            team2 = row2[TEAM_INDEX].text

            score1 = int(row1[SCORE_INDEX].text)
            score2 = int(row2[SCORE_INDEX].text)

            regular = row1[LOCATION_INDEX].text != "N"

            open1 = floatData(row1[OPEN_INDEX].text)
            open2 = floatData(row2[OPEN_INDEX].text)

            close1 = floatData(row1[CLOSE_INDEX].text)
            close2 = floatData(row2[CLOSE_INDEX].text)

            moneyline1 = floatData(row1[MONEYLINE_INDEX].text)
            moneyline2 = floatData(row2[MONEYLINE_INDEX].text)

            half1 = floatData(row1[HALF_INDEX].text)
            half2 = floatData(row2[HALF_INDEX].text)

            (homeTeam, awayTeam,
             homeScore, awayScore,
             homeMoneyline, awayMoneyline,
             spreadOpen, spreadClose, spreadHalf,
             overUnderOpen, overUnderClose, overUnderHalf) = organizeData(moneyline1, moneyline2, open1, open2, close1, close2, half1, half2, row1[LOCATION_INDEX].text, team1, team2, score1, score2)
                

            result = 0
            if homeScore > awayScore:
                result = 1
            
            gameData = [processedDate, season, regular, homeTeam, awayTeam, homeScore, awayScore, result, spreadOpen, spreadClose, spreadHalf, overUnderOpen, overUnderClose, overUnderHalf, homeMoneyline, awayMoneyline]

            if regular:
                finalData.append(gameData)
            else:
                neutralData.append(gameData)

        except:
            error = [row1[DATE_INDEX].text, season, row1[LOCATION_INDEX].text != "N",
             row1[TEAM_INDEX].text, row2[TEAM_INDEX].text, row1[SCORE_INDEX].text, row2[SCORE_INDEX].text,
             row1[OPEN_INDEX].text, row2[OPEN_INDEX].text, row1[CLOSE_INDEX].text, row2[CLOSE_INDEX].text,
             row1[HALF_INDEX].text, row2[HALF_INDEX].text, row1[MONEYLINE_INDEX].text, row2[MONEYLINE_INDEX].text,]
            errorData.append(error)

with open("sportsbookreviewsonline/ncaaf/processsed_data/sbro.csv", 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(finalData)

with open("sportsbookreviewsonline/ncaaf/processsed_data/sbroMissing.csv", 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(errorData)

with open("sportsbookreviewsonline/ncaaf/processsed_data/sbroNeutral.csv", 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(neutralData)










