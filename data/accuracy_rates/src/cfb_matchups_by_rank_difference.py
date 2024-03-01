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
    print(grouped1)
    wins1list = grouped1["wins"].to_list()
    games1list = grouped1["games"].to_list()
    data1rows=[]
    for i in range(5):
        wins1rows = wins1list[2*i] + wins1list[2*i+1]
        games1rows = games1list[2*i] + games1list[2*i+1]
        winPct1rows = wins1rows / games1rows
        data1rows.append({"rankDiff":"".join(str([2*i+1,2*i+2])),"winsHome":wins1rows,"gamesHome":games1rows,"winPctHome":winPct1rows})
        df1_2rows = pd.DataFrame(data1rows)
    
    #if away team is ranked i and home team is ranked j
    dictList2 = []
    for i in range (highRankLower,highRankUpper + 1):
        data_i = data[data.awayRank == i]
        for j in range(lowRankLower,lowRankUpper + 1):
            data_ij = data_i[data_i.homeRank == j]
            if (j > i):
                rankDiff = j-i
                games = len(data_ij)
                wins = len(data_ij[data_ij.result == 0])
            else:
                continue
            dictList2.append({"rankDiff":rankDiff,"wins":wins,"games":games})
    df2 = pd.DataFrame(dictList2)
    grouped2 = df2.groupby("rankDiff").agg("sum").reset_index()
    print(grouped2)
    wins2list = grouped2["wins"].to_list()
    games2list = grouped2["games"].to_list()
    data2rows=[]
    for i in range(5):
        wins2rows = wins2list[2*i] + wins2list[2*i+1]
        games2rows = games2list[2*i] + games2list[2*i+1]
        winPct2rows = wins2rows / games2rows
        data2rows.append({"rankDiff":"".join(str([2*i+1,2*i+2])),"winsAway":wins2rows,"gamesAway":games2rows,"winPctAway":winPct2rows})
    df2_2rows = pd.DataFrame(data2rows)

    #df1_2rows.to_csv("data/accuracy_rates/processed_data/by_rank_difference_home" + str(highRankLower) + "-" + str(highRankUpper) + ".csv")
    #df2_2rows.to_csv("data/accuracy_rates/processed_data/by_rank_difference_away" + str(highRankLower) + "-" + str(highRankUpper) + ".csv")
    print(df1_2rows)
    print(df2_2rows)
    df = pd.merge(df1_2rows,df2_2rows,on="rankDiff")
    df.to_csv("data/accuracy_rates/processed_data/by_rank_difference_combined" + str(hrl) + "-" + str(hru) + ".csv")

matchups_by_rank_difference(1,5,1,25)
matchups_by_rank_difference(6,10,1,25)
matchups_by_rank_difference(11,15,1,25)
matchups_by_rank_difference(1,10,1,25)
matchups_by_rank_difference(11,20,1,25)
matchups_by_rank_difference(15,20,1,25)

#graphics:
# top ten teams vs teams ranked x teams below them, 1 < x < 10
# 11-20 teams vs teams ranked x teams below them, 1 < x <10
# top 5 teams vs teams ranked x teams below them, 1 < x < 10
# 6-10 teams vs teams ranked x  teams below them, 1 < x < 10
# 11-15 teams vs teams ranked x teams below them, 1 < x < 10
# 15-20 teams vs teams ranked x teams below them, 1 < x < 10