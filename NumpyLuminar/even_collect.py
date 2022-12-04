import numpy as np
a=np.array([41,34,56,46,38,47,52,57,49,65,34,39])
print(a)

#even_collect

b=(a%2==0)
print(b)
c=a[b]
print(c)
