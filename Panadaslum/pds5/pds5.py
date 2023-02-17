import pandas as pd
df=pd.read_csv("student.csv")
print(df)

#droping uneeded coloumns

"""syntax"""
#newdf=olddf.drop(['colname'])
stdent1=df.drop(['name'], axis=1)
#print(stdent1)

"""Q)1.collect name,mark,gender
     2.collect male and mark>80
     3. "      4thh class data
     4. 4th class 5 topers
     5. 3rd class 5 backers
     6.mark b/w 50 to 60
     7.males mark b/w 50 to 60
     8.females max mark 1 student [name],[class],[id]
     """

#Ans
print(df[['name','mark','gender']])                             #1 

print(df.loc[(df['gender']=='male') & (df['mark']>80)])         #2

print(df.loc[df['class']=='Four'])                              #3

df1=df.sort_values(by='mark', ascending=False)           
df2=df1.loc[df1['class']=='Four']            
print(df2.head())                                               #4

df3=df.loc[df['class']=='Three']
df4=df3.sort_values(by='mark')
print(df4.head())                                               #5

print(df.loc[(df['mark']>50)&(df['mark']<60)])                  #6

df5=df.loc[df['gender']=='male']
print(df5.loc[(df5['mark']>50)&(df5['mark']<60)])               #7

df6=df.loc[df['gender']=='female']
df7=df6.sort_values(by='mark', ascending=False)
print(df7[['name', 'class', 'id']].head(1))                     #8



#Delete duplicate rows in a datafr
"""drop_duplicates"""
#Syntax===>df1.drop_duplicates()
df8=df.drop_duplicates()
