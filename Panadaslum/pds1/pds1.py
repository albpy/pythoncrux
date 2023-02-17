#Pandas
#Used for data manipulation
#Data Analysis
#Data cleaning===>Handling missing value

"""Data structure are list
                      set
                      tuples
                      dictionary"""

#3 Data structures in python

#1. Series ==>1D data

#2. Data_frame==>@ D Data

#3.Label==>3D Data

import numpy as np
import pandas as pd
a=pd.Series([4,5,6,7])
print(a)
print(a.shape, a.size, a.dtypes)

ser=pd.Series([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])
#print(ser)
#or
sr=np.arange(1,31)
srr=pd.Series(sr)
print(srr)

"""ndimensional array is the class of np array:"""
#print first five rows usin head function
print(srr.head())
print(srr.head(1))

#print last rows of data
print(srr.tail())

"""Append 2 series"""
s1=pd.Series([5,6,7,8,9])
s2=pd.Series([4,2,6,7,3])
s3=s1.append(s2, ignore_index=True)
print(s3)
s4=s1.subtract(s2)
print(s4)
s5=s1.multiply(s2)
print(s5)
s6=s1.div(s2)
print(s6)
print(s6.dtype)
