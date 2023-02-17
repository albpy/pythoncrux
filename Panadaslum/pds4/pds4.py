
#Collecting columns from dataframe
import pandas as pd
df=pd.read_csv("elect-card-trnsc-nov-2022.csv")

"""Q) Collect columns period and Series_title_4 along with first 50 rows"""

print(df[['Period','Series_title_4']].head(50))


"""Q) Collect columns period and Series_title_4 of last 25 rows"""

print(df[['Period', 'Series_title_4']].iloc[-25:])


#loc ====> collect data of a particular condition(similar to filter)

"""Syntax """
#newdfname=olddfname.loc[olddfname['colname']condition] [[coloumns]]


print(df)

newdf=df.loc[df['Data_value']>30000] [['Period','Suppressed']]
print(newdf)

"""satisfy 2 condition"""
#newdf=olddf.loc[(olddf['colname']condition1)&(olddfname['colname1']condition2]

"""Data_value>30000 & UNITS=Dollars"""
newdfaa=df.loc[(df['Data_value']>30000)&(df['UNITS']=='Dollars')]
print(newdfaa)
   
"""Sort"""
#ascending order
#sort_values
"""syntax"""
#newdf=olddf.sort_values(by='colname')

"""Ex"""
df11=df.sort_values(by='Data_value')
print(df11)

#descending

df111=df.sort_values(by='Data_value', ascending=False) 
print(df111)

"""Q) collect max Data_value card and min datavalued card"""

#max Data_value
print(df111[['Period','Data_value']].head(1))
#min Data_value
print(df11[['Period','Data_value']].head(1))
print(df111[['Period','Data_value']].tail(1))

