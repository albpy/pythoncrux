import numpy as np 
a=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
for i in a:
    for j in i:
        for k in j:
            print(k)
#Join
mat1=np.array([1,2,3,4,5])
mat2=np.array([6,7,8,9,10])
#Using CONCANTENATE function
mat=np.concatenate((mat1,mat2))
print(mat)
#Concatenate join based on row
D2_1=np.array([[1,2,3],[4,5,6],[7,8,9]])
D2_2=np.array([[11,12,13],[14,15,16,],[17,18,19]])
D2_3=np.concatenate((D2_1,D2_2))
print(D2_3)
D2_4=np.concatenate((D2_1,D2_2),axis=1)
print(D2_4)

#Split functionality
SP1D=np.array([1,2,3,4,5,6,7,8,9,10])
Splitted=np.array_split(SP1D,3)
print(Splitted)

#Search Using (where function)
srch=np.where(SP1D==4)
print(srch)

srch2D=np.where(D2_2>15)
print(srch2D)

#Filter
fil=np.array([1,2,3,4,5,6,7,8,9])
filtered=fil>6
fila=fil[filtered]
print(fila)


