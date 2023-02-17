import numpy as np
#Addition
a=np.array([[2,3,4],[6,4,3],[3,5,2]])
b=np.array([[2,6,4],[5,4,2],[3,7,5]])
c=np.add(a,b)
print(c)
#Adding subtracting  different order matrix is not possible


#Subtraction
#-----------
d=np.subtract(a,b)
print(d)

#multiply matrixes -: Here pure multiplication is conducted  not dot product
#-----------------
e=np.multiply(a,b)
print(e)

#division-----------
f=np.divide(a,b)
print(f)

#=======square====
f=np.square(a)
print(f)

#------sqareroot------
g=np.sqrt(a)
print(g)

#-------------Trignometric(sin, cos, tan) functions-----------
print(np.sin(a))
print(np.cos(a))
print(np.tan(a))



"""DOT PRODUCT"""
#1D dot
#------

ab=np.array([4,5,6,7])
bc=np.array([3,2,5,3])
ac=np.dot(ab,bc)
print(ac)

#2D dot
-------
cd=np.array([[1,3,5],[2,4,6],[9,8,7]])
de=np.array([[2,1,3],[3,5,4],[5,2,7]])
print(cd)
print(de)
ce=np.dot(cd,de)
print(ce)
"""Rows of matrix should be same for dot and columns might be different
sorry columns of first matrix equals rows of second matrix
eg: 4x3*5x3 is not but 4x3 * 3x4 is possible"""
