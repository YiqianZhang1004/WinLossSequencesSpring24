import pandas as pd
cfb = pd.read_csv("combined_cfb_poll_data.csv")
cbb = pd.read_csv("combined_cbb_poll_data.csv")
cfb2 = cfb[["Date","Rank","Team (FPV)","TeamID","Points"]]
cbb2 = cbb[["Date","Rank","Team (FPV)","TeamID","Points"]]
cfb2.to_csv("cfb_polls_trim.csv")
cbb2.to_csv("cbb_polls_trim.csv")