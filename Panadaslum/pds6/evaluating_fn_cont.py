#Evaluating fn cont

#max
#---
#                                       col to    col to 
#Group and find max                     group     find max
#syntax==>(newdfname=olddfname.groupby('colname')['colname'].max())
import pandas as pd
df=pd.read_csv('student.csv')
print(df)
"""Q) find each classes max marks from student.csv"""

newdf=df.groupby('class')['mark'].max()
print(newdf)


#min()
#-----
"""Q) find min mark of tach class"""
newmin=df.groupby('class')['mark'].min()
print(newmin)

#Total and Mean
#--------------
#SUM
newsum=df.groupby('class')['mark'].sum()
print(newsum)

newmean=df.groupby('class')['mark'].mean()
print(newmean)

