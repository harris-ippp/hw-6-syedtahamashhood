import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
#create a list with all the years whin our dfs
dataframes=[]

for line in open("ELECTION_ID"):
    new=line.strip().split() #create a new variable which is a list consisting of two elements, namely the election id and the year
    year = new[1] +".csv"

    header = pd.read_csv(year, nrows = 1).dropna(axis = 1)
    d = header.iloc[0].to_dict()

    df = pd.read_csv(year, index_col = 0, thousands = ",", skiprows = [1])
    df.rename(inplace = True, columns = d) # rename to democrat/republican
    df.dropna(inplace = True, axis = 1)    # drop empty columns
    df["Year"] = new[1]
    dataframes.append(df[["Democratic", "Republican", "Total Votes Cast", "Year"]])


allyears=pd.concat(dataframes)


#include new column with Republican Share by dividing the columns Republican with total votes cast
allyears["Republican Share"]=allyears["Republican"].div(allyears["Total Votes Cast"])
accomack = allyears.loc['Accomack County'].sort_values(by = 'Year', ascending = True)#sort by values and look for where the value is accomack county
print(allyears)
#print(list(allyears.index))
print(accomack)

accomack.plot(kind ="line", x ="Year", y="Republican Share").get_figure().savefig('q3accomack.png')
