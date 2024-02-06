import pandas as pd
cfb = pd.read_csv("combined_cfb_poll_data.csv")
cbb = pd.read_csv("combined_cbb_poll_data.csv")
cfb_trim = cfb[["Date","Rank","Team (FPV)","TeamID","Points"]]
cbb_trim = cbb[["Date","Rank","Team (FPV)","TeamID","Points"]]
cfb_trim.to_csv("cfb_polls_trim.csv")
cbb_trim.to_csv("cbb_polls_trim.csv")