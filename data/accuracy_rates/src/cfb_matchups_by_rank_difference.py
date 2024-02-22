import pandas as pd
data = pd.read_csv("data/cfbd/processed_data/cfbd_close_only.csv")

highRankLower = 1
highRankUpper = 5
lowRankLower = 1
lowRankUpper = 25

def matchups_by_rank_difference(hrl,hru,lwl,lru):    
    highRankLower = hrl
    highRankUpper = hru
    lowRankLower = lwl
    lowRankUpper = lru
    #if home team is ranked i and away team is ranked j
    dictList1 = []
    for i in range (highRankLower,highRankUpper + 1):
        data_i = data[data.homeRank == i]
        for j in range(lowRankLower,lowRankUpper + 1):
            data_ij = data_i[data_i.awayRank == j]
            if (j > i):
                rankDiff = j-i
                games = len(data_ij)
                wins = len(data_ij[data_ij.result == 1])
            else:
                continue
            dictList1.append({"rankDiff":rankDiff,"wins":wins,"games":games})
    df1 = pd.DataFrame(dictList1)
    grouped1 = df1.groupby("rankDiff").agg("sum").reset_index()
    grouped1["winPct"] = grouped1["wins"] / grouped1["games"]

    #if away team is ranked i and home team is ranked j
    dictList2 = []
    for i in range (highRankLower,highRankUpper + 1):
        data_i = data[data.homeRank == i]
        for j in range(lowRankLower,lowRankUpper + 1):
            data_ij = data_i[data_i.awayRank == j]
            if (j > i):
                rankDiff = j-i
                games = len(data_ij)
                wins = len(data_ij[data_ij.result == 0])
            else:
                continue
            dictList2.append({"rankDiff":rankDiff,"wins":wins,"games":games})
    df2 = pd.DataFrame(dictList2)
    grouped2 = df2.groupby("rankDiff").agg("sum").reset_index()
    grouped2["winPct"] = grouped2["wins"] / grouped2["games"]

    grouped1.to_csv("data/accuracy_rates/processed_data/by_rank_difference_home" + str(highRankLower) + "-" + str(highRankUpper) + ".csv")
    grouped2.to_csv("data/accuracy_rates/processed_data/by_rank_difference_away" + str(highRankLower) + "-" + str(highRankUpper) + ".csv")

matchups_by_rank_difference(1,5,1,25)
matchups_by_rank_difference(6,10,1,25)
matchups_by_rank_difference(15,20,1,25)
matchups_by_rank_difference(20,25,1,25)