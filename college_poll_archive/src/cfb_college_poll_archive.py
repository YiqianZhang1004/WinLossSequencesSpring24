from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(options= Options())
df = pd.DataFrame()

for i in range(1,1234):
    url = "https://collegepollarchive.com/football/ap/seasons.cfm?appollid=" + str(i)
    driver.get(url)
    time.sleep(1)
    date = driver.find_element(By.CSS_SELECTOR, "h2").text.split(" A")[0]
    table = driver.find_elements(By.CSS_SELECTOR, "table")
    time.sleep(1)
    print(len(table))
    rows = table[0].find_elements(By.CSS_SELECTOR, "tr")
    print(len(rows))
    data = []
    for i in range(1,min(len(rows)-1,26)):
        print("[" + str(i) + "]")
        row1 = rows[i].find_elements(By.CSS_SELECTOR, "td")
        print(row1[0].text)
        print(row1[1].text)
        print(row1[2].text)
        print(row1[3].text)
        print(row1[4].text)
        print(row1[5].text)
        print(row1[6].text)
        print(row1[7].text)
        linkstring = row1[3].find_element(By.TAG_NAME, "a").get_attribute("href")
        d = {"Date":date,"Rank":row1[0].text,"Team (FPV)":row1[3].text,"TeamID":linkstring.split("=")[2],"Conference":row1[4].text,"Record":row1[5].text,"Points":row1[6].text,"Last Week":row1[7].text}
        data.append(d)
    dftemp = pd.DataFrame(data)
    print(dftemp)
    df = pd.concat([df,dftemp])

df.to_csv("combined_cfb_poll_data.csv")