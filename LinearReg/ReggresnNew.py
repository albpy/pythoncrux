import numpy as np
import pandas as pd
df=pd.read_csv("SOCR-HeightWeight.csv")
df.pop("Index")
print("Pured data is : ",df)
"""Print sum of null charecters"""
print("Totel missing value : ", df.isna().sum())
x=df.iloc[:,0]
print(x)
y=df.iloc[:,1]
print(y)

import matplotlib.pyplot as plt
plt.scatter(x,y, color='brown')
plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("Height vs Weight")
#plt.show()


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y, test_size=0.30, random_state=42)
print("X_train is :",x_train)

#NO NORMELISATION

from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(x_train,y_train)

y_pred=model.predict(x_test)

print(y_pred)
