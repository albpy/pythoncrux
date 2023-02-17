import numpy as np
import pandas as pd
df=pd.read_csv("Salary_Data.csv")
print(df)
print(df.head(),df.tail())
print("sum of null datas is",df.isna().sum())
x=df.iloc[:,:-1].values #Input
y=df.iloc[:,-1].values

import matplotlib.pyplot as plt
print(plt.__file__)
#plt.use('TkAgg')
plt.scatter(x,y,color='red')
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.title("Exp vs Salary")
#plt.show()

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y, test_size=0.30, random_state=42)
print(x_train)


"""2) Because This is normal regression model We dont need Normalisation"""


"""3) Creating Regression model"""

from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(x_train,y_train)

y_pred=model.predict(x_test)
#print(y_pred)
"""Q) predict Salary for 6.2 years experience"""
print(model.predict([[6.2]]))

#viewing predicted value using pyplt(matplotlib)

plt.scatter(x_train, y_train,color='red')
plt.plot(x_test, y_pred)
#plt.show()

"""Equation of a line is y=mx+c
Displaying slope and c of line""" #complex algo for slope and const
print("Slope is: ", model.coef_, "Const is :", model.intercept_)

#Actual values is in y_test
#Difference betweed actual y_test and predicted y_pred is called error/bias
"""Create dataframe between actual value and predicted values and find error"""
df1=pd.DataFrame({"Actual_value":y_test, "Predicted_value":y_pred})
print(df1)

#Performance measurement of performance of Classification  model

"""#1) Acuracy Score = ( (True+) + (True-) )/ ( (True+) + (True-) +(False+) + (False-) )
    2) Confusion metrics
    3) Recall = (True+) /( (True+) + (False-) )
    4) Precision = (True+) / ( (True+) + (False+) )
    5) F1 Score  = (2*Recall*precesion) / (Recall+Precesion)
    6) Weighted avg
    7) Macro_avg"""

#Performance measurement for Regression model is done via:
"""1) Mean Absolute Error (MAE)
   2) Mean_Absolute_Percentage_Error (MAPE)
   3) Mean Squared Error (MSE)
   4) Root Mean Squered Error (RMSE)
   5) R2 Score"""

#mean_absolure_error
from sklearn.metrics import mean_absolute_error
print("Error is", mean_absolute_error(y_test, y_pred))

#mean_absolute_percentage_error
from sklearn.metrics import mean_absolute_percentage_error
print("Percentage error", mean_absolute_percentage_error(y_test,y_pred))

#mean_squared_error
from sklearn.metrics import mean_squared_error
print("Squared error is", mean_squared_error(y_test, y_pred))

#Root Mean Square error
z=mean_squared_error(y_test,y_pred)
print(np.sqrt(z))

#R2 Square
from sklearn.metrics import r2_score
print("R2_score is", r2_score(y_test,y_pred))


"""Best Model has mean absolute percentage has lower value and R2 core higher value"""

