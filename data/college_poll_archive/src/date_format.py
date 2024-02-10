from datetime import datetime
import pandas as pd

cbb = pd.read_csv("cbb_polls_trim.csv")

def formatDatesCBB(date_string):
    if "Preseason" in date_string:
        return date_string
    elif "Final" in date_string:
        return date_string
    date_object = datetime.strptime(date_string, "%d-%b-%y")
    return date_object.strftime("%Y-%m-%d")

cbb["Date"] = cbb["Date"].apply(formatDatesCBB)

cfb = pd.read_csv("cfb_polls_trim.csv")

def formatDatesCFB(date_string):
    if "Preseason" in date_string:
        return date_string
    elif "Final" in date_string:
        return date_string
    date_object = datetime.strptime(date_string, "%B %d, %Y")
    return date_object.strftime("%Y-%m-%d")

cfb["Date"] = cfb["Date"].apply(formatDatesCFB)

cbb.to_csv("cbb_polls_trim.csv")
cfb.to_csv("cfb_polls_trim.csv")