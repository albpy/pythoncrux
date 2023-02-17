"""Full Matrics"""
#In full matric all elements should be same

import numpy as np
a=np.full([4,5],3)
print(a)

b=np.full([4,4],5, dtype=float)
print(b)

c=np.full([4],6)
print(c)

d=np.full([2,4,5],4)
print(d)

#Identity matrix==>Diagonal elements is 1 and remaining is 0
"""Using eye function"""
e=np.eye(4, dtype=int)
print(e)
"""Using Identity function"""
f=np.identity(5, dtype=int)
print(f)

#COMPLEX MATRIX
#--------------
"""Complex numbers are (a+iv),(u+iv),(x+iy)"""
#in a+ij==>3+i6
#a=Real part-->3
#b=Imaginary part-->6

g=np.ones([3,3],dtype=complex)
print(g)

h=[[[1+2i],[3+5i],[2+4i]],[[4+9i],[2+4i],[2+5i]],[[3+2i],[4+5i],[3+2i]]]
print(h)
