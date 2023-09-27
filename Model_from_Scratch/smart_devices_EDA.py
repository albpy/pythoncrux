import pandas as pd
Data_ = pd.read_csv("Physical_activity_prediction_Dataset\Physical_activity_prediction_Dataset.csv")
pd.set_option('display.max_columns', None)
pd.set_option('display.precision', 2)

# Our Data has 
"""print(f'rows: {len(Data_.axes[0])} '+ f'cols: {len(Data_.axes[1])}')"""

# Null values of each column
"""print("Null vales per column: \n", Data_.isna().sum())"""

# Maximum and minimum values of each column
"""print(Data_.agg(['min', 'max']))"""

# show some random rows
"""print(Data_.sample())"""

#Get the datatype information and memory usage
"""print(Data_.info())"""

#Statistics 
"""print(Data_.describe())"""


#Get unique vales of PeopleId
"""print(Data_["PeopleId"].value_counts())"""

# value_percent
"""print(Data_["heart_rate"].value_counts() / (len(Data_)) * 100)"""

import matplotlib.pyplot as plt
#Visulize the intense workers(heart rate)
"""Data_["heart_rate"].value_counts().head(15).plot(kind = "bar")
plt.show()"""

#plot hist to check balance
"""Data_.hist(figsize=(15, 10), bins =20)
plt.tight_layout()"""
"""plt.show()"""

#Check no of unique values in datset
def col_unique_val_check(df):
    for i,col in enumerate(df.columns):
        print(f"{col:40} ----> {df[col].nunique():10} unique values with dtype {str(df[col].dtype):10} at index {i}")  

# col_unique_val_check(Data_)
import seaborn as sns

def heat_map(df):
    plt.figure(figsize=(20,12))
    Data_1 = Data_.drop("activityID", axis=1)
    sns.heatmap(Data_.corr(),cmap='cividis',annot=True)
    plt.tight_layout()
    plt.show()
target = 'activationID'
def count_plt(df):
    plt.figure(figsize=(18,4))
    sns.countplot(x=target, data=df, palette='tab10')
    plt.tight_layout()

def kernel_density_estimate(df):
    plt.figure(figsize=(20,18))
    j=1
    for i,columns in enumerate(['heart_rate','hand temperature (°C)','ankle temperature (°C)','chest temperature (°C)']):
        plt.subplot(2,2,j)
        sns.kdeplot(x=columns,data=df,palette='deep',hue=target)
        j+=1
    plt.tight_layout()
    plt.show()

# We dont want PeopleId for prediction

Data_.drop('PeopleId', axis = 1, inplace=True)

