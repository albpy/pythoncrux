import numpy as np
arr=np.array([4,3,2,1,5])
print(arr, type(arr))

#Dimension ==> is the number of axis
"""--------------------------------"""
#1 D ====> 1 axis (x)
#2 D ====> 2 axis (x, y)
#3 D ===>  3 axis (z, x, y) -->Always write x axis first
#
#order of matrix is nxm(rows x colomn)

"""we can print dimension(number of axis)  of matrix by using ndim"""
#                                            ----
print(arr.ndim)
"""order"""
#----------
#[4,3,2,1,5] ======>Machine read it as:
#                                   [4]
#                                   [3]
#                                   [2]
#                                   [1]
#                                   [5]
"""we can print order of matrix  by shape"""
print(arr.shape)

#TOTAl number of elements in matrix is multiplication rows and colomns


"""Q) create a 1 D matrix having total elements/shape 8"""

arr1=np.array([2,3,4,5,6,7,8,9])
print(arr1.ndim)
print(arr1.shape)

"""Q) Create a 2 D matrix"""
arr2_D=np.array([[1,3,5,7,9],[2,4,6,8,0]])
print(arr2_D)
print(arr2_D.ndim)
print(arr2_D.shape)
"""Q) Create 3x4 matrix in 2D using numpy"""
arr2_D1=np.array([[2,3,4,5],[5,4,3,2],[9,9,8,7]])
print(arr2_D1)
print(arr2_D1.ndim)
print(arr2_D1.shape)
"""Q) Create a 2 D matrix of order 5*4"""
arr2_D3=np.array([[1,2,3,4],[7,6,5,4],[4,8,7,5],[3,2,1,6],[2,7,6,4]])
print(arr2_D3)
print(arr2_D3.ndim)
print(arr2_D3.shape)

"""Q) Create a 3 D matrix of order (1,3,3)"""
arr3_D=np.array([[[1,2,3],[42,3,5],[4,98,8]]])
print(arr3_D)
print(arr3_D.ndim)
print(arr3_D.shape)

"""Q) create 3_D matrix of order (1,3,4)"""
arr3_D1=np.array([[[1,2,3,4],[2,45,2,3],[23,45,67,5]]])
print(arr3_D1)
print(arr3_D1.ndim)
print(arr3_D1.shape)

"""Create a 1 D matrix, and print datatype of matrix using dtype and change the data type to float"""
mat_1D=np.array([1,4,6,3,7], dtype=float)
print(mat_1D)
print(mat_1D.dtype)
"""Q) Dra a 3*3 float matrix"""
mat_2D=np.array([[1,4,6],[2,65,4],[23,24,25]], dtype=float)
print(mat_2D)
print(mat_2D.ndim)
print(mat_2D.shape)

#size function is used to print total number of elements in matrix
print(mat_2D.size)

