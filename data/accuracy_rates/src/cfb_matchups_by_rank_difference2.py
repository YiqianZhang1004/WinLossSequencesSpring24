import pandas as pd
data = pd.read_csv("data/cfbd/processed_data/cfbd_close_only.csv")


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
            dictList1.append({"rankDiff":rankDiff,"homeWins":wins,"homeGames":games})
    df1 = pd.DataFrame(dictList1)
    grouped1 = df1.groupby("rankDiff").agg("sum").reset_index()
    print(grouped1)

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
            dictList2.append({"rankDiff":rankDiff,"awayWins":wins,"awayGames":games})
    df2 = pd.DataFrame(dictList2)
    grouped2 = df2.groupby("rankDiff").agg("sum").reset_index()
    print(grouped2)

    #combine home and away
    combined = pd.merge(grouped1, grouped2, on="rankDiff")
    combined["combinedWins"] = combined["homeWins"] + combined["awayWins"]
    combined["combinedGames"] = combined["homeGames"] + combined["awayGames"]
    combined["combinedWinPct"] = combined["combinedWins"] / combined["combinedGames"]
    print(combined)
    combined.to_csv("data/accuracy_rates/processed_data/by_rank_difference_combined11-25(2).csv")

matchups_by_rank_difference(11,25,1,25)