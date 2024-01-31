import pandas as pd

def getDates(year):
    if (year == 2003):
        datecols = pd.read_html("https://en.wikipedia.org/wiki/2003_NCAA_Division_I-A_football_rankings")[3]
    elif (year >= 2006):
        datecols = pd.read_html("https://en.wikipedia.org/wiki/" + str(year) + "_NCAA_Division_I_FBS_football_rankings")[2]
    elif (year >= 1978):
        datecols = pd.read_html("https://en.wikipedia.org/wiki/" + str(year) + "_NCAA_Division_I-A_football_rankings")[2]
    elif (year >= 1973):
        datecols = pd.read_html("https://en.wikipedia.org/wiki/" + str(year) + "_NCAA_Division_I_football_rankings")[2]
    elif (year >= 1956):
        datecols = pd.read_html("https://en.wikipedia.org/wiki/" + str(year) + "_NCAA_University_Division_football_rankings")[2]
    elif (year >= 1937):
        datecols = pd.read_html("https://en.wikipedia.org/wiki/" + str(year) + "_NCAA_football_rankings")[2]
    else:
        datecols = pd.read_html("https://en.wikipedia.org/wiki/1936_college_football_rankings")[2]
    list = []
    for col in datecols.columns:
        list.append(col)
    datelist = []
    for i in range(1,len(list)-1):
        datelist.append(list[i])
    return datelist

def url_ListMaker(start,end):
    urlList = []
    for i in range(start,end+1):
        base = "https://collegepollarchive.com/football/ap/seasons.cfm?appollid="
        urlList.append(base + str(i))
    return urlList

data = []
startindex = 1
for i in range(1936,2020):
    dateList = getDates(i)
    d = {"year":i,"numpolls":len(dateList),"startindex":startindex,"endindex":(startindex+len(dateList)-1)}
    startindex = startindex+len(dateList)
    data.append(d)
    data.append({"year":2020,"numpolls":17,"startindex":1169,"endindex":1185})
    data.append({"year":2021,"numpolls":len(dateList),"startindex":1186,"endindex":1201})
    data.append({"year":2022,"numpolls":len(dateList),"startindex":1202,"endindex":1217})
    data.append({"year":2023,"numpolls":len(dateList),"startindex":1218,"endindex":1233})
numpollsdf = pd.DataFrame(data)
numpollsdf

def yearlyRanking(year):
    dateList = getDates(year)
    for i in range(len(numpollsdf)):
        if (numpollsdf.iat[i,0] == year):
            URL_list = url_ListMaker(numpollsdf.iat[i,2],numpollsdf.iat[i,3])
    if len(dateList) == len(URL_list):
        df_list = []
        for i in range(len(dateList)):
            dfl = pd.read_html(URL_list[i])
            df = dfl[0]
            df["Date"] = dateList[i]
            df["Year"] = year
            df_list.append(df)
        totaldf = pd.concat(df_list,ignore_index=True)
        return totaldf
    else:
        print(len(dateList))
        print(len(URL_list))
        return False

