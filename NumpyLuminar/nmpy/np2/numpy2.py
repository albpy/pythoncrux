#Zero matrix
"""all elements in the matrix is zero
[0 0 0]
[0 0 0]
[0 0 0]"""
#How to create zero matrix

import numpy as np
a=np.zeros([3,4])
print(a)
print(a.dtype)

b=np.zeros([3,4], dtype=int)
print(b)
print(b.dtype)

c=np.zeros([5,5], dtype=int)
print(c)
print(c.dtype)

"""Q) create a zero matrix in 1D"""
z1=np.zeros([3,], dtype=int)
print(z1)
print(z1.dtype)
print(z1.size)
print(z1.ndim)

"""Q) create a 3 D zero matrix of 5*4 int type"""
z3D=np.zeros([1,5,4], dtype=int)
print(z3D)
print(z3D.ndim)

z3D1=np.zeros([2,5,4], dtype=int)
print(z3D1.ndim)
print(z3D1.size)
print(z3D1.shape)


#UNITY MATRIX
"""all elements in the matrix is 1"""
one=np.ones([3,4], dtype=int)
print(one)
one1_D=np.ones([4,], dtype=int)
print(one1_D)
one3_D=np.ones([3,3,4], dtype=int)
print(one3_D.ndim)
print(one3_D.shape)
print(one3_D.size)
print(one3_D)
