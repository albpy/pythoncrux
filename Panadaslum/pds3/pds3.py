import pandas as pd
import numpy as np

data=[
        [1,'sara','joseph',24,'lover',40000],
        [2,'komal','kurian',23,'engineer',50000],
        [3,'kajal','nara', 30, 'lover',60000],
        [4,'kanan','kulam',28,'lover',35000],
        [5,'jeevan','joseph',45,'engineer',200000],
        [6,'jana','mara', 35, 'engineer',300000]]

df=pd.DataFrame(data)
df.columns=['id','fname','lname','age','prof','salary']

print(df.describe)
print(df.describe(include='O'))
print(df.describe(include='all'))
df['Gender']=['M','f','m','f','m']
print(df)