df1936 = yearlyRanking(1936)
df1937 = yearlyRanking(1937)
df1938 = yearlyRanking(1938)
df1939 = yearlyRanking(1939)
df1940 = yearlyRanking(1940)
df1941 = yearlyRanking(1941)
df1942 = yearlyRanking(1942)
df1943 = yearlyRanking(1943)
df1944 = yearlyRanking(1944)
df1945 = yearlyRanking(1945)
df1946 = yearlyRanking(1946)
df1947 = yearlyRanking(1947)
df1948 = yearlyRanking(1948)
df1949 = yearlyRanking(1949)
df1950 = yearlyRanking(1950)
df1951 = yearlyRanking(1951)
df1952 = yearlyRanking(1952)
df1953 = yearlyRanking(1953)
df1954 = yearlyRanking(1954)
df1955 = yearlyRanking(1955)
df1956 = yearlyRanking(1956)
df1957 = yearlyRanking(1957)
df1958 = yearlyRanking(1958)
df1959 = yearlyRanking(1959)
df1960 = yearlyRanking(1960)
df1961 = yearlyRanking(1961)
df1962 = yearlyRanking(1962)
df1963 = yearlyRanking(1963)
df1964 = yearlyRanking(1964)
df1965 = yearlyRanking(1965)
df1966 = yearlyRanking(1966)
df1967 = yearlyRanking(1967)
df1968 = yearlyRanking(1968)
df1969 = yearlyRanking(1969)
df1970 = yearlyRanking(1970)
df1971 = yearlyRanking(1971)
df1972 = yearlyRanking(1972)
df1973 = yearlyRanking(1973)
df1974 = yearlyRanking(1974)
df1975 = yearlyRanking(1975)
df1976 = yearlyRanking(1976)
df1977 = yearlyRanking(1977)
df1978 = yearlyRanking(1978)
df1979 = yearlyRanking(1979)
df1980 = yearlyRanking(1980)
df1981 = yearlyRanking(1981)
df1982 = yearlyRanking(1982)
df1983 = yearlyRanking(1983)
df1984 = yearlyRanking(1984)
df1985 = yearlyRanking(1985)
df1986 = yearlyRanking(1986)
df1987 = yearlyRanking(1987)
df1988 = yearlyRanking(1988)
df1989 = yearlyRanking(1989)
df1990 = yearlyRanking(1990)
df1991 = yearlyRanking(1991)
df1992 = yearlyRanking(1992)
df1993 = yearlyRanking(1993)
df1994 = yearlyRanking(1994)
df1995 = yearlyRanking(1995)
df1996 = yearlyRanking(1996)
df1997 = yearlyRanking(1997)
df1998 = yearlyRanking(1998)
df1999 = yearlyRanking(1999)
df2000 = yearlyRanking(2000)
df2001 = yearlyRanking(2001)
df2002 = yearlyRanking(2002)
df2003 = yearlyRanking(2003)
df2004 = yearlyRanking(2004)
df2005 = yearlyRanking(2005)
df2006 = yearlyRanking(2006)
df2007 = yearlyRanking(2007)
df2008 = yearlyRanking(2008)
df2009 = yearlyRanking(2009)
df2010 = yearlyRanking(2010)
df2011 = yearlyRanking(2011)
df2012 = yearlyRanking(2012)
df2013 = yearlyRanking(2013)
df2014 = yearlyRanking(2014)
df2015 = yearlyRanking(2015)
df2016 = yearlyRanking(2016)
df2017 = yearlyRanking(2017)
df2018 = yearlyRanking(2018)
df2019 = yearlyRanking(2019)
df2021 = yearlyRanking(2021)
df2022 = yearlyRanking(2022)
df2023 = yearlyRanking(2023)

