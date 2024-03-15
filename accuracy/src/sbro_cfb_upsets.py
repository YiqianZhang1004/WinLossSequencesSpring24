import pandas as pd
df = pd.read_csv("data/sportsbookreviewsonline/ncaaf/processsed_data/sbro_ncaaf_close_only_with_ranks.csv")
#df = pd.read_csv("data/cfbd/processed_data/cfbd_close_only.csv")
#df = pd.read_csv("data/combined_football/processed/combined.csv")

homewin = df[df.result == 1]
awaywin = df[df.result == 0]

homeupsetsm = homewin[homewin.homeMoneyline > 0]
awayupsetsm = awaywin[awaywin.awayMoneyline > 0]
upsetsm = pd.concat([homeupsetsm,awayupsetsm])
upsetsm = upsetsm[(upsetsm.homeTeamRank > 0) & (upsetsm.awayTeamRank > 0)]
upsetsm.to_csv("data/accuracy_rates/processed_data/sbro_cfb_upsetsm.csv")

homeupsetsr = homewin[homewin.homeTeamRank > homewin.awayTeamRank]
awayupsetsr = awaywin[awaywin.awayTeamRank > awaywin.homeTeamRank]
upsetsr = pd.concat([homeupsetsr,awayupsetsr])
upsetsr.to_csv("data/accuracy_rates/processed_data/sbro_cfb_upsetsr.csv")

homeupsets = homeupsetsr[homeupsetsr.homeMoneyline > 0]
awayupsets = awayupsetsr[awayupsetsr.awayMoneyline > 0]
upsets = pd.concat([homeupsets,awayupsets])
upsets.to_csv("data/accuracy_rates/processed_data/sbro_cfb_upsets.csv")