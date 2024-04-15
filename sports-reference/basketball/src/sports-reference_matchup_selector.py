from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd
driver = webdriver.Chrome(options= Options())

data = []
for i in range(1,26):
    homeRank = i
    for j in range(1,26):
        print(str(i)+"-----------------------------------------"+str(j))
        if i == j:
            continue
        awayRank = j
        driver.get("https://www.sports-reference.com/cbb/play-index/matchup_finder.cgi?request=1&year_min=1950&year_max=2024&comp_school=eq&rank_school="+str(i)+"&comp_opp=eq&rank_opp="+str(j)+"&game_location=H&game_type=A&order_by=date_game")
        time.sleep(0.5)
        try:
            table_container = driver.find_element(By.ID, "div_stats")
            table = table_container.find_element(By.ID, "stats")
            rows = table.find_elements(By.CSS_SELECTOR,"tr")
            print(len(rows))
            
            for k in range(1,len(rows)):
                year = rows[k].find_element(By.CSS_SELECTOR,"th")
                row = rows[k].find_elements(By.CSS_SELECTOR,"td")
                if (row[7].text == "W"):
                    result = 1
                elif (row[7].text == "L"):
                    result = 0
                else:
                    result = 0.5
                print(len(row))
                d = {"Year":year.text,"Date":row[0].text,"Home":row[2].text,"HomeRank":row[3].text,"Away":row[5].text,"AwayRank":row[6].text,"Result":result,"HomePTS":row[9].text,"AwayPTS":row[10].text,"MOV":row[11].text}
                data.append(d)
        except:
            continue
df = pd.DataFrame(data)
df.to_csv("sports-reference/basketball/raw_data/matchup_selector.csv")