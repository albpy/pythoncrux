from sklearn.model_selection import train_test_split
from smart_devices_EDA import Data_
# print(Data_.head()) 

X = Data_.drop("activityID", axis=1)
obj_df = Data_.select_dtypes(include=['object']).copy() # get object datatypes from data
obj_df.isna().sum() # Get no of total null values
obj_df.value_counts() # Get total no of various values
"""Its easy since the much of data is already preprocessed. it doesnt contain any null values""" 
# print(y.unique()) #to get unique values

from sklearn.preprocessing import OrdinalEncoder

ord_enc = OrdinalEncoder()
new_encoded_column = 'New'
old_column_name = 'activityID'

def ordinal_encode_of(column, new_encoded_column, old_column_name):
    column[new_encoded_column] = ord_enc.fit_transform(column[[old_column_name]])
    return obj_df

categorical_values = ordinal_encode_of(obj_df, new_encoded_column, old_column_name)
y, y_name = categorical_values['New'], categorical_values['activityID']

#Get values and their categories
activity_value_pair = categorical_values.value_counts().sort_values()

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8)
X_train, X_valid, y_train, y_valid = train_test_split(X_train, y_train, train_size=0.9)