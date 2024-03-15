from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(options= Options())
df = pd.DataFrame()

for i in range(1,1273):
    url = "https://collegepollarchive.com/mbasketball/ap/seasons.cfm?appollid=" + str(i)
    driver.get(url)
    time.sleep(1)
    date = driver.find_element(By.CSS_SELECTOR, "h2").text.split(" A")[0]
    table = driver.find_elements(By.CSS_SELECTOR, "table")
    time.sleep(1)
    print(len(table))
    rows = table[8].find_elements(By.CSS_SELECTOR, "tr")
    print(len(rows))
    data = []
    for i in range(1,min(len(rows)-1,26)):
        print("[" + str(i) + "]")
        row1 = rows[i].find_elements(By.CSS_SELECTOR, "td")
        print(row1[2].text)
        linkstring = row1[2].find_element(By.TAG_NAME, "a").get_attribute("href")
        d = {"Date":date,"Rank":row1[0].text,"Team (FPV)":row1[2].text,"TeamID":linkstring.split("=")[2],"Conference":row1[3].text,"Record":row1[4].text,"Points":row1[5].text}
        data.append(d)
    dftemp = pd.DataFrame(data)
    print(dftemp)
    df = pd.concat([df,dftemp])

df.to_csv("combined_cfb_poll_data.csv")