#Evaluating Function


"""1.count
   2.max
   3.min
   4.sum
   5.mean"""


import pandas as pd

#Count==>total count of a particular column's data

df=pd.read_csv('student.csv')

print(df)


#Syntax==>1.first perform group operation, and then count
    #newdf=olddf.groupby('coloumn') ['coloumn'].count

df1=df.groupby('mark') ['mark'].count()
print(df1)

"""Q) calculate each class count"""
df2=df.groupby('class') ['class'].count()
print(df2.sort_values(ascending=False)) #Descending order
print(df2.sort_values())                #Ascending order


