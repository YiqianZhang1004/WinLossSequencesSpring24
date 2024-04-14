from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd
edge_options = Options()
edge_options.add_argument('--headless')
driver = webdriver.Edge(options= edge_options)

data = []
# 1872-2024
for i in range(1980,2024):
    print(i)
    driver.get("https://www.sports-reference.com/cfb/years/"+str(i)+"-schedule.html")
    time.sleep(0.5)
    print("here")
    try:
        table_container = driver.find_element(By.ID, "div_schedule")
        table = table_container.find_element(By.ID, "schedule")
        rows = table.find_elements(By.CSS_SELECTOR,"tr") #730
        # get list of rows, but for rows[i], if no tds, then skip it
        print("about to look at rows")
        for k in range(1,len(rows)):
            row = rows[k].find_elements(By.CSS_SELECTOR,"td")
            if len(row) == 0:
                continue
            if (i>=2013):
                d = {"date":row[1].text,"winner":row[4].text,"location":row[6].text,"loser":row[7].text}
            else:
                d = {"date":row[1].text,"winner":row[3].text,"location":row[5].text,"loser":row[6].text}
            data.append(d)
    except:
        print("except")
        continue
df = pd.DataFrame(data)
df.to_csv("sports-reference/raw_data/cfb_seasons.csv")