import pandas as pd
import numpy as np

df_no_header=pd.read_csv("elect-card-trnsc-nov-2022.csv", header=None)
print(df_no_header)
df=pd.read_csv("elect-card-trnsc-nov-2022.csv")
print(df)


#total number of missing value
print(df.isna().sum) 

#Filling all Missing value in individual columns
"""using fillna()"""

df1=df.fillna('india')
print(df1)
print(df1.isna().sum)

df2=df.iloc[1]
print(df2)
#Print 1 to 4 rows of dataset
df3=df.iloc[1:5]
print(df3)

