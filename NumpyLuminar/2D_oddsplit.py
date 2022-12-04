import numpy as np
#1 to 50 matrics odd numbers 2 d [5*5]

a=np.arange(1,51)
print(a)
b=a%2!=0
c=a[b].reshape([5,5])
print(c)