df1936.to_csv('1936_CFB_rankings.csv')
df1937.to_csv('1937_CFB_rankings.csv')
df1938.to_csv('1938_CFB_rankings.csv')
df1939.to_csv('1939_CFB_rankings.csv')
df1940.to_csv('1940_CFB_rankings.csv')
df1941.to_csv('1941_CFB_rankings.csv')
df1942.to_csv('1942_CFB_rankings.csv')
df1943.to_csv('1943_CFB_rankings.csv')
df1944.to_csv('1944_CFB_rankings.csv')
df1945.to_csv('1945_CFB_rankings.csv')
df1946.to_csv('1946_CFB_rankings.csv')
df1947.to_csv('1947_CFB_rankings.csv')
df1948.to_csv('1948_CFB_rankings.csv')
df1949.to_csv('1949_CFB_rankings.csv')
df1950.to_csv('1950_CFB_rankings.csv')
df1951.to_csv('1951_CFB_rankings.csv')
df1952.to_csv('1952_CFB_rankings.csv')
df1953.to_csv('1953_CFB_rankings.csv')
df1954.to_csv('1954_CFB_rankings.csv')
df1955.to_csv('1955_CFB_rankings.csv')
df1956.to_csv('1956_CFB_rankings.csv')
df1957.to_csv('1957_CFB_rankings.csv')
df1958.to_csv('1958_CFB_rankings.csv')
df1959.to_csv('1959_CFB_rankings.csv')
df1960.to_csv('1960_CFB_rankings.csv')
df1961.to_csv('1961_CFB_rankings.csv')
df1962.to_csv('1962_CFB_rankings.csv')
df1963.to_csv('1963_CFB_rankings.csv')
df1964.to_csv('1964_CFB_rankings.csv')
df1965.to_csv('1965_CFB_rankings.csv')
df1966.to_csv('1966_CFB_rankings.csv')
df1967.to_csv('1967_CFB_rankings.csv')
df1968.to_csv('1968_CFB_rankings.csv')
df1969.to_csv('1969_CFB_rankings.csv')
df1970.to_csv('1970_CFB_rankings.csv')
df1971.to_csv('1971_CFB_rankings.csv')
df1972.to_csv('1972_CFB_rankings.csv')
df1973.to_csv('1973_CFB_rankings.csv')
df1974.to_csv('1974_CFB_rankings.csv')
df1975.to_csv('1975_CFB_rankings.csv')
df1976.to_csv('1976_CFB_rankings.csv')
df1977.to_csv('1977_CFB_rankings.csv')
df1978.to_csv('1978_CFB_rankings.csv')
df1979.to_csv('1979_CFB_rankings.csv')
df1980.to_csv('1980_CFB_rankings.csv')
df1981.to_csv('1981_CFB_rankings.csv')
df1982.to_csv('1982_CFB_rankings.csv')
df1983.to_csv('1983_CFB_rankings.csv')
df1984.to_csv('1984_CFB_rankings.csv')
df1985.to_csv('1985_CFB_rankings.csv')
df1986.to_csv('1986_CFB_rankings.csv')
df1987.to_csv('1987_CFB_rankings.csv')
df1988.to_csv('1988_CFB_rankings.csv')
df1989.to_csv('1989_CFB_rankings.csv')
df1990.to_csv('1990_CFB_rankings.csv')
df1991.to_csv('1991_CFB_rankings.csv')
df1992.to_csv('1992_CFB_rankings.csv')
df1993.to_csv('1993_CFB_rankings.csv')
df1994.to_csv('1994_CFB_rankings.csv')
df1995.to_csv('1995_CFB_rankings.csv')
df1996.to_csv('1996_CFB_rankings.csv')
df1997.to_csv('1997_CFB_rankings.csv')
df1998.to_csv('1998_CFB_rankings.csv')
df1999.to_csv('1999_CFB_rankings.csv')
df2000.to_csv('2000_CFB_rankings.csv')
df2001.to_csv('2001_CFB_rankings.csv')
df2002.to_csv('2002_CFB_rankings.csv')
df2003.to_csv('2003_CFB_rankings.csv')
df2004.to_csv('2004_CFB_rankings.csv')
df2005.to_csv('2005_CFB_rankings.csv')
df2006.to_csv('2006_CFB_rankings.csv')
df2007.to_csv('2007_CFB_rankings.csv')
df2008.to_csv('2008_CFB_rankings.csv')
df2009.to_csv('2009_CFB_rankings.csv')
df2010.to_csv('2010_CFB_rankings.csv')
df2011.to_csv('2011_CFB_rankings.csv')
df2012.to_csv('2012_CFB_rankings.csv')
df2013.to_csv('2013_CFB_rankings.csv')
df2014.to_csv('2014_CFB_rankings.csv')
df2015.to_csv('2015_CFB_rankings.csv')
df2016.to_csv('2016_CFB_rankings.csv')
df2017.to_csv('2017_CFB_rankings.csv')
df2018.to_csv('2018_CFB_rankings.csv')
df2019.to_csv('2019_CFB_rankings.csv')
df2021.to_csv('2021_CFB_rankings.csv')
df2022.to_csv('2022_CFB_rankings.csv')
df2023.to_csv('2023_CFB_rankings.csv')