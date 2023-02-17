from sklearn.cluster import KMeans

import pandas as pd 
import numpy as np
df = pd.read_csv("/home/tc/Pythoncrux/Bigdata/KMEANS/Parkbrimingam/dataset.csv", sep=",")
print(df.isna().sum()) #0
x=df.iloc[:,[1,2]]
print(x)

wcss=[]
for i in range(1,11):
	data=KMeans(n_clusters=i, init='k-means++', random_state=42)
	data.fit(x)
	wcss.append(data.inertia_)
print(wcss)
