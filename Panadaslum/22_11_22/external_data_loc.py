#newdframe=olddframe.loc[olddfname['colname']condition]

import pandas as pd
df=pd.read_csv('/home/tc/Pythoncrux/filestoimport/sample4.txt', sep=",",header=None, names=["fname","lname","age","phno","loc"])
print(df)
df1=df.loc[df['age']>23]
print(df1)

#collect fname, lname,age, phno of people works at chennai
df2=df.loc[df['loc']=='Chennai'] [['fname','lname','age','phno']]
print(df2)


# 2 conditions--> age above 23 and work chennai
"""df3=df.loc[(['age']>23)&(df['loc']=='Chennai')]"""
