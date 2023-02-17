#dictionary

#id, fname, lname, age,salary

import pandas as pd
import numpy as np

dic={'id':101,'fname':'vinay','lname':'k','age':26,'salary':1000}
s1=pd.Series(dic,['age', 'lname','fname','id','salary','age'])
print(s1)

"""DATA FRAME"""    #Nested list
data=[
        [1,'sara','joseph',24,'license',40000],
        [2,'komal','kurian',23,'voter id',50000],
        [3,'kajal','nara', 30, 'stockid',60000],
        [4,'kanan','kulam',28,'companyid',35000],
        [5,'jeevan','joseph',45,'Idcard',200000],
        [6,'jana','mara', 335, 'lic card',300000]]
df=pd.DataFrame(data)
df.columns=['id','fname','lname','age','prof','salary']


print(df,df.shape, df.size, df.columns)

#Nested dictionay

nesteddict=[{'id':1001, 'name': 'soman',   'age':29 , 'loc': 'chennai' ,      'dept':'mechanical'},
            {'id':1002, 'name': 'jhon',    'age':50 , 'loc': 'maharastra',    'dept':'data science'},
            {'id':1003, 'name': 'saritha', 'age':51 , 'loc': 'uttar-pradesh', 'dept':'Embeded'},
            {'id':1004, 'name': 'keerthi', 'age':43 , 'loc': 'surat',         'dept':'Api Development'},
            {'id':1005, 'name': 'tamana',  'age':68 , 'loc': 'panjab',        'dept':'Father'}
            ]
df1=pd.DataFrame(nesteddict)
print(df1)
#Describe function
print(df1.dtypes)

"""string in pandas is called as object"""
print(df1.describe())
print(df1.describe(include='O'))
df1['Power']=['200hp','30hp','100hp','500hp','60hp']
print(df1)
df1=df.rename(columns={'lname':'last_name'})
print(df1)
